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
    ArgumentEvaluation,
    Claim,
    ExtractedAnalysis,
    PreparationGap,
    Provenance,
    ReadingStep,
    ResearchBaseModel,
    SourceAnalysis,
    SourceDocument,
    Support,
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
        "reading_plan": "A short journal review, moderately dense; steps of about a paragraph.",
        "reading_path": [
            ReadingStep(
                location="page 1, Introduction",
                moves="a premise, supported by a reported figure",
                claims=[
                    Claim(
                        text="Cooling drives most on-site water use.",
                        form="paraphrased",
                        support=[
                            Support(
                                text="Cooling accounted for the majority of withdrawal.",
                                form="paraphrased",
                            )
                        ],
                    )
                ],
                meaning="The opening premise; nothing precedes it.",
            )
        ],
    }
    return ExtractedAnalysis(**{**defaults, **overrides})  # type: ignore[arg-type]


def test_unknown_fields_are_rejected_so_an_invented_field_fails_loudly() -> None:
    """The one Pydantic setting we choose: extra='forbid' on every model."""
    with pytest.raises(ValidationError):
        ResearchBaseModel.model_validate({"unexpected": 1})
    with pytest.raises(ValidationError):
        Claim.model_validate({"text": "x", "form": "verbatim", "confidence": 0.9})


def test_the_model_cannot_supply_application_owned_fields() -> None:
    """ExtractedAnalysis is the schema sent to the API. An id, provenance, or
    timestamp coming back from the model is a value we would have to trust."""
    for field in ("id", "provenance", "analyzed_at", "source_id"):
        with pytest.raises(ValidationError):
            ExtractedAnalysis.model_validate(
                {**_content().model_dump(), field: "anything"},
            )


def test_every_claim_says_whether_it_is_the_author_s_exact_words() -> None:
    """Verbatim is what a text search can check against the source, so the
    form is required rather than defaulted."""
    with pytest.raises(ValidationError):
        Claim.model_validate({"text": "unlabelled"})
    with pytest.raises(ValidationError):
        Claim.model_validate({"text": "x", "form": "quoted"})


def test_a_claim_the_author_simply_asserts_stands_without_support() -> None:
    """Support is only what the author offers. An asserted claim has none, and
    that is a finding for the evaluation, not a reason to reject the JSON."""
    claim = Claim(text="Cooling drives most on-site water use.", form="verbatim")
    assert claim.support == []


def test_the_close_reading_carries_no_attribution_labels() -> None:
    """Claims are the author's and moves and meaning are the model's, by where
    they sit; no label repeats what the structure already says (ADR-0013)."""
    claim_fields = set(Claim.model_json_schema()["properties"])
    support_fields = set(Support.model_json_schema()["properties"])
    assert claim_fields == {"text", "form", "support"}
    assert support_fields == {"text", "form", "citations"}


def test_analysis_wraps_model_content_with_provenance_and_timestamp() -> None:
    analysis = SourceAnalysis(provenance=PROVENANCE, content=_content())
    assert analysis.content.reading_path[0].claims[0].form == "paraphrased"
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


def test_the_argument_evaluation_schema_holds_only_the_model_s_judgment() -> None:
    """The second call's schema is the model's prose and nothing else: no
    attribution label to misread as a claim about the source, and nothing
    application-owned for the model to supply."""
    assert set(ArgumentEvaluation.model_json_schema()["properties"]) == {"evaluation"}
    for field in ("id", "analysis_id", "provenance", "statement_origin"):
        with pytest.raises(ValidationError):
            ArgumentEvaluation.model_validate({"evaluation": "It holds.", field: "x"})


def test_a_reading_step_may_make_no_claim() -> None:
    """A transition or a definition still belongs on the path; claims are what a
    step states, not what it must state."""
    step = ReadingStep(
        location="page 3, Section 4",
        moves="a turn to a new line of discussion",
        meaning="Leaves the local conflicts behind for technical alternatives.",
    )
    assert step.claims == []


def test_the_reading_plan_comes_first_and_is_required() -> None:
    """The model sets its pace before it starts the path, so the plan is the
    first field it writes, and a close reading without one does not fit."""
    schema = ExtractedAnalysis.model_json_schema()
    assert next(iter(schema["properties"])) == "reading_plan"
    assert "reading_plan" in schema["required"]
