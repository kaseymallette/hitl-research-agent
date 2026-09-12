from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints

NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class ResearchBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


STATEMENT_ORIGIN_DESCRIPTION = (
    "Whether this statement is explicitly made by the source "
    "(author_stated) or synthesized by the model as an interpretation "
    "not explicitly stated in the source text (model_inferred)."
)
