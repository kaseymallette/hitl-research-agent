"""What the model receives: the three input modes, their attachments, and the
syntax marking material that preparation could not extract.

An attachment is content the model gets in addition to, or instead of, the
prepared text. Anything the model reports from a PDF page or a crop is its
reading of an image, recorded as paraphrased and naming the figure or table it
came from, and unverified until a human checks it against the original.

Blocks are emitted in LangChain's standard multimodal shape, which
`langchain-core` translates to the Responses API's `input_file` / `input_image`.
"""

import base64
import hashlib
import re
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

InputMode = Literal["prepared_text", "prepared_text_and_crops", "pdf"]

# OpenAI documents a 50 MB combined limit for files in one request.
MAX_REQUEST_FILE_BYTES = 50 * 1024 * 1024

PDF_MIME_TYPE = "application/pdf"
IMAGE_MIME_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


# --------------------------------------------------------------------------- annotations

ANNOTATION_OPEN = "⟦"
ANNOTATION_CLOSE = "⟧"
ANNOTATION_PREFIX = "PREP-ANNOTATION"

_ANNOTATION_RE = re.compile(
    re.escape(ANNOTATION_OPEN)
    + re.escape(ANNOTATION_PREFIX)
    + r" (?P<id>[A-Za-z0-9_\-]+)[^"
    + re.escape(ANNOTATION_OPEN + ANNOTATION_CLOSE)
    + r"]*"
    + re.escape(ANNOTATION_CLOSE)
)
_RESERVED = (ANNOTATION_OPEN, ANNOTATION_CLOSE)


@dataclass(frozen=True)
class AnnotationSpan:
    annotation_id: str
    start: int
    end: int


def find_annotations(text: str) -> list[AnnotationSpan]:
    """Every well-formed annotation in `text`, with its character offsets."""
    return [
        AnnotationSpan(match.group("id"), match.start(), match.end())
        for match in _ANNOTATION_RE.finditer(text)
    ]


def reserved_character_problems(text: str) -> list[str]:
    """Problems that make `text` unsafe as source text: annotation delimiters
    appearing outside a well-formed annotation."""
    remainder = _ANNOTATION_RE.sub("", text)
    return [
        f"source text contains the reserved character {char!r} outside a well-formed "
        "preparation annotation"
        for char in _RESERVED
        if char in remainder
    ]


def format_annotation(annotation_id: str, fields: dict[str, str], note: str) -> str:
    """Build one well-formed annotation. The note carries no values and no
    interpretation of the missing content; callers pass a fixed phrase."""
    parts = [annotation_id] + [f"{key}={value}" for key, value in fields.items()]
    body = " ".join(parts) + ": " + note
    annotation = f"{ANNOTATION_OPEN}{ANNOTATION_PREFIX} {body}{ANNOTATION_CLOSE}"
    if reserved_character_problems(annotation) or not _ANNOTATION_RE.fullmatch(annotation):
        raise ValueError(f"Annotation fields contain reserved characters: {annotation!r}")
    return annotation


# --------------------------------------------------------------------------- attachments


@dataclass(frozen=True)
class Attachment:
    """What was sent with a request, recorded for audit.

    The bytes are not stored — only the path they came from and their sha256,
    so a saved result names its exact inputs without embedding them.
    """

    kind: Literal["pdf", "image"]
    path: str  # repository-relative
    mime_type: str
    sha256: str
    byte_size: int
    page: int | None = None
    gap_id: str | None = None
    label: str | None = None

    def as_record(self) -> dict[str, Any]:
        """The audit form saved in a run record."""
        return {
            "kind": self.kind,
            "path": self.path,
            "mime_type": self.mime_type,
            "sha256": self.sha256,
            "byte_size": self.byte_size,
            "page": self.page,
            "gap_id": self.gap_id,
            "label": self.label,
        }


@dataclass(frozen=True)
class LoadedAttachment:
    """An `Attachment` together with the base64 payload sent to the model."""

    record: Attachment
    data: str

    def content_blocks(self) -> list[dict[str, Any]]:
        """The identifying text block and the data block, in that order.

        The text block tells the model what it is looking at and how to locate
        it again. It is not source text.
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

    These are caller mistakes, not model failures, so they raise ValueError
    rather than entering the analysis failure categories.
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
