"""What reaches the model, per input mode.

These guard the A/B experiment's central requirement: that the two arms differ
in input format and nothing else, and that a saved result names the exact bytes
that were sent.
"""

import base64
import hashlib
from datetime import UTC, datetime
from pathlib import Path

import pytest

from hitl_research_agent.inputs import (
    MAX_REQUEST_FILE_BYTES,
    Attachment,
    LoadedAttachment,
    find_annotations,
    format_annotation,
    load_attachment,
    validate_attachments,
)
from hitl_research_agent.models import PreparationGap, Provenance, SourceDocument
from hitl_research_agent.prompts import (
    CROPS_INPUT_INSTRUCTIONS,
    PDF_INPUT_INSTRUCTIONS,
    SYSTEM_PROMPT,
    build_messages,
)

PROVENANCE = Provenance(
    source_title="A Paper",
    source_type="peer_reviewed_paper",
    retrieved_at=datetime(2026, 10, 13, tzinfo=UTC),
)
ANNOTATION = format_annotation(
    "U1", {"kind": "figure", "label": "Figure 1", "page": "4"}, "content not extracted"
)
GAP = PreparationGap(id="U1", kind="figure", page=4, label="Figure 1", image="images/U1_p04.png")


def _source(*, annotated: bool = False) -> SourceDocument:
    return SourceDocument(
        text=f"Body text. {ANNOTATION} More body." if annotated else "Body text only.",
        provenance=PROVENANCE,
        preparation_directory="outputs/preparation/fixture" if annotated else None,
        preparation_gaps=[GAP] if annotated else [],
    )


def _pdf(
    tmp_path: Path, name: str = "source.pdf", data: bytes = b"%PDF-1.7 body"
) -> LoadedAttachment:
    (tmp_path / name).write_bytes(data)
    return load_attachment(tmp_path, name, kind="pdf")


def _crop(tmp_path: Path, gap_id: str = "U1") -> LoadedAttachment:
    (tmp_path / "crop.png").write_bytes(b"\x89PNG\r\n\x1a\n fake")
    return load_attachment(
        tmp_path, "crop.png", kind="image", page=4, gap_id=gap_id, label="Figure 1"
    )


# --------------------------------------------------------------------------- loading


def test_an_attachment_hashes_exactly_the_bytes_that_are_sent(tmp_path: Path) -> None:
    """The sha256 in a run record has to identify the real input, or the record
    cannot be used to reproduce the run."""
    data = b"%PDF-1.7 specific bytes"
    loaded = _pdf(tmp_path, data=data)
    assert loaded.record.sha256 == hashlib.sha256(data).hexdigest()
    assert loaded.record.byte_size == len(data)
    assert base64.b64decode(loaded.data) == data


def test_an_empty_or_mistyped_attachment_is_refused(tmp_path: Path) -> None:
    (tmp_path / "empty.pdf").write_bytes(b"")
    with pytest.raises(ValueError, match="empty"):
        load_attachment(tmp_path, "empty.pdf", kind="pdf")
    (tmp_path / "notes.txt").write_bytes(b"text")
    with pytest.raises(ValueError, match="unsupported image type"):
        load_attachment(tmp_path, "notes.txt", kind="image")
    with pytest.raises(ValueError, match="expected a .pdf"):
        load_attachment(tmp_path, "notes.txt", kind="pdf")


# --------------------------------------------------------------------------- validation


def test_each_input_mode_requires_its_own_attachments(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="sends no attachments"):
        validate_attachments("prepared_text", [_pdf(tmp_path)], [])
    with pytest.raises(ValueError, match="exactly one pdf"):
        validate_attachments("pdf", [], [])
    with pytest.raises(ValueError, match="exactly one pdf"):
        validate_attachments("pdf", [_crop(tmp_path)], ["U1"])
    with pytest.raises(ValueError, match="at least one image"):
        validate_attachments("prepared_text_and_crops", [_pdf(tmp_path)], ["U1"])
    validate_attachments("pdf", [_pdf(tmp_path)], [])
    validate_attachments("prepared_text_and_crops", [_crop(tmp_path)], ["U1"])


def test_a_crop_must_name_a_gap_the_document_declares(tmp_path: Path) -> None:
    """Otherwise a result could ship a crop for material its text never marked."""
    with pytest.raises(ValueError, match="unknown gap ids"):
        validate_attachments("prepared_text_and_crops", [_crop(tmp_path, "T9")], ["U1"])
    with pytest.raises(ValueError, match="must name the preparation gap"):
        validate_attachments("prepared_text_and_crops", [_crop(tmp_path, None)], ["U1"])  # type: ignore[arg-type]


def test_attachments_over_the_documented_request_limit_are_refused() -> None:
    oversized = LoadedAttachment(
        record=Attachment(
            kind="pdf",
            path="data/research/huge.pdf",
            mime_type="application/pdf",
            sha256="0" * 64,
            byte_size=MAX_REQUEST_FILE_BYTES + 1,
        ),
        data="",
    )
    with pytest.raises(ValueError, match="per-request limit"):
        validate_attachments("pdf", [oversized], [])


# --------------------------------------------------------------------------- message assembly


def test_every_mode_sends_the_same_analysis_prompt(tmp_path: Path) -> None:
    """The experiment compares input formats. If the analysis instructions
    differed between arms, the comparison would measure nothing."""
    plain = build_messages(_source())
    as_pdf = build_messages(_source(), input_mode="pdf", attachments=[_pdf(tmp_path)])
    as_crops = build_messages(
        _source(annotated=True), input_mode="prepared_text_and_crops", attachments=[_crop(tmp_path)]
    )
    for messages in (plain, as_pdf, as_crops):
        assert messages[0].content == SYSTEM_PROMPT


def test_the_pdf_mode_sends_the_file_and_withholds_the_prepared_text(tmp_path: Path) -> None:
    attachment = _pdf(tmp_path)
    messages = build_messages(_source(), input_mode="pdf", attachments=[attachment])
    blocks = messages[1].content
    assert isinstance(blocks, list)
    assert any(b.get("type") == "file" for b in blocks if isinstance(b, dict))
    text = " ".join(b["text"] for b in blocks if isinstance(b, dict) and b.get("type") == "text")
    assert PDF_INPUT_INSTRUCTIONS in text
    assert "Body text only." not in text  # the prepared text is not the input in this mode


def test_the_crops_mode_sends_the_text_and_one_image_per_gap(tmp_path: Path) -> None:
    messages = build_messages(
        _source(annotated=True), input_mode="prepared_text_and_crops", attachments=[_crop(tmp_path)]
    )
    blocks = messages[1].content
    assert isinstance(blocks, list)
    assert sum(1 for b in blocks if isinstance(b, dict) and b.get("type") == "image") == 1
    text = " ".join(b["text"] for b in blocks if isinstance(b, dict) and b.get("type") == "text")
    assert CROPS_INPUT_INSTRUCTIONS in text
    assert "Body text." in text
    assert "gap U1" in text and "page 4" in text  # the model can locate the crop again


def test_text_only_mode_sends_one_plain_string_and_no_format_instructions() -> None:
    messages = build_messages(_source())
    assert messages[1].content == (
        "Source title: A Paper\nSource type: peer_reviewed_paper\n\nBody text only."
    )


# --------------------------------------------------------------------------- annotations


def test_an_annotation_is_locatable_and_carries_no_interpretation() -> None:
    spans = find_annotations(f"Before. {ANNOTATION} After.")
    assert [span.annotation_id for span in spans] == ["U1"]
    assert "content not extracted" in ANNOTATION


def test_annotation_fields_cannot_smuggle_in_reserved_characters() -> None:
    with pytest.raises(ValueError, match="reserved characters"):
        format_annotation("U1", {"label": "Figure ⟧ 1"}, "note")
