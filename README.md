# hitl-research-agent

A human-in-the-loop research system: three agents that prepare evidence for a
human researcher, and a separate evaluation step that says how much to trust
what they produced.

> Increase the amount and quality of evidence a researcher can reason over,
> without replacing human judgment.

## The three agents

**Single-source analysis** turns one article into a structured JSON analysis —
research problem, central claims, supporting evidence, methodology,
assumptions, limitations, proposed solutions, open questions, and source-level
provenance. It is *question-independent*: it never receives a research
question, so the analysis stays reusable for questions no one has asked yet.

**Synthesis** compares analyses across sources for agreements, disagreements,
methodological differences, limitations, and open questions, preserving which
source said what.

**Research** finds articles relevant to an explicit research question, explains
why each is relevant, and leaves the decision to add any of them to the
researcher.

## What the analysis records

Every interpreted element carries `statement_origin`, so the analysis stays
split in two everywhere it matters:

| Author-stated | Model-inferred |
| --- | --- |
| the research problem as the source frames it | the problem as the model reconstructs it |
| claims the source makes | claims the model synthesizes from it |
| assumptions the authors state | assumptions the model finds the argument needs |
| limitations the authors acknowledge | limitations the model identifies |

Proposed solutions, open questions, and the methodology record carry the same
label. Evidence carries a second, independent split: `verbatim` for an exact
quotation from the source, `paraphrased` for the model's own words — and a
faithful paraphrase is a correct answer, never a lesser one than a quotation.

Citations record what the source itself cites, extracted from the document and
not retrieved or fact-checked. The goal is argument reconstruction and evidence
extraction, not summarization.

## Workflow

```
article + prompt → model → JSON → separate evaluation → accept · reject · revise · rerun
```

Evaluation is a separate step, not a gate. No quality check blocks the JSON
from being returned: a paraphrase, a missing evidence label, or a thin claim is
something for evaluation and human review to report, not a reason to withhold
the analysis. Only a technical failure — an API error, an unreadable response —
stops a run.

### What evaluation measures

DeepEval targets named behaviors, not a general impression of quality:

| Question | Behavioral axes |
| --- | --- |
| Do author-attributed claims reflect the source? | source faithfulness, argument reconstruction |
| Are qualifications and citations preserved? | citation faithfulness, evidence mapping |
| Are model interpretations distinguished? | assumption discipline, limitation discipline, inference control |
| Are important arguments covered? | argument reconstruction, research usefulness |

The judge is evaluated too: the researcher scores a sample independently and
the two are compared, so the judge's reliability is measured rather than
assumed.

### Human review

The researcher is not a reader at the end of a pipeline — they operate the gate
that decides what enters the research store. After analysis and evaluation they
see the structured analysis, its supporting citations, the evaluation scores,
and the evaluation's explanations, and then:

**accept → reject → revise → rerun**

Only accepted analyses enter the store. Interpretation, inference, deciding
what matters, and choosing the next research direction stay with the
researcher.

## Research question

> Why does AI infrastructure use freshwater, and under what conditions could
> alternative cooling methods or water supplies — including desalination —
> reduce pressure on local freshwater resources?

The investigation distinguishes freshwater, drinking-quality water, and water
suitable for a particular process, and examines desalination as a possible
supply option without assuming it is the preferred solution. These distinctions
are load-bearing: collapsing them is the first way a retrieval or relevance
judgment goes wrong.

The source collection is 16 articles in [`data/research/`](data/research), four
of which are the A/B experiment set in
[`data/research/ab_testing/`](data/research/ab_testing).

## Phases

| Phase | What it does |
| --- | --- |
| 0 | **Review and redesign** — audit the v1 code, restructure the repository and documentation around these phases |
| 1 | **A/B testing** — 4 articles × {full PDF, extracted text + crops} × {GPT-6.1 Sol medium, GPT-6 Astra low} = 16 analyses, with usage, cost, runtime, and preparation effort recorded |
| 2 | **DeepEval** — rubrics for the axes above, applied to the 16 analyses, with human spot checks of the judge; choose the model and input method |
| 3 | **Research collection** — analyze and evaluate all 16 articles with the chosen configuration, reusing suitable experiment outputs |
| 4 | **Synthesis agent** — compare sources, with its own evaluation design |
| 5 | **Research agent** — find relevant articles for explicit research questions |
| 6 | **RAG** — retrieval across sources, analyses, evaluations, and syntheses |

Phase 1 holds the analysis prompt and output structure constant so that input
method and model are the only things that vary.

See the [build plan](docs/BUILD_PLAN.md) for the detail, including what v1 code
each phase reuses, simplifies, or removes.

## Status

**Phase 0 — in progress.** The v1 single-source analysis pipeline works end to
end and returns JSON without quality gates; it is the starting point for Phase
1. Evaluation, synthesis, research, and retrieval are not built.

v1 experiment outputs are kept for history in
[`outputs/v1_archive/`](outputs/v1_archive) and are not part of the Phase 1
results.

## Stack

Python 3.12 · LangChain + OpenAI Responses API · Pydantic · PyMuPDF ·
DeepEval *(Phase 2)* · embeddings and retrieval *(Phase 6)* · uv · Ruff · mypy ·
pre-commit · GitHub Actions · Claude Code

## How this is built

Two AI tools, with a deliberate division of labor: **Claude Code** is
responsible for all of the code, and **Codex** helps with design and prompt
writing. Neither decides what to research or what the evidence means.

The [prompt log](docs/prompt_log.md) records that collaboration — one file per
phase, holding the prompts as given and what came back, including what was
claimed but never independently checked — so the reasoning behind the project's
structure stays visible alongside the code it produced.

## Documentation

- [Build Plan](docs/BUILD_PLAN.md) — the phases in engineering detail
- [Prompt Log](docs/prompt_log.md) — one log per phase

## Setup

**Prerequisites:** [uv](https://docs.astral.sh/uv/) (manages Python 3.12
itself) and git 2.31+.

```bash
brew install uv
uv sync
uv run pre-commit install
```

Set `OPENAI_API_KEY` in `.env` (see [`.env.example`](.env.example)).

### Checks

```bash
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy src
```

## Why this project

Most descriptions of AI research assistants ask how much autonomy a model can
be given. This one asks how much useful research work AI can do while the
researcher keeps interpretation, inference, and intellectual direction — not to
replace the researcher, but to build a better research instrument.
