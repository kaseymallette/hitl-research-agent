#!/usr/bin/env python
"""Literacy pilot: each approach's top pieces for every question, pooled for judging.

    uv run python scripts/pool.py [--depth 3] [--seed 1] [--archive NAME]

Reads the questions from `studies/literacy_pilot/data/topics.yaml` and searches both
of the pilot's indexes (build them first with `build_index.py build ... --study
literacy_pilot`). Writes, under `studies/literacy_pilot/outputs/`:

    runs/<approach>.trec   each approach's ranked list in TREC run format:
                           question, Q0, piece ID, rank, score, approach
    judging/pool.json      every pooled piece: its sheet code, question, piece ID, and
                           each approach's rank and score for it
    judging/sheet.csv      what the expert grades: one row per pooled piece, with the
                           question, its relevance criteria, the article, the piece's
                           text, and empty grade and note columns
    judging/sheet.md       the same pieces to read and grade: each question with its
                           criteria once, then its pieces by code, each ending in a
                           `Grade:` and a `Note:` line to type into

Every run first copies the grades and notes typed into sheet.md into sheet.csv (a blank
line in sheet.md leaves the CSV's value alone), so either file can be used to grade. A
grade other than 0, 1, or 2 stops the run and names the piece. `--markdown` only does
that and rewrites sheet.md from sheet.csv. When a pool already
exists, a full run needs `--archive NAME`: it moves the current runs/ and judging/ files
to `archive/NAME/`, then carries every grade and note to the new sheet for the same
piece and question, so nothing is graded twice. The new pool.json records which
embedding model each approach's index was built with.

Depth-k pooling as in TREC: a question's pool is the union of the approaches' top k.
On the sheet, each question's pieces are shuffled (with `--seed`, recorded in
pool.json) and carry only a code such as Q01-03, never the approach, rank, or score.
The sheet holds the articles' text, so git ignores it.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import build_index
import yaml

STUDY = Path(__file__).resolve().parents[1] / "studies" / "literacy_pilot"
TOPICS = STUDY / "data" / "topics.yaml"
SOURCES = STUDY / "data" / "sources.yaml"
OUTPUTS = STUDY / "outputs"
SHEET_COLUMNS = (
    "piece",
    "question_id",
    "question",
    "relevant",
    "not_relevant",
    "article",
    "text",
    "grade",
    "note",
)

Ranked = list[tuple[float, dict[str, Any]]]


def trec_lines(topic_id: str, ranked: Ranked, tag: str) -> list[str]:
    """One TREC run line per piece, ranks from 1."""
    return [
        f"{topic_id} Q0 {piece['id']} {rank} {score:.6f} {tag}"
        for rank, (score, piece) in enumerate(ranked, start=1)
    ]


def pool(topic_id: str, runs: dict[str, Ranked], rng: random.Random) -> list[dict[str, Any]]:
    """The union of the runs' pieces for one question, shuffled and coded in that order.
    A piece in more than one run appears once, with each run's rank and score."""
    pieces: dict[str, dict[str, Any]] = {}
    for approach, ranked in runs.items():
        for rank, (score, piece) in enumerate(ranked, start=1):
            entry = pieces.setdefault(piece["id"], {"piece": piece, "runs": {}})
            entry["runs"][approach] = {"rank": rank, "score": round(score, 6)}
    entries = list(pieces.values())
    rng.shuffle(entries)
    for n, entry in enumerate(entries, start=1):
        entry["code"] = f"{topic_id}-{n:02d}"
    return entries


Grades = dict[tuple[str, str], tuple[str, str]]


def sheet_row(
    topic: dict[str, Any], entry: dict[str, Any], titles: dict[str, str], graded: Grades
) -> list[str]:
    piece = entry["piece"]
    grade, note = graded.get((topic["id"], piece["id"]), ("", ""))
    return [
        entry["code"],
        topic["id"],
        topic["question"],
        topic["relevant"],
        topic["not_relevant"],
        titles[piece["slug"]],
        piece["text"],
        grade,
        note,
    ]


def carried_grades(sheet: list[dict[str, str]], pooled: list[dict[str, Any]]) -> Grades:
    """Each graded (question, piece ID): its grade and note, joined through the codes."""
    by_code = {row["piece"]: row for row in sheet}
    return {
        (p["question_id"], p["id"]): (by_code[p["code"]]["grade"], by_code[p["code"]]["note"])
        for p in pooled
        if by_code[p["code"]]["grade"].strip() or by_code[p["code"]]["note"].strip()
    }


def _quote(text: str) -> str:
    return "\n".join(f"> {line}".rstrip() for line in text.splitlines())


def sheet_markdown(rows: list[dict[str, str]]) -> str:
    """The sheet's rows as a document to read: a section per question, in sheet order."""
    out = [
        "# Grading sheet",
        "",
        "Grade each piece against its question's criteria: **2** directly relevant, "
        "**1** partially relevant, **0** not relevant. Type the grade after `Grade:` "
        "under the piece (and anything else after `Note:`), then save. "
        "`uv run python scripts/pool.py --markdown` copies the grades into `sheet.csv`.",
    ]
    question = None
    for row in rows:
        if row["question_id"] != question:
            question = row["question_id"]
            out += [
                "",
                f"## {question}. {row['question']}",
                "",
                f"**Relevant:** {row['relevant']}",
                "",
                f"**Not relevant:** {row['not_relevant']}",
            ]
        out += [
            "",
            f"### {row['piece']}",
            "",
            f"*{row['article']}*",
            "",
            _quote(row["text"]),
            "",
            f"Grade: {row['grade'].strip()}".rstrip(),
            "",
            f"Note: {row['note'].strip()}".rstrip(),
        ]
    return "\n".join(out) + "\n"


GRADES = {"", "0", "1", "2"}


def markdown_grades(markdown: str) -> dict[str, tuple[str, str]]:
    """The Grade and Note typed under each piece's heading, by piece code."""
    found: dict[str, list[str]] = {}
    code = None
    for line in markdown.splitlines():
        if line.startswith("### "):
            code = line[4:].strip()
            found[code] = ["", ""]
        elif code is not None and line.startswith("Grade:"):
            found[code][0] = line[len("Grade:") :].strip()
        elif code is not None and line.startswith("Note:"):
            found[code][1] = line[len("Note:") :].strip()
    bad = [f"{c} ({g!r})" for c, (g, _) in found.items() if g not in GRADES]
    if bad:
        raise SystemExit("sheet.md has grades other than 0, 1, or 2: " + ", ".join(bad))
    return {c: (g, n) for c, (g, n) in found.items()}


def sync_from_markdown(judging: Path) -> int:
    """Copy sheet.md's typed grades and notes into sheet.csv; returns how many changed."""
    sheet, md = judging / "sheet.csv", judging / "sheet.md"
    if not (sheet.exists() and md.exists()):
        return 0
    typed = markdown_grades(md.read_text(encoding="utf-8"))
    rows = read_sheet(sheet)
    changed = 0
    for row in rows:
        grade, note = typed.get(row["piece"], ("", ""))
        for column, value in (("grade", grade), ("note", note)):
            if value and value != row[column].strip():
                row[column] = value
                changed += 1
    write_sheet(sheet, [[row[c] for c in SHEET_COLUMNS] for row in rows])
    return changed


def write_sheet(path: Path, rows: list[list[str]]) -> None:
    # utf-8-sig so Excel reads the accents and curly quotes correctly.
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(SHEET_COLUMNS)
        writer.writerows(rows)


def read_sheet(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--depth", type=int, default=3, help="pieces per approach (k; default: 3)")
    parser.add_argument("--seed", type=int, default=1, help="seed for the sheet's order")
    parser.add_argument(
        "--markdown", action="store_true", help="only rewrite sheet.md from sheet.csv"
    )
    parser.add_argument("--archive", help="archive/ folder for the current pool")
    args = parser.parse_args(argv)
    judging = OUTPUTS / "judging"
    sheet = judging / "sheet.csv"
    changed = sync_from_markdown(judging)
    if changed:
        print(f"{changed} grades and notes copied from sheet.md to sheet.csv", file=sys.stderr)
    if args.markdown:
        (judging / "sheet.md").write_text(sheet_markdown(read_sheet(sheet)), encoding="utf-8")
        print(f"-> {judging / 'sheet.md'}", file=sys.stderr)
        return 0
    graded: Grades = {}
    if sheet.exists():
        if not args.archive:
            print(f"{sheet} exists: pass --archive NAME to keep it.", file=sys.stderr)
            return 1
        archive = OUTPUTS / "archive" / args.archive
        if archive.exists():
            print(f"{archive} already exists.", file=sys.stderr)
            return 1
        old_pool = json.loads((judging / "pool.json").read_text(encoding="utf-8"))["pool"]
        graded = carried_grades(read_sheet(sheet), old_pool)
        archive.mkdir(parents=True)
        for folder in ("runs", "judging"):
            if (OUTPUTS / folder).exists():
                (OUTPUTS / folder).rename(archive / folder)
        print(f"previous pool -> {archive}; {len(graded)} grades carried", file=sys.stderr)

    build_index.use_study("literacy_pilot")
    topics = yaml.safe_load(TOPICS.read_text(encoding="utf-8"))["topics"]
    titles = {
        s["slug"]: s["source_title"]
        for s in yaml.safe_load(SOURCES.read_text(encoding="utf-8"))["sources"]
    }
    rng = random.Random(args.seed)
    run_lines: dict[str, list[str]] = {a: [] for a in build_index.APPROACHES}
    pooled: list[dict[str, Any]] = []
    rows: list[list[str]] = []
    for topic in topics:
        runs = {
            approach: build_index.retrieve(approach, topic["question"], args.depth)
            for approach in build_index.APPROACHES
        }
        for approach, ranked in runs.items():
            run_lines[approach] += trec_lines(topic["id"], ranked, approach)
        for entry in pool(topic["id"], runs, rng):
            pooled.append(
                {"code": entry["code"], "question_id": topic["id"], "id": entry["piece"]["id"]}
                | {"runs": entry["runs"]}
            )
            rows.append(sheet_row(topic, entry, titles, graded))
        print(
            f"{topic['id']}: {sum(1 for p in pooled if p['question_id'] == topic['id'])} "
            "pieces pooled",
            file=sys.stderr,
        )

    runs_dir = OUTPUTS / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    judging.mkdir(parents=True, exist_ok=True)
    for approach, lines in run_lines.items():
        (runs_dir / f"{approach}.trec").write_text("\n".join(lines) + "\n", encoding="utf-8")
    record = {
        "built_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "depth": args.depth,
        "seed": args.seed,
        "approaches": dict(build_index.APPROACHES),
        "embedding_models": {
            approach: build_index.load_index(index)[0]["embedding_model"]
            for approach, index in build_index.APPROACHES.items()
        },
        "grades_carried": len(graded),
        "pieces": len(pooled),
        "pool": pooled,
    }
    (judging / "pool.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    write_sheet(sheet, rows)
    (judging / "sheet.md").write_text(sheet_markdown(read_sheet(sheet)), encoding="utf-8")
    print(f"{len(pooled)} pieces -> {judging / 'sheet.csv'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
