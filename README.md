# mom-research

A workspace branch of `hitl-research-agent` for running single-source
analyses on a set of articles. It is an orphan branch: it shares no history
with `main` and is not merged back. Changes worth keeping on `main`, such as
edits to the rubric or prompts, are carried over by hand.

```
├── data/
│   ├── epoch-1/          articles and their source details
│   ├── epoch-2/
│   └── epoch-3/
├── evaluations/          the workspace for one article's run; see evaluations/README.md
├── outputs/              results copied out of evaluations/, per article
├── scripts/              this branch's own code, such as loading an article into evaluations/
├── src/                  the hitl_research_agent package from main, unchanged
├── prompts/              the prompt originals; evaluations/prompts/ must match them
├── docs/RUBRIC.md        the rubric original; evaluations/RUBRIC.md must match it
└── tests/                tests for src/ and the prompt and rubric copies
```

Checks: `uv run pytest` · `uv run ruff check . && uv run ruff format --check .` · `uv run mypy src`
