# Build Plan

This document turns the phases in [README.md](../README.md) into an engineering
plan. It is developed one phase at a time: the current phase is specified in
full, later phases state their goal and the decisions they must make, and are
filled in once the prior phase is accepted.

This is the v2 plan. It replaces the nine-phase v1 plan. v1 built a working
single-source analysis pipeline and then spent a long sequence of turns on
grounding checks that were ultimately removed; what survives of that history in
this branch is the audit in Phase 0 below. The v1 prompt logs and experiment
outputs were removed with the redesign and remain in git history;
[`docs/prompt_log.md`](prompt_log.md) now indexes one log per v2 phase.

---

## System Architecture

### The three agents

| Agent | Input | Output | Question-aware? |
| --- | --- | --- | --- |
| **Single-source analysis** | one article | one structured JSON analysis | No — never receives a research question |
| **Synthesis** | several accepted analyses | a cross-source comparison | No |
| **Research** | an explicit research question | candidate articles with stated relevance | Yes — this is the only question-aware agent |

Single-source analysis stays question-independent so that an analysis produced
today remains usable for a question asked later, and so that no analysis is
shaped toward a conclusion the researcher is looking for. Synthesis compares
what the sources say to each other, not to a question. Only the research agent
reads the research question, and it only proposes; the researcher selects.

### Workflow contract

```
article + prompt → model → JSON → separate evaluation → accept · reject · revise · rerun
```

Four rules hold across every phase:

1. **Evaluation is separate from production.** Quality assessment never runs
   inside the analysis call and never decides whether the JSON is returned.
2. **No hard quality gates.** Only a technical failure — an API error, an
   unreadable response, output that cannot be parsed into the schema — stops a
   run. A paraphrase instead of a quotation, a claim with no evidence item, a
   thin analysis: these are reported by evaluation and human review, never
   grounds for withholding the result. v1 accumulated such gates and they were
   removed deliberately; they are not to be restored.
3. **Model interpretation stays labelled.** `author_stated` vs.
   `model_inferred` is carried on every claim, assumption, limitation, proposed
   solution, open question, and methodology record — so assumptions the authors
   state stay separable from assumptions the model found the argument needs, and
   limitations the authors acknowledge from limitations the model identified.
   Evidence carries a second, independent split: `verbatim` vs. `paraphrased`.
4. **The human operates a gate, not a reading chair.** Analysis and evaluation
   end at a four-state decision — **accept, reject, revise, rerun** — and only
   accepted analyses enter the research collection. This is a runtime boundary
   rather than a phase: Phase 2 exercises it on the judge's own output, Phase 3
   on what enters the collection, Phase 4 on syntheses. What the researcher
   needs in front of them to make that decision — the analysis, its citations,
   the evaluation scores, and the evaluation's explanations — is therefore a
   requirement on how analyses and evaluations are stored, not a later
   presentation concern.

### Repository layout

```
data/research/                      16 source PDFs
  ab_testing/                       the 4 A/B experiment articles
  sources.yaml                      provenance manifest, owner-confirmed
outputs/
  preparation/<slug>/               extracted text, crops, preparation record
  ab_testing/<slug>/<config>/       Phase 1: analysis.json + run_record.json
  analyses/<slug>/                  Phase 3: analysis in the chosen configuration
  evaluations/<slug>/               Phase 3: evaluation, stored apart from the analysis
  synthesis/                        Phase 4
src/hitl_research_agent/
  models/                           the analysis data model
  extraction/                       the single-source analysis agent
scripts/                            runnable entry points
```

Data folders are named by role, not by phase number, so that a phase
renumbering never moves source material again.

---

## Phase 0 — Review and Redesign

### Goal

Decide what of v1 carries into v2 before any v2 code is written, and restructure
the repository and documentation around the v2 phases.

### What the v1 audit found

v1 is about 1,350 lines of application code and 2,200 lines of tests, with 181
passing tests and clean Ruff/mypy. The single-source analysis pipeline works:
it sends an article to the model with the analysis prompt, accepts one
correction attempt if the output does not fit the schema, records per-attempt
usage and timing, and returns the JSON without judging its quality. That is
already the v2 contract, and it already supports both Phase 1 input methods and
any model/effort pair through configuration.

The dead weight is all downstream of the grounding checks that were removed late
in v1: the helpers that supported them, the scope strings that still describe
them, and a 664-line one-source pilot script built around their failures.

#### Reuse unchanged

| Component | Why it carries over |
| --- | --- |
| `models/` — `SourceAnalysis`, `Claim`/`Evidence`, `Citation`, `Provenance`, `Methodology`, interpreted statements | This is the output structure Phase 1 must hold constant. The `author_stated`/`model_inferred` and `verbatim`/`paraphrased` distinctions are exactly what Phase 2 evaluates. |
| `extraction/pipeline.py` — `analyze_source()` | One call plus one schema correction, attempt records, usage, refusal and incomplete-response detection, no quality gates. The v2 workflow contract, already implemented. |
| `extraction/prompts.py` — `SYSTEM_PROMPT` and the per-input-mode instructions | The core analysis prompt. Phase 1 holds it constant; the input-mode instructions describe layout only, so input format stays the only intended difference between arms. |
| `extraction/attachments.py` | PDF and image attachments with the sha256 of the exact bytes sent, and the documented 50 MB per-request limit. Both Phase 1 input methods are already supported. |
| `extraction/attempts.py`, `extraction/errors.py` | Per-attempt usage (including reasoning and cached-input tokens), timing, request ids, and the error taxonomy. This is Phase 1's measurement instrument. |
| `config.py` — `Settings` | `openai_model`, `openai_reasoning_effort`, `max_output_tokens`, `openai_max_retries`. The whole A/B matrix is a configuration change, not a code change. |
| `scripts/prepare_phase_3_sources.py` | PDF → extracted text, crops, page images, and a preparation record of what text could not represent. The only producer of the text-plus-crops arm. Rename to `prepare_sources.py`. |

#### Simplify

| Component | Change |
| --- | --- |
| `scripts/analyze_pdf.py` | Generalize into the single analysis runner: both input methods, the configuration in the output path, and usage, cost, and runtime in the run record. **It also has a live bug** — line 153 reads `result.grounding_notes`, a field removed from `AnalysisResult`, so a *successful* run raises `AttributeError` after writing `analysis.json` and before writing `run_record.json`. Phase 1 cannot measure anything until this is fixed. |
| `scripts/run_li_input_pilot.py` (664 lines) | **Deleted.** Hard-coded to one article — Li, which is not in the A/B set — and built around pre-call token projection, an offline dry run, a payload inventory, and a cross-invocation spending guard. Three things from it are worth carrying into the Phase 1 matrix runner: the documented per-model rate table, cost calculated from *actual* reported usage, and the timing and usage records. The projection, the dry run, and the per-run approval gates are not. |
| `extraction/schemas.py` — `ANALYSIS_SCOPE`, `ANALYSIS_SCOPE_PDF`, `ANALYSIS_SCOPE_TEXT_AND_CROPS` | Three paragraphs that still describe verbatim-grounding checks against a declared grounding reference. Those checks no longer exist, so the strings are now false on a saved result. Replace with one short, true sentence per input method, saying what the model received and that image readings are unverified. |
| `extraction/annotations.py` | **Done.** `grounding_view()`, `contains_reserved_character()`, and `SENTINEL` are gone, along with their exports and the tests covering them. `reserved_character_problems()` now checks the two annotation delimiters only, which is one character less than before and costs nothing, since nothing produces the sentinel any more. `find_annotations`, `format_annotation`, and `reserved_character_problems` stay: the preparation script and the `SourceDocument` validator that ties in-text annotations to declared gaps both still need them for the text-plus-crops arm. |

#### Remove

| Component | Why |
| --- | --- |
| `tests/pilots/test_li_input_pilot_guard.py` (193 lines) | **Deleted** with the pilot script it tested; it covered that script's spending guard and approval gates. |
| The v1 nine-phase roadmap in `README.md`, and Phases 4–9 of the v1 build plan | Replaced by the v2 phases. |
| Phase-numbered data and output folders | Done in this phase (below). |

#### Build new

Nothing in v1 covers evaluation, synthesis, research, or retrieval. DeepEval is
named in the v1 README but was never added as a dependency and no evaluation
code exists. Phases 2, 4, 5, and 6 start from nothing.

### Restructuring performed

- `data/phase_3/*.pdf` (12 articles) → `data/research/`
- `data/phase_3/ab_testing/*.pdf` (4 articles) → `data/research/ab_testing/`
- `data/phase_3/sources.yaml` → `data/research/sources.yaml`, with its `pdf:`
  path updated
- `data/phase_2/` (the v1 development source, not one of the 16), `outputs/phase_2/`
  (8 v1 analyses of it), and `outputs/phase_3/` (the Li input-format experiment:
  source PDF, extracted text, 8 crops, 3 analyses) were removed from this branch.
  They remain in git history at commit `0fd1ccf` and earlier.

Code removed: `scripts/run_li_input_pilot.py` and
`tests/pilots/test_li_input_pilot_guard.py`, and the dead grounding helpers
(`grounding_view`, `contains_reserved_character`, `SENTINEL`) with their exports
and tests.

Path references updated: the manifest's own `pdf:` entry, `DEFAULT_MANIFEST` in
the preparation script, and the `analyze_pdf.py` usage example. `README.md` and
this plan were rewritten. 169 tests pass, with Ruff, formatting, and mypy clean.

### Open items carried into Phase 1

1. **The manifest covers none of the A/B articles.** `data/research/sources.yaml`
   holds a single entry, for `li_et_al_2025_making_ai_less_thirsty`, which is a
   collection article and not one of the four. All four A/B articles need
   owner-confirmed provenance entries before preparation can run, since the
   preparation script reads the manifest and the manifest records these as
   confirmed by the project owner rather than inferred. **This needs the project
   owner.**
2. **The `analyze_pdf.py` crash** above blocks measurement.
3. **No preparation artifacts exist.** `outputs/` was removed with the v1
   material, so Phase 1 prepares all four A/B articles from their PDFs and times
   that work as it goes, which is what the preparation-effort measurement needs
   anyway.

### Acceptance criteria

- [x] Every v1 component has a reuse, simplify, or remove verdict with a reason.
- [x] Data and output folders are named by role; no phase-numbered folders
      remain; nothing was deleted.
- [x] README is short and describes the three agents, the workflow, and the
      seven phases.
- [x] This plan specifies Phase 1 in full.
- [x] Checks pass after the restructuring.

---

## Phase 1 — A/B Testing

### Goal

Establish, by measurement rather than assumption, whether preparing a PDF into
extracted text plus crops buys anything over sending the PDF itself, and
whether the expensive model buys anything over the cheap one. v1 never compared
these: it assumed extracted text because its first implementation needed a
local text reference, and the one paired comparison it ran was judged by
grounding checks that favored the arm receiving the prepared text, so it settled
nothing.

Phase 1 produces the evidence. It does not choose — Phase 2 chooses, on quality
and cost together.

### The matrix

4 articles × 2 input methods × 2 model configurations = **16 analyses**.

| Articles | `data/research/ab_testing/` | pages | chars |
| --- | --- | --- | --- |
| | `barnett_itzhaki_2026_water_footprint_artificial_intelligence` | 7 | 51k |
| | `kanbur_et_al_2020_desalination_integrated_data_center_cooling` | 18 | 82k |
| | `katakam_et_al_2027_desalination_systems_data_center_water_needs` | 20 | 107k |
| | `lei_et_al_2025_water_use_data_center_workloads` | 60 | 97k |

| Input method | `input_mode` | What the model receives |
| --- | --- | --- |
| Full PDF | `pdf` | the original PDF; the API supplies its text layer and page images |
| Extracted text + crops | `prepared_text_and_crops` | the prepared text, plus one retained crop per item preparation could not represent |

| Model configuration | Model | Reasoning effort |
| --- | --- | --- |
| Sol medium | `gpt-6.1-sol` | `medium` |
| Astra low | `gpt-6-astra` | `low` |

Configuration slug, used in output paths: `{pdf,text_crops}__{sol-medium,astra-low}`.

The page spread is deliberate. The PDF arm's input cost scales with page count,
so `lei` at 60 pages is the stress case for that arm, and `barnett` at 7 pages
the cheap case. If the two arms differ in cost, they will differ most there.

### Held constant

The analysis prompt (`SYSTEM_PROMPT`), the output schema (`ExtractedAnalysis`
and the `models/` structure), the one-correction policy, and the
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
  quality difference it finds.
- **Runtime** — wall clock per attempt and per analysis.
- **Attempts** — outcome, request id, and problems for each, including a first
  attempt that failed the schema.

Per article, once, in a preparation record shared by both `text_crops` cells:

- **Preparation effort** — wall-clock preparation time, number and kind of
  preparation gaps (figures, equations, multi-level table headers), number of
  crops retained, and any manual intervention needed. The `pdf` arm's
  preparation effort is zero; owner-confirmed provenance is needed by both arms
  and is not attributed to either.

### Output layout

```
outputs/ab_testing/<slug>/<config>/analysis.json      the analysis, indented, unchanged
outputs/ab_testing/<slug>/<config>/run_record.json    usage, cost, runtime, attempts
outputs/ab_testing/summary.csv                        one row per cell, for Phase 2
outputs/preparation/<slug>/                           extracted text, crops, preparation record
```

A cell holds the analysis the model returned. A thin or heavily paraphrased
analysis is a result, recorded as-is for Phase 2 to assess. A *technical*
failure — API error, unreadable response, output that will not parse — is not a
result: record it and rerun that cell.

### Implementation tasks

1. Fix the `analyze_pdf.py` `grounding_notes` crash.
2. Add owner-confirmed provenance entries for the four A/B articles to
   `data/research/sources.yaml`. **Blocked on the project owner.**
3. Rename `prepare_phase_3_sources.py` → `prepare_sources.py`; update its
   references.
4. Prepare the four articles, timing each; record gaps and crops.
5. Generalize the analysis runner into a matrix runner: takes an article and a
   configuration slug, selects the input mode, loads the PDF or the prepared
   text plus crops, writes `analysis.json` and `run_record.json` to the cell.
   Carry over the rate table and cost-from-actual-usage from the pilot script.
6. Simplify the three `ANALYSIS_SCOPE` strings so a saved result describes what
   actually happened.
7. Run the 16 cells. Write `summary.csv`.

Cost: on the one measured v1 data point, two Sol-medium analyses of a 36.6k-char
article, each including a correction attempt, had a combined calculated cost of
$0.5173 — about $0.26 per analysis. These articles are 1.4–2.9× that length, the
removal of the quality gates should make most runs single-attempt, and Astra's
rates are 5× Sol's. The order of magnitude for all 16 is therefore roughly
$10–15, dominated by the eight Astra cells. That is a projection from one
article, not a cap; the runner should take an explicit per-run confirmation and
report actual cost as it goes.

### Tests

Offline, with no API calls: configuration slug → input mode and settings;
attachment assembly for both arms; the run record capturing usage, cost, and
runtime from a faked response; a cell with a first-attempt schema failure
recording both attempts; cost calculation against known rates and usage; and
that a technical failure writes a run record rather than a half-written cell.

### Acceptance criteria

- [ ] 16 `analysis.json` files exist, one per cell, indented and readable, each
      the analysis the model returned, unmodified.
- [ ] Each cell has a `run_record.json` with usage, calculated cost, runtime,
      and per-attempt records; no fabricated values.
- [ ] Preparation effort recorded for all four articles.
- [ ] The prompt, schema, and correction policy are identical across all 16
      cells, and that is demonstrable from the records.
- [ ] `summary.csv` lets Phase 2 pick up the comparison without rereading 16
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

Design metrics and rubrics, evaluate the 16 analyses, and choose the model and
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
  model call across 16 analyses and several metrics.
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

Four of the 16 are the A/B articles, and four of their 16 cells already hold an
analysis in the chosen configuration — those are reused rather than rerun, if
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

## Phase 5 — Research Agent

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
