from datetime import UTC, datetime

import pytest
from openai.lib._pydantic import to_strict_json_schema
from pydantic import ValidationError

from hitl_research_agent.extraction.schemas import (
    AnalysisResult,
    ExtractedAnalysis,
    ExtractedClaim,
    ExtractedEvidence,
    SourceDocument,
)
from hitl_research_agent.models.analysis import SourceAnalysis
from hitl_research_agent.models.claim import Claim, Evidence
from hitl_research_agent.models.interpreted import ResearchProblem
from hitl_research_agent.models.provenance import Provenance


def _minimal_source_analysis() -> SourceAnalysis:
    return SourceAnalysis(
        provenance=Provenance(
            source_title="T", source_type="peer_reviewed_paper", retrieved_at=datetime.now(UTC)
        ),
        research_problem=ResearchProblem(text="Problem", statement_origin="author_stated"),
        central_claims=[
            Claim(
                text="Claim",
                statement_origin="author_stated",
                evidence=[
                    Evidence(
                        text="quote",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
            )
        ],
    )


def test_source_document_rejects_empty_text() -> None:
    with pytest.raises(ValidationError):
        SourceDocument(
            text="   ",
            provenance=Provenance(
                source_title="T", source_type="other", retrieved_at=datetime.now(UTC)
            ),
        )


def test_extracted_evidence_has_no_id_field() -> None:
    evidence = ExtractedEvidence(
        text="quote", evidence_form="verbatim", relationship_to_claim="claim_grounding"
    )
    assert "id" not in evidence.model_dump()


def test_extracted_claim_has_no_id_field_and_requires_evidence() -> None:
    claim = ExtractedClaim(
        text="claim",
        statement_origin="author_stated",
        evidence=[
            ExtractedEvidence(
                text="quote", evidence_form="verbatim", relationship_to_claim="claim_grounding"
            )
        ],
    )
    assert "id" not in claim.model_dump()
    with pytest.raises(ValidationError):
        ExtractedClaim(text="claim", statement_origin="author_stated", evidence=[])


def test_extracted_analysis_requires_at_least_one_claim() -> None:
    with pytest.raises(ValidationError):
        ExtractedAnalysis(
            research_problem=ResearchProblem(text="p", statement_origin="author_stated"),
            central_claims=[],
        )


def test_analysis_result_bounds_attempt_count_and_tokens() -> None:
    analysis = _minimal_source_analysis()
    with pytest.raises(ValidationError):
        AnalysisResult(
            analysis=analysis, model="gpt-6-sol", input_tokens=1, output_tokens=1, attempt_count=3
        )
    with pytest.raises(ValidationError):
        AnalysisResult(
            analysis=analysis, model="gpt-6-sol", input_tokens=-1, output_tokens=1, attempt_count=1
        )


def test_strict_schema_conversion_succeeds_and_omits_application_owned_ids() -> None:
    """Exercises the same schema-conversion code path langchain-openai's
    method="json_schema" uses, without sending any request, so incompatible
    schema shapes are caught locally rather than at call time."""
    schema = to_strict_json_schema(ExtractedAnalysis)
    defs = schema["$defs"]

    assert "id" not in defs["ExtractedEvidence"]["properties"]
    assert "id" not in defs["ExtractedClaim"]["properties"]

    # Optional fields stay present-but-nullable, matching OpenAI's documented
    # "every property required, use null for absence" strict-mode pattern.
    assert "locator" in defs["ExtractedEvidence"]["required"]
    assert schema["properties"]["methodology"] == {
        "anyOf": [{"$ref": "#/$defs/Methodology"}, {"type": "null"}]
    }
    assert "methodology" in schema["required"]
