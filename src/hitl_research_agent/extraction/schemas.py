from typing import Literal

from pydantic import Field, model_validator

from ..models._base import NonEmptyStr, ResearchBaseModel
from ..models.analysis import SourceAnalysis
from ..models.citation import Citation
from ..models.interpreted import (
    Assumption,
    Limitation,
    OpenQuestion,
    ProposedSolution,
    ResearchProblem,
)
from ..models.methodology import Methodology
from ..models.provenance import Provenance
from .annotations import find_annotations, reserved_character_problems
from .attachments import Attachment, InputMode
from .attempts import AttemptRecord

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
    """One thing the preparation step could not represent faithfully in text.

    Mirrors an entry of ``prep_record.json["annotations"]``. ``image`` is relative
    to ``preparation_directory`` on the document or result that carries this gap;
    the two are kept together so a crop stays resolvable without absolute paths.
    """

    id: NonEmptyStr
    kind: NonEmptyStr  # figure | equation | table
    page: int = Field(ge=1)
    label: str | None = None
    image: str | None = None


class SourceDocument(ResearchBaseModel):
    """Phase 2's input contract: source text plus the provenance describing it.

    Does not define how the text was normalized (that is Phase 5's concern) —
    it only states what Phase 2 requires to already be true of the text it
    receives.
    """

    text: NonEmptyStr
    provenance: Provenance
    preparation_directory: str | None = Field(
        default=None,
        description=(
            "Repo-relative preparation directory the text came from. Crop paths in "
            "preparation_gaps resolve against it."
        ),
    )
    preparation_gaps: list[PreparationGap] = Field(
        default_factory=list,
        description=(
            "What preparation could not represent in this text, from the source's "
            "preparation record. Empty means the text carries no annotations."
        ),
    )

    @model_validator(mode="after")
    def _reject_reserved_characters(self) -> "SourceDocument":
        problems = reserved_character_problems(self.text)
        if problems:
            raise ValueError("; ".join(problems))
        return self

    @model_validator(mode="after")
    def _gaps_match_the_annotations_in_the_text(self) -> "SourceDocument":
        """A result must never claim coverage the text does not have."""
        in_text = {span.annotation_id for span in find_annotations(self.text)}
        declared = {gap.id for gap in self.preparation_gaps}
        if in_text - declared:
            raise ValueError(
                "the text contains preparation annotations with no matching entry in "
                f"preparation_gaps: {sorted(in_text - declared)}"
            )
        if declared - in_text:
            raise ValueError(
                "preparation_gaps names items that do not appear in the text: "
                f"{sorted(declared - in_text)}"
            )
        if self.preparation_gaps and not self.preparation_directory:
            raise ValueError("preparation_gaps requires preparation_directory to resolve images")
        return self


class ExtractedEvidence(ResearchBaseModel):
    """Evidence as produced by the model. Same fields as Evidence minus `id`,
    which is application-owned and has no legitimate model-generated value."""

    text: NonEmptyStr
    locator: NonEmptyStr | None = None
    citations: list[Citation] = Field(default_factory=list)
    evidence_form: Literal["verbatim", "paraphrased"] = Field(
        description=(
            "Whether this evidence text is a verbatim quotation from the "
            "source (verbatim) or a paraphrase of source content (paraphrased)."
        )
    )
    relationship_to_claim: Literal[
        "claim_grounding", "direct_support", "partial_support", "contextual_support"
    ] = Field(
        description=(
            "How this evidence relates to the claim it is attached to. "
            "'claim_grounding' is categorically distinct from the other three "
            "values: it means the source itself states or makes the claim "
            "(attribution), not that source material evidentially supports it. "
            "The other three values describe how source material supports the "
            "claim and are not an ordered strength scale: 'direct_support' "
            "supports the claim in full, 'partial_support' supports only part "
            "of the claim, and 'contextual_support' provides relevant context "
            "without directly supporting the claim."
        )
    )


class ExtractedClaim(ResearchBaseModel):
    """A claim as produced by the model. Same fields as Claim minus `id`.

    Carries no cross-field validator of its own: statement_origin/evidence
    consistency is enforced once, when a real Claim is assembled from this
    data after the model call returns.
    """

    text: NonEmptyStr
    statement_origin: Literal["author_stated", "model_inferred"] = Field(
        description=(
            "Whether this statement is explicitly made by the source "
            "(author_stated) or synthesized by the model as an interpretation "
            "not explicitly stated in the source text (model_inferred)."
        )
    )
    evidence: list[ExtractedEvidence] = Field(default_factory=list)
    support_assessment: NonEmptyStr | None = Field(
        default=None,
        description=(
            "A provisional, passage-grounded judgment, for human review, of "
            "whether the reasons offered elsewhere in this analysis meet this "
            "claim's own stated strength and scope. Always your own critical "
            "assessment, never something the source itself states, and never "
            "a claim that a cited work has been verified. Reserved for claims "
            "whose importance to the argument and whose own wording call for "
            "this scrutiny; most claims will not have one. Leaving this unset "
            "means the claim was not assessed — never that it is well-"
            "supported or that no issue was found."
        ),
    )


class ExtractedAnalysis(ResearchBaseModel):
    """The complete model-generated content of a SourceAnalysis.

    Everything the application owns (`id`, `provenance`, `analyzed_at`) is
    absent; every other field mirrors SourceAnalysis exactly, reusing the
    Phase 1 models directly wherever they carry no application-owned field.
    """

    research_problem: ResearchProblem
    central_claims: list[ExtractedClaim] = Field(default_factory=list)
    methodology: Methodology | None = None
    assumptions: list[Assumption] = Field(default_factory=list)
    limitations: list[Limitation] = Field(default_factory=list)
    proposed_solutions: list[ProposedSolution] = Field(default_factory=list)
    open_questions: list[OpenQuestion] = Field(default_factory=list)


class AnalysisResult(ResearchBaseModel):
    """What analyze_source() returns: the completed analysis plus call facts.

    input_tokens/output_tokens are the exact sum of usage reported for every
    call counted in attempt_count — never a fabricated value standing in for
    an unknown one.
    """

    analysis: SourceAnalysis
    analysis_scope: NonEmptyStr = Field(
        default=ANALYSIS_SCOPE,
        description=(
            "What this result does and does not cover. Carried on the saved result so "
            "the text-only limit travels with it into synthesis and retrieval."
        ),
    )
    preparation_directory: str | None = None
    preparation_gaps: list[PreparationGap] = Field(
        default_factory=list,
        description="Copied from the analyzed SourceDocument; images are relative to "
        "preparation_directory.",
    )
    input_mode: InputMode = Field(
        default="prepared_text",
        description="What the model actually received for this analysis.",
    )
    model_inputs: list[Attachment] = Field(
        default_factory=list,
        description=(
            "Attachments sent with the request, with the sha256 of the exact bytes. "
            "Empty for a text-only analysis."
        ),
    )
    model: NonEmptyStr
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    attempt_count: int = Field(ge=1, le=2)
    attempts: list[AttemptRecord] = Field(
        default_factory=list,
        description=(
            "One record per model call, kept for audit. Empty only for results "
            "saved before attempt retention existed."
        ),
    )

    @model_validator(mode="after")
    def _attempts_match_count(self) -> "AnalysisResult":
        if self.attempts and len(self.attempts) != self.attempt_count:
            raise ValueError("attempts must contain exactly attempt_count records when present")
        if self.preparation_gaps and not self.preparation_directory:
            raise ValueError("preparation_gaps requires preparation_directory to resolve images")
        if self.model_inputs and self.input_mode == "prepared_text":
            raise ValueError("input_mode 'prepared_text' records no model_inputs")
        return self
