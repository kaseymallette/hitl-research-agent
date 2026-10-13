import json
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType
from typing import Any

import pymupdf
import pymupdf4llm
import pytest
from pdf_fixtures import make_image_only_pdf, make_table_pdf, make_text_pdf
from pydantic import ValidationError

from hitl_research_agent.extraction.annotations import grounding_view

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


def _extraction(prep: ModuleType, blocks: list[Any], items: list[Any]) -> Any:
    return prep.Extraction(
        pages=2,
        blocks=blocks,
        items=items,
        removed_lines=[],
        printed_labels={1: None, 2: None},
        pages_without_text=[],
    )


def _col(prep: ModuleType, text: str, x0: float, y0: float, page: int = 1) -> Any:
    return prep.Block("text", page, text, bbox=[x0, y0, x0 + 150, y0 + 40])


@pytest.fixture(scope="module")
def prepared_fixture(prep: ModuleType, tmp_path_factory: pytest.TempPathFactory) -> dict[str, Any]:
    root = tmp_path_factory.mktemp("prep")
    pdf = root / "fixture.pdf"
    make_text_pdf(pdf, PAGES)
    out = root / "out"
    summary = prep.prepare_source(entry(prep, pdf), out, max_characters=200_000)
    return {"pdf": pdf, "out": out, "dir": out / "fixture", "summary": summary}


# --- parser settings (verified against the installed version) ---------------------------------


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


# --- the shared process on a generated PDF ------------------------------------------------------


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
    flat = " ".join((prepared_fixture["dir"] / "prepared_text.md").read_text().split())
    assert "consumption of freshwater" in flat or "con-sumption" in flat or "con- sumption" in flat
    assert "that the trend continues on the next page" in flat


def test_records_include_tool_version_hashes_and_measured_time(
    prepared_fixture: dict[str, Any],
) -> None:
    record = json.loads((prepared_fixture["dir"] / "prep_record.json").read_text())
    assert record["parser"]["name"] == "pymupdf4llm"
    assert record["parser"]["version"] == "1.28.2"
    assert record["parser_settings"]["use_ocr"] is False
    for key in ("pdf_sha256", "prepared_text_sha256", "script_sha256", "settings_sha256"):
        assert len(record[key]) == 64, key
    assert record["timing"]["elapsed_seconds"] > 0
    assert record["timing"]["model_calls"] == 0
    assert record["within_size_limit"] is True
    assert record["preparation_limits"]  # the gaps this method always leaves are stated


def test_a_page_image_is_retained_for_every_page(prepared_fixture: dict[str, Any]) -> None:
    record = json.loads((prepared_fixture["dir"] / "prep_record.json").read_text())
    assert record["page_images"] == ["page_01.png", "page_02.png"]
    for name in record["page_images"]:
        assert (prepared_fixture["dir"] / "images" / name).exists()


def test_original_pdf_is_untouched(prepared_fixture: dict[str, Any], prep: ModuleType) -> None:
    assert (
        prep.sha256_file(prepared_fixture["pdf"])
        == json.loads((prepared_fixture["dir"] / "prep_record.json").read_text())["pdf_sha256"]
    )


def test_oversized_text_is_recorded_not_truncated(prep: ModuleType, tmp_path: Path) -> None:
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    summary = prep.prepare_source(entry(prep, pdf), tmp_path / "out", max_characters=10)
    text = (tmp_path / "out" / "fixture" / "prepared_text.md").read_text()
    assert summary["within_size_limit"] is False
    assert len(text) == summary["characters"] > 10  # nothing was cut to fit


# --- pages with no text layer (OCR off) ---------------------------------------------------------


def test_page_without_a_text_layer_is_recorded_not_ocred(prep: ModuleType, tmp_path: Path) -> None:
    pdf = tmp_path / "scan.pdf"
    make_image_only_pdf(pdf)
    summary = prep.prepare_source(
        entry(prep, pdf, slug="scan"), tmp_path / "out", max_characters=10**6
    )
    record = json.loads((tmp_path / "out" / "scan" / "prep_record.json").read_text())
    assert summary["pages_without_text_layer"] == [2]
    assert record["parser_settings"]["use_ocr"] is False
    assert "Scanned words" not in (tmp_path / "out" / "scan" / "prepared_text.md").read_text()


# --- what this method cannot represent ----------------------------------------------------------


def test_a_captioned_figure_is_annotated_and_decorative_art_is_not(prep: ModuleType) -> None:
    doc = pymupdf.open()
    page = doc.new_page(width=595, height=842)
    page.draw_rect(pymupdf.Rect(72, 80, 523, 300), fill=(0.8, 0.9, 0.8))
    page.insert_textbox(pymupdf.Rect(72, 310, 523, 340), "Figure 1. A water flow diagram.")
    page.insert_textbox(
        pymupdf.Rect(72, 360, 523, 460),
        "The diagram above shows how water moves through the cooling system.",
        fontsize=11,
    )
    items = [
        prep.Item("U1", "figure", 1, prep.NOTE_FIGURE, label="Figure 1"),
    ]
    blocks = [
        prep.Block("text", 1, "Before the figure."),
        prep.Block("visual", 1, "", "U1"),
        prep.Block("text", 1, "After the figure."),
    ]
    result = prep.assemble(_extraction(prep, blocks, items))
    assert [a["id"] for a in result.annotations] == ["U1"]
    assert "Figure 1" in result.text
    # the figure's content is never guessed at
    assert "estimate" not in result.text.lower()


def test_every_table_is_annotated_and_a_multilevel_header_says_so(prep: ModuleType) -> None:
    simple = "|Site|Water|\n|---|---|\n|Alpha|10.5|"
    spanning = "|||**Wa**|**ter for Trai**<br>**(million L)**|\n|---|---|---|---|\n|A|1|2|3|"
    assert prep._has_multilevel_header(simple) is False
    assert prep._has_multilevel_header(spanning) is True
    items = [
        prep.Item("T1", "table", 1, prep.NOTE_TABLE, label="Table 1"),
        prep.Item("T2", "table", 1, prep.NOTE_TABLE_MULTILEVEL, label="Table 2"),
    ]
    blocks = [prep.Block("table", 1, simple, "T1"), prep.Block("table", 1, spanning, "T2")]
    result = prep.assemble(_extraction(prep, blocks, items))
    assert [a["id"] for a in result.annotations] == ["T1", "T2"]
    # the data rows stay in the text; only the header grouping is called unrecoverable
    assert "Alpha" in result.text and "10.5" in result.text
    assert "multi-level column header is not recoverable" in result.text


def test_an_equation_paragraph_is_annotated_as_possibly_unfaithful(prep: ModuleType) -> None:
    assert prep._EQUATION_HINT.search("W = ∑ t=1 et · ρ")
    assert not prep._EQUATION_HINT.search("Ordinary prose about water and energy use.")
    items = [prep.Item("E1", "equation", 1, prep.NOTE_EQUATION)]
    blocks = [prep.Block("text", 1, "The footprint is W = ∑ t=1 et · ρ as shown.", "E1")]
    result = prep.assemble(_extraction(prep, blocks, items))
    assert [a["id"] for a in result.annotations] == ["E1"]
    # the raw text layer is kept, and flagged rather than silently trusted
    assert "W = ∑ t=1 et · ρ" in result.text
    assert "may not be faithfully rendered" in result.text


def test_annotations_can_never_match_as_verbatim_source_text(prep: ModuleType) -> None:
    items = [prep.Item("U1", "figure", 1, prep.NOTE_FIGURE, label="Figure 1")]
    blocks = [
        prep.Block("text", 1, "Before."),
        prep.Block("visual", 1, "", "U1"),
        prep.Block("text", 1, "After."),
    ]
    result = prep.assemble(_extraction(prep, blocks, items))
    assert "PREP-ANNOTATION" not in grounding_view(result.text)
    assert "Before. After." not in grounding_view(result.text)  # no match across the gap


def test_prepared_text_with_reserved_characters_is_refused(
    prep: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    bad = _extraction(prep, [prep.Block("text", 1, "Text with a stray ⟦ delimiter.")], [])
    monkeypatch.setattr(prep, "extract_pdf", lambda *_a, **_k: bad)
    with pytest.raises(ValueError, match="reserved"):
        prep.prepare_source(entry(prep, pdf), tmp_path / "out", max_characters=10**6)


def test_real_ruled_table_is_extracted_with_rows_and_columns(
    prep: ModuleType, tmp_path: Path
) -> None:
    pdf = tmp_path / "t.pdf"
    make_table_pdf(pdf)
    prep.prepare_source(entry(prep, pdf, slug="t"), tmp_path / "out", max_characters=10**6)
    text = (tmp_path / "out" / "t" / "prepared_text.md").read_text()
    table_lines = [line for line in text.splitlines() if line.startswith("|")]
    assert len(table_lines) >= 5  # header, separator, three data rows
    assert len({line.count("|") for line in table_lines}) == 1  # aligned columns
    flat = "".join(table_lines)
    for value in ("Alpha", "10.5", "20.1", "Gamma", "6.4"):
        assert value in flat
    record = json.loads((tmp_path / "out" / "t" / "prep_record.json").read_text())
    tables = [a for a in record["annotations"] if a["kind"] == "table"]
    assert tables and tables[0]["image"]  # an image is retained so the header can be checked


# --- reading order ------------------------------------------------------------------------------


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
    result, _ = prep.reorder_column_segments([left, caption, visual, a, b, c, d])
    assert [x.text for x in result][:3] == ["left", "Figure 1.", ""]
    assert [x.text for x in result][3:] == ["a-center", "c-center", "b-right", "d-right"]


def test_reorder_does_not_cross_pages(prep: ModuleType) -> None:
    p1 = [_col(prep, "p1-mid", 215, 100, page=1), _col(prep, "p1-right", 388, 100, page=1)]
    p2 = [_col(prep, "p2-mid", 215, 100, page=2), _col(prep, "p2-right", 388, 100, page=2)]
    result, changes = prep.reorder_column_segments(p1 + p2)
    assert result == p1 + p2 and changes == []


def test_reorder_is_on_by_default_and_recorded(prep: ModuleType, tmp_path: Path) -> None:
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    prep.prepare_source(entry(prep, pdf), tmp_path / "out", max_characters=10**6)
    record = json.loads((tmp_path / "out" / "fixture" / "prep_record.json").read_text())
    assert record["parser_settings"]["reorder_columns"] == prep.REORDER_METHOD
    # a single-column source has nothing to reorder, and the record says so
    assert record["reading_order_changes"] == []


# --- manifest and provenance --------------------------------------------------------------------


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


def test_cli_prepares_one_slug(
    prep: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    pdf = tmp_path / "f.pdf"
    make_text_pdf(pdf, PAGES)
    monkeypatch.setattr(prep, "load_manifest", lambda _path: [entry(prep, pdf)])
    assert prep.main(["prepare", "--slug", "fixture", "--output-root", str(tmp_path)]) == 0
    assert (tmp_path / "fixture" / "prepared_text.md").exists()
    assert prep.main(["prepare", "--slug", "nope", "--output-root", str(tmp_path)]) == 2
