"""The two pilot input formats: what gets sent, and what stays unchanged.

Every test here is offline. The payload tests show how a request would be
assembled and translated for the Responses API; they establish nothing about
whether a live model accepts it.
"""

import base64
import json
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pytest
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from hitl_research_agent.config import Settings
from hitl_research_agent.extraction.annotations import format_annotation
from hitl_research_agent.extraction.attachments import (
    MAX_REQUEST_FILE_BYTES,
    Attachment,
    LoadedAttachment,
    load_attachment,
    validate_attachments,
)
from hitl_research_agent.extraction.pipeline import analyze_source
from hitl_research_agent.extraction.prompts import (
    CROPS_INPUT_INSTRUCTIONS,
    PDF_INPUT_INSTRUCTIONS,
    build_messages,
)
from hitl_research_agent.extraction.schemas import (
    ANALYSIS_SCOPE,
    ANALYSIS_SCOPE_PDF,
    ANALYSIS_SCOPE_TEXT_AND_CROPS,
    AnalysisResult,
    ExtractedAnalysis,
    ExtractedClaim,
    ExtractedEvidence,
    PreparationGap,
    SourceDocument,
)
from hitl_research_agent.models.provenance import Provenance

QUOTE = "cooling towers evaporate freshwater"
ANNOTATION = format_annotation(
    "U1", {"kind": "figure", "page": "4", "label": "Figure 1"}, "content not extracted"
)
PLAIN_TEXT = f"Data centers use water. {QUOTE} in large volumes. End of source."
ANNOTATED_TEXT = f"Data centers use water. {ANNOTATION} {QUOTE} in large volumes."

GAP = PreparationGap(id="U1", kind="figure", page=4, label="Figure 1", image="images/U1_p04.png")


class FakeStructuredModel:
    def __init__(self, responses: list[dict[str, Any]]) -> None:
        self._responses = list(responses)
        self.calls: list[Sequence[BaseMessage]] = []

    def invoke(self, input: Sequence[BaseMessage]) -> dict[str, Any]:
        self.calls.append(input)
        return self._responses.pop(0)


def _provenance() -> Provenance:
    return Provenance(
        source_title="Making AI Less Thirsty",
        source_type="peer_reviewed_paper",
        retrieved_at=datetime.now(UTC),
    )


def _source(text: str = PLAIN_TEXT, *, annotated: bool = False) -> SourceDocument:
    return SourceDocument(
        text=text,
        provenance=_provenance(),
        preparation_directory="outputs/preparation/fixture" if annotated else None,
        preparation_gaps=[GAP] if annotated else [],
    )


def _png(tmp_path: Path, name: str = "U1_p04.png") -> Path:
    """A real 1x1 PNG, so the loader's sniffing and hashing run on real bytes."""
    data = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8AAAwAB/AGLvQAAAABJRU5ErkJggg=="
    )
    path = tmp_path / name
    path.write_bytes(data)
    return path


def _pdf(tmp_path: Path) -> Path:
    path = tmp_path / "source.pdf"
    path.write_bytes(b"%PDF-1.4\n% minimal fixture\n")
    return path


def _crop(tmp_path: Path, gap_id: str = "U1") -> LoadedAttachment:
    _png(tmp_path)
    return load_attachment(
        tmp_path, "U1_p04.png", kind="image", page=4, gap_id=gap_id, label="Figure 1"
    )


def _pdf_attachment(tmp_path: Path) -> LoadedAttachment:
    _pdf(tmp_path)
    return load_attachment(tmp_path, "source.pdf", kind="pdf")


def _extracted(quote: str = QUOTE) -> ExtractedAnalysis:
    return ExtractedAnalysis(
        research_problem={
            "text": "Why do data centers use water?",
            "statement_origin": "author_stated",
        },
        central_claims=[
            ExtractedClaim(
                text="Data centers evaporate freshwater in cooling towers.",
                statement_origin="author_stated",
                evidence=[
                    ExtractedEvidence(
                        text=quote,
                        evidence_form="verbatim",
                        relationship_to_claim="claim_grounding",
                    )
                ],
            )
        ],
    )


def _unreadable() -> dict[str, Any]:
    """The remaining reason for a correction attempt: JSON we could not read."""
    return {
        "raw": AIMessage(
            content="",
            usage_metadata={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150},
        ),
        "parsed": None,
        "parsing_error": ValueError("could not parse model output"),
    }


def _response(parsed: ExtractedAnalysis) -> dict[str, Any]:
    return {
        "raw": AIMessage(
            content="",
            usage_metadata={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150},
        ),
        "parsed": parsed,
        "parsing_error": None,
    }


def _settings(**overrides: Any) -> Settings:
    base: dict[str, Any] = {"openai_api_key": "sk-test"}
    base.update(overrides)
    return Settings(**base)


def _blocks(message: BaseMessage) -> list[dict[str, Any]]:
    assert isinstance(message.content, list)
    return [block for block in message.content if isinstance(block, dict)]


# --- the default text path is untouched -------------------------------------


def test_default_mode_builds_the_same_plain_string_message_as_before() -> None:
    messages = build_messages(_source())
    human = messages[1]
    assert isinstance(human.content, str)
    assert human.content == (
        f"Source title: Making AI Less Thirsty\nSource type: peer_reviewed_paper\n\n{PLAIN_TEXT}"
    )
    assert PDF_INPUT_INSTRUCTIONS not in human.content
    assert CROPS_INPUT_INSTRUCTIONS not in human.content


def test_default_mode_result_keeps_the_prepared_text_only_scope() -> None:
    model = FakeStructuredModel([_response(_extracted())])
    result = analyze_source(_source(), model=model, settings=_settings())
    assert result.input_mode == "prepared_text"
    assert result.analysis_scope == ANALYSIS_SCOPE
    assert result.model_inputs == []


def test_settings_leave_max_output_tokens_unset_by_default() -> None:
    assert _settings().max_output_tokens is None


# --- payload construction ---------------------------------------------------


def test_pdf_mode_sends_the_pdf_and_withholds_the_prepared_text(tmp_path: Path) -> None:
    attachment = _pdf_attachment(tmp_path)
    messages = build_messages(_source(), input_mode="pdf", attachments=[attachment])
    blocks = _blocks(messages[1])
    text = "\n".join(block["text"] for block in blocks if block["type"] == "text")
    assert PLAIN_TEXT not in text
    assert PDF_INPUT_INSTRUCTIONS in text
    files = [block for block in blocks if block["type"] == "file"]
    assert len(files) == 1
    assert files[0]["mime_type"] == "application/pdf"
    assert files[0]["base64"] == attachment.data


def test_crops_mode_sends_the_text_and_one_labelled_image_per_gap(tmp_path: Path) -> None:
    attachment = _crop(tmp_path)
    messages = build_messages(
        _source(ANNOTATED_TEXT, annotated=True),
        input_mode="prepared_text_and_crops",
        attachments=[attachment],
    )
    blocks = _blocks(messages[1])
    text = "\n".join(block["text"] for block in blocks if block["type"] == "text")
    assert ANNOTATED_TEXT in text
    assert CROPS_INPUT_INSTRUCTIONS in text
    assert "preparation gap U1" in text
    assert "Figure 1" in text
    assert "page 4" in text
    images = [block for block in blocks if block["type"] == "image"]
    assert len(images) == 1
    assert images[0]["mime_type"] == "image/png"


def test_system_prompt_is_identical_across_input_modes(tmp_path: Path) -> None:
    text_mode = build_messages(_source())
    pdf_mode = build_messages(_source(), input_mode="pdf", attachments=[_pdf_attachment(tmp_path)])
    crops_mode = build_messages(
        _source(ANNOTATED_TEXT, annotated=True),
        input_mode="prepared_text_and_crops",
        attachments=[_crop(tmp_path)],
    )
    assert text_mode[0].content == pdf_mode[0].content == crops_mode[0].content


def test_blocks_translate_to_the_responses_api_file_and_image_inputs(tmp_path: Path) -> None:
    """Offline payload translation only. No request is made and none is implied."""
    chat = ChatOpenAI(
        model="gpt-6.1-sol",
        reasoning_effort="medium",
        use_responses_api=True,
        max_completion_tokens=24_000,
        api_key=SecretStr("sk-test"),
    )
    messages = build_messages(
        _source(ANNOTATED_TEXT, annotated=True),
        input_mode="prepared_text_and_crops",
        attachments=[_crop(tmp_path)],
    ) + [
        HumanMessage(
            content=[
                {
                    "type": "file",
                    "base64": "QUJD",
                    "mime_type": "application/pdf",
                    "filename": "source.pdf",
                }
            ]
        )
    ]
    payload = chat._get_request_payload(messages)
    types = {
        block["type"]
        for item in payload["input"]
        if isinstance(item.get("content"), list)
        for block in item["content"]
    }
    assert {"input_text", "input_image", "input_file"} <= types
    assert payload["max_output_tokens"] == 24_000
    assert payload["reasoning"]["effort"] == "medium"


# --- attachments survive the correction attempt -----------------------------


def test_correction_attempt_resends_the_attachments(tmp_path: Path) -> None:
    attachment = _crop(tmp_path)
    model = FakeStructuredModel([_unreadable(), _response(_extracted())])
    result = analyze_source(
        _source(ANNOTATED_TEXT, annotated=True),
        model=model,
        settings=_settings(),
        input_mode="prepared_text_and_crops",
        attachments=[attachment],
    )
    assert result.attempt_count == 2
    assert len(model.calls) == 2
    correction = model.calls[1]
    images = [
        block
        for message in correction
        if isinstance(message.content, list)
        for block in message.content
        if isinstance(block, dict) and block.get("type") == "image"
    ]
    assert len(images) == 1
    assert images[0]["base64"] == attachment.data


def test_pdf_correction_attempt_resends_the_pdf(tmp_path: Path) -> None:
    attachment = _pdf_attachment(tmp_path)
    model = FakeStructuredModel([_unreadable(), _response(_extracted())])
    analyze_source(
        _source(),
        model=model,
        settings=_settings(),
        input_mode="pdf",
        attachments=[attachment],
    )
    files = [
        block
        for message in model.calls[1]
        if isinstance(message.content, list)
        for block in message.content
        if isinstance(block, dict) and block.get("type") == "file"
    ]
    assert len(files) == 1
    assert files[0]["base64"] == attachment.data


# --- grounding safeguards are unchanged in every mode -----------------------


def test_text_mode_rejects_attachments(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="sends no attachments"):
        analyze_source(
            _source(),
            model=FakeStructuredModel([]),
            settings=_settings(),
            attachments=[_pdf_attachment(tmp_path)],
        )


def test_pdf_mode_requires_exactly_one_pdf(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="exactly one pdf"):
        validate_attachments("pdf", [], [])
    with pytest.raises(ValueError, match="exactly one pdf"):
        validate_attachments("pdf", [_pdf_attachment(tmp_path), _pdf_attachment(tmp_path)], [])


def test_crops_mode_rejects_a_crop_for_an_undeclared_gap(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="unknown gap ids"):
        validate_attachments("prepared_text_and_crops", [_crop(tmp_path, "T9")], ["U1"])


def test_crops_mode_rejects_an_unlabelled_crop(tmp_path: Path) -> None:
    _png(tmp_path)
    anonymous = load_attachment(tmp_path, "U1_p04.png", kind="image", page=4)
    with pytest.raises(ValueError, match="must name the preparation gap"):
        validate_attachments("prepared_text_and_crops", [anonymous], ["U1"])


def test_crops_mode_rejects_a_pdf(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="at least one image"):
        validate_attachments("prepared_text_and_crops", [_pdf_attachment(tmp_path)], ["U1"])


def test_attachments_over_the_documented_request_limit_are_rejected(tmp_path: Path) -> None:
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


def test_loader_rejects_a_mismatched_file_type(tmp_path: Path) -> None:
    _png(tmp_path)
    with pytest.raises(ValueError, match="expected a .pdf"):
        load_attachment(tmp_path, "U1_p04.png", kind="pdf")


def test_loader_hashes_the_exact_bytes_sent(tmp_path: Path) -> None:
    path = _png(tmp_path)
    attachment = load_attachment(tmp_path, "U1_p04.png", kind="image", gap_id="U1")
    assert attachment.record.byte_size == path.stat().st_size
    assert base64.b64decode(attachment.data) == path.read_bytes()


# --- the saved record describes what was sent -------------------------------


def test_pdf_result_records_its_input_and_scope(tmp_path: Path) -> None:
    attachment = _pdf_attachment(tmp_path)
    model = FakeStructuredModel([_response(_extracted())])
    result = analyze_source(
        _source(),
        model=model,
        settings=_settings(),
        input_mode="pdf",
        attachments=[attachment],
    )
    assert result.input_mode == "pdf"
    assert result.analysis_scope == ANALYSIS_SCOPE_PDF
    assert "page image" in result.analysis_scope
    assert [item.path for item in result.model_inputs] == ["source.pdf"]
    assert result.model_inputs[0].sha256 == attachment.record.sha256


def test_crops_result_records_each_crop_against_its_gap(tmp_path: Path) -> None:
    model = FakeStructuredModel([_response(_extracted())])
    result = analyze_source(
        _source(ANNOTATED_TEXT, annotated=True),
        model=model,
        settings=_settings(),
        input_mode="prepared_text_and_crops",
        attachments=[_crop(tmp_path)],
    )
    assert result.analysis_scope == ANALYSIS_SCOPE_TEXT_AND_CROPS
    assert "unverified" in result.analysis_scope
    assert [item.gap_id for item in result.model_inputs] == ["U1"]
    assert [gap.id for gap in result.preparation_gaps] == ["U1"]
    restored = AnalysisResult.model_validate_json(result.model_dump_json())
    assert restored.model_inputs == result.model_inputs
    assert restored.input_mode == "prepared_text_and_crops"


def test_saved_results_without_the_new_fields_still_load() -> None:
    model = FakeStructuredModel([_response(_extracted())])
    valid = analyze_source(_source(), model=model, settings=_settings())
    payload = json.loads(valid.model_dump_json())
    for field in ("input_mode", "model_inputs"):
        payload.pop(field)
    restored = AnalysisResult.model_validate(payload)
    assert restored.input_mode == "prepared_text"
    assert restored.model_inputs == []
