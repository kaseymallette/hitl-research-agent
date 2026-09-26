from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Protocol

from langchain_core.messages import AIMessage, BaseMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr, ValidationError

from ..config import Settings
from ..models.analysis import SourceAnalysis
from ..models.claim import Claim, Evidence
from ..models.provenance import Provenance
from .errors import (
    SourceAnalysisError,
    SourceAnalysisExtractionError,
    SourceAnalysisIncompleteError,
    SourceAnalysisRefusedError,
    SourceAnalysisValidationError,
    SourceTooLargeError,
)
from .grounding import find_ungrounded_verbatim_evidence, find_unverifiable_citations
from .prompts import build_correction_messages, build_messages
from .schemas import AnalysisResult, ExtractedAnalysis, SourceDocument


class StructuredOutputModel(Protocol):
    """The minimal interface analyze_source() depends on.

    Satisfied by `ChatOpenAI(...).with_structured_output(ExtractedAnalysis,
    include_raw=True)`, and by any fake test double exposing the same
    invoke() -> {"raw", "parsed", "parsing_error"} shape.
    """

    def invoke(self, input: Sequence[BaseMessage]) -> dict[str, Any]: ...


class _InvalidAnalysis(Exception):
    """Internal signal that an attempt's output failed grounding or
    Phase 1 validation. Never escapes this module."""

    def __init__(self, problems: list[str]) -> None:
        super().__init__("; ".join(problems))
        self.problems = problems


@dataclass
class _AttemptOutcome:
    analysis: SourceAnalysis | None
    raw: AIMessage
    input_tokens: int
    output_tokens: int
    problems: list[str]


def _build_default_model(settings: Settings) -> StructuredOutputModel:
    chat = ChatOpenAI(
        model=settings.openai_model,
        reasoning_effort=settings.openai_reasoning_effort,
        use_responses_api=True,
        api_key=SecretStr(settings.openai_api_key) if settings.openai_api_key else None,
    )
    return chat.with_structured_output(
        ExtractedAnalysis, method="json_schema", strict=True, include_raw=True
    )


def _check_size_limit(text: str, limit: int) -> None:
    if len(text) > limit:
        raise SourceTooLargeError(len(text), limit)


def _usage_from_raw(raw: AIMessage) -> tuple[int, int]:
    usage = raw.usage_metadata
    if not usage:
        raise SourceAnalysisExtractionError(
            "Model response did not include usage metadata; token usage cannot be reported."
        )
    return usage["input_tokens"], usage["output_tokens"]


def _detect_refusal(raw: AIMessage) -> str | None:
    """Best-effort detection of the Responses API's `refusal` signal.

    The exact field placement here is inferred from OpenAI's documented
    response shape, not confirmed against a real captured langchain-openai
    response, so both plausible locations are checked defensively.
    """
    refusal = raw.additional_kwargs.get("refusal")
    if refusal:
        return str(refusal)
    content = raw.content
    if isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "refusal":
                return str(block.get("refusal") or block.get("text") or "refused")
    return None


def _detect_incomplete(raw: AIMessage) -> str | None:
    """Best-effort detection of the Responses API's incomplete-generation
    signal (status="incomplete"), for the same reason as _detect_refusal."""
    metadata = raw.response_metadata or {}
    if metadata.get("status") == "incomplete":
        details = metadata.get("incomplete_details") or {}
        reason = details.get("reason")
        return str(reason) if reason else "incomplete"
    return None


def _assemble_analysis(
    extracted: ExtractedAnalysis, provenance: Provenance, source_text: str
) -> SourceAnalysis:
    problems = find_ungrounded_verbatim_evidence(extracted.central_claims, source_text)
    problems += find_unverifiable_citations(extracted.central_claims, source_text)
    if problems:
        raise _InvalidAnalysis(problems)
    try:
        claims = [
            Claim(
                text=claim.text,
                statement_origin=claim.statement_origin,
                support_assessment=claim.support_assessment,
                evidence=[
                    Evidence(
                        text=evidence.text,
                        locator=evidence.locator,
                        citations=evidence.citations,
                        evidence_form=evidence.evidence_form,
                        relationship_to_claim=evidence.relationship_to_claim,
                    )
                    for evidence in claim.evidence
                ],
            )
            for claim in extracted.central_claims
        ]
        return SourceAnalysis(
            provenance=provenance,
            research_problem=extracted.research_problem,
            central_claims=claims,
            methodology=extracted.methodology,
            assumptions=extracted.assumptions,
            limitations=extracted.limitations,
            proposed_solutions=extracted.proposed_solutions,
            open_questions=extracted.open_questions,
        )
    except ValidationError as exc:
        raise _InvalidAnalysis([str(exc)]) from exc


def _evaluate_attempt(
    model: StructuredOutputModel,
    messages: list[BaseMessage],
    provenance: Provenance,
    source_text: str,
    model_name: str,
) -> _AttemptOutcome:
    try:
        result = model.invoke(messages)
    except SourceAnalysisError:
        raise
    except Exception as exc:
        raise SourceAnalysisExtractionError(f"Model call failed: {exc}") from exc

    raw = result["raw"]
    if not isinstance(raw, AIMessage):
        raise SourceAnalysisExtractionError("Model call did not return an AIMessage.")

    input_tokens, output_tokens = _usage_from_raw(raw)

    refusal = _detect_refusal(raw)
    if refusal is not None:
        raise SourceAnalysisRefusedError(
            refusal, model=model_name, input_tokens=input_tokens, output_tokens=output_tokens
        )

    incomplete = _detect_incomplete(raw)
    if incomplete is not None:
        raise SourceAnalysisIncompleteError(
            incomplete, model=model_name, input_tokens=input_tokens, output_tokens=output_tokens
        )

    parsed = result.get("parsed")
    parsing_error = result.get("parsing_error")
    if parsed is None or parsing_error is not None:
        reason = (
            str(parsing_error)
            if parsing_error
            else "Model output did not match the required schema."
        )
        return _AttemptOutcome(None, raw, input_tokens, output_tokens, [reason])

    try:
        analysis = _assemble_analysis(parsed, provenance, source_text)
    except _InvalidAnalysis as exc:
        return _AttemptOutcome(None, raw, input_tokens, output_tokens, exc.problems)

    return _AttemptOutcome(analysis, raw, input_tokens, output_tokens, [])


def analyze_source(
    source: SourceDocument,
    *,
    model: StructuredOutputModel | None = None,
    settings: Settings | None = None,
) -> AnalysisResult:
    settings = settings or Settings()
    _check_size_limit(source.text, settings.max_source_characters)

    runnable = model or _build_default_model(settings)
    messages = build_messages(source)

    first = _evaluate_attempt(
        runnable, messages, source.provenance, source.text, settings.openai_model
    )
    if first.analysis is not None:
        return AnalysisResult(
            analysis=first.analysis,
            model=settings.openai_model,
            input_tokens=first.input_tokens,
            output_tokens=first.output_tokens,
            attempt_count=1,
        )

    correction_messages = build_correction_messages(messages, first.raw, first.problems)
    second = _evaluate_attempt(
        runnable, correction_messages, source.provenance, source.text, settings.openai_model
    )
    total_input = first.input_tokens + second.input_tokens
    total_output = first.output_tokens + second.output_tokens

    if second.analysis is not None:
        return AnalysisResult(
            analysis=second.analysis,
            model=settings.openai_model,
            input_tokens=total_input,
            output_tokens=total_output,
            attempt_count=2,
        )

    raise SourceAnalysisValidationError(
        second.problems,
        model=settings.openai_model,
        input_tokens=total_input,
        output_tokens=total_output,
        attempt_count=2,
    )
