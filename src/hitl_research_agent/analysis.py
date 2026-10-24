"""The single-source analysis call path: article plus prompt, to model, to JSON.

Two calls, each with one correction attempt if the model's output does not fit
its schema: `analyze_source()` makes the close reading, and
`evaluate_argument()` gives the model the article and that close reading and
asks for its own judgment of the argument (ADR-0012). An analysis is returned
whenever the output can be read, however thin or heavily paraphrased it is.
Only a technical failure stops a run: a transport error, a refusal, a
generation that stopped early, or output that still will not parse after the
correction. Whether a returned analysis is any good is an evaluation question,
answered elsewhere.
"""

import json
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Literal, Protocol

from langchain_core.messages import AIMessage, BaseMessage
from langchain_openai import ChatOpenAI
from pydantic import AwareDatetime, Field, JsonValue, SecretStr, ValidationError

from .config import Settings
from .inputs import Attachment, InputMode, LoadedAttachment, validate_attachments
from .models import (
    ANALYSIS_SCOPE,
    ANALYSIS_SCOPE_BY_INPUT_MODE,
    ArgumentEvaluation,
    ExtractedAnalysis,
    NonEmptyStr,
    PreparationGap,
    Primer,
    ResearchBaseModel,
    SourceAnalysis,
    SourceDocument,
)
from .prompts import (
    build_correction_messages,
    build_evaluation_messages,
    build_messages,
    build_primer_messages,
)

AttemptOutcome = Literal[
    "valid",
    "invalid_analysis",
    "parse_error",
    "refused",
    "incomplete",
    "technical_failure",
]

FailureKind = Literal[
    "source_too_large",
    "transport",
    "refused",
    "incomplete",
    "invalid_after_correction",
]


class AnalysisError(Exception):
    """A run that produced no analysis.

    `kind` says which failure it was; `attempts` holds a record of every model
    call made before it, empty when the failure preceded any call. Usage is
    whatever the responses reported and zero when no response arrived — never a
    fabricated stand-in.
    """

    def __init__(
        self,
        message: str,
        *,
        kind: FailureKind,
        model: str | None = None,
        input_tokens: int = 0,
        output_tokens: int = 0,
        problems: Sequence[str] = (),
    ) -> None:
        super().__init__(message)
        self.kind = kind
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.problems = list(problems)
        self.attempts: list[AttemptRecord] = []


class AttemptUsage(ResearchBaseModel):
    """Token usage as reported for one response. `reasoning_tokens` is a subset
    of `output_tokens` and must never be added to it."""

    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    reasoning_tokens: int | None = Field(default=None, ge=0)
    cached_input_tokens: int | None = Field(default=None, ge=0)
    cache_creation_input_tokens: int | None = Field(default=None, ge=0)


class AttemptRecord(ResearchBaseModel):
    """One model call, kept whether it succeeded or failed."""

    attempt_number: int = Field(ge=1)
    outcome: AttemptOutcome
    problems: list[str] = Field(default_factory=list)
    error: str | None = None
    request_id: str | None = None
    started_at: AwareDatetime
    ended_at: AwareDatetime
    elapsed_seconds: float = Field(ge=0)
    usage: AttemptUsage | None = None
    parsed_output: dict[str, JsonValue] | None = None


class AnalysisResult(ResearchBaseModel):
    """What `analyze_source()` returns: the analysis plus the facts of the run.

    `input_tokens` / `output_tokens` are the exact sum over every call counted
    in `attempt_count`.
    """

    analysis: SourceAnalysis
    analysis_scope: NonEmptyStr = Field(default=ANALYSIS_SCOPE)
    input_mode: InputMode = "prepared_text"
    model_inputs: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Attachments sent, with the sha256 of the exact bytes.",
    )
    preparation_directory: str | None = None
    preparation_gaps: list[PreparationGap] = Field(default_factory=list)
    model: NonEmptyStr
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    attempt_count: int = Field(ge=1, le=2)
    attempts: list[AttemptRecord] = Field(default_factory=list)


class ArgumentEvaluationResult(ResearchBaseModel):
    """What `evaluate_argument()` returns: the evaluation plus the facts of the
    call, with the same accounting as `AnalysisResult`."""

    evaluation: ArgumentEvaluation
    model: NonEmptyStr
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    attempt_count: int = Field(ge=1, le=2)
    attempts: list[AttemptRecord] = Field(default_factory=list)


class PrimerResult(ResearchBaseModel):
    """What `write_primer()` returns: the primer plus the facts of the call."""

    primer: Primer
    model: NonEmptyStr
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    attempt_count: int = Field(ge=1, le=2)
    attempts: list[AttemptRecord] = Field(default_factory=list)


class StructuredOutputModel(Protocol):
    """The minimal interface this module depends on.

    Satisfied by `ChatOpenAI(...).with_structured_output(ExtractedAnalysis,
    include_raw=True)`, and by any test double with the same
    invoke() -> {"raw", "parsed", "parsing_error"} shape.
    """

    def invoke(self, input: Sequence[BaseMessage]) -> dict[str, Any]: ...


@dataclass
class _Attempt[Content: ResearchBaseModel]:
    """One evaluated call: the content if it was usable, and what it cost."""

    content: Content | None
    raw: AIMessage
    input_tokens: int
    output_tokens: int
    problems: list[str]


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _usage(raw: AIMessage) -> AttemptUsage | None:
    reported = raw.usage_metadata
    if not reported:
        return None
    output_details: dict[str, Any] = dict(reported.get("output_token_details") or {})
    input_details: dict[str, Any] = dict(reported.get("input_token_details") or {})
    return AttemptUsage(
        input_tokens=reported["input_tokens"],
        output_tokens=reported["output_tokens"],
        reasoning_tokens=output_details.get("reasoning"),
        cached_input_tokens=input_details.get("cache_read"),
        cache_creation_input_tokens=input_details.get("cache_creation"),
    )


def _record(
    *,
    number: int,
    outcome: AttemptOutcome,
    started: datetime,
    ended: datetime,
    raw: AIMessage | None = None,
    problems: Sequence[str] = (),
    error: str | None = None,
    parsed: object = None,
) -> AttemptRecord:
    parsed_output = None
    if isinstance(parsed, ResearchBaseModel):
        parsed_output = json.loads(parsed.model_dump_json())
    request_id = None
    if raw is not None:
        request_id = raw.id or (raw.response_metadata or {}).get("id")
    return AttemptRecord(
        attempt_number=number,
        outcome=outcome,
        problems=list(problems),
        error=error,
        request_id=str(request_id) if request_id else None,
        started_at=started,
        ended_at=ended,
        elapsed_seconds=max((ended - started).total_seconds(), 0.0),
        usage=_usage(raw) if raw is not None else None,
        parsed_output=parsed_output,
    )


def _build_default_model(
    settings: Settings, schema: type[ResearchBaseModel] = ExtractedAnalysis
) -> StructuredOutputModel:
    chat = ChatOpenAI(
        model=settings.openai_model,
        reasoning_effort=settings.openai_reasoning_effort,
        use_responses_api=True,
        max_completion_tokens=settings.max_output_tokens,
        max_retries=settings.openai_max_retries,
        api_key=SecretStr(settings.openai_api_key) if settings.openai_api_key else None,
    )
    return chat.with_structured_output(schema, method="json_schema", strict=True, include_raw=True)


def _detect_refusal(raw: AIMessage) -> str | None:
    """The Responses API's `refusal` signal.

    Both documented placements are checked: one live run has been observed, but
    not a live refusal, so neither location is confirmed redundant.
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
    """The Responses API's incomplete-generation signal."""
    metadata = raw.response_metadata or {}
    if metadata.get("status") == "incomplete":
        reason = (metadata.get("incomplete_details") or {}).get("reason")
        return str(reason) if reason else "incomplete"
    return None


def _evaluate[Content: ResearchBaseModel](
    model: StructuredOutputModel,
    messages: list[BaseMessage],
    model_name: str,
    schema: type[Content],
    *,
    attempts: list[AttemptRecord],
    clock: Callable[[], datetime],
) -> _Attempt[Content]:
    """Run one call, append its record to `attempts` before raising anything,
    and classify what came back."""
    number = len(attempts) + 1
    started = clock()

    def fail(kind: FailureKind, message: str, raw: AIMessage | None = None) -> AnalysisError:
        attempts.append(
            _record(
                number=number,
                outcome="technical_failure",
                started=started,
                ended=clock(),
                raw=raw,
                error=message,
            )
        )
        return AnalysisError(message, kind=kind, model=model_name)

    try:
        result = model.invoke(messages)
    except Exception as exc:
        raise fail("transport", f"Model call failed: {exc}") from exc
    ended = clock()

    raw = result["raw"]
    if not isinstance(raw, AIMessage):
        raise fail("transport", "Model call did not return an AIMessage.")
    reported = raw.usage_metadata
    if not reported:
        raise fail(
            "transport",
            "Model response did not include usage metadata; token usage cannot be reported.",
            raw,
        )
    input_tokens, output_tokens = reported["input_tokens"], reported["output_tokens"]

    def stop(
        outcome: AttemptOutcome, kind: FailureKind, message: str, reason: str
    ) -> AnalysisError:
        """Record the response and fail: neither a refusal nor a truncated
        generation is something a correction attempt can fix."""
        attempts.append(
            _record(
                number=number,
                outcome=outcome,
                started=started,
                ended=ended,
                raw=raw,
                problems=[reason],
            )
        )
        return AnalysisError(
            message,
            kind=kind,
            model=model_name,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            problems=[reason],
        )

    refusal = _detect_refusal(raw)
    if refusal is not None:
        raise stop("refused", "refused", f"Model refused to analyze the source: {refusal}", refusal)

    incomplete = _detect_incomplete(raw)
    if incomplete is not None:
        raise stop(
            "incomplete",
            "incomplete",
            f"Generation stopped before completion: {incomplete}",
            incomplete,
        )

    parsed = result.get("parsed")
    parsing_error = result.get("parsing_error")
    if parsed is None or parsing_error is not None:
        reason = str(parsing_error) if parsing_error else "Model output did not match the schema."
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
        return _Attempt(None, raw, input_tokens, output_tokens, [reason])

    try:
        content = schema.model_validate(parsed.model_dump())
    except ValidationError as exc:
        attempts.append(
            _record(
                number=number,
                outcome="invalid_analysis",
                started=started,
                ended=ended,
                raw=raw,
                problems=[str(exc)],
                parsed=parsed,
            )
        )
        return _Attempt(None, raw, input_tokens, output_tokens, [str(exc)])

    attempts.append(
        _record(
            number=number,
            outcome="valid",
            started=started,
            ended=ended,
            raw=raw,
            parsed=content,
        )
    )
    return _Attempt(content, raw, input_tokens, output_tokens, [])


def analyze_source(
    source: SourceDocument,
    *,
    model: StructuredOutputModel | None = None,
    settings: Settings | None = None,
    clock: Callable[[], datetime] | None = None,
    input_mode: InputMode = "prepared_text",
    attachments: Sequence[LoadedAttachment] = (),
) -> AnalysisResult:
    """Analyze one source in one of the three input modes.

    `input_mode` chooses what the model receives. The analysis prompt, output
    schema, and one-correction policy are identical in every mode, so input
    format stays the only intended difference between runs.
    """
    settings = settings or Settings()
    clock = clock or _utc_now
    validate_attachments(input_mode, attachments, [gap.id for gap in source.preparation_gaps])
    if len(source.text) > settings.max_source_characters:
        raise AnalysisError(
            f"Source text is {len(source.text)} characters, over the configured limit of "
            f"{settings.max_source_characters}.",
            kind="source_too_large",
        )

    attempts: list[AttemptRecord] = []
    try:
        return _run(source, model, settings, clock, attempts, input_mode, attachments)
    except AnalysisError as exc:
        exc.attempts = list(attempts)
        raise


def _run(
    source: SourceDocument,
    model: StructuredOutputModel | None,
    settings: Settings,
    clock: Callable[[], datetime],
    attempts: list[AttemptRecord],
    input_mode: InputMode,
    attachments: Sequence[LoadedAttachment],
) -> AnalysisResult:
    runnable = model or _build_default_model(settings)
    messages = build_messages(source, input_mode=input_mode, attachments=attachments)
    records: list[Attachment] = [item.record for item in attachments]

    def result(content: ExtractedAnalysis, input_tokens: int, output_tokens: int) -> AnalysisResult:
        return AnalysisResult(
            analysis=SourceAnalysis(provenance=source.provenance, content=content),
            analysis_scope=ANALYSIS_SCOPE_BY_INPUT_MODE[input_mode],
            input_mode=input_mode,
            model_inputs=[record.as_record() for record in records],
            preparation_directory=source.preparation_directory,
            preparation_gaps=list(source.preparation_gaps),
            model=settings.openai_model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            attempt_count=len(attempts),
            attempts=list(attempts),
        )

    content, input_tokens, output_tokens = _call_with_correction(
        runnable, messages, settings.openai_model, ExtractedAnalysis, attempts, clock
    )
    return result(content, input_tokens, output_tokens)


def _call_with_correction[Content: ResearchBaseModel](
    runnable: StructuredOutputModel,
    messages: list[BaseMessage],
    model_name: str,
    schema: type[Content],
    attempts: list[AttemptRecord],
    clock: Callable[[], datetime],
) -> tuple[Content, int, int]:
    """One call, and one correction attempt if its output does not fit the
    schema. Returns the content and the tokens of every call counted."""
    first = _evaluate(runnable, messages, model_name, schema, attempts=attempts, clock=clock)
    if first.content is not None:
        return first.content, first.input_tokens, first.output_tokens

    corrected = build_correction_messages(messages, first.raw, first.problems)
    second = _evaluate(runnable, corrected, model_name, schema, attempts=attempts, clock=clock)
    total_in = first.input_tokens + second.input_tokens
    total_out = first.output_tokens + second.output_tokens
    if second.content is not None:
        return second.content, total_in, total_out

    raise AnalysisError(
        f"Output remained invalid after 2 attempts: {'; '.join(second.problems)}",
        kind="invalid_after_correction",
        model=model_name,
        input_tokens=total_in,
        output_tokens=total_out,
        problems=second.problems,
    )


def evaluate_argument(
    source: SourceDocument,
    close_reading: ExtractedAnalysis,
    *,
    model: StructuredOutputModel | None = None,
    settings: Settings | None = None,
    clock: Callable[[], datetime] | None = None,
    input_mode: InputMode = "prepared_text",
    attachments: Sequence[LoadedAttachment] = (),
) -> ArgumentEvaluationResult:
    """The second call: the model's own evaluation of the argument, given the
    article in the same input mode as the close reading, and the close reading.

    A failure raises AnalysisError like the first call; the caller keeps the
    close reading either way.
    """
    settings = settings or Settings()
    clock = clock or _utc_now
    validate_attachments(input_mode, attachments, [gap.id for gap in source.preparation_gaps])
    attempts: list[AttemptRecord] = []
    try:
        runnable = model or _build_default_model(settings, ArgumentEvaluation)
        messages = build_evaluation_messages(
            source, close_reading, input_mode=input_mode, attachments=attachments
        )
        content, input_tokens, output_tokens = _call_with_correction(
            runnable, messages, settings.openai_model, ArgumentEvaluation, attempts, clock
        )
    except AnalysisError as exc:
        exc.attempts = list(attempts)
        raise
    return ArgumentEvaluationResult(
        evaluation=content,
        model=settings.openai_model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        attempt_count=len(attempts),
        attempts=list(attempts),
    )


def write_primer(
    source: SourceDocument,
    *,
    model: StructuredOutputModel | None = None,
    settings: Settings | None = None,
    clock: Callable[[], datetime] | None = None,
    input_mode: InputMode = "pdf",
    attachments: Sequence[LoadedAttachment] = (),
) -> PrimerResult:
    """Background on the article's field, for the researcher to read first.

    Separate from the analysis: its output is never given to the close reading
    or the argument evaluation (ADR-0016).
    """
    settings = settings or Settings()
    clock = clock or _utc_now
    validate_attachments(input_mode, attachments, [gap.id for gap in source.preparation_gaps])
    attempts: list[AttemptRecord] = []
    try:
        runnable = model or _build_default_model(settings, Primer)
        messages = build_primer_messages(source, input_mode=input_mode, attachments=attachments)
        content, input_tokens, output_tokens = _call_with_correction(
            runnable, messages, settings.openai_model, Primer, attempts, clock
        )
    except AnalysisError as exc:
        exc.attempts = list(attempts)
        raise
    return PrimerResult(
        primer=content,
        model=settings.openai_model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        attempt_count=len(attempts),
        attempts=list(attempts),
    )
