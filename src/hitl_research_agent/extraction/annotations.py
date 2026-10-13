"""Preparation annotations: the reserved syntax and the grounding view.

A preparation annotation marks material the preparation step could not extract
faithfully (a figure, a diagram, an equation, an uncertain table). It is shown
to the analyzer so the analyzer knows content is missing, but it is **not source
text** and must never match as verbatim evidence, a citation marker, or a
reference entry.

The grounding checks therefore run against a *grounding view* of the source in
which every annotation is replaced by a single sentinel character. Replacement
(not deletion) keeps the text on either side of an annotation from becoming
adjacent, so a quotation cannot match across the gap.
"""

import re
from dataclasses import dataclass

ANNOTATION_OPEN = "⟦"  # ⟦
ANNOTATION_CLOSE = "⟧"  # ⟧
ANNOTATION_PREFIX = "PREP-ANNOTATION"
# A private-use character: not whitespace and unchanged by casefold(), so it
# survives the whitespace/case normalization the grounding checks apply and
# keeps the text on either side of an annotation from becoming adjacent.
SENTINEL = ""

_ANNOTATION_RE = re.compile(
    re.escape(ANNOTATION_OPEN)
    + re.escape(ANNOTATION_PREFIX)
    + r" (?P<id>[A-Za-z0-9_\-]+)[^"
    + re.escape(ANNOTATION_OPEN + ANNOTATION_CLOSE)
    + r"]*"
    + re.escape(ANNOTATION_CLOSE)
)
_RESERVED = (ANNOTATION_OPEN, ANNOTATION_CLOSE, SENTINEL)


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


def grounding_view(text: str) -> str:
    """`text` with each annotation replaced by one sentinel character."""
    return _ANNOTATION_RE.sub(SENTINEL, text)


def contains_reserved_character(value: str) -> bool:
    """Whether a model-produced string contains annotation delimiters or the
    sentinel — never legitimate in a quotation, marker, or reference entry."""
    return any(char in value for char in _RESERVED)


def reserved_character_problems(text: str) -> list[str]:
    """Problems that make `text` unsafe as source text: delimiters outside a
    well-formed annotation, or the sentinel itself."""
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
