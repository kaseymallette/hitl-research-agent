from typing import Literal
from uuid import UUID, uuid4

from pydantic import Field, model_validator

from ._base import NonEmptyStr, ResearchBaseModel
from .interpreted import InterpretedStatement


class Evidence(ResearchBaseModel):
    id: UUID = Field(default_factory=uuid4)
    text: NonEmptyStr
    locator: NonEmptyStr | None = None
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
