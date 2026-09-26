import re
from collections.abc import Sequence

from .schemas import ExtractedClaim


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def find_ungrounded_verbatim_evidence(
    claims: Sequence[ExtractedClaim], source_text: str
) -> list[str]:
    """Return a description for every 'verbatim' evidence item that does not
    literally appear in the source text (case/whitespace-normalized).

    Paraphrased evidence is never checked — this is a mechanical grounding
    check, not a faithfulness evaluation.
    """
    normalized_source = _normalize(source_text)
    problems: list[str] = []
    for claim in claims:
        for evidence in claim.evidence:
            if evidence.evidence_form != "verbatim":
                continue
            if _normalize(evidence.text) not in normalized_source:
                problems.append(
                    f"Evidence marked verbatim was not found in the source text: {evidence.text!r}"
                )
    return problems
