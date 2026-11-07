"""Calculated cost, from the usage a response actually reported.

Calculated cost is not billing. It is the documented rate multiplied by the
tokens the API said it used, which is the number the A/B comparison needs; what
the invoice says is a separate fact and is not recorded here.
"""

from dataclasses import dataclass

RATE_SOURCE = "OpenAI model pages, read 2026-10-15"


@dataclass(frozen=True)
class Rates:
    """USD per million tokens."""

    input: float
    output: float
    cached_input: float


RATES_BY_MODEL: dict[str, Rates] = {
    "gpt-6.1-sol": Rates(input=2.00, output=10.00, cached_input=0.10),
    "gpt-6-astra": Rates(input=10.00, output=50.00, cached_input=1.00),
}


def calculated_cost(
    model: str,
    *,
    input_tokens: int,
    output_tokens: int,
    cached_input_tokens: int = 0,
) -> dict[str, object]:
    """Cost for one run, with the arithmetic shown.

    Cached input tokens are billed at the cached rate and are a subset of
    `input_tokens`, so they are subtracted out before the full-rate charge.
    Raises for a model with no recorded rate rather than guessing one.
    """
    if model not in RATES_BY_MODEL:
        raise ValueError(f"no documented rates recorded for {model}; refusing to estimate")
    rates = RATES_BY_MODEL[model]
    full_input = max(input_tokens - cached_input_tokens, 0)
    input_usd = full_input / 1_000_000 * rates.input
    cached_usd = cached_input_tokens / 1_000_000 * rates.cached_input
    output_usd = output_tokens / 1_000_000 * rates.output
    return {
        "model": model,
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_input_tokens,
        "output_tokens": output_tokens,
        "input_usd": round(input_usd, 6),
        "cached_input_usd": round(cached_usd, 6),
        "output_usd": round(output_usd, 6),
        "total_usd": round(input_usd + cached_usd + output_usd, 6),
        "rates_usd_per_mtok": {
            "input": rates.input,
            "output": rates.output,
            "cached_input": rates.cached_input,
        },
        "rate_source": RATE_SOURCE,
        "note": "calculated from reported usage; not confirmed billing",
    }
