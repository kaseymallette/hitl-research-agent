# hitl-research-agent

A human-in-the-loop multi-agent research framework for building and examining a collection of evidence across articles. Three AI agents handle these tasks: single source analysis, synthesis, and literature review, giving researchers a way to examine individual arguments and understand how they relate across a research collection.

The analyses connect authors’ claims to their evidence, methods, assumptions, and limitations, while making the model’s own interpretations explicit. A separate evaluation step checks whether those analyses faithfully represent the sources. Researchers review the results before adding them to their collection and use that collection to investigate disagreements, gaps, and new questions.

## Purpose

I’m building this framework to become a better researcher: to work through more literature, make connections across sources, and pursue questions I might otherwise miss. When using AI to summarize and analyze articles, I’ve noticed models misattribute claims, leave out important qualifications, or attach evidence that does not support their interpretations. These errors make it difficult to rely on an analysis when comparing sources or deciding which evidence supports an argument.

Which brings me to the core question:

> Why use AI to help with research when I can read the articles myself?

That is why I want to ensure that AI adds something worthwhile, whether that is helping me compare explanations, noticing conflicting evidence, or identifying an assumption worth investigating. *Does this system help me conduct better research that justifies the time and money spent to use it?*


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

The source collection is 16 articles in [`data/research/`](data/research), four
of which are the experiment set in
[`data/research/ab_testing/`](data/research/ab_testing).

I chose this question because it is narrow, contested, and evidence-heavy
enough to develop the framework against, with real disagreement in the
literature to work through. It shapes which sources I collect and what I ask
the literature review agent. It does not reach single source analysis or
synthesis, both of which stay question-independent so that the analyses and
comparisons I produce now remain useful when I move on to a different question.


## How the system supports the researcher

Three agents do the preparatory work.

| Agent | Given | Produces |
| --- | --- | --- |
| **Single source analysis** | one article | a structured JSON analysis of it: claims, evidence, citations, methodology, assumptions, limitations, proposed solutions, open questions, provenance |
| **Synthesis** | several accepted analyses | a cross-source comparison of agreements, disagreements, methodological differences, limitations, and open questions, with each position still attributed to its source |
| **Literature review** | an explicit research question | candidate articles with an explanation of why each one is relevant |

Neither single source analysis nor synthesis receives a research question, so
their output stays useful for questions I have not asked yet. Synthesis
compares what the sources say to each other, not to a question. Only the
literature review agent sees a question, and it only proposes articles.

```
article + prompt → model → JSON → separate evaluation → accept · reject · revise · rerun
```

What I receive is the structured analysis, the citations supporting it, the
evaluation scores, and the evaluation’s explanation of those scores. Evaluation
informs my review rather than replacing it, and it does not act as a gate. A
paraphrase, a missing evidence label, or a thin claim gets reported rather than
withheld, because I want to see the analysis and judge it myself. Only a
technical failure stops a run: an API error, an unreadable response, or output
that will not parse.

The decision stays with me. I accept, reject, revise, or rerun, and only
accepted analyses enter the research collection. Interpretation, inference,
deciding what matters, and choosing what to pursue next are mine. The system
does not rank sources, resolve disagreements, or draw conclusions.

## What an analysis records, and what needs checking

An analysis records four kinds of content: what the source states, what the
model interprets, the evidence offered for each claim, and provenance, meaning
the source’s identity, where each piece of evidence sits in it, and what the
source itself cites.

All of it is produced by the model, including the parts labeled as the source’s
own statements. That is the part most easily misread.

### `statement_origin` records an attribution, not a verification

Each claim, assumption, limitation, proposed solution, open question, and the
methodology record carries `statement_origin`:

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

### Faithfulness, support, and what is out of scope

A faithful analysis can accurately reproduce a weak argument, a poorly
evidenced one, or a wrong one. If I treated faithfulness as though it also
established soundness, the framework would pass bad sources through
unexamined, so I keep three questions separate and avoid using "validity" as a
single term for all of them.

| Question | What it is about |
| --- | --- |
| Does the analysis represent the source? | the analysis, and the first thing evaluation has to establish |
| Do the source’s reasons meet its claim? | the source’s argument, which can be weak even when the analysis of it is perfect |
| Is the source’s method sound? | the source’s reasoning. Judging this is held back until the first two are reliable |

The second question is the one that takes judgment rather than reading. An
analysis can record a claim and its evidence accurately and still leave open
whether that evidence carries the claim, and the schema keeps room for that
judgment: how a piece of evidence relates to its claim, and whether a claim’s
reasons meet the strength it was stated with. How far the system should go in
making those judgments, rather than representing the argument and leaving them
to me, is something I will decide later.

External factual verification is out of scope. Citations record what the source
itself cites, extracted from the document. No cited work is retrieved, and no
claim is checked against the world. An analysis can be faithful to a source
that is factually wrong, and nothing here will notice.


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

Before analyzing the collection, I am running one 2 × 2 comparison across four
articles, producing 16 analyses.

| | GPT-6.1 Sol, medium effort | GPT-6 Astra, low effort |
| --- | --- | --- |
| **Full PDF** | 4 analyses | 4 analyses |
| **Extracted text + crops** | 4 analyses | 4 analyses |

Held fixed: the analysis prompt, the output schema, the one-correction policy,
and the question-independence of the task. The only intended differences are
the input format and the model configuration.

The input-method axis is there because it is a real engineering question worth
measuring rather than assuming. The extraction pipeline came first, turning a
PDF into cleaned text with crops retained for the figures, equations, and
tables that text cannot represent, and that pipeline works. What it has not had
is a controlled comparison against the simpler alternative of sending the PDF
straight to the model. Preparation may turn out to be the most expensive part
of the workflow, and if the two methods produce comparable analyses it is worth
knowing that before committing the whole collection to the longer route.

The model axis asks a cost question. Sol could lower the cost of analyzing the
collection. I want to test whether Astra produces better analyses and whether
that improvement justifies its additional cost.

Quality alone will not decide this, which is why I record four things for every
analysis: quality, token usage and calculated cost, runtime, and preparation
effort. Whether those four point to the same configuration is one of the things
the experiment is meant to find out. The documented rate for Astra is five
times Sol’s, and the full-PDF arm sends every page as an image, so cost there
should scale with page count in a way the extracted-text arm does not. If an
approach analyzes only slightly better for several times the cost and a
preparation step for every article, it may not be worth it to me.

The result informs one decision: which configuration analyzes the full
16-article collection. Four articles give me an initial comparison rather than
proof that one configuration is better in general, since they are four articles
on one topic and a configuration that does well here may not do well on a
different kind of source.

This experiment will help me choose a configuration; the broader question is whether using it improves my research enough to justify the time spent preparing, reviewing, and correcting its output.

## Current status and roadmap

| | |
| --- | --- |
| **Working now** | the analysis data model, single source analysis running end to end and returning JSON, and PDF preparation into cleaned text and crops |
| **Designed, not yet built** | evaluation against the axes above, synthesis, literature review, and retrieval |
| **Next** | the A/B experiment, which decides the configuration the collection is analyzed with |

| Phase | What it does |
| --- | --- |
| 0 | **Review and redesign**: audit the earlier code and restructure the repository and documentation around these phases *(complete)* |
| 1 | **A/B testing**: the 2 × 2 above, recording usage, cost, runtime, and preparation effort |
| 2 | **DeepEval**: rubrics for the axes above, applied to the 16 analyses, with independent human scoring of a sample, and the choice of model and input method |
| 3 | **Research collection**: analyze and evaluate all 16 articles with the chosen configuration, reusing suitable experiment outputs |
| 4 | **Synthesis agent**: compare sources, with its own evaluation design |
| 5 | **Literature review agent**: find relevant articles for explicit research questions |
| 6 | **RAG**: retrieval across sources, analyses, evaluations, and syntheses |

The [build plan](docs/BUILD_PLAN.md) has each phase in engineering detail,
including Phase 1’s open items and what earlier code each phase reuses,
simplifies, or removes. Experiment outputs from the previous design are kept
for history in [`outputs/v1_archive/`](outputs/v1_archive).

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

- [Build Plan](docs/BUILD_PLAN.md) — the phases in engineering detail, with
  rubrics and procedures
- [Prompt Log](docs/prompt_log.md) — one log per phase, recording the prompts
  given to Claude Code and Codex while building this and what came back
