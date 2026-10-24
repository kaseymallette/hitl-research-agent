"""docs/PROMPTS.md is the readable copy of the prompts; it must not drift."""

from pathlib import Path

from hitl_research_agent.prompts import (
    CROPS_INPUT_INSTRUCTIONS,
    EVALUATION_INPUT_NOTES,
    EVALUATION_PROMPT,
    PDF_INPUT_INSTRUCTIONS,
    PRIMER_PROMPT,
    SYSTEM_PROMPT,
)

DOC = (Path(__file__).resolve().parents[1] / "docs" / "PROMPTS.md").read_text(encoding="utf-8")


def test_the_prompts_document_holds_every_prompt_exactly_as_the_code_sends_it() -> None:
    texts = {
        "SYSTEM_PROMPT": SYSTEM_PROMPT,
        "EVALUATION_PROMPT": EVALUATION_PROMPT,
        "PDF_INPUT_INSTRUCTIONS": PDF_INPUT_INSTRUCTIONS,
        "PRIMER_PROMPT": PRIMER_PROMPT,
        "CROPS_INPUT_INSTRUCTIONS": CROPS_INPUT_INSTRUCTIONS,
        **{
            f"EVALUATION_INPUT_NOTES[{mode}]": note for mode, note in EVALUATION_INPUT_NOTES.items()
        },
    }
    stale = [name for name, text in texts.items() if text.strip() not in DOC]
    assert not stale, f"docs/PROMPTS.md is out of date for: {', '.join(stale)}"


ROOT = Path(__file__).resolve().parents[1]


def test_the_agent_prompt_files_carry_the_prompts_the_code_sends() -> None:
    """prompts/ is what an agent such as Codex follows; its prompt text must
    be the API's, so an agent run differs only in how it is run."""
    close = (ROOT / "prompts" / "close-reading.md").read_text(encoding="utf-8")
    evaluate = (ROOT / "prompts" / "evaluate-argument.md").read_text(encoding="utf-8")
    assert SYSTEM_PROMPT.strip() in close
    assert PDF_INPUT_INSTRUCTIONS.strip() in close
    assert EVALUATION_PROMPT.strip() in evaluate
    assert EVALUATION_INPUT_NOTES["pdf"] in evaluate
