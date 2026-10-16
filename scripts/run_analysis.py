#!/usr/bin/env python
"""Run one cell of the A/B matrix: one article, one input method, one model.

    uv run python scripts/run_analysis.py --pdf data/research/ab_testing/<name>.pdf \
        --title "Paper title" --input pdf --model gpt-6.1-sol --effort medium --confirm-paid

    uv run python scripts/run_analysis.py --slug <slug> --input text_crops \
        --model gpt-6-astra --effort low --confirm-paid

`--input pdf` sends the original PDF. `--input text_crops` sends the prepared
text plus its retained crops, read from the preparation directory that
`prepare_sources.py` wrote.

Writes <out>/<slug>/<config>/analysis.json (the analysis as the model returned
it) and run_record.json (configuration, usage, calculated cost, runtime,
request ids, and every attempt).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

import pymupdf  # noqa: E402

from hitl_research_agent.analysis import AnalysisError, analyze_source  # noqa: E402
from hitl_research_agent.config import Settings  # noqa: E402
from hitl_research_agent.cost import calculated_cost  # noqa: E402
from hitl_research_agent.inputs import LoadedAttachment, load_attachment  # noqa: E402
from hitl_research_agent.models import PreparationGap, Provenance, SourceDocument  # noqa: E402

SOURCE_TYPES = (
    "peer_reviewed_paper",
    "preprint",
    "government_report",
    "government_policy",
    "research_institute_report",
    "technical_document",
    "industry_report",
    "news_article",
    "blog_post",
    "other",
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


def load_pdf_source(pdf: Path, relative: str, title: str, source_type: str) -> SourceDocument:
    with pymupdf.open(pdf) as document:
        pages = document.page_count
        embedded = (document.metadata or {}).get("title") or ""
    resolved = title or embedded.strip()
    if not resolved:
        raise SystemExit("No title given and none embedded in the PDF; pass --title.")
    return SourceDocument(
        # The model reads the attached PDF; this text is the placeholder the
        # input contract requires and is never sent.
        text=f"(the source is supplied as the attached PDF: {relative}, {pages} pages)",
        provenance=Provenance(
            source_title=resolved,
            source_type=source_type,  # type: ignore[arg-type]
            retrieved_at=datetime.now(UTC),
        ),
    )


def load_prepared_source(
    prep_dir: Path, title: str, source_type: str
) -> tuple[SourceDocument, list[LoadedAttachment]]:
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
        provenance=Provenance(
            source_title=title or confirmed["source_title"],
            source_authors=confirmed.get("source_authors", []),
            publication_date=confirmed.get("publication_date"),
            source_type=confirmed.get("source_type", source_type),
            doi=confirmed.get("doi"),
            publisher=confirmed.get("publisher"),
            url=confirmed.get("url"),
            retrieved_at=confirmed["retrieved_at"],
        ),
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", help="path to the PDF, relative to the repo")
    parser.add_argument("--slug", help="preparation slug, for --input text_crops")
    parser.add_argument("--title", default="", help="source title; defaults to the PDF's own")
    parser.add_argument("--source-type", default="peer_reviewed_paper", choices=SOURCE_TYPES)
    parser.add_argument("--input", default="pdf", choices=sorted(INPUT_MODES))
    parser.add_argument("--model", default=None, help="defaults to the configured model")
    parser.add_argument("--effort", default=None, help="reasoning effort")
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--prepared", default="outputs/preparation")
    parser.add_argument("--out", default="outputs/ab_testing")
    parser.add_argument("--confirm-paid", action="store_true", help="required: this calls the API")
    args = parser.parse_args()

    if not args.confirm_paid:
        print("Refusing to run: a paid call needs --confirm-paid.", file=sys.stderr)
        return 2

    overrides: dict[str, Any] = {}
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
        source = load_pdf_source(pdf, args.pdf, args.title, args.source_type)
        attachments = [load_attachment(REPO_ROOT, args.pdf, kind="pdf")]
    else:
        if not args.slug:
            print(f"--input {args.input} needs --slug.", file=sys.stderr)
            return 2
        slug = args.slug
        prep_dir = REPO_ROOT / args.prepared / slug
        source, crops = load_prepared_source(prep_dir, args.title, args.source_type)
        attachments = crops if args.input == "text_crops" else []
        if args.input == "text_crops" and not crops:
            # Preparation found nothing text could not carry, so this cell is
            # prepared text with a crop count of zero. The arm is the input
            # workflow, not the crops, so the article stays in the experiment.
            input_mode = "prepared_text"
            print(f"{shown(prep_dir)} declares no crops; sending prepared text alone.")

    config = config_slug(args.input, settings.openai_model, settings.openai_reasoning_effort)
    destination = REPO_ROOT / args.out / slug / config
    destination.mkdir(parents=True, exist_ok=True)

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
        "model_inputs": [item.record.as_record() for item in attachments],
        "started_at": started.isoformat(),
        "elapsed_seconds": round((ended - started).total_seconds(), 3),
        "outcome": "analysis returned" if result else f"failed: {error.kind if error else '?'}",
        "attempts": [
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
        ],
    }

    cached = sum(a.usage.cached_input_tokens or 0 for a in attempts if a.usage)
    tokens_in = result.input_tokens if result else (error.input_tokens if error else 0)
    tokens_out = result.output_tokens if result else (error.output_tokens if error else 0)
    record["usage"] = {
        "input_tokens": tokens_in,
        "output_tokens": tokens_out,
        "cached_input_tokens": cached,
    }
    try:
        record["calculated_cost"] = calculated_cost(
            settings.openai_model,
            input_tokens=tokens_in,
            output_tokens=tokens_out,
            cached_input_tokens=cached,
        )
    except ValueError as exc:
        record["calculated_cost"] = {"error": str(exc)}

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
            f"  {len(result.analysis.content.central_claims)} claims, "
            f"{tokens_in} in / {tokens_out} out, "
            f"{result.attempt_count} attempt(s), "
            f"{record['elapsed_seconds']}s, "
            f"${cost.get('total_usd', '?')} calculated"
        )
    else:
        print(f"no analysis returned: {error.kind if error else '?'}: {error}", file=sys.stderr)

    (destination / "run_record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"run record: {shown(destination / 'run_record.json')}")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
