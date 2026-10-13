import pytest
from pydantic import ValidationError

from hitl_research_agent.extraction.annotations import (
    SENTINEL,
    contains_reserved_character,
    find_annotations,
    format_annotation,
    grounding_view,
    reserved_character_problems,
)
from hitl_research_agent.extraction.grounding import (
    _normalize,
    find_ungrounded_verbatim_evidence,
    find_unverifiable_citations,
)
from hitl_research_agent.extraction.schemas import (
    ExtractedClaim,
    ExtractedEvidence,
    SourceDocument,
)
from hitl_research_agent.models.citation import Citation
from hitl_research_agent.models.provenance import Provenance

ANNOTATION = format_annotation(
    "U1",
    {"kind": "figure", "label": "Figure 1", "page": "2", "image": "images/p2.png"},
    "not source text; content not extracted",
)
TEXT = f"Water use rose sharply in 2023. {ANNOTATION} Cooling relied on evaporative towers."


def _claim(evidence: ExtractedEvidence) -> ExtractedClaim:
    return ExtractedClaim(text="A claim.", statement_origin="author_stated", evidence=[evidence])


def _verbatim(text: str, **kwargs: object) -> ExtractedEvidence:
    return ExtractedEvidence(
        text=text,
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        **kwargs,  # type: ignore[arg-type]
    )


def test_annotation_is_well_formed_and_located() -> None:
    spans = find_annotations(TEXT)
    assert [span.annotation_id for span in spans] == ["U1"]
    assert TEXT[spans[0].start : spans[0].end] == ANNOTATION


def test_grounding_view_replaces_each_annotation_with_one_sentinel() -> None:
    view = grounding_view(TEXT)
    assert view.count(SENTINEL) == 1
    assert "PREP-ANNOTATION" not in view
    assert "Water use rose sharply in 2023." in view


def test_sentinel_survives_the_grounding_normalization() -> None:
    normalized = _normalize(grounding_view(TEXT))
    assert SENTINEL in normalized
    assert normalized.index(SENTINEL) > normalized.index("2023.")


def test_text_without_annotations_is_unchanged_by_the_grounding_view() -> None:
    plain = "No annotations here."
    assert grounding_view(plain) == plain


def test_quote_of_annotation_text_fails_grounding() -> None:
    view = grounding_view(TEXT)
    for quoted in (ANNOTATION, "not source text; content not extracted", "Figure 1"):
        problems = find_ungrounded_verbatim_evidence([_claim(_verbatim(quoted))], view)
        assert len(problems) == 1, quoted


def test_quote_spanning_an_annotation_fails_but_adjacent_real_text_passes() -> None:
    view = grounding_view(TEXT)
    spanning = "rose sharply in 2023. Cooling relied on"
    assert find_ungrounded_verbatim_evidence([_claim(_verbatim(spanning))], view)
    assert not find_ungrounded_verbatim_evidence(
        [_claim(_verbatim("Cooling relied on evaporative towers"))], view
    )
    assert not find_ungrounded_verbatim_evidence(
        [_claim(_verbatim("Water use rose sharply in 2023."))], view
    )


def test_quote_without_a_gap_does_not_match_across_an_annotation_with_no_spaces() -> None:
    glued = f"before{format_annotation('U2', {'kind': 'equation'}, 'not source text')}after"
    view = grounding_view(glued)
    assert find_ungrounded_verbatim_evidence([_claim(_verbatim("beforeafter"))], view)
    assert not find_ungrounded_verbatim_evidence([_claim(_verbatim("before"))], view)


def test_model_quote_containing_the_sentinel_or_delimiters_is_invalid() -> None:
    view = grounding_view(TEXT)
    for quoted in (f"2023.{SENTINEL}Cooling", "⟦PREP-ANNOTATION", "text⟧"):
        problems = find_ungrounded_verbatim_evidence([_claim(_verbatim(quoted))], view)
        assert problems and "not source text" in problems[0]
        assert contains_reserved_character(quoted)


def test_citation_marker_and_reference_entry_cannot_come_from_an_annotation() -> None:
    view = grounding_view(TEXT)
    marker = _verbatim(
        "Cooling relied on evaporative towers",
        citations=[Citation(citation_text="Figure 1")],
    )
    assert find_unverifiable_citations([_claim(marker)], view)  # 'Figure 1' appears only inside it

    annotation_marker = _verbatim(
        "Cooling relied on evaporative towers",
        citations=[Citation(citation_text="⟦PREP-ANNOTATION U1")],
    )
    assert find_unverifiable_citations([_claim(annotation_marker)], view)

    spanning_entry = _verbatim(
        "Cooling relied on evaporative towers",
        citations=[
            Citation(citation_text="2023", reference_entry="rose sharply in 2023. Cooling relied")
        ],
    )
    assert find_unverifiable_citations([_claim(spanning_entry)], view)

    real = _verbatim(
        "Cooling relied on evaporative towers",
        citations=[
            Citation(citation_text="2023", reference_entry="Water use rose sharply in 2023.")
        ],
    )
    assert find_unverifiable_citations([_claim(real)], view) == []


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
    assert SourceDocument(text=TEXT, provenance=provenance).text == TEXT


def test_annotation_fields_cannot_smuggle_delimiters() -> None:
    with pytest.raises(ValueError):
        format_annotation("U3", {"label": "bad ⟧ label"}, "not source text")
