from typing import Literal

from pydantic import Field

from ._base import STATEMENT_ORIGIN_DESCRIPTION, NonEmptyStr, ResearchBaseModel


class Methodology(ResearchBaseModel):
    summary: NonEmptyStr
    study_design: NonEmptyStr | None = None
    data_sources: list[NonEmptyStr] = Field(default_factory=list)
    sample_or_scope: NonEmptyStr | None = None
    analysis_methods: list[NonEmptyStr] = Field(default_factory=list)
    statement_origin: Literal["author_stated", "model_inferred"] = Field(
        description=STATEMENT_ORIGIN_DESCRIPTION
    )
