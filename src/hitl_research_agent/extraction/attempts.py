"""Per-attempt records: what every returned model response contained and cost.

One `AttemptRecord` is kept for each model call, on success and on terminal
failure, so a run can be audited afterwards. Usage is exactly what the response
reported; nothing is fabricated for a call that returned no response.
"""

from typing import Literal

from pydantic import AwareDatetime, Field, JsonValue

from ..models._base import ResearchBaseModel

AttemptOutcome = Literal[
    "valid",
    "invalid_analysis",
    "parse_error",
    "refused",
    "incomplete",
    "technical_failure",
]

# Only these response-metadata keys are stored; anything else (headers, keys,
# request bodies) is never copied.
ALLOWED_RESPONSE_METADATA = (
    "id",
    "model",
    "model_name",
    "object",
    "status",
    "service_tier",
    "incomplete_details",
)


class AttemptUsage(ResearchBaseModel):
    """Token usage as reported for one response. `reasoning_tokens` is a subset
    of `output_tokens` and must never be added to it."""

    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    reasoning_tokens: int | None = Field(default=None, ge=0)
    cached_input_tokens: int | None = Field(default=None, ge=0)
    cache_creation_input_tokens: int | None = Field(default=None, ge=0)


class AttemptRecord(ResearchBaseModel):
    attempt_number: int = Field(ge=1)
    outcome: AttemptOutcome
    problems: list[str] = Field(default_factory=list)
    error: str | None = None
    request_id: str | None = Field(
        default=None, description="The response identifier the API returned, if any."
    )
    response_metadata: dict[str, JsonValue] = Field(default_factory=dict)
    raw_content: JsonValue = None
    parsed_output: dict[str, JsonValue] | None = None
    started_at: AwareDatetime
    ended_at: AwareDatetime
    elapsed_seconds: float = Field(ge=0)
    usage: AttemptUsage | None = None
