class SourceAnalysisError(Exception):
    """Base class for every Phase 2 single-source analysis failure."""


class SourceTooLargeError(SourceAnalysisError):
    """The source text exceeds the configured character limit.

    Raised before any model call — Phase 2 never truncates or chunks a
    source.
    """

    def __init__(self, character_count: int, limit: int) -> None:
        super().__init__(
            f"Source text is {character_count} characters, which exceeds the "
            f"configured limit of {limit} characters."
        )
        self.character_count = character_count
        self.limit = limit


class SourceAnalysisExtractionError(SourceAnalysisError):
    """A technical/transport-level failure: network error, timeout, rate
    limit, server error, or a returned response with no usable usage data.

    No response was reliably received, so there is no usage to report and
    no AnalysisResult is produced.
    """


class SourceAnalysisRefusedError(SourceAnalysisError):
    """The model declined to analyze the source.

    A response was returned (usage is known), but there is no partial
    analysis to give corrective feedback on, so this does not consume the
    one correction attempt.
    """

    def __init__(self, reason: str, *, model: str, input_tokens: int, output_tokens: int) -> None:
        super().__init__(f"Model refused to analyze the source: {reason}")
        self.reason = reason
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens


class SourceAnalysisIncompleteError(SourceAnalysisError):
    """Generation stopped before completion (e.g. max_output_tokens reached).

    A response was returned (usage is known), but retrying identically is
    unlikely to help — this points at output-budget configuration, not
    content that a correction attempt could fix.
    """

    def __init__(self, reason: str, *, model: str, input_tokens: int, output_tokens: int) -> None:
        super().__init__(f"Generation stopped before completion: {reason}")
        self.reason = reason
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens


class SourceAnalysisValidationError(SourceAnalysisError):
    """The model's analysis remained invalid after the one correction attempt.

    Usage is accumulated across both attempts.
    """

    def __init__(
        self,
        problems: list[str],
        *,
        model: str,
        input_tokens: int,
        output_tokens: int,
        attempt_count: int,
    ) -> None:
        joined = "; ".join(problems)
        super().__init__(f"Analysis remained invalid after {attempt_count} attempt(s): {joined}")
        self.problems = problems
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.attempt_count = attempt_count
