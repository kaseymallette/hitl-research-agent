"""Model-input attachments: the original PDF, or the retained element crops.

An attachment is content the *model* receives in addition to, or instead of,
the prepared source text. It is never part of the grounding reference: the
verbatim-evidence, citation-marker, and reference-entry checks continue to
match only against the declared source text, so nothing the model reads from
a PDF page or from a crop can pass as a verbatim quotation. Anything the model
reports from an image is paraphrased evidence with a page/crop locator, and is
unverified until a human checks it against the original image.

Blocks are emitted in LangChain's standard multimodal shape, which
`langchain-core` translates to the Responses API's `input_file` / `input_image`.
"""

import base64
import hashlib
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from pydantic import Field

from ..models._base import NonEmptyStr, ResearchBaseModel

InputMode = Literal["prepared_text", "prepared_text_and_crops", "pdf"]

# OpenAI documents a 50 MB combined limit for files in one request.
MAX_REQUEST_FILE_BYTES = 50 * 1024 * 1024

PDF_MIME_TYPE = "application/pdf"
IMAGE_MIME_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


class Attachment(ResearchBaseModel):
    """What was sent with a request, recorded for audit.

    The bytes themselves are not stored here — only the path they were read
    from and their sha256, so a saved result names its exact inputs without
    embedding them.
    """

    kind: Literal["pdf", "image"]
    path: NonEmptyStr  # repository-relative
    mime_type: NonEmptyStr
    sha256: NonEmptyStr
    byte_size: int = Field(ge=1)
    page: int | None = Field(default=None, ge=1)
    gap_id: str | None = Field(
        default=None, description="The preparation gap this crop was retained for."
    )
    label: str | None = None


@dataclass(frozen=True)
class LoadedAttachment:
    """An `Attachment` together with the base64 payload sent to the model."""

    record: Attachment
    data: str

    def content_blocks(self) -> list[dict[str, Any]]:
        """The identifying text block and the data block, in that order.

        The text block tells the model what it is looking at and how to locate
        it again. It is not source text and is not in the grounding reference,
        so quoting it verbatim fails grounding like any other non-source text.
        """
        record = self.record
        if record.kind == "pdf":
            return [
                {
                    "type": "text",
                    "text": (
                        f"The complete original source PDF is attached ({record.path}). "
                        "It is the only source content supplied for this analysis."
                    ),
                },
                {
                    "type": "file",
                    "base64": self.data,
                    "mime_type": record.mime_type,
                    "filename": Path(record.path).name,
                },
            ]
        parts = [f"Retained source image for preparation gap {record.gap_id}"]
        if record.label:
            parts.append(f"labelled {record.label} in the source")
        if record.page is not None:
            parts.append(f"on page {record.page}")
        parts.append(f"file {record.path}")
        return [
            {"type": "text", "text": ", ".join(parts) + "."},
            {"type": "image", "base64": self.data, "mime_type": record.mime_type},
        ]


def load_attachment(
    repo_root: Path,
    relative_path: str,
    *,
    kind: Literal["pdf", "image"],
    page: int | None = None,
    gap_id: str | None = None,
    label: str | None = None,
) -> LoadedAttachment:
    """Read one attachment from disk, hashing exactly the bytes that are sent."""
    path = repo_root / relative_path
    raw = path.read_bytes()
    if not raw:
        raise ValueError(f"attachment is empty: {relative_path}")
    suffix = path.suffix.lower()
    if kind == "pdf":
        if suffix != ".pdf":
            raise ValueError(f"expected a .pdf attachment, got {relative_path}")
        mime_type = PDF_MIME_TYPE
    else:
        if suffix not in IMAGE_MIME_TYPES:
            raise ValueError(f"unsupported image type for attachment: {relative_path}")
        mime_type = IMAGE_MIME_TYPES[suffix]
    return LoadedAttachment(
        record=Attachment(
            kind=kind,
            path=relative_path,
            mime_type=mime_type,
            sha256=hashlib.sha256(raw).hexdigest(),
            byte_size=len(raw),
            page=page,
            gap_id=gap_id,
            label=label,
        ),
        data=base64.b64encode(raw).decode("ascii"),
    )


def validate_attachments(
    input_mode: InputMode,
    attachments: Sequence[LoadedAttachment],
    declared_gap_ids: Sequence[str],
) -> None:
    """Reject an input that does not match the declared input mode.

    These are programming errors in a caller, not model failures, so they raise
    ValueError rather than entering the analysis failure categories.
    """
    kinds = [item.record.kind for item in attachments]
    if input_mode == "prepared_text":
        if attachments:
            raise ValueError("input_mode 'prepared_text' sends no attachments")
    elif input_mode == "pdf":
        if kinds != ["pdf"]:
            raise ValueError("input_mode 'pdf' requires exactly one pdf attachment")
    else:
        if not attachments or set(kinds) != {"image"}:
            raise ValueError(
                "input_mode 'prepared_text_and_crops' requires at least one image "
                "attachment and no other kind"
            )
        if any(item.record.gap_id is None for item in attachments):
            raise ValueError("every crop must name the preparation gap it was retained for")
        declared = set(declared_gap_ids)
        unknown = sorted(
            str(item.record.gap_id) for item in attachments if item.record.gap_id not in declared
        )
        if unknown:
            raise ValueError(
                "every crop must name a preparation gap declared on the source document; "
                f"unknown gap ids: {unknown}"
            )
    total = sum(item.record.byte_size for item in attachments)
    if total > MAX_REQUEST_FILE_BYTES:
        raise ValueError(
            f"attachments total {total} bytes, over the documented "
            f"{MAX_REQUEST_FILE_BYTES}-byte per-request limit"
        )
