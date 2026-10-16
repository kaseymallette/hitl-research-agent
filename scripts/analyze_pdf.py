#!/usr/bin/env python
"""Analyze one PDF and write the analysis as indented JSON.

The PDF itself goes to the model with the existing analysis prompt. Nothing is
extracted for the model to read, and the returned analysis is not checked
against the source -- that is an evaluation question for DeepEval and human
review, not a condition of writing the file.

    uv run python scripts/analyze_pdf.py --pdf data/research/<name>.pdf \
        --title "Paper title" --confirm-paid

Writes <out>/<slug>/analysis.json (the analysis) and run_record.json (model,
usage, timing, request ids, attempts, and the advisory notes).
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

from hitl_research_agent.config import Settings  # noqa: E402
from hitl_research_agent.extraction import (  # noqa: E402
    SourceAnalysisError,
    SourceDocument,
    analyze_source,
    load_attachment,
)
from hitl_research_agent.models.provenance import Provenance  # noqa: E402

SOURCE_TYPES = ("peer_reviewed_paper", "preprint", "report", "article", "book_chapter")


def shown(path: Path) -> str:
    """Repo-relative where possible, absolute otherwise (--out may point anywhere)."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, help="path to the PDF, relative to the repo")
    parser.add_argument("--title", help="source title; defaults to the PDF's embedded title")
    parser.add_argument("--source-type", default="peer_reviewed_paper", choices=SOURCE_TYPES)
    parser.add_argument("--model", default=None, help="defaults to the configured analyzer model")
    parser.add_argument("--effort", default=None, help="reasoning effort")
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--out", default="outputs/analyses")
    parser.add_argument("--confirm-paid", action="store_true", help="required: this calls the API")
    args = parser.parse_args()

    if not args.confirm_paid:
        print("Refusing to run: a paid call needs --confirm-paid.", file=sys.stderr)
        return 2

    pdf = REPO_ROOT / args.pdf
    if not pdf.is_file():
        print(f"No such PDF: {args.pdf}", file=sys.stderr)
        return 2

    with pymupdf.open(pdf) as document:
        pages = document.page_count
        embedded_title = (document.metadata or {}).get("title") or ""
    title = args.title or embedded_title.strip()
    if not title:
        print("No title given and none embedded in the PDF; pass --title.", file=sys.stderr)
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

    source = SourceDocument(
        # The model reads the attached PDF; this text is a placeholder the input
        # contract requires and is never sent.
        text=f"(the source is supplied as the attached PDF: {args.pdf}, {pages} pages)",
        provenance=Provenance(
            source_title=title,
            source_type=args.source_type,
            retrieved_at=datetime.now(UTC),
        ),
    )
    attachment = load_attachment(REPO_ROOT, args.pdf, kind="pdf")

    destination = REPO_ROOT / args.out / pdf.stem
    destination.mkdir(parents=True, exist_ok=True)
    started = datetime.now(UTC)
    error: SourceAnalysisError | None = None
    result = None
    try:
        result = analyze_source(
            source,
            settings=settings,
            input_mode="pdf",
            attachments=[attachment],
        )
    except SourceAnalysisError as exc:
        error = exc
    ended = datetime.now(UTC)

    attempts = list(result.attempts) if result else list(getattr(error, "attempts", []))
    record: dict[str, Any] = {
        "pdf": args.pdf,
        "pdf_sha256": attachment.record.sha256,
        "model": settings.openai_model,
        "reasoning_effort": settings.openai_reasoning_effort,
        "max_output_tokens": settings.max_output_tokens,
        "started_at": started.isoformat(),
        "elapsed_seconds": round((ended - started).total_seconds(), 3),
        "outcome": "analysis returned" if result else f"failed: {type(error).__name__}",
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
    if result:
        record["input_tokens"] = result.input_tokens
        record["output_tokens"] = result.output_tokens
        record["analysis_scope"] = result.analysis_scope
        analysis_path = destination / "analysis.json"
        analysis_path.write_text(
            json.dumps(json.loads(result.analysis.model_dump_json()), indent=2, ensure_ascii=False)
            + "\n"
        )
        print(f"analysis: {shown(analysis_path)}")
        print(
            f"  {len(result.analysis.central_claims)} claims, "
            f"{len(result.grounding_notes)} advisory note(s), "
            f"{result.input_tokens} in / {result.output_tokens} out, "
            f"attempt {result.attempt_count}"
        )
    else:
        print(f"no analysis returned: {type(error).__name__}: {error}", file=sys.stderr)

    (destination / "run_record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"diagnostics: {shown(destination / 'run_record.json')}")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
