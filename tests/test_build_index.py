"""scripts/build_index.py: chunking the prepared text and labeling chunks with pages.

The script is not a package module, so it is loaded by file path. A word count stands in
for the model's tokenizer.
"""

import importlib.util
import json
import sys
import types
from pathlib import Path
from types import ModuleType
from typing import Any

import numpy as np
import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_index.py"


def load_script() -> ModuleType:
    spec = importlib.util.spec_from_file_location("build_index", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bi = load_script()


def words(s: str) -> int:
    return len(s.split())


def paragraph(n: int, words_each: int = 8) -> str:
    return " ".join(f"p{n}w{i}" for i in range(words_each - 1)) + " end."


def check_invariants(text: str, spans: list[tuple[int, int]], max_t: int, overlap_t: int) -> None:
    starts = [s for s, _ in spans]
    assert starts == sorted(set(starts)), "chunk starts strictly increase"
    for s, e in spans:
        assert words(text[s:e]) <= max_t
        assert text[s:e] == text[s:e].strip()
    for (_, prev_end), (start, end) in zip(spans, spans[1:], strict=False):
        assert end > prev_end, "each chunk reaches past the previous one"
        assert words(text[start:prev_end]) <= overlap_t
    covered = set()
    for s, e in spans:
        covered.update(range(s, e))
    assert all(i in covered for i, ch in enumerate(text) if not ch.isspace())


@pytest.mark.parametrize("text", ["", "   \n\n  "])
def test_empty_text_has_no_chunks(text: str) -> None:
    assert bi.chunk_spans(text, words, 20, 5) == []


def test_short_text_is_one_chunk_without_surrounding_whitespace() -> None:
    text = "\n\n" + paragraph(0) + "\n\n" + paragraph(1) + "\n"
    [(s, e)] = bi.chunk_spans(text, words, 20, 5)
    assert text[s:e] == text.strip()


def test_paragraphs_pack_and_overlap() -> None:
    text = "\n\n".join(paragraph(n) for n in range(10))
    spans = bi.chunk_spans(text, words, 20, 8)
    check_invariants(text, spans, 20, 8)
    assert len(spans) > 1
    # Chunks break between paragraphs, and the overlap is the previous chunk's last one.
    assert all(text[s:e].startswith("p") and text[s:e].endswith("end.") for s, e in spans)
    assert text[spans[1][0] :].startswith(text[spans[0][0] : spans[0][1]].split("\n\n")[-1])


def test_no_overlap_when_the_last_piece_is_too_long() -> None:
    text = "\n\n".join(paragraph(n) for n in range(6))
    spans = bi.chunk_spans(text, words, 20, 5)
    check_invariants(text, spans, 20, 5)
    assert all(e <= s2 for (_, e), (s2, _) in zip(spans, spans[1:], strict=False))


def test_long_paragraph_splits_at_sentences_then_words() -> None:
    sentences = " ".join(f"Sentence {n} has five words." for n in range(12))
    run_on = " ".join(f"w{i}" for i in range(50))
    text = sentences + "\n\n" + run_on
    spans = bi.chunk_spans(text, words, 12, 0)
    check_invariants(text, spans, 12, 0)
    sentence_chunks = [text[s:e] for s, e in spans if e <= len(sentences)]
    assert all(c.endswith("words.") for c in sentence_chunks)


def test_word_longer_than_max_is_its_own_chunk() -> None:
    long_word = "x" * 50

    def chars(s: str) -> int:
        return len(s)

    text = "short words here\n\n" + long_word + "\n\nmore words"
    spans = bi.chunk_spans(text, chars, 20, 0)
    assert long_word in [text[s:e] for s, e in spans]


PAGE_MAP: list[dict[str, Any]] = [
    {
        "pdf_page": 1,
        "printed_label": "10",
        "mapped_text": True,
        "start_offset": 0,
        "end_offset": 100,
    },
    {
        "pdf_page": 2,
        "printed_label": "11",
        "mapped_text": False,
        "start_offset": None,
        "end_offset": None,
    },
    {
        "pdf_page": 3,
        "printed_label": None,
        "mapped_text": True,
        "start_offset": 100,
        "end_offset": 250,
    },
]


@pytest.mark.parametrize(
    ("start", "end", "pages"),
    [(0, 100, [1]), (99, 101, [1, 3]), (100, 250, [3]), (50, 250, [1, 3])],
)
def test_pages_for_uses_half_open_offsets_and_skips_unmapped_pages(
    start: int, end: int, pages: list[int]
) -> None:
    assert [p["pdf_page"] for p in bi.pages_for(start, end, PAGE_MAP)] == pages


def test_article_chunks_records_are_slices_with_pages() -> None:
    text = "\n\n".join(paragraph(n) for n in range(6))
    page_map = [
        {
            "pdf_page": 1,
            "printed_label": "1",
            "mapped_text": True,
            "start_offset": 0,
            "end_offset": len(text) // 2,
        },
        {
            "pdf_page": 2,
            "printed_label": "2",
            "mapped_text": True,
            "start_offset": len(text) // 2,
            "end_offset": len(text),
        },
    ]
    records = bi.article_chunks("demo", text, page_map, words, max_tokens=20, overlap_tokens=8)
    assert [r["id"] for r in records] == [f"demo#{n:03d}" for n in range(len(records))]
    for r in records:
        assert r["text"] == text[r["start"] : r["end"]]
        assert r["kind"] == "source_text"
        assert r["pdf_pages"] and r["printed_pages"] == [str(p) for p in r["pdf_pages"]]
    assert records[0]["pdf_pages"] == [1] and records[-1]["pdf_pages"] == [2]


CLAIMS_MD = """# Claims reference: article.pdf

## Source, scope, and use

Opening paragraph,
continued on a second line.

## Claims

### Background (p. 2)

- **C1 — First.** A claim
  that wraps onto an indented line.
  - a nested detail
- **C2 — Second.** Another claim,
lazily continued.

1. **Numbered.** An ordered entry.

| Col | Val |
| --- | --- |
| a | 1 |

#### Detail (p. 3)

- **C3 — Deep.** Under a subsection.

### Results

Closing prose.
"""


def test_claims_reference_items_follow_lists_tables_paragraphs_and_headings() -> None:
    items = bi.claims_reference_items(CLAIMS_MD)
    assert items == [
        ("Section: Source, scope, and use", "Opening paragraph,\ncontinued on a second line."),
        (
            "Section: Claims > Background (p. 2)",
            "- **C1 — First.** A claim\n  that wraps onto an indented line.\n  - a nested detail",
        ),
        (
            "Section: Claims > Background (p. 2)",
            "- **C2 — Second.** Another claim,\nlazily continued.",
        ),
        ("Section: Claims > Background (p. 2)", "1. **Numbered.** An ordered entry."),
        ("Section: Claims > Background (p. 2)", "| Col | Val |\n| --- | --- |\n| a | 1 |"),
        (
            "Section: Claims > Background (p. 2) > Detail (p. 3)",
            "- **C3 — Deep.** Under a subsection.",
        ),
        ("Section: Claims > Results", "Closing prose."),
    ]


def test_claims_reference_items_before_any_heading_have_no_prefix() -> None:
    assert bi.claims_reference_items("- lone entry\n") == [("", "- lone entry")]


def test_argument_evaluation_items_are_paragraphs() -> None:
    md = "Title: X\nType: y\n\nFirst paragraph.\n\n\n  Second paragraph.  \n"
    assert bi.argument_evaluation_items(md) == [
        ("", "Title: X\nType: y"),
        ("", "First paragraph."),
        ("", "Second paragraph."),
    ]


def test_close_reading_items_render_every_step() -> None:
    reading = {
        "reading_plan": "plan",
        "reading_path": [
            {
                "location": "p. 1",
                "moves": "Frames.",
                "claims": [
                    {
                        "text": "Claim one.",
                        "form": "paraphrased",
                        "support": [
                            {
                                "text": "Cited support.",
                                "form": "verbatim",
                                "citations": [{"citation_text": "9", "reference_entry": "Ref 9."}],
                            },
                            {"text": "Bare support.", "form": "paraphrased", "citations": []},
                        ],
                    }
                ],
                "meaning": "So what.",
            },
            {"location": "p. 2", "moves": "Ends.", "claims": [], "meaning": "Done."},
        ],
    }
    items = bi.close_reading_items(reading)
    assert items == [
        (
            "Location: p. 1\nMoves: Frames.",
            "Claims:\n- Claim one. (paraphrased)\n"
            "  Support: Cited support. (verbatim) Cites: [9] Ref 9.\n"
            "  Support: Bare support. (paraphrased)\nMeaning: So what.",
        ),
        ("Location: p. 2\nMoves: Ends.", "Claims:\nMeaning: Done."),
    ]


def test_analysis_records_split_long_items_and_repeat_the_prefix() -> None:
    body = "\n".join(f"line {n} has five words" for n in range(10))
    items = [("Section: S", "short item"), ("Section: L", body), ("", "no prefix")]
    records = bi.analysis_records("demo", "claims_reference", "02", items, words, max_tokens=17)
    assert [r["id"] for r in records] == [f"demo#02-{n:03d}" for n in range(len(records))]
    assert records[0]["text"] == "Section: S\nshort item"
    assert records[-1]["text"] == "no prefix"
    long_parts = records[1:-1]
    assert len(long_parts) > 1
    assert all(r["text"].startswith("Section: L\n") for r in long_parts)
    assert all(r["tokens"] == words(r["text"]) <= 17 for r in records)
    assert "\n".join(r["text"].removeprefix("Section: L\n") for r in long_parts) == body
    assert {r["kind"] for r in records} == {"claims_reference"}


def test_nearest_ranks_by_similarity_and_keeps_index_order_on_ties() -> None:
    chunks = [{"id": n} for n in "abcd"]
    vectors = np.array([[1.0, 0.0], [0.0, 1.0], [0.6, 0.8], [0.0, 1.0]])
    query = np.array([0.0, 1.0])
    assert [c["id"] for _, c in bi.nearest(chunks, vectors, query, 3)] == ["b", "d", "c"]
    assert len(bi.nearest(chunks, vectors, query, 10)) == 4


def write_index(
    root: Path, name: str, ids: list[str], vectors: list[list[float]], model: str
) -> None:
    folder = root / name
    folder.mkdir(parents=True)
    index = {"embedding_model": model, "query_instruction": "Q: "}
    (folder / "index.json").write_text(json.dumps(index), encoding="utf-8")
    lines = [json.dumps({"id": i, "kind": name}) for i in ids]
    (folder / "chunks.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    np.save(folder / "embeddings.npy", np.array(vectors, dtype=np.float32))


class FakeEmbedding:
    """Embeds every text as the same direction, and records what it was given."""

    seen: list[str] = []

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def embed(self, texts: list[str]) -> list[np.ndarray]:
        FakeEmbedding.seen.extend(texts)
        return [np.array([0.0, 2.0]) for _ in texts]


@pytest.fixture
def indexes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(bi, "INDEX_ROOT", tmp_path)
    monkeypatch.setitem(
        sys.modules, "fastembed", types.SimpleNamespace(TextEmbedding=FakeEmbedding)
    )
    FakeEmbedding.seen = []
    return tmp_path


def test_each_approach_searches_its_own_index(indexes: Path) -> None:
    write_index(indexes, "source_text", ["s1", "s2"], [[1.0, 0.0], [0.0, 1.0]], "m")
    write_index(indexes, "analyses", ["a1", "a2"], [[0.6, 0.8], [0.8, 0.6]], "m")
    assert [c["id"] for _, c in bi.retrieve("rag", "why?")] == ["s2", "s1"]
    assert [c["id"] for _, c in bi.retrieve("structured", "why?", 1)] == ["a1"]
    assert FakeEmbedding.seen == ["Q: why?", "Q: why?"]
