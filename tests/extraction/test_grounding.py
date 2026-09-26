from hitl_research_agent.extraction.grounding import find_ungrounded_verbatim_evidence
from hitl_research_agent.extraction.schemas import ExtractedClaim, ExtractedEvidence

SOURCE_TEXT = "Data centers used 1.7 billion  gallons of water in 2023 for cooling."


def _claim(*evidence: ExtractedEvidence) -> ExtractedClaim:
    return ExtractedClaim(text="claim", statement_origin="author_stated", evidence=list(evidence))


def test_verbatim_evidence_present_in_source_passes() -> None:
    evidence = ExtractedEvidence(
        text="1.7 billion gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
    )
    assert find_ungrounded_verbatim_evidence([_claim(evidence)], SOURCE_TEXT) == []


def test_verbatim_evidence_absent_from_source_fails() -> None:
    evidence = ExtractedEvidence(
        text="3 billion gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
    )
    problems = find_ungrounded_verbatim_evidence([_claim(evidence)], SOURCE_TEXT)
    assert len(problems) == 1
    assert "3 billion gallons" in problems[0]


def test_paraphrased_evidence_is_not_checked() -> None:
    evidence = ExtractedEvidence(
        text="an amount of water no one measured",
        evidence_form="paraphrased",
        relationship_to_claim="direct_support",
    )
    assert find_ungrounded_verbatim_evidence([_claim(evidence)], SOURCE_TEXT) == []


def test_matching_is_case_and_whitespace_insensitive() -> None:
    evidence = ExtractedEvidence(
        text="1.7 BILLION   gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
    )
    assert find_ungrounded_verbatim_evidence([_claim(evidence)], SOURCE_TEXT) == []
