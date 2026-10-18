"""The research data model: what an analysis is.

Two layers, kept apart on purpose:

* `ExtractedAnalysis` is what the model produces. Every field in it is content
  the model is allowed to supply.
* `SourceAnalysis` wraps that content with the three things the application
  owns and a model has no legitimate value for: an identifier, the source's
  provenance, and when the analysis was made.

Within the model's own content, `statement_origin` records whether the model is
reporting what the source says or offering its own interpretation. That label is
an attribution, not a verification of one: whether an `author_stated` claim is
really in the source is an evaluation question, answered outside this module.
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

STATEMENT_ORIGIN_DESCRIPTION = (
    "Whether this statement is explicitly made by the source (author_stated) "
    "or synthesized by the model as an interpretation not explicitly stated "
    "in the source text (model_inferred)."
)


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


class Statement(ResearchBaseModel):
    """One statement with its attribution.

    Used for the research problem, assumptions, limitations, proposed
    solutions, and open questions. These were five identical types; the field
    that distinguishes them is the list a statement appears in.
    """

    text: NonEmptyStr
    statement_origin: Literal["author_stated", "model_inferred"] = Field(
        description=STATEMENT_ORIGIN_DESCRIPTION
    )


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


class Evidence(ResearchBaseModel):
    """Source material offered in support of a claim."""

    text: NonEmptyStr
    locator: NonEmptyStr | None = None
    citations: list[Citation] = Field(
        default_factory=list,
        description=(
            "Works the source cites in connection with this evidence. A marker may "
            "sit next to the passage rather than inside it, so this is not required "
            "to be a substring of `text`."
        ),
    )
    evidence_form: Literal["verbatim", "paraphrased"] = Field(
        description=(
            "Whether this text is an exact quotation from the source (verbatim) or "
            "a paraphrase of source content (paraphrased)."
        )
    )
    relationship_to_claim: Literal[
        "claim_grounding", "direct_support", "partial_support", "contextual_support"
    ] = Field(
        description=(
            "How this evidence relates to its claim. 'claim_grounding' is "
            "categorically different from the other three: it means the source "
            "itself states the claim (attribution), not that source material "
            "evidentially supports it. The other three are not an ordered strength "
            "scale: 'direct_support' supports the claim in full, 'partial_support' "
            "supports part of it, and 'contextual_support' gives relevant context "
            "without directly supporting it."
        )
    )


class Claim(ResearchBaseModel):
    """A claim that matters to the source's argument, with its evidence."""

    text: NonEmptyStr
    statement_origin: Literal["author_stated", "model_inferred"] = Field(
        description=STATEMENT_ORIGIN_DESCRIPTION
    )
    evidence: list[Evidence] = Field(default_factory=list)
    support_assessment: NonEmptyStr | None = Field(
        default=None,
        description=(
            "A provisional, passage-grounded judgment of whether the reasons offered "
            "meet this claim's own stated strength and scope. Always the model's own "
            "assessment, never something the source states, and never a claim that a "
            "cited work has been verified. Reserved for claims whose importance and "
            "wording call for it; most claims will not have one. Unset means the claim "
            "was not assessed — never that it is well-supported or that no issue exists."
        ),
    )


class Methodology(ResearchBaseModel):
    """How the source says it did its work. Recording it is not assessing it."""

    summary: NonEmptyStr
    study_design: NonEmptyStr | None = None
    data_sources: list[NonEmptyStr] = Field(default_factory=list)
    sample_or_scope: NonEmptyStr | None = None
    analysis_methods: list[NonEmptyStr] = Field(default_factory=list)
    statement_origin: Literal["author_stated", "model_inferred"] = Field(
        description=STATEMENT_ORIGIN_DESCRIPTION
    )


class ExtractedAnalysis(ResearchBaseModel):
    """Exactly what the model is asked to return.

    This is the schema sent to the API. It holds no identifier, no provenance,
    and no timestamp, so there is nothing application-owned for the model to
    invent a value for.
    """

    research_problem: Statement
    central_claims: list[Claim] = Field(default_factory=list)
    methodology: Methodology | None = None
    assumptions: list[Statement] = Field(default_factory=list)
    limitations: list[Statement] = Field(default_factory=list)
    proposed_solutions: list[Statement] = Field(default_factory=list)
    open_questions: list[Statement] = Field(default_factory=list)


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
