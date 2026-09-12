from datetime import date
from typing import Literal
from uuid import UUID, uuid4

from pydantic import AwareDatetime, Field, HttpUrl

from ._base import NonEmptyStr, ResearchBaseModel

SourceType = Literal[
    "peer_reviewed_paper",
    "preprint",
    "government_report",
    "government_policy",
    "research_institute_report",
    "technical_document",
    "industry_report",
    "news_article",
    "blog_post",
    "other",
]


class Provenance(ResearchBaseModel):
    source_id: UUID = Field(
        default_factory=uuid4,
        description=(
            "Identifies the underlying source itself, independent of any "
            "particular analysis of it. Reuse the same source_id when the "
            "same source is reanalyzed (e.g. on rerun or revision) so that "
            "multiple SourceAnalysis records can be recognized as analyses "
            "of the same source. Contrast with SourceAnalysis.id, which "
            "identifies one specific analysis result, not the source."
        ),
    )
    source_title: NonEmptyStr
    source_authors: list[NonEmptyStr] = Field(default_factory=list)
    publication_date: date | None = None
    source_type: SourceType
    doi: NonEmptyStr | None = None
    publisher: NonEmptyStr | None = None
    url: HttpUrl | None = None
    retrieved_at: AwareDatetime = Field(
        description=(
            "Application-supplied metadata recording when this source was "
            "actually retrieved for analysis. This is not model-generated "
            "content — it should be set by retrieval/ingestion code, never "
            "inferred or produced by an LLM."
        )
    )
