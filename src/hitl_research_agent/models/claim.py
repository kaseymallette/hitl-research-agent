from typing import Literal
from uuid import UUID, uuid4

from pydantic import Field, model_validator

from ._base import NonEmptyStr, ResearchBaseModel
from .citation import Citation
from .interpreted import InterpretedStatement


class Evidence(ResearchBaseModel):
    id: UUID = Field(default_factory=uuid4)
    text: NonEmptyStr
    locator: NonEmptyStr | None = None
    citations: list[Citation] = Field(
        default_factory=list,
        description=(
            "Works the source cites in connection with this evidence. A "
            "citation marker may sit next to the quoted or paraphrased "
            "passage rather than inside it, so this is not required to be a "
            "substring of `text`. Distinct from Provenance: these record "
            "what the source cites, not a work this system has retrieved or "
            "verified."
        ),
    )
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

    @model_validator(mode="after")
    def _claim_grounding_requires_verbatim(self) -> "Evidence":
        if self.relationship_to_claim == "claim_grounding" and self.evidence_form != "verbatim":
            raise ValueError("Evidence marked 'claim_grounding' must use evidence_form='verbatim'.")
        return self


class Claim(InterpretedStatement):
    id: UUID = Field(default_factory=uuid4)
    evidence: list[Evidence] = Field(min_length=1)
    support_assessment: NonEmptyStr | None = Field(
        default=None,
        description=(
            "A provisional, passage-grounded judgment, for human review, of "
            "whether the reasons offered elsewhere in this analysis meet this "
            "claim's own stated strength and scope. Always the model's own "
            "critical assessment, never something the source itself states, "
            "and never a claim that a cited work has been verified. Reserved "
            "for claims whose importance to the argument and whose own "
            "wording call for this scrutiny; most claims will not have one. "
            "None means the claim was not assessed — it is not a judgment "
            "that the claim is well-supported or that no issue was found."
        ),
    )

    @model_validator(mode="after")
    def _validate_grounding_consistency(self) -> "Claim":
        has_grounding = any(e.relationship_to_claim == "claim_grounding" for e in self.evidence)
        if self.statement_origin == "author_stated" and not has_grounding:
            raise ValueError(
                "An author_stated claim must include at least one Evidence "
                "item whose relationship_to_claim is 'claim_grounding'."
            )
        if self.statement_origin == "model_inferred" and has_grounding:
            raise ValueError("A model_inferred claim must not contain 'claim_grounding' evidence.")
        return self
