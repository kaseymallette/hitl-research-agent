"""The scholarly harness, run against a fake Codex CLI.

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
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
PROMPTS = REPO_ROOT / "studies" / "science_of_reading" / "harness" / "scholarly" / "prompts"
HARNESS = REPO_ROOT / "scripts" / "run_scholarly.py"
SLUG = "author_2020_an_article"

FAKE_CODEX = """\
import json, os, sys
from pathlib import Path

args = sys.argv[1:]
workspace = Path(args[args.index("--cd") + 1])
label = workspace.name.removeprefix("scholarly_").split("-")[0]
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
    "01": {"write": ["01_claims_reference.md", "claims"]},
    "02": {"write": ["02_baseline_answers.md", "baseline"]},
    "03": {"write": ["03_close_reading.json", '{"reading_plan": "p", "reading_path": []}']},
    "04": {"write": ["04_close_reading_answers.md", "close reading answers"]},
    "05": {"write": ["05_scoring.md", "scoring"]},
}


def load_harness() -> ModuleType:
    spec = importlib.util.spec_from_file_location("run_scholarly", HARNESS)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module  # dataclasses look their module up here
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def harness(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> ModuleType:
    module = load_harness()
    # The real articles stay local, so the study is a temporary one with a stand-in PDF.
    study = tmp_path / "study"
    (study / "data" / "scholarly").mkdir(parents=True)
    (study / "data" / "scholarly" / f"{SLUG}.pdf").write_bytes(b"%PDF-1.4 stand-in")
    sources = study / "data" / "scholarly" / "sources.yaml"
    sources.write_text(
        yaml.safe_dump(
            {
                "sources": [
                    {
                        "slug": SLUG,
                        "pdf": f"data/scholarly/{SLUG}.pdf",
                        "source_title": "An Article",
                        "source_type": "peer_reviewed_paper",
                        "publisher": "A Journal",
                        "doi": None,
                    }
                ]
            }
        )
    )
    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(module, "STUDY", study)
    monkeypatch.setattr(module, "SOURCES", sources)
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
        "01_claims_reference.md",
        "02_baseline_answers.md",
        "03_close_reading.json",
        "04_close_reading_answers.md",
        "05_scoring.md",
    ]
    assert [s["label"] for s in sessions(tmp_path)] == ["01", "02", "03", "04", "05"]
    assert all(s["model"] == "gpt-6.1-sol" for s in sessions(tmp_path))


def test_each_session_sees_only_what_its_call_reads(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    run(harness, tmp_path, monkeypatch, GOOD)
    seen = {s["label"]: s["files"] for s in sessions(tmp_path)}
    assert seen["01"] == ["article.pdf", "source.yaml"]
    assert seen["02"] == ["article.pdf", "source.yaml"]
    assert seen["03"] == ["article.pdf", "source.yaml"]
    assert seen["04"] == ["03_close_reading.json", "article.pdf", "source.yaml"]
    assert seen["05"] == [
        "01_claims_reference.md",
        "02_baseline_answers.md",
        "04_close_reading_answers.md",
        "article.pdf",
        "source.yaml",
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
    assert not (article_dir(tmp_path) / "04_close_reading_answers.md").exists()

    assert run(harness, tmp_path, monkeypatch, GOOD) == 0
    assert [s["label"] for s in sessions(tmp_path)] == ["01", "02", "03", "03", "04", "05"]


def test_only_reruns_one_call_and_overwrites_its_file(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    run(harness, tmp_path, monkeypatch, GOOD)
    plan = {"05": {"write": ["05_scoring.md", "scoring, again"]}}
    assert run(harness, tmp_path, monkeypatch, plan, "--only", "05") == 0
    assert (article_dir(tmp_path) / "05_scoring.md").read_text() == "scoring, again"
    assert [s["label"] for s in sessions(tmp_path)][-1] == "05"


def test_a_call_whose_inputs_are_missing_does_not_start(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert run(harness, tmp_path, monkeypatch, GOOD, "--only", "04") == 1
    assert sessions(tmp_path) == []


@pytest.mark.parametrize(
    "step",
    [
        {"exit": 2},
        {},
        {"write": ["03_close_reading.json", "not json {"]},
    ],
    ids=["codex-error", "no-file", "invalid-json"],
)
def test_a_technical_failure_stops_the_run_and_writes_nothing(
    harness: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, step: dict[str, Any]
) -> None:
    assert run(harness, tmp_path, monkeypatch, {**GOOD, "03": step}) == 1
    assert not (article_dir(tmp_path) / "03_close_reading.json").exists()
    assert [s["label"] for s in sessions(tmp_path)] == ["01", "02", "03"]


def test_every_call_reads_its_request_from_its_prompt_file() -> None:
    """prompts/ holds exactly what each session is sent, so a call can be run
    by hand by pasting the same file."""
    harness = load_harness()
    calls = list(harness.CALLS.values())
    assert sorted(call.prompt for call in calls) == sorted(p.name for p in PROMPTS.glob("*.md"))
    for call in calls:
        assert call.request == (PROMPTS / call.prompt).read_text(encoding="utf-8")
