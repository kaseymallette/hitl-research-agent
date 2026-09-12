import pytest
from pydantic import ValidationError

from hitl_research_agent.models.methodology import Methodology


def test_methodology_requires_non_empty_summary() -> None:
    with pytest.raises(ValidationError):
        Methodology(summary="   ", statement_origin="author_stated")


def test_methodology_requires_valid_statement_origin() -> None:
    with pytest.raises(ValidationError):
        Methodology(summary="Summary", statement_origin="not_a_valid_value")


def test_methodology_list_defaults_are_independent() -> None:
    a = Methodology(summary="Summary A", statement_origin="author_stated")
    b = Methodology(summary="Summary B", statement_origin="author_stated")
    a.data_sources.append("Dataset A")
    a.analysis_methods.append("Regression")
    assert b.data_sources == []
    assert b.analysis_methods == []


def test_methodology_full_construction() -> None:
    m = Methodology(
        summary="Mixed-methods study of X.",
        study_design="Longitudinal cohort",
        data_sources=["Survey responses", "Administrative records"],
        sample_or_scope="1,200 participants over 5 years",
        analysis_methods=["Regression", "Thematic coding"],
        statement_origin="author_stated",
    )
    assert m.study_design == "Longitudinal cohort"
