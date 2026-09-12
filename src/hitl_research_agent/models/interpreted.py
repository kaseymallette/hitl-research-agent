from typing import Literal

from pydantic import Field

from ._base import STATEMENT_ORIGIN_DESCRIPTION, NonEmptyStr, ResearchBaseModel


class InterpretedStatement(ResearchBaseModel):
    text: NonEmptyStr
    statement_origin: Literal["author_stated", "model_inferred"] = Field(
        description=STATEMENT_ORIGIN_DESCRIPTION
    )


class ResearchProblem(InterpretedStatement):
    pass


class Assumption(InterpretedStatement):
    pass


class Limitation(InterpretedStatement):
    pass


class ProposedSolution(InterpretedStatement):
    pass


class OpenQuestion(InterpretedStatement):
    pass
