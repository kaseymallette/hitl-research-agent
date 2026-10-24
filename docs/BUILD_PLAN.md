# Build Plan

> **Being rewritten.** [ADR-0019](adr/0019-four-phases-head-to-head-evaluation.md)
> replaces this plan's seven phases with four after Phase 0: A/B testing on two
> articles, a head-to-head evaluation, synthesis with the collection and
> retrieval, and the research assistant
> ([ADR-0018](adr/0018-three-agents-analysis-synthesis-research-assistant.md)).
> Until this document is rewritten around them, the phases below describe the
> earlier plan.

This document turns the phases in [README.md](../README.md) into an engineering
plan. It is developed one phase at a time: the current phase is specified in
full, later phases state their goal and the decisions they must make, and are
filled in once the prior phase is accepted.

This is the v2 plan. It replaces the nine-phase v1 plan. v1 built a working
single-source analysis pipeline and then spent a long sequence of turns on
grounding checks that were ultimately removed; what survives of that history
here is the audit in Phase 0 below. The v1 prompt logs and experiment outputs
were removed in the redesign and stay at the `v1-final` tag;
[`docs/prompt_log.md`](prompt_log.md) now indexes one log per phase.

The architecture these phases build — the three agents, the workflow
contract, the data model, and the rules that hold across every phase — is in
[DESIGN.md](DESIGN.md).

---

## Phase 0 — Review and Redesign

### Goal

Decide what of v1 carries into v2 before any v2 code is written, and restructure
the repository and documentation around the v2 phases.

### What the audit found

v1 was 1,675 lines of application code across 17 files, with 181 tests. The
single-source analysis pipeline worked: it sent an article to the model with the
analysis prompt, accepted one correction attempt if the output did not fit the
schema, recorded per-attempt usage and timing, and returned the JSON without
judging its quality. That was already the v2 contract, and it already supported
both Phase 1 input methods and any model/effort pair through configuration.

What it also carried was structure built for a system that does not exist yet,
and dead weight left behind when v1's grounding checks were removed: the helpers
that supported them, scope strings that still described them, and a 664-line
one-source pilot script built around their failures. The codebase was then
consolidated to what the experiment needs.

**Net: 17 source files to 6, 1,675 lines to 1,289** (220 of them prompt text),
**and 181 tests to 73** — twelve went with the dead grounding helpers, the rest
with the consolidation below.
[`REPOSITORY.md`](REPOSITORY.md) records every file that remains and what was
deleted. Kept here is only the part it does not cover: why seventeen files
became six.

| Was | Became | What changed |
| --- | --- | --- |
| `models/` (8 files, 267) | `models.py` (302) | Six classes with identical fields — `InterpretedStatement` and five subclasses — became one `Statement`. |
| `ExtractedClaim`, `ExtractedEvidence`, `_assemble_analysis()` | nothing | They existed only to strip UUIDs the model must not supply. Nothing read those UUIDs, so both duplicates and the 40-line copy function went. `SourceAnalysis` still wraps model content with `id`, `provenance`, and `analyzed_at`. |
| `pipeline.py` (476), `attempts.py` (61), `errors.py` (94) | `analysis.py` (448) | Six exception classes became one `AnalysisError` with a `kind`; nothing caught the subclasses. The response-metadata allowlist recorded fields nobody read. |
| `attachments.py` (175), `annotations.py` (62) | `inputs.py` (238) | Both describe what reaches the model. `grounding_view()`, `contains_reserved_character()`, and `SENTINEL` were dead. |
| `schemas.py`'s three `ANALYSIS_SCOPE` strings | `models.py` | They described grounding checks that no longer exist, so each was false on every saved result. |
| the pilot script's rate table | `cost.py` (64) | Cost from reported usage, cached input at the cached rate. The projection, dry run, and spending guard did not come with it. |
| `scripts/analyze_pdf.py` (165) | `scripts/run_analysis.py` (273) | Now takes any input method and records cost. The old one handled only the PDF arm and **crashed on success**, reading `result.grounding_notes` after a field of that name had been removed. |

Nothing in v1 covered evaluation, synthesis, literature review, or retrieval.
DeepEval was named in the v1 README but never added as a dependency. Phases 2,
4, 5, and 6 start from nothing.

### What moved

- `data/phase_3/*.pdf` (12 articles) → `data/research/`, and its `ab_testing/`
  four → `data/research/ab_testing/`, with `sources.yaml` and its `pdf:` paths
- `data/phase_2/` (the v1 development source, not one of the 16) and the v1
  experiment outputs under `outputs/` were removed. They stay at the
  `v1-final` tag.
- `prepare_phase_3_sources.py` → `prepare_sources.py`. Its extraction behavior
  is unchanged — the only edits were the import path and writing its output as
  `prepared_text.txt` rather than `.md`, since the pipeline produces no Markdown.
- `data/research/sources.yaml` gained owner-confirmed entries for the four A/B
  articles. Title, authors, publication date, type, DOI, publisher, and
  publication URL were verified against each PDF and its Crossref record, with
  `provenance_basis` naming the source of every field and keeping each file's
  email download origin out of `url`.

73 tests pass, with Ruff, formatting, and mypy clean.

### Acceptance criteria

- [x] Every v1 component has a reuse, simplify, or remove verdict with a reason.
- [x] Every verdict is **applied**: the removals are removed, the
      simplifications simplified, and nothing is deferred to a later phase.
- [x] Data folders are named by role, with no phase-numbered folders left.
- [x] README introduces the project, its three agents, and the phases.
- [x] Every file in the repository is accounted for in
      [`REPOSITORY.md`](REPOSITORY.md), with a reason for existing.
- [x] This plan specifies Phase 1 in full, and Phase 1 contains no cleanup.
- [x] The code is reduced to what the experiment needs: 6 source files,
      1,289 lines, 73 tests, with Ruff, formatting, and mypy clean.
- [x] Nothing is left open: every source in the experiment has confirmed
      provenance, and Phase 1 starts by preparing articles, not by finishing
      Phase 0.

---

## Phase 1 — A/B Testing

### Goal

Establish, by measurement rather than assumption, whether preparing a PDF into
extracted text plus crops buys anything over sending the PDF itself, and
whether the expensive model buys anything over the cheap one, including the
cheap one given more reasoning effort. v1 never compared
these: it assumed extracted text because its first implementation needed a
local text reference, and the one paired comparison it ran was judged by
grounding checks that favored the arm receiving the prepared text, so it settled
nothing.

Phase 1 produces the evidence. It does not choose — Phase 2 chooses, on quality
and cost together.

### Two experiments

**Phase 1 is complete.** It ran as two experiments, one per article, the
second designed around what the first left open
([ADR-0015](adr/0015-phase-1-as-three-experiments.md),
[ADR-0019](adr/0019-four-phases-head-to-head-evaluation.md)), with Codex
added to the second ([ADR-0020](adr/0020-codex-joins-experiment-2.md)).

| Experiment | Article | Design | Runs |
| --- | --- | --- | --- |
| 1 | Barnett | 3 model configurations × 2 input methods | 6, complete |
| 2 | kanbur | PDF only: 2 efforts (medium, high) × 2 ways of running GPT-6.1 Sol (the API; the ChatGPT app in work mode, memory off, my instructions for Sunny on); the API runs also write the primer ([ADR-0017](adr/0017-experiment-2-api-against-the-app-with-the-primer.md)); and Codex, from the instruction files in `prompts/` ([ADR-0020](adr/0020-codex-joins-experiment-2.md)) | 6, complete |

Astra low is dropped after Experiment 1, and prepared text sits out
Experiment 2. There is no Experiment 3: lei is analyzed with the rest of the
collection, and the input-method question is settled in Phase 2 from Barnett. The app runs are run by hand with the
same prompts, as set out in [PROMPTS.md](PROMPTS.md#running-the-prompts-in-the-chatgpt-app),
and saved with the API's runs in `outputs/ab_testing/<slug>/adr_0017/`: the API
as `pdf__gpt-6.1-sol-<effort>/`, the app as `app__gpt-6.1-sol-<effort>-work/`,
each holding `primer.md`, `analysis.json`, and the argument evaluation. The app
reports no usage or cost, so its runs have no run record.

The rest of this section describes Experiment 1's matrix, which set the
articles, configurations, and slugs. Its 3 articles × 2 input methods × 3
configurations were the original plan for all of Phase 1
([ADR-0009](adr/0009-phase-1-matrix-three-configurations-three-articles.md),
revising [ADR-0008](adr/0008-compare-pdf-against-prepared-text.md)'s 2 × 2 over
four articles; [ADR-0014](adr/0014-kanbur-replaces-katakam.md) set the third
article).

| Articles | `data/research/ab_testing/` | pages | chars |
| --- | --- | --- | --- |
| | `barnett_itzhaki_2026_water_footprint_artificial_intelligence` | 7 | 51k |
| | `kanbur_et_al_2020_desalination_integrated_data_center_cooling` | 18 | 82k |
| | `lei_et_al_2025_water_use_data_center_workloads` | 60 | 97k |

| Input method | `input_mode` | What the model receives |
| --- | --- | --- |
| Full PDF | `pdf` | the original PDF; the API supplies its text layer and page images |
| Extracted text + crops | `prepared_text_and_crops` | the prepared text, plus one retained crop per item preparation could not represent |
| (the same arm, when an article has no crops) | `prepared_text` | the prepared text alone |

| Model configuration | Model | Reasoning effort |
| --- | --- | --- |
| Sol medium | `gpt-6.1-sol` | `medium` |
| Sol high | `gpt-6.1-sol` | `high` |
| Astra low | `gpt-6-astra` | `low` |

Configuration slug, used in output paths: `<input>__<model>-<effort>`, so
`pdf__gpt-6.1-sol-medium`, `pdf__gpt-6.1-sol-high`, `pdf__gpt-6-astra-low`,
`text_crops__gpt-6.1-sol-medium`, `text_crops__gpt-6.1-sol-high`, and
`text_crops__gpt-6-astra-low`.

Sol high is there so model and effort are not confounded: Sol medium against
Sol high isolates effort, and Sol high against Astra low compares the models
with Sol given more reasoning. Astra runs at one setting, so its model and
effort still cannot be separated.

The page spread is deliberate. The PDF arm's input cost scales with page count,
so `lei` at 60 pages is the stress case for that arm, and `barnett` at 7 pages
the cheap case. If the two arms differ in cost, they will differ most there.
The articles also come from three journals. Of the original four, kanbur and
`katakam_et_al_2027_desalination_systems_data_center_water_needs` cover the same
subject; one left the experiment to pay for the third configuration. Katakam
was kept at first, then replaced by kanbur because it shares Barnett's journal,
*Water Research*. Katakam is in `data/research/` with the rest of the
collection.

### Held constant

The analysis prompt (`SYSTEM_PROMPT`), the output schema (`ExtractedAnalysis`
in `models.py`), the one-correction policy, and the
question-independence of the task. The only intended differences are the input
format, its format-specific layout instructions, and the model configuration.

Each cell makes two calls: the close reading, under that prompt and schema, and
the model's own evaluation of the argument, under `EVALUATION_PROMPT`
([ADR-0012](adr/0012-close-reading-and-argument-evaluation-are-two-calls.md)). That design was settled after Barnett's first
runs; Barnett is rerun under it, so all 18 cells share the same two prompts and
schemas, which their run records' fingerprints show.

### What is measured

Per analysis, in `run_record.json`:

- **Usage** — input, output, reasoning, and cached-input tokens, per attempt and
  in total, taken from what the API reported. Never a value standing in for an
  unknown one.
- **Cost** — calculated from the documented per-model rates and the actual
  usage, recorded separately from any confirmed billing. The rates recorded in
  v1 (read from OpenAI's model pages on 2026-10-15) are $2.00/$10.00 per MTok
  input/output for `gpt-6.1-sol` and $10.00/$50.00 for `gpt-6-astra` — Astra is
  five times the rate, which Phase 2's choice has to weigh against whatever
  quality difference it finds. Reasoning tokens are billed at the output rate,
  so Sol high costs more than Sol medium by however many more it uses.
- **Runtime** — wall clock per attempt and per analysis.
- **Attempts** — outcome, request id, and problems for each, including a first
  attempt that failed the schema.

Per article, once, in a preparation record shared by its three `text_crops` cells:

- **Preparation effort** — wall-clock preparation time, number and kind of
  preparation gaps (figures, equations, multi-level table headers), number of
  crops retained, and any manual intervention needed. The `pdf` arm's
  preparation effort is zero; owner-confirmed provenance is needed by both arms
  and is not attributed to either.

### Output layout

```
outputs/ab_testing/<slug>/<config>/analysis.json      the analysis, indented, unchanged
outputs/ab_testing/<slug>/<config>/argument_evaluation.json  the model's evaluation of the argument
outputs/ab_testing/<slug>/<config>/run_record.json    usage, cost, runtime, attempts
outputs/ab_testing/<slug>/<config>/failed_run_<n>.json  an earlier failed run of the cell, kept for its cost
outputs/ab_testing/summary.csv                        one row per cell, for Phase 2
outputs/preparation/<slug>/                           extracted text, crops, preparation record
```

A cell holds the analysis the model returned. A thin or heavily paraphrased
analysis is a result, recorded as-is for Phase 2 to assess. A *technical*
failure — API error, unreadable response, output that will not parse — is not a
result: record it and rerun that cell.

An article with no figures, equations, or multi-level table headers produces no
crops, and its three `text_crops` cells send prepared text alone. They still run
and still count: the arm being compared is the **input workflow** — prepare the
PDF locally, or hand the PDF to the API — and a crop count of zero is a property
of that article, not a defect in the cell. The run record carries `input_mode`
and `crops_sent` so the count is available to Phase 2. The experiment does not
claim to measure the independent effect of crops, and nothing here is set up to:
crops vary with the article, not with a condition anyone assigned.

### Implementation tasks

Phase 0 left the code and the provenance ready for these; nothing here is
cleanup, and nothing is blocked.

1. Prepare each article with `prepare_sources.py`, timing it; record gaps and
   crops. Barnett and kanbur are prepared.
2. Run each experiment's API cells with `run_analysis.py`: it takes an
   article, an input method, and a model, and writes `analysis.json`,
   `argument_evaluation.json`, and `run_record.json` with usage, calculated
   cost, and runtime. Run Experiment 2's app cells by hand.
3. Write `summary.csv` — one row per cell, the only new code this phase needs.

Cost: on the one measured v1 data point, two Sol-medium analyses of a 36.6k-char
article, each including a correction attempt, had a combined calculated cost of
$0.5173 — about $0.26 per analysis. These articles are 1.4–2.9× that length, the
removal of the quality gates should make most runs single-attempt, and Astra's
rates are 5× Sol's. For the original 16-cell design that put the order of
magnitude at roughly $10–15, dominated by the eight Astra cells. The 18-cell
design has six Astra cells rather than eight, and six Sol-high cells whose
reasoning usage has not been measured, so no revised figure is given here.
That is a projection from one article at one effort level, not a cap; the runner should take an explicit per-run confirmation and
report actual cost as it goes.

Actual: the ten runs that make up the two experiments cost $5.34 through the
API — $3.81 for Barnett's six, Astra's two accounting for $2.47 of it, and
$1.53 for kanbur's two API runs with their primers. Kanbur's PDF costs about
70,000 input tokens per call against Barnett's 19,000. The app runs cost
nothing beyond the subscription. Earlier runs under superseded prompts are not
counted. The four Codex sessions — two close readings and two evaluations —
used about 1% of a ChatGPT Pro weekly limit, which reports no tokens.

Billed in all: $11.89 on the OpenAI account. The run records account for
$10.61 of it — Barnett under ADR-0009 ($1.97), ADR-0010 ($1.77), ADR-0011
($1.07), and ADR-0012 ($0.45), and the two experiments ($5.34) — so about half
the API spend went into the prompt iterations that led to the final design.
The remaining $1.28 is most likely a Barnett run stopped mid-call, which left
no record, and the difference between `cost.py`'s rates and actual billing.

### Tests

Phase 0 left 73 tests covering the call path, the input modes, the schema rules,
cost, the runner's input handling, and PDF preparation. Phase 1 adds only what the matrix runner itself needs,
offline and with no API calls: that a configuration slug maps to the right input
mode and settings, that a failed cell still writes a run record rather than a
half-written directory, and that `summary.csv` reports what the run records hold.

### Acceptance criteria

- [x] Every cell of each experiment has an `analysis.json`, indented and
      readable, the analysis the model returned, unmodified.
- [x] Every cell has its argument evaluation — `argument_evaluation.json` from
      the API, `argument_evaluation.md` from the app and from Codex. Where an evaluation was
      rerun on a saved close reading, after a connection error or a prompt
      revision, the rerun has its own record.
- [x] Each API cell has a `run_record.json` with usage, calculated cost,
      runtime, and per-attempt records for both calls; no fabricated values.
- [x] Preparation effort recorded for every article given the text arm
      (Barnett).
- [x] Within an experiment, the prompts, schema, and correction policy are
      identical across API cells, demonstrably from the records: every close
      reading carries the same `SYSTEM_PROMPT` fingerprint, and every
      evaluation in use the same `EVALUATION_PROMPT` fingerprint. App cells
      use the same prompts with only the format instruction added; Codex
      cells use the same prompt text from `prompts/`, checked by a test.
- [x] My notes on each article are written before its outputs are read —
      for Barnett. Kanbur's were suspended after three steps
      ([ADR-0017](adr/0017-experiment-2-api-against-the-app-with-the-primer.md)).
- [ ] `summary.csv` lets Phase 2 pick up the comparison without rereading the
      run records. Not written: Phase 2's head-to-head reads the runs and their
      records directly.
- [x] No quality check anywhere can prevent an analysis from being written.

### What Phase 1 does not decide

Which configuration wins. Counts of claims, evidence items, or citations do not
establish fidelity, and neither does a run completing. Readings of figures,
tables, and equations from either arm are unverified until a human checks them
against the original images. Phase 1 hands Phase 2 artifacts and measurements.

---

## Phase 2 — Evaluation

### Goal

Judge both experiments head to head, and choose how the collection is
analyzed: model, effort, input method, and API or app, on quality and cost
together ([ADR-0019](adr/0019-four-phases-head-to-head-evaluation.md)).

### The head-to-head judgment

For each experiment, Claude reads the article and every run side by side and
writes one judgment, saved apart from the analyses as
`outputs/judgments/<slug>.md`:

- **Close readings:** how many of the article's claims and figures each run
  caught or missed; how faithfully each is recorded against the article —
  qualifiers and strength of language kept, nothing invented, citations as
  printed; and how detailed and readable each is.
- **Argument evaluations:** whose reasoning holds up, what each found that the
  others did not, and where each is wrong.
- **Primers** (kanbur's API runs): accuracy and usefulness for a reader new to
  the field.
- **A ranking with reasons,** beside each run's cost.

The failure modes in the README's evaluation design are what it looks for. The
mechanical checks already run — verbatim text, numbers, and reference entries
against each article — feed into it.

### Decisions this phase makes

- **The configuration for the collection:** GPT-6.1 Sol at medium or high
  effort, and the API or the app, weighing quality against the cost each run
  recorded.
- **The input method:** the PDF or prepared text with crops, from Barnett,
  where both ran. This settles
  [ADR-0008](adr/0008-compare-pdf-against-prepared-text.md); if the PDF wins,
  `prepare_sources.py` can go.

### Checking the judge

Claude is not a blind judge: it helped design the prompts and knows my views
on the articles. It is a different model from the one judged, so it is not
grading its own work. I check its judgment against my own reading, at least
for Barnett, where I have full notes. Where we disagree, that is a case to look
into, not a verdict either way.

### Done when

- [ ] A judgment for each experiment, saved in `outputs/judgments/`.
- [ ] My check of at least one, with any disagreement noted.
- [ ] The configuration for the collection chosen and recorded in an ADR,
      with the input-method question settled.

---

## Phase 3 — Research Collection

### Goal

Analyze and evaluate all 16 articles in `data/research/` using the Phase 2
configuration, reusing the Phase 1 outputs that already used it.

Three of the 16 are the A/B articles, and three of their 18 cells already hold
an analysis in the chosen configuration — those are reused rather than rerun, if
their records show the same prompt, schema, and settings. Analyses go to
`outputs/analyses/<slug>/` and evaluations to `outputs/evaluations/<slug>/`, so
an analysis is never conflated with the judgment of it, and either can be
regenerated without the other.

This phase also establishes what a *collection* needs that a single analysis
does not: provenance for all 16 articles, a record of which configuration
produced each analysis, and enough consistency for Phase 4 to compare them.

---

## Phase 4 — Synthesis Agent

### Goal

Compare accepted analyses for agreements, disagreements, methodological
differences, limitations, and open questions, preserving which source said
what, and evaluate the result.

Synthesis receives no research question. Source attribution is the hard
requirement: a synthesis that blends two sources into one unattributed claim has
destroyed the thing it was built to preserve, and a disagreement must name both
sides. The evaluation has to be designed for synthesis rather than borrowed from
Phase 2 — faithfulness here means faithfulness to the analyses and the
attribution, which is a different question from faithfulness to one source, and
the new failure mode is a manufactured agreement or disagreement between sources
that do not actually address the same point.

---

## Phase 5 — Literature Review Agent

### Goal

Given an explicit research question, find candidate articles, explain why each
is relevant, and let the researcher select which to add to the collection.

This is the only question-aware agent. It proposes and explains; it does not
add. A selected article enters the Phase 3 path — provenance, analysis,
evaluation — and the explanation of relevance is recorded with it, since it is
the agent's reasoning about a question and not a property of the source.

---

## Phase 6 — RAG

### Goal

Connect retrieval to all three agents so the researcher can navigate source
material, analyses, evaluations, and syntheses using explicit questions,
including literature-review questions.

Four kinds of thing are retrievable and they are not interchangeable: a passage
from a source, a claim from an analysis, a judgment from an evaluation, and a
comparison from a synthesis. Retrieval has to preserve which kind it returned
and which source it came from, and it must not let an analysis's
`model_inferred` content come back as something a source said. Retrieval quality
is evaluated separately from the quality of what the model generates from what
it retrieved.

Relevance judgments here depend on the distinctions the research question draws
— freshwater, drinking-quality water, and water suitable for a particular
process are not interchangeable, and desalination is a supply candidate under
investigation rather than the answer. A retrieval step that treats those as
synonyms will return confidently wrong material, so they belong in the
retrieval evaluation as explicit cases rather than being left to the embedding. Single-source analysis stays question-independent: retrieval
serves the researcher and the question-aware agents, and never feeds the
research question back into the analysis step.
