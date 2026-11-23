"""scripts/build_index.py: chunking the prepared text and labeling chunks with pages.

The script is not a package module, so it is loaded by file path. A word count stands in
for the model's tokenizer.
"""

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

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
