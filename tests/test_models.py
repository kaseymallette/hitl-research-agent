"""Schema rules that would cost us something if they broke.

Not tested here: that Pydantic strips whitespace, rejects unknown fields, or
gives each instance its own default list. Those are library guarantees, and one
check on `ResearchBaseModel` covers the only one we configure ourselves.
"""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from hitl_research_agent.inputs import format_annotation
from hitl_research_agent.models import (
    Claim,
    Evidence,
    ExtractedAnalysis,
    PreparationGap,
    Provenance,
    ResearchBaseModel,
    SourceAnalysis,
    SourceDocument,
    Statement,
    source_id_for,
)

PROVENANCE = Provenance(
    source_title="Making AI Less Thirsty",
    source_type="other",
    retrieved_at=datetime(2026, 10, 13, tzinfo=UTC),
)
ANNOTATION = format_annotation(
    "U1", {"kind": "figure", "label": "Figure 1", "page": "2"}, "content not extracted"
)
GAP = PreparationGap(id="U1", kind="figure", page=2, label="Figure 1", image="images/p2.png")


def _content(**overrides: object) -> ExtractedAnalysis:
    defaults: dict[str, object] = {
        "research_problem": Statement(
            text="Water use is unmeasured.", statement_origin="author_stated"
        ),
        "central_claims": [
            Claim(
                text="Cooling drives most on-site water use.",
                statement_origin="author_stated",
                evidence=[
                    Evidence(
                        text="Cooling accounted for the majority of withdrawal.",
                        evidence_form="paraphrased",
                        relationship_to_claim="direct_support",
                    )
                ],
            )
        ],
    }
    return ExtractedAnalysis(**{**defaults, **overrides})  # type: ignore[arg-type]


def test_unknown_fields_are_rejected_so_an_invented_field_fails_loudly() -> None:
    """The one Pydantic setting we choose: extra='forbid' on every model."""
    with pytest.raises(ValidationError):
        ResearchBaseModel.model_validate({"unexpected": 1})
    with pytest.raises(ValidationError):
        Statement.model_validate(
            {"text": "x", "statement_origin": "author_stated", "confidence": 0.9}
        )


def test_the_model_cannot_supply_application_owned_fields() -> None:
    """ExtractedAnalysis is the schema sent to the API. An id, provenance, or
    timestamp coming back from the model is a value we would have to trust."""
    for field in ("id", "provenance", "analyzed_at", "source_id"):
        with pytest.raises(ValidationError):
            ExtractedAnalysis.model_validate(
                {**_content().model_dump(), field: "anything"},
            )


def test_statement_origin_is_required_on_every_interpreted_statement() -> None:
    with pytest.raises(ValidationError):
        Statement.model_validate({"text": "unlabelled"})
    with pytest.raises(ValidationError):
        Claim.model_validate({"text": "unlabelled", "evidence": []})


def test_an_author_stated_claim_may_rest_on_a_paraphrase() -> None:
    """A faithful paraphrase is a correct answer. Nothing requires a quotation,
    and the labels are recorded as given rather than cross-enforced."""
    claim = Claim(
        text="Cooling drives most on-site water use.",
        statement_origin="author_stated",
        evidence=[
            Evidence(
                text="in our own words",
                evidence_form="paraphrased",
                relationship_to_claim="partial_support",
            )
        ],
    )
    assert claim.evidence[0].evidence_form == "paraphrased"
    assert claim.support_assessment is None  # unset means not assessed


def test_a_claim_with_no_evidence_is_accepted() -> None:
    """Thin output is an evaluation finding, not a reason to reject the JSON."""
    assert Claim(text="bare", statement_origin="model_inferred").evidence == []


def test_analysis_wraps_model_content_with_provenance_and_timestamp() -> None:
    analysis = SourceAnalysis(provenance=PROVENANCE, content=_content())
    assert analysis.content.central_claims[0].statement_origin == "author_stated"
    assert analysis.provenance.source_title == "Making AI Less Thirsty"
    assert analysis.analyzed_at.tzinfo is not None
    assert analysis.id != SourceAnalysis(provenance=PROVENANCE, content=_content()).id


def test_analysis_survives_a_round_trip_through_json() -> None:
    """Analyses are read back by evaluation and review, not just written."""
    analysis = SourceAnalysis(provenance=PROVENANCE, content=_content())
    restored = SourceAnalysis.model_validate_json(analysis.model_dump_json())
    assert restored == analysis


def test_declared_gaps_must_match_the_annotations_in_the_text() -> None:
    """A result must never claim coverage its text does not have."""
    with pytest.raises(ValidationError, match="no matching entry"):
        SourceDocument(
            text=f"Before. {ANNOTATION} After.",
            provenance=PROVENANCE,
            preparation_directory="outputs/preparation/x",
        )
    with pytest.raises(ValidationError, match="absent from the text"):
        SourceDocument(
            text="No annotations here.",
            provenance=PROVENANCE,
            preparation_directory="outputs/preparation/x",
            preparation_gaps=[GAP],
        )
    document = SourceDocument(
        text=f"Before. {ANNOTATION} After.",
        provenance=PROVENANCE,
        preparation_directory="outputs/preparation/x",
        preparation_gaps=[GAP],
    )
    assert [gap.id for gap in document.preparation_gaps] == ["U1"]


def test_gaps_require_a_directory_so_crops_stay_resolvable() -> None:
    with pytest.raises(ValidationError, match="preparation_directory"):
        SourceDocument(
            text=f"Before. {ANNOTATION} After.",
            provenance=PROVENANCE,
            preparation_gaps=[GAP],
        )


def test_source_text_with_a_stray_reserved_character_is_refused() -> None:
    """Annotation delimiters in source text would let a quotation masquerade
    as a preparation annotation."""
    for bad in ("stray ⟦ opener", "stray ⟧ closer"):
        with pytest.raises(ValidationError, match="reserved character"):
            SourceDocument(text=bad, provenance=PROVENANCE)


def test_a_source_id_is_the_same_for_every_analysis_of_one_slug() -> None:
    """Analyses of one source are recognized as such by a shared source_id,
    and the id is a stored identity, so the derivation must never drift."""
    slug = "barnett_itzhaki_2026_water_footprint_artificial_intelligence"
    assert source_id_for(slug) == source_id_for(slug)
    assert str(source_id_for(slug)) == "53ded687-3b31-5225-9dd6-52a9a05922cf"
    assert source_id_for(slug) != source_id_for("lei_et_al_2025_water_use_data_center_workloads")
