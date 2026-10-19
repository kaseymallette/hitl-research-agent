#!/usr/bin/env python
"""Run one cell of the A/B matrix: one article, one input method, one model.

    uv run python scripts/run_analysis.py --pdf data/research/ab_testing/<name>.pdf \
        --input pdf --model gpt-6.1-sol --effort medium --confirm-paid

    uv run python scripts/run_analysis.py --slug <slug> --input text_crops \
        --model gpt-6-astra --effort low --confirm-paid

`--input pdf` sends the original PDF. `--input text_crops` sends the prepared
text plus its retained crops, read from the preparation directory that
`prepare_sources.py` wrote.

Both arms take the source's provenance from the owner-confirmed manifest,
`data/research/sources.yaml`: the PDF arm directly, the text arm through the
`provenance.json` preparation copied from it. The title and source type are
part of the prompt, so reading them from one place keeps the prompt identical
across arms.

Writes <out>/<slug>/<config>/analysis.json (the analysis as the model returned
it) and run_record.json (configuration, usage, calculated cost, runtime,
request ids, every attempt, and fingerprints of the prompt, schema, and code).
When the close reading succeeds, a second call gives the model the article and
that close reading and writes its own judgment of the argument to
argument_evaluation.json (ADR-0012); its usage and cost are recorded alongside.
A cell that already holds an analysis is not rerun; delete its directory first.
Rerunning a failed cell keeps the failed run's record as failed_run_<n>.json,
since its tokens were billed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

import pymupdf  # noqa: E402
import yaml  # noqa: E402

from hitl_research_agent.analysis import (  # noqa: E402
    AnalysisError,
    AttemptRecord,
    analyze_source,
    evaluate_argument,
)
from hitl_research_agent.config import Settings  # noqa: E402
from hitl_research_agent.cost import calculated_cost  # noqa: E402
from hitl_research_agent.inputs import LoadedAttachment, load_attachment  # noqa: E402
from hitl_research_agent.models import (  # noqa: E402
    ArgumentEvaluation,
    ExtractedAnalysis,
    PreparationGap,
    Provenance,
    SourceAnalysis,
    SourceArgumentEvaluation,
    SourceDocument,
    source_id_for,
)
from hitl_research_agent.prompts import (  # noqa: E402
    EVALUATION_PROMPT,
    INPUT_MODE_INSTRUCTIONS,
    SYSTEM_PROMPT,
)

INPUT_MODES = {"pdf": "pdf", "text_crops": "prepared_text_and_crops", "text": "prepared_text"}


def shown(path: Path) -> str:
    """Repo-relative where possible, absolute otherwise."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def config_slug(input_choice: str, model: str, effort: str) -> str:
    return f"{input_choice}__{model}-{effort}"


PROVENANCE_FIELDS = (
    "source_title",
    "source_authors",
    "publication_date",
    "source_type",
    "doi",
    "publisher",
    "url",
    "retrieved_at",
)


def confirmed_provenance(data: dict[str, Any], slug: str) -> Provenance:
    """Provenance from a manifest entry or the provenance.json copied from one,
    with the source_id every analysis of this slug shares."""
    fields = {key: data[key] for key in PROVENANCE_FIELDS if data.get(key) not in (None, [])}
    return Provenance.model_validate({**fields, "source_id": source_id_for(slug)})


def manifest_provenance(manifest: Path, slug: str) -> Provenance:
    entries = yaml.safe_load(manifest.read_text(encoding="utf-8"))["sources"]
    for entry in entries:
        if entry["slug"] == slug:
            return confirmed_provenance(entry, slug)
    raise SystemExit(f"No entry for {slug} in {shown(manifest)}; its provenance must be confirmed.")


def load_pdf_source(pdf: Path, relative: str, provenance: Provenance) -> SourceDocument:
    with pymupdf.open(pdf) as document:
        pages = document.page_count
    return SourceDocument(
        # The model reads the attached PDF; this text is the placeholder the
        # input contract requires and is never sent.
        text=f"(the source is supplied as the attached PDF: {relative}, {pages} pages)",
        provenance=provenance,
    )


def load_prepared_source(prep_dir: Path) -> tuple[SourceDocument, list[LoadedAttachment]]:
    """The prepared text plus one crop per declared preparation gap."""
    record_path = prep_dir / "prep_record.json"
    if not record_path.is_file():
        raise SystemExit(
            f"No preparation record at {shown(record_path)}. "
            "Run scripts/prepare_sources.py for this slug first."
        )
    record = json.loads(record_path.read_text())
    text = (prep_dir / record["prepared_text"]).read_text()
    # Provenance is owner-confirmed and written beside the text, not in the record.
    confirmed = json.loads((prep_dir / "provenance.json").read_text())
    gaps = [
        PreparationGap(
            id=item["id"],
            kind=item["kind"],
            page=item["page"],
            label=item.get("label"),
            image=item.get("image"),
        )
        for item in record.get("annotations", [])
    ]
    source = SourceDocument(
        text=text,
        provenance=confirmed_provenance(confirmed, record["slug"]),
        preparation_directory=shown(prep_dir),
        preparation_gaps=gaps,
    )
    crops = [
        load_attachment(
            REPO_ROOT,
            shown(prep_dir / str(gap.image)),
            kind="image",
            page=gap.page,
            gap_id=gap.id,
            label=gap.label,
        )
        for gap in gaps
        if gap.image
    ]
    # No crops is a legitimate preparation outcome: an article with no figures,
    # equations, or multi-level table headers has nothing text could not carry.
    # The caller then runs this cell in prepared_text mode and records that it
    # did, rather than claiming crops were sent.
    return source, crops


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fingerprints(input_mode: str) -> dict[str, Any]:
    """What makes the prompt, schema, and correction policy demonstrably the
    same across cells. Computed before the paid call, so a failure here costs
    nothing."""

    def git(*args: str) -> str:
        return subprocess.run(
            ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()

    instructions = INPUT_MODE_INSTRUCTIONS[input_mode]  # type: ignore[index]
    return {
        "system_prompt_sha256": sha256_text(SYSTEM_PROMPT),
        "input_mode_instructions_sha256": sha256_text(instructions) if instructions else None,
        "output_schema_sha256": sha256_text(
            json.dumps(ExtractedAnalysis.model_json_schema(), sort_keys=True)
        ),
        "evaluation_prompt_sha256": sha256_text(EVALUATION_PROMPT),
        "evaluation_schema_sha256": sha256_text(
            json.dumps(ArgumentEvaluation.model_json_schema(), sort_keys=True)
        ),
        "git_commit": git("rev-parse", "HEAD"),
        # The correction policy is code; uncommitted changes to it would make
        # git_commit an incomplete description of what ran.
        "code_uncommitted_changes": bool(git("status", "--porcelain", "--", "src", "scripts")),
    }


def attempt_entries(attempts: list[AttemptRecord]) -> list[dict[str, Any]]:
    return [
        {
            "attempt_number": a.attempt_number,
            "outcome": a.outcome,
            "request_id": a.request_id,
            "elapsed_seconds": a.elapsed_seconds,
            "usage": a.usage.model_dump(mode="json") if a.usage else None,
            "problems": a.problems,
            "error": a.error,
        }
        for a in attempts
    ]


def cost_of(model: str, totals: dict[str, int | None]) -> dict[str, Any]:
    try:
        return calculated_cost(
            model,
            input_tokens=totals["input_tokens"] or 0,
            output_tokens=totals["output_tokens"] or 0,
            cached_input_tokens=totals["cached_input_tokens"] or 0,
        )
    except ValueError as exc:
        return {"error": str(exc)}


def usage_totals(attempts: list[AttemptRecord]) -> dict[str, int | None]:
    """Totals over every attempt that reported usage, including attempts in a
    run that then failed, since those tokens were still spent.

    The reasoning total is None when any reporting attempt left it unreported.
    An unreported cached count is taken as zero, which prices those tokens at
    the full input rate rather than understating the cost.
    """
    usages = [a.usage for a in attempts if a.usage]
    reasoning = [u.reasoning_tokens for u in usages]
    return {
        "input_tokens": sum(u.input_tokens for u in usages),
        "output_tokens": sum(u.output_tokens for u in usages),
        "reasoning_tokens": sum(r or 0 for r in reasoning)
        if usages and None not in reasoning
        else None,
        "cached_input_tokens": sum(u.cached_input_tokens or 0 for u in usages),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", help="path to the PDF, relative to the repo")
    parser.add_argument("--slug", help="preparation slug, for --input text_crops")
    parser.add_argument("--input", default="pdf", choices=sorted(INPUT_MODES))
    parser.add_argument("--model", default=None, help="defaults to the configured model")
    parser.add_argument("--effort", default=None, help="reasoning effort")
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--manifest", default="data/research/sources.yaml")
    parser.add_argument("--prepared", default="outputs/preparation")
    parser.add_argument("--out", default="outputs/ab_testing")
    parser.add_argument("--confirm-paid", action="store_true", help="required: this calls the API")
    args = parser.parse_args(argv)

    if not args.confirm_paid:
        print("Refusing to run: a paid call needs --confirm-paid.", file=sys.stderr)
        return 2

    # No hidden client retries: every request is an attempt the record can see,
    # and runtime is not inflated by retries nobody recorded. A transient
    # failure fails the cell, which is then rerun.
    overrides: dict[str, Any] = {"openai_max_retries": 0}
    if args.model:
        overrides["openai_model"] = args.model
    if args.effort:
        overrides["openai_reasoning_effort"] = args.effort
    if args.max_output_tokens:
        overrides["max_output_tokens"] = args.max_output_tokens
    settings = Settings(**overrides)
    if not settings.openai_api_key:
        print("Refusing to run: no OPENAI_API_KEY in the environment or .env.", file=sys.stderr)
        return 2

    attachments: list[LoadedAttachment] = []
    input_mode = INPUT_MODES[args.input]
    if args.input == "pdf":
        if not args.pdf:
            print("--input pdf needs --pdf.", file=sys.stderr)
            return 2
        pdf = REPO_ROOT / args.pdf
        if not pdf.is_file():
            print(f"No such PDF: {args.pdf}", file=sys.stderr)
            return 2
        slug = pdf.stem
        provenance = manifest_provenance(REPO_ROOT / args.manifest, slug)
        source = load_pdf_source(pdf, args.pdf, provenance)
        attachments = [load_attachment(REPO_ROOT, args.pdf, kind="pdf")]
    else:
        if not args.slug:
            print(f"--input {args.input} needs --slug.", file=sys.stderr)
            return 2
        slug = args.slug
        prep_dir = REPO_ROOT / args.prepared / slug
        source, crops = load_prepared_source(prep_dir)
        attachments = crops if args.input == "text_crops" else []
        if args.input == "text_crops" and not crops:
            # Preparation found nothing text could not carry, so this cell is
            # prepared text with a crop count of zero. The arm is the input
            # workflow, not the crops, so the article stays in the experiment.
            input_mode = "prepared_text"
            print(f"{shown(prep_dir)} declares no crops; sending prepared text alone.")

    config = config_slug(args.input, settings.openai_model, settings.openai_reasoning_effort)
    destination = REPO_ROOT / args.out / slug / config
    if (destination / "analysis.json").exists():
        print(
            f"{shown(destination)} already holds an analysis; delete the directory to rerun it.",
            file=sys.stderr,
        )
        return 2
    fingerprint = fingerprints(input_mode)

    started = datetime.now(UTC)
    result = None
    error: AnalysisError | None = None
    try:
        result = analyze_source(
            source,
            settings=settings,
            input_mode=input_mode,  # type: ignore[arg-type]
            attachments=attachments,
        )
    except AnalysisError as exc:
        error = exc
    ended = datetime.now(UTC)
    # Created only once there is a record to write, so a crash before the call
    # leaves no empty cell behind.
    destination.mkdir(parents=True, exist_ok=True)

    attempts = list(result.attempts) if result else list(error.attempts if error else [])
    record: dict[str, Any] = {
        "slug": slug,
        "config": config,
        "input_method": args.input,
        # input_method is the arm; input_mode is what the model actually
        # received, which differs when the prepared article had no crops.
        "input_mode": input_mode,
        "crops_sent": len(attachments) if args.input == "text_crops" else None,
        "model": settings.openai_model,
        "reasoning_effort": settings.openai_reasoning_effort,
        "max_output_tokens": settings.max_output_tokens,
        "openai_max_retries": settings.openai_max_retries,
        **fingerprint,
        "model_inputs": [item.record.as_record() for item in attachments],
        "started_at": started.isoformat(),
        "elapsed_seconds": round((ended - started).total_seconds(), 3),
        "outcome": "analysis returned" if result else f"failed: {error.kind if error else '?'}",
        "attempts": attempt_entries(attempts),
    }

    totals = usage_totals(attempts)
    record["usage"] = totals
    tokens_in, tokens_out = totals["input_tokens"] or 0, totals["output_tokens"] or 0
    record["calculated_cost"] = cost_of(settings.openai_model, totals)

    if result:
        record["analysis_scope"] = result.analysis_scope
        analysis_path = destination / "analysis.json"
        analysis_path.write_text(
            json.dumps(json.loads(result.analysis.model_dump_json()), indent=2, ensure_ascii=False)
            + "\n"
        )
        cost = record["calculated_cost"]
        print(f"analysis: {shown(analysis_path)}")
        print(
            f"  {len(result.analysis.content.reading_path)} steps, "
            f"{sum(len(step.claims) for step in result.analysis.content.reading_path)} claims, "
            f"{tokens_in} in / {tokens_out} out, "
            f"{result.attempt_count} attempt(s), "
            f"{record['elapsed_seconds']}s, "
            f"${cost.get('total_usd', '?')} calculated"
        )
    else:
        print(f"no analysis returned: {error.kind if error else '?'}: {error}", file=sys.stderr)

    evaluated = False
    if result:
        evaluated = run_argument_evaluation(
            source, result.analysis, settings, input_mode, attachments, destination, record
        )

    record_path = destination / "run_record.json"
    if record_path.exists():
        # Only a failed run leaves a record without an analysis (an analysis
        # refuses the rerun above). Its tokens were billed, so it is kept.
        number = len(list(destination.glob("failed_run_*.json"))) + 1
        kept = destination / f"failed_run_{number}.json"
        record_path.rename(kept)
        print(f"previous failed run kept: {shown(kept)}")
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    print(f"run record: {shown(destination / 'run_record.json')}")
    return 0 if result and evaluated else 1


def run_argument_evaluation(
    source: SourceDocument,
    analysis: SourceAnalysis,
    settings: Settings,
    input_mode: str,
    attachments: list[LoadedAttachment],
    destination: Path,
    record: dict[str, Any],
) -> bool:
    """The second call. Its failure is recorded and the close reading is kept."""
    started = datetime.now(UTC)
    try:
        evaluation = evaluate_argument(
            source,
            analysis.content,
            settings=settings,
            input_mode=input_mode,  # type: ignore[arg-type]
            attachments=attachments,
        )
        attempts, outcome = list(evaluation.attempts), "evaluation returned"
    except AnalysisError as exc:
        evaluation, attempts, outcome = None, list(exc.attempts), f"failed: {exc.kind}"
        print(f"no argument evaluation returned: {exc.kind}: {exc}", file=sys.stderr)
    ended = datetime.now(UTC)

    totals = usage_totals(attempts)
    section: dict[str, Any] = {
        "outcome": outcome,
        "started_at": started.isoformat(),
        "elapsed_seconds": round((ended - started).total_seconds(), 3),
        "attempts": attempt_entries(attempts),
        "usage": totals,
        "calculated_cost": cost_of(settings.openai_model, totals),
    }
    record["argument_evaluation"] = section
    costs = [
        record["calculated_cost"].get("total_usd"),
        section["calculated_cost"].get("total_usd"),
    ]
    record["total_calculated_cost_usd"] = (
        round(sum(costs), 6) if all(c is not None for c in costs) else None
    )

    if evaluation is None:
        return False
    stored = SourceArgumentEvaluation(
        analysis_id=analysis.id, provenance=analysis.provenance, content=evaluation.evaluation
    )
    path = destination / "argument_evaluation.json"
    path.write_text(
        json.dumps(json.loads(stored.model_dump_json()), indent=2, ensure_ascii=False) + "\n"
    )
    print(
        f"argument evaluation: {shown(path)}\n"
        f"  {len(evaluation.evaluation.evaluation.split())} words, "
        f"{totals['input_tokens']} in / {totals['output_tokens']} out, "
        f"{section['elapsed_seconds']}s, "
        f"${section['calculated_cost'].get('total_usd', '?')} calculated; "
        f"${record['total_calculated_cost_usd']} for both calls"
    )
    return True


if __name__ == "__main__":
    raise SystemExit(main())
