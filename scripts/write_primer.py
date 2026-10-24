#!/usr/bin/env python
"""Write a primer for one article: background on its field, to read first.

    uv run python scripts/write_primer.py \
        --pdf data/research/ab_testing/<name>.pdf --confirm-paid

The primer is the model's general knowledge — the article's concepts and
terms, what its numbers are measured against, and where it sits in its field —
not a reading of the article, and it is never given to the analysis
(ADR-0016). Writes <out>/<slug>/primer.md and primer_record.json (usage,
calculated cost, runtime, attempts). An article that already has a primer is
not rewritten; delete its directory first.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_analysis import (  # noqa: E402
    REPO_ROOT,
    attempt_entries,
    cost_of,
    fingerprints,
    load_attachment,
    load_pdf_source,
    manifest_provenance,
    sha256_text,
    shown,
    usage_totals,
)

from hitl_research_agent.analysis import AnalysisError, write_primer  # noqa: E402
from hitl_research_agent.config import Settings  # noqa: E402
from hitl_research_agent.prompts import PRIMER_PROMPT  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, help="path to the PDF, relative to the repo")
    parser.add_argument("--model", default="gpt-6.1-sol")
    parser.add_argument("--effort", default="medium")
    parser.add_argument("--manifest", default="data/research/sources.yaml")
    parser.add_argument("--out", default="outputs/primers")
    parser.add_argument("--confirm-paid", action="store_true", help="required: this calls the API")
    args = parser.parse_args(argv)

    if not args.confirm_paid:
        print("Refusing to run: a paid call needs --confirm-paid.", file=sys.stderr)
        return 2
    settings = Settings(
        openai_model=args.model, openai_reasoning_effort=args.effort, openai_max_retries=0
    )
    if not settings.openai_api_key:
        print("Refusing to run: no OPENAI_API_KEY in the environment or .env.", file=sys.stderr)
        return 2

    pdf = REPO_ROOT / args.pdf
    if not pdf.is_file():
        print(f"No such PDF: {args.pdf}", file=sys.stderr)
        return 2
    slug = pdf.stem
    destination = REPO_ROOT / args.out / slug
    if (destination / "primer.md").exists():
        print(
            f"{shown(destination)} already holds a primer; delete it to rewrite.", file=sys.stderr
        )
        return 2
    provenance = manifest_provenance(REPO_ROOT / args.manifest, slug)
    source = load_pdf_source(pdf, args.pdf, provenance)
    attachments = [load_attachment(REPO_ROOT, args.pdf, kind="pdf")]
    code = fingerprints("pdf")

    started = datetime.now(UTC)
    try:
        result = write_primer(source, settings=settings, input_mode="pdf", attachments=attachments)
        attempts, outcome = list(result.attempts), "primer returned"
    except AnalysisError as exc:
        result, attempts, outcome = None, list(exc.attempts), f"failed: {exc.kind}"
        print(f"no primer returned: {exc.kind}: {exc}", file=sys.stderr)
    ended = datetime.now(UTC)
    destination.mkdir(parents=True, exist_ok=True)

    totals = usage_totals(attempts)
    record: dict[str, Any] = {
        "slug": slug,
        "model": settings.openai_model,
        "reasoning_effort": settings.openai_reasoning_effort,
        "primer_prompt_sha256": sha256_text(PRIMER_PROMPT),
        "git_commit": code["git_commit"],
        "code_uncommitted_changes": code["code_uncommitted_changes"],
        "started_at": started.isoformat(),
        "elapsed_seconds": round((ended - started).total_seconds(), 3),
        "outcome": outcome,
        "attempts": attempt_entries(attempts),
        "usage": totals,
        "calculated_cost": cost_of(settings.openai_model, totals),
    }
    (destination / "primer_record.json").write_text(json.dumps(record, indent=2) + "\n")
    if result is None:
        return 1

    heading = (
        f"# Primer — {provenance.source_title}\n\n"
        f"*Background from {settings.openai_model} at {settings.openai_reasoning_effort} "
        f"effort, {started.date().isoformat()}. This is the model's general knowledge of the "
        "field, written to read before the article; it is not a reading of the article "
        "and is unchecked.*\n\n"
    )
    path = destination / "primer.md"
    path.write_text(heading + result.primer.primer.strip() + "\n", encoding="utf-8")
    print(
        f"primer: {shown(path)}\n"
        f"  {len(result.primer.primer.split())} words, "
        f"{totals['input_tokens']} in / {totals['output_tokens']} out, "
        f"{record['elapsed_seconds']}s, ${record['calculated_cost'].get('total_usd', '?')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
