"""Water experiment, original-documents approach (standard RAG): build and search the index.

    uv run python scripts/build_index.py build
    uv run python scripts/build_index.py search "QUESTION" [-k 5]

``build`` reads each article's prepared text and page map from ``outputs/preparation``
(run ``prepare_sources.py prepare`` for every article first), splits the text into
passages of at most ``MAX_TOKENS`` model tokens that overlap by up to ``OVERLAP_TOKENS``,
labels each passage with its article and PDF pages, embeds the passages, and writes
``outputs/index/source_text/``:

* ``chunks.jsonl``: one passage per line; its ``text`` is exactly
  ``prepared_text[start:end]``;
* ``embeddings.npy``: one unit-length vector per passage, in the same order;
* ``index.json``: the model, the chunking settings, and the prepared text each article's
  passages were cut from.

``search`` embeds a question the same way and prints the nearest passages, for spot checks.
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
INDEX_DIR = STUDY / "outputs" / "index" / "source_text"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
# BGE's recommended prefix for retrieval queries; passages are embedded without one.
QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "
# The model reads at most 512 tokens, including its two special tokens.
MAX_TOKENS = 450
OVERLAP_TOKENS = 50

Span = tuple[int, int]
CountTokens = Callable[[str], int]

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
    max_tokens: int = MAX_TOKENS,
    overlap_tokens: int = OVERLAP_TOKENS,
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


def build() -> int:
    from fastembed import TextEmbedding

    count = _token_counter()
    chunks: list[dict[str, Any]] = []
    sources: dict[str, Any] = {}
    for slug in _slugs():
        prepared = PREPARATION / slug
        if not (prepared / "prepared_text.txt").is_file():
            sys.exit(
                f"no prepared text for {slug}: run "
                f"`uv run python scripts/prepare_sources.py prepare --slug {slug}`"
            )
        raw = (prepared / "prepared_text.txt").read_bytes()
        text = raw.decode("utf-8")
        page_map = json.loads((prepared / "page_map.json").read_text(encoding="utf-8"))
        records = article_chunks(slug, text, page_map, count)
        sources[slug] = {
            "prepared_text_sha256": hashlib.sha256(raw).hexdigest(),
            "chunks": len(records),
        }
        chunks.extend(records)
        print(f"{slug}: {len(records)} chunks", file=sys.stderr)

    model = TextEmbedding(model_name=EMBEDDING_MODEL)
    vectors = _unit(np.array(list(model.embed([c["text"] for c in chunks])), dtype=np.float32))

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    with (INDEX_DIR / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    np.save(INDEX_DIR / "embeddings.npy", vectors)
    index = {
        "built_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "embedding_model": EMBEDDING_MODEL,
        "query_instruction": QUERY_INSTRUCTION,
        "dimension": int(vectors.shape[1]),
        "max_tokens": MAX_TOKENS,
        "overlap_tokens": OVERLAP_TOKENS,
        "chunks": len(chunks),
        "sources": sources,
    }
    (INDEX_DIR / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"{len(chunks)} chunks from {len(sources)} articles -> {INDEX_DIR}", file=sys.stderr)
    return 0


def search(question: str, k: int) -> int:
    from fastembed import TextEmbedding

    index = json.loads((INDEX_DIR / "index.json").read_text(encoding="utf-8"))
    with (INDEX_DIR / "chunks.jsonl").open(encoding="utf-8") as f:
        chunks = [json.loads(line) for line in f]
    vectors = np.load(INDEX_DIR / "embeddings.npy")
    model = TextEmbedding(model_name=index["embedding_model"])
    query = _unit(np.array(list(model.embed([index["query_instruction"] + question]))))[0]
    scores = vectors @ query
    for rank in np.argsort(-scores)[:k]:
        c = chunks[rank]
        print(f"\n[{scores[rank]:.3f}] {c['id']}  pdf pages {c['pdf_pages']}")
        print(c["text"][:600] + ("…" if len(c["text"]) > 600 else ""))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build", help="chunk, embed, and index the prepared article text")
    s = sub.add_parser("search", help="print the passages nearest a question")
    s.add_argument("question")
    s.add_argument("-k", type=int, default=5)
    args = parser.parse_args(argv)
    if args.command == "build":
        return build()
    return search(args.question, args.k)


if __name__ == "__main__":
    raise SystemExit(main())
