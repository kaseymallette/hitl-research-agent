"""The call path: what comes back, what is recorded, and what stops a run.

The measurement machinery is the point of these: Phase 1 compares four
configurations on usage, cost and runtime, so a lost attempt record or a
miscounted token is a broken experiment, not a cosmetic bug.
"""

from collections.abc import Sequence
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import pytest
from langchain_core.messages import AIMessage, BaseMessage

from hitl_research_agent.analysis import AnalysisError, analyze_source
from hitl_research_agent.config import Settings
from hitl_research_agent.inputs import format_annotation, load_attachment
from hitl_research_agent.models import (
    ANALYSIS_SCOPE,
    ANALYSIS_SCOPE_PDF,
    ANALYSIS_SCOPE_TEXT_AND_CROPS,
    Claim,
    Evidence,
    ExtractedAnalysis,
    PreparationGap,
    Provenance,
    SourceDocument,
    Statement,
)

PROVENANCE = Provenance(
    source_title="A Paper",
    source_type="peer_reviewed_paper",
    retrieved_at=datetime(2026, 10, 13, tzinfo=UTC),
)
ANNOTATION = format_annotation(
    "U1", {"kind": "figure", "label": "Figure 1", "page": "4"}, "content not extracted"
)
GAP = PreparationGap(id="U1", kind="figure", page=4, label="Figure 1", image="images/U1_p04.png")


def _settings(**overrides: Any) -> Settings:
    base: dict[str, Any] = {"openai_api_key": "test-key", "openai_model": "gpt-6.1-sol"}
    return Settings(**{**base, **overrides})


def _source(*, annotated: bool = False, text: str | None = None) -> SourceDocument:
    return SourceDocument(
        text=text or (f"Body. {ANNOTATION} More." if annotated else "Body text."),
        provenance=PROVENANCE,
        preparation_directory="outputs/preparation/fixture" if annotated else None,
        preparation_gaps=[GAP] if annotated else [],
    )


def _content(claim_text: str = "Cooling drives water use.") -> ExtractedAnalysis:
    return ExtractedAnalysis(
        research_problem=Statement(
            text="Water use is unmeasured.", statement_origin="author_stated"
        ),
        central_claims=[
            Claim(
                text=claim_text,
                statement_origin="author_stated",
                evidence=[
                    Evidence(
                        text="Cooling accounted for most withdrawal.",
                        evidence_form="paraphrased",
                        relationship_to_claim="direct_support",
                    )
                ],
            )
        ],
        argument_assessment="The conclusion follows only if measurement is feasible.",
    )


def _response(
    parsed: ExtractedAnalysis | None,
    *,
    input_tokens: int = 100,
    output_tokens: int = 50,
    reasoning: int | None = None,
    cached: int | None = None,
    parsing_error: Exception | None = None,
    metadata: dict[str, Any] | None = None,
    additional_kwargs: dict[str, Any] | None = None,
    content: Any = "",
    request_id: str = "resp_1",
) -> dict[str, Any]:
    usage: dict[str, Any] = {"input_tokens": input_tokens, "output_tokens": output_tokens}
    usage["total_tokens"] = input_tokens + output_tokens
    if reasoning is not None:
        usage["output_token_details"] = {"reasoning": reasoning}
    if cached is not None:
        usage["input_token_details"] = {"cache_read": cached}
    raw = AIMessage(
        content=content,
        id=request_id,
        usage_metadata=usage,  # type: ignore[arg-type]
        response_metadata=metadata or {},
        additional_kwargs=additional_kwargs or {},
    )
    return {"raw": raw, "parsed": parsed, "parsing_error": parsing_error}


class FakeModel:
    """Returns queued responses and records what it was sent."""

    def __init__(self, responses: Sequence[dict[str, Any]]) -> None:
        self._responses = list(responses)
        self.calls: list[Sequence[BaseMessage]] = []

    def invoke(self, input: Sequence[BaseMessage]) -> dict[str, Any]:
        self.calls.append(list(input))
        if not self._responses:
            raise AssertionError("the pipeline made more calls than the test queued")
        return self._responses.pop(0)


class ExplodingModel:
    def invoke(self, input: Sequence[BaseMessage]) -> dict[str, Any]:
        raise RuntimeError("connection reset")


def _clock() -> Any:
    start = datetime(2026, 10, 15, 12, tzinfo=UTC)
    ticks = iter(range(100))
    return lambda: start + timedelta(seconds=next(ticks) * 3)


# --------------------------------------------------------------------------- the happy path


def test_one_call_returns_the_analysis_the_model_produced() -> None:
    model = FakeModel([_response(_content())])
    result = analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    assert result.analysis.content.central_claims[0].text == "Cooling drives water use."
    assert result.analysis.provenance == PROVENANCE  # application-owned, not from the model
    assert result.attempt_count == 1
    assert result.model == "gpt-6.1-sol"
    assert result.analysis_scope == ANALYSIS_SCOPE


def test_usage_and_runtime_are_recorded_per_attempt_and_in_total() -> None:
    model = FakeModel(
        [_response(_content(), input_tokens=1200, output_tokens=800, reasoning=600, cached=300)]
    )
    result = analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    assert (result.input_tokens, result.output_tokens) == (1200, 800)
    usage = result.attempts[0].usage
    assert usage is not None
    assert usage.reasoning_tokens == 600  # a subset of output, never added to it
    assert usage.cached_input_tokens == 300
    assert result.attempts[0].elapsed_seconds == 3.0
    assert result.attempts[0].request_id == "resp_1"


# --------------------------------------------------------------------------- the correction


def test_unparseable_output_gets_one_correction_and_both_attempts_are_kept() -> None:
    model = FakeModel(
        [
            _response(None, parsing_error=ValueError("not valid JSON"), request_id="resp_1"),
            _response(_content(), input_tokens=130, output_tokens=70, request_id="resp_2"),
        ]
    )
    result = analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    assert result.attempt_count == 2
    assert [a.outcome for a in result.attempts] == ["parse_error", "valid"]
    assert (result.input_tokens, result.output_tokens) == (230, 120)  # summed, not replaced
    assert [a.request_id for a in result.attempts] == ["resp_1", "resp_2"]


def test_the_correction_message_carries_the_problem_and_the_original_input() -> None:
    model = FakeModel(
        [_response(None, parsing_error=ValueError("missing field")), _response(_content())]
    )
    analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    second = model.calls[1]
    assert len(second) > len(model.calls[0])  # the original turn is still present
    assert "missing field" in str(second[-1].content)


def test_a_second_failure_raises_with_both_attempts_and_the_summed_usage() -> None:
    model = FakeModel(
        [
            _response(None, parsing_error=ValueError("bad"), input_tokens=100, output_tokens=50),
            _response(
                None, parsing_error=ValueError("still bad"), input_tokens=110, output_tokens=60
            ),
        ]
    )
    with pytest.raises(AnalysisError) as caught:
        analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    error = caught.value
    assert error.kind == "invalid_after_correction"
    assert len(error.attempts) == 2
    assert (error.input_tokens, error.output_tokens) == (210, 110)
    assert "still bad" in str(error)


# --------------------------------------------------------------------------- what stops a run


def test_a_refusal_stops_the_run_without_spending_the_correction() -> None:
    """There is no partial analysis to correct, so a second call would be waste."""
    model = FakeModel([_response(None, additional_kwargs={"refusal": "cannot assist"})])
    with pytest.raises(AnalysisError) as caught:
        analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    assert caught.value.kind == "refused"
    assert len(caught.value.attempts) == 1
    assert caught.value.attempts[0].outcome == "refused"
    assert caught.value.input_tokens == 100  # a response arrived, so usage is known


def test_a_refusal_in_a_content_block_is_also_detected() -> None:
    """Both documented placements are checked; no live refusal has been seen."""
    model = FakeModel([_response(None, content=[{"type": "refusal", "refusal": "declined"}])])
    with pytest.raises(AnalysisError) as caught:
        analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    assert caught.value.kind == "refused"
    assert caught.value.problems == ["declined"]


def test_a_truncated_generation_stops_the_run_and_names_the_reason() -> None:
    model = FakeModel(
        [
            _response(
                None,
                metadata={
                    "status": "incomplete",
                    "incomplete_details": {"reason": "max_output_tokens"},
                },
            )
        ]
    )
    with pytest.raises(AnalysisError) as caught:
        analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    assert caught.value.kind == "incomplete"
    assert caught.value.problems == ["max_output_tokens"]


def test_a_transport_failure_is_recorded_with_no_fabricated_usage() -> None:
    with pytest.raises(AnalysisError) as caught:
        analyze_source(_source(), model=ExplodingModel(), settings=_settings(), clock=_clock())
    error = caught.value
    assert error.kind == "transport"
    assert error.input_tokens == 0 and error.output_tokens == 0
    assert len(error.attempts) == 1
    assert error.attempts[0].outcome == "technical_failure"
    assert error.attempts[0].usage is None
    assert "connection reset" in str(error.attempts[0].error)


def test_a_response_without_usage_metadata_is_a_failure_not_a_zero() -> None:
    """Reporting zero tokens for a call that happened would corrupt the cost record."""
    raw = AIMessage(content="", id="resp_1")
    model = FakeModel([{"raw": raw, "parsed": _content(), "parsing_error": None}])
    with pytest.raises(AnalysisError, match="usage metadata"):
        analyze_source(_source(), model=model, settings=_settings(), clock=_clock())


def test_an_oversized_source_is_refused_before_any_call_is_made() -> None:
    model = FakeModel([])
    with pytest.raises(AnalysisError) as caught:
        analyze_source(
            _source(text="x" * 500),
            model=model,
            settings=_settings(max_source_characters=100),
            clock=_clock(),
        )
    assert caught.value.kind == "source_too_large"
    assert caught.value.attempts == []
    assert model.calls == []  # nothing was spent


# --------------------------------------------------------------------------- input modes


def test_a_pdf_run_records_its_scope_and_the_bytes_it_sent(tmp_path: Path) -> None:
    (tmp_path / "source.pdf").write_bytes(b"%PDF-1.7 body")
    attachment = load_attachment(tmp_path, "source.pdf", kind="pdf")
    model = FakeModel([_response(_content())])
    result = analyze_source(
        _source(),
        model=model,
        settings=_settings(),
        clock=_clock(),
        input_mode="pdf",
        attachments=[attachment],
    )
    assert result.input_mode == "pdf"
    assert result.analysis_scope == ANALYSIS_SCOPE_PDF
    assert "page image" in result.analysis_scope
    assert [item["path"] for item in result.model_inputs] == ["source.pdf"]
    assert result.model_inputs[0]["sha256"] == attachment.record.sha256


def test_a_crops_run_records_each_crop_against_its_gap(tmp_path: Path) -> None:
    (tmp_path / "crop.png").write_bytes(b"\x89PNG\r\n\x1a\n fake")
    crop = load_attachment(tmp_path, "crop.png", kind="image", page=4, gap_id="U1")
    model = FakeModel([_response(_content())])
    result = analyze_source(
        _source(annotated=True),
        model=model,
        settings=_settings(),
        clock=_clock(),
        input_mode="prepared_text_and_crops",
        attachments=[crop],
    )
    assert result.analysis_scope == ANALYSIS_SCOPE_TEXT_AND_CROPS
    assert result.model_inputs[0]["gap_id"] == "U1"
    assert [gap.id for gap in result.preparation_gaps] == ["U1"]
    assert result.preparation_directory == "outputs/preparation/fixture"


def test_attachments_are_resent_with_the_correction(tmp_path: Path) -> None:
    """A correction that dropped the source would be answered from nothing."""
    (tmp_path / "source.pdf").write_bytes(b"%PDF-1.7 body")
    attachment = load_attachment(tmp_path, "source.pdf", kind="pdf")
    model = FakeModel([_response(None, parsing_error=ValueError("bad")), _response(_content())])
    analyze_source(
        _source(),
        model=model,
        settings=_settings(),
        clock=_clock(),
        input_mode="pdf",
        attachments=[attachment],
    )
    resent = str(model.calls[1][1].content)
    assert "file" in resent and attachment.data[:40] in resent


def test_a_mismatched_input_mode_is_a_caller_error_not_an_analysis_failure(tmp_path: Path) -> None:
    (tmp_path / "source.pdf").write_bytes(b"%PDF-1.7 body")
    attachment = load_attachment(tmp_path, "source.pdf", kind="pdf")
    with pytest.raises(ValueError, match="sends no attachments"):
        analyze_source(
            _source(), model=FakeModel([]), settings=_settings(), attachments=[attachment]
        )


def test_the_result_round_trips_so_a_run_record_can_be_read_back() -> None:
    from hitl_research_agent.analysis import AnalysisResult

    model = FakeModel([_response(_content())])
    result = analyze_source(_source(), model=model, settings=_settings(), clock=_clock())
    restored = AnalysisResult.model_validate_json(result.model_dump_json())
    assert restored.input_tokens == result.input_tokens
    assert restored.attempts[0].outcome == "valid"
