"""Water experiment: build and search the indexes the approaches retrieve from.

    uv run python scripts/build_index.py build  {source_text,analyses}
    uv run python scripts/build_index.py search {rag,structured} "QUESTION" [-k 5]

``source_text`` (original documents, standard RAG) reads each article's prepared text
and page map from ``outputs/preparation`` (run ``prepare_sources.py prepare`` for every
article first) and splits the text into passages of at most ``SOURCE_MAX_TOKENS`` model
tokens that overlap by up to ``SOURCE_OVERLAP_TOKENS``. Each passage's ``text`` is exactly
``prepared_text[start:end]`` and is labeled with its article and PDF pages.

``analyses`` (structured analyses) reads each article's close reading (01), claims
reference (02), and argument evaluation (04) from ``outputs/analyses`` and splits them
into items: a step of the close reading, an entry of the claims reference, a paragraph
of the argument evaluation. Each item is labeled with its article and its kind, so the
model's reading and judgment are never taken for what the source says. An item longer
than ``MAX_TOKENS`` is split, with its location or section repeated on every part.

``build`` embeds the items and writes ``outputs/index/<index>/``: ``chunks.jsonl`` (one
item per line), ``embeddings.npy`` (one unit-length vector per item, in the same order),
and ``index.json`` (the model, the settings, and a hash of every file the items came
from). ``search`` embeds a question the same way and prints the nearest items, for spot
checks. It takes an approach rather than an index: ``rag`` searches ``source_text``,
and ``structured`` searches ``analyses``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy as np
import yaml

STUDY = Path(__file__).resolve().parents[1] / "studies" / "water"
MANIFEST = STUDY / "data" / "sources.yaml"
PREPARATION = STUDY / "outputs" / "preparation"
ANALYSES = STUDY / "outputs" / "analyses"
ANALYSIS_FILES = ("01_close_reading.json", "02_claims_reference.md", "04_argument_evaluation.md")
INDEX_ROOT = STUDY / "outputs" / "index"
INDEXES = ("source_text", "analyses")
# The experiment's two approaches, and the index each retrieves from.
APPROACHES = {"rag": "source_text", "structured": "analyses"}

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
# BGE's recommended prefix for retrieval queries; passages are embedded without one.
QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "
# The model reads at most 512 tokens, including its two special tokens.
MAX_TOKENS = 450
# Article passages are cut to about the size of an analysis item (mean 177 tokens), so the
# same retrieved-text budget holds about as many pieces for either approach.
SOURCE_MAX_TOKENS = 200
SOURCE_OVERLAP_TOKENS = 25

Span = tuple[int, int]
CountTokens = Callable[[str], int]
Records = tuple[list[dict[str, Any]], dict[str, str]]

# Coarsest to finest: paragraphs, lines, sentences, words.
_SEPARATORS = (
    re.compile(r"\n\s*\n"),
    re.compile(r"\n"),
    re.compile(r"(?<=[.!?])\s+"),
    re.compile(r"\s+"),
)


def _pieces(text: str, start: int, end: int, count: CountTokens, max_tokens: int) -> list[Span]:
    """Split text[start:end] at the coarsest separator that yields pieces of at most
    max_tokens. A single word longer than max_tokens stays one piece."""

    def split(start: int, end: int, level: int) -> list[Span]:
        if level == len(_SEPARATORS) or count(text[start:end]) <= max_tokens:
            return [(start, end)]
        spans: list[Span] = []
        pos = start
        for match in _SEPARATORS[level].finditer(text, start, end):
            if match.start() > pos:
                spans.extend(split(pos, match.start(), level + 1))
            pos = match.end()
        if pos < end:
            spans.extend(split(pos, end, level + 1))
        return spans

    trimmed = []
    for s, e in split(start, end, 0):
        piece = text[s:e]
        if piece.strip():
            s += len(piece) - len(piece.lstrip())
            e -= len(piece) - len(piece.rstrip())
            trimmed.append((s, e))
    return trimmed


def chunk_spans(text: str, count: CountTokens, max_tokens: int, overlap_tokens: int) -> list[Span]:
    """Pack consecutive pieces into chunks of at most max_tokens.

    Each chunk after the first starts with the trailing pieces of the one before, up to
    overlap_tokens, and always reaches at least one piece the previous chunk did not.
    Chunk starts strictly increase, and every non-whitespace character of text is in some
    chunk. Only a piece that is itself longer than max_tokens (a single word) exceeds it.
    """
    pieces = _pieces(text, 0, len(text), count, max_tokens)
    chunks: list[Span] = []
    i = 0
    while i < len(pieces):
        j = i + 1  # the chunk is pieces[i:j]
        while j < len(pieces) and count(text[pieces[i][0] : pieces[j][1]]) <= max_tokens:
            j += 1
        chunks.append((pieces[i][0], pieces[j - 1][1]))
        if j == len(pieces):
            break
        k = j  # the next chunk starts at pieces[k], with i < k <= j
        while (
            k - 1 > i
            and count(text[pieces[k - 1][0] : pieces[j - 1][1]]) <= overlap_tokens
            and count(text[pieces[k - 1][0] : pieces[j][1]]) <= max_tokens
        ):
            k -= 1
        i = k
    return chunks


def pages_for(start: int, end: int, page_map: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """The page-map entries whose text overlaps text[start:end], in page order."""
    return [
        page
        for page in page_map
        if page["mapped_text"] and page["start_offset"] < end and start < page["end_offset"]
    ]


def article_chunks(
    slug: str,
    text: str,
    page_map: list[dict[str, Any]],
    count: CountTokens,
    max_tokens: int = SOURCE_MAX_TOKENS,
    overlap_tokens: int = SOURCE_OVERLAP_TOKENS,
) -> list[dict[str, Any]]:
    records = []
    for n, (start, end) in enumerate(chunk_spans(text, count, max_tokens, overlap_tokens)):
        pages = pages_for(start, end, page_map)
        records.append(
            {
                "id": f"{slug}#{n:03d}",
                "slug": slug,
                "kind": "source_text",
                "pdf_pages": [p["pdf_page"] for p in pages],
                "printed_pages": [p["printed_label"] for p in pages],
                "start": start,
                "end": end,
                "tokens": count(text[start:end]),
                "text": text[start:end],
            }
        )
    return records


# --------------------------------------------------------------------------- analyses
#
# Each analysis is split into items: a step of the close reading (01), an entry of the
# claims reference (02), a paragraph of the argument evaluation (04). An item is a
# (prefix, body) pair: the prefix says where in the article or analysis it comes from and
# is repeated on every part if a body too long for the model has to be split.

Item = tuple[str, str]

_LIST_ITEM = re.compile(r"(?:[-*]|\d+\.)\s")
_HEADING = re.compile(r"(#+)\s+(.*)")


def close_reading_items(reading: dict[str, Any]) -> list[Item]:
    items = []
    for step in reading["reading_path"]:
        prefix = f"Location: {step['location']}\nMoves: {step['moves']}"
        lines = ["Claims:"]
        for claim in step["claims"]:
            lines.append(f"- {claim['text']} ({claim['form']})")
            for support in claim["support"]:
                cites = "; ".join(
                    f"[{c['citation_text']}] {c['reference_entry']}"
                    for c in support.get("citations", [])
                )
                lines.append(
                    f"  Support: {support['text']} ({support['form']})"
                    + (f" Cites: {cites}" if cites else "")
                )
        lines.append(f"Meaning: {step['meaning']}")
        items.append((prefix, "\n".join(lines)))
    return items


def claims_reference_items(markdown: str) -> list[Item]:
    """One item per top-level list entry (with its nested lines), table, or paragraph,
    prefixed with the headings it sits under. The document title is left out."""
    items: list[Item] = []
    path: list[str] = []
    block: list[str] = []
    kind = ""  # "list", "table", or "para" while a block is open
    blank = False

    def flush() -> None:
        nonlocal block, kind
        if block:
            items.append(("Section: " + " > ".join(path) if path else "", "\n".join(block)))
        block, kind = [], ""

    for line in markdown.splitlines():
        heading = _HEADING.fullmatch(line)
        if heading:
            flush()
            level = len(heading.group(1))
            if level > 1:
                path[level - 2 :] = [heading.group(2).strip()]
        elif not line.strip():
            blank = True
            continue
        elif _LIST_ITEM.match(line):
            flush()
            block, kind = [line], "list"
        elif line.startswith("|"):
            if kind != "table":
                flush()
                kind = "table"
            block.append(line)
        elif line[0].isspace() and kind in ("list", "para"):
            block.append(line)
        elif kind in ("list", "para") and not blank:
            block.append(line)
        else:
            flush()
            block, kind = [line], "para"
        blank = False
    flush()
    return items


def argument_evaluation_items(markdown: str) -> list[Item]:
    return [("", p.strip()) for p in re.split(r"\n\s*\n", markdown) if p.strip()]


def analysis_records(
    slug: str,
    kind: str,
    code: str,
    items: list[Item],
    count: CountTokens,
    max_tokens: int = MAX_TOKENS,
) -> list[dict[str, Any]]:
    """Records for one analysis, ids "<slug>#<code>-NNN" in order. An item over max_tokens
    is split at paragraph, line, sentence, or word breaks, its prefix on every part."""
    records = []
    for prefix, body in items:
        head = prefix + "\n" if prefix else ""
        whole = head + body
        if count(whole) <= max_tokens:
            parts = [whole]
        else:
            budget = max_tokens - count(head)
            parts = [head + body[s:e] for s, e in chunk_spans(body, count, budget, 0)]
        for text in parts:
            records.append(
                {
                    "id": f"{slug}#{code}-{len(records):03d}",
                    "slug": slug,
                    "kind": kind,
                    "tokens": count(text),
                    "text": text,
                }
            )
    return records


# --------------------------------------------------------------------------- I/O


def _slugs() -> list[str]:
    return [s["slug"] for s in yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))["sources"]]


def _token_counter() -> CountTokens:
    from tokenizers import Tokenizer

    tokenizer = Tokenizer.from_pretrained(EMBEDDING_MODEL)
    tokenizer.no_truncation()
    return lambda s: len(tokenizer.encode(s, add_special_tokens=False).ids)


def _unit(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)


def _source_text_records(slug: str, count: CountTokens) -> Records:
    prepared = PREPARATION / slug
    if not (prepared / "prepared_text.txt").is_file():
        sys.exit(
            f"no prepared text for {slug}: run "
            f"`uv run python scripts/prepare_sources.py prepare --slug {slug}`"
        )
    raw = (prepared / "prepared_text.txt").read_bytes()
    page_map = json.loads((prepared / "page_map.json").read_text(encoding="utf-8"))
    records = article_chunks(slug, raw.decode("utf-8"), page_map, count)
    return records, {"prepared_text.txt": hashlib.sha256(raw).hexdigest()}


def _analysis_records(slug: str, count: CountTokens) -> Records:
    folder = ANALYSES / slug
    files = {name: (folder / name).read_bytes() for name in ANALYSIS_FILES}
    reading = json.loads(files["01_close_reading.json"])
    claims = files["02_claims_reference.md"].decode("utf-8")
    evaluation = files["04_argument_evaluation.md"].decode("utf-8")
    records = (
        analysis_records(slug, "close_reading", "01", close_reading_items(reading), count)
        + analysis_records(slug, "claims_reference", "02", claims_reference_items(claims), count)
        + analysis_records(
            slug, "argument_evaluation", "04", argument_evaluation_items(evaluation), count
        )
    )
    return records, {name: hashlib.sha256(raw).hexdigest() for name, raw in files.items()}


def build(name: str) -> int:
    from fastembed import TextEmbedding

    count = _token_counter()
    records_for = _source_text_records if name == "source_text" else _analysis_records
    chunks: list[dict[str, Any]] = []
    sources: dict[str, Any] = {}
    for slug in _slugs():
        records, hashes = records_for(slug, count)
        sources[slug] = {"sha256": hashes, "chunks": len(records)}
        chunks.extend(records)
        print(f"{slug}: {len(records)} chunks", file=sys.stderr)

    model = TextEmbedding(model_name=EMBEDDING_MODEL)
    vectors = _unit(np.array(list(model.embed([c["text"] for c in chunks])), dtype=np.float32))

    out = INDEX_ROOT / name
    out.mkdir(parents=True, exist_ok=True)
    with (out / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    np.save(out / "embeddings.npy", vectors)
    index = {
        "built_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "embedding_model": EMBEDDING_MODEL,
        "query_instruction": QUERY_INSTRUCTION,
        "dimension": int(vectors.shape[1]),
        "max_tokens": SOURCE_MAX_TOKENS if name == "source_text" else MAX_TOKENS,
        "overlap_tokens": SOURCE_OVERLAP_TOKENS if name == "source_text" else 0,
        "chunks": len(chunks),
        "sources": sources,
    }
    (out / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"{len(chunks)} chunks from {len(sources)} articles -> {out}", file=sys.stderr)
    return 0


def load_index(name: str) -> tuple[dict[str, Any], list[dict[str, Any]], np.ndarray]:
    folder = INDEX_ROOT / name
    index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
    with (folder / "chunks.jsonl").open(encoding="utf-8") as f:
        chunks = [json.loads(line) for line in f]
    return index, chunks, np.load(folder / "embeddings.npy")


def nearest(
    chunks: list[dict[str, Any]], vectors: np.ndarray, query: np.ndarray, k: int | None = None
) -> list[tuple[float, dict[str, Any]]]:
    """The k chunks (all, if k is None) most similar to the unit-length query, most
    similar first; ties keep index order. Vectors and query are unit length, so the dot
    product is the cosine."""
    scores = vectors @ query
    order = np.argsort(-scores, kind="stable")[:k]
    return [(float(scores[i]), chunks[i]) for i in order]


def retrieve(
    approach: str, question: str, k: int | None = None
) -> list[tuple[float, dict[str, Any]]]:
    """The k items (all, if k is None) nearest the question in the approach's index,
    with the question embedded by the model and instruction the index was built with."""
    from fastembed import TextEmbedding

    index, chunks, vectors = load_index(APPROACHES[approach])
    model = TextEmbedding(model_name=index["embedding_model"])
    query = _unit(np.array(list(model.embed([index["query_instruction"] + question]))))[0]
    return nearest(chunks, vectors, query, k)


def search(approach: str, question: str, k: int) -> int:
    for score, c in retrieve(approach, question, k):
        where = f"  pdf pages {c['pdf_pages']}" if "pdf_pages" in c else ""
        print(f"\n[{score:.3f}] {c['id']}  {c['kind']}{where}")
        print(c["text"][:600] + ("…" if len(c["text"]) > 600 else ""))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build", help="split, embed, and index one approach's material")
    b.add_argument("index", choices=INDEXES)
    s = sub.add_parser("search", help="print the items nearest a question")
    s.add_argument("approach", choices=APPROACHES)
    s.add_argument("question")
    s.add_argument("-k", type=int, default=5)
    args = parser.parse_args(argv)
    if args.command == "build":
        return build(args.index)
    return search(args.approach, args.question, args.k)


if __name__ == "__main__":
    raise SystemExit(main())
