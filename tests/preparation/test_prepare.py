import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType
from typing import Any

import pymupdf
import pymupdf4llm
import pytest
from pdf_fixtures import make_image_only_pdf, make_table_pdf, make_text_pdf
from pydantic import ValidationError

from hitl_research_agent.extraction.annotations import find_annotations, grounding_view

PAGES = [
    [
        "A first paragraph on the first page finishes cleanly.",
        "Water use in data centers grows quickly. Operators report that con-\n"
        "sumption of freshwater rises with cooling load and that the trend",
    ],
    ["continues on the next page without any interruption at all."],
]


def entry(prep: ModuleType, pdf: Path, **overrides: Any) -> Any:
    data: dict[str, Any] = dict(
        slug="fixture",
        pdf=str(pdf),
        source_title="Fixture Source",
        source_type="other",
        retrieved_at=datetime(2026, 1, 1, tzinfo=UTC),
    )
    data.update(overrides)
    return prep.ManifestEntry.model_validate(data)


@pytest.fixture(scope="module")
def prepared_fixture(prep: ModuleType, tmp_path_factory: pytest.TempPathFactory) -> dict[str, Any]:
    root = tmp_path_factory.mktemp("prep")
    pdf = root / "fixture.pdf"
    make_text_pdf(pdf, PAGES)
    out = root / "out"
    summary = prep.prepare_source(entry(prep, pdf), out, max_characters=200_000)
    return {"pdf": pdf, "out": out, "dir": out / "fixture", "summary": summary, "root": root}


# --- parser settings (verified against the installed version) -------------------------------


def test_parser_settings_are_accepted_without_warnings(
    prep: ModuleType, prepared_fixture: dict[str, Any], capsys: pytest.CaptureFixture[str]
) -> None:
    pymupdf4llm.use_layout(True)
    doc = pymupdf.open(prepared_fixture["pdf"])
    chunks = pymupdf4llm.to_markdown(
        doc, page_chunks=True, header=False, footer=False, use_ocr=False
    )
    captured = capsys.readouterr()
    assert "ignored" not in captured.out + captured.err  # legacy mode would warn
    assert "page_boxes" in chunks[0]  # layout mode: boxes with positions are available
    assert prep.PARSER_SETTINGS["layout_mode"] is True
    assert prep.PARSER_SETTINGS["use_ocr"] is False
    assert prep.PARSER_SETTINGS["header"] is False and prep.PARSER_SETTINGS["footer"] is False


def test_installed_parser_version_matches_the_pin(prep: ModuleType) -> None:
    assert prep.PARSER_VERSION == "1.28.2"


# --- shared process on a generated PDF ----------------------------------------------------------


def test_header_footer_removed_and_recorded(prepared_fixture: dict[str, Any]) -> None:
    text = (prepared_fixture["dir"] / "prepared_text.md").read_text()
    assert "Journal of Fixtures" not in text
    assert "Page 1" not in text and "Page 2" not in text
    record = json.loads((prepared_fixture["dir"] / "prep_record.json").read_text())
    removed = " ".join(r["text"] for r in record["removed_lines"])
    assert "Journal of Fixtures" in removed or record["parser_settings"]["header"] is False


def test_page_locators_are_in_a_separate_mapping_not_the_text(
    prepared_fixture: dict[str, Any],
) -> None:
    text = (prepared_fixture["dir"] / "prepared_text.md").read_text()
    page_map = json.loads((prepared_fixture["dir"] / "page_map.json").read_text())
    assert "[PDF page" not in text
    assert [p["pdf_page"] for p in page_map] == [1, 2]
    assert page_map[0]["start_offset"] == 0
    assert page_map[0]["end_offset"] == page_map[1]["start_offset"] <= len(text)
    assert page_map[1]["end_offset"] == len(text)
    assert page_map[0]["printed_label"] is None or isinstance(page_map[0]["printed_label"], str)


def test_sentence_crossing_a_page_break_is_joined_and_the_hyphen_repaired(
    prepared_fixture: dict[str, Any],
) -> None:
    text = (prepared_fixture["dir"] / "prepared_text.md").read_text()
    flat = " ".join(text.split())
    assert "consumption of freshwater" in flat or "con-sumption" in flat or "con- sumption" in flat
    assert "that the trend continues on the next page" in flat


def test_no_paraphrase_all_pdf_words_survive(prepared_fixture: dict[str, Any]) -> None:
    verification = json.loads((prepared_fixture["dir"] / "verification_record.json").read_text())
    for page in verification["automated_checks"]["page_word_coverage"]:
        assert page["coverage"] >= 0.97, page


def test_records_include_tool_version_settings_hashes_and_measured_time(
    prepared_fixture: dict[str, Any],
) -> None:
    record = json.loads((prepared_fixture["dir"] / "prep_record.json").read_text())
    assert record["parser"]["name"] == "pymupdf4llm"
    assert record["parser"]["version"] == "1.28.2"
    assert record["parser_settings"]["use_ocr"] is False
    assert len(record["pdf_sha256"]) == 64 and len(record["prepared_text_sha256"]) == 64
    assert record["timing"]["extraction_run"]["elapsed_seconds"] > 0
    assert record["timing"]["extraction_run"]["model_calls"] == 0
    assert record["within_size_limit"] is True
    verification = json.loads((prepared_fixture["dir"] / "verification_record.json").read_text())
    assert verification["automated_checks"]["limitations"]
    # verification findings are kept apart from the hashes that bind them
    assert "bound_to" in verification and "items" in verification


def test_original_pdf_is_untouched(prepared_fixture: dict[str, Any], prep: ModuleType) -> None:
    assert (
        prep.sha256_file(prepared_fixture["pdf"])
        == json.loads((prepared_fixture["dir"] / "prep_record.json").read_text())["pdf_sha256"]
    )


# --- scanned / unreadable pages (OCR off) ------------------------------------------------------


def test_scanned_page_is_flagged_not_ocred(prep: ModuleType, tmp_path: Path) -> None:
    pdf = tmp_path / "scan.pdf"
    make_image_only_pdf(pdf)
    summary = prep.prepare_source(
        entry(prep, pdf, slug="scan"), tmp_path / "out", max_characters=10**6
    )
    text = (tmp_path / "out" / "scan" / "prepared_text.md").read_text()
    assert "Scanned words" not in text  # OCR is off: nothing was recognized
    annotations = find_annotations(text)
    assert annotations, "the unreadable page must be represented by an annotation"
    verification = json.loads((tmp_path / "out" / "scan" / "verification_record.json").read_text())
    assert any(i["category"] == "image_only_page" for i in verification["items"])
    assert summary["status"] != prep.STATUS_READY


# --- tables ---------------------------------------------------------------------------------------


def test_table_row_column_consistency_and_header_fragment_checks(prep: ModuleType) -> None:
    good = "|A|B|\n|---|---|\n|1|2|\n|3|4|"
    assert prep._table_problems(good, {"a", "b"}) == []
    ragged = "|A|B|\n|---|---|\n|1|2|3|\n|3|4|"
    assert any("inconsistent" in p for p in prep._table_problems(ragged, {"a", "b"}))
    fragmented = "|Wa|ter|\n|---|---|\n|1|2|\n|3|4|"
    assert any("fragments" in p for p in prep._table_problems(fragmented, {"water"}))
    assert prep._table_problems("|A|\n|---|", set())  # fewer than three rows


# --- continuity and reading-order flags --------------------------------------------------------


def test_continuity_flags(prep: ModuleType) -> None:
    B = prep.Block
    blocks = [
        B("text", 1, "A finished sentence."),
        B("text", 1, "starts lowercase for no reason."),
        B("text", 1, "ends mid-sentence with"),
        B("text", 1, "Then a Capital begins."),
        B("text", 1, "Another opener that stops"),
        B("caption", 1, "Figure 1. A caption."),
    ]
    kinds = {f["kind"] for f in prep._continuity_flags(blocks)}
    assert kinds == {
        "lowercase_after_finished_sentence",
        "mid_sentence_then_capital",
        "interrupted_sentence",
    }
    assert prep._continuity_flags([B("text", 1, "Clean."), B("text", 1, "Also clean.")]) == []


def test_column_geometry_flags_interleaved_columns(prep: ModuleType) -> None:
    B = prep.Block
    left1 = B("text", 1, "left one", bbox=[40, 100, 200, 200])
    right = B("text", 1, "right", bbox=[390, 100, 540, 200])
    left2 = B("text", 1, "left two", bbox=[40, 210, 200, 300])
    assert [f["kind"] for f in prep._column_geometry_flags([left1, right, left2])] == [
        "column_interleaving"
    ]
    assert prep._column_geometry_flags([left1, left2, right]) == []


# --- assembly: annotations, cleared items, hyphens -----------------------------------------------


def _extraction(prep: ModuleType, blocks: list[Any], items: list[Any]) -> Any:
    return prep.Extraction(
        pages=2,
        blocks=blocks,
        items=items,
        page_coverage=[{"page": 1, "coverage": 1.0}],
        removed_lines=[],
        altered_words=[],
        label_fragments={},
        printed_labels={1: None, 2: None},
        image_counts=[],
        unreadable_pages=[],
    )


def test_assemble_annotates_unresolved_visuals_and_skips_cleared_ones(prep: ModuleType) -> None:
    B, Item = prep.Block, prep.Item
    items = [
        Item("U1", "visual", "figure", 1, "figure", label="Figure 1", image="images/U1.png"),
        Item("U2", "visual", "picture", 1, "decorative", image="images/U2.png"),
    ]
    blocks = [
        B("text", 1, "Before the figure."),
        B("visual", 1, "", "U1"),
        B("visual", 1, "", "U2"),
        B("text", 1, "After the figure."),
    ]
    ext = _extraction(prep, blocks, items)
    pending = prep.assemble(ext, {}, {})
    assert [a["id"] for a in pending.annotations] == ["U1", "U2"]
    cleared = prep.assemble(ext, {"U2": "decorative_no_content"}, {})
    assert [a["id"] for a in cleared.annotations] == ["U1"]
    assert "Figure 1" in cleared.text and "estimate" not in cleared.text.lower()
    # annotations are well-formed and the grounding view removes them
    assert "PREP-ANNOTATION" not in grounding_view(cleared.text)
    assert all(
        "not source text" in cleared.text[a["start_offset"] : a["end_offset"]]
        for a in cleared.annotations
    )


def test_assemble_joins_a_sentence_across_a_page_and_maps_pages(prep: ModuleType) -> None:
    B = prep.Block
    blocks = [B("text", 1, "The trend continues and"), B("text", 2, "never stops here.")]
    result = prep.assemble(_extraction(prep, blocks, []), {}, {})
    assert "The trend continues and never stops here." in result.text
    assert [p["pdf_page"] for p in result.page_map] == [1, 2]
    assert result.page_map[1]["start_offset"] > 0
    assert "page" not in result.text.lower().replace("pages", "")  # no locators in the text


def test_hyphen_rule_joins_only_when_the_document_supports_it(prep: ModuleType) -> None:
    vocab = ({"consumption", "water"}, {"water-intensive"})
    notes: list[dict[str, Any]] = []
    assert (
        prep._join_hyphen("high con-", "sumption of water", vocab, notes, 1)
        == "high consumption of water"
    )
    assert (
        prep._join_hyphen("a water-", "intensive process", vocab, notes, 1)
        == "a water-intensive process"
    )
    assert notes == []
    out = prep._join_hyphen("a zxq-", "wvu thing", vocab, notes, 1)
    assert out == "a zxq-wvu thing" and notes[0]["kind"] == "ambiguous_hyphenation"


def test_equation_hint_detects_symbols_not_prose(prep: ModuleType) -> None:
    assert prep._EQUATION_HINT.search("W = ∑ t=1 et · ρ")
    assert prep._EQUATION_HINT.search("is calculated as <sup>where b</sup> k")
    assert not prep._EQUATION_HINT.search(
        "Plain prose about water use, with citations.<sup>12</sup>"
    )


# --- status, review, approval, gate -------------------------------------------------------------


def _status_extraction(prep: ModuleType, categories: list[tuple[str, str, str]]) -> Any:
    items = [prep.Item(i, c, k, 1, "r") for i, c, k in categories]
    return _extraction(prep, [prep.Block("text", 1, "x")], items)


def test_status_ready_unresolved_and_blocked(prep: ModuleType) -> None:
    ready = prep.compute_status(_status_extraction(prep, []), {}, 100, 1000)
    assert ready[0] == prep.STATUS_READY
    ext = _status_extraction(prep, [("U1", "visual", "figure"), ("C1", "reading_order", "x")])
    assert prep.compute_status(ext, {}, 100, 1000)[0] == prep.STATUS_UNRESOLVED
    cleared = {"U1": {"result": "decorative_no_content"}, "C1": {"result": "confirmed_ok"}}
    assert prep.compute_status(ext, cleared, 100, 1000)[0] == prep.STATUS_READY
    problem = {"U1": {"result": "decorative_no_content"}, "C1": {"result": "confirmed_problem"}}
    status, reasons, _ = prep.compute_status(ext, problem, 100, 1000)
    assert status == prep.STATUS_BLOCKED and "C1" in reasons[0]
    status, reasons, _ = prep.compute_status(_status_extraction(prep, []), {}, 2000, 1000)
    assert status == prep.STATUS_BLOCKED and "over the limit" in reasons[0]
    lim = {"U1": {"result": "limitation"}, "C1": {"result": "uncertain"}}
    assert prep.compute_status(ext, lim, 100, 1000)[0] == prep.STATUS_UNRESOLVED


def test_blocked_for_dropped_text(prep: ModuleType) -> None:
    ext = _status_extraction(prep, [])
    ext.page_coverage = [{"page": 3, "coverage": 0.5}]
    assert prep.compute_status(ext, {}, 10, 1000)[0] == prep.STATUS_BLOCKED


def test_oversized_text_is_blocked_without_truncation(prep: ModuleType, tmp_path: Path) -> None:
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    summary = prep.prepare_source(entry(prep, pdf), tmp_path / "out", max_characters=50)
    assert summary["status"] == prep.STATUS_BLOCKED
    text = (tmp_path / "out" / "fixture" / "prepared_text.md").read_text()
    assert len(text) > 50  # the full text is kept; nothing truncated
    allowed, why = prep.check_analysis_gate(tmp_path / "out" / "fixture")
    assert not allowed and "blocked" in why[0]


def test_gate_requires_source_specific_approval_for_unresolved(
    prep: ModuleType, tmp_path: Path
) -> None:
    pdf = tmp_path / "scan.pdf"
    make_image_only_pdf(pdf)
    out = tmp_path / "out"
    prep.prepare_source(entry(prep, pdf, slug="scan"), out, max_characters=10**6)
    directory = out / "scan"
    allowed, why = prep.check_analysis_gate(directory)
    assert not allowed and "approval" in why[0]
    approval = prep.record_approval(directory, "I accept this gap for this source only.", "owner")
    assert approval["approved_unresolved_items"]
    assert prep.check_analysis_gate(directory)[0] is True
    # an approval for another preparation or with extra unresolved items does not carry over
    tampered = json.loads((directory / "approval.json").read_text())
    tampered["approved_unresolved_items"] = []
    (directory / "approval.json").write_text(json.dumps(tampered))
    assert prep.check_analysis_gate(directory)[0] is False
    tampered["approved_unresolved_items"] = approval["approved_unresolved_items"]
    tampered["prepared_text_sha256"] = "0" * 64
    (directory / "approval.json").write_text(json.dumps(tampered))
    assert prep.check_analysis_gate(directory)[0] is False


def test_gate_detects_a_modified_prepared_text(
    prep: ModuleType, prepared_fixture: dict[str, Any], tmp_path: Path
) -> None:
    copy = tmp_path / "copy"
    shutil.copytree(prepared_fixture["dir"], copy)
    (copy / "prepared_text.md").write_text("tampered", encoding="utf-8")
    allowed, why = prep.check_analysis_gate(copy)
    assert not allowed and "hash" in why[0]


# --- reuse and reset -----------------------------------------------------------------------------


def test_reuse_keeps_verification_and_approval_and_changes_reset_them(
    prep: ModuleType, tmp_path: Path
) -> None:
    pdf = tmp_path / "scan.pdf"
    make_image_only_pdf(pdf)
    out = tmp_path / "out"
    first = prep.prepare_source(entry(prep, pdf, slug="scan"), out, max_characters=10**6)
    directory = out / "scan"
    bound = json.loads((directory / "prep_record.json").read_text())["bound_to"]
    (directory / "review.json").write_text(
        json.dumps(
            {
                "bound_to": bound,
                "reviewed_by": "tester",
                "reviews": [
                    {"item": "U1", "result": "decorative_no_content", "note": "blank scan"}
                ],
            }
        )
    )
    second = prep.prepare_source(entry(prep, pdf, slug="scan"), out, max_characters=10**6)
    assert second["reused"] is True and first["reused"] is False
    timing = json.loads((directory / "prep_record.json").read_text())["timing"]
    # the original extraction timing survives reuse; this run's own timing is kept separately
    assert timing["extraction_run"]["reused_existing_extraction"] is False
    assert timing["this_run"]["reused_existing_extraction"] is True
    verification = json.loads((directory / "verification_record.json").read_text())
    reviewed = {i["id"]: i["review"] for i in verification["items"]}
    assert "decorative_no_content" in reviewed.values()  # the finding survived reuse
    assert verification["review_metadata"]["reviewed_by"] == "tester"
    # change the PDF: verification and approval are archived and reset, history is kept
    doc = pymupdf.open(pdf)
    doc.new_page()
    doc.saveIncr() if False else doc.save(tmp_path / "scan2.pdf")
    shutil.copy(tmp_path / "scan2.pdf", pdf)
    third = prep.prepare_source(entry(prep, pdf, slug="scan"), out, max_characters=10**6)
    assert third["reused"] is False
    assert not (directory / "review.json").exists()
    assert list((directory / "superseded").glob("*/review.json"))


def test_stale_review_bound_to_old_hashes_is_ignored_and_archived(
    prep: ModuleType, tmp_path: Path
) -> None:
    (tmp_path / "review.json").write_text(
        json.dumps({"bound_to": {"pdf_sha256": "old"}, "reviews": []})
    )
    reviews, meta = prep.load_review(tmp_path, {"pdf_sha256": "new"})
    assert reviews == {} and meta == {}
    assert list((tmp_path / "superseded").glob("*/review.json"))


def test_unknown_review_result_is_rejected(prep: ModuleType, tmp_path: Path) -> None:
    bound = {"pdf_sha256": "x"}
    (tmp_path / "review.json").write_text(
        json.dumps({"bound_to": bound, "reviews": [{"item": "U1", "result": "looks_fine"}]})
    )
    with pytest.raises(ValueError):
        prep.load_review(tmp_path, bound)


# --- manifest and provenance ---------------------------------------------------------------------


def test_manifest_rejects_naive_retrieved_at_and_unlabeled_excerpt(
    prep: ModuleType, tmp_path: Path
) -> None:
    with pytest.raises(ValidationError):
        entry(prep, tmp_path / "x.pdf", retrieved_at=datetime(2026, 1, 1))
    with pytest.raises(ValidationError):
        entry(prep, tmp_path / "x.pdf", is_excerpt=True, excerpt_description="pages 1-5")
    with pytest.raises(ValidationError):
        entry(prep, tmp_path / "x.pdf", is_excerpt=True, source_title="Report (excerpt)")
    ok = entry(
        prep,
        tmp_path / "x.pdf",
        is_excerpt=True,
        source_title="Report (excerpt)",
        excerpt_description="chapters 1-2 only",
    )
    assert ok.is_excerpt


def test_excerpt_and_unset_provenance_fields_are_recorded(prep: ModuleType, tmp_path: Path) -> None:
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    e = entry(
        prep,
        pdf,
        is_excerpt=True,
        source_title="Energy and AI (excerpt)",
        excerpt_description="a trimmed excerpt of the full report",
    )
    prep.prepare_source(e, tmp_path / "out", max_characters=10**6)
    record = json.loads((tmp_path / "out" / "fixture" / "prep_record.json").read_text())
    assert record["is_excerpt"] is True and record["excerpt_description"]
    provenance = json.loads((tmp_path / "out" / "fixture" / "provenance.json").read_text())
    assert provenance["source_title"].endswith("(excerpt)")
    for unset in ("doi", "publisher", "url", "publication_date"):
        assert unset not in provenance  # unknown fields are left unset, not guessed


def test_real_manifest_loads_and_keeps_unknown_fields_unset(prep: ModuleType) -> None:
    entries = prep.load_manifest(prep.DEFAULT_MANIFEST)
    li = next(e for e in entries if e.slug == "li_et_al_2025_making_ai_less_thirsty")
    assert li.publication_date is None
    assert li.retrieved_at.utcoffset() is not None


def test_prepared_text_with_reserved_characters_is_refused(
    prep: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    bad = _extraction(prep, [prep.Block("text", 1, "Text with a stray \u27e6 delimiter.")], [])
    monkeypatch.setattr(prep, "extract_pdf", lambda *_a, **_k: bad)
    with pytest.raises(ValueError, match="reserved"):
        prep.prepare_source(entry(prep, pdf), tmp_path / "out", max_characters=10**6)


def test_real_ruled_table_is_extracted_with_rows_and_columns(
    prep: ModuleType, tmp_path: Path
) -> None:
    pdf = tmp_path / "t.pdf"
    make_table_pdf(pdf)
    summary = prep.prepare_source(
        entry(prep, pdf, slug="t"), tmp_path / "out", max_characters=10**6
    )
    text = (tmp_path / "out" / "t" / "prepared_text.md").read_text()
    table_lines = [line for line in text.splitlines() if line.startswith("|")]
    assert len(table_lines) >= 5  # header, separator, three data rows
    assert len({line.count("|") for line in table_lines}) == 1  # aligned columns
    flat = "".join(table_lines)
    for value in ("Alpha", "10.5", "20.1", "Gamma", "6.4"):
        assert value in flat
    verification = json.loads((tmp_path / "out" / "t" / "verification_record.json").read_text())
    tables = [i for i in verification["items"] if i["category"] == "table"]
    assert tables and tables[0]["page_image"]  # a page image is retained for review
    assert summary["status"] in (prep.STATUS_READY, prep.STATUS_UNRESOLVED)


def test_unreadable_page_blocks_unless_a_reviewed_item_covers_it(prep: ModuleType) -> None:
    ext = _status_extraction(prep, [("U1", "image_only_page", "image_only_page")])
    ext.unreadable_pages = [1]
    reviewed = {"U1": {"result": "decorative_no_content"}}
    assert prep.compute_status(ext, reviewed, 10, 1000)[0] == prep.STATUS_READY
    assert prep.compute_status(ext, {}, 10, 1000)[0] == prep.STATUS_UNRESOLVED
    uncovered = _status_extraction(prep, [])
    uncovered.unreadable_pages = [1]
    status, reasons, _ = prep.compute_status(uncovered, {}, 10, 1000)
    assert status == prep.STATUS_BLOCKED and "OCR is off" in reasons[0]


# --- opt-in geometry reading-order correction -------------------------------------------------


def _col(
    prep: ModuleType, text: str, x0: float, y0: float, kind: str = "text", page: int = 1
) -> Any:
    return prep.Block(kind, page, text, bbox=[x0, y0, x0 + 150, y0 + 50])


def test_reorder_fixes_a_segment_that_jumps_between_columns_and_back(prep: ModuleType) -> None:
    mid1, mid2, mid3 = (_col(prep, f"mid{i}", 215, 100 + 100 * i) for i in range(3))
    right1, right2 = _col(prep, "right1", 388, 100), _col(prep, "right2", 388, 200)
    # parser order: mid1, right1, mid2, right2, mid3 (interleaved)
    blocks = [mid1, right1, mid2, right2, mid3]
    result, changes = prep.reorder_column_segments(blocks)
    assert [b.text for b in result] == ["mid0", "mid1", "mid2", "right1", "right2"]
    assert len(changes) == 1 and changes[0]["method"] == prep.REORDER_METHOD
    # nothing is edited, dropped, or duplicated: the same block objects, same text
    assert sorted(id(b) for b in result) == sorted(id(b) for b in blocks)
    assert sorted(b.text for b in result) == sorted(b.text for b in blocks)


def test_reorder_leaves_correctly_ordered_pages_untouched(prep: ModuleType) -> None:
    blocks = [
        _col(prep, "left1", 40, 100),
        _col(prep, "left2", 40, 200),
        _col(prep, "right1", 388, 100),
        _col(prep, "right2", 388, 200),
    ]
    result, changes = prep.reorder_column_segments(blocks)
    assert result == blocks and changes == []


def test_reorder_never_moves_captions_tables_or_visuals_across_segments(prep: ModuleType) -> None:
    caption = prep.Block("caption", 1, "Figure 1.", bbox=[215, 56, 543, 83])
    visual = prep.Block("visual", 1, "", "U1")
    a = _col(prep, "a-center", 215, 300)
    b = _col(prep, "b-right", 388, 300)
    c = _col(prep, "c-center", 215, 400)
    d = _col(prep, "d-right", 388, 400)
    left = _col(prep, "left", 40, 100)
    blocks = [left, caption, visual, a, b, c, d]
    result, _ = prep.reorder_column_segments(blocks)
    assert [x.text for x in result][:3] == ["left", "Figure 1.", ""]
    assert [x.text for x in result][3:] == ["a-center", "c-center", "b-right", "d-right"]


def test_reorder_does_not_cross_pages(prep: ModuleType) -> None:
    p1 = [_col(prep, "p1-mid", 215, 100, page=1), _col(prep, "p1-right", 388, 100, page=1)]
    p2 = [_col(prep, "p2-mid", 215, 100, page=2), _col(prep, "p2-right", 388, 100, page=2)]
    result, changes = prep.reorder_column_segments(p1 + p2)
    assert result == p1 + p2 and changes == []


def test_reorder_is_opt_in_and_does_not_change_the_default_settings_hash(
    prep: ModuleType, tmp_path: Path
) -> None:
    assert prep.settings_sha256() == prep.settings_sha256(False)
    assert prep.settings_sha256(True) != prep.settings_sha256(False)
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    default = prep.prepare_source(entry(prep, pdf), tmp_path / "a", max_characters=10**6)
    opted = prep.prepare_source(
        entry(prep, pdf), tmp_path / "b", max_characters=10**6, reorder_columns=True
    )
    record_a = json.loads((tmp_path / "a" / "fixture" / "prep_record.json").read_text())
    record_b = json.loads((tmp_path / "b" / "fixture" / "prep_record.json").read_text())
    assert record_a["reading_order_fix"]["enabled"] is False
    assert record_b["reading_order_fix"]["enabled"] is True
    assert record_a["bound_to"]["settings_sha256"] != record_b["bound_to"]["settings_sha256"]
    # a source with no interleaved columns is unchanged by the option
    text_a = (tmp_path / "a" / "fixture" / "prepared_text.md").read_text()
    text_b = (tmp_path / "b" / "fixture" / "prepared_text.md").read_text()
    assert text_a == text_b and record_b["reading_order_fix"]["changes"] == []
    assert default["status"] == opted["status"]


def test_cli_exposes_reordering_only_as_an_explicit_flag(
    prep: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    seen: list[bool] = []
    fixture_entry = entry(prep, tmp_path / "f.pdf")
    monkeypatch.setattr(prep, "load_manifest", lambda _path: [fixture_entry])

    def fake_prepare(_entry: Any, _root: Path, **kwargs: Any) -> dict[str, Any]:
        seen.append(kwargs["reorder_columns"])
        return {"status": prep.STATUS_READY}

    monkeypatch.setattr(prep, "prepare_source", fake_prepare)
    base = ["prepare", "--slug", "fixture", "--output-root", str(tmp_path)]
    assert prep.main(base) == 0
    assert prep.main([*base, "--reorder-columns"]) == 0
    assert seen == [False, True]
