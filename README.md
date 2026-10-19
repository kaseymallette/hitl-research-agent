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


## How the system supports the researcher

Three agents do the preparatory work.

| Agent | Given | Produces |
| --- | --- | --- |
| **Single source analysis** | one article | two documents: a close reading as structured JSON, a step-by-step reading path through the paper with the claims, evidence, and citations met along the way, and, from a second call, the model's own evaluation of the argument |
| **Synthesis** | several accepted analyses | a cross-source comparison of agreements, disagreements, methodological differences, limitations, and open questions, with each position still attributed to its source |
| **Literature review** | an explicit research question | candidate articles with an explanation of why each one is relevant |

Neither single source analysis nor synthesis receives a research question, so
their output stays useful for questions I have not asked yet. Synthesis
compares what the sources say to each other, not to a question. Only the
literature review agent sees a question, and it only proposes articles.

```
article + prompt → model → JSON → separate evaluation → accept · reject · revise · rerun
```

The planned review workflow will present the structured analysis, the citations
supporting it, the evaluation scores, and the evaluation’s explanation of those
scores. Evaluation will inform my review rather than replacing it, and it will
not act as a gate. A
paraphrase, a missing evidence label, or a thin claim gets reported rather than
withheld, because I want to see the analysis and judge it myself. Only a
technical failure stops a run: an API error, an unreadable response, or output
that will not parse.

The decision stays with me. I accept, reject, revise, or rerun, and only
accepted analyses enter the research collection. The agents interpret sources
and assess arguments. I review those assessments, decide which conclusions
are justified, and choose what to pursue next.

## What an analysis records, and what needs checking

An analysis records four kinds of content: what the source states, what the
model interprets, the evidence offered for each claim, and provenance, meaning
the source’s identity, where each piece of evidence sits in it, and what the
source itself cites.

All of it is produced by the model, including the parts labeled as the source’s
own statements. That is the part most easily misread.

### `statement_origin` records an attribution, not a verification

Each claim in the close reading carries `statement_origin`:

| Value | What it means | What it does not mean |
| --- | --- | --- |
| `author_stated` | the model asserts that the source says this | that the source has been checked and does say this |
| `model_inferred` | the model is interpreting rather than reporting | that the inference is sound |

`author_stated` is the model’s claim about provenance, and it can be wrong in
either direction: an interpretation presented as something the authors said, or
something the authors did say recorded as the model’s interpretation. This is
the hardest part of the system to get right. Saying that the analysis separates
author statements from model inference describes the schema correctly but
promises nothing, because the separation is only as good as the model’s
attributions. Checking them is what the evaluation step is for.

### What can and cannot be checked mechanically

When evidence is marked `verbatim`, a text search can look for it in the
document, and a match is good evidence that the quotation is real. A failure to
match is weaker evidence than it looks: PDF extraction, markdown formatting,
line-break hyphenation, and OCR all break exact matching on text the source
genuinely contains, so a miss marks a passage to look at by eye rather than a
fabrication.

A faithful paraphrase is also `author_stated` and does not appear in the
document at all, so a text search cannot tell a paraphrase that preserves the
authors’ meaning from one that drops a qualification. Paraphrased attributions
are reachable only through evaluation and my own review, which is why
`author_stated` needs checking rather than trust.

`evidence_form`, either `verbatim` or `paraphrased`, is independent of
`statement_origin`. It describes the form of the evidence text rather than who
is committed to its content, and a faithful paraphrase is not a lesser answer
than a quotation the model was unsure of.

### Evaluating the model and the authors’ arguments

Evaluation will check two things. Does the model faithfully represent the
source, preserving what the authors actually claim and distinguishing it from
the model’s own interpretation? And does the model make a defensible assessment
of the argument, grounding its judgments in the source’s evidence and reasoning?
Accurately reporting a claim does not establish that the claim is well supported,
and identifying a supposed weakness does not establish that the model is right.

The evaluation will examine both the accuracy of the model’s account and
the reasoning behind its assessment. Human review will check those judgments,
including the judgments made by the evaluation model. The goal is to establish
whether AI can help me evaluate arguments, and where its assessments need
correction.

The current analysis step works from the supplied article. It records the
article’s citations but does not retrieve the cited studies or independently
verify their findings. Its assessment of an argument is based on what the
article provides.


## Evaluation design

Each axis targets a specific failure, so a rubric can be written against
something concrete rather than a general impression of quality.

| Failure mode | What it looks like | Axis |
| --- | --- | --- |
| Invented attribution | a claim labeled `author_stated` that the source does not make | source faithfulness |
| Omitted qualification | hedges, conditions, sample, or scope stripped from a claim the source stated carefully | source faithfulness, limitation discipline |
| Unsupported inference | reasoning past what the source supports, or inference presented as report | inference control, assumption discipline |
| Mismatched evidence | evidence attached to a claim it does not support, or a wrong `relationship_to_claim` | evidence mapping |
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

### The A/B experiment

The coding assistants suggested extracting text from the PDFs and preparing
image crops for content such as figures and tables. After that approach was
underway, I asked: **Why not just send the PDF?** We had built a preparation
pipeline without first testing whether it improved the analysis. This
experiment compares the two approaches to find out whether that extra work
is worthwhile.

I’m also testing GPT-6.1 Sol at medium and high reasoning effort against
GPT-6 Astra at low reasoning effort. Sol could lower the cost of analyzing the
collection, but I want to see whether it represents and assesses the authors’
arguments as well as Astra, and whether any improvement from Astra justifies
its additional cost. Running Sol at two effort levels keeps the model and the
effort from being confounded: if Astra comes out ahead of Sol medium, Sol high
shows whether Sol only needed more reasoning.

Each configuration will analyze the same three articles using both input
methods, producing **18 analyses**:

| | GPT-6.1 Sol, medium effort | GPT-6.1 Sol, high effort | GPT-6 Astra, low effort |
| --- | --- | --- | --- |
| **Full PDF** | 3 analyses | 3 analyses | 3 analyses |
| **Extracted text + crops** | 3 analyses | 3 analyses | 3 analyses |

The experiment began as a 2 × 2 over four articles. Adding Sol high and
dropping one of the two desalination articles kept the number of analyses
close to the original; the reasons are in
[ADR-0009](docs/adr/0009-phase-1-matrix-three-configurations-three-articles.md).

The analysis prompt, output schema, one-correction policy, and
question-independence of the task stay fixed. The intended differences are
the input method and model configuration.

I will compare the analyses for faithful representation of the sources and
the quality of their assessments of the authors’ arguments. Alongside those
results, I will record token usage, calculated cost, runtime, and the time
and manual work needed to prepare the text and crops. That will let me weigh
any improvement in analysis against what it costs to produce.

The results will help me choose a configuration for the full 16-article
collection. Three articles provide an initial comparison, not a conclusion
about which approach works best across all research topics. The broader
question remains whether the system improves my research enough to justify
the time spent preparing, reviewing, and correcting its output.

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
| **Working now** | the analysis data model, single source analysis running end to end and returning JSON, and PDF preparation into cleaned text and crops |
| **Designed, not yet built** | evaluation against the axes above, synthesis, literature review, and retrieval |
| **Next** | the A/B experiment, which decides the configuration the collection is analyzed with |

| Phase | What it does |
| --- | --- |
| 0 | **Review and redesign**: audit the earlier code and restructure the repository and documentation around these phases *(complete)* |
| 1 | **A/B testing**: the 2 × 3 above, recording usage, cost, runtime, and preparation effort |
| 2 | **DeepEval**: rubrics for the axes above, applied to the 18 analyses, with independent human scoring of a sample, and the choice of model and input method |
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
│   └── prepare_sources.py            PDF -> text + crops (the experimental arm)
├── tests/
│   ├── test_analysis.py              the call path, failures, usage arithmetic
│   ├── test_inputs.py                per-mode validation, identical prompt
│   ├── test_models.py                schema rules, attribution labels, round trip
│   ├── test_cost.py                  rates, cached input, unknown model
│   └── preparation/                  PDF extraction behavior, with fixtures
├── docs/
│   ├── BUILD_PLAN.md                 the phases in engineering detail
│   ├── DESIGN.md                     the system, and the rules it holds to
│   ├── ENGINEERING_DIRECTIVES.md     DSA and SWE directives for code changes
│   ├── REPOSITORY.md                 every file, and why it exists
│   ├── adr/0001-0012.md              one record per architectural decision
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
- [Repository Inventory](docs/REPOSITORY.md) — every file, what it is for, and
  where the code is heavier than it needs to be
- [Decision Records](docs/adr/) — one dated record per architectural decision,
  with the alternatives and what each one cost
- [Prompt Log](docs/prompt_log.md) — one log per phase, recording the prompts
  given to Claude Code and Codex while building this and what came back
