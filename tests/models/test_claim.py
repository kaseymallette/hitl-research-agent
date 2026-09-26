import pytest
from pydantic import ValidationError

from hitl_research_agent.models.citation import Citation
from hitl_research_agent.models.claim import Claim, Evidence


def _grounding_evidence() -> Evidence:
    return Evidence(
        text="The study reports X.",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
    )


def test_evidence_citations_default_to_an_empty_list() -> None:
    assert _grounding_evidence().citations == []


def test_evidence_citations_default_is_independent_across_instances() -> None:
    a = _grounding_evidence()
    b = _grounding_evidence()
    a.citations.append(Citation(citation_text="Smith, 2020"))
    assert b.citations == []


def test_evidence_accepts_citations() -> None:
    evidence = Evidence(
        text="detail [Smith, 2020]",
        evidence_form="verbatim",
        relationship_to_claim="direct_support",
        citations=[
            Citation(citation_text="Smith, 2020", reference_entry="Smith, J. A Study. 2020.")
        ],
    )
    assert evidence.citations[0].citation_text == "Smith, 2020"
    assert evidence.citations[0].reference_entry == "Smith, J. A Study. 2020."


def test_whitespace_only_text_rejected() -> None:
    with pytest.raises(ValidationError):
        Evidence(text="   ", evidence_form="verbatim", relationship_to_claim="direct_support")


def test_text_is_stripped() -> None:
    evidence = Evidence(
        text="  hello  ", evidence_form="verbatim", relationship_to_claim="direct_support"
    )
    assert evidence.text == "hello"


def test_unexpected_field_rejected() -> None:
    with pytest.raises(ValidationError):
        Evidence.model_validate(
            {
                "text": "hello",
                "evidence_form": "verbatim",
                "relationship_to_claim": "direct_support",
                "unexpected_field": "nope",
            }
        )


def test_claim_requires_at_least_one_evidence() -> None:
    with pytest.raises(ValidationError):
        Claim(text="X", statement_origin="author_stated", evidence=[])


def test_author_stated_claim_requires_grounding_evidence() -> None:
    with pytest.raises(ValidationError):
        Claim(
            text="X",
            statement_origin="author_stated",
            evidence=[
                Evidence(
                    text="detail",
                    evidence_form="paraphrased",
                    relationship_to_claim="direct_support",
                )
            ],
        )


def test_model_inferred_claim_rejects_grounding_evidence() -> None:
    with pytest.raises(ValidationError):
        Claim(text="X", statement_origin="model_inferred", evidence=[_grounding_evidence()])


def test_claim_grounding_evidence_must_be_verbatim() -> None:
    with pytest.raises(ValidationError):
        Evidence(
            text="paraphrased text",
            evidence_form="paraphrased",
            relationship_to_claim="claim_grounding",
        )


def test_author_stated_claim_with_grounding_evidence_is_valid() -> None:
    claim = Claim(text="X", statement_origin="author_stated", evidence=[_grounding_evidence()])
    assert claim.evidence[0].relationship_to_claim == "claim_grounding"


def test_claim_support_assessment_defaults_to_none() -> None:
    claim = Claim(text="X", statement_origin="author_stated", evidence=[_grounding_evidence()])
    assert claim.support_assessment is None


def test_claim_support_assessment_field_documents_null_as_not_assessed() -> None:
    description = Claim.model_fields["support_assessment"].description
    assert description is not None
    lowered = description.lower()
    assert "none means the claim was not assessed" in lowered
    assert "well-supported" in lowered
    assert "no issue was found" in lowered


def test_claim_accepts_a_support_assessment() -> None:
    claim = Claim(
        text="X",
        statement_origin="author_stated",
        evidence=[_grounding_evidence()],
        support_assessment=(
            "The reasons offered address only two of several plausible alternatives."
        ),
    )
    assert claim.support_assessment == (
        "The reasons offered address only two of several plausible alternatives."
    )


def test_claim_support_assessment_rejects_whitespace_only_when_provided() -> None:
    with pytest.raises(ValidationError):
        Claim(
            text="X",
            statement_origin="author_stated",
            evidence=[_grounding_evidence()],
            support_assessment="   ",
        )
