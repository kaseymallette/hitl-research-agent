from typing import Literal

from pydantic import Field

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


class SourceDocument(ResearchBaseModel):
    """Phase 2's input contract: source text plus the provenance describing it.

    Does not define how the text was normalized (that is Phase 5's concern) —
    it only states what Phase 2 requires to already be true of the text it
    receives.
    """

    text: NonEmptyStr
    provenance: Provenance


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
    evidence: list[ExtractedEvidence] = Field(min_length=1)
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
    central_claims: list[ExtractedClaim] = Field(min_length=1)
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
    model: NonEmptyStr
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    attempt_count: int = Field(ge=1, le=2)
