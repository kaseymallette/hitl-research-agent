"""Calculated cost, which the A/B comparison is partly decided on."""

import pytest

from hitl_research_agent.cost import RATES_BY_MODEL, calculated_cost


def test_cost_is_the_documented_rate_times_the_reported_usage() -> None:
    cost = calculated_cost("gpt-6.1-sol", input_tokens=1_000_000, output_tokens=1_000_000)
    assert cost["input_usd"] == 2.0
    assert cost["output_usd"] == 10.0
    assert cost["total_usd"] == 12.0


def test_cached_input_is_billed_at_the_cached_rate_and_not_twice() -> None:
    """Cached tokens are a subset of input_tokens, so charging both rates on
    the same tokens would overstate every cached run."""
    cost = calculated_cost(
        "gpt-6.1-sol", input_tokens=1_000_000, output_tokens=0, cached_input_tokens=400_000
    )
    assert cost["input_usd"] == pytest.approx(600_000 / 1_000_000 * 2.0)
    assert cost["cached_input_usd"] == pytest.approx(400_000 / 1_000_000 * 0.10)
    assert cost["total_usd"] == pytest.approx(1.24)


def test_astra_costs_five_times_sol_for_the_same_usage() -> None:
    """The comparison exists because of this gap; if the rates were equal there
    would be no cost question to answer."""
    usage = {"input_tokens": 50_000, "output_tokens": 20_000}
    sol = calculated_cost("gpt-6.1-sol", **usage)["total_usd"]
    astra = calculated_cost("gpt-6-astra", **usage)["total_usd"]
    assert isinstance(sol, float) and isinstance(astra, float)
    assert astra == pytest.approx(sol * 5)


def test_an_unknown_model_refuses_rather_than_guessing_a_rate() -> None:
    with pytest.raises(ValueError, match="no documented rates"):
        calculated_cost("gpt-7-nova", input_tokens=1, output_tokens=1)


def test_the_record_says_it_is_calculated_and_names_its_rate_source() -> None:
    """Calculated cost is not billing, and a saved record has to say so."""
    cost = calculated_cost("gpt-6-astra", input_tokens=10, output_tokens=10)
    assert "not confirmed billing" in str(cost["note"])
    assert "2026-10-15" in str(cost["rate_source"])
    assert cost["rates_usd_per_mtok"] == {
        "input": RATES_BY_MODEL["gpt-6-astra"].input,
        "output": RATES_BY_MODEL["gpt-6-astra"].output,
        "cached_input": RATES_BY_MODEL["gpt-6-astra"].cached_input,
    }
