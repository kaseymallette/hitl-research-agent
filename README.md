# hitl-research-agent

A human-in-the-loop multi-agent research framework for building and examining a collection of evidence across articles. Three AI agents handle these tasks: single source analysis, synthesis, and literature review, giving researchers a way to examine individual arguments and understand how they relate across a research collection.

The analyses connect authors’ claims to their evidence, methods, assumptions, and limitations, while making the model’s own interpretations explicit. A separate evaluation step will check whether those analyses faithfully represent the sources and whether their assessments of the authors’ arguments are justified. Researchers will review the results before adding them to their collection and use that collection to investigate disagreements, gaps, and new questions.

## Purpose

I’m building this framework to become a better researcher: to work through more literature, make connections across sources, and pursue questions I might otherwise miss. I want AI to help me evaluate the authors’ arguments: whether their evidence supports their claims, whether their methods justify their conclusions, and what assumptions or limitations affect those conclusions.

But before I can rely on AI to judge an argument, I need to judge AI. When using models to summarize and analyze articles, I’ve noticed that they can misattribute claims, leave out important qualifications, or attach evidence that does not support their interpretations. This project therefore evaluates both how faithfully the model represents a source and how well it reasons about the authors’ claims. I need to know whether its assessment helps me understand the argument or gives me errors to correct.

### AI as a research assistant?

The justification to use AI to support research still needs to be made, and that is what this system is for.

> Why use AI when I can read the articles and evaluate the authors' arguments myself?

The AI agents need to add something worthwhile, whether that is helping me compare explanations, noticing conflicting evidence, or identifying an assumption worth investigating. *Does this system help me conduct better research that justifies the time and money spent to build and implement it?* *Will I use it to support my research consistently?*


## Research

This framework is intended to support research across different topics. My starting point is a broader investigation into how we can build AI better, with this first question focused on the infrastructure that supports it and the water it uses. As that investigation develops, I want to build on the evidence already collected and pursue new questions.

### Pilot study

> Why does AI infrastructure use freshwater, and under what conditions could
> alternative cooling methods or water supplies, including desalination, reduce
> pressure on local freshwater resources?

The investigation distinguishes freshwater, drinking-quality water, and water
suitable for a particular process, and examines desalination as a possible
supply option rather than assuming it is the preferred one. These distinctions
matter for relevance: a source about process-grade cooling water is not
evidence about drinking water, and treating them as the same thing is the first
way a judgment about relevance goes wrong.

The source collection is 16 articles in [`data/research/`](data/research), three
of which are the experiment set in
[`data/research/ab_testing/`](data/research/ab_testing).

I collected the 16 articles for this pilot study myself, using the research question to identify relevant sources. The planned literature review agent will assist with that work by finding candidate articles and explaining their relevance for me to review. Single source analysis and synthesis remain question-independent so their outputs can support other research questions as the collection grows.


## Design

### How the system supports the researcher

Three agents do the preparatory work.

| Agent | Given | Produces |
| --- | --- | --- |
| **Single source analysis** | one article | two readings of it: a close reading, which follows the article step by step and records the author's claims and what each step is doing, and an argument evaluation, the model's own judgment of the argument |
| **Synthesis** | several accepted analyses | a cross-source comparison of agreements, disagreements, methodological differences, limitations, and open questions, with each position still attributed to its source |
| **Literature review** | an explicit research question | candidate articles with an explanation of why each one is relevant |

Neither single source analysis nor synthesis receives a research question, so
their output stays useful for questions I have not asked yet. Synthesis
compares what the sources say to each other, not to a question. Only the
literature review agent sees a question, and it only proposes articles.

```
article → close reading → argument evaluation → evaluation of both → accept · reject · revise · rerun
```

The planned review workflow will present both readings, the citations
supporting them, the evaluation scores, and the evaluation's explanation of
those scores. Evaluation will inform my review rather than replacing it, and it
will not act as a gate. A paraphrase, a claim with no support, or a thin reading
gets reported rather than withheld, because I want to see the analysis and
judge it myself. Only a technical failure stops a run: an API error, an
unreadable response, or output that will not parse.

The decision stays with me. I accept, reject, revise, or rerun, and only
accepted analyses enter the research collection. The agents interpret sources
and assess arguments. I review those assessments, decide which conclusions
are justified, and choose what to pursue next.

### Single source analysis: two readings

Reading an argument well asks for two different things, and in one prompt each
got in the way of the other. Recording what an author says takes restraint:
report it faithfully, and keep your own view out of it. Judging the argument
takes the opposite: reason independently, question whether the conclusions
follow, and say what you think. So single source analysis is two calls, with
two prompts, producing two documents
([ADR-0012](docs/adr/0012-close-reading-and-argument-evaluation-are-two-calls.md)).

**The close reading** follows the article the way a careful reader meets it for
the first time, from the opening to the last page. It first takes a look at the
kind of writing it is and how densely it is written, and lets that set the
pace: each step takes in roughly 200 to 500 words of the article. At each step
it records where we are, the move the author is making — a premise, evidence, a
definition, an inference, a qualification, a conclusion — the claims made
there with the support the author offers, and what the step means given what
came before. It knows only what it has read so far, and it does not judge
whether the argument holds.

**The argument evaluation** is given the article and the close reading and asks
for the model's own judgment of the argument as a whole: where the paper was
published and for whom, what it rests on, how it spends its attention, whether
its conclusions are required by the evidence or only permitted by it, and what
bias shapes the author's framing and the model's own reading. It is written in
the model's voice and read as its interpretation, not as a report of what the
author said.

Both prompts are in [docs/PROMPTS.md](docs/PROMPTS.md).

### Whose words are whose

All of an analysis is produced by the model, including the parts that report
what the author said. That is the part most easily misread.

The close reading keeps the author's words and the model's reading apart by
where they sit
([ADR-0013](docs/adr/0013-lean-close-reading.md)):

| Where | Whose | What it means |
| --- | --- | --- |
| a step's claims and their support | the author's | the model asserts the article says this, in the author's words where it can; not that anyone has checked |
| a step's moves and meaning | the model's | its reading of what the author is doing and how the step fits the path |
| the argument evaluation | the model's | its judgment of the argument |

Each claim and each piece of support is marked `verbatim`, the author's exact
wording, or `paraphrased`. A faithful paraphrase is not a lesser answer than a
quotation the model was unsure of. Either way, a claim recorded as the author's
is the model's assertion about the article, and it can be wrong in either
direction: an interpretation presented as something the author said, or
something the author did say left out or softened. Checking that is what the
rest of the design is for.

### What can be checked, and how

Some of it can be checked mechanically against the article:

- **Verbatim text.** A text search can look for a `verbatim` claim in the
  article, and a match is good evidence the wording is real. A miss is weaker
  evidence than it looks: PDF extraction, hyphenation, and accented characters
  all break exact matching on text the article genuinely contains, so a miss
  marks a passage to look at, not a fabrication.
- **Numbers.** Every figure in a claim or its support can be searched for in
  the article, which catches a number that is not there.
- **Citations.** A recorded reference entry can be matched against the
  article's own reference list, which catches an invented or garbled entry.

None of that can tell a paraphrase that keeps the author's meaning from one that
drops a qualification, a number attached to the wrong thing, or a judgment that
is badly reasoned. Those are checked by reading: by my own notes, and later by
the Phase 2 evaluation, which is itself checked against my scoring.

Neither reading retrieves the works an article cites or verifies their
findings. Both work from what the article provides.

### My notes as the independent reference

For each article I write my own reading before I look at any model output:
what the article says, its key figures with their context, and my judgment of
its argument. Those notes are the reference both readings are compared
against, so they have to be independent of them. For longer articles, the text
is split mechanically into steps of the same 200 to 500 words, so I can write
notes against each step without deciding how to organize them; nothing in the
split names a move or says what a step means. The notes are in
[`data/research/ab_testing/notes/`](data/research/ab_testing/notes).

### A primer before the reading

Some articles are written for specialists and explain nothing their field
takes for granted. Reading kanbur, I could record its numbers but not tell
whether they were good, bad, or ordinary. So on request the system writes a
primer: the concepts and terms an article relies on, what its numbers are
measured against, and where it sits in its field, for me to read before the
article ([ADR-0016](docs/adr/0016-a-primer-before-the-reading.md)).

The primer is the model's general knowledge rather than a reading of the
article, so it can be wrong in ways a check against the article will not catch.
I treat it as a colleague's briefing, not as evidence. It is separate from the
analysis and never given to either reading. For an article in an experiment, I
read it after writing my notes, so the notes stay independent.

## Evaluation design

Each axis targets a specific failure, so a rubric can be written against
something concrete rather than a general impression of quality.

| Failure mode | What it looks like | Axis |
| --- | --- | --- |
| Invented attribution | a claim recorded as the author's that the article does not make | source faithfulness |
| Omitted qualification | hedges, conditions, sample, or scope stripped from a claim the source stated carefully | source faithfulness, limitation discipline |
| Unsupported inference | reasoning past what the article supports, or the model's reading presented as the author's claim | inference control, assumption discipline |
| Mismatched evidence | support attached to a claim it does not support | evidence mapping |
| Inaccurate citation extraction | a misquoted marker, an invented reference entry, a citation attached to the wrong passage | citation faithfulness |
| Missing central argument | an argument the source’s case rests on, absent from the analysis | argument reconstruction |
| Faulty argument assessment | the model accepts an unsupported conclusion or criticizes an argument without adequate justification | argument assessment |
| Unusable output | faithful, complete, and still no help to me | research usefulness |

The judge needs checking as well, since it is a model making claims about
another model’s claims. I will score a sample myself, without seeing the
judge’s scores, and compare the two. Where we disagree, that marks a case worth
investigating rather than a verdict: the judge may have applied the rubric
badly, or my own reading may be the one that is wrong, and finding out which
is the point of looking. An evaluation I have not checked is not evidence that
an analysis is good.

Rubrics, scales, and the evaluation procedure are in the
[build plan](docs/BUILD_PLAN.md).

### The A/B experiments

The coding assistants suggested extracting text from the PDFs and preparing
image crops for content such as figures and tables. After that approach was
underway, I asked: **Why not just send the PDF?** We had built a preparation
pipeline without first testing whether it improved the analysis. Phase 1 tests
that, along with which model to use and, now, whether the API is needed at all.

Phase 1 runs as three experiments, one per article, each designed around what
is still open after the one before
([ADR-0015](docs/adr/0015-phase-1-as-three-experiments.md)). The two prompts
stay the same throughout; what changes is how they are run.

**Experiment 1 — Barnett (complete).** Three model configurations, each with
both input methods, for six runs:

| | GPT-6.1 Sol, medium effort | GPT-6.1 Sol, high effort | GPT-6 Astra, low effort |
| --- | --- | --- | --- |
| **Full PDF** | 1 | 1 | 1 |
| **Extracted text + crops** | 1 | 1 | 1 |

Astra cost about four times as much as Sol and recorded fewer claims, without
reading the article better that I could see. The two input methods produced
readings of about the same quality, while the prepared text needed manual
fixes and, on the next article, lost every figure.

**Experiment 2 — kanbur.** The PDF only, and a new question: does the API add
anything over the ChatGPT app I already use, set up with my instructions for
Sunny, the persona I work with? The same prompts run on the same model, GPT-6.1
Sol, through the API and through the app in work mode, at two reasoning
efforts, for four runs
([ADR-0017](docs/adr/0017-experiment-2-api-against-the-app-with-the-primer.md)):

| | API, GPT-6.1 Sol | App, GPT-6.1 Sol, work mode |
| --- | --- | --- |
| **Medium effort** | 1 | 1 |
| **High effort** | 1 | 1 |

Each run makes all three calls: the primer, the close reading, and the
argument evaluation. In the app, memory is off and my instructions for Sunny
are on. With the same model on both sides, a difference between the API and
the app comes from the app itself.

I started my notes on kanbur and stopped after three sections: the paper is
written for specialists, and without background I was recording mostly what I
did not understand. That reading is what showed the system needed the primer.
So Experiment 2 is judged without a full set of my notes: the runs are compared
with each other, against the article, and through the mechanical checks.

The app runs are done by hand, with one addition the app needs: since it
cannot enforce the output schema, call 1 asks for JSON in that shape. If the
app reads as well, the API's value is what surrounds the model: enforced
structure, run records with exact usage and cost, the same settings every
time, and analyzing a collection without pasting it article by article.

**Experiment 3 — lei.** Designed once Experiment 2 is in. Lei, at 60 pages, is
where the input method matters most for cost, so it is the likely place to
compare the PDF and the prepared text again, on two models.

For every run I record what the API reports: token usage, calculated cost, and
runtime. The app reports none of these. I compare the readings for faithful
representation of the article and the quality of their judgments about its
argument, against my own notes, written first.

The results will help me choose how to analyze the full 16-article collection.
Three articles provide an initial comparison, not a conclusion about which
approach works best across all research topics. The broader question remains
whether the system improves my research enough to justify the time spent
preparing, reviewing, and correcting its output.

## Development approach and lessons

Two coding assistants helped me build this project.

- **Claude Code** is responsible for all of the code.
- **Codex** helps with design and prompt writing, and maintains the
  [prompt log](docs/prompt_log.md).

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

## Current status and roadmap

| | |
| --- | --- |
| **Working now** | single source analysis as two calls — the close reading and the argument evaluation — running end to end with run records, and PDF preparation into cleaned text and crops |
| **Designed, not yet built** | evaluation against the axes above, synthesis, literature review, and retrieval |
| **Next** | Experiments 2 and 3 of Phase 1, which decide how the collection is analyzed |

| Phase | What it does |
| --- | --- |
| 0 | **Review and redesign**: audit the earlier code and restructure the repository and documentation around these phases *(complete)* |
| 1 | **A/B testing**: three experiments, one per article, comparing models, input methods, and the API against the ChatGPT app *(Experiment 1 complete)* |
| 2 | **DeepEval**: rubrics for the axes above, applied to the Phase 1 runs, with independent human scoring of a sample, and the choice of model and input method |
| 3 | **Research collection**: analyze and evaluate all 16 articles with the chosen configuration, reusing suitable experiment outputs |
| 4 | **Synthesis agent**: compare sources, with its own evaluation design |
| 5 | **Literature review agent**: find relevant articles for explicit research questions |
| 6 | **RAG**: retrieval across sources, analyses, evaluations, and syntheses |

The [build plan](docs/BUILD_PLAN.md) has each phase in engineering detail,
including Phase 1’s open items and what earlier code each phase reuses,
simplifies, or removes.

## Repository structure

```
.
├── data/research/                    the 16 source articles
│   ├── <13 collection PDFs>
│   ├── ab_testing/                   the 3 A/B experiment articles
│   │   └── notes/                    my own reading of each, by slug
│   └── sources.yaml                  provenance manifest, owner-confirmed
├── src/hitl_research_agent/
│   ├── models.py                     every research type, and the model-content split
│   ├── analysis.py                   analyze_source(): the call path, attempts, errors
│   ├── prompts.py                    SYSTEM_PROMPT and the per-input-mode instructions
│   ├── inputs.py                     attachment loading and validation; annotations
│   ├── cost.py                       per-model rates; cost from reported usage
│   └── config.py                     Settings: key, model, effort, limits
├── scripts/
│   ├── run_analysis.py               one A/B cell -> analysis, argument evaluation, run record
│   ├── write_primer.py               an article -> a primer on its field, to read first
│   └── prepare_sources.py            PDF -> text + crops (the experimental arm)
├── tests/
│   ├── test_analysis.py              the call path, failures, usage arithmetic
│   ├── test_inputs.py                per-mode validation, identical prompt
│   ├── test_models.py                schema rules, the reading path, round trip
│   ├── test_prompts_doc.py           PROMPTS.md matches the prompts in code
│   ├── test_cost.py                  rates, cached input, unknown model
│   ├── test_run_analysis.py          the runner, offline: provenance, records, both calls
│   ├── test_write_primer.py          the primer script, offline
│   └── preparation/                  PDF extraction behavior, with fixtures
├── docs/
│   ├── BUILD_PLAN.md                 the phases in engineering detail
│   ├── DESIGN.md                     the system, and the rules it holds to
│   ├── PROMPTS.md                    the two analysis prompts, as the code sends them
│   ├── ENGINEERING_DIRECTIVES.md     DSA and SWE directives for code changes
│   ├── REPOSITORY.md                 every file, and why it exists
│   ├── adr/0001-0017.md              one record per architectural decision
│   ├── phases/phase_1-6.md           one prompt log per phase
│   └── prompt_log.md                 index of those logs, and the conventions
├── CLAUDE.md                         what Claude Code loads in every session
├── pyproject.toml                    dependencies, Ruff, mypy, the src/ package
├── uv.lock                           resolved dependency set
├── .python-version                   3.12, matching requires-python and CI
├── .pre-commit-config.yaml           Ruff, formatting, mypy on commit
├── .github/workflows/ci.yml          the same checks plus pytest
└── .env.example                      OPENAI_API_KEY (.env is gitignored)
```

### Output layout
```
outputs/                              created by the pipeline, not in git
├── preparation/<slug>/               prepared text, crops, prep_record.json
├── ab_testing/<slug>/<config>/       Phase 1: analysis, argument evaluation, run record
├── primers/<slug>/                   primer.md + primer_record.json, on request
├── analyses/<slug>/                  Phase 3: analysis in the chosen configuration
├── evaluations/<slug>/               Phase 3: evaluation, stored apart from it
└── synthesis/                        Phase 4
```

Analyses and evaluations are stored separately so neither is confused with the
other and either can be regenerated alone. Data folders are named by role
rather than by phase number, so renumbering a phase never moves source
material. The only files the pipeline writes are JSON, plus the `.txt` and
`.png` that preparation produces.

## Stack, setup, and documentation

Python 3.12 · LangChain + OpenAI Responses API · Pydantic · PyMuPDF ·
DeepEval *(Phase 2)* · embeddings and retrieval *(Phase 6)* · uv · Ruff · mypy ·
pre-commit · GitHub Actions

**Prerequisites:** [uv](https://docs.astral.sh/uv/) (manages Python 3.12
itself) and git 2.31+.

```bash
brew install uv
uv sync
uv run pre-commit install
```

Set `OPENAI_API_KEY` in `.env` (see [`.env.example`](.env.example)).

```bash
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy src
```

- [Design](docs/DESIGN.md) — the three agents, the workflow contract, the data
  model, and the rules that hold across every phase
- [Build Plan](docs/BUILD_PLAN.md) — the phases in engineering detail, with
  rubrics and procedures
- [Prompts](docs/PROMPTS.md) — the close-reading and argument-evaluation
  prompts in full, and how they are run in the ChatGPT app
- [Repository Inventory](docs/REPOSITORY.md) — every file, what it is for, and
  where the code is heavier than it needs to be
- [Decision Records](docs/adr/) — one dated record per architectural decision,
  with the alternatives and what each one cost
- [Prompt Log](docs/prompt_log.md) — one log per phase, recording the prompts
  given to Claude Code and Codex while building this and what came back
