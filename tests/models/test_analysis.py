from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from hitl_research_agent.models.analysis import SourceAnalysis
from hitl_research_agent.models.claim import Claim, Evidence
from hitl_research_agent.models.interpreted import ResearchProblem
from hitl_research_agent.models.provenance import Provenance


def _minimal_source_analysis(**overrides: object) -> SourceAnalysis:
    defaults: dict[str, object] = dict(
        provenance=Provenance(
            source_title="T",
            source_type="peer_reviewed_paper",
            retrieved_at=datetime.now(UTC),
        ),
        research_problem=ResearchProblem(text="Problem", statement_origin="author_stated"),
        central_claims=[
            Claim(
                text="Claim",
                statement_origin="author_stated",
                evidence=[
                    Evidence(
                        text="quote",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
            )
        ],
    )
    defaults.update(overrides)
    return SourceAnalysis(**defaults)  # type: ignore[arg-type]


def test_methodology_may_be_absent() -> None:
    assert _minimal_source_analysis().methodology is None


def test_source_analysis_requires_at_least_one_central_claim() -> None:
    with pytest.raises(ValidationError):
        _minimal_source_analysis(central_claims=[])


def test_analyzed_at_defaults_to_aware_datetime() -> None:
    assert _minimal_source_analysis().analyzed_at.utcoffset() is not None


def test_analyzed_at_rejects_naive_datetime() -> None:
    with pytest.raises(ValidationError):
        _minimal_source_analysis(analyzed_at=datetime.now())


def test_source_analysis_ids_are_unique() -> None:
    a = _minimal_source_analysis()
    b = _minimal_source_analysis()
    assert a.id != b.id


def test_source_analysis_round_trips_with_research_problem() -> None:
    original = _minimal_source_analysis()
    assert isinstance(original.research_problem, ResearchProblem)

    restored = SourceAnalysis.model_validate_json(original.model_dump_json())

    assert restored == original
    assert isinstance(restored.research_problem, ResearchProblem)
