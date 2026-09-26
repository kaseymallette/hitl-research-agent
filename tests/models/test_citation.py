import pytest
from pydantic import ValidationError

from hitl_research_agent.models.citation import Citation


def test_citation_requires_non_empty_citation_text() -> None:
    with pytest.raises(ValidationError):
        Citation(citation_text="   ")


def test_citation_reference_entry_defaults_to_none() -> None:
    citation = Citation(citation_text="Harrison Dupre, 2025")
    assert citation.reference_entry is None


def test_citation_reference_entry_rejects_whitespace_only_when_provided() -> None:
    with pytest.raises(ValidationError):
        Citation(citation_text="Harrison Dupre, 2025", reference_entry="   ")


def test_citation_rejects_unrecognized_fields() -> None:
    with pytest.raises(ValidationError):
        Citation(citation_text="Harrison Dupre, 2025", url="https://example.com")  # type: ignore[call-arg]


def test_citation_constructs_with_reference_entry() -> None:
    citation = Citation(
        citation_text="Harrison Dupre, 2025",
        reference_entry=(
            'Maggie Harrison Dupre. Stanford Research Finds That "Therapist" Chatbots Are '
            "Encouraging Users' Schizophrenic Delusions and Suicidal Thoughts. June 2025."
        ),
    )
    assert citation.reference_entry is not None
    assert citation.reference_entry.startswith("Maggie Harrison Dupre")
