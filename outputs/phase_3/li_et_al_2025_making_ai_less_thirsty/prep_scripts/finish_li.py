import hashlib, json, sys
from datetime import UTC, datetime
from pathlib import Path
import pymupdf, pymupdf4llm

PDF, OUT = Path(sys.argv[1]), Path(sys.argv[2])
doc = pymupdf.open(PDF)
(OUT / "images").mkdir(parents=True, exist_ok=True)
for pn in (4, 5, 6, 7):
    doc[pn - 1].get_pixmap(dpi=130).save(OUT / f"images/pdf_p0{pn}_page.png")
doc[3].get_pixmap(dpi=200, clip=pymupdf.Rect(215, 85, 545, 300)).save(OUT / "images/pdf_p04_figure1.png")
doc[5].get_pixmap(dpi=200, clip=pymupdf.Rect(40, 50, 548, 385)).save(OUT / "images/pdf_p06_table1.png")
doc[6].get_pixmap(dpi=200, clip=pymupdf.Rect(30, 115, 545, 272)).save(OUT / "images/pdf_p07_figure2.png")

text = (OUT / "source.md").read_text(encoding="utf-8")
sha = lambda b: hashlib.sha256(b).hexdigest()
st = PDF.stat()
record = {
    "slug": "li_et_al_2025_making_ai_less_thirsty",
    "pdf_path": str(PDF),
    "pdf_sha256": sha(PDF.read_bytes()),
    "pdf_pages": len(doc),
    "prepared_source": "source.md",
    "prepared_source_sha256": sha(text.encode("utf-8")),
    "prepared_source_characters": len(text),
    "max_source_characters_setting": 200000,
    "size_check": "pending_run_script",
    "is_excerpt": False,
    "tools": {"pymupdf": pymupdf.__version__, "pymupdf4llm_used_for_extraction": False,
              "note": "Text read with PyMuPDF dict blocks; pymupdf4llm was only used to probe the PDF and compare. Installed ephemerally with `uv run --no-project --with pymupdf4llm`; the project's pyproject.toml and uv.lock were not changed."},
    "provenance_basis": {
        "source_title": "first page of the PDF (title and subtitle)",
        "source_authors": "first-page byline",
        "doi": "first page ('DOI:10.1145/3724499')",
        "publisher": "page footers ('COMMUNICATIONS OF THE ACM', JULY 2025, VOL. 68, NO. 7) and copyright line; ACM named as the journal publisher, not independently confirmed",
        "publication_date": "left unset: only the issue (July 2025) is printed in the PDF, not a day; none invented",
        "source_type": "'other': a magazine-style feature in Communications of the ACM ('sustainability' section); the PDF does not state whether it was peer reviewed",
        "url": "left unset: the original download location is not recorded",
        "retrieved_at": "local PDF file modification time, used as a proxy; the true download time is not recorded",
        "pdf_file_mtime_utc": datetime.fromtimestamp(st.st_mtime, tz=UTC).isoformat(),
    },
    "transcriptions": [
        {"id": "T1", "kind": "figure", "label": "Figure 1 (datacenter water schematic)", "pdf_page": 4, "journal_page": 57,
         "image": "images/pdf_p04_figure1.png", "page_image": "images/pdf_p04_page.png", "produced_by": "local visual inspection by the assistant; no paid vision call",
         "not_recoverable": "arrow directions and the meaning of the tap icon are the transcriber's reading of the drawing; the figure has no numeric data"},
        {"id": "T2", "kind": "figure", "label": "Figure 2 (a)-(c) carbon/water efficiency and fuel mixes", "pdf_page": 7, "journal_page": 60,
         "image": "images/pdf_p07_figure2.png", "page_image": "images/pdf_p07_page.png", "produced_by": "local visual inspection by the assistant; no paid vision call",
         "not_recoverable": "coordinates of ~20 unlabeled scatter points, exact hourly values in (b) and (c), exact series values; all plotted values are visual estimates"},
        {"id": "E1", "kind": "equation", "pdf_page": 5, "journal_page": 58, "image": "images/pdf_p05_page.png", "produced_by": "local visual inspection; text layer was garbled"},
        {"id": "E2", "kind": "equation", "pdf_page": 6, "journal_page": 59, "image": "images/pdf_p06_page.png", "produced_by": "local visual inspection; text layer was garbled"},
        {"id": "E3", "kind": "equation", "pdf_page": 6, "journal_page": 59, "image": "images/pdf_p06_page.png", "produced_by": "local visual inspection; text layer was garbled"},
        {"id": "E4", "kind": "equation", "pdf_page": 6, "journal_page": 59, "image": "images/pdf_p06_page.png", "produced_by": "local visual inspection; text layer was garbled"},
    ],
    "extracted_tables": [
        {"id": "Table 1", "pdf_page": 6, "journal_page": 59, "rows": 18, "columns": 11, "image": "images/pdf_p06_table1.png",
         "method": "cell values read directly from the PDF text layer (not transcribed); two-level column header restructured by hand into one row; every row compared with the page image"}],
    "marker_syntax": {
        "transcription_blocks": "<<<TRANSCRIPTION id kind=... pdf_page=... image=... produced_by=...>>> ... <<<END TRANSCRIPTION id>>> (block form for figures, inline form for equations)",
        "extracted_table": "<<<EXTRACTED TABLE 1 ...>>> ... <<<END EXTRACTED TABLE 1>>>",
        "superscripts": "<sup>..</sup> marks superscript citation markers and footnote letters",
    },
    "normalizations_applied": [
        "reading order assigned per page from the three-column layout; figure/table placed where it sits on the page",
        "page markers '[PDF page N]' added at the start of each page; sentences that continue across a page break are left split at the marker",
        "line breaks joined; end-of-line hyphenation repaired unless the hyphenated compound occurs unbroken elsewhere in the document",
        "bold run-in headings marked with **; bullet glyph replaced by '-'",
        "footnotes a and b moved to the end of their page and labeled; pull quotes moved to the end of their page and labeled (they repeat body text)",
        "reference list split one entry per line; spaces removed inside broken URLs",
        "zero-width and thin-space characters removed",
        "omitted: running headers/footers, the rotated image credit on page 1, and the decorative page-2 illustration (noted in the text)",
    ],
    "information_not_recovered": [
        "Figure 2 per-point and hourly values (see T2); only approximate visual estimates are provided",
        "Figure 1 company/model logos are named in the transcription but not reproduced",
        "PDF page 2 is a decorative illustration with no content",
    ],
    "created_at_utc": datetime.now(UTC).isoformat(),
}
(OUT / "prep_record.json").write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
print("ok", len(text))
