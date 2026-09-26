from collections.abc import Sequence
from datetime import UTC, datetime
from typing import Any

import pytest
from langchain_core.messages import AIMessage, BaseMessage

from hitl_research_agent.config import Settings
from hitl_research_agent.extraction.errors import (
    SourceAnalysisExtractionError,
    SourceAnalysisIncompleteError,
    SourceAnalysisRefusedError,
    SourceAnalysisValidationError,
    SourceTooLargeError,
)
from hitl_research_agent.extraction.pipeline import analyze_source
from hitl_research_agent.extraction.schemas import (
    ExtractedAnalysis,
    ExtractedClaim,
    ExtractedEvidence,
    SourceDocument,
)
from hitl_research_agent.models.citation import Citation
from hitl_research_agent.models.interpreted import Assumption, ResearchProblem
from hitl_research_agent.models.provenance import Provenance

SOURCE_TEXT = (
    "Data centers used 1.7 billion gallons of water in 2023 for cooling "
    "[Lee, 2021]. Lee, K. Cooling Systems Report. 2021."
)


class FakeStructuredModel:
    """Test double satisfying the StructuredOutputModel protocol: returns
    canned responses (or raises canned exceptions) in order, one per call."""

    def __init__(self, responses: list[dict[str, Any] | Exception]) -> None:
        self._responses = list(responses)
        self.calls: list[Sequence[BaseMessage]] = []

    def invoke(self, input: Sequence[BaseMessage]) -> dict[str, Any]:
        self.calls.append(input)
        response = self._responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


def _settings(**overrides: Any) -> Settings:
    defaults: dict[str, Any] = dict(openai_api_key="sk-test")
    defaults.update(overrides)
    return Settings(**defaults)


def _source(text: str = SOURCE_TEXT) -> SourceDocument:
    return SourceDocument(
        text=text,
        provenance=Provenance(
            source_title="Data Center Water Use",
            source_type="peer_reviewed_paper",
            retrieved_at=datetime.now(UTC),
        ),
    )


def _valid_extracted_analysis() -> ExtractedAnalysis:
    return ExtractedAnalysis(
        research_problem=ResearchProblem(
            text="Why do data centers use freshwater?", statement_origin="author_stated"
        ),
        central_claims=[
            ExtractedClaim(
                text="Data centers used 1.7 billion gallons of water in 2023.",
                statement_origin="author_stated",
                evidence=[
                    ExtractedEvidence(
                        text="1.7 billion gallons of water",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
            )
        ],
    )


def _invalid_extracted_analysis() -> ExtractedAnalysis:
    """Valid shape, but the verbatim quote does not appear in SOURCE_TEXT."""
    return ExtractedAnalysis(
        research_problem=ResearchProblem(
            text="Why do data centers use freshwater?", statement_origin="author_stated"
        ),
        central_claims=[
            ExtractedClaim(
                text="Data centers used 3 billion gallons of water in 2023.",
                statement_origin="author_stated",
                evidence=[
                    ExtractedEvidence(
                        text="3 billion gallons of water",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
            )
        ],
    )


def _raw_message(**overrides: Any) -> AIMessage:
    defaults: dict[str, Any] = dict(
        content="",
        usage_metadata={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150},
    )
    defaults.update(overrides)
    return AIMessage(**defaults)


def _response(
    parsed: ExtractedAnalysis | None = None,
    parsing_error: Exception | None = None,
    raw: AIMessage | None = None,
) -> dict[str, Any]:
    return {
        "raw": raw if raw is not None else _raw_message(),
        "parsed": parsed,
        "parsing_error": parsing_error,
    }


def test_oversized_source_raises_before_model_is_invoked() -> None:
    model = FakeStructuredModel([])
    with pytest.raises(SourceTooLargeError):
        analyze_source(
            _source(text="x " * 20),
            model=model,
            settings=_settings(max_source_characters=10),
        )
    assert model.calls == []


def test_valid_first_attempt_returns_result_with_attempt_count_one() -> None:
    model = FakeStructuredModel([_response(parsed=_valid_extracted_analysis())])
    result = analyze_source(_source(), model=model, settings=_settings())

    assert result.attempt_count == 1
    assert result.input_tokens == 100
    assert result.output_tokens == 50
    assert result.model == "gpt-6-astra"
    assert len(model.calls) == 1


def test_invalid_then_valid_sums_usage_and_reports_attempt_count_two() -> None:
    first_raw = _raw_message(
        usage_metadata={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150}
    )
    second_raw = _raw_message(
        usage_metadata={"input_tokens": 120, "output_tokens": 60, "total_tokens": 180}
    )
    model = FakeStructuredModel(
        [
            _response(parsed=_invalid_extracted_analysis(), raw=first_raw),
            _response(parsed=_valid_extracted_analysis(), raw=second_raw),
        ]
    )

    result = analyze_source(_source(), model=model, settings=_settings())

    assert result.attempt_count == 2
    assert result.input_tokens == 220
    assert result.output_tokens == 110
    assert len(model.calls) == 2
    # The correction call includes the prior AI response and feedback about
    # what was wrong with it.
    correction_call = model.calls[1]
    assert correction_call[-2] is first_raw
    assert "3 billion gallons" in correction_call[-1].content


def test_invalid_on_both_attempts_raises_after_exactly_one_retry() -> None:
    model = FakeStructuredModel(
        [
            _response(parsed=_invalid_extracted_analysis()),
            _response(parsed=_invalid_extracted_analysis()),
        ]
    )

    with pytest.raises(SourceAnalysisValidationError) as exc_info:
        analyze_source(_source(), model=model, settings=_settings())

    assert exc_info.value.attempt_count == 2
    assert len(model.calls) == 2


def test_refusal_raises_immediately_without_a_correction_attempt() -> None:
    raw = _raw_message(additional_kwargs={"refusal": "the request could not be fulfilled"})
    model = FakeStructuredModel([_response(raw=raw)])

    with pytest.raises(SourceAnalysisRefusedError):
        analyze_source(_source(), model=model, settings=_settings())

    assert len(model.calls) == 1


def test_incomplete_output_raises_immediately_without_a_correction_attempt() -> None:
    raw = _raw_message(
        response_metadata={
            "status": "incomplete",
            "incomplete_details": {"reason": "max_output_tokens"},
        }
    )
    model = FakeStructuredModel([_response(raw=raw)])

    with pytest.raises(SourceAnalysisIncompleteError):
        analyze_source(_source(), model=model, settings=_settings())

    assert len(model.calls) == 1


def test_technical_failure_raises_and_produces_no_result() -> None:
    model = FakeStructuredModel([TimeoutError("connection timed out")])

    with pytest.raises(SourceAnalysisExtractionError):
        analyze_source(_source(), model=model, settings=_settings())


def test_missing_usage_metadata_raises_rather_than_reporting_zero() -> None:
    raw = _raw_message(usage_metadata=None)
    model = FakeStructuredModel([_response(parsed=_valid_extracted_analysis(), raw=raw)])

    with pytest.raises(SourceAnalysisExtractionError):
        analyze_source(_source(), model=model, settings=_settings())


def _extracted_analysis_with_citation(*, reference_entry: str | None) -> ExtractedAnalysis:
    return ExtractedAnalysis(
        research_problem=ResearchProblem(
            text="Why do data centers use freshwater?", statement_origin="author_stated"
        ),
        central_claims=[
            ExtractedClaim(
                text="Data centers used 1.7 billion gallons of water in 2023.",
                statement_origin="author_stated",
                evidence=[
                    ExtractedEvidence(
                        text="1.7 billion gallons of water",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                        citations=[
                            Citation(citation_text="Lee, 2021", reference_entry=reference_entry)
                        ],
                    )
                ],
            )
        ],
    )


def test_citations_survive_assembly_into_the_final_analysis() -> None:
    extracted = _extracted_analysis_with_citation(
        reference_entry="Lee, K. Cooling Systems Report. 2021."
    )
    model = FakeStructuredModel([_response(parsed=extracted)])

    result = analyze_source(_source(), model=model, settings=_settings())

    assert result.attempt_count == 1
    citations = result.analysis.central_claims[0].evidence[0].citations
    assert len(citations) == 1
    assert citations[0].citation_text == "Lee, 2021"
    assert citations[0].reference_entry == "Lee, K. Cooling Systems Report. 2021."


def test_unverifiable_citation_triggers_one_correction_attempt() -> None:
    invalid = _extracted_analysis_with_citation(
        reference_entry="Nguyen, T. An Invented Study. 1999."
    )
    model = FakeStructuredModel(
        [
            _response(parsed=invalid),
            _response(parsed=_valid_extracted_analysis()),
        ]
    )

    result = analyze_source(_source(), model=model, settings=_settings())

    assert result.attempt_count == 2
    correction_call = model.calls[1]
    assert "Invented Study" in correction_call[-1].content


def test_support_assessment_and_its_assumption_survive_assembly() -> None:
    """Plumbing only: proves a support_assessment and a connected assumption
    written by an (injected, fake) model reach the final SourceAnalysis
    unchanged. This says nothing about whether a live model can produce a
    sound assessment — that requires a real run, not a fixture."""
    extracted = ExtractedAnalysis(
        research_problem=ResearchProblem(
            text="Why do data centers use freshwater?", statement_origin="author_stated"
        ),
        central_claims=[
            ExtractedClaim(
                text="Data centers used 1.7 billion gallons of water in 2023.",
                statement_origin="author_stated",
                evidence=[
                    ExtractedEvidence(
                        text="1.7 billion gallons of water",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
                support_assessment=(
                    "The passage states the figure but does not explain how it was measured; "
                    "an assumption about measurement reliability is needed to accept it as stated."
                ),
            )
        ],
        assumptions=[
            Assumption(
                text=(
                    "The cited water-use figure was measured reliably enough to state without "
                    "qualification."
                ),
                statement_origin="model_inferred",
            )
        ],
    )
    model = FakeStructuredModel([_response(parsed=extracted)])

    result = analyze_source(_source(), model=model, settings=_settings())

    claim = result.analysis.central_claims[0]
    assert claim.support_assessment == (
        "The passage states the figure but does not explain how it was measured; "
        "an assumption about measurement reliability is needed to accept it as stated."
    )
    assert len(result.analysis.assumptions) == 1
    assert result.analysis.assumptions[0].statement_origin == "model_inferred"


def test_support_assessment_defaults_to_none_when_not_provided() -> None:
    model = FakeStructuredModel([_response(parsed=_valid_extracted_analysis())])
    result = analyze_source(_source(), model=model, settings=_settings())
    assert result.analysis.central_claims[0].support_assessment is None
