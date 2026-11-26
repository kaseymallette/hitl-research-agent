"""scripts/pool.py: TREC run lines, depth-k pooling, and the blind judging sheet.

Retrieval is replaced by fixed rankings, so no index or embedding model is needed.
"""

import csv
import importlib.util
import json
import random
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load_script() -> ModuleType:
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))  # pool.py imports build_index
    spec = importlib.util.spec_from_file_location("pool", SCRIPTS / "pool.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pool = load_script()


def piece(pid: str, text: str = "") -> dict[str, Any]:
    default = "passage " + pid.replace("#", " ")
    return {"id": pid, "slug": pid.split("#")[0], "text": text or default}


RAG = [(0.9, piece("a#001")), (0.8, piece("a#002")), (0.7, piece("b#001"))]
STRUCTURED = [(0.95, piece("a#01-001")), (0.6, piece("b#02-003"))]


def test_trec_lines_rank_from_one_in_order() -> None:
    assert pool.trec_lines("E01", RAG, "rag") == [
        "E01 Q0 a#001 1 0.900000 rag",
        "E01 Q0 a#002 2 0.800000 rag",
        "E01 Q0 b#001 3 0.700000 rag",
    ]
    assert pool.trec_lines("E01", [], "rag") == []


def test_pool_is_the_union_with_unique_codes() -> None:
    entries = pool.pool("C02", {"rag": RAG, "structured": STRUCTURED}, random.Random(1))
    assert sorted(e["piece"]["id"] for e in entries) == sorted(p["id"] for _, p in RAG + STRUCTURED)
    assert [e["code"] for e in entries] == [f"C02-{n:02d}" for n in range(1, 6)]


def test_pool_order_is_seeded() -> None:
    def order(seed: int) -> list[str]:
        runs = {"rag": RAG, "structured": STRUCTURED}
        return [e["piece"]["id"] for e in pool.pool("E01", runs, random.Random(seed))]

    assert order(7) == order(7)
    assert len({tuple(order(s)) for s in range(10)}) > 1


def test_a_piece_in_both_runs_is_pooled_once_with_both_ranks() -> None:
    shared = piece("a#001")
    runs = {"rag": [(0.9, shared)], "structured": [(0.5, piece("x#01-001")), (0.4, shared)]}
    entries = pool.pool("S01", runs, random.Random(1))
    assert len(entries) == 2
    both = next(e for e in entries if e["piece"]["id"] == "a#001")
    assert both["runs"] == {
        "rag": {"rank": 1, "score": 0.9},
        "structured": {"rank": 2, "score": 0.4},
    }


def test_main_writes_runs_pool_and_a_blind_sheet(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    topics = tmp_path / "topics.yaml"
    topics.write_text(
        "topics:\n"
        "  - {id: E01, kind: explicit, question: Q one, relevant: R1, not_relevant: N1}\n"
        "  - {id: S01, kind: synthesis, question: Q two, relevant: R2, not_relevant: N2}\n",
        encoding="utf-8",
    )
    sources = tmp_path / "sources.yaml"
    sources.write_text(
        "sources:\n"
        "  - {slug: a, source_title: Article A}\n"
        "  - {slug: b, source_title: Article B}\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(pool, "TOPICS", topics)
    monkeypatch.setattr(pool, "SOURCES", sources)
    monkeypatch.setattr(pool, "OUTPUTS", tmp_path / "outputs")
    ranked = {"rag": RAG, "structured": STRUCTURED}
    calls: list[tuple[str, str, int]] = []

    def fake_retrieve(approach: str, question: str, k: int) -> list[Any]:
        calls.append((approach, question, k))
        return ranked[approach][:k]

    monkeypatch.setattr(pool.build_index, "retrieve", fake_retrieve)
    monkeypatch.setattr(pool.build_index, "use_study", lambda name: None)
    monkeypatch.setattr(
        pool.build_index, "load_index", lambda name: ({"embedding_model": f"m-{name}"}, [], None)
    )

    assert pool.main(["--depth", "2", "--seed", "3"]) == 0

    assert calls == [
        ("rag", "Q one", 2),
        ("structured", "Q one", 2),
        ("rag", "Q two", 2),
        ("structured", "Q two", 2),
    ]
    rag_run = (tmp_path / "outputs" / "runs" / "rag.trec").read_text(encoding="utf-8")
    assert rag_run.splitlines()[0] == "E01 Q0 a#001 1 0.900000 rag"
    assert len(rag_run.splitlines()) == 4

    record = json.loads((tmp_path / "outputs" / "judging" / "pool.json").read_text())
    assert (record["depth"], record["seed"], record["pieces"]) == (2, 3, 8)
    assert record["embedding_models"] == {"rag": "m-source_text", "structured": "m-analyses"}

    with (tmp_path / "outputs" / "judging" / "sheet.csv").open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert list(rows[0]) == list(pool.SHEET_COLUMNS)
    assert [r["question_id"] for r in rows] == ["E01"] * 4 + ["S01"] * 4
    assert {r["article"] for r in rows} == {"Article A", "Article B"}
    assert all(r["grade"] == "" for r in rows)
    sheet = (tmp_path / "outputs" / "judging" / "sheet.csv").read_text(encoding="utf-8-sig")
    for hidden in ("rag", "structured", "0.9", "#"):
        assert hidden not in sheet  # no approach, score, or piece ID on the sheet
    markdown = (tmp_path / "outputs" / "judging" / "sheet.md").read_text(encoding="utf-8")
    assert markdown.count("### ") == 8
    for hidden in ("rag", "structured", "0.9", "#0", "#1"):
        assert hidden not in markdown.replace("# Grading", "")


ROW = {
    "question": "Q one",
    "relevant": "R1",
    "not_relevant": "N1",
    "article": "Article A",
    "grade": "",
    "note": "",
}


def test_sheet_markdown_gives_each_question_its_criteria_once() -> None:
    rows = [
        ROW | {"piece": "E01-01", "question_id": "E01", "text": "first line\n\nsecond"},
        ROW | {"piece": "E01-02", "question_id": "E01", "text": "other"},
        ROW | {"piece": "S01-01", "question_id": "S01", "question": "Q two", "text": "t"},
    ]
    md = pool.sheet_markdown(rows)
    assert md.count("## E01. Q one") == 1
    assert md.count("**Relevant:** R1") == 2  # once per question
    assert md.index("### E01-01") < md.index("### E01-02") < md.index("## S01. Q two")
    assert "> first line\n>\n> second" in md


def write_sheet(path: Path, grade: str) -> None:
    path.parent.mkdir(parents=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(pool.SHEET_COLUMNS)
        writer.writerow(["E01-01", "E01", "Q one", "R1", "N1", "Article A", "text", grade, ""])


def test_markdown_option_leaves_the_csv_untouched(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(pool, "OUTPUTS", tmp_path)
    sheet = tmp_path / "judging" / "sheet.csv"
    write_sheet(sheet, "2")
    before = sheet.read_bytes()
    assert pool.main(["--markdown"]) == 0
    assert sheet.read_bytes() == before
    assert "### E01-01" in (tmp_path / "judging" / "sheet.md").read_text(encoding="utf-8")


def test_an_existing_pool_needs_an_archive_name(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(pool, "OUTPUTS", tmp_path)
    sheet = tmp_path / "judging" / "sheet.csv"
    write_sheet(sheet, "1")
    before = sheet.read_bytes()
    assert pool.main([]) == 1
    assert sheet.read_bytes() == before


def test_carried_grades_follow_the_piece_not_the_code() -> None:
    sheet = [
        ROW | {"piece": "E01-01", "question_id": "E01", "text": "t", "grade": "2"},
        ROW | {"piece": "E01-02", "question_id": "E01", "text": "t", "grade": ""},
        ROW | {"piece": "E01-03", "question_id": "E01", "text": "t", "note": "unsure"},
    ]
    pooled = [
        {"code": "E01-01", "question_id": "E01", "id": "a#005"},
        {"code": "E01-02", "question_id": "E01", "id": "a#006"},
        {"code": "E01-03", "question_id": "E01", "id": "b#01-002"},
    ]
    assert pool.carried_grades(sheet, pooled) == {
        ("E01", "a#005"): ("2", ""),
        ("E01", "b#01-002"): ("", "unsure"),
    }


def test_a_rebuild_archives_the_old_pool_and_prefills_its_grades(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    topics = tmp_path / "topics.yaml"
    topics.write_text(
        "topics:\n  - {id: E01, kind: explicit, question: Q, relevant: R, not_relevant: N}\n",
        encoding="utf-8",
    )
    sources = tmp_path / "sources.yaml"
    sources.write_text("sources:\n  - {slug: a, source_title: A}\n", encoding="utf-8")
    monkeypatch.setattr(pool, "TOPICS", topics)
    monkeypatch.setattr(pool, "SOURCES", sources)
    monkeypatch.setattr(pool, "OUTPUTS", tmp_path / "outputs")
    monkeypatch.setattr(pool.build_index, "use_study", lambda name: None)
    monkeypatch.setattr(
        pool.build_index, "load_index", lambda name: ({"embedding_model": "m"}, [], None)
    )
    judging = tmp_path / "outputs" / "judging"
    write_sheet(judging / "sheet.csv", "2")
    old = {"pool": [{"code": "E01-01", "question_id": "E01", "id": "a#002"}]}
    (judging / "pool.json").write_text(json.dumps(old), encoding="utf-8")
    ranked = [(0.9, piece("a#001")), (0.8, piece("a#002"))]
    monkeypatch.setattr(pool.build_index, "retrieve", lambda approach, q, k: ranked)

    assert pool.main(["--archive", "first"]) == 0

    archived = tmp_path / "outputs" / "archive" / "first" / "judging"
    assert (archived / "sheet.csv").exists() and (archived / "pool.json").exists()
    rows = pool.read_sheet(judging / "sheet.csv")
    grades = {
        pool.json.loads((judging / "pool.json").read_text())["pool"][i]["id"]: r["grade"]
        for i, r in enumerate(rows)
    }
    assert grades == {"a#001": "", "a#002": "2"}
    assert "\nGrade: 2\n" in (judging / "sheet.md").read_text(encoding="utf-8")
    assert pool.main(["--archive", "first"]) == 1  # an archive is never overwritten


def test_grades_typed_in_the_markdown_reach_the_csv(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(pool, "OUTPUTS", tmp_path)
    judging = tmp_path / "judging"
    write_sheet(judging / "sheet.csv", "")
    md = pool.sheet_markdown(pool.read_sheet(judging / "sheet.csv"))
    assert "\nGrade:\n" in md and "\nNote:\n" in md
    (judging / "sheet.md").write_text(
        md.replace("Grade:\n", "Grade: 1\n").replace("Note:\n", "Note: method section\n"),
        encoding="utf-8",
    )
    assert pool.main(["--markdown"]) == 0
    row = pool.read_sheet(judging / "sheet.csv")[0]
    assert (row["grade"], row["note"]) == ("1", "method section")
    assert "Grade: 1" in (judging / "sheet.md").read_text(encoding="utf-8")


def test_a_blank_markdown_grade_keeps_the_csv_grade(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    judging = tmp_path / "judging"
    write_sheet(judging / "sheet.csv", "2")
    blank = pool.sheet_markdown(pool.read_sheet(judging / "sheet.csv")).replace(
        "Grade: 2", "Grade:"
    )
    (judging / "sheet.md").write_text(blank, encoding="utf-8")
    assert pool.sync_from_markdown(judging) == 0
    assert pool.read_sheet(judging / "sheet.csv")[0]["grade"] == "2"


def test_a_grade_outside_the_scale_stops_and_names_the_piece() -> None:
    with pytest.raises(SystemExit, match="E01-01"):
        pool.markdown_grades("### E01-01\n\nGrade: 3\n")
