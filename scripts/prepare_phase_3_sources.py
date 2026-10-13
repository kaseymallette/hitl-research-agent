"""Shared Phase 3 source preparation: PDF -> prepared text plus audit records.

One process for every PDF (no per-source code, no tool switching):

    python scripts/prepare_phase_3_sources.py prepare --slug SLUG
    python scripts/prepare_phase_3_sources.py status  --slug SLUG
    python scripts/prepare_phase_3_sources.py approve --slug SLUG --statement "..."

What it does, per the Phase 3 plan:

* extracts text and tables with ``pymupdf4llm`` (pinned; layout mode; header/footer
  removal on; OCR off) and renders page images with PyMuPDF;
* cleans conservatively: recurring headers/footers removed, wraps/hyphenation repaired
  only where the document's own text supports it, nothing paraphrased or reconstructed;
* keeps page locators in a separate mapping, never inside the text;
* never estimates chart values or interprets figures/equations. Anything it cannot
  extract faithfully becomes an *unresolved item* shown to the analyzer as a labeled
  preparation annotation (see ``hitl_research_agent.extraction.annotations``);
* checks the result against the PDF's own text layer and reports flags that must be
  spot-checked against the page images. Automated checks cannot prove correct reading
  order or complete visual coverage, and the records say so;
* assigns a status: ``ready`` / ``ready_with_unresolved`` / ``blocked``. A
  ``ready_with_unresolved`` source needs an explicit, source-specific approval record
  before analysis; a ``blocked`` source cannot proceed.

Verification findings are stored separately from hashes: matching hashes show that an
extraction is unchanged, not that it was verified.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import time
from collections import Counter
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
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "outputs" / "phase_3" / "prepared"

PARSER_NAME = "pymupdf4llm"
PARSER_VERSION = pymupdf4llm.__version__ if hasattr(pymupdf4llm, "__version__") else "unknown"
# Settings verified against the installed version (see tests/preparation and the
# verification notes in the Phase 3 report): layout mode keeps tables and exposes
# page boxes; header/footer/OCR arguments are honored (legacy mode ignores them and
# drops Table 1 on the Li paper).
PARSER_SETTINGS: dict[str, Any] = {
    "layout_mode": True,
    "header": False,
    "footer": False,
    "use_ocr": False,
    "page_chunks": True,
    "page_image_dpi": 130,
    "crop_image_dpi": 200,
}

REORDER_METHOD = "geometry_column_segments_v1"
REORDER_COLUMN_GAP = 40.0  # points between column left edges that separate columns

STATUS_READY = "ready"
STATUS_UNRESOLVED = "ready_with_unresolved"
STATUS_BLOCKED = "blocked"

COVERAGE_REVIEW_BELOW = 0.97
COVERAGE_BLOCK_BELOW = 0.85
MARGIN_TOP = 70.0
MARGIN_BOTTOM_FRACTION = 0.95
ANNOTATION_NOTE = "not source text; content not extracted"
TERMINAL = (".", "?", "!", ":", "”", '"', ")", "]")
_EQUATION_HINT = re.compile(r"[∑∫√∏⋯±≈≤≥∂\u0370-\u03ff]|<sup>[A-Za-z][A-Za-z ]{3,}</sup>")
CLEARED_RESULTS = {"confirmed_ok", "decorative_no_content"}
REVIEW_RESULTS = CLEARED_RESULTS | {"confirmed_problem", "limitation", "uncertain"}

AUTOMATED_LIMITATIONS = [
    "Word coverage compares the extraction with the PDF text layer; it detects dropped or "
    "altered words, not wrong ordering.",
    "Continuity and column-geometry checks flag some reading-order problems; they cannot "
    "prove reading order is correct.",
    "Visual detection uses parser page boxes and embedded-image bounding boxes; it cannot "
    "prove every figure, diagram, or equation was found.",
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


def settings_sha256(reorder_columns: bool = False) -> str:
    """Hash of the parser and its settings. The opt-in column reordering is part of the
    settings only when enabled, so the default hash is unchanged by that option."""
    settings: dict[str, Any] = dict(PARSER_SETTINGS)
    if reorder_columns:
        settings["reorder_columns"] = REORDER_METHOD
    payload = json.dumps(
        {"parser": PARSER_NAME, "version": PARSER_VERSION, "settings": settings}, sort_keys=True
    )
    return sha256_bytes(payload.encode())


def now_utc() -> str:
    return datetime.now(UTC).isoformat()


# --------------------------------------------------------------------------- text helpers

_TOKEN = re.compile(r"[0-9A-Za-zÀ-ɏ]+")


def tokens(text: str) -> list[str]:
    """Alphanumeric tokens, case-folded, with markup (tags, emphasis, table bars) ignored."""
    stripped = re.sub(r"<[^>]+>|[*_#|>`]", " ", text)
    return [t.casefold() for t in _TOKEN.findall(stripped)]


def _plain(text: str) -> str:
    return re.sub(r"\*\*|<sup>.*?</sup>", "", text).rstrip()


def _norm_line(text: str) -> str:
    plain = re.sub(r"[*_#`>|]|<[^>]+>", "", text)
    return re.sub(r"\d+", "#", re.sub(r"\s+", " ", plain)).strip().casefold()


# --------------------------------------------------------------------------- extraction


@dataclass
class Block:
    """One paragraph-level unit in reading order, before final assembly."""

    kind: str  # text | list | caption | heading | table | visual
    page: int
    text: str
    item_id: str | None = None  # visual/table items link here
    bbox: list[float] | None = None


@dataclass
class Item:
    """Something that needs review or is unresolved: visual, table, equation, flag."""

    item_id: str
    category: (
        str  # visual | image_only_page | table | equation | reading_order | coverage | hyphenation
    )
    kind: str
    page: int
    reason: str
    label: str | None = None
    bbox: list[float] | None = None
    image: str | None = None
    page_image: str | None = None
    detail: dict[str, Any] = field(default_factory=dict)


@dataclass
class Extraction:
    pages: int
    blocks: list[Block]
    items: list[Item]
    page_coverage: list[dict[str, Any]]
    removed_lines: list[dict[str, Any]]
    altered_words: list[dict[str, Any]]
    label_fragments: dict[str, str]
    printed_labels: dict[int, str | None]
    image_counts: list[dict[str, Any]]
    unreadable_pages: list[int]
    reading_order_changes: list[dict[str, Any]] = field(default_factory=list)


def _parse_chunks(pdf: Path) -> tuple[pymupdf.Document, list[dict[str, Any]], str]:
    pymupdf4llm.use_layout(PARSER_SETTINGS["layout_mode"])
    doc = pymupdf.open(pdf)
    chunks = pymupdf4llm.to_markdown(
        doc,
        page_chunks=True,
        header=PARSER_SETTINGS["header"],
        footer=PARSER_SETTINGS["footer"],
        use_ocr=PARSER_SETTINGS["use_ocr"],
    )
    return doc, chunks, "ok"


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


def _classify_blocks(
    chunk: dict[str, Any],
    page_no: int,
    visual_texts: dict[int, str],
) -> list[tuple[str, str, dict[str, Any]]]:
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
            fragments = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
            visual_texts[len(visual_texts)] = fragments
            out.append(("visual", fragments, box))
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
    """Opt-in, narrowly scoped reading-order correction from block geometry.

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


def extract_pdf(pdf: Path, image_dir: Path, *, reorder_columns: bool = False) -> Extraction:
    """Run the shared extraction and the automated checks. Pure data; no judgement calls."""
    doc, chunks, _ = _parse_chunks(pdf)
    heights = [doc[i].rect.height for i in range(len(doc))]
    visual_texts: dict[int, str] = {}
    per_page = [_classify_blocks(c, i + 1, visual_texts) for i, c in enumerate(chunks)]
    recurring = _recurring_margin_lines(per_page, heights)

    blocks: list[Block] = []
    items: list[Item] = []
    removed_lines: list[dict[str, Any]] = []
    label_fragments: dict[str, str] = {}
    page_coverage: list[dict[str, Any]] = []
    image_counts: list[dict[str, Any]] = []
    unreadable: list[int] = []
    counters = {"U": 0, "T": 0, "E": 0, "C": 0, "H": 0, "P": 0}

    def new_id(prefix: str) -> str:
        counters[prefix] += 1
        return f"{prefix}{counters[prefix]}"

    printed_labels = _printed_labels(doc)
    pages_needing_image: set[int] = set()
    margin_bands: dict[int, list[list[float]]] = {}
    picture_boxes: dict[int, list[list[float]]] = {}

    for page_no, parts in enumerate(per_page, start=1):
        page = doc[page_no - 1]
        margin_bands[page_no] = []
        picture_boxes[page_no] = []
        captions = [b for k, b, _ in parts if k == "caption"]
        pictures = [p for p in parts if p[0] == "visual"]
        for kind, body, box in parts:
            bbox = box.get("bbox")
            if kind == "removed":
                removed_lines.append({"page": page_no, "text": body, "why": "parser header/footer"})
                if bbox:
                    margin_bands[page_no].append(bbox)
                continue
            if kind != "visual" and bbox and _norm_line(body) in recurring:
                removed_lines.append(
                    {"page": page_no, "text": body, "why": "recurring margin line (>=2 pages)"}
                )
                margin_bands[page_no].append(bbox)
                continue
            if kind == "visual":
                item_id = new_id("U")
                label = None
                if len(pictures) == 1 and len(captions) == 1:
                    match = re.match(r"\W*(Figure|Fig\.|Table)\s*\d+", captions[0])
                    label = match.group(0).strip("* ") if match else None
                bbox_list = [round(float(v), 1) for v in bbox] if bbox else None
                if bbox_list:
                    picture_boxes[page_no].append(bbox_list)
                items.append(
                    Item(
                        item_id,
                        "visual",
                        "figure" if body else "picture",
                        page_no,
                        "figure or picture; its content is not extracted"
                        if body
                        else "picture with no extractable text",
                        label=label,
                        bbox=bbox_list,
                    )
                )
                if body:
                    label_fragments[item_id] = body
                blocks.append(Block("visual", page_no, "", item_id, bbox_list))
                pages_needing_image.add(page_no)
                continue
            blocks.append(
                Block(kind, page_no, body, None, [float(v) for v in bbox] if bbox else None)
            )

        # embedded images not covered by any picture box (e.g. a full-page illustration)
        infos = page.get_image_info()
        stray = [
            i
            for i in infos
            if not any(_overlaps(i["bbox"], pb) for pb in picture_boxes[page_no])
            and (i["bbox"][2] - i["bbox"][0]) * (i["bbox"][3] - i["bbox"][1]) > 2500
        ]
        image_counts.append(
            {
                "page": page_no,
                "embedded_images": len(infos),
                "images_not_in_a_picture_box": len(stray),
                "vector_drawings": len(page.get_drawings()),
            }
        )
        if stray:
            item_id = new_id("U")
            area = max((i["bbox"][2] - i["bbox"][0]) * (i["bbox"][3] - i["bbox"][1]) for i in stray)
            page_area = page.rect.width * page.rect.height
            kind = "image_only_page" if area / page_area > 0.6 else "image"
            items.append(
                Item(
                    item_id,
                    "image_only_page" if kind == "image_only_page" else "visual",
                    kind,
                    page_no,
                    "embedded image outside any detected picture box; its content is not extracted",
                    bbox=None,
                )
            )
            blocks.append(Block("visual", page_no, "", item_id, None))
            pages_needing_image.add(page_no)

    reading_order_changes: list[dict[str, Any]] = []
    if reorder_columns:
        blocks, reading_order_changes = reorder_column_segments(blocks)
    altered: list[dict[str, Any]] = _hyphen_joins(doc, blocks)

    # ---- tables, equations, flags on the cleaned block sequence
    page_tokens = {
        n: tokens(" ".join(b.text for b in blocks if b.page == n)) for n in range(1, len(doc) + 1)
    }
    pdf_words = {
        n: _page_words(doc[n - 1], margin_bands[n], picture_boxes[n])
        for n in range(1, len(doc) + 1)
    }
    all_pdf_vocab = {w for ws in pdf_words.values() for w in ws}

    new_blocks: list[Block] = []
    for index, block in enumerate(blocks):
        new_blocks.append(block)
        if block.kind == "table":
            problems = _table_problems(block.text, all_pdf_vocab)
            item_id = new_id("T")
            block.item_id = item_id
            if problems:
                items.append(
                    Item(
                        item_id,
                        "table",
                        "table_header_or_alignment",
                        block.page,
                        "; ".join(problems),
                        label=_table_label(blocks, index),
                        bbox=block.bbox,
                    )
                )
            else:
                items.append(
                    Item(
                        item_id,
                        "table",
                        "table_extracted",
                        block.page,
                        "table rows and header passed the automated checks",
                        label=_table_label(blocks, index),
                        bbox=block.bbox,
                        detail={"automated": "pass"},
                    )
                )
            pages_needing_image.add(block.page)
        elif block.kind in ("text", "list") and _EQUATION_HINT.search(block.text):
            item_id = new_id("E")
            items.append(
                Item(
                    item_id,
                    "equation",
                    "equation_like_text",
                    block.page,
                    "paragraph contains symbols or subscript/superscript runs typical of an "
                    "equation whose text layer may not be faithful",
                    detail={"paragraph_excerpt": block.text[:240]},
                )
            )
            block.item_id = item_id
            pages_needing_image.add(block.page)

    blocks = new_blocks

    ambiguous_joins = [a for a in altered if a["resolution"].startswith("ambiguous")]
    if ambiguous_joins:
        item_id = new_id("H")
        items.append(
            Item(
                item_id,
                "hyphenation",
                "ambiguous_hyphen_joins",
                ambiguous_joins[0]["page"],
                f"{len(ambiguous_joins)} word(s) were joined across an end-of-line hyphen with no "
                "corroboration in the PDF; kept as the parser produced them",
                detail={"words": ambiguous_joins},
            )
        )
        pages_needing_image.add(ambiguous_joins[0]["page"])

    # reading-order and continuity flags
    for flag in _continuity_flags(blocks) + _column_geometry_flags(blocks):
        item_id = new_id("C")
        items.append(
            Item(item_id, "reading_order", flag["kind"], flag["page"], flag["reason"], detail=flag)
        )
        pages_needing_image.add(flag["page"])

    # word coverage per page against the PDF text layer
    for n in range(1, len(doc) + 1):
        pdf_text = "".join(pdf_words[n])
        ext_text = "".join(page_tokens[n])
        total = len(pdf_words[n])
        pdf_grams = Counter(pdf_text[i : i + 5] for i in range(max(len(pdf_text) - 4, 0)))
        ext_grams = Counter(ext_text[i : i + 5] for i in range(max(len(ext_text) - 4, 0)))
        gram_total = sum(pdf_grams.values())
        coverage = (
            1.0 if gram_total == 0 else 1 - sum((pdf_grams - ext_grams).values()) / gram_total
        )
        missing = Counter(w for w in pdf_words[n] if len(w) >= 4 and w not in ext_text)
        page_coverage.append(
            {
                "page": n,
                "pdf_words": total,
                "coverage_method": "character 5-gram overlap of PDF text layer vs extraction "
                "(tolerant of line-end hyphen joins and superscript spacing)",
                "coverage": round(coverage, 4),
                "pdf_words_not_found_in_extraction_sample": [w for w, _ in missing.most_common(15)],
            }
        )
        if total == 0:
            if any(b.page == n and b.kind == "visual" for b in blocks):
                unreadable.append(n)
        elif coverage < COVERAGE_REVIEW_BELOW:
            item_id = new_id("P")
            items.append(
                Item(
                    item_id,
                    "coverage",
                    "word_coverage",
                    n,
                    f"word coverage {coverage:.1%} is below {COVERAGE_REVIEW_BELOW:.0%}",
                    detail={
                        "coverage": round(coverage, 4),
                        "pdf_words_not_found": [w for w, _ in missing.most_common(30)],
                    },
                )
            )
            pages_needing_image.add(n)

    for n in sorted(pages_needing_image):
        path = image_dir / f"pdf_p{n:02d}_page.png"
        doc[n - 1].get_pixmap(dpi=PARSER_SETTINGS["page_image_dpi"]).save(path)
    for item in items:
        if item.page in pages_needing_image:
            item.page_image = f"images/pdf_p{item.page:02d}_page.png"
        if item.bbox and item.category in ("visual", "table"):
            clip = pymupdf.Rect(*item.bbox)
            path = image_dir / f"{item.item_id}_p{item.page:02d}.png"
            doc[item.page - 1].get_pixmap(dpi=PARSER_SETTINGS["crop_image_dpi"], clip=clip).save(
                path
            )
            item.image = f"images/{path.name}"
        elif item.page_image:
            item.image = item.page_image

    return Extraction(
        pages=len(doc),
        blocks=blocks,
        items=items,
        page_coverage=page_coverage,
        removed_lines=removed_lines,
        altered_words=altered,
        label_fragments=label_fragments,
        printed_labels=printed_labels,
        image_counts=image_counts,
        unreadable_pages=unreadable,
        reading_order_changes=reading_order_changes,
    )


def _hyphen_joins(doc: pymupdf.Document, blocks: list[Block]) -> list[dict[str, Any]]:
    """Words the parser joined across an end-of-line hyphen in the PDF text layer.

    * joined form occurs elsewhere as a standalone word -> corroborated, nothing to do;
    * hyphenated form occurs elsewhere inside a line -> the hyphen is corroborated and is
      restored in the blocks (the original text supports it);
    * neither -> ambiguous: kept as the parser produced it and listed for review.
    """
    inline_hyphenated: set[str] = set()
    standalone: set[str] = set()
    pairs: list[tuple[int, str, str]] = []
    for page in doc:
        words = page.get_text("words")
        for index, (_x0, _y0, _x1, _y1, word, block_no, line_no, _w) in enumerate(words):
            clean = word.strip()
            if re.fullmatch(r"[A-Za-z]+(?:-[A-Za-z]+)+", clean):
                inline_hyphenated.add(clean.casefold())
            elif re.fullmatch(r"[A-Za-z]{3,}", clean):
                standalone.add(clean.casefold())
            if re.fullmatch(r"[A-Za-z]{2,}-", clean) and index + 1 < len(words):
                nxt = words[index + 1]
                if (
                    nxt[5] == block_no
                    and nxt[6] == line_no + 1
                    and re.fullmatch(r"[A-Za-z0-9]{2,}", nxt[4])
                ):
                    pairs.append((page.number + 1, clean[:-1], nxt[4]))
    results: list[dict[str, Any]] = []
    for page_no, first, second in pairs:
        joined, hyphenated = (first + second).casefold(), f"{first}-{second}".casefold()
        if hyphenated in inline_hyphenated:
            for block in blocks:
                if block.page == page_no and joined in block.text.casefold():
                    block.text = re.sub(
                        re.escape(first + second), f"{first}-{second}", block.text, flags=re.I
                    )
            results.append(
                {
                    "page": page_no,
                    "word": f"{first}-{second}",
                    "resolution": "hyphen restored (the hyphenated form occurs inside a line "
                    "elsewhere in the PDF)",
                }
            )
        elif joined in standalone:
            continue
        else:
            results.append(
                {
                    "page": page_no,
                    "word": first + second,
                    "pdf_line_break": f"{first}- / {second}",
                    "resolution": "ambiguous: the PDF breaks the word at a hyphen and nothing in "
                    "the document shows whether it is a line-break hyphen or part of a "
                    "compound; kept as the parser produced it",
                }
            )
    return results


def _overlaps(a: Any, b: Any) -> bool:
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def _page_words(
    page: pymupdf.Page, margin_boxes: list[list[float]], picture_boxes: list[list[float]]
) -> list[str]:
    """PDF text-layer tokens outside removed header/footer bands and picture boxes."""
    height = page.rect.height
    out: list[str] = []
    for x0, y0, x1, y1, word, *_rest in page.get_text("words"):
        box = [x0, y0, x1, y1]
        if y1 <= MARGIN_TOP or y0 >= height * MARGIN_BOTTOM_FRACTION:
            continue
        if any(_overlaps(box, m) for m in margin_boxes + picture_boxes):
            continue
        out.extend(tokens(word))
    return out


def _table_label(blocks: list[Block], index: int) -> str | None:
    for neighbor in blocks[max(0, index - 2) : index + 3]:
        if neighbor.kind == "caption":
            match = re.match(r"\W*(Table|Figure|Fig\.)\s*\d+", neighbor.text)
            if match:
                return match.group(0).strip("* ")
    return None


def _table_problems(markdown: str, pdf_vocab: set[str]) -> list[str]:
    rows = [line for line in markdown.splitlines() if line.startswith("|")]
    if len(rows) < 3:
        return ["table has fewer than three rows"]
    widths = {line.count("|") for line in rows}
    problems: list[str] = []
    if len(widths) != 1:
        problems.append(f"rows have inconsistent column counts {sorted(widths)}")
    header_cells = [c for line in rows[:2] for c in line.strip("|").split("|")]
    stray = sorted(
        {t for c in header_cells for t in tokens(c) if len(t) >= 2 and t not in pdf_vocab}
    )
    if stray:
        problems.append(
            "header text contains fragments that are not words in the PDF text layer: "
            + ", ".join(stray[:8])
        )
    if any(not c.strip() for c in rows[0].strip("|").split("|")):
        problems.append("header row has empty cells (merged or multi-level header not captured)")
    return problems


def _continuity_flags(blocks: list[Block]) -> list[dict[str, Any]]:
    flags: list[dict[str, Any]] = []
    prose = [b for b in blocks if b.kind in ("text", "list", "caption", "table", "visual")]
    for before, after in zip(prose, prose[1:], strict=False):
        if before.kind != "text" or after.kind != "text":
            if before.kind == "text" and _midsentence(before.text) and after.kind != "text":
                flags.append(
                    _flag(
                        "interrupted_sentence",
                        before,
                        f"text ends mid-sentence before a {after.kind}",
                        before.text[-60:],
                    )
                )
            continue
        ends_open = _midsentence(before.text)
        if ends_open and after.text[:1].isupper() and not _starts_new_unit(after.text):
            flags.append(
                _flag(
                    "mid_sentence_then_capital",
                    after,
                    "paragraph ends mid-sentence but the next starts with a capital",
                    before.text[-50:] + " || " + after.text[:50],
                )
            )
        if not ends_open and after.text[:1].islower():
            flags.append(
                _flag(
                    "lowercase_after_finished_sentence",
                    after,
                    "paragraph starts lowercase after a finished sentence",
                    before.text[-50:] + " || " + after.text[:50],
                )
            )
    return flags


def _midsentence(text: str) -> bool:
    plain = _plain(text.strip())
    return bool(plain) and not plain.endswith(TERMINAL)


def _starts_new_unit(text: str) -> bool:
    return text.startswith(("#", "*", "-", ">", "|", "_", "[")) or bool(re.match(r"\d+\.\s", text))


def _flag(kind: str, block: Block, reason: str, excerpt: str) -> dict[str, Any]:
    return {"kind": kind, "page": block.page, "reason": reason, "excerpt": excerpt}


def _column_geometry_flags(blocks: list[Block]) -> list[dict[str, Any]]:
    """Flag a column-to-column jump that immediately jumps back (interleaved columns)."""
    flags: list[dict[str, Any]] = []
    by_page: dict[int, list[Block]] = {}
    for b in blocks:
        if b.bbox and b.kind in ("text", "list"):
            by_page.setdefault(b.page, []).append(b)
    for page, seq in by_page.items():
        for a, b, c in zip(seq, seq[1:], seq[2:], strict=False):
            if abs(a.bbox[0] - c.bbox[0]) < 25 and abs(a.bbox[0] - b.bbox[0]) > 100:  # type: ignore[index]
                flags.append(
                    {
                        "kind": "column_interleaving",
                        "page": page,
                        "reason": "reading order jumps to another column and back",
                        "excerpt": b.text[:60],
                    }
                )
    return flags


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
    prefix = left[: head.start()]
    rest = right[tail.end() :]
    joined = (first + second).casefold()
    hyph = f"{first}-{second}".casefold()
    if hyph in hyphenated:
        return prefix + f"{first}-{second}" + rest
    if joined in unbroken:
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


def assemble(
    extraction: Extraction,
    dispositions: dict[str, str],
    image_of: dict[str, str],
) -> Prepared:
    """Build the analyzer text. `dispositions[item_id]` in CLEARED_RESULTS suppresses that
    item's annotation; every other visual/table/equation item is annotated."""
    vocab = _hyphen_vocab(extraction.blocks)
    notes: list[dict[str, Any]] = []
    paragraphs: list[dict[str, Any]] = []  # {"text": str, "pieces": [(page, start)]}
    annotations: list[dict[str, Any]] = []
    items = {i.item_id: i for i in extraction.items}

    def annotate(item: Item) -> str:
        fields = {"kind": item.kind, "page": str(item.page)}
        if item.label:
            fields["label"] = item.label
        if item.image:
            fields["image"] = item.image
        return format_annotation(item.item_id, fields, ANNOTATION_NOTE)

    def uncleared(item_id: str | None) -> Item | None:
        if not item_id:
            return None
        item = items[item_id]
        if dispositions.get(item_id) in CLEARED_RESULTS:
            return None
        if (
            item.category == "table"
            and item.detail.get("automated") == "pass"
            and item_id not in dispositions
        ):
            return None
        return item

    pending: list[Block] = []
    for block in extraction.blocks:
        if block.kind == "visual":
            item = uncleared(block.item_id)
            if item:
                paragraphs.append(
                    {"text": annotate(item), "pieces": [(block.page, 0)], "mergeable": False}
                )
            continue
        paragraphs.append(
            {"text": block.text, "pieces": [(block.page, 0)], "mergeable": block.kind == "text"}
        )
        item = uncleared(block.item_id) if block.kind in ("table", "text", "list") else None
        if item:
            paragraphs.append(
                {"text": annotate(item), "pieces": [(block.page, 0)], "mergeable": False}
            )
    del pending

    merged: list[dict[str, Any]] = []
    for para in paragraphs:
        if (
            merged
            and para["mergeable"]
            and merged[-1]["mergeable"]
            and para["text"][:1].islower()
            and _midsentence(merged[-1]["text"])
        ):
            prev = merged[-1]
            page = para["pieces"][0][0]
            if _plain(prev["text"]).endswith("-"):
                left = prev["text"]
                new_text = _join_hyphen(left, para["text"], vocab, notes, page)
                start = len(new_text) - len(para["text"]) + 0
            else:
                new_text = prev["text"].rstrip() + " " + para["text"]
                start = len(prev["text"].rstrip()) + 1
            prev["pieces"].append((page, max(start, 0)))
            prev["text"] = new_text
        else:
            merged.append(dict(para, pieces=list(para["pieces"])))

    # within-paragraph "word- word" breaks left by the parser
    for para in merged:

        def fix(match: re.Match[str], para: dict[str, Any] = para) -> str:
            first, second = match.group(1), match.group(2)
            hyph = f"{first}-{second}".casefold()
            if hyph in vocab[1]:
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

    ordered = sorted(page_starts.items())
    page_map = []
    for i, (page, start) in enumerate(ordered):
        end = ordered[i + 1][1] if i + 1 < len(ordered) else len(text)
        page_map.append(
            {
                "pdf_page": page,
                "printed_label": extraction.printed_labels.get(page),
                "start_offset": start,
                "end_offset": end,
            }
        )
    for span in find_annotations(text):
        item = items.get(span.annotation_id)
        annotations.append(
            {
                "id": span.annotation_id,
                "start_offset": span.start,
                "end_offset": span.end,
                "kind": item.kind if item else None,
                "page": item.page if item else None,
                "label": item.label if item else None,
                "image": image_of.get(span.annotation_id) or (item.image if item else None),
            }
        )
    return Prepared(text=text, page_map=page_map, annotations=annotations, hyphen_notes=notes)


# --------------------------------------------------------------------------- review / status


def load_review(
    directory: Path, bound: dict[str, str]
) -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    """Reviews bound to the current hashes; stale reviews are archived and ignored.

    Returns (reviews by item id, review metadata: reviewer, time, free-form notes)."""
    path = directory / "review.json"
    if not path.exists():
        return {}, {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("bound_to") != bound:
        _archive(directory, ["review.json", "approval.json"], reason="hash change reset review")
        return {}, {}
    out: dict[str, dict[str, str]] = {}
    for review in data.get("reviews", []):
        if review["result"] not in REVIEW_RESULTS:
            raise ValueError(f"unknown review result {review['result']!r}")
        out[review["item"]] = review
    meta = {k: data.get(k) for k in ("reviewed_by", "reviewed_at", "notes", "method")}
    return out, meta


def _archive(directory: Path, names: list[str], reason: str) -> None:
    present = [n for n in names if (directory / n).exists()]
    if not present:
        return
    target = directory / "superseded" / datetime.now(UTC).strftime("%Y%m%dT%H%M%S%fZ")
    target.mkdir(parents=True, exist_ok=True)
    for name in present:
        shutil.move(str(directory / name), str(target / name))
    (target / "REASON.txt").write_text(reason + "\n", encoding="utf-8")


def compute_status(
    extraction: Extraction,
    reviews: dict[str, dict[str, str]],
    text_length: int,
    limit: int,
) -> tuple[str, list[str], list[dict[str, Any]]]:
    """Return (status, reasons, unresolved item list). Conservative: an item with no
    review, or any review other than confirmed_ok / decorative_no_content, is unresolved."""
    blocked: list[str] = []
    unresolved: list[dict[str, Any]] = []
    if text_length > limit:
        blocked.append(f"prepared text is {text_length} characters, over the limit of {limit}")
    for cov in extraction.page_coverage:
        if cov["coverage"] < COVERAGE_BLOCK_BELOW:
            blocked.append(
                f"page {cov['page']} word coverage {cov['coverage']:.1%} (possible dropped text)"
            )
    for item in extraction.items:
        review = reviews.get(item.item_id)
        result = review["result"] if review else None
        if item.category == "table" and item.detail.get("automated") == "pass" and result is None:
            continue  # table passed automated checks; no flag raised
        if result in CLEARED_RESULTS:
            continue
        if item.category in ("reading_order", "coverage") and result == "confirmed_problem":
            blocked.append(
                f"{item.item_id} ({item.kind}, page {item.page}): confirmed problem: {item.reason}"
            )
            continue
        unresolved.append(
            {
                "id": item.item_id,
                "category": item.category,
                "kind": item.kind,
                "page": item.page,
                "label": item.label,
                "reason": item.reason,
                "image": item.image,
                "page_image": item.page_image,
                "review": review["result"] if review else "unreviewed",
                "review_note": review.get("note") if review else None,
            }
        )
    covered_pages = {item.page for item in extraction.items}
    for page in extraction.unreadable_pages:
        if page not in covered_pages:
            blocked.append(f"page {page} has no readable text layer (OCR is off)")
    if blocked:
        return STATUS_BLOCKED, blocked, unresolved
    if unresolved:
        return (
            STATUS_UNRESOLVED,
            [f"{len(unresolved)} unresolved or unreviewed item(s)"],
            unresolved,
        )
    return STATUS_READY, ["no flags and nothing unresolved"], unresolved


# --------------------------------------------------------------------------- orchestration


def _write_json(path: Path, data: Any) -> None:
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8"
    )


def prepare_source(
    entry: ManifestEntry,
    output_root: Path,
    *,
    max_characters: int,
    force: bool = False,
    reorder_columns: bool = False,
) -> dict[str, Any]:
    """Prepare one source (or reuse a verified preparation); returns the status summary."""
    pdf = (REPO_ROOT / entry.pdf) if not Path(entry.pdf).is_absolute() else Path(entry.pdf)
    out = output_root / entry.slug
    out.mkdir(parents=True, exist_ok=True)
    pdf_hash, script_hash = sha256_file(pdf), script_sha256()
    settings_hash = settings_sha256(reorder_columns)
    bound = {"pdf_sha256": pdf_hash, "script_sha256": script_hash, "settings_sha256": settings_hash}

    prep_path = out / "prep_record.json"
    reused = False
    if prep_path.exists() and not force:
        old = json.loads(prep_path.read_text(encoding="utf-8"))
        if old.get("bound_to") == bound and (out / "extraction.json").exists():
            reused = True
    if not reused:
        _archive(
            out,
            ["prep_record.json", "verification_record.json", "review.json", "approval.json"],
            reason="pdf, script, or settings changed: preparation, verification and approval reset",
        )

    started = time.monotonic()
    started_at = now_utc()
    (out / "images").mkdir(exist_ok=True)
    if reused:
        extraction = _load_extraction(out / "extraction.json")
    else:
        for stale in (out / "images").glob("*.png"):
            stale.unlink()
        extraction = extract_pdf(pdf, out / "images", reorder_columns=reorder_columns)
        _save_extraction(out / "extraction.json", extraction)

    reviews, review_meta = load_review(out, bound)
    dispositions = {k: v["result"] for k, v in reviews.items()}
    prepared = assemble(extraction, dispositions, {})
    problems = reserved_character_problems(prepared.text)
    if problems:
        raise ValueError("; ".join(problems))
    status, reasons, unresolved = compute_status(
        extraction, reviews, len(prepared.text), max_characters
    )
    elapsed = time.monotonic() - started

    this_run_timing = {
        "started_at_utc": started_at,
        "elapsed_seconds": round(elapsed, 2),
        "measured": "wall clock of extraction (or reuse), assembly, checks and record writing",
        "reused_existing_extraction": reused,
        "model_calls": 0,
        "usage": "no model usage: local extraction only",
    }
    extraction_timing = this_run_timing
    if reused:
        previous = json.loads(prep_path.read_text(encoding="utf-8"))["timing"]
        extraction_timing = previous.get("extraction_run", previous)
    text_hash = sha256_bytes(prepared.text.encode("utf-8"))
    (out / "prepared_text.md").write_text(prepared.text, encoding="utf-8")
    _write_json(out / "page_map.json", prepared.page_map)
    _write_json(out / "provenance.json", json.loads(_provenance_json(entry)))
    record: dict[str, Any] = {
        "slug": entry.slug,
        "source_pdf": entry.pdf,
        "bound_to": bound,
        "pdf_sha256": pdf_hash,
        "prepared_text": "prepared_text.md",
        "prepared_text_sha256": text_hash,
        "prepared_text_characters": len(prepared.text),
        "max_source_characters": max_characters,
        "within_size_limit": len(prepared.text) <= max_characters,
        "is_excerpt": entry.is_excerpt,
        "excerpt_description": entry.excerpt_description,
        "parser": {"name": PARSER_NAME, "version": PARSER_VERSION, "pymupdf": pymupdf.__version__},
        "parser_settings": PARSER_SETTINGS,
        "reading_order_fix": {
            "enabled": reorder_columns,
            "method": REORDER_METHOD if reorder_columns else None,
            "scope": "opt-in per run; only segments whose order jumps between columns and back",
            "changes": extraction.reading_order_changes,
        },
        "script_sha256": script_hash,
        "pages": extraction.pages,
        "timing": {
            "extraction_run": extraction_timing,
            "this_run": this_run_timing,
        },
        "provenance_basis": entry.provenance_basis,
        "cleanup_applied": [
            "parser header/footer removal; recurring margin lines removed (listed below)",
            "continuation paragraphs joined only when the previous paragraph ends mid-sentence and "
            "the next starts lowercase; end-of-line hyphens joined or kept only where the "
            "document's own text supports it, otherwise kept as extracted and listed",
            "no paraphrasing, summarizing, or reconstruction; headings, citations, footnotes, "
            "units, and table headers kept as extracted",
        ],
        "removed_lines": extraction.removed_lines,
        "hyphenation_notes": prepared.hyphen_notes,
        "annotations": prepared.annotations,
        "page_images": sorted(p.name for p in (out / "images").glob("pdf_p*_page.png")),
    }
    _write_json(prep_path, record)
    verification = {
        "bound_to": bound,
        "prepared_text_sha256": text_hash,
        "status": status,
        "status_reasons": reasons,
        "automated_checks": {
            "page_word_coverage": extraction.page_coverage,
            "altered_or_joined_words_not_in_pdf_text_layer": extraction.altered_words,
            "image_and_graphics_counts": extraction.image_counts,
            "unreadable_pages_ocr_off": extraction.unreadable_pages,
            "size": {"characters": len(prepared.text), "limit": max_characters},
            "limitations": AUTOMATED_LIMITATIONS,
        },
        "items": [_item_json(i, reviews.get(i.item_id)) for i in extraction.items],
        "unresolved": unresolved,
        "picture_label_fragments_not_in_analyzer_text": extraction.label_fragments,
        "spot_check_reviews_apply_to": "review.json (separate; bound to the same hashes)",
        "review_metadata": review_meta,
        "approval_required": status == STATUS_UNRESOLVED,
        "approval_present": (out / "approval.json").exists(),
    }
    _write_json(out / "verification_record.json", verification)
    return {
        "slug": entry.slug,
        "status": status,
        "reasons": reasons,
        "characters": len(prepared.text),
        "elapsed_seconds": round(elapsed, 2),
        "unresolved": len(unresolved),
        "reused": reused,
        "directory": str(out),
    }


def _provenance_json(entry: ManifestEntry) -> str:
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
    return json.dumps({k: v for k, v in data.items() if v not in (None, [])}, ensure_ascii=False)


def _item_json(item: Item, review: dict[str, str] | None) -> dict[str, Any]:
    return {
        "id": item.item_id,
        "category": item.category,
        "kind": item.kind,
        "page": item.page,
        "label": item.label,
        "reason": item.reason,
        "bbox": item.bbox,
        "image": item.image,
        "page_image": item.page_image,
        "detail": item.detail,
        "review": review["result"] if review else None,
        "review_note": review.get("note") if review else None,
    }


def _save_extraction(path: Path, extraction: Extraction) -> None:
    data = {
        "pages": extraction.pages,
        "blocks": [vars(b) for b in extraction.blocks],
        "items": [vars(i) for i in extraction.items],
        "page_coverage": extraction.page_coverage,
        "removed_lines": extraction.removed_lines,
        "altered_words": extraction.altered_words,
        "label_fragments": extraction.label_fragments,
        "printed_labels": {str(k): v for k, v in extraction.printed_labels.items()},
        "image_counts": extraction.image_counts,
        "unreadable_pages": extraction.unreadable_pages,
        "reading_order_changes": extraction.reading_order_changes,
    }
    _write_json(path, data)


def _load_extraction(path: Path) -> Extraction:
    d = json.loads(path.read_text(encoding="utf-8"))
    return Extraction(
        pages=d["pages"],
        blocks=[Block(**b) for b in d["blocks"]],
        items=[Item(**i) for i in d["items"]],
        page_coverage=d["page_coverage"],
        removed_lines=d["removed_lines"],
        altered_words=d["altered_words"],
        label_fragments=d["label_fragments"],
        printed_labels={int(k): v for k, v in d["printed_labels"].items()},
        image_counts=d["image_counts"],
        unreadable_pages=d["unreadable_pages"],
        reading_order_changes=d.get("reading_order_changes", []),
    )


# --------------------------------------------------------------------------- gate / approval


def check_analysis_gate(directory: Path) -> tuple[bool, list[str]]:
    """May this source go to analysis? Blocked: never. ready_with_unresolved: only with a
    source-specific approval that matches the current hashes and unresolved items."""
    try:
        record = json.loads((directory / "prep_record.json").read_text(encoding="utf-8"))
        verification = json.loads(
            (directory / "verification_record.json").read_text(encoding="utf-8")
        )
        text = (directory / record["prepared_text"]).read_text(encoding="utf-8")
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        return False, [f"preparation records are missing or unreadable: {exc}"]
    if sha256_bytes(text.encode("utf-8")) != record["prepared_text_sha256"]:
        return False, ["prepared text no longer matches its recorded hash"]
    if verification["prepared_text_sha256"] != record["prepared_text_sha256"]:
        return False, ["verification record does not match the prepared text"]
    status = verification["status"]
    if status == STATUS_BLOCKED:
        return False, ["status is blocked: " + "; ".join(verification["status_reasons"])]
    if status == STATUS_READY:
        return True, ["status is ready"]
    approval_path = directory / "approval.json"
    if not approval_path.exists():
        return False, [
            "ready_with_unresolved requires the project owner's source-specific approval"
        ]
    approval = json.loads(approval_path.read_text(encoding="utf-8"))
    if (
        approval.get("slug") != record["slug"]
        or approval.get("prepared_text_sha256") != record["prepared_text_sha256"]
        or approval.get("bound_to") != record["bound_to"]
    ):
        return False, ["approval does not match this source's current preparation"]
    current = {u["id"] for u in verification["unresolved"]}
    missing = current - set(approval.get("approved_unresolved_items", []))
    if missing:
        return False, [f"approval does not cover unresolved items: {sorted(missing)}"]
    return True, ["approved ready_with_unresolved"]


def record_approval(directory: Path, statement: str, approved_by: str) -> dict[str, Any]:
    """Write an approval for exactly the current unresolved items. Only called on the
    project owner's explicit instruction."""
    record = json.loads((directory / "prep_record.json").read_text(encoding="utf-8"))
    verification = json.loads((directory / "verification_record.json").read_text(encoding="utf-8"))
    if verification["status"] != STATUS_UNRESOLVED:
        raise ValueError(
            f"only ready_with_unresolved sources take an approval (status {verification['status']})"
        )
    approval = {
        "slug": record["slug"],
        "approved_by": approved_by,
        "statement": statement,
        "approved_at": now_utc(),
        "bound_to": record["bound_to"],
        "prepared_text_sha256": record["prepared_text_sha256"],
        "approved_unresolved_items": [u["id"] for u in verification["unresolved"]],
        "applies_to": "this source and preparation only",
    }
    _write_json(directory / "approval.json", approval)
    return approval


# --------------------------------------------------------------------------- CLI


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "status", "approve"):
        p = sub.add_parser(name)
        p.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
        p.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
        p.add_argument("--slug", required=True)
        if name == "prepare":
            p.add_argument("--force", action="store_true")
            p.add_argument(
                "--reorder-columns",
                action="store_true",
                help="opt-in: reorder blocks whose order jumps between columns and back",
            )
        if name == "approve":
            p.add_argument("--statement", required=True)
            p.add_argument("--approved-by", default="project owner")
    args = parser.parse_args(argv)
    directory = args.output_root / args.slug
    if args.command == "prepare":
        entries = {e.slug: e for e in load_manifest(args.manifest)}
        if args.slug not in entries:
            print(f"unknown slug {args.slug!r}", file=sys.stderr)
            return 2
        limit = Settings().max_source_characters
        summary = prepare_source(
            entries[args.slug],
            args.output_root,
            max_characters=limit,
            force=args.force,
            reorder_columns=args.reorder_columns,
        )
        print(json.dumps(summary, indent=2))
        return 0 if summary["status"] != STATUS_BLOCKED else 1
    if args.command == "status":
        allowed, why = check_analysis_gate(directory)
        print(json.dumps({"analysis_allowed": allowed, "reasons": why}, indent=2))
        return 0 if allowed else 1
    approval = record_approval(directory, args.statement, args.approved_by)
    print(json.dumps(approval, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"manifest error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
