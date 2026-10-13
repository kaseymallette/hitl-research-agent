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
            "(e.g. 'Harrison Dupre, 2025', or a grouped numeric marker such as "
            "'23,32,33'). One Citation records one cited work: when a single "
            "marker groups several works, record a separate Citation for each, "
            "each carrying the marker as printed. " + CITATION_DESCRIPTION
        )
    )
    reference_entry: NonEmptyStr | None = Field(
        default=None,
        description=(
            "Exactly one entry copied as written from the source's own reference "
            "list, if a matching entry can be located in the source text — never "
            "several entries joined together. Left unset rather than invented "
            "when no matching entry is present. " + CITATION_DESCRIPTION
        ),
    )
