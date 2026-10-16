from collections.abc import Sequence
from datetime import UTC, datetime, timedelta
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
    AnalysisResult,
    ExtractedAnalysis,
    ExtractedClaim,
    ExtractedEvidence,
    PreparationGap,
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


GAP_U1 = PreparationGap(id="U1", kind="figure", page=2, label="Figure 1", image="images/p2.png")


def _source(text: str = SOURCE_TEXT) -> SourceDocument:
    """Annotated text must declare its gaps, so the helper supplies them when present."""
    annotated = "PREP-ANNOTATION U1" in text
    return SourceDocument(
        text=text,
        preparation_directory="outputs/phase_3/prepared/fixture" if annotated else None,
        preparation_gaps=[GAP_U1] if annotated else [],
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


def _unreadable_response(raw: AIMessage | None = None) -> dict[str, Any]:
    """An attempt whose JSON could not be read -- the remaining reason for a
    correction attempt now that quotation and label checks are advisory."""
    return _response(parsing_error=ValueError("could not parse model output"), raw=raw)


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


def test_unreadable_then_valid_sums_usage_and_reports_attempt_count_two() -> None:
    first_raw = _raw_message(
        usage_metadata={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150}
    )
    second_raw = _raw_message(
        usage_metadata={"input_tokens": 120, "output_tokens": 60, "total_tokens": 180}
    )
    model = FakeStructuredModel(
        [
            _unreadable_response(raw=first_raw),
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
    assert "could not parse model output" in correction_call[-1].content


def test_unreadable_on_both_attempts_raises_after_exactly_one_retry() -> None:
    model = FakeStructuredModel([_unreadable_response(), _unreadable_response()])

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


# --- Change 1: annotation-aware grounding through the pipeline -----------------------------

ANNOTATED_SOURCE = (
    "Data centers used 1.7 billion gallons of water in 2023. "
    "⟦PREP-ANNOTATION U1 kind=figure label=Figure 1 page=2 image=images/p2.png: "
    "not source text; content not extracted⟧ Cooling relied on evaporative towers."
)


def _analysis_quoting(quote: str) -> ExtractedAnalysis:
    return ExtractedAnalysis(
        research_problem=ResearchProblem(text="Why?", statement_origin="author_stated"),
        central_claims=[
            ExtractedClaim(
                text="A claim.",
                statement_origin="author_stated",
                evidence=[
                    ExtractedEvidence(
                        text=quote,
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
            )
        ],
    )


def test_source_without_annotations_behaves_as_before() -> None:
    model = FakeStructuredModel([_response(parsed=_valid_extracted_analysis())])
    assert analyze_source(_source(), model=model, settings=_settings()).attempt_count == 1


# --- Change 2: citation formatting through the pipeline ------------------------------------

GROUPED_SOURCE = (
    "Data centers used 1.7 billion gallons of water in 2023.<sup>23,32,33</sup>\n"
    "References\n"
    "23. Reig, P. Guidance for water use. WRI (2020).\n"
    "24. Other, A. Filler entry. (2021).\n"
    "32. EIA. Open Data.\n"
    "33. EPA. eGRID Data Explorer.\n"
)
_ENTRIES = [
    "23. Reig, P. Guidance for water use. WRI (2020).",
    "32. EIA. Open Data.",
    "33. EPA. eGRID Data Explorer.",
]


def _analysis_with_citations(citations: list[Citation]) -> ExtractedAnalysis:
    return ExtractedAnalysis(
        research_problem=ResearchProblem(text="Why?", statement_origin="author_stated"),
        central_claims=[
            ExtractedClaim(
                text="Data centers used 1.7 billion gallons of water in 2023.",
                statement_origin="author_stated",
                evidence=[
                    ExtractedEvidence(
                        text="1.7 billion gallons of water",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                        citations=citations,
                    )
                ],
            )
        ],
    )


# --- Change 3: attempt retention -----------------------------------------------------------


class _Clock:
    """Deterministic clock: each call advances 1 second."""

    def __init__(self) -> None:
        self._now = datetime(2026, 1, 1, tzinfo=UTC)

    def __call__(self) -> datetime:
        current = self._now
        self._now = self._now + timedelta(seconds=1)
        return current


def _raw_with_detail(response_id: str, *, reasoning: int, cache_read: int = 0) -> AIMessage:
    return AIMessage(
        content="raw model text",
        id=response_id,
        usage_metadata={
            "input_tokens": 100,
            "output_tokens": 50,
            "total_tokens": 150,
            "input_token_details": {"cache_read": cache_read, "cache_creation": 7},
            "output_token_details": {"reasoning": reasoning},
        },
        response_metadata={
            "id": response_id,
            "model_name": "gpt-6-astra",
            "status": "completed",
            "service_tier": "default",
            "authorization": "Bearer sk-secret",
            "headers": {"x-api-key": "sk-secret"},
        },
    )


def test_first_attempt_success_records_one_attempt_with_usage_and_timing() -> None:
    model = FakeStructuredModel(
        [
            _response(
                parsed=_valid_extracted_analysis(), raw=_raw_with_detail("resp_1", reasoning=14)
            )
        ]
    )
    result = analyze_source(_source(), model=model, settings=_settings(), clock=_Clock())

    assert len(result.attempts) == result.attempt_count == 1
    record = result.attempts[0]
    assert record.outcome == "valid"
    assert record.request_id == "resp_1"
    assert record.elapsed_seconds == 1.0
    assert record.parsed_output is not None
    assert record.raw_content == "raw model text"
    assert record.usage is not None
    assert (record.usage.input_tokens, record.usage.output_tokens) == (100, 50)
    assert record.usage.reasoning_tokens == 14
    assert record.usage.cache_creation_input_tokens == 7


def test_correction_success_retains_the_failed_attempt_with_errors_and_parsed_output() -> None:
    model = FakeStructuredModel(
        [
            _response(
                parsed=_invalid_extracted_analysis(),
                parsing_error=ValueError("schema mismatch"),
                raw=_raw_with_detail("resp_a", reasoning=3),
            ),
            _response(
                parsed=_valid_extracted_analysis(),
                raw=_raw_with_detail("resp_b", reasoning=5, cache_read=100),
            ),
        ]
    )
    result = analyze_source(_source(), model=model, settings=_settings(), clock=_Clock())

    first, second = result.attempts
    assert (first.outcome, second.outcome) == ("parse_error", "valid")
    assert "schema mismatch" in first.problems[0]
    assert first.parsed_output is not None
    assert [first.request_id, second.request_id] == ["resp_a", "resp_b"]
    assert second.usage is not None and second.usage.cached_input_tokens == 100
    # totals are exactly the sum of reported usage; reasoning is not added again
    assert result.output_tokens == 100
    assert sum(a.usage.output_tokens for a in result.attempts if a.usage) == 100


def test_terminal_validation_failure_exposes_every_attempt() -> None:
    model = FakeStructuredModel(
        [
            _response(
                parsed=_invalid_extracted_analysis(),
                parsing_error=ValueError("schema mismatch"),
                raw=_raw_with_detail("r1", reasoning=1),
            ),
            _response(
                parsed=_invalid_extracted_analysis(),
                parsing_error=ValueError("schema mismatch"),
                raw=_raw_with_detail("r2", reasoning=2),
            ),
        ]
    )
    with pytest.raises(SourceAnalysisValidationError) as exc_info:
        analyze_source(_source(), model=model, settings=_settings())
    exc = exc_info.value
    assert [a.request_id for a in exc.attempts] == ["r1", "r2"]
    assert all(a.outcome == "parse_error" and a.parsed_output for a in exc.attempts)
    assert exc.output_tokens == 100 and exc.attempt_count == 2


def test_parse_error_is_recorded_without_parsed_output() -> None:
    model = FakeStructuredModel(
        [
            _response(
                parsing_error=ValueError("bad json"), raw=_raw_with_detail("r1", reasoning=0)
            ),
            _response(parsed=_valid_extracted_analysis(), raw=_raw_with_detail("r2", reasoning=0)),
        ]
    )
    result = analyze_source(_source(), model=model, settings=_settings())
    assert [a.outcome for a in result.attempts] == ["parse_error", "valid"]
    assert result.attempts[0].parsed_output is None
    assert "bad json" in result.attempts[0].problems[0]


def test_refusal_incomplete_and_technical_failures_keep_categories_and_carry_attempts() -> None:
    refusal = AIMessage(
        content="",
        id="r_refused",
        additional_kwargs={"refusal": "no"},
        usage_metadata={"input_tokens": 1, "output_tokens": 1, "total_tokens": 2},
    )
    with pytest.raises(SourceAnalysisRefusedError) as refused:
        analyze_source(
            _source(), model=FakeStructuredModel([_response(raw=refusal)]), settings=_settings()
        )
    assert [a.outcome for a in refused.value.attempts] == ["refused"]
    assert refused.value.attempts[0].request_id == "r_refused"

    incomplete = _raw_message(
        response_metadata={
            "status": "incomplete",
            "incomplete_details": {"reason": "max_output_tokens"},
        }
    )
    with pytest.raises(SourceAnalysisIncompleteError) as stopped:
        analyze_source(
            _source(), model=FakeStructuredModel([_response(raw=incomplete)]), settings=_settings()
        )
    assert [a.outcome for a in stopped.value.attempts] == ["incomplete"]

    with pytest.raises(SourceAnalysisExtractionError) as failed:
        analyze_source(
            _source(),
            model=FakeStructuredModel([TimeoutError("timed out")]),
            settings=_settings(),
        )
    record = failed.value.attempts[0]
    assert record.outcome == "technical_failure" and record.usage is None
    assert "timed out" in (record.error or "")


def test_technical_failure_on_the_correction_call_keeps_the_first_attempt() -> None:
    model = FakeStructuredModel(
        [
            _unreadable_response(raw=_raw_with_detail("r1", reasoning=1)),
            TimeoutError("timed out"),
        ]
    )
    with pytest.raises(SourceAnalysisExtractionError) as failed:
        analyze_source(_source(), model=model, settings=_settings())
    assert [a.outcome for a in failed.value.attempts] == ["parse_error", "technical_failure"]


def test_missing_usage_keeps_the_raw_response_as_a_technical_failure_record() -> None:
    raw = _raw_message(usage_metadata=None, content="payload", id="r_nousage")
    model = FakeStructuredModel([_response(parsed=_valid_extracted_analysis(), raw=raw)])
    with pytest.raises(SourceAnalysisExtractionError) as failed:
        analyze_source(_source(), model=model, settings=_settings())
    record = failed.value.attempts[0]
    assert record.raw_content == "payload" and record.usage is None


def test_secrets_and_unlisted_metadata_are_not_stored() -> None:
    model = FakeStructuredModel(
        [_response(parsed=_valid_extracted_analysis(), raw=_raw_with_detail("resp_1", reasoning=0))]
    )
    result = analyze_source(_source(), model=model, settings=_settings(openai_api_key="sk-secret"))
    dumped = result.model_dump_json()
    assert "sk-secret" not in dumped
    assert "authorization" not in dumped and "x-api-key" not in dumped
    assert set(result.attempts[0].response_metadata) <= {
        "id",
        "model",
        "model_name",
        "object",
        "status",
        "service_tier",
        "incomplete_details",
    }


def test_analysis_result_with_attempts_round_trips_and_old_json_still_loads() -> None:
    model = FakeStructuredModel(
        [_response(parsed=_valid_extracted_analysis(), raw=_raw_with_detail("resp_1", reasoning=2))]
    )
    result = analyze_source(_source(), model=model, settings=_settings())
    assert AnalysisResult.model_validate_json(result.model_dump_json()) == result

    legacy = result.model_dump(mode="json")
    del legacy["attempts"]
    loaded = AnalysisResult.model_validate(legacy)
    assert loaded.attempts == [] and loaded.attempt_count == 1


def test_attempts_must_match_attempt_count_when_present() -> None:
    model = FakeStructuredModel([_response(parsed=_valid_extracted_analysis())])
    result = analyze_source(_source(), model=model, settings=_settings())
    broken = result.model_dump(mode="json")
    broken["attempt_count"] = 2
    with pytest.raises(ValueError):
        AnalysisResult.model_validate(broken)
