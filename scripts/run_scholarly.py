#!/usr/bin/env python
"""Run the scholarly harness for one article in Codex: five calls, five files.

    uv run python scripts/run_scholarly.py <slug>
    uv run python scripts/run_scholarly.py <slug> --only 03

The article is the `<slug>` entry in
`studies/science_of_reading/data/scholarly/sources.yaml`. Each call is its own
Codex session (`codex exec`) on GPT-6.1 Sol at medium effort, billed through
the API using OPENAI_API_KEY (or CODEX_API_KEY), and writes one file to
`studies/science_of_reading/outputs/scholarly/<slug>/`:

    01_claims_reference.md        every claim in the article, quoted: the answer key
    02_baseline_answers.md        Method A, Baseline: the questions from the article alone
    03_close_reading.json         Method B: the close reading, quoted, for the questions
    04_close_reading_answers.md   Method B, Close Reading: the questions from the article and 03
    05_scoring.md                 02 and 04 scored against 01 for recall and precision

With no option, the calls whose file is missing run in order, so a stopped run
picks up where it left off. `--only` reruns one call and overwrites its file.

Each call's request is its file in `harness/scholarly/prompts/`, so a call can
be run by hand by pasting the same file. Each session runs in a temporary
folder holding only the files that call reads, so 01 and 02 never see the
close reading. Only a technical failure stops a run: Codex exiting with an error or
timing out, the call's file not written, or a close reading that does not
parse as JSON. Codex's event log and final message for each call go to
`.codex_runs/<slug>/`, which git ignores.
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
STUDY = REPO_ROOT / "studies" / "science_of_reading"
# The scholarly harness's prompts.
PROMPTS = STUDY / "harness" / "scholarly" / "prompts"
SOURCES = STUDY / "data" / "scholarly" / "sources.yaml"
ANALYSES = STUDY / "outputs" / "scholarly"
LOGS = REPO_ROOT / ".codex_runs"
APP_CODEX = Path("/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex")

MODEL = "gpt-6.1-sol"
EFFORT = "medium"
TIMEOUT_SECONDS = 60 * 60

SOURCE_FIELDS = ("source_title", "source_type", "publisher", "doi")

CLAIMS_REFERENCE = "01_claims_reference.md"
BASELINE_ANSWERS = "02_baseline_answers.md"
CLOSE_READING = "03_close_reading.json"
CLOSE_READING_ANSWERS = "04_close_reading_answers.md"
SCORING = "05_scoring.md"


@dataclass(frozen=True)
class Call:
    label: str
    output: str
    reads: tuple[str, ...]
    prompt: str  # file in prompts/ whose text is the session's request

    @property
    def request(self) -> str:
        return (PROMPTS / self.prompt).read_text(encoding="utf-8")


CALLS = {
    "01": Call("01", CLAIMS_REFERENCE, ("article.pdf", "source.yaml"), "01_claims_reference.md"),
    "02": Call("02", BASELINE_ANSWERS, ("article.pdf", "source.yaml"), "02_baseline_answers.md"),
    "03": Call("03", CLOSE_READING, ("article.pdf", "source.yaml"), "03_close_reading.md"),
    "04": Call(
        "04",
        CLOSE_READING_ANSWERS,
        ("article.pdf", "source.yaml", CLOSE_READING),
        "04_close_reading_answers.md",
    ),
    "05": Call(
        "05",
        SCORING,
        ("article.pdf", "source.yaml", CLAIMS_REFERENCE, BASELINE_ANSWERS, CLOSE_READING_ANSWERS),
        "05_scoring.md",
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
            shutil.copyfile(STUDY / entry["pdf"], target)
        elif name == "source.yaml":
            fields = {field: entry.get(field) for field in SOURCE_FIELDS}
            target.write_text(yaml.safe_dump(fields, sort_keys=False), encoding="utf-8")
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
    api_key = (
        os.environ.get("OPENAI_API_KEY", "").strip() or os.environ.get("CODEX_API_KEY", "").strip()
    )
    if not api_key:
        raise CallFailed("Set OPENAI_API_KEY (or CODEX_API_KEY) to run with API billing")
    # CODEX_API_KEY overrides saved ChatGPT authentication for this invocation.
    env = dict(os.environ)
    env.pop("OPENAI_API_KEY", None)
    env.pop("CODEX_ACCESS_TOKEN", None)
    env["CODEX_API_KEY"] = api_key
    log_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"scholarly_{call.label}-") as tmp:
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


def calls_to_run(only: str | None, article_dir: Path) -> list[Call]:
    if only is not None:
        return [CALLS[only]]
    return [call for call in CALLS.values() if not (article_dir / call.output).exists()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("slug", help="the article's slug in data/scholarly/sources.yaml")
    parser.add_argument("--only", choices=sorted(CALLS), help="rerun one call")
    parser.add_argument("--codex", type=Path, help="path to the Codex CLI")
    args = parser.parse_args(argv)

    entry = source_entry(args.slug)
    article_dir = ANALYSES / args.slug
    calls = calls_to_run(args.only, article_dir)
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
