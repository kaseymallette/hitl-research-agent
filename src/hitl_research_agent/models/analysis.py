from datetime import UTC, datetime
from uuid import UUID, uuid4

from pydantic import AwareDatetime, Field

from ._base import ResearchBaseModel
from .claim import Claim
from .interpreted import Assumption, Limitation, OpenQuestion, ProposedSolution, ResearchProblem
from .methodology import Methodology
from .provenance import Provenance


class SourceAnalysis(ResearchBaseModel):
    id: UUID = Field(default_factory=uuid4)
    provenance: Provenance
    research_problem: ResearchProblem
    central_claims: list[Claim] = Field(min_length=1)
    methodology: Methodology | None = None
    assumptions: list[Assumption] = Field(default_factory=list)
    limitations: list[Limitation] = Field(default_factory=list)
    proposed_solutions: list[ProposedSolution] = Field(default_factory=list)
    open_questions: list[OpenQuestion] = Field(default_factory=list)
    analyzed_at: AwareDatetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description=(
            "Application-generated timestamp recording when this specific "
            "analysis result was created. Not produced by the LLM. Contrast "
            "with Provenance.retrieved_at, which records when the underlying "
            "source itself was retrieved, independent of when it was analyzed."
        ),
    )
