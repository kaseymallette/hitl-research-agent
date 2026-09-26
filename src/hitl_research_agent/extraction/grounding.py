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


def find_unverifiable_citations(claims: Sequence[ExtractedClaim], source_text: str) -> list[str]:
    """Return a description for every citation whose marker, or whose stated
    reference-list entry, does not appear anywhere in the source text.

    A citation marker may sit next to its evidence rather than inside it, so
    this checks the whole source text, not the specific Evidence.text it is
    attached to.
    """
    normalized_source = _normalize(source_text)
    problems: list[str] = []
    for claim in claims:
        for evidence in claim.evidence:
            for citation in evidence.citations:
                if _normalize(citation.citation_text) not in normalized_source:
                    problems.append(
                        "Citation marker was not found anywhere in the source text: "
                        f"{citation.citation_text!r}"
                    )
                if (
                    citation.reference_entry
                    and _normalize(citation.reference_entry) not in normalized_source
                ):
                    problems.append(
                        "Reference-list entry was not found anywhere in the source text: "
                        f"{citation.reference_entry!r}"
                    )
    return problems
