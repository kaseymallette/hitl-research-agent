from pydantic import Field

from ._base import NonEmptyStr, ResearchBaseModel

CITATION_DESCRIPTION = (
    "Records what the analyzed source itself cites — extracted from this "
    "document, not independently verified. No retrieval or fact-checking of "
    "the cited work occurs during single-source analysis."
)


class Citation(ResearchBaseModel):
    citation_text: NonEmptyStr = Field(
        description=(
            "The in-text citation marker exactly as it appears in the source "
            "(e.g. 'Harrison Dupre, 2025'). " + CITATION_DESCRIPTION
        )
    )
    reference_entry: NonEmptyStr | None = Field(
        default=None,
        description=(
            "The source's own corresponding entry from its reference list, if "
            "one can be located in the source text. Left unset rather than "
            "invented when no matching entry is present. " + CITATION_DESCRIPTION
        ),
    )
