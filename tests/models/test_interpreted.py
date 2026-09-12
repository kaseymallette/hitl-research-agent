import pytest
from pydantic import ValidationError

from hitl_research_agent.models.interpreted import (
    Assumption,
    InterpretedStatement,
    Limitation,
    OpenQuestion,
    ProposedSolution,
    ResearchProblem,
)

_SUBCLASSES: list[type[InterpretedStatement]] = [
    ResearchProblem,
    Assumption,
    Limitation,
    ProposedSolution,
    OpenQuestion,
]


@pytest.mark.parametrize("model_cls", _SUBCLASSES)
def test_interpreted_statement_rejects_empty_text(model_cls: type[InterpretedStatement]) -> None:
    with pytest.raises(ValidationError):
        model_cls(text="   ", statement_origin="author_stated")


@pytest.mark.parametrize("model_cls", _SUBCLASSES)
def test_interpreted_statement_rejects_invalid_origin(
    model_cls: type[InterpretedStatement],
) -> None:
    with pytest.raises(ValidationError):
        model_cls(text="valid", statement_origin="not_a_valid_value")


@pytest.mark.parametrize("model_cls", _SUBCLASSES)
def test_interpreted_statement_valid_construction(
    model_cls: type[InterpretedStatement],
) -> None:
    instance = model_cls(text="valid", statement_origin="model_inferred")
    assert instance.text == "valid"
