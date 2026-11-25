#!/usr/bin/env python
"""Water experiment, the answering step: answer research questions from retrieved items.

    uv run python scripts/answer.py --questions 1 5
    uv run python scripts/answer.py --questions 1 --approaches structured --dry-run
    uv run python scripts/answer.py --questions 1 --budget 6000 --force

For each question (numbered as in ``docs/PROJECT.md``) and approach (``rag`` and
``structured``; both by default), the items nearest the question are
taken in rank order until the next one would overflow the budget (``--budget``, default
4,000 tokens of item text, counted with the embedding model's tokenizer). They are
written to ``retrieved.md`` with the question and the sources they come from, and one
Codex session answers from them with ``prompts/06_answer.md``: the same model, effort,
and ChatGPT sign-in as single-source analysis. The prompt, model, and budget are the
same for every approach; only the retrieved items differ.

Each answer goes to ``outputs/answers/<approach>/q<NN>/``:

* ``answer.md``: the answer;
* ``record.json``: the question, the budget, every retrieved item (its label in the
  answer, chunk id, article, kind, score, and tokens), the citations found in the
  answer, Codex's token usage, the time taken, and what is known about cost.

``retrieved.md`` and Codex's event log go to ``.codex_runs/answers/<approach>/q<NN>/``,
which git ignores, since the retrieved text includes the copyrighted articles' text.
Answers already written are skipped unless ``--force``. ``--dry-run`` writes
``retrieved.md`` and stops before Codex. Only a technical failure stops a run: Codex
exiting with an error or timing out, or ``answer.md`` not written. An answer that cites
nothing, or cites a label it was not given, is recorded as it is.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml
from build_index import APPROACHES, EMBEDDING_MODEL, INDEX_ROOT, retrieve
from run_single_source import (
    EFFORT,
    LOGS,
    MODEL,
    REPO_ROOT,
    SOURCES,
    STUDY,
    TIMEOUT_SECONDS,
    CallFailed,
    codex_command,
    find_codex,
)

PROJECT = REPO_ROOT / "docs" / "PROJECT.md"
PROMPT = STUDY / "prompts" / "06_answer.md"
ANSWERS = STUDY / "outputs" / "answers"
ANSWER_LOGS = LOGS / "answers"
DEFAULT_BUDGET = 4000

KIND_LABELS = {
    "source_text": "article text",
    "close_reading": "close reading",
    "claims_reference": "claims reference",
    "argument_evaluation": "argument evaluation",
}
_CITATION = re.compile(r"\[(E\d+(?:\s*,\s*E\d+)*)\]")

Ranked = list[tuple[float, dict[str, Any]]]


def research_questions(project_md: str) -> dict[int, str]:
    """The numbered list under the "Research questions" heading, as one line each."""
    _, found, rest = project_md.partition("### Research questions\n")
    if not found:
        raise ValueError("no '### Research questions' heading")
    section = re.split(r"^#", rest, maxsplit=1, flags=re.M)[0]
    pairs = re.findall(r"^(\d+)\.\s+(.*?)(?=^\d+\.\s|\Z)", section, flags=re.M | re.S)
    return {int(n): " ".join(text.split()) for n, text in pairs}


def within_budget(ranked: Ranked, budget: int) -> Ranked:
    """The ranked items, in order, up to the first that would take the total over budget."""
    kept: Ranked = []
    used = 0
    for score, chunk in ranked:
        if used + chunk["tokens"] > budget:
            break
        kept.append((score, chunk))
        used += chunk["tokens"]
    return kept


def _source_line(entry: dict[str, Any]) -> str:
    year = re.search(r"_(\d{4})_", entry["slug"])
    authors = ", ".join(entry.get("source_authors") or [entry.get("publisher", "")])
    return (
        f"- {entry['slug']}: {authors} ({year.group(1) if year else 'n.d.'}). "
        f"{entry['source_title']}. {entry.get('publisher', '')}."
    )


def render_retrieved(question: str, items: Ranked, sources: dict[str, dict[str, Any]]) -> str:
    """retrieved.md: the question, the sources the items come from, and the items as
    [E1], [E2], ... in rank order."""
    slugs = sorted({chunk["slug"] for _, chunk in items})
    parts = [f"# Question\n\n{question}\n", "# Sources\n"]
    parts += [_source_line(sources[slug]) for slug in slugs]
    parts.append("\n# Material\n")
    for n, (_, chunk) in enumerate(items, start=1):
        where = ""
        if chunk.get("pdf_pages"):
            where = ", PDF p. " + ", ".join(str(p) for p in chunk["pdf_pages"])
        parts.append(f"## [E{n}] {chunk['slug']}: {KIND_LABELS[chunk['kind']]}{where}\n")
        parts.append(chunk["text"].strip() + "\n")
    return "\n".join(parts)


def citations(answer: str, given: int) -> dict[str, Any]:
    """Which item labels the answer cites, how often, and any it was not given."""
    cited = Counter(
        label.strip() for group in _CITATION.findall(answer) for label in group.split(",")
    )
    labels = [f"E{n}" for n in range(1, given + 1)]
    return {
        "cited": {label: cited[label] for label in labels if cited[label]},
        "not_cited": [label for label in labels if not cited[label]],
        "unknown": sorted(set(cited) - set(labels), key=lambda s: int(s[1:])),
    }


def usage_from_log(log: str) -> dict[str, int] | None:
    """Token usage summed over the session's completed turns, or None if Codex reported none."""
    total: Counter[str] = Counter()
    found = False
    for line in log.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue  # Codex prints a few plain-text lines among its events
        if isinstance(event, dict) and event.get("type") == "turn.completed":
            total.update(event.get("usage", {}))
            found = True
    return dict(total) if found else None


# --------------------------------------------------------------------------- running


def run_codex(codex: Path, retrieved: str, log_dir: Path) -> str:
    """One Codex session in a folder holding only retrieved.md; returns answer.md."""
    log_dir.mkdir(parents=True, exist_ok=True)
    # No API key reaches Codex, so it runs on the ChatGPT sign-in and is never billed per token.
    env = {key: value for key, value in os.environ.items() if key != "OPENAI_API_KEY"}
    request = PROMPT.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="answer-") as tmp:
        workspace = Path(tmp)
        (workspace / "retrieved.md").write_text(retrieved, encoding="utf-8")
        command = codex_command(codex, workspace, log_dir / "message.md", request)
        with (log_dir / "codex.jsonl").open("w", encoding="utf-8") as log:
            try:
                result = subprocess.run(
                    command,
                    stdin=subprocess.DEVNULL,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    env=env,
                    timeout=TIMEOUT_SECONDS,
                    check=False,
                )
            except subprocess.TimeoutExpired as error:
                raise CallFailed(f"Codex did not finish within {TIMEOUT_SECONDS} s") from error
        if result.returncode != 0:
            raise CallFailed(f"Codex exited with status {result.returncode}")
        produced = workspace / "answer.md"
        if not produced.is_file():
            raise CallFailed("Codex did not write answer.md")
        return produced.read_text(encoding="utf-8")


def answer_one(
    number: int,
    question: str,
    approach: str,
    budget: int,
    sources: dict[str, dict[str, Any]],
    codex: Path | None,
) -> Path:
    """Retrieve, write retrieved.md, and (unless codex is None, a dry run) answer."""
    log_dir = ANSWER_LOGS / approach / f"q{number:02d}"
    log_dir.mkdir(parents=True, exist_ok=True)
    items = within_budget(retrieve(approach, question), budget)
    retrieved = render_retrieved(question, items, sources)
    (log_dir / "retrieved.md").write_text(retrieved, encoding="utf-8")
    if codex is None:
        return log_dir / "retrieved.md"

    started_at = datetime.now(UTC).isoformat(timespec="seconds")
    started = time.monotonic()
    answer = run_codex(codex, retrieved, log_dir)
    seconds = round(time.monotonic() - started, 1)

    name = APPROACHES[approach]
    index = json.loads((INDEX_ROOT / name / "index.json").read_text(encoding="utf-8"))
    indexes = {name: {"built_at": index["built_at"], "chunks": index["chunks"]}}
    record = {
        "question_number": number,
        "question": question,
        "approach": approach,
        "budget_tokens": budget,
        "budget_counts": f"item text, in {EMBEDDING_MODEL} tokenizer tokens",
        "retrieved_tokens": sum(chunk["tokens"] for _, chunk in items),
        "retrieved": [
            {
                "label": f"E{n}",
                "id": chunk["id"],
                "slug": chunk["slug"],
                "kind": chunk["kind"],
                "score": round(score, 4),
                "tokens": chunk["tokens"],
            }
            for n, (score, chunk) in enumerate(items, start=1)
        ],
        "citations": citations(answer, len(items)),
        "indexes": indexes,
        "model": MODEL,
        "effort": EFFORT,
        "prompt": str(PROMPT.relative_to(STUDY)),
        "prompt_sha256": hashlib.sha256(PROMPT.read_bytes()).hexdigest(),
        "started_at": started_at,
        "seconds": seconds,
        "usage": usage_from_log((log_dir / "codex.jsonl").read_text(encoding="utf-8")),
        "cost": {
            "billing": "ChatGPT sign-in, no API key: not billed per token",
            "usd": None,
        },
    }
    out = ANSWERS / approach / f"q{number:02d}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "answer.md").write_text(answer, encoding="utf-8")
    (out / "record.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--questions", type=int, nargs="+", required=True)
    parser.add_argument("--approaches", nargs="+", choices=APPROACHES, default=list(APPROACHES))
    parser.add_argument("--budget", type=int, default=DEFAULT_BUDGET, help="tokens of item text")
    parser.add_argument("--force", action="store_true", help="redo answers already written")
    parser.add_argument("--dry-run", action="store_true", help="write retrieved.md only")
    parser.add_argument("--codex", type=Path, help="path to the Codex CLI")
    args = parser.parse_args(argv)

    questions = research_questions(PROJECT.read_text(encoding="utf-8"))
    unknown = sorted(set(args.questions) - set(questions))
    if unknown:
        parser.error(f"no research question {unknown}; PROJECT.md has 1-{len(questions)}")
    manifest = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    sources = {entry["slug"]: entry for entry in manifest["sources"]}
    codex = None if args.dry_run else find_codex(args.codex)

    for number in args.questions:
        for approach in args.approaches:
            label = f"q{number:02d} {approach}"
            if not args.dry_run and not args.force:
                if (ANSWERS / approach / f"q{number:02d}" / "answer.md").exists():
                    print(f"{label}: already answered; --force to redo", flush=True)
                    continue
            print(f"{datetime.now():%H:%M} {label}: running", flush=True)
            try:
                written = answer_one(
                    number, questions[number], approach, args.budget, sources, codex
                )
            except CallFailed as error:
                log = ANSWER_LOGS / approach / f"q{number:02d}" / "codex.jsonl"
                print(f"{label} failed: {error}. Log: {log}", file=sys.stderr)
                return 1
            print(
                f"{datetime.now():%H:%M} {label}: wrote {written.relative_to(REPO_ROOT)}",
                flush=True,
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
