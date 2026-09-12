import pytest
from pydantic import ValidationError

from hitl_research_agent.models.claim import Claim, Evidence


def _grounding_evidence() -> Evidence:
    return Evidence(
        text="The study reports X.",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
    )


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
