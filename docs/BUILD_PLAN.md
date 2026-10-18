# Build Plan

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

### The matrix

3 articles × 2 input methods × 3 model configurations = **18 analyses**
([ADR-0009](adr/0009-phase-1-matrix-three-configurations-three-articles.md)
revised [ADR-0008](adr/0008-compare-pdf-against-prepared-text.md)'s 2 × 2 over
four articles).

| Articles | `data/research/ab_testing/` | pages | chars |
| --- | --- | --- | --- |
| | `barnett_itzhaki_2026_water_footprint_artificial_intelligence` | 7 | 51k |
| | `katakam_et_al_2027_desalination_systems_data_center_water_needs` | 20 | 107k |
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
`kanbur_et_al_2020_desalination_integrated_data_center_cooling` was the fourth
article; it covered the same topic as `katakam`, the more recent of the two,
and left the experiment to pay for the third configuration. It is in
`data/research/` with the rest of the collection.

### Held constant

The analysis prompt (`SYSTEM_PROMPT`), the output schema (`ExtractedAnalysis`
in `models.py`), the one-correction policy, and the
question-independence of the task. The only intended differences are the input
format, its format-specific layout instructions, and the model configuration.

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

1. Prepare the three articles with `prepare_sources.py`, timing each; record
   gaps and crops.
2. Run the 18 cells with `run_analysis.py`: it takes an article, an input
   method, and a model, and writes `analysis.json` and `run_record.json` with
   usage, calculated cost, and runtime.
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

### Tests

Phase 0 left 73 tests covering the call path, the input modes, the schema rules,
cost, the runner's input handling, and PDF preparation. Phase 1 adds only what the matrix runner itself needs,
offline and with no API calls: that a configuration slug maps to the right input
mode and settings, that a failed cell still writes a run record rather than a
half-written directory, and that `summary.csv` reports what the run records hold.

### Acceptance criteria

- [ ] 18 `analysis.json` files exist, one per cell, indented and readable, each
      the analysis the model returned, unmodified.
- [ ] Each cell has a `run_record.json` with usage, calculated cost, runtime,
      and per-attempt records; no fabricated values.
- [ ] Preparation effort recorded for all three articles.
- [ ] The prompt, schema, and correction policy are identical across all 18
      cells, and that is demonstrable from the records.
- [ ] `summary.csv` lets Phase 2 pick up the comparison without rereading 18
      run records.
- [ ] No quality check anywhere can prevent an analysis from being written.

### What Phase 1 does not decide

Which configuration wins. Counts of claims, evidence items, or citations do not
establish fidelity, and neither does a run completing. Readings of figures,
tables, and equations from either arm are unverified until a human checks them
against the original images. Phase 1 hands Phase 2 artifacts and measurements.

---

## Phase 2 — DeepEval

### Goal

Design metrics and rubrics, evaluate the 18 analyses, and choose the model and
input method on quality and cost together.

### The behavioral axes

The four questions below are what the researcher wants answered. Each is
measured through named behaviors, so a rubric targets a specific failure rather
than a general impression of quality:

| Question | Axes |
| --- | --- |
| Claim attribution | source faithfulness, argument reconstruction |
| Qualification and citation fidelity | citation faithfulness, evidence mapping |
| Interpretation discipline | assumption discipline, limitation discipline, inference control |
| Argument coverage | argument reconstruction, research usefulness |

`research usefulness` is the one axis that is not a faithfulness measure: it
asks whether the analysis is actually usable as research input, which is the
question Phase 1's counts cannot answer and the one most likely to separate the
two models. It is also the axis most at risk of collapsing into the judge's
taste, so it needs the tightest rubric and the closest human spot-checking.

### The four questions to measure

1. **Claim attribution** — do claims marked `author_stated` actually reflect
   what the source says? Faithful paraphrases are acceptable: a paraphrase that
   preserves the authors' meaning is a correct answer, not a defect. v1's
   requirement of a verbatim quotation per author-stated claim was removed for
   this reason and is not to return as a metric.
2. **Qualification and citation fidelity** — are hedges, conditions, scope
   limits, and strength of language preserved rather than softened or
   hardened? Are in-text citation markers and reference entries recorded as the
   source prints them, without invented bibliography detail?
3. **Interpretation discipline** — is `model_inferred` content actually absent
   from the source, and is `author_stated` content actually in it? Both
   directions are errors: an interpretation presented as the authors' claim, and
   an authors' claim demoted to interpretation.
4. **Argument coverage** — are the arguments that matter to the source present?
   Coverage is about what was missed, not about volume; a longer analysis is not
   a better one.

### Decisions this phase must make

- Rubrics specific enough that two runs of the judge on the same analysis agree,
  and the scale each metric reports on.
- The judge model and configuration, and its cost — the judge is itself a paid
  model call across 18 analyses and several metrics.
- How the judge gets the source: it faces the same input-method question the
  analyses do, and a judge that only reads extracted text cannot assess a
  reading of a figure.
- **Human spot checks of the judge**, designed in: a sample the researcher
  scores independently, compared against the judge's scores, so the judge's own
  reliability is evidence rather than assumption. A judge that disagrees with
  the researcher is a finding about the judge.
- Where evaluations are stored, separately from the analyses they assess.

The output is a recommended configuration with the measured quality and cost
behind it, including the cases where the two point in different directions.

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
