"""Preparation gaps and the analysis scope travel with the saved result."""

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError

from hitl_research_agent.extraction import (
    ANALYSIS_SCOPE,
    AnalysisResult,
    PreparationGap,
    SourceDocument,
)
from hitl_research_agent.extraction.annotations import format_annotation
from hitl_research_agent.models.analysis import SourceAnalysis
from hitl_research_agent.models.claim import Claim, Evidence
from hitl_research_agent.models.interpreted import ResearchProblem
from hitl_research_agent.models.provenance import Provenance

REPO_ROOT = Path(__file__).resolve().parents[2]

ANNOTATION = format_annotation(
    "U1",
    {"kind": "figure", "label": "Figure 1", "page": "4", "image": "images/U1_p04.png"},
    "content not extracted; see the retained image",
)
TEXT = f"Water use rose sharply. {ANNOTATION} Cooling relied on evaporative towers."
GAP = PreparationGap(id="U1", kind="figure", page=4, label="Figure 1", image="images/U1_p04.png")
PREP_DIR = "outputs/preparation/li_et_al_2025_making_ai_less_thirsty"


def _provenance() -> Provenance:
    return Provenance(
        source_title="T", source_type="peer_reviewed_paper", retrieved_at=datetime.now(UTC)
    )


def _analysis() -> SourceAnalysis:
    return SourceAnalysis(
        provenance=_provenance(),
        research_problem=ResearchProblem(text="Why?", statement_origin="author_stated"),
        central_claims=[
            Claim(
                text="A claim.",
                statement_origin="author_stated",
                evidence=[
                    Evidence(
                        text="Water use rose sharply.",
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
            )
        ],
    )


def _result(**overrides: Any) -> AnalysisResult:
    data: dict[str, Any] = dict(
        analysis=_analysis(),
        preparation_directory=PREP_DIR,
        preparation_gaps=[GAP],
        model="gpt-6-astra",
        input_tokens=10,
        output_tokens=5,
        attempt_count=1,
    )
    data.update(overrides)
    return AnalysisResult(**data)


# --- the scope statement ------------------------------------------------------------------------


def test_scope_states_the_text_only_limit_and_is_on_every_result() -> None:
    assert ANALYSIS_SCOPE == (
        "Analysis used prepared text only. Listed items were omitted or incompletely "
        "represented; their original image content was not assessed."
    )
    assert _result().analysis_scope == ANALYSIS_SCOPE  # default, not opt-in


def test_scope_survives_a_round_trip_through_json() -> None:
    """The limit must reach Phase 6 and 7, not just the reviewer's screen."""
    restored = AnalysisResult.model_validate_json(_result().model_dump_json())
    assert restored.analysis_scope == ANALYSIS_SCOPE
    assert [g.id for g in restored.preparation_gaps] == ["U1"]
    assert restored.preparation_directory == PREP_DIR


# --- gaps stay resolvable -----------------------------------------------------------------------


def test_crop_paths_stay_relative_and_resolve_against_the_preparation_directory() -> None:
    result = _result()
    gap = result.preparation_gaps[0]
    assert gap.image is not None
    assert not Path(gap.image).is_absolute()  # moving the repo must not break it
    assert (REPO_ROOT / result.preparation_directory / gap.image).parent.name == "images"


def test_gaps_without_a_preparation_directory_are_rejected() -> None:
    with pytest.raises(ValidationError, match="preparation_directory"):
        _result(preparation_directory=None)
    with pytest.raises(ValidationError, match="preparation_directory"):
        SourceDocument(text=TEXT, provenance=_provenance(), preparation_gaps=[GAP])


# --- the document and its text agree -------------------------------------------------------------


def test_a_document_must_declare_every_annotation_its_text_carries() -> None:
    with pytest.raises(ValidationError, match="no matching entry"):
        SourceDocument(text=TEXT, provenance=_provenance())


def test_a_document_cannot_claim_a_gap_its_text_does_not_contain() -> None:
    with pytest.raises(ValidationError, match="do not appear in the text"):
        SourceDocument(
            text="Plain prose with no annotations.",
            provenance=_provenance(),
            preparation_directory=PREP_DIR,
            preparation_gaps=[GAP],
        )


def test_plain_text_needs_no_gaps() -> None:
    document = SourceDocument(text="Plain prose.", provenance=_provenance())
    assert document.preparation_gaps == [] and document.preparation_directory is None


# --- the shape matches the preparation record it is copied from -----------------------------------


def test_gaps_can_be_built_from_a_prep_record_without_new_vocabulary(tmp_path: Path) -> None:
    """A preparation record's annotations map straight onto PreparationGap, and
    its relative image paths resolve under the preparation directory."""
    (tmp_path / "images").mkdir()
    (tmp_path / "images" / "U1_p04.png").write_bytes(b"png")
    (tmp_path / "images" / "T1_p06.png").write_bytes(b"png")
    record = {
        "annotations": [
            {
                "id": "U1",
                "kind": "figure",
                "page": 4,
                "label": "Figure 1",
                "image": "images/U1_p04.png",
            },
            {
                "id": "T1",
                "kind": "table",
                "page": 6,
                "label": "Table 1",
                "image": "images/T1_p06.png",
            },
        ]
    }
    (tmp_path / "prep_record.json").write_text(json.dumps(record))

    loaded = json.loads((tmp_path / "prep_record.json").read_text())
    gaps = [
        PreparationGap(
            id=a["id"], kind=a["kind"], page=a["page"], label=a["label"], image=a["image"]
        )
        for a in loaded["annotations"]
    ]
    assert {g.kind for g in gaps} <= {"figure", "equation", "table"}
    for gap in gaps:
        assert gap.image is not None and not Path(gap.image).is_absolute()
        assert (tmp_path / gap.image).exists()
