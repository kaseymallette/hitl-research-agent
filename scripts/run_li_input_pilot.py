#!/usr/bin/env python
"""Li input-format pilot: the same analysis task, supplied two ways.

Path A (`--path pdf`) sends the original PDF. Path B (`--path crops`) sends the
existing prepared text plus the eight retained crops. Model, reasoning effort,
analysis instructions, output schema, validation rules, one-correction policy,
and the grounding reference are the same in both paths; only the input format
and its format-specific instructions differ.

    uv run python scripts/run_li_input_pilot.py dry-run --path pdf
    uv run python scripts/run_li_input_pilot.py run --path pdf --confirm-paid

`dry-run` builds the request payload and prints a projection. It makes no API
request, so it cannot show that the model accepts this payload — only a live
call establishes that.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import struct
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from hitl_research_agent.config import Settings  # noqa: E402
from hitl_research_agent.extraction import (  # noqa: E402
    AnalysisResult,
    InputMode,
    LoadedAttachment,
    PreparationGap,
    SourceAnalysisError,
    SourceDocument,
    analyze_source,
    find_annotations,
    grounding_view,
    load_attachment,
)
from hitl_research_agent.extraction.prompts import (  # noqa: E402
    INPUT_MODE_INSTRUCTIONS,
    SYSTEM_PROMPT,
    build_messages,
)
from hitl_research_agent.models.provenance import Provenance  # noqa: E402

SLUG = "li_et_al_2025_making_ai_less_thirsty"
PREPARATION_DIR = f"outputs/preparation/{SLUG}"
SOURCE_PDF = f"data/research/{SLUG}.pdf"
PILOT_ROOT = REPO_ROOT / "outputs/v1_archive/li_input_format_pilot"

PILOT_MODEL = "gpt-6.1-sol"
PILOT_REASONING_EFFORT = "medium"
# Sent as max_output_tokens, so each call's output is bounded server-side.
PILOT_MAX_OUTPUT_TOKENS = 24_000
# No retries inside the OpenAI client for this pilot, so the one-correction
# policy is the only thing that can produce a second billable request and every
# request appears in an attempt record. Ordinary runs keep the client default.
PILOT_MAX_RETRIES = 0
# Documented rates per 1M tokens, read from OpenAI's model pages on 2026-10-15.
RATES_BY_MODEL = {
    "gpt-6.1-sol": {"input": 2.0, "output": 10.0, "cached_input": 0.10},
    "gpt-6-astra": {"input": 10.0, "output": 50.0, "cached_input": 1.00},
}
RATES_USD_PER_MTOK = RATES_BY_MODEL[PILOT_MODEL]
RATE_SOURCE = "https://developers.openai.com/api/docs/models/<model> (read 2026-10-15)"
DEFAULT_CAP_USD = 2.00

PATHS: dict[str, InputMode] = {"pdf": "pdf", "crops": "prepared_text_and_crops"}

# Estimation constants, used only for the pre-call projection and the cap check.
CHARS_PER_TOKEN = 3.0  # from observed Phase 3 usage: 36,626 chars -> 13,056 input tokens
SYSTEM_PROMPT_TOKENS = 1_600
IMAGE_PATCH_MULTIPLIER = 1.2  # documented for every patch-based model listed; not for 6.1-sol
IMAGE_PATCH_CAP = 2_500
ASSUMED_PAGE_IMAGE_TOKENS = 1_400  # the API's page-render resolution is not documented


def _apply_overrides(args: argparse.Namespace) -> None:
    """Apply the CLI's model/effort/output-cap/output-root choices.

    These are module-level so the record builders and the spending guard all
    see the same configuration without threading it through every signature.
    """
    global PILOT_MODEL, PILOT_REASONING_EFFORT, PILOT_MAX_OUTPUT_TOKENS
    global RATES_USD_PER_MTOK, RATE_SOURCE, PILOT_ROOT
    PILOT_MODEL = args.model
    PILOT_REASONING_EFFORT = args.effort
    PILOT_MAX_OUTPUT_TOKENS = args.max_output_tokens
    if PILOT_MODEL not in RATES_BY_MODEL:
        raise SystemExit(f"no documented rates recorded for {PILOT_MODEL}; refusing to estimate")
    RATES_USD_PER_MTOK = RATES_BY_MODEL[PILOT_MODEL]
    RATE_SOURCE = f"https://developers.openai.com/api/docs/models/{PILOT_MODEL} (read 2026-10-15)"
    if args.out_root:  # None leaves PILOT_ROOT as set (tests point it at a tmp tree)
        PILOT_ROOT = REPO_ROOT / "outputs/pilots" / args.out_root


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_commit() -> str | None:
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.strip() or None


def png_size(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:33]
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def image_tokens(path: Path) -> int:
    width, height = png_size(path)
    patches = math.ceil(width / 32) * math.ceil(height / 32)
    return math.ceil(min(patches, IMAGE_PATCH_CAP) * IMAGE_PATCH_MULTIPLIER)


def load_prep_record() -> dict[str, Any]:
    record: dict[str, Any] = json.loads(
        (REPO_ROOT / PREPARATION_DIR / "prep_record.json").read_text()
    )
    return record


def load_source() -> tuple[SourceDocument, dict[str, Any]]:
    """The prepared text and provenance, used in both paths.

    In the crops path this text is the model's input. In the PDF path it is the
    grounding reference only and is never sent to the model.
    """
    prep_dir = REPO_ROOT / PREPARATION_DIR
    prep_record = load_prep_record()
    text = (prep_dir / "prepared_text.md").read_text()
    provenance = Provenance.model_validate_json((prep_dir / "provenance.json").read_text())
    gaps = [
        PreparationGap(
            id=item["id"],
            kind=item["kind"],
            page=item["page"],
            label=item.get("label"),
            image=item.get("image"),
        )
        for item in prep_record["annotations"]
    ]
    source = SourceDocument(
        text=text,
        provenance=provenance,
        preparation_directory=PREPARATION_DIR,
        preparation_gaps=gaps,
    )
    return source, prep_record


def load_raw_source() -> tuple[SourceDocument, dict[str, Any]]:
    """The PDF's raw extracted text as the grounding reference, nothing else.

    No cleanup, no reading-order correction, no annotations. This text is never
    sent to the model in the pdf input mode; it exists only so a quotation can
    be checked against something.
    """
    import pymupdf

    prep_record = load_prep_record()
    with pymupdf.open(REPO_ROOT / SOURCE_PDF) as doc:
        raw = "\n".join(page.get_text() for page in doc)
    provenance = Provenance.model_validate_json(
        (REPO_ROOT / PREPARATION_DIR / "provenance.json").read_text()
    )
    return SourceDocument(text=raw, provenance=provenance), prep_record


def build_attachments(path: str, source: SourceDocument) -> list[LoadedAttachment]:
    if path == "pdf":
        return [load_attachment(REPO_ROOT, SOURCE_PDF, kind="pdf")]
    attachments = []
    for gap in source.preparation_gaps:
        if not gap.image:
            raise ValueError(f"preparation gap {gap.id} has no retained image")
        attachments.append(
            load_attachment(
                REPO_ROOT,
                f"{PREPARATION_DIR}/{gap.image}",
                kind="image",
                page=gap.page,
                gap_id=gap.id,
                label=gap.label,
            )
        )
    return attachments


def grounding_basis(source: SourceDocument, reference: str) -> dict[str, Any]:
    view = grounding_view(source.text)
    if reference == "raw":
        description = (
            "The PDF's raw extracted text layer (pymupdf get_text(), page order, no "
            "cleanup, no reading-order correction, no annotations), normalized for "
            "whitespace and case as the existing check already does. The model never "
            "sees this text; it exists only so a quotation can be checked. Where the "
            "raw layer renders a passage differently from the printed page, a correct "
            "quotation will be flagged -- that is a limitation of the check, not an "
            "analytical error."
        )
    else:
        description = (
            "The prepared text of this source, with each preparation annotation replaced "
            "by the grounding sentinel."
        )
    return {
        "reference": reference,
        "description": description,
        "source_text_sha256": sha256_text(source.text),
        "source_text_characters": len(source.text),
        "grounding_view_sha256": sha256_text(view),
        "annotations_excluded": len(find_annotations(source.text)),
    }


def project_usage(path: str, source: SourceDocument) -> dict[str, Any]:
    """A pre-call projection, for the cap check and for the record.

    Every figure here is an estimate with its assumption named. None of it is
    measured usage.
    """
    if path == "pdf":
        import pymupdf

        with pymupdf.open(REPO_ROOT / SOURCE_PDF) as doc:
            pages = doc.page_count
            text_chars = sum(len(page.get_text()) for page in doc)
        text_tokens = int(text_chars / CHARS_PER_TOKEN) + SYSTEM_PROMPT_TOKENS
        attachment_tokens = pages * ASSUMED_PAGE_IMAGE_TOKENS
        assumptions = [
            f"text layer {text_chars} chars at ~{CHARS_PER_TOKEN} chars/token",
            f"{pages} page images at an assumed {ASSUMED_PAGE_IMAGE_TOKENS} tokens each; "
            "the API's page-render resolution is not documented, so this term is the "
            "weakest number here",
        ]
    else:
        text_tokens = int(len(source.text) / CHARS_PER_TOKEN) + SYSTEM_PROMPT_TOKENS
        crops = [REPO_ROOT / PREPARATION_DIR / str(gap.image) for gap in source.preparation_gaps]
        attachment_tokens = sum(image_tokens(crop) for crop in crops)
        assumptions = [
            f"prepared text {len(source.text)} chars at ~{CHARS_PER_TOKEN} chars/token",
            f"{len(crops)} crops measured from their pixel dimensions at high detail, "
            f"assuming the {IMAGE_PATCH_MULTIPLIER} patch multiplier documented for other "
            "patch-based models but not for gpt-6.1-sol",
        ]
    projected_input = text_tokens + attachment_tokens
    # Worst case under the existing policy: two attempts, the second resending the
    # whole first request plus the first response, each call capped server-side.
    worst_input = projected_input * 2 + PILOT_MAX_OUTPUT_TOKENS
    worst_output = PILOT_MAX_OUTPUT_TOKENS * 2
    worst_cost = (
        worst_input * RATES_USD_PER_MTOK["input"] + worst_output * RATES_USD_PER_MTOK["output"]
    ) / 1_000_000
    return {
        "projected_input_tokens": projected_input,
        "projected_input_text_tokens": text_tokens,
        "projected_input_attachment_tokens": attachment_tokens,
        "assumptions": assumptions,
        "worst_case_input_tokens": worst_input,
        "worst_case_output_tokens": worst_output,
        "worst_case_calculated_cost_usd": round(worst_cost, 4),
        "worst_case_basis": (
            "two attempts (the one-correction policy), the second resending the first "
            "request and response, with every call bounded by max_output_tokens="
            f"{PILOT_MAX_OUTPUT_TOKENS}"
        ),
    }


def calculated_cost(input_tokens: int, output_tokens: int, cached_input: int = 0) -> dict[str, Any]:
    uncached = max(input_tokens - cached_input, 0)
    total = (
        uncached * RATES_USD_PER_MTOK["input"]
        + cached_input * RATES_USD_PER_MTOK["cached_input"]
        + output_tokens * RATES_USD_PER_MTOK["output"]
    ) / 1_000_000
    return {
        "rates_usd_per_mtok": RATES_USD_PER_MTOK,
        "rate_source": RATE_SOURCE,
        "uncached_input_tokens": uncached,
        "cached_input_tokens": cached_input,
        "output_tokens": output_tokens,
        "total_usd": round(total, 4),
        "note": (
            "Calculated from reported usage at documented rates. This is not confirmed "
            "billing; confirmed_billing is filled in from the API usage dashboard."
        ),
    }


def recorded_runs() -> list[tuple[Path, dict[str, Any]]]:
    """Every invocation this pilot has recorded, successful or not."""
    runs = []
    for record in sorted(PILOT_ROOT.glob("*/runs/*/run_record.json")):
        runs.append((record, json.loads(record.read_text())))
    return runs


def spent_so_far() -> tuple[float, list[str]]:
    """Calculated cost already recorded, and reasons not to spend more.

    Failed and partial invocations count exactly like successful ones: what
    matters is whether a request was made, not whether it produced an analysis.
    An invocation whose usage could not be read is never counted as zero — it
    becomes a blocker instead, because a request that may have been charged
    cannot be reconciled against this guard.
    """
    total = 0.0
    blockers: list[str] = []
    for path, data in recorded_runs():
        where = path.relative_to(PILOT_ROOT)
        cost = (data.get("calculated_cost") or {}).get("total_usd")
        if isinstance(cost, int | float):
            total += float(cost)
        accounting = data.get("usage_accounting") or {}
        if accounting.get("usage_complete") is not True:
            blockers.append(
                f"{where}: usage could not be read for "
                f"{accounting.get('attempts_missing_usage') or 'an unknown attempt'}, so its "
                "cost is unknown rather than zero"
            )
        if not isinstance(cost, int | float):
            blockers.append(f"{where}: no calculated cost recorded")
    return total, blockers


def over_cap(already: float, worst: float, cap: float) -> bool:
    return already + worst > cap


def invocation_dir(path: str) -> Path:
    """A fresh directory per invocation, so no earlier record is overwritten."""
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    directory = PILOT_ROOT / path / "runs" / stamp
    suffix = 1
    while directory.exists():
        suffix += 1
        directory = PILOT_ROOT / path / "runs" / f"{stamp}-{suffix}"
    directory.mkdir(parents=True)
    return directory


def out_dir(path: str) -> Path:
    directory = PILOT_ROOT / path
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def payload_inventory(messages: list[Any]) -> list[dict[str, Any]]:
    inventory: list[dict[str, Any]] = []
    for message in messages:
        content = message.content
        if isinstance(content, str):
            inventory.append({"role": message.type, "block": "text", "characters": len(content)})
            continue
        for block in content:
            entry: dict[str, Any] = {"role": message.type, "block": block["type"]}
            if block["type"] == "text":
                entry["characters"] = len(block["text"])
                entry["preview"] = block["text"][:120]
            else:
                entry["mime_type"] = block.get("mime_type")
                entry["base64_characters"] = len(block.get("base64", ""))
            inventory.append(entry)
    return inventory


def base_record(
    path: str, source: SourceDocument, prep_record: dict[str, Any], reference: str
) -> dict[str, Any]:
    instructions = INPUT_MODE_INSTRUCTIONS[PATHS[path]] or ""
    return {
        "pilot": "li_input_format",
        "path": path,
        "input_mode": PATHS[path],
        "git_commit": git_commit(),
        "model": PILOT_MODEL,
        "reasoning_effort": PILOT_REASONING_EFFORT,
        "max_output_tokens": PILOT_MAX_OUTPUT_TOKENS,
        "openai_client_max_retries": PILOT_MAX_RETRIES,
        "request_accounting": (
            "Client retries are disabled for this pilot, so each analysis attempt is one "
            "HTTP request and every request it makes has an attempt record. At most two "
            "requests per invocation, from the one-correction policy."
        ),
        "system_prompt_sha256": sha256_text(SYSTEM_PROMPT),
        "input_instructions_sha256": sha256_text(instructions),
        "input_instructions": instructions,
        "source": {
            "slug": SLUG,
            "pdf": SOURCE_PDF,
            "pdf_sha256": sha256_file(REPO_ROOT / SOURCE_PDF),
            "preparation_directory": PREPARATION_DIR,
            "prepared_text_characters": len(source.text),
            "prep_record_sha256": sha256_file(REPO_ROOT / PREPARATION_DIR / "prep_record.json"),
            "preparation_gaps": [gap.model_dump(mode="json") for gap in source.preparation_gaps],
        },
        "grounding_reference": grounding_basis(source, reference),
        "preparation_effort": {
            "measured_extraction": prep_record.get("timing"),
            "note": (
                "Only parser wall time is measured. Tooling, manual image checking, and "
                "review time for this preparation were not measured and are not guessed "
                "here; the comparison has to account for them separately."
            ),
        },
        "preparation_limits": prep_record.get("preparation_limits"),
    }


def cmd_dry_run(args: argparse.Namespace) -> int:
    _apply_overrides(args)
    source, prep_record = load_raw_source() if args.grounding == "raw" else load_source()
    attachments = build_attachments(args.path, source)
    messages = build_messages(source, input_mode=PATHS[args.path], attachments=attachments)
    projection = project_usage(args.path, source)
    record = base_record(args.path, source, prep_record, args.grounding)
    record.update(
        {
            "kind": "dry_run",
            "performed_at": datetime.now(UTC).isoformat(),
            "api_requests_made": 0,
            "model_inputs": [item.record.model_dump(mode="json") for item in attachments],
            "payload_inventory": payload_inventory(messages),
            "projection": projection,
            "caveat": (
                "A dry run builds the payload locally. It does not establish that the "
                "model or the API accepts this payload, that structured output works "
                "with these attachments, or what the real usage will be."
            ),
        }
    )
    destination = out_dir(args.path) / "dry_run_record.json"
    destination.write_text(json.dumps(record, indent=2) + "\n")

    print(f"path={args.path}  input_mode={PATHS[args.path]}  (no API request made)")
    for entry in record["payload_inventory"]:
        detail = (
            f"{entry.get('characters')} chars"
            if entry["block"] == "text"
            else f"{entry.get('mime_type')} {entry.get('base64_characters')} base64 chars"
        )
        print(f"  {entry['role']:6s} {entry['block']:12s} {detail}")
    print(
        f"  projected input ~{projection['projected_input_tokens']} tokens "
        f"(text ~{projection['projected_input_text_tokens']}, "
        f"attachments ~{projection['projected_input_attachment_tokens']})"
    )
    print(f"  worst-case calculated cost ${projection['worst_case_calculated_cost_usd']}")
    print(f"  written: {destination.relative_to(REPO_ROOT)}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    _apply_overrides(args)
    if not args.confirm_paid:
        print("Refusing to run: a paid call needs --confirm-paid.", file=sys.stderr)
        return 2
    already, blockers = spent_so_far()
    if blockers:
        print(
            "Refusing to run: an earlier invocation of this pilot may have been charged "
            "an amount this guard cannot account for:",
            file=sys.stderr,
        )
        for blocker in blockers:
            print(f"  - {blocker}", file=sys.stderr)
        print(
            "Reconcile those requests against the usage dashboard before spending more.",
            file=sys.stderr,
        )
        return 5
    source, prep_record = load_raw_source() if args.grounding == "raw" else load_source()
    attachments = build_attachments(args.path, source)
    projection = project_usage(args.path, source)
    worst = float(projection["worst_case_calculated_cost_usd"])
    if over_cap(already, worst, args.cap_usd):
        print(
            f"Refusing to run: ${already:.2f} already calculated across "
            f"{len(recorded_runs())} recorded invocation(s) of this pilot plus a "
            f"${worst:.2f} worst case exceeds the ${args.cap_usd:.2f} cap.",
            file=sys.stderr,
        )
        return 3

    settings = Settings(
        openai_model=PILOT_MODEL,
        openai_reasoning_effort=PILOT_REASONING_EFFORT,
        max_output_tokens=PILOT_MAX_OUTPUT_TOKENS,
        openai_max_retries=PILOT_MAX_RETRIES,
    )
    if not settings.openai_api_key:
        print("Refusing to run: no OPENAI_API_KEY in the environment or .env.", file=sys.stderr)
        return 4

    record = base_record(args.path, source, prep_record, args.grounding)
    record.update(
        {
            "kind": "run",
            "api_requests_made": "see attempts",
            "model_inputs": [item.record.model_dump(mode="json") for item in attachments],
            "projection": projection,
            "confirmed_billing": None,
            "confirmed_billing_note": (
                "Fill in from the API usage dashboard, matched by request id. Calculated "
                "cost is never presented as confirmed billing."
            ),
        }
    )
    destination = invocation_dir(args.path)
    started = datetime.now(UTC)
    result: AnalysisResult | None = None
    error: SourceAnalysisError | None = None
    try:
        result = analyze_source(
            source,
            settings=settings,
            input_mode=PATHS[args.path],
            attachments=attachments,
        )
    except SourceAnalysisError as exc:
        error = exc
    ended = datetime.now(UTC)

    attempts = list(result.attempts) if result is not None else list(getattr(error, "attempts", []))
    record["timing"] = {
        "started_at": started.isoformat(),
        "ended_at": ended.isoformat(),
        "elapsed_seconds": round((ended - started).total_seconds(), 3),
    }
    record["attempts_summary"] = [
        {
            "attempt_number": attempt.attempt_number,
            "outcome": attempt.outcome,
            "request_id": attempt.request_id,
            "elapsed_seconds": attempt.elapsed_seconds,
            "usage": attempt.usage.model_dump(mode="json") if attempt.usage else None,
            "problems": attempt.problems,
            "error": attempt.error,
        }
        for attempt in attempts
    ]
    # Grounding and validation failures are recorded as validation facts, kept
    # apart from any judgment of analytical quality.
    record["validation"] = {
        "outcome": "valid" if result is not None else "failed",
        "failure_type": type(error).__name__ if error else None,
        "problems_by_attempt": {
            str(attempt.attempt_number): attempt.problems
            for attempt in attempts
            if attempt.problems
        },
        "note": (
            "A grounding failure means a quotation did not match the declared grounding "
            "reference. In the PDF path that can happen because the extraction renders "
            "the passage differently, so it is not evidence about analysis quality."
        ),
    }
    total_input = sum(a.usage.input_tokens for a in attempts if a.usage)
    total_output = sum(a.usage.output_tokens for a in attempts if a.usage)
    cached = sum(a.usage.cached_input_tokens or 0 for a in attempts if a.usage)
    record["reported_usage"] = {
        "input_tokens": total_input,
        "output_tokens": total_output,
        "cached_input_tokens": cached,
        "reasoning_tokens": sum(a.usage.reasoning_tokens or 0 for a in attempts if a.usage),
        "note": "Reasoning tokens are a subset of output tokens and are not added again.",
    }
    record["calculated_cost"] = calculated_cost(total_input, total_output, cached)
    # An attempt with no reported usage may still have been charged. Record that
    # as unknown, never as zero, and let the guard refuse the next paid run.
    missing = [
        {
            "attempt_number": attempt.attempt_number,
            "outcome": attempt.outcome,
            "response_received": attempt.raw_content is not None,
            "request_id": attempt.request_id,
        }
        for attempt in attempts
        if attempt.usage is None
    ]
    record["usage_accounting"] = {
        "usage_complete": not missing,
        "attempts_recorded": len(attempts),
        "attempts_missing_usage": missing,
        "note": (
            "Calculated cost covers only attempts that reported usage. Any attempt listed "
            "in attempts_missing_usage may have been charged an amount this record cannot "
            "state; it is counted as unknown, not as zero, and blocks further paid runs of "
            "this pilot until reconciled against the usage dashboard."
        ),
    }

    if result is not None:
        (destination / "analysis_result.json").write_text(result.model_dump_json(indent=2) + "\n")
    for attempt in attempts:
        (destination / f"attempt_{attempt.attempt_number}.json").write_text(
            attempt.model_dump_json(indent=2) + "\n"
        )
    (destination / "run_record.json").write_text(json.dumps(record, indent=2) + "\n")

    print(f"path={args.path}  outcome={record['validation']['outcome']}")
    print(f"  attempts: {len(attempts)}  elapsed: {record['timing']['elapsed_seconds']}s")
    print(f"  reported usage: {total_input} in / {total_output} out (cached {cached})")
    print(f"  calculated cost: ${record['calculated_cost']['total_usd']} (not confirmed billing)")
    if not record["usage_accounting"]["usage_complete"]:
        print(
            "  WARNING: an attempt reported no usage; its cost is unknown, not zero, "
            "and further paid runs of this pilot are blocked until reconciled.",
        )
    print(f"  written: {destination.relative_to(REPO_ROOT)}")
    return 0 if result is not None else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, handler in (("dry-run", cmd_dry_run), ("run", cmd_run)):
        child = sub.add_parser(name)
        child.add_argument("--path", choices=sorted(PATHS), required=True)
        child.add_argument("--cap-usd", type=float, default=DEFAULT_CAP_USD)
        child.add_argument("--model", default=PILOT_MODEL, choices=sorted(RATES_BY_MODEL))
        child.add_argument("--effort", default=PILOT_REASONING_EFFORT)
        child.add_argument("--max-output-tokens", type=int, default=PILOT_MAX_OUTPUT_TOKENS)
        child.add_argument(
            "--grounding",
            choices=("prepared", "raw"),
            default="prepared",
            help="what verbatim quotations are checked against",
        )
        child.add_argument("--out-root", default="li_input_format")
        if name == "run":
            child.add_argument("--confirm-paid", action="store_true")
        child.set_defaults(handler=handler)
    args = parser.parse_args()
    handler: Any = args.handler
    return int(handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
