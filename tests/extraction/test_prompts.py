from hitl_research_agent.extraction.prompts import SYSTEM_PROMPT


def test_system_prompt_requires_scanning_the_conclusion_for_new_claims() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "conclusion" in lowered
    assert "not stated earlier" in lowered


def test_system_prompt_forbids_softening_strong_or_speculative_claims() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "do not omit, soften, or normalize a claim" in lowered
    assert "speculative" in lowered
    assert "controversial" in lowered
    assert "preserve the authors' own strength of language" in lowered


def test_system_prompt_directs_weakness_to_separate_fields_not_the_claim_text() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "represent any weakness in its support separately" in lowered
    assert "evidence_form" in SYSTEM_PROMPT
    assert "relationship_to_claim" in SYSTEM_PROMPT
    assert "limitation" in lowered


def test_system_prompt_requires_equal_treatment_of_claim_types() -> None:
    lowered = SYSTEM_PROMPT.lower()
    for claim_type in ("normative", "causal", "predictive", "prescriptive"):
        assert claim_type in lowered


def test_system_prompt_forbids_merging_distinct_claims() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "keep sentences as separate claims" in lowered


def test_system_prompt_still_requires_selective_structured_output() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "not summarization" in lowered
    assert "not every sentence in the source" in lowered


def test_system_prompt_requires_scanning_background_paragraphs_for_claims() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "prior literature" in lowered
    assert "do not treat such a paragraph as citation only" in lowered


def test_system_prompt_requires_preserving_worked_example_tradeoffs() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "concrete example" in lowered
    assert "tradeoff" in lowered
    assert "not incidental color" in lowered


def test_system_prompt_forbids_redundant_claims_for_a_repeated_thesis() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "states the same thesis more than once" in lowered
    assert "distinct point, qualification, or piece of evidence" in lowered


def test_system_prompt_directs_citations_to_the_citations_field() -> None:
    assert '"citations"' in SYSTEM_PROMPT
    assert "citation_text" in SYSTEM_PROMPT
    assert "reference_entry" in SYSTEM_PROMPT


def test_system_prompt_allows_citation_marker_outside_evidence_text() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "may sit next to the quoted or paraphrased passage rather than inside it" in lowered


def test_system_prompt_forbids_inventing_bibliography_details() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "never invent or complete a missing bibliography detail" in lowered


def test_system_prompt_clarifies_citations_are_not_verification() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "you are not verifying, retrieving, or assessing the cited work" in lowered


def test_system_prompt_selects_assessment_claims_by_importance_not_keyword() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert '"support_assessment"' in lowered
    assert "never by matching a keyword" in lowered
    assert "most claims will not need this field" in lowered


def test_system_prompt_defines_unset_assessment_as_not_assessed() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "leaving it unset means the claim was not assessed at all" in lowered
    assert "not a judgment that the claim is well-supported" in lowered
    assert "not a claim that no issue exists" in lowered


def test_system_prompt_uses_necessity_as_an_illustration_not_a_rule() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "necessary for what, under which conditions" in lowered
    assert "elimination only" in lowered
    assert "not a rule to apply mechanically or a predetermined verdict" in lowered


def test_system_prompt_distinguishes_announced_aim_from_developed_argument() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "is not itself a reason for the conclusion" in lowered


def test_system_prompt_requires_passage_references_for_assessments() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "cite the specific passages and locations" in lowered


def test_system_prompt_connects_inferred_assumptions_to_their_claim() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "say in the assessment which claim it is needed for" in lowered
    assert "do not state it as if the authors said it" in lowered


def test_system_prompt_allows_insufficient_information_and_sound_arguments() -> None:
    lowered = SYSTEM_PROMPT.lower()
    assert "if there is not enough in the source to decide, say so" in lowered
    assert "recognize a well-supported claim as such" in lowered
