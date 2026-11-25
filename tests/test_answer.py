"""scripts/answer.py: the budget, retrieved.md, the record, and a run against a fake Codex.

The fake Codex is a real executable, so the subprocess boundary is exercised; retrieval
is replaced by a fixed ranking, so no index or embedding model is needed.
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
SCRIPTS = REPO_ROOT / "scripts"


def load_script() -> ModuleType:
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))  # answer.py imports its sibling scripts
    spec = importlib.util.spec_from_file_location("answer", SCRIPTS / "answer.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ans = load_script()


def chunk(cid: str, tokens: int, kind: str = "source_text", **extra: Any) -> dict[str, Any]:
    slug = cid.split("#")[0]
    return {
        "id": cid,
        "slug": slug,
        "kind": kind,
        "tokens": tokens,
        "text": f"text of {cid}",
        **extra,
    }


def test_project_md_has_the_ten_research_questions() -> None:
    questions = ans.research_questions((REPO_ROOT / "docs" / "PROJECT.md").read_text())
    assert sorted(questions) == list(range(1, 11))
    assert all("\n" not in q and q.endswith("?") for q in questions.values())


def test_research_questions_stop_at_the_next_heading() -> None:
    md = (
        "### Research questions\n\nIntro.\n\n1. First\n   wraps?\n2. Second?\n\n"
        "### Steps\n\n1. Not a question\n"
    )
    assert ans.research_questions(md) == {1: "First wraps?", 2: "Second?"}
    with pytest.raises(ValueError):
        ans.research_questions("# Nothing here\n")


@pytest.mark.parametrize(
    ("budget", "kept"),
    [
        (0, []),
        (99, []),
        (100, ["a"]),
        (250, ["a", "b"]),
        (349, ["a", "b"]),
        (10_000, ["a", "b", "c", "d"]),
    ],
)
def test_within_budget_keeps_rank_order_and_stops_at_the_first_overflow(
    budget: int, kept: list[str]
) -> None:
    ranked = [
        (0.9, chunk("a#0", 100)),
        (0.8, chunk("b#0", 150)),
        (0.7, chunk("c#0", 300)),
        (0.6, chunk("d#0", 10)),
    ]
    assert [c["slug"] for _, c in ans.within_budget(ranked, budget)] == kept


SOURCES = {
    "li_et_al_2025_x": {
        "slug": "li_et_al_2025_x",
        "source_title": "Thirsty",
        "source_authors": ["Pengfei Li", "Shaolei Ren"],
        "publisher": "ACM",
    },
    "ceres_2026_y": {"slug": "ceres_2026_y", "source_title": "Watts", "publisher": "Ceres"},
}


def test_render_retrieved_labels_items_in_rank_order_with_kind_and_pages() -> None:
    items = [
        (0.9, chunk("li_et_al_2025_x#003", 5, pdf_pages=[2, 3])),
        (0.8, chunk("ceres_2026_y#04-001", 5, kind="argument_evaluation")),
    ]
    text = ans.render_retrieved("Why water?", items, SOURCES)
    assert text.startswith("# Question\n\nWhy water?\n")
    assert "- ceres_2026_y: Ceres (2026). Watts. Ceres." in text
    assert "- li_et_al_2025_x: Pengfei Li, Shaolei Ren (2025). Thirsty. ACM." in text
    assert (
        "## [E1] li_et_al_2025_x: article text, PDF p. 2, 3\n\ntext of li_et_al_2025_x#003" in text
    )
    assert "## [E2] ceres_2026_y: argument evaluation\n\ntext of ceres_2026_y#04-001" in text
    assert text.index("[E1]") < text.index("[E2]")


def test_citations_count_known_labels_and_report_the_rest() -> None:
    answer = "One [E1]. Two [E1, E3]. Bad [E9]. Not a citation: E2."
    assert ans.citations(answer, 3) == {
        "cited": {"E1": 2, "E3": 1},
        "not_cited": ["E2"],
        "unknown": ["E9"],
    }
    assert ans.citations("No citations.", 2) == {
        "cited": {},
        "not_cited": ["E1", "E2"],
        "unknown": [],
    }


def test_usage_from_log_sums_turns_and_skips_plain_text() -> None:
    log = "\n".join(
        [
            "Reading additional input from stdin...",
            json.dumps({"type": "thread.started"}),
            json.dumps(
                {"type": "turn.completed", "usage": {"input_tokens": 10, "output_tokens": 2}}
            ),
            json.dumps(
                {"type": "turn.completed", "usage": {"input_tokens": 5, "output_tokens": 1}}
            ),
        ]
    )
    assert ans.usage_from_log(log) == {"input_tokens": 15, "output_tokens": 3}
    assert ans.usage_from_log("plain\n") is None


FAKE_CODEX = """\
import json, os, sys
from pathlib import Path

args = sys.argv[1:]
workspace = Path(args[args.index("--cd") + 1])
files = sorted(p.name for p in workspace.iterdir())
Path(os.environ["FAKE_RECORD"]).write_text(json.dumps({
    "files": files,
    "api_key": "OPENAI_API_KEY" in os.environ,
    "model": args[args.index("--model") + 1],
    "request": args[-1],
}))
print(json.dumps({"type": "turn.completed", "usage": {"input_tokens": 7, "output_tokens": 3}}))
if os.environ.get("FAKE_WRITE") == "1":
    (workspace / "answer.md").write_text("Freshwater is used [E1], per an evaluation [E2] [E5].")
sys.exit(int(os.environ.get("FAKE_EXIT", "0")))
"""

RANKED = [
    (0.91, chunk("li_et_al_2025_x#000", 300, pdf_pages=[1])),
    (0.85, chunk("ceres_2026_y#04-000", 300, kind="argument_evaluation")),
    (0.80, chunk("li_et_al_2025_x#001", 300, pdf_pages=[2])),
]


@pytest.fixture
def harness(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(ans, "ANSWERS", tmp_path / "answers")
    monkeypatch.setattr(ans, "ANSWER_LOGS", tmp_path / "logs")
    monkeypatch.setattr(ans, "retrieve", lambda approach, question: RANKED)
    index_root = tmp_path / "index"
    for name in ("source_text", "analyses"):
        (index_root / name).mkdir(parents=True)
        (index_root / name / "index.json").write_text(json.dumps({"built_at": "t", "chunks": 3}))
    monkeypatch.setattr(ans, "INDEX_ROOT", index_root)
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-not-real")
    monkeypatch.setenv("FAKE_RECORD", str(tmp_path / "seen.json"))
    codex = tmp_path / "codex"
    codex.write_text(f"#!{sys.executable}\n{FAKE_CODEX}")
    codex.chmod(codex.stat().st_mode | stat.S_IEXEC)
    return codex


def test_answer_writes_the_answer_and_its_record(
    harness: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("FAKE_WRITE", "1")
    out = ans.answer_one(3, "Why water?", "structured", 650, SOURCES, harness)
    assert out == tmp_path / "answers" / "structured" / "q03"
    seen = json.loads((tmp_path / "seen.json").read_text())
    assert seen["files"] == ["retrieved.md"]
    assert seen["api_key"] is False
    assert seen["model"] == ans.MODEL
    assert seen["request"] == ans.PROMPT.read_text(encoding="utf-8")

    assert (out / "answer.md").read_text().startswith("Freshwater is used [E1]")
    record = json.loads((out / "record.json").read_text())
    assert record["question_number"] == 3 and record["approach"] == "structured"
    assert record["budget_tokens"] == 650 and record["retrieved_tokens"] == 600
    assert [(r["label"], r["id"], r["kind"]) for r in record["retrieved"]] == [
        ("E1", "li_et_al_2025_x#000", "source_text"),
        ("E2", "ceres_2026_y#04-000", "argument_evaluation"),
    ]
    assert record["citations"] == {"cited": {"E1": 1, "E2": 1}, "not_cited": [], "unknown": ["E5"]}
    assert record["usage"] == {"input_tokens": 7, "output_tokens": 3}
    assert record["cost"]["usd"] is None
    assert set(record["indexes"]) == {"analyses"}
    retrieved = (tmp_path / "logs" / "structured" / "q03" / "retrieved.md").read_text()
    assert "[E2]" in retrieved and "[E3]" not in retrieved


def test_dry_run_writes_retrieved_md_and_runs_no_codex(harness: Path, tmp_path: Path) -> None:
    out = ans.answer_one(1, "Why water?", "rag", 4000, SOURCES, None)
    assert out == tmp_path / "logs" / "rag" / "q01" / "retrieved.md"
    assert "[E3]" in out.read_text()
    assert not (tmp_path / "seen.json").exists()
    assert not (tmp_path / "answers").exists()


@pytest.mark.parametrize(
    ("write", "exit_code", "message"), [("0", "0", "did not write"), ("1", "2", "status 2")]
)
def test_technical_failures_stop_without_writing_an_answer(
    harness: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    write: str,
    exit_code: str,
    message: str,
) -> None:
    monkeypatch.setenv("FAKE_WRITE", write)
    monkeypatch.setenv("FAKE_EXIT", exit_code)
    with pytest.raises(ans.CallFailed, match=message):
        ans.answer_one(1, "Why water?", "structured", 4000, SOURCES, harness)
    assert not (tmp_path / "answers").exists()


def test_main_skips_answers_already_written(
    harness: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    existing = tmp_path / "answers" / "structured" / "q02" / "answer.md"
    existing.parent.mkdir(parents=True)
    existing.write_text("kept")
    assert (
        ans.main(["--questions", "2", "--approaches", "structured", "--codex", str(harness)]) == 0
    )
    assert existing.read_text() == "kept"
    assert not (tmp_path / "seen.json").exists()
