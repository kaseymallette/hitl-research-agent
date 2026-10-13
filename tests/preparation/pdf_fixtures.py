from pathlib import Path

import pymupdf


def make_text_pdf(
    path: Path, pages: list[list[str]], header: str = "Journal of Fixtures 2026"
) -> None:
    """Pages of plain paragraphs with a repeated header and a numbered footer."""
    doc = pymupdf.open()
    for number, paragraphs in enumerate(pages, start=1):
        page = doc.new_page(width=595, height=842)
        page.insert_text((72, 40), header, fontsize=9)
        y = 100.0
        for paragraph in paragraphs:
            page.insert_textbox(pymupdf.Rect(72, y, 523, y + 130), paragraph, fontsize=11)
            y += 140
        page.insert_text((72, 810), f"Page {number}", fontsize=9)
    doc.save(path)


def make_image_only_pdf(path: Path) -> None:
    """One text page followed by a page that is only a picture of text (no text layer)."""
    source = pymupdf.open()
    page = source.new_page(width=595, height=842)
    page.insert_textbox(
        pymupdf.Rect(72, 100, 523, 400), "Scanned words that have no text layer.", fontsize=16
    )
    pix = page.get_pixmap(dpi=100)
    doc = pymupdf.open()
    text_page = doc.new_page(width=595, height=842)
    y = 100.0
    for paragraph in (
        "An ordinary readable first page begins with a full paragraph about water use.",
        "A second paragraph explains that cooling systems consume freshwater every day.",
        "A third paragraph closes the page with one more complete and plain sentence.",
    ):
        text_page.insert_textbox(pymupdf.Rect(72, y, 523, y + 100), paragraph, fontsize=11)
        y += 110
    scan = doc.new_page(width=595, height=842)
    scan.insert_image(scan.rect, pixmap=pix)
    doc.save(path)


def make_table_pdf(path: Path) -> None:
    """A page with prose and a ruled 4x3 table (header + three rows)."""
    doc = pymupdf.open()
    page = doc.new_page(width=595, height=842)
    page.insert_textbox(
        pymupdf.Rect(72, 80, 523, 160),
        "Table 1 below lists measured water use for three sites in the study.",
        fontsize=11,
    )
    rows = [
        ["Site", "Water (L)", "Energy (kWh)"],
        ["Alpha", "10.5", "3.2"],
        ["Beta", "20.1", "4.8"],
        ["Gamma", "30.7", "6.4"],
    ]
    x0, y0, cw, rh = 72, 200, 150, 28
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            rect = pymupdf.Rect(x0 + c * cw, y0 + r * rh, x0 + (c + 1) * cw, y0 + (r + 1) * rh)
            page.draw_rect(rect, width=0.8)
            page.insert_textbox(rect + (4, 6, -2, 0), cell, fontsize=11)
    page.insert_textbox(
        pymupdf.Rect(72, 360, 523, 460),
        "The table shows that water use rises with energy use across the three sites.",
        fontsize=11,
    )
    doc.save(path)
