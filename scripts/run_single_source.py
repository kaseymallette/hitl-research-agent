#!/usr/bin/env python
"""Run single-source analysis for one article in Codex: five calls, five files.

    uv run python scripts/run_single_source.py <slug>
    uv run python scripts/run_single_source.py <slug> --only 03
    uv run python scripts/run_single_source.py <slug> --revise 01

The article is the `<slug>` entry in `data/research/sources.yaml`. Each call is
its own Codex session (`codex exec`) on GPT-6.1 Sol at medium effort (ADR-0021),
signed in with ChatGPT rather than an API key, and writes one file to
`outputs/analyses/<slug>/` (ADR-0022):

    01_close_reading.json          the close reading
    02_claims_reference.md         the article's own claims, from the article alone
    03_close_reading_judgment.md   01 judged against the article and 02, on A1-A5
    04_argument_evaluation.md      the argument evaluation, from the article and 01
    05_argument_judgment.md        04 judged against the article alone, on B1-B6

With no option, the calls whose file is missing run in order, so a stopped run
picks up where it left off. `--only` reruns one call and overwrites its file.
`--revise 01` edits the close reading in place from 03's judgment, and
`--revise 04` the argument evaluation from 05's; commit first if you want the
earlier version, then rerun the judgment with `--only`.

Each session runs in a temporary folder holding only the files that call reads,
so no session can see another's judgment. Only a technical failure stops a run:
Codex exiting with an error or timing out, the call's file not written, or a
close reading that does not parse as JSON (ADR-0005). Codex's event log and
final message for each call go to `.codex_runs/<slug>/`, which git ignores.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCES = REPO_ROOT / "data" / "research" / "sources.yaml"
ANALYSES = REPO_ROOT / "outputs" / "analyses"
LOGS = REPO_ROOT / ".codex_runs"
APP_CODEX = Path("/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex")

MODEL = "gpt-6.1-sol"
EFFORT = "medium"
TIMEOUT_SECONDS = 60 * 60

# Repository files a session may be given, under the name it sees them by.
REPO_FILES = {
    "RUBRIC.md": REPO_ROOT / "docs" / "RUBRIC.md",
    "prompts/close-reading.md": REPO_ROOT / "prompts" / "close-reading.md",
    "prompts/evaluate-argument.md": REPO_ROOT / "prompts" / "evaluate-argument.md",
}
SOURCE_FIELDS = ("source_title", "source_type", "publisher", "doi")

CLOSE_READING = "01_close_reading.json"
CLAIMS_REFERENCE = "02_claims_reference.md"
CLOSE_READING_JUDGMENT = "03_close_reading_judgment.md"
ARGUMENT_EVALUATION = "04_argument_evaluation.md"
ARGUMENT_JUDGMENT = "05_argument_judgment.md"


@dataclass(frozen=True)
class Call:
    label: str
    output: str
    reads: tuple[str, ...]
    request: str


CALLS = {
    "01": Call(
        "01",
        CLOSE_READING,
        ("article.pdf", "source.yaml", "prompts/close-reading.md"),
        "Follow prompts/close-reading.md. The files it names are in this folder.",
    ),
    "02": Call(
        "02",
        CLAIMS_REFERENCE,
        ("article.pdf", "RUBRIC.md"),
        """\
Hi! You're writing a reference list for judging a close reading of an
academic article. Please start by reading RUBRIC.md, which explains the
setup, and especially its section "The claims reference list".

This session reads article.pdf on its own and writes the article's own claims
to 02_claims_reference.md, as the rubric describes. A later session judges the
close reading against your list as written, so take care that it's complete:
cover the conclusion of every section and subsection, not only the article's
summary claims, along with every contribution, abstract claim, figure, and
table.

Please open only RUBRIC.md and article.pdf.""",
    ),
    "03": Call(
        "03",
        CLOSE_READING_JUDGMENT,
        (
            "article.pdf",
            "RUBRIC.md",
            "prompts/close-reading.md",
            CLAIMS_REFERENCE,
            CLOSE_READING,
        ),
        """\
Hi! You're judging a close reading of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the reading followed.

Read article.pdf and 02_claims_reference.md, the reference list an earlier
session wrote from the article. Use it as written; don't change it.

Then open 01_close_reading.json and judge it against the article and the list
on A1-A5. Write the judgment to 03_close_reading_judgment.md.

Please open only these files.""",
    ),
    "04": Call(
        "04",
        ARGUMENT_EVALUATION,
        ("article.pdf", "source.yaml", "prompts/evaluate-argument.md", CLOSE_READING),
        "Follow prompts/evaluate-argument.md. The files it names are in this folder.",
    ),
    "05": Call(
        "05",
        ARGUMENT_JUDGMENT,
        ("article.pdf", "RUBRIC.md", "prompts/evaluate-argument.md", ARGUMENT_EVALUATION),
        """\
Hi! You're judging an evaluation of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluation
followed.

Read article.pdf, then open 04_argument_evaluation.md and judge it against
the article on B1-B6. There is no reference list for this session: check each
problem the evaluation raises against the article itself. Write the judgment
to 05_argument_judgment.md.

Please open only these files.""",
    ),
}

REVISIONS = {
    "01": Call(
        "01_revise",
        CLOSE_READING,
        (
            "article.pdf",
            "source.yaml",
            "RUBRIC.md",
            "prompts/close-reading.md",
            CLAIMS_REFERENCE,
            CLOSE_READING,
            CLOSE_READING_JUDGMENT,
        ),
        """\
Hi! You're revising a close reading of an academic article. Please start by
reading prompts/close-reading.md, which holds the instructions the reading
followed, and RUBRIC.md, which holds the criteria it was judged on.

03_close_reading_judgment.md judges 01_close_reading.json against article.pdf
and 02_claims_reference.md. Check each problem the judgment raises against the
article itself. Where the article bears it out, fix it in
01_close_reading.json; where it doesn't, leave that part as it is. Change
nothing the judgment didn't raise, and keep the JSON in the same shape. Edit
01_close_reading.json in place.

In your final message, list what you changed, and each point of the judgment
you left alone and why.

Please open only these files.""",
    ),
    "04": Call(
        "04_revise",
        ARGUMENT_EVALUATION,
        (
            "article.pdf",
            "source.yaml",
            "RUBRIC.md",
            "prompts/evaluate-argument.md",
            CLOSE_READING,
            ARGUMENT_EVALUATION,
            ARGUMENT_JUDGMENT,
        ),
        """\
Hi! You're revising an evaluation of an academic article's argument. Please
start by reading prompts/evaluate-argument.md, which holds the instructions
the evaluation followed, and RUBRIC.md, which holds the criteria it was
judged on.

05_argument_judgment.md judges 04_argument_evaluation.md against article.pdf.
Check each problem the judgment raises against the article itself. Where the
article bears it out, fix it in 04_argument_evaluation.md; where it doesn't,
leave that part as it is. Change nothing the judgment didn't raise. The
evaluation stays your own judgment of the argument, in prose. Edit
04_argument_evaluation.md in place.

In your final message, list what you changed, and each point of the judgment
you left alone and why.

Please open only these files.""",
    ),
}


class CallFailed(Exception):
    """A technical failure: the call produced no usable file."""


def source_entry(slug: str) -> dict[str, Any]:
    manifest = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    for entry in manifest["sources"]:
        if entry["slug"] == slug:
            return dict(entry)
    raise SystemExit(f"{slug} is not in {SOURCES.relative_to(REPO_ROOT)}")


def stage(call: Call, entry: dict[str, Any], article_dir: Path, workspace: Path) -> None:
    """Put exactly the files the call reads into its workspace."""
    for name in call.reads:
        target = workspace / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if name == "article.pdf":
            shutil.copyfile(REPO_ROOT / entry["pdf"], target)
        elif name == "source.yaml":
            fields = {field: entry.get(field) for field in SOURCE_FIELDS}
            target.write_text(yaml.safe_dump(fields, sort_keys=False), encoding="utf-8")
        elif name in REPO_FILES:
            shutil.copyfile(REPO_FILES[name], target)
        else:
            shutil.copyfile(article_dir / name, target)


def missing_inputs(call: Call, article_dir: Path) -> list[str]:
    earlier = (name for name in call.reads if name[:2].isdigit())
    return [name for name in earlier if not (article_dir / name).exists()]


def codex_command(codex: Path, workspace: Path, message_file: Path, request: str) -> list[str]:
    return [
        str(codex),
        "exec",
        "--model",
        MODEL,
        "--config",
        f'model_reasoning_effort="{EFFORT}"',
        "--ignore-user-config",
        "--sandbox",
        "workspace-write",
        "--skip-git-repo-check",
        "--cd",
        str(workspace),
        "--json",
        "--output-last-message",
        str(message_file),
        request,
    ]


def run_call(
    call: Call, entry: dict[str, Any], article_dir: Path, codex: Path, log_dir: Path
) -> None:
    """Run one Codex session and copy its file into the article's folder."""
    log_dir.mkdir(parents=True, exist_ok=True)
    # No API key reaches Codex, so it runs on the ChatGPT sign-in and is never billed per token.
    env = {key: value for key, value in os.environ.items() if key != "OPENAI_API_KEY"}
    with tempfile.TemporaryDirectory(prefix=f"single_source_{call.label}-") as tmp:
        workspace = Path(tmp)
        stage(call, entry, article_dir, workspace)
        message_file = log_dir / f"{call.label}_message.md"
        command = codex_command(codex, workspace, message_file, call.request)
        with (log_dir / f"{call.label}.jsonl").open("w", encoding="utf-8") as log:
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
        produced = workspace / call.output
        if not produced.is_file():
            raise CallFailed(f"Codex did not write {call.output}")
        if produced.suffix == ".json":
            try:
                json.loads(produced.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as error:
                raise CallFailed(f"{call.output} is not valid JSON: {error}") from error
        article_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(produced, article_dir / call.output)


def find_codex(given: Path | None) -> Path:
    if given is not None:
        return given
    on_path = shutil.which("codex")
    if on_path is not None:
        return Path(on_path)
    if APP_CODEX.exists():
        return APP_CODEX
    raise SystemExit("Codex CLI not found: put `codex` on PATH or pass --codex")


def calls_to_run(only: str | None, revise: str | None, article_dir: Path) -> list[Call]:
    if revise is not None:
        return [REVISIONS[revise]]
    if only is not None:
        return [CALLS[only]]
    return [call for call in CALLS.values() if not (article_dir / call.output).exists()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("slug", help="the article's slug in data/research/sources.yaml")
    choice = parser.add_mutually_exclusive_group()
    choice.add_argument("--only", choices=sorted(CALLS), help="rerun one call")
    choice.add_argument("--revise", choices=sorted(REVISIONS), help="revise 01 or 04 in place")
    parser.add_argument("--codex", type=Path, help="path to the Codex CLI")
    args = parser.parse_args(argv)

    entry = source_entry(args.slug)
    article_dir = ANALYSES / args.slug
    calls = calls_to_run(args.only, args.revise, article_dir)
    if not calls:
        print(f"All five files are already in {article_dir.relative_to(REPO_ROOT)}.")
        return 0
    codex = find_codex(args.codex)
    log_dir = LOGS / args.slug

    for call in calls:
        missing = missing_inputs(call, article_dir)
        if missing:
            print(f"{call.label} needs {', '.join(missing)}; run that call first.", file=sys.stderr)
            return 1
        print(f"{datetime.now():%H:%M} {call.label}: running, writes {call.output}", flush=True)
        try:
            run_call(call, entry, article_dir, codex, log_dir)
        except CallFailed as error:
            log = log_dir / f"{call.label}.jsonl"
            print(f"{call.label} failed: {error}. Log: {log}", file=sys.stderr)
            return 1
        print(f"{datetime.now():%H:%M} {call.label}: done", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
