# hitl-research-agent

A human-in-the-loop AI research framework for analyzing sources, evaluating arguments, and synthesizing findings across a research collection. The project investigates how AI can support rigorous research while keeping human judgment and intellectual direction central.

> Can AI meaningfully support rigorous, evidence-grounded research?

## Purpose

Researchers are right to be skeptical of AI for synthesis: models misattribute claims, drop qualifications, and cite evidence that doesn't support them. This project builds an analysis process that can be checked at every step. Each document gets a close reading, and a separate session judges that reading against the source. The analysis is then compared across documents to answer a researcher's questions. It is applied to a real study, done with a professor of literacy education who directs the questions and judges what the evidence means.

## Overview

I’m building this framework to become a better researcher: to work through more literature, make connections across sources, and pursue questions I might otherwise miss. I want AI to help me evaluate the authors’ arguments: whether their evidence supports their claims, whether their methods justify their conclusions, and what assumptions or limitations affect those conclusions.

### Judging the judge

But before I can rely on AI to judge an argument, I need to judge AI. When using models to summarize and analyze articles, I’ve noticed that they can misattribute claims, leave out important qualifications, or attach evidence that does not support their interpretations. This project therefore evaluates both how faithfully the model represents a source and how well it reasons about the authors’ claims. I need to know whether its assessment helps me understand the argument or gives me errors to correct.

### AI as a research assistant?

The justification to use AI to support research still needs to be made, and that is what this system is for.

> Why use AI when I can read the articles and evaluate the authors' arguments myself?

The AI agents need to add something worthwhile, whether that is helping me compare explanations, noticing conflicting evidence, or identifying an assumption worth investigating. *Does this system help me conduct better research that justifies the time and money spent to build and implement it?* *Will I use it to support my research consistently?*

## The science of reading study

The [science of reading study](studies/science_of_reading/) is a collaboration with a professor of literacy education. It examines how the science of reading is defined, simplified, and contested as it moves from scholarship, through the popular press, into state legislation, using critical discourse analysis across the three corpora.

Working title: *Science by Other Means: Reading Research, Legislative Mandates, and the Spaces Between*

In research, the science of reading is broad: the idea that there is a scientific basis for how we teach reading. By the time it reaches legislation, it is often reduced to directives such as "phonics first" or "don't use three-cueing." The study traces that pathway and where things are lost in translation. It does not evaluate whether any approach to reading instruction is effective.

## Findings so far: six state laws

Six laws have been analyzed and judged: California AB 1454 (2025), Arkansas's Right to Read Act (2017) and its 2025 code, Ohio (2026), Georgia HB 1193 (2026), and Minnesota's Read Act (2026). Three of the expert's questions are answered from those analyses:

- **[How is the science of reading defined?](studies/science_of_reading/questions/01_how_is_the_science_of_reading_defined.md)** Only Ohio and Arkansas 2025 define it outright, and differently: Ohio as a body of evidence, Arkansas as a field of study. The other laws give it content through a list of instructional components, a manner of teaching ("explicit, systematic"), or a ban on three-cueing.
- **[How is teachers' knowledge positioned?](studies/science_of_reading/questions/02_how_is_teachers_knowledge_positioned.md)** As something the state must verify, update, and supervise, through credentials, required training, and fidelity checks. No law says outright that teachers lack the knowledge, and most also owe them support.
- **[How are students positioned?](studies/science_of_reading/questions/03_how_are_students_positioned.md)** As beneficiaries of required intervention and as objects of measurement and placement. The laws divide on retention, and range from treating English learners as exceptions to treating their home languages as assets. Students never speak or act.

These cover legislation only. The scholarly corpus is next.

## How it works

Each document runs through five Codex sessions, in order:

1. **Close reading:** the argument step by step, with what each step claims and its support.
2. **Claims reference:** what the document itself claims or provides.
3. **Judgment of the close reading:** checked against the document.
4. **Discourse analysis:** coded on five critical discourse analysis dimensions: lexical choices and definitional framing (LEX), presuppositions (PRE), foregrounding and silencing (FOS), subject positioning (SUB), and intertextuality (INT).
5. **Judgment of the discourse analysis:** every observation checked against the document, and whether its code fits.

The framework distinguishes what an author states from what the model infers or evaluates. Human review determines which analyses enter the research collection.

![Single source analysis: the close reading and the claims reference feed the close reading judgment; the argument evaluation feeds the argument judgment; both judgments go to review, to accept, revise, rerun, or reject.](studies/water/assets/single-source-flow.svg)

The design choices:

- **Independent sessions.** [`scripts/workspace.py`](scripts/workspace.py) loads one document (its PDF, extracted text, and page images) into a workspace outside the repository, so no session sees other runs or judgments. Saving copies the results to `outputs/<corpus>/<slug>/` and clears the workspace for the next one.
- **The prompts are the requests.** Each session gets its prompt file from [`studies/science_of_reading/prompts/`](studies/science_of_reading/prompts/) exactly as written.
- **The researcher decides.** The judgments are recorded, and the expert accepts or revises; nothing is withheld because an analysis is weak.
- **Why Codex.** Blind head-to-head A/B tests chose GPT-6.1 Sol at medium effort, reading the PDF, run through Codex ([details](studies/water/README.md#the-ab-experiments)). It beat a costlier model and extracted text, and Codex runs within the ChatGPT plan.

The commands for each run are in the study's [`RUNBOOK.md`](studies/science_of_reading/RUNBOOK.md).

## Development approach and lessons

Two coding assistants helped me build this project.

- **Claude Code** is responsible for all of the code.
- **Codex** helps with design and prompt writing.

Neither decides what I research or what the evidence means.

What has been difficult about working this way:

- Each implementation step produced the next step’s problem, and the design
  grew to absorb every one. A safeguard added for one failure became the thing
  the next step had to work around. The accumulated machinery eventually cost
  more than the failures it caught, and removing it took longer than building
  it had.
- The architecture drifted without my deciding it should. No single step chose
  to turn quotation matching into a hard acceptance gate, but it arrived there
  across many small changes that each looked reasonable at the time, and the
  direction was only visible in aggregate.
- The coding assistants did not consistently follow my instructions. I had to repeat requirements, correct assumptions, and undo changes I had not asked for. That took time and money away from the research and made supervising the assistants a substantial part of the work.

## Status

- **Done:** six state laws analyzed and judged; the codebook revised from them; three of the expert's questions answered.
- **Next:** the scholarly corpus (the expert's articles are listed in `studies/science_of_reading/data/scholarly/sources.yaml`), then the popular press.

Decisions and open questions are in [`docs/PROJECT.md`](docs/PROJECT.md).

## Layout

```
├── docs/
│   ├── PROJECT.md                 the questions, current decisions, and status
│   └── ENGINEERING_DIRECTIVES.md  the coding baseline
├── studies/
│   ├── science_of_reading/        the study: corpora, codebook, prompts, results, and answered questions
│   ├── water/                     earlier work, where the analysis harness was built
│   └── literacy_pilot/            earlier work: a retrieval comparison, not continued
├── scripts/
│   ├── workspace.py               load a document into the Codex workspace, save its results
│   ├── prepare_sources.py         extracts a PDF's text, tables, and figure crops
│   └── run_single_source.py, build_index.py, answer.py, pool.py   earlier work
├── src/hitl_research_agent/       the data models and input handling prepare_sources.py uses
└── tests/
```

Earlier versions are kept as tags: `v1-final`, and `v2-final` (the A/B
experiments, the decision records, the prompt log, and the API pipeline). The
science of reading study was developed separately and is kept as `mom-research-final`.

## Setup and checks

```bash
uv sync
```

```bash
uv run pytest
```

```bash
uv run ruff check . && uv run ruff format --check .
```

```bash
uv run mypy src
```
