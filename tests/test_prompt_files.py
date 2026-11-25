"""The science of reading workspace holds copies of the rubric and prompts; they must not drift."""

from pathlib import Path

STUDY = Path(__file__).resolve().parents[1] / "studies" / "science_of_reading"


def test_the_evaluations_workspace_copies_match_their_originals() -> None:
    """evaluations/ is copied out of the repository for judging, so it holds
    its own copies of the rubric and prompts; they must match the originals."""
    copies = {
        "evaluations/RUBRIC.md": "docs/RUBRIC.md",
        "evaluations/prompts/close-reading.md": "prompts/close-reading.md",
        "evaluations/prompts/evaluate-argument.md": "prompts/evaluate-argument.md",
    }
    for copy, original in copies.items():
        assert (STUDY / copy).read_bytes() == (STUDY / original).read_bytes(), copy
