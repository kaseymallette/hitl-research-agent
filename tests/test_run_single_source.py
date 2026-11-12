"""The single-source harness, run against a fake Codex CLI.

The fake is a real executable, so the subprocess boundary is exercised: it
records which files each session could see, then writes, or fails to write,
the call's file as the test's plan says. No Codex session is started.
"""

import importlib.util
import json
import stat
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
HARNESS = REPO_ROOT / "scripts" / "run_single_source.py"
SLUG = "li_et_al_2025_making_ai_less_thirsty"

FAKE_CODEX = """\
import json, os, sys
from pathlib import Path

args = sys.argv[1:]
workspace = Path(args[args.index("--cd") + 1])
label = workspace.name.removeprefix("single_source_").split("-")[0]
files = sorted(str(p.relative_to(workspace)) for p in workspace.rglob("*") if p.is_file())
with open(os.environ["FAKE_RECORD"], "a") as record:
    record.write(json.dumps({
        "label": label,
        "files": files,
        "api_key": "OPENAI_API_KEY" in os.environ,
        "model": args[args.index("--model") + 1],
    }) + "\\n")
step = json.loads(os.environ["FAKE_PLAN"]).get(label, {})
if "write" in step:
    name, content = step["write"]
    (workspace / name).write_text(content)
sys.exit(step.get("exit", 0))
"""

GOOD = {
    "01": {"write": ["01_close_reading.json", '{"reading_plan": "p", "reading_path": []}']},
    "02": {"write": ["02_claims_reference.md", "claims"]},
    "03": {"write": ["03_close_reading_judgment.md", "judgment A"]},
    "04": {"write": ["04_argument_evaluation.md", "evaluation"]},
    "05": {"write": ["05_argument_judgment.md", "judgment B"]},
}


def load_harness() -> ModuleType:
    spec = importlib.util.spec_from_file_location("run_single_source", HARNESS)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module  # dataclasses look their module up here
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def harness(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> ModuleType:
    module = load_harness()
    monkeypatch.setattr(module, "ANALYSES", tmp_path / "analyses")
    monkeypatch.setattr(module, "LOGS", tmp_path / "logs")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-not-real")
    monkeypatch.setenv("FAKE_RECORD", str(tmp_path / "record.jsonl"))
    codex = tmp_path / "codex"
    codex.write_text(f"#!{sys.executable}\n{FAKE_CODEX}")
    codex.chmod(codex.stat().st_mode | stat.S_IEXEC)
    return module


def run(
    harness: ModuleType,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    plan: dict[str, Any],
    *args: str,
) -> int:
    monkeypatch.setenv("FAKE_PLAN", json.dumps(plan))
    result: int = harness.main([SLUG, "--codex", str(tmp_path / "codex"), *args])
    return result


def sessions(tmp_path: Path) -> list[dict[str, Any]]:
    record = tmp_path / "record.jsonl"
    if not record.exists():
        return []
    return [json.loads(line) for line in record.read_text().splitlines()]


def article_dir(tmp_path: Path) -> Path:
    return tmp_path / "analyses" / SLUG


def test_a_full_run_writes_the_five_files_in_order(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert run(harness, tmp_path, monkeypatch, GOOD) == 0
    assert sorted(p.name for p in article_dir(tmp_path).iterdir()) == [
        "01_close_reading.json",
        "02_claims_reference.md",
        "03_close_reading_judgment.md",
        "04_argument_evaluation.md",
        "05_argument_judgment.md",
    ]
    assert [s["label"] for s in sessions(tmp_path)] == ["01", "02", "03", "04", "05"]
    assert all(s["model"] == "gpt-6.1-sol" for s in sessions(tmp_path))


def test_each_session_sees_only_what_its_call_reads(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    run(harness, tmp_path, monkeypatch, GOOD)
    seen = {s["label"]: s["files"] for s in sessions(tmp_path)}
    assert seen["02"] == ["RUBRIC.md", "article.pdf"]
    assert seen["03"] == [
        "01_close_reading.json",
        "02_claims_reference.md",
        "RUBRIC.md",
        "article.pdf",
        "prompts/01_close_reading.md",
    ]
    assert seen["05"] == [
        "04_argument_evaluation.md",
        "RUBRIC.md",
        "article.pdf",
        "prompts/04_argument_evaluation.md",
    ]


def test_no_api_key_reaches_codex(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    run(harness, tmp_path, monkeypatch, GOOD)
    assert not any(s["api_key"] for s in sessions(tmp_path))


def test_a_stopped_run_picks_up_at_the_first_missing_file(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    plan = {**GOOD, "03": {"exit": 1}}
    assert run(harness, tmp_path, monkeypatch, plan) == 1
    assert not (article_dir(tmp_path) / "04_argument_evaluation.md").exists()

    assert run(harness, tmp_path, monkeypatch, GOOD) == 0
    assert [s["label"] for s in sessions(tmp_path)] == ["01", "02", "03", "03", "04", "05"]


def test_only_reruns_one_call_and_overwrites_its_file(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    run(harness, tmp_path, monkeypatch, GOOD)
    plan = {"03": {"write": ["03_close_reading_judgment.md", "judgment A, again"]}}
    assert run(harness, tmp_path, monkeypatch, plan, "--only", "03") == 0
    judgment = article_dir(tmp_path) / "03_close_reading_judgment.md"
    assert judgment.read_text() == "judgment A, again"
    assert [s["label"] for s in sessions(tmp_path)][-1] == "03"


def test_a_call_whose_inputs_are_missing_does_not_start(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert run(harness, tmp_path, monkeypatch, GOOD, "--only", "03") == 1
    assert sessions(tmp_path) == []


def test_revise_edits_the_close_reading_in_place_from_the_judgment(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    run(harness, tmp_path, monkeypatch, GOOD)
    revised = '{"reading_plan": "revised", "reading_path": []}'
    plan = {"01_revise": {"write": ["01_close_reading.json", revised]}}
    assert run(harness, tmp_path, monkeypatch, plan, "--revise", "01") == 0
    assert (article_dir(tmp_path) / "01_close_reading.json").read_text() == revised
    seen = sessions(tmp_path)[-1]["files"]
    assert "03_close_reading_judgment.md" in seen
    assert "04_argument_evaluation.md" not in seen


@pytest.mark.parametrize(
    "step",
    [
        {"exit": 2},
        {},
        {"write": ["01_close_reading.json", "not json {"]},
    ],
    ids=["codex-error", "no-file", "invalid-json"],
)
def test_a_technical_failure_stops_the_run_and_writes_nothing(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, step: dict[str, Any]
) -> None:
    assert run(harness, tmp_path, monkeypatch, {**GOOD, "01": step}) == 1
    assert not (article_dir(tmp_path) / "01_close_reading.json").exists()
    assert [s["label"] for s in sessions(tmp_path)] == ["01"]


def test_a_failed_revision_leaves_the_close_reading_as_it_was(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    run(harness, tmp_path, monkeypatch, GOOD)
    original = (article_dir(tmp_path) / "01_close_reading.json").read_text()
    plan = {"01_revise": {"write": ["01_close_reading.json", "broken {"]}}
    assert run(harness, tmp_path, monkeypatch, plan, "--revise", "01") == 1
    assert (article_dir(tmp_path) / "01_close_reading.json").read_text() == original


def test_every_call_reads_its_request_from_its_prompt_file() -> None:
    """prompts/ holds exactly what each session is sent, so a call can be run
    by hand by pasting the same file."""
    harness = load_harness()
    calls = [*harness.CALLS.values(), *harness.REVISIONS.values()]
    assert sorted(call.prompt for call in calls) == sorted(
        p.name for p in (REPO_ROOT / "prompts").glob("*.md")
    )
    for call in calls:
        assert call.request == (REPO_ROOT / "prompts" / call.prompt).read_text(encoding="utf-8")
