"""Preparation annotations: the reserved syntax used to mark missing material.

A preparation annotation marks material the preparation step could not extract
faithfully (a figure, a diagram, an equation, an uncertain table). It is shown to
the analyzer so the analyzer knows content is missing, and it is **not source
text**: it carries no values and no interpretation of what it stands in for.
"""

import re
from dataclasses import dataclass

ANNOTATION_OPEN = "⟦"  # ⟦
ANNOTATION_CLOSE = "⟧"  # ⟧
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
    """Build one well-formed annotation. The note must contain no values or
    interpretation of the missing content; callers pass a fixed phrase."""
    parts = [annotation_id] + [f"{key}={value}" for key, value in fields.items()]
    body = " ".join(parts) + ": " + note
    annotation = f"{ANNOTATION_OPEN}{ANNOTATION_PREFIX} {body}{ANNOTATION_CLOSE}"
    if reserved_character_problems(annotation) or not _ANNOTATION_RE.fullmatch(annotation):
        raise ValueError(f"Annotation fields contain reserved characters: {annotation!r}")
    return annotation
