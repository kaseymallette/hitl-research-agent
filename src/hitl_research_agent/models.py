"""The research data model: what an analysis is.

Two layers, kept apart on purpose:

* `ExtractedAnalysis` is what the model produces: a close reading, recorded as
  a reading path through the document. Every field in it is content the model
  is allowed to supply.
* `SourceAnalysis` wraps that content with the three things the application
  owns and a model has no legitimate value for: an identifier, the source's
  provenance, and when the analysis was made.

Within the close reading, what the author says and what the model reads into it
are kept apart by where they sit: claims and their support are the author's,
recorded as verbatim or paraphrased; a step's moves and meaning are the model's
reading. A claim marked verbatim is the model's assertion that the source says
this, not a verification of it.
"""

from datetime import UTC, date, datetime
from typing import Annotated, Literal
from uuid import UUID, uuid4, uuid5

from pydantic import (
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    model_validator,
)

from .inputs import InputMode, find_annotations, reserved_character_problems

NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class ResearchBaseModel(BaseModel):
    """Rejects unknown fields, so a model inventing one fails loudly."""

    model_config = ConfigDict(extra="forbid")


# --------------------------------------------------------------------------- source identity

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


# Fixed for the life of the project: changing it changes every source's id.
SOURCE_ID_NAMESPACE = UUID("900c49b2-1de2-43bd-9483-a29096029beb")


def source_id_for(slug: str) -> UUID:
    """The source's stable identifier, derived from its slug, so every analysis
    of one source carries the same `source_id` without the id being stored."""
    return uuid5(SOURCE_ID_NAMESPACE, slug)


class Provenance(ResearchBaseModel):
    """Application-supplied facts about the source. Never model-generated."""

    source_id: UUID = Field(
        default_factory=uuid4,
        description=(
            "Identifies the source itself, independent of any analysis of it. "
            "Reuse it when the same source is reanalyzed, so analyses of one "
            "source can be recognized as such."
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
        description="When the source was retrieved. Set by the caller, never by the model."
    )


# --------------------------------------------------------------------------- model content


class Citation(ResearchBaseModel):
    """A work the analyzed source cites, as the source prints it.

    Extracted from the document and not independently verified: no cited work
    is retrieved and no claim in it is checked.
    """

    citation_text: NonEmptyStr = Field(
        description=(
            "The in-text marker exactly as it appears (e.g. 'Harrison Dupre, 2025', "
            "or a grouped numeric marker such as '23,32,33'). One Citation records "
            "one cited work: when a marker groups several works, record a separate "
            "Citation for each, each carrying the marker as printed."
        )
    )
    reference_entry: NonEmptyStr | None = Field(
        default=None,
        description=(
            "Exactly one entry copied as written from the source's reference list, "
            "if a matching entry is present — never several joined together. Left "
            "unset rather than invented when no matching entry can be found."
        ),
    )


Form = Literal["verbatim", "paraphrased"]
FORM_DESCRIPTION = (
    "Whether this text reproduces the source's exact wording (verbatim) or puts "
    "source content in other words (paraphrased)."
)


class Support(ResearchBaseModel):
    """Something the author offers in support of a claim: a figure, a study, an
    example. Only what the author offers, never the claim restated."""

    text: NonEmptyStr
    form: Form = Field(description=FORM_DESCRIPTION)
    citations: list[Citation] = Field(
        default_factory=list,
        description=(
            "Works the source cites for this support. A marker may sit next to the "
            "passage rather than inside it, so this is not required to be a "
            "substring of `text`."
        ),
    )


class Claim(ResearchBaseModel):
    """A claim the author makes, met along the reading path."""

    text: NonEmptyStr
    form: Form = Field(description=FORM_DESCRIPTION)
    support: list[Support] = Field(
        default_factory=list,
        description="What the author offers in support. Empty when the claim is asserted.",
    )


class ReadingStep(ResearchBaseModel):
    """One step of the close reading, in the order the document unfolds."""

    location: NonEmptyStr = Field(
        description="Where in the document this step is: page, section, or paragraph."
    )
    moves: NonEmptyStr = Field(
        description=(
            "The move or moves the author is making here, in the terms of argument: "
            "a premise, evidence, a definition, an inference, an assumption, a "
            "qualification, a conclusion, and so on."
        )
    )
    claims: list[Claim] = Field(
        default_factory=list,
        description="The claims stated at this step. A step can make none.",
    )
    meaning: NonEmptyStr = Field(
        description=(
            "What this step means in light of what came before: whether it follows "
            "from, builds on, qualifies, or departs from the earlier steps. The "
            "model's reading of the path, never something the source states."
        )
    )


class ExtractedAnalysis(ResearchBaseModel):
    """Exactly what the model is asked to return: the close reading.

    This is the schema sent to the API. It holds no identifier, no provenance,
    and no timestamp, so there is nothing application-owned for the model to
    invent a value for.
    """

    # First, so the model sets its pace before it starts the path.
    reading_plan: NonEmptyStr = Field(
        description=(
            "The first look: what kind of document this is, how densely it reads, "
            "and the pace chosen for the steps."
        )
    )
    reading_path: list[ReadingStep] = Field(default_factory=list)


class SourceAnalysis(ResearchBaseModel):
    """One analysis of one source: the model's content plus what we own."""

    id: UUID = Field(default_factory=uuid4)
    provenance: Provenance
    analyzed_at: AwareDatetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description=(
            "When this analysis was produced. Contrast Provenance.retrieved_at, "
            "which records when the source was retrieved."
        ),
    )
    content: ExtractedAnalysis


class ArgumentEvaluation(ResearchBaseModel):
    """What the model returns from the second call: its own judgment of the
    argument, read as its interpretation, never as what the source states."""

    evaluation: NonEmptyStr


class SourceArgumentEvaluation(ResearchBaseModel):
    """One argument evaluation, tied to the close reading it was given."""

    id: UUID = Field(default_factory=uuid4)
    analysis_id: UUID = Field(description="The SourceAnalysis this evaluation was given.")
    provenance: Provenance
    evaluated_at: AwareDatetime = Field(default_factory=lambda: datetime.now(UTC))
    content: ArgumentEvaluation


# --------------------------------------------------------------------------- analysis input

ANALYSIS_SCOPE = (
    "The model received prepared text only. Items in preparation_gaps were omitted or "
    "incompletely represented in that text, and their image content was not seen."
)

ANALYSIS_SCOPE_PDF = (
    "The model received the original source PDF, so nothing was withheld from it. Content "
    "it reports from a figure, table, or equation was read from a page image and is "
    "unverified until a human checks it against that page."
)

ANALYSIS_SCOPE_TEXT_AND_CROPS = (
    "The model received the prepared text plus one retained crop for each item in "
    "preparation_gaps. Content it reports from a crop was read from that image and is "
    "unverified until a human checks it against the original."
)

ANALYSIS_SCOPE_BY_INPUT_MODE: dict[InputMode, str] = {
    "prepared_text": ANALYSIS_SCOPE,
    "prepared_text_and_crops": ANALYSIS_SCOPE_TEXT_AND_CROPS,
    "pdf": ANALYSIS_SCOPE_PDF,
}


class PreparationGap(ResearchBaseModel):
    """One thing preparation could not represent faithfully in text.

    `image` is relative to the `preparation_directory` of whatever carries this
    gap, so a crop stays resolvable without absolute paths.
    """

    id: NonEmptyStr
    kind: NonEmptyStr  # figure | equation | table
    page: int = Field(ge=1)
    label: str | None = None
    image: str | None = None


class SourceDocument(ResearchBaseModel):
    """What `analyze_source()` needs to already be true of its input."""

    text: NonEmptyStr
    provenance: Provenance
    preparation_directory: str | None = Field(
        default=None,
        description="Repo-relative directory the text came from; crop paths resolve against it.",
    )
    preparation_gaps: list[PreparationGap] = Field(
        default_factory=list,
        description="What preparation could not represent in this text. Empty means none.",
    )

    @model_validator(mode="after")
    def _text_is_safe_and_gaps_match_it(self) -> "SourceDocument":
        """A result must never claim coverage its text does not have."""
        problems = reserved_character_problems(self.text)
        if problems:
            raise ValueError("; ".join(problems))
        in_text = {span.annotation_id for span in find_annotations(self.text)}
        declared = {gap.id for gap in self.preparation_gaps}
        if in_text - declared:
            raise ValueError(
                "the text contains preparation annotations with no matching entry in "
                f"preparation_gaps: {sorted(in_text - declared)}"
            )
        if declared - in_text:
            raise ValueError(
                f"preparation_gaps names items absent from the text: {sorted(declared - in_text)}"
            )
        if self.preparation_gaps and not self.preparation_directory:
            raise ValueError("preparation_gaps requires preparation_directory to resolve images")
        return self
