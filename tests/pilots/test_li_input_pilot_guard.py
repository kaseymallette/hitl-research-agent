"""The pilot's request accounting and spending guard. All offline.

These cover the two ways the guard could be wrong about money: forgetting a
request that was made but produced no analysis, and treating a request whose
usage could not be read as free.
"""

import importlib.util
import json
from pathlib import Path
from typing import Any

import pytest
from langchain_openai import ChatOpenAI

from hitl_research_agent.config import Settings
from hitl_research_agent.extraction.pipeline import _build_default_model

REPO_ROOT = Path(__file__).resolve().parents[2]


def _client_max_retries(settings: Settings) -> int:
    """The retry count the OpenAI client is actually built with."""
    runnable = _build_default_model(settings)
    chat = runnable.steps[0].steps__["raw"].bound
    assert isinstance(chat, ChatOpenAI)
    return int(chat.root_client.max_retries)


def _load_pilot() -> Any:
    spec = importlib.util.spec_from_file_location(
        "li_input_pilot", REPO_ROOT / "scripts/run_li_input_pilot.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def pilot(tmp_path: Path) -> Any:
    module = _load_pilot()
    module.PILOT_ROOT = tmp_path / "li_input_format"
    return module


def _args(pilot: Any, **overrides: Any) -> Any:
    """CLI arguments as the parser would supply them, but with out_root=None so
    the fixture's temporary PILOT_ROOT survives."""
    defaults = {
        "path": "pdf",
        "cap_usd": 2.0,
        "confirm_paid": True,
        "model": pilot.PILOT_MODEL,
        "effort": pilot.PILOT_REASONING_EFFORT,
        "max_output_tokens": pilot.PILOT_MAX_OUTPUT_TOKENS,
        "grounding": "prepared",
        "out_root": None,
    }
    defaults.update(overrides)
    return pilot.argparse.Namespace(**defaults)


def _write_run(pilot: Any, path: str, stamp: str, record: dict[str, Any]) -> Path:
    directory = pilot.PILOT_ROOT / path / "runs" / stamp
    directory.mkdir(parents=True)
    (directory / "run_record.json").write_text(json.dumps(record))
    return directory


def _record(cost: float, *, usage_complete: bool = True) -> dict[str, Any]:
    return {
        "calculated_cost": {"total_usd": cost},
        "usage_accounting": {
            "usage_complete": usage_complete,
            "attempts_missing_usage": [] if usage_complete else [{"attempt_number": 1}],
        },
    }


# --- client retries ---------------------------------------------------------


def test_ordinary_settings_leave_the_client_default_retries_untouched() -> None:
    assert Settings().openai_max_retries is None
    assert _client_max_retries(Settings(openai_api_key="sk-test")) == 2


def test_the_pilot_disables_client_retries(pilot: Any) -> None:
    assert pilot.PILOT_MAX_RETRIES == 0
    settings = Settings(openai_api_key="sk-test", openai_max_retries=pilot.PILOT_MAX_RETRIES)
    assert _client_max_retries(settings) == 0


# --- the guard counts every request that was made ---------------------------


def test_a_failed_invocation_with_usage_still_counts(pilot: Any) -> None:
    _write_run(pilot, "pdf", "20261015T120000Z", _record(0.41))
    total, blockers = pilot.spent_so_far()
    assert total == pytest.approx(0.41)
    assert blockers == []


def test_costs_accumulate_across_invocations_and_paths(pilot: Any) -> None:
    _write_run(pilot, "pdf", "20261015T120000Z", _record(0.41))
    _write_run(pilot, "pdf", "20261015T130000Z", _record(0.52))
    _write_run(pilot, "crops", "20261015T140000Z", _record(0.33))
    total, blockers = pilot.spent_so_far()
    assert total == pytest.approx(1.26)
    assert blockers == []
    assert len(pilot.recorded_runs()) == 3


def test_a_later_invocation_does_not_overwrite_an_earlier_record(pilot: Any) -> None:
    first = pilot.invocation_dir("pdf")
    (first / "run_record.json").write_text(json.dumps(_record(0.41)))
    second = pilot.invocation_dir("pdf")
    assert second != first
    assert (first / "run_record.json").exists()
    total, _ = pilot.spent_so_far()
    assert total == pytest.approx(0.41)


# --- unknown usage is never free --------------------------------------------


def test_unreadable_usage_blocks_further_paid_runs(pilot: Any) -> None:
    _write_run(pilot, "pdf", "20261015T120000Z", _record(0.0, usage_complete=False))
    total, blockers = pilot.spent_so_far()
    assert total == pytest.approx(0.0)
    assert len(blockers) == 1
    assert "unknown rather than zero" in blockers[0]


def test_a_record_without_a_calculated_cost_blocks_too(pilot: Any) -> None:
    _write_run(pilot, "crops", "20261015T120000Z", {"usage_accounting": {"usage_complete": True}})
    _total, blockers = pilot.spent_so_far()
    assert any("no calculated cost" in blocker for blocker in blockers)


def test_run_refuses_while_a_blocker_stands(pilot: Any, capsys: Any) -> None:
    _write_run(pilot, "pdf", "20261015T120000Z", _record(0.0, usage_complete=False))
    args = _args(pilot, path="crops", cap_usd=2.0)
    assert pilot.cmd_run(args) == 5
    assert "cannot account for" in capsys.readouterr().err
    assert not list(pilot.PILOT_ROOT.glob("crops/runs/*"))


def test_recorded_cost_plus_the_worst_case_is_measured_against_the_cap(pilot: Any) -> None:
    _write_run(pilot, "pdf", "20261015T120000Z", _record(1.80))
    already, blockers = pilot.spent_so_far()
    assert blockers == []
    assert pilot.over_cap(already, 0.60, 2.00)
    assert not pilot.over_cap(already, 0.10, 2.00)


# --- the signal the record keys off is real pipeline behavior ---------------


def test_a_response_without_usage_leaves_an_attempt_the_record_flags() -> None:
    """The guard's "unknown, not zero" case, as the pipeline actually reports it."""
    from datetime import UTC, datetime

    from langchain_core.messages import AIMessage

    from hitl_research_agent.extraction.errors import SourceAnalysisExtractionError
    from hitl_research_agent.extraction.pipeline import analyze_source
    from hitl_research_agent.extraction.schemas import SourceDocument
    from hitl_research_agent.models.provenance import Provenance

    class NoUsageModel:
        def invoke(self, input: Any) -> dict[str, Any]:
            return {
                "raw": AIMessage(content="a response arrived", usage_metadata=None),
                "parsed": None,
                "parsing_error": None,
            }

    source = SourceDocument(
        text="Data centers use water for cooling.",
        provenance=Provenance(
            source_title="Fixture",
            source_type="peer_reviewed_paper",
            retrieved_at=datetime.now(UTC),
        ),
    )
    with pytest.raises(SourceAnalysisExtractionError) as failure:
        analyze_source(source, model=NoUsageModel(), settings=Settings(openai_api_key="sk-test"))
    attempts = failure.value.attempts
    assert len(attempts) == 1
    assert attempts[0].usage is None
    assert attempts[0].raw_content is not None  # a request was made and answered
