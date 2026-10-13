import json
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Protocol

from langchain_core.messages import AIMessage, BaseMessage
from langchain_openai import ChatOpenAI
from pydantic import JsonValue, SecretStr, ValidationError

from ..config import Settings
from ..models.analysis import SourceAnalysis
from ..models.claim import Claim, Evidence
from ..models.provenance import Provenance
from .annotations import grounding_view
from .attempts import (
    ALLOWED_RESPONSE_METADATA,
    AttemptOutcome,
    AttemptRecord,
    AttemptUsage,
)
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


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _json_safe(value: object) -> JsonValue:
    """A JSON-safe copy of `value` (unserializable objects become strings)."""
    safe: JsonValue = json.loads(json.dumps(value, default=str))
    return safe


def _usage_details(raw: AIMessage) -> AttemptUsage | None:
    usage = raw.usage_metadata
    if not usage:
        return None
    output_details: dict[str, Any] = dict(usage.get("output_token_details") or {})
    input_details: dict[str, Any] = dict(usage.get("input_token_details") or {})
    return AttemptUsage(
        input_tokens=usage["input_tokens"],
        output_tokens=usage["output_tokens"],
        reasoning_tokens=output_details.get("reasoning"),
        cached_input_tokens=input_details.get("cache_read"),
        cache_creation_input_tokens=input_details.get("cache_creation"),
    )


def _allowed_metadata(raw: AIMessage) -> dict[str, JsonValue]:
    metadata = raw.response_metadata or {}
    return {key: _json_safe(metadata[key]) for key in ALLOWED_RESPONSE_METADATA if key in metadata}


def _record(
    *,
    number: int,
    outcome: AttemptOutcome,
    started: datetime,
    ended: datetime,
    raw: AIMessage | None = None,
    problems: list[str] | None = None,
    error: str | None = None,
    parsed: object = None,
) -> AttemptRecord:
    parsed_output: dict[str, JsonValue] | None = None
    if isinstance(parsed, ExtractedAnalysis):
        dumped = _json_safe(parsed.model_dump(mode="json"))
        parsed_output = dumped if isinstance(dumped, dict) else None
    metadata = _allowed_metadata(raw) if raw is not None else {}
    request_id = raw.id if raw is not None and raw.id else None
    if request_id is None and isinstance(metadata.get("id"), str):
        request_id = str(metadata["id"])
    return AttemptRecord(
        attempt_number=number,
        outcome=outcome,
        problems=problems or [],
        error=error,
        request_id=request_id,
        response_metadata=metadata,
        raw_content=_json_safe(raw.content) if raw is not None else None,
        parsed_output=parsed_output,
        started_at=started,
        ended_at=ended,
        elapsed_seconds=max((ended - started).total_seconds(), 0.0),
        usage=_usage_details(raw) if raw is not None else None,
    )


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
    grounding_text: str,
    model_name: str,
    *,
    attempts: list[AttemptRecord],
    clock: Callable[[], datetime],
) -> _AttemptOutcome:
    """Run one model call, append its AttemptRecord to `attempts` (before any
    error is raised), and classify the outcome."""
    number = len(attempts) + 1
    started = clock()
    try:
        result = model.invoke(messages)
    except SourceAnalysisError:
        raise
    except Exception as exc:
        attempts.append(
            _record(
                number=number,
                outcome="technical_failure",
                started=started,
                ended=clock(),
                error=f"{type(exc).__name__}: {exc}",
            )
        )
        raise SourceAnalysisExtractionError(f"Model call failed: {exc}") from exc
    ended = clock()

    raw = result["raw"]
    if not isinstance(raw, AIMessage):
        attempts.append(
            _record(
                number=number,
                outcome="technical_failure",
                started=started,
                ended=ended,
                error="Model call did not return an AIMessage.",
            )
        )
        raise SourceAnalysisExtractionError("Model call did not return an AIMessage.")

    try:
        input_tokens, output_tokens = _usage_from_raw(raw)
    except SourceAnalysisExtractionError as exc:
        attempts.append(
            _record(
                number=number,
                outcome="technical_failure",
                started=started,
                ended=ended,
                raw=raw,
                error=str(exc),
            )
        )
        raise

    refusal = _detect_refusal(raw)
    if refusal is not None:
        attempts.append(
            _record(
                number=number,
                outcome="refused",
                started=started,
                ended=ended,
                raw=raw,
                problems=[refusal],
            )
        )
        raise SourceAnalysisRefusedError(
            refusal, model=model_name, input_tokens=input_tokens, output_tokens=output_tokens
        )

    incomplete = _detect_incomplete(raw)
    if incomplete is not None:
        attempts.append(
            _record(
                number=number,
                outcome="incomplete",
                started=started,
                ended=ended,
                raw=raw,
                problems=[incomplete],
            )
        )
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
        attempts.append(
            _record(
                number=number,
                outcome="parse_error",
                started=started,
                ended=ended,
                raw=raw,
                problems=[reason],
                parsed=parsed,
            )
        )
        return _AttemptOutcome(None, raw, input_tokens, output_tokens, [reason])

    try:
        analysis = _assemble_analysis(parsed, provenance, grounding_text)
    except _InvalidAnalysis as exc:
        attempts.append(
            _record(
                number=number,
                outcome="invalid_analysis",
                started=started,
                ended=ended,
                raw=raw,
                problems=exc.problems,
                parsed=parsed,
            )
        )
        return _AttemptOutcome(None, raw, input_tokens, output_tokens, exc.problems)

    attempts.append(
        _record(
            number=number, outcome="valid", started=started, ended=ended, raw=raw, parsed=parsed
        )
    )
    return _AttemptOutcome(analysis, raw, input_tokens, output_tokens, [])


def analyze_source(
    source: SourceDocument,
    *,
    model: StructuredOutputModel | None = None,
    settings: Settings | None = None,
    clock: Callable[[], datetime] | None = None,
) -> AnalysisResult:
    settings = settings or Settings()
    clock = clock or _utc_now
    _check_size_limit(source.text, settings.max_source_characters)

    attempts: list[AttemptRecord] = []
    try:
        return _analyze(source, model, settings, clock, attempts)
    except SourceAnalysisError as exc:
        exc.attempts = list(attempts)
        raise


def _analyze(
    source: SourceDocument,
    model: StructuredOutputModel | None,
    settings: Settings,
    clock: Callable[[], datetime],
    attempts: list[AttemptRecord],
) -> AnalysisResult:
    runnable = model or _build_default_model(settings)
    messages = build_messages(source)
    # Grounding checks run against the source with preparation annotations
    # replaced by a sentinel, so an annotation can never match as source text.
    grounding_text = grounding_view(source.text)

    first = _evaluate_attempt(
        runnable,
        messages,
        source.provenance,
        grounding_text,
        settings.openai_model,
        attempts=attempts,
        clock=clock,
    )
    if first.analysis is not None:
        return AnalysisResult(
            analysis=first.analysis,
            preparation_directory=source.preparation_directory,
            preparation_gaps=list(source.preparation_gaps),
            model=settings.openai_model,
            input_tokens=first.input_tokens,
            output_tokens=first.output_tokens,
            attempt_count=1,
            attempts=list(attempts),
        )

    correction_messages = build_correction_messages(messages, first.raw, first.problems)
    second = _evaluate_attempt(
        runnable,
        correction_messages,
        source.provenance,
        grounding_text,
        settings.openai_model,
        attempts=attempts,
        clock=clock,
    )
    total_input = first.input_tokens + second.input_tokens
    total_output = first.output_tokens + second.output_tokens

    if second.analysis is not None:
        return AnalysisResult(
            analysis=second.analysis,
            preparation_directory=source.preparation_directory,
            preparation_gaps=list(source.preparation_gaps),
            model=settings.openai_model,
            input_tokens=total_input,
            output_tokens=total_output,
            attempt_count=2,
            attempts=list(attempts),
        )

    raise SourceAnalysisValidationError(
        second.problems,
        model=settings.openai_model,
        input_tokens=total_input,
        output_tokens=total_output,
        attempt_count=2,
    )
