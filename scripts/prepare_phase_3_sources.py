"""Shared Phase 3 source preparation: PDF -> prepared text plus provenance records.

One process for every PDF (no per-source code, no tool switching):

    python scripts/prepare_phase_3_sources.py prepare --slug SLUG
    python scripts/prepare_phase_3_sources.py page    --slug SLUG --page N

What it does:

* extracts text and tables with ``pymupdf4llm`` (pinned; layout mode; header/footer
  removal on; OCR off) and renders a page image for every page;
* corrects reading order where a run of paragraphs jumps between columns and back
  (geometry only; whole blocks are reordered, no text is edited);
* cleans conservatively: recurring headers/footers removed, line-break hyphens joined
  only where the document's own text supports it, nothing paraphrased or reconstructed;
* keeps page locators in a separate mapping, never inside the text;
* never estimates chart values, interprets figures, or transcribes equations.

What it does **not** do: it makes no judgement about whether a source is good enough to
analyze. It states, unconditionally, the three things this extraction method cannot
represent faithfully — figures, equations, and multi-level table headers — as labeled
preparation annotations (see ``hitl_research_agent.extraction.annotations``). Every page
image is retained so any of them can be checked by eye. Deciding whether the gaps matter
is the researcher's call, in review, not this script's.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pymupdf
import pymupdf4llm
import yaml
from pydantic import AwareDatetime, BaseModel, ConfigDict, HttpUrl, ValidationError, model_validator

from hitl_research_agent.config import Settings
from hitl_research_agent.extraction.annotations import (
    find_annotations,
    format_annotation,
    reserved_character_problems,
)
from hitl_research_agent.models.provenance import SourceType

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO_ROOT / "data" / "phase_3" / "sources.yaml"
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "outputs" / "preparation"

PARSER_NAME = "pymupdf4llm"
PARSER_VERSION = pymupdf4llm.__version__ if hasattr(pymupdf4llm, "__version__") else "unknown"
REORDER_METHOD = "geometry_column_segments_v1"
# Verified against the installed version (see tests/preparation): layout mode keeps tables
# and exposes page boxes; header/footer/OCR arguments are honored (legacy mode ignores
# them and drops Table 1 on the Li paper).
PARSER_SETTINGS: dict[str, Any] = {
    "layout_mode": True,
    "header": False,
    "footer": False,
    "use_ocr": False,
    "page_chunks": True,
    "page_image_dpi": 130,
    "crop_image_dpi": 200,
    "reorder_columns": REORDER_METHOD,
}

REORDER_COLUMN_GAP = 40.0  # points between column left edges that separate columns
MARGIN_TOP = 70.0
MARGIN_BOTTOM_FRACTION = 0.95

# The three things this extraction method cannot represent. Stated unconditionally, not
# detected: no heuristic decides whether a given figure or equation "came out well."
NOTE_FIGURE = "content not extracted; see the retained image"
NOTE_EQUATION = (
    "the symbols above are the raw text layer and may not be faithfully rendered; "
    "see the retained image"
)
NOTE_TABLE_MULTILEVEL = (
    "data rows extracted above; the grouping of the multi-level column header is not "
    "recoverable from the extracted text; see the retained image"
)
NOTE_TABLE = "verify the column headers against the retained image"

NO_MAPPED_TEXT = (
    "this page contributed no text: it held only an image, a header or footer, or a "
    "recurring margin line (see removed_lines). Render it with the `page` command to look."
)

_EQUATION_HINT = re.compile(r"[∑∫√∏⋯±≈≤≥∂Ͱ-Ͽ]|<sup>[A-Za-z][A-Za-z ]{3,}</sup>")

PREPARATION_LIMITS = [
    "Figures and diagrams are not transcribed or interpreted. Each one is cropped and "
    "retained, and any whole page can be rendered from the PDF with the `page` command.",
    "Equations appear only as the PDF's raw text layer, which is frequently not faithful.",
    "Multi-level table headers lose their grouping; the data rows are extracted as-is.",
    "Reading order is corrected only where block geometry shows a column jump. It is not "
    "proven correct anywhere.",
    "An uncaptioned figure produces no annotation and no crop; it is visible only by "
    "rendering its page.",
]


# --------------------------------------------------------------------------- manifest


class ManifestEntry(BaseModel):
    """One source: provenance (confirmed by the project owner) plus excerpt facts."""

    model_config = ConfigDict(extra="forbid")

    slug: str
    pdf: str
    source_title: str
    source_authors: list[str] = []
    publication_date: str | None = None
    source_type: SourceType
    doi: str | None = None
    publisher: str | None = None
    url: HttpUrl | None = None
    retrieved_at: AwareDatetime
    is_excerpt: bool = False
    excerpt_description: str | None = None
    provenance_basis: dict[str, str] = {}

    @model_validator(mode="after")
    def _excerpt_is_labeled(self) -> ManifestEntry:
        if self.is_excerpt:
            if not self.excerpt_description:
                raise ValueError("an excerpt needs an excerpt_description")
            if "(excerpt)" not in self.source_title.lower():
                raise ValueError("an excerpt's source_title must include '(excerpt)'")
        return self


def load_manifest(path: Path) -> list[ManifestEntry]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [ManifestEntry.model_validate(item) for item in data["sources"]]


# --------------------------------------------------------------------------- hashing


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def script_sha256() -> str:
    return sha256_file(Path(__file__).resolve())


def settings_sha256() -> str:
    payload = json.dumps(
        {"parser": PARSER_NAME, "version": PARSER_VERSION, "settings": PARSER_SETTINGS},
        sort_keys=True,
    )
    return sha256_bytes(payload.encode())


def now_utc() -> str:
    return datetime.now(UTC).isoformat()


# --------------------------------------------------------------------------- extraction


def _plain(text: str) -> str:
    return re.sub(r"\*\*|<sup>.*?</sup>", "", text).rstrip()


def _norm_line(text: str) -> str:
    plain = re.sub(r"[*_#`>|]|<[^>]+>", "", text)
    return re.sub(r"\d+", "#", re.sub(r"\s+", " ", plain)).strip().casefold()


def _midsentence(text: str) -> bool:
    return not _plain(text).endswith((".", "?", "!", ":", "”", '"', ")", "]"))


@dataclass
class Block:
    """One paragraph-level unit in reading order, before final assembly."""

    kind: str  # text | list | caption | heading | table | visual
    page: int
    text: str
    item_id: str | None = None  # figure/table/equation items link here
    bbox: list[float] | None = None


@dataclass
class Item:
    """Something this method cannot represent faithfully: a figure, equation, or table."""

    item_id: str
    kind: str  # figure | equation | table
    page: int
    note: str
    label: str | None = None
    bbox: list[float] | None = None
    image: str | None = None


@dataclass
class Extraction:
    pages: int
    blocks: list[Block]
    items: list[Item]
    removed_lines: list[dict[str, Any]]
    printed_labels: dict[int, str | None]
    pages_without_text: list[int]
    reading_order_changes: list[dict[str, Any]] = field(default_factory=list)


def _parse_chunks(pdf: Path) -> tuple[pymupdf.Document, list[dict[str, Any]]]:
    pymupdf4llm.use_layout(PARSER_SETTINGS["layout_mode"])
    doc = pymupdf.open(pdf)
    chunks = pymupdf4llm.to_markdown(
        doc,
        page_chunks=True,
        header=PARSER_SETTINGS["header"],
        footer=PARSER_SETTINGS["footer"],
        use_ocr=PARSER_SETTINGS["use_ocr"],
    )
    return doc, chunks


def _margin_numbers(page: pymupdf.Page) -> set[int]:
    height = page.rect.height
    return {
        int(word)
        for _x0, y0, _x1, y1, word, *_rest in page.get_text("words")
        if (y1 < MARGIN_TOP or y0 > height * MARGIN_BOTTOM_FRACTION)
        and re.fullmatch(r"\d{1,4}", word)
    }


def _printed_labels(doc: pymupdf.Document) -> dict[int, str | None]:
    """Printed page labels: the margin number that advances by one per page, if any."""
    numbers = {n: _margin_numbers(doc[n - 1]) for n in range(1, len(doc) + 1)}
    best_offset, best_hits = None, 0
    for offset in {v - n for n, vs in numbers.items() for v in vs}:
        hits = sum(1 for n, vs in numbers.items() if n + offset in vs)
        if hits > best_hits:
            best_offset, best_hits = offset, hits
    if best_offset is None or best_hits < max(2, len(doc) // 2):
        return {n: None for n in numbers}
    return {
        n: (str(n + best_offset) if n + best_offset in vs else None) for n, vs in numbers.items()
    }


def _classify_blocks(chunk: dict[str, Any], page_no: int) -> list[tuple[str, str, dict[str, Any]]]:
    """Split a page chunk into (kind, text, box) by its page boxes, in text order."""
    text: str = chunk["text"]
    out: list[tuple[str, str, dict[str, Any]]] = []
    covered = 0
    for box in sorted(chunk["page_boxes"], key=lambda b: b["pos"][0]):
        start, end = box["pos"]
        if start < covered:
            continue
        if start > covered and text[covered:start].strip():
            out.append(("text", text[covered:start].strip(), {"class": "text", "bbox": None}))
        covered = max(covered, end)
        body = text[start:end]
        cls = box["class"]
        if cls in ("page-header", "page-footer"):
            if body.strip():
                out.append(("removed", body.strip(), box))
            continue
        if cls == "picture":
            out.append(("visual", re.sub(r"<!--.*?-->", "", body, flags=re.S).strip(), box))
            continue
        if not body.strip():
            continue
        kind = {
            "caption": "caption",
            "table": "table",
            "section-header": "heading",
            "list-item": "list",
        }.get(cls, "text")
        out.append((kind, body.strip(), box))
    if text[covered:].strip():
        out.append(("text", text[covered:].strip(), {"class": "text", "bbox": None}))
    return out


def _recurring_margin_lines(
    per_page: list[list[tuple[str, str, dict[str, Any]]]], heights: list[float]
) -> set[str]:
    """Normalized lines that sit in the top/bottom margin band on at least two pages."""
    seen: dict[str, set[int]] = {}
    for page_no, parts in enumerate(per_page, start=1):
        for kind, body, box in parts:
            bbox = box.get("bbox")
            if kind in ("removed", "visual") or not bbox or "\n" in body.strip():
                continue
            if bbox[3] <= MARGIN_TOP or bbox[1] >= heights[page_no - 1] * MARGIN_BOTTOM_FRACTION:
                seen.setdefault(_norm_line(body), set()).add(page_no)
    return {line for line, pages in seen.items() if line and len(pages) >= 2}


def _column_index(x0: float, left_edges: list[float]) -> int:
    return min(range(len(left_edges)), key=lambda i: abs(left_edges[i] - x0))


def reorder_column_segments(blocks: list[Block]) -> tuple[list[Block], list[dict[str, Any]]]:
    """Reading-order correction from block geometry.

    A *segment* is a maximal run of consecutive text/list blocks that all have a
    bounding box (captions, tables, visuals, and blocks without a box end a segment and
    keep their place). Only a segment whose order jumps from one column to another and
    back is changed: its blocks are sorted by column (left to right), then top to bottom.
    No text is edited, merged, or dropped here; only the order of whole blocks changes.
    """
    out: list[Block] = []
    changes: list[dict[str, Any]] = []
    segment: list[Block] = []

    def flush() -> None:
        if not segment:
            return
        xs = sorted({b.bbox[0] for b in segment if b.bbox})
        edges: list[float] = []
        for x in xs:
            if not edges or x - edges[-1] > REORDER_COLUMN_GAP:
                edges.append(x)
        cols = [_column_index(b.bbox[0], edges) for b in segment if b.bbox]  # type: ignore[index]
        interleaved = any(
            cols[i] == cols[k] != cols[j]
            for i in range(len(cols))
            for j in range(i + 1, len(cols))
            for k in range(j + 1, len(cols))
        )
        if interleaved:
            order = sorted(
                range(len(segment)),
                key=lambda i: (cols[i], segment[i].bbox[1], i),  # type: ignore[index]
            )
            reordered = [segment[i] for i in order]
            changes.append(
                {
                    "page": segment[0].page,
                    "method": REORDER_METHOD,
                    "columns_detected": len(edges),
                    "before": [b.text[:50] for b in segment],
                    "after": [b.text[:50] for b in reordered],
                }
            )
            out.extend(reordered)
        else:
            out.extend(segment)
        segment.clear()

    for block in blocks:
        if block.kind in ("text", "list") and block.bbox:
            if segment and block.page != segment[0].page:
                flush()
            segment.append(block)
        else:
            flush()
            out.append(block)
    flush()
    return out, changes


def _caption_label(captions: list[str]) -> str | None:
    """'Figure 1' / 'Table 2' from a caption, if one of them names a numbered exhibit."""
    for caption in captions:
        match = re.match(r"\W*(Figure|Fig\.|Table)\s*\d+", caption)
        if match:
            return match.group(0).strip("* ")
    return None


def _has_multilevel_header(markdown: str) -> bool:
    """A spanning (two-row) header leaves empty leading cells or <br>-split cells."""
    rows = [r for r in markdown.splitlines() if r.strip().startswith("|")]
    if not rows:
        return False
    cells = [c.strip() for c in rows[0].strip("|").split("|")]
    return sum(1 for c in cells if not c) >= 2 or any("<br>" in c for c in cells)


def extract_pdf(pdf: Path, image_dir: Path) -> Extraction:
    """Extract blocks in corrected reading order, and name what cannot be represented."""
    doc, chunks = _parse_chunks(pdf)
    heights = [doc[i].rect.height for i in range(len(doc))]
    per_page = [_classify_blocks(c, i + 1) for i, c in enumerate(chunks)]
    recurring = _recurring_margin_lines(per_page, heights)

    blocks: list[Block] = []
    items: list[Item] = []
    removed_lines: list[dict[str, Any]] = []
    counters = {"U": 0, "T": 0, "E": 0}

    def new_id(prefix: str) -> str:
        counters[prefix] += 1
        return f"{prefix}{counters[prefix]}"

    for page_no, parts in enumerate(per_page, start=1):
        captions = [b for k, b, _ in parts if k == "caption"]
        for kind, body, box in parts:
            bbox = box.get("bbox")
            if kind == "removed":
                removed_lines.append({"page": page_no, "text": body, "why": "parser header/footer"})
                continue
            if kind != "visual" and bbox and _norm_line(body) in recurring:
                removed_lines.append(
                    {"page": page_no, "text": body, "why": "recurring margin line (>=2 pages)"}
                )
                continue
            if kind == "visual":
                # Only a captioned, numbered exhibit is annotated. Decorative art (rules,
                # mastheads, pull-quote boxes) carries no content and is left out; the
                # retained page images cover anything this rule misses.
                label = _caption_label(captions)
                if not label:
                    continue
                item_id = new_id("U")
                bbox_list = [round(float(v), 1) for v in bbox] if bbox else None
                items.append(Item(item_id, "figure", page_no, NOTE_FIGURE, label, bbox_list))
                blocks.append(Block("visual", page_no, "", item_id, bbox_list))
                continue
            blocks.append(
                Block(kind, page_no, body, None, [float(v) for v in bbox] if bbox else None)
            )

    blocks, reading_order_changes = reorder_column_segments(blocks)

    # Tables and equations, on the corrected block sequence.
    for index, block in enumerate(blocks):
        if block.kind == "table":
            block.item_id = new_id("T")
            items.append(
                Item(
                    block.item_id,
                    "table",
                    block.page,
                    NOTE_TABLE_MULTILEVEL if _has_multilevel_header(block.text) else NOTE_TABLE,
                    _caption_label([b.text for b in blocks[max(0, index - 2) : index + 3]]),
                    block.bbox,
                )
            )
        elif block.kind in ("text", "list") and _EQUATION_HINT.search(block.text):
            block.item_id = new_id("E")
            items.append(
                Item(block.item_id, "equation", block.page, NOTE_EQUATION, bbox=block.bbox)
            )

    # Only the elements this method cannot represent are cropped and kept. A whole page is
    # rendered from the PDF on demand (the `page` command), never stored speculatively.
    for item in items:
        if not item.bbox:
            continue
        path = image_dir / f"{item.item_id}_p{item.page:02d}.png"
        doc[item.page - 1].get_pixmap(
            dpi=PARSER_SETTINGS["crop_image_dpi"], clip=pymupdf.Rect(*item.bbox)
        ).save(path)
        item.image = f"images/{path.name}"

    return Extraction(
        pages=len(doc),
        blocks=blocks,
        items=items,
        removed_lines=removed_lines,
        printed_labels=_printed_labels(doc),
        pages_without_text=[n for n in range(1, len(doc) + 1) if not doc[n - 1].get_text().strip()],
        reading_order_changes=reading_order_changes,
    )


# --------------------------------------------------------------------------- assembly


@dataclass
class Prepared:
    text: str
    page_map: list[dict[str, Any]]
    annotations: list[dict[str, Any]]
    hyphen_notes: list[dict[str, Any]]


def _hyphen_vocab(blocks: list[Block]) -> tuple[set[str], set[str]]:
    unbroken: set[str] = set()
    hyphenated: set[str] = set()
    for b in blocks:
        plain = re.sub(r"<[^>]+>|[*_`]", "", b.text)
        for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)+", plain):
            hyphenated.add(w.casefold())
        for w in re.findall(r"[A-Za-z]{3,}", plain):
            unbroken.add(w.casefold())
    return unbroken, hyphenated


def _join_hyphen(
    left: str, right: str, vocab: tuple[set[str], set[str]], notes: list[dict[str, Any]], page: int
) -> str:
    """Join text split at an end-of-line hyphen only where the document supports it."""
    unbroken, hyphenated = vocab
    head = re.search(r"([A-Za-z]+)-\s*$", left)
    tail = re.match(r"[A-Za-z]+", right)
    if not head or not tail:
        return left.rstrip() + " " + right
    first, second = head.group(1), tail.group(0)
    prefix, rest = left[: head.start()], right[tail.end() :]
    if f"{first}-{second}".casefold() in hyphenated:
        return prefix + f"{first}-{second}" + rest
    if (first + second).casefold() in unbroken:
        return prefix + first + second + rest
    notes.append(
        {
            "page": page,
            "kind": "ambiguous_hyphenation",
            "text": f"{first}-{second}",
            "kept_as": f"{first}-{second}",
        }
    )
    return prefix + f"{first}-{second}" + rest


def assemble(extraction: Extraction) -> Prepared:
    """Build the analyzer text: blocks in reading order, each item's annotation after it."""
    vocab = _hyphen_vocab(extraction.blocks)
    notes: list[dict[str, Any]] = []
    paragraphs: list[dict[str, Any]] = []
    items = {i.item_id: i for i in extraction.items}

    def annotate(item: Item) -> str:
        fields = {"kind": item.kind, "page": str(item.page)}
        if item.label:
            fields["label"] = item.label
        if item.image:
            fields["image"] = item.image
        return format_annotation(item.item_id, fields, item.note)

    for block in extraction.blocks:
        if block.kind != "visual":
            paragraphs.append(
                {"text": block.text, "page": block.page, "mergeable": block.kind == "text"}
            )
        if block.item_id:
            annotation = annotate(items[block.item_id])
            paragraphs.append({"text": annotation, "page": block.page, "mergeable": False})

    merged: list[dict[str, Any]] = []
    for para in paragraphs:
        prev = merged[-1] if merged else None
        if (
            prev
            and para["mergeable"]
            and prev["mergeable"]
            and para["text"][:1].islower()
            and _midsentence(prev["text"])
        ):
            if _plain(prev["text"]).endswith("-"):
                new_text = _join_hyphen(prev["text"], para["text"], vocab, notes, para["page"])
                start = len(new_text) - len(para["text"])
            else:
                new_text = prev["text"].rstrip() + " " + para["text"]
                start = len(prev["text"].rstrip()) + 1
            prev["pieces"].append((para["page"], max(start, 0)))
            prev["text"] = new_text
        else:
            merged.append(dict(para, pieces=[(para["page"], 0)]))

    # within-paragraph "word- word" breaks left by the parser
    for para in merged:

        def fix(match: re.Match[str], para: dict[str, Any] = para) -> str:
            first, second = match.group(1), match.group(2)
            if f"{first}-{second}".casefold() in vocab[1]:
                return f"{first}-{second}"
            if (first + second).casefold() in vocab[0]:
                return first + second
            notes.append(
                {
                    "page": para["pieces"][0][0],
                    "kind": "ambiguous_hyphenation",
                    "text": f"{first}- {second}",
                    "kept_as": f"{first}- {second}",
                }
            )
            return match.group(0)

        para["text"] = re.sub(r"([A-Za-z]{2,})- ([a-z]{2,})", fix, para["text"])

    text = ""
    page_starts: dict[int, int] = {}
    for para in merged:
        base = len(text)
        for page, start in para["pieces"]:
            page_starts.setdefault(page, base + min(start, max(len(para["text"]) - 1, 0)))
        text += para["text"] + "\n\n"
    text = text.rstrip() + "\n"

    # Every PDF page gets an entry. A page that contributed no text says so, so that a
    # missing entry always means something went wrong rather than "this page was quiet".
    ordered = sorted(page_starts.items())
    spans = {
        page: (start, ordered[i + 1][1] if i + 1 < len(ordered) else len(text))
        for i, (page, start) in enumerate(ordered)
    }
    page_map: list[dict[str, Any]] = []
    for page in range(1, extraction.pages + 1):
        span = spans.get(page)
        entry: dict[str, Any] = {
            "pdf_page": page,
            "printed_label": extraction.printed_labels.get(page),
            "mapped_text": span is not None,
            "start_offset": span[0] if span else None,
            "end_offset": span[1] if span else None,
        }
        if span is None:
            entry["why"] = NO_MAPPED_TEXT
        page_map.append(entry)
    annotations = [
        {
            "id": span.annotation_id,
            "start_offset": span.start,
            "end_offset": span.end,
            "kind": items[span.annotation_id].kind,
            "page": items[span.annotation_id].page,
            "label": items[span.annotation_id].label,
            "image": items[span.annotation_id].image,
        }
        for span in find_annotations(text)
    ]
    return Prepared(text=text, page_map=page_map, annotations=annotations, hyphen_notes=notes)


# --------------------------------------------------------------------------- orchestration


def _write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _provenance_json(entry: ManifestEntry) -> dict[str, Any]:
    data = entry.model_dump(
        mode="json",
        include={
            "source_title",
            "source_authors",
            "publication_date",
            "source_type",
            "doi",
            "publisher",
            "url",
            "retrieved_at",
        },
    )
    return {k: v for k, v in data.items() if v not in (None, [])}


def prepare_source(
    entry: ManifestEntry, output_root: Path, *, max_characters: int
) -> dict[str, Any]:
    """Prepare one source. Returns a summary; writes the text and records to disk."""
    pdf = (REPO_ROOT / entry.pdf) if not Path(entry.pdf).is_absolute() else Path(entry.pdf)
    out = output_root / entry.slug
    (out / "images").mkdir(parents=True, exist_ok=True)
    for stale in (out / "images").glob("*.png"):
        stale.unlink()

    started = time.monotonic()
    started_at = now_utc()
    extraction = extract_pdf(pdf, out / "images")
    prepared = assemble(extraction)
    problems = reserved_character_problems(prepared.text)
    if problems:
        raise ValueError("; ".join(problems))
    elapsed = time.monotonic() - started

    (out / "prepared_text.md").write_text(prepared.text, encoding="utf-8")
    _write_json(out / "page_map.json", prepared.page_map)
    _write_json(out / "provenance.json", _provenance_json(entry))
    record = {
        "slug": entry.slug,
        "source_pdf": entry.pdf,
        "pdf_sha256": sha256_file(pdf),
        "prepared_text": "prepared_text.md",
        "prepared_text_sha256": sha256_bytes(prepared.text.encode("utf-8")),
        "prepared_text_characters": len(prepared.text),
        "max_source_characters": max_characters,
        "within_size_limit": len(prepared.text) <= max_characters,
        "is_excerpt": entry.is_excerpt,
        "excerpt_description": entry.excerpt_description,
        "parser": {"name": PARSER_NAME, "version": PARSER_VERSION, "pymupdf": pymupdf.__version__},
        "parser_settings": PARSER_SETTINGS,
        "settings_sha256": settings_sha256(),
        "script_sha256": script_sha256(),
        "pages": extraction.pages,
        "timing": {
            "started_at_utc": started_at,
            "elapsed_seconds": round(elapsed, 2),
            "measured": "wall clock of extraction, assembly and record writing",
            "model_calls": 0,
            "usage": "no model usage: local extraction only",
        },
        "provenance_basis": entry.provenance_basis,
        "cleanup_applied": [
            "parser header/footer removal; recurring margin lines removed (listed below)",
            "continuation paragraphs joined only when the previous ends mid-sentence and the "
            "next starts lowercase; end-of-line hyphens joined or kept only where the "
            "document's own text supports it, otherwise kept as extracted and listed",
            "no paraphrasing, summarizing, or reconstruction",
        ],
        "reading_order_changes": extraction.reading_order_changes,
        "removed_lines": extraction.removed_lines,
        "hyphenation_notes": prepared.hyphen_notes,
        "annotations": prepared.annotations,
        "pages_without_text_layer_ocr_off": extraction.pages_without_text,
        "preparation_limits": PREPARATION_LIMITS,
        "retained_images": sorted(p.name for p in (out / "images").glob("*.png")),
    }
    _write_json(out / "prep_record.json", record)
    return {
        "slug": entry.slug,
        "characters": len(prepared.text),
        "within_size_limit": record["within_size_limit"],
        "pages": extraction.pages,
        "annotations": len(prepared.annotations),
        "reading_order_changes": len(extraction.reading_order_changes),
        "pages_without_text_layer": extraction.pages_without_text,
        "elapsed_seconds": round(elapsed, 2),
        "directory": str(out),
    }


def render_page(entry: ManifestEntry, output_root: Path, page_no: int) -> Path:
    """Render one whole page from the original PDF, for a human who needs to look."""
    pdf = (REPO_ROOT / entry.pdf) if not Path(entry.pdf).is_absolute() else Path(entry.pdf)
    doc = pymupdf.open(pdf)
    if not 1 <= page_no <= len(doc):
        raise ValueError(f"page {page_no} is outside this {len(doc)}-page PDF")
    out = output_root / entry.slug / "images"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"page_{page_no:02d}.png"
    doc[page_no - 1].get_pixmap(dpi=PARSER_SETTINGS["page_image_dpi"]).save(path)
    return path


# --------------------------------------------------------------------------- CLI


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "page"):
        p = sub.add_parser(name)
        p.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
        p.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
        p.add_argument("--slug", required=True)
        if name == "page":
            p.add_argument("--page", type=int, required=True, help="PDF page number to render")
    args = parser.parse_args(argv)

    entries = {e.slug: e for e in load_manifest(args.manifest)}
    if args.slug not in entries:
        print(f"unknown slug {args.slug!r}", file=sys.stderr)
        return 2
    if args.command == "page":
        print(render_page(entries[args.slug], args.output_root, args.page))
        return 0
    summary = prepare_source(
        entries[args.slug], args.output_root, max_characters=Settings().max_source_characters
    )
    print(json.dumps(summary, indent=2))
    if not summary["within_size_limit"]:
        print("prepared text is over max_source_characters", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"manifest error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
