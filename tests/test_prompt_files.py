"""prompts/ holds the prompts as agent instruction files; they must not drift."""

from pathlib import Path

from hitl_research_agent.prompts import (
    EVALUATION_INPUT_NOTES,
    EVALUATION_PROMPT,
    PDF_INPUT_INSTRUCTIONS,
    SYSTEM_PROMPT,
)

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
