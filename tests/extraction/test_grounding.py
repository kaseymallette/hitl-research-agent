from hitl_research_agent.extraction.grounding import (
    find_ungrounded_verbatim_evidence,
    find_unverifiable_citations,
)
from hitl_research_agent.extraction.schemas import ExtractedClaim, ExtractedEvidence
from hitl_research_agent.models.citation import Citation

SOURCE_TEXT = (
    "Data centers used 1.7 billion  gallons of water in 2023 for cooling "
    "[Smith, 2020]. Smith, J. Water Use Report. 2020."
)


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


def test_citation_marker_in_source_passes_even_when_not_inside_evidence_text() -> None:
    # "Smith, 2020" sits next to this evidence in the source, not inside it.
    evidence = ExtractedEvidence(
        text="1.7 billion gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        citations=[Citation(citation_text="Smith, 2020")],
    )
    assert find_unverifiable_citations([_claim(evidence)], SOURCE_TEXT) == []


def test_citation_marker_absent_from_source_fails() -> None:
    evidence = ExtractedEvidence(
        text="1.7 billion gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        citations=[Citation(citation_text="Jones, 1999")],
    )
    problems = find_unverifiable_citations([_claim(evidence)], SOURCE_TEXT)
    assert len(problems) == 1
    assert "Jones, 1999" in problems[0]


def test_reference_entry_present_in_source_passes() -> None:
    evidence = ExtractedEvidence(
        text="1.7 billion gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        citations=[
            Citation(
                citation_text="Smith, 2020", reference_entry="Smith, J. Water Use Report. 2020."
            )
        ],
    )
    assert find_unverifiable_citations([_claim(evidence)], SOURCE_TEXT) == []


def test_reference_entry_absent_from_source_fails() -> None:
    evidence = ExtractedEvidence(
        text="1.7 billion gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        citations=[
            Citation(
                citation_text="Smith, 2020", reference_entry="Smith, J. An Invented Title. 2020."
            )
        ],
    )
    problems = find_unverifiable_citations([_claim(evidence)], SOURCE_TEXT)
    assert len(problems) == 1
    assert "Invented Title" in problems[0]


def test_citation_without_reference_entry_only_checks_the_marker() -> None:
    evidence = ExtractedEvidence(
        text="1.7 billion gallons of water",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        citations=[Citation(citation_text="Smith, 2020")],
    )
    assert find_unverifiable_citations([_claim(evidence)], SOURCE_TEXT) == []


def test_combined_non_adjacent_reference_entries_still_fail_with_actionable_guidance() -> None:
    source = (
        "Text <sup>23,32,33</sup>\n"
        "23. Reig, P. Guidance. WRI (2020).\n24. Other, A. Filler. (2021).\n"
        "32. EIA. Open Data.\n33. EPA. eGRID Data Explorer.\n"
    )
    combined = (
        "23. Reig, P. Guidance. WRI (2020).\n32. EIA. Open Data.\n33. EPA. eGRID Data Explorer."
    )
    evidence = ExtractedEvidence(
        text="Text",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        citations=[Citation(citation_text="23,32,33", reference_entry=combined)],
    )
    problems = find_unverifiable_citations([_claim(evidence)], source)
    assert len(problems) == 1  # the grounding check itself is not weakened
    assert "exactly one entry" in problems[0]
    assert "one citation per work" in problems[0]


def test_grouped_marker_split_into_one_citation_per_work_passes() -> None:
    source = (
        "Text <sup>23,32,33</sup>\n"
        "23. Reig, P. Guidance. WRI (2020).\n24. Other, A. Filler. (2021).\n"
        "32. EIA. Open Data.\n33. EPA. eGRID Data Explorer.\n"
    )
    entries = [
        "23. Reig, P. Guidance. WRI (2020).",
        "32. EIA. Open Data.",
        "33. EPA. eGRID Data Explorer.",
    ]
    evidence = ExtractedEvidence(
        text="Text",
        evidence_form="verbatim",
        relationship_to_claim="claim_grounding",
        citations=[Citation(citation_text="23,32,33", reference_entry=e) for e in entries],
    )
    assert find_unverifiable_citations([_claim(evidence)], source) == []
