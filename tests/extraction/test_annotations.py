import pytest
from pydantic import ValidationError

from hitl_research_agent.extraction.annotations import (
    SENTINEL,
    find_annotations,
    format_annotation,
    grounding_view,
    reserved_character_problems,
)
from hitl_research_agent.extraction.schemas import PreparationGap, SourceDocument
from hitl_research_agent.models.provenance import Provenance

ANNOTATION = format_annotation(
    "U1",
    {"kind": "figure", "label": "Figure 1", "page": "2", "image": "images/p2.png"},
    "not source text; content not extracted",
)
TEXT = f"Water use rose sharply in 2023. {ANNOTATION} Cooling relied on evaporative towers."
GAP_U1 = PreparationGap(id="U1", kind="figure", page=2, label="Figure 1", image="images/p2.png")


def test_annotation_is_well_formed_and_located() -> None:
    spans = find_annotations(TEXT)
    assert [span.annotation_id for span in spans] == ["U1"]
    assert TEXT[spans[0].start : spans[0].end] == ANNOTATION


def test_grounding_view_replaces_each_annotation_with_one_sentinel() -> None:
    view = grounding_view(TEXT)
    assert view.count(SENTINEL) == 1
    assert "PREP-ANNOTATION" not in view
    assert "Water use rose sharply in 2023." in view


def test_text_without_annotations_is_unchanged_by_the_grounding_view() -> None:
    plain = "No annotations here."
    assert grounding_view(plain) == plain


def test_source_text_with_stray_reserved_characters_is_rejected() -> None:
    provenance = Provenance(
        source_title="T",
        source_type="other",
        retrieved_at="2026-01-01T00:00:00+00:00",  # type: ignore[arg-type]
    )
    for bad in ("stray ⟦ opener", "stray ⟧ closer", f"has {SENTINEL} sentinel"):
        assert reserved_character_problems(bad)
        with pytest.raises(ValidationError):
            SourceDocument(text=bad, provenance=provenance)
    # a well-formed annotation is accepted
    document = SourceDocument(
        text=TEXT,
        provenance=provenance,
        preparation_directory="outputs/preparation/fixture",
        preparation_gaps=[GAP_U1],
    )
    assert document.text == TEXT
    # the declared gaps must match the annotations the text actually carries
    with pytest.raises(ValidationError):
        SourceDocument(text=TEXT, provenance=provenance)
    with pytest.raises(ValidationError):
        SourceDocument(
            text=TEXT,
            provenance=provenance,
            preparation_directory="d",
            preparation_gaps=[GAP_U1, GAP_U1.model_copy(update={"id": "U9"})],
        )
    with pytest.raises(ValidationError):
        SourceDocument(text=TEXT, provenance=provenance, preparation_gaps=[GAP_U1])


def test_annotation_fields_cannot_smuggle_delimiters() -> None:
    with pytest.raises(ValueError):
        format_annotation("U3", {"label": "bad ⟧ label"}, "not source text")
