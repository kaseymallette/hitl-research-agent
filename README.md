# hitl-research-agent

A human-in-the-loop AI research framework for analyzing sources, evaluating arguments, and synthesizing findings across a research collection. The project investigates how AI can support rigorous research while keeping human judgment and intellectual direction central.

> Can AI meaningfully support rigorous, evidence-grounded research?

## Purpose

Researchers are right to be skeptical of AI for synthesis: models misattribute claims, drop qualifications, and cite evidence that doesn't support them. This project builds an analysis process that can be checked at every step. Each document gets a close reading, and each point in its answers is traced to the page it comes from. The analysis is then compared across documents to answer a researcher's questions. It is applied to a real study, done with a professor of literacy education who directs the questions and judges what the evidence means.

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

These cover legislation only. The scholarly articles are being run now.

## How it works

Each document runs through a series of Codex sessions, in order. Each session sees only the files its step needs. There are two harnesses: one for scholarly articles and one for legislation.

### Scholarly articles: does close reading give better answers?

Each article is used to answer three questions:

- How is the science of reading defined, and how is it enacted?
- How is teachers' knowledge positioned?
- How are students positioned?

The harness tests two ways of answering them. Every answer quotes the article's exact words.

- **Null hypothesis:** Method B is no better than Method A.

**1. Claims reference:** every claim in the article, quoted exactly, listed from the article alone. It doesn't know the questions, so it favors neither method.

**Method A: Baseline**

**2.** Answer the questions from the article alone, with quotes.

**Method B: Close Reading**

**3.** Close read the article for the questions, quoting only the relevant passages.<br>
**4.** Answer the questions using the close reading, with quotes.

**5. Scoring:** compare Method A (2) and Method B (4) against the claims reference.

- **Recall:** which relevant claims did each method use, and which did it miss?
- **Precision:** which of each method's quotes are real claims, quoted exactly and relevant, and which aren't?

![Scholarly harness: the article feeds the claims reference (1), Method A's baseline answers (2), and Method B's close reading (3), which feeds the close reading answers (4); scoring (5) compares 2 and 4 against the claims reference.](studies/science_of_reading/assets/scholarly-flow.svg)

```bash
uv run python scripts/run_scholarly.py <slug>
```

[`scripts/run_scholarly.py`](scripts/run_scholarly.py) runs the five steps, in order, for one article from [`data/scholarly/sources.yaml`](studies/science_of_reading/data/scholarly/sources.yaml), each in its own Codex session, and writes five files to `outputs/scholarly/<slug>/`:

| Step | Reads | Writes |
| --- | --- | --- |
| 1. Claims reference | the article | `01_claims_reference.md` |
| 2. Baseline answers | the article | `02_baseline_answers.md` |
| 3. Close reading | the article | `03_close_reading.json` |
| 4. Close Reading answers | the article and the close reading | `04_close_reading_answers.md` |
| 5. Scoring | the article, the claims reference, and both sets of answers | `05_scoring.md` |

No step sees another step's file unless the table says so: the claims reference and the baseline answers never see the close reading. With no option, only the steps whose file is missing run, so a stopped run picks up where it left off; `--only 03` reruns one step. The prompts are in [`harness/scholarly/prompts/`](studies/science_of_reading/harness/scholarly/prompts/), and each session is sent its prompt file exactly as written.

### Legislation: discourse analysis

1. **Close reading** of the law.
2. **Claims reference:** the law's own claims, listed from the law alone.
3. **Judgment of the close reading:** checked against the law and the claims reference.
4. **Discourse analysis:** coded on five critical discourse analysis dimensions: lexical choices and definitional framing (LEX), presuppositions (PRE), foregrounding and silencing (FOS), subject positioning (SUB), and intertextuality (INT).
5. **Judgment of the discourse analysis:** every observation checked against the law, and whether its code fits.

![Legislation harness: the close reading and the claims reference feed the close reading judgment; the discourse analysis, which reads the close reading, feeds the discourse analysis judgment; both judgments go to review, to accept, revise, rerun, or reject.](studies/science_of_reading/assets/legislation-flow.svg)

[`scripts/workspace.py`](scripts/workspace.py) loads one law (its PDF, extracted text, and page images) into a workspace outside the repository, where the five prompts in [`harness/legislation/`](studies/science_of_reading/harness/legislation/) are run in Codex; saving copies the results to `outputs/legislation/<slug>/`. The commands are in the study's [`RUNBOOK.md`](studies/science_of_reading/RUNBOOK.md).

### Design choices

- **The researcher decides.** The framework distinguishes what an author states from what the model infers or evaluates. Every result is recorded, and the expert accepts, revises, reruns, or rejects it; nothing is withheld because an analysis is weak.
- **Only a technical failure stops a run:** Codex exiting with an error or timing out, a step's file not written, or a close reading that isn't valid JSON.
- **Why Codex.** Blind head-to-head A/B tests chose GPT-6.1 Sol at medium effort, reading the PDF, run through Codex ([details](https://github.com/kaseymallette/hitl-research-agent/blob/b887401/studies/water/README.md#the-ab-experiments)). It beat a costlier model and extracted text, and Codex runs within the ChatGPT plan, with no API key.

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
- **In progress:** the scholarly corpus. Reinking, Hruby, & Risko (2023) is done; the other seven articles in `studies/science_of_reading/data/scholarly/sources.yaml` are running.
- **Next:** the popular press.

Decisions and open questions are in [`docs/PROJECT.md`](docs/PROJECT.md).

## Layout

```
├── docs/
│   ├── PROJECT.md                 the questions, current decisions, and status
│   └── ENGINEERING_DIRECTIVES.md  the coding baseline
├── studies/
│   └── science_of_reading/        the study: corpora, codebook, prompts, results, and answered questions
├── scripts/
│   ├── run_scholarly.py           the scholarly harness: five Codex sessions per article
│   └── workspace.py               legislation: load a law into the Codex workspace, save its results
├── src/hitl_research_agent/       the data models for a source's provenance
└── tests/
```

Earlier versions are kept as tags: `v1-final`, and `v2-final` (the A/B
experiments, the decision records, the prompt log, and the API pipeline). The
science of reading study was developed separately and is kept as `mom-research-final`.
The water study, where the analysis harness was built, and the retrieval
experiments are in git history and on the `wip-2026-11-25` branch.

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
