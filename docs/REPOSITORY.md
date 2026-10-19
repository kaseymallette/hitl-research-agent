# Repository Inventory

Why each file exists, and what was removed to get here. The repository was
consolidated at the end of Phase 0 down to what the A/B experiment actually
needs: from 1,675 lines across 17 source files and 181 tests, to 1,289 lines
across 6 and 73 tests.

The structure itself — the annotated tree, with line counts — is in
[README.md](../README.md#repository-structure), kept in one place. This document
is the reasoning behind it.

---

## What the code has to do

Everything here supports five things, and nothing else was kept:

1. Analyze an article, given either a full PDF or prepared text plus image crops.
2. Compare GPT-6.1 Sol at medium effort against GPT-6 Astra at low effort.
3. Return structured claims, evidence, author/model attribution, and the
   model's assessments of the authors' arguments.
4. Record the output, the configuration, token usage, calculated cost, and runtime.
5. Leave evaluation and human review as separate steps.

---

## `src/hitl_research_agent/`

The importable package. The directory name is the import name; the `src/`
wrapper means the package can only be imported through the editable install,
not from the working directory, so tests exercise what would ship.

### `models.py` (312 lines)

Every research type, in one module, in two layers:

- **`ExtractedAnalysis`** is the schema sent to the API: the close reading, a
  `reading_path` of steps in the order the document unfolds. Every field is
  content the model may supply.
- **`SourceAnalysis`** wraps that content with the three things the application
  owns and a model has no legitimate value for: `id`, `provenance`, `analyzed_at`.
- **`ArgumentEvaluation`** is the schema for the second call: one prose field,
  the model's own judgment of the argument. **`SourceArgumentEvaluation`** wraps
  it with its own `id`, the `analysis_id` of the close reading it was given,
  `provenance`, and `evaluated_at` ([ADR-0012](adr/0012-close-reading-and-argument-evaluation-are-two-calls.md)).

Inside the model's content: `ReadingStep` (location, the author's moves in the
terms of argument, the claims stated there, and what the step means given what
came before), `Claim` (text, `statement_origin`, evidence), `Evidence` (text,
locator, citations, `evidence_form`, `relationship_to_claim`), and `Citation`.

Also here: `Provenance`, whose `source_id` names the source rather than any one
analysis of it — `source_id_for()` derives it from the slug, so every analysis of
one article shares it without anything being stored, and changing
`SOURCE_ID_NAMESPACE` would change every source's id; `SourceDocument`, the analysis input contract, carrying
the validator that ties in-text preparation annotations to declared gaps so a
result cannot claim coverage its text lacks; `PreparationGap`; and the three
`ANALYSIS_SCOPE` strings that travel on a saved result to say what the model saw.

**Consolidated from eight files.** `InterpretedStatement` plus `ResearchProblem`,
`Assumption`, `Limitation`, `ProposedSolution`, and `OpenQuestion` were six
classes with identical fields — one `Statement` replaces them, and the list a
statement appears in is what distinguishes it. `ExtractedClaim` and
`ExtractedEvidence` were duplicates of `Claim` and `Evidence` that existed only
to strip UUIDs the model must not supply; those UUIDs were never read anywhere,
so dropping them removed both duplicate classes and the 40-line function that
copied between them.

### `analysis.py` (522 lines)

`analyze_source()`: build the messages, call the model, accept one correction
attempt if the output does not fit the schema, return an `AnalysisResult`.
`evaluate_argument()` is the second call: it sends the evaluation prompt, the
article in the same input mode, and the close reading, with the same
one-correction policy, and returns an `ArgumentEvaluationResult`
([ADR-0012](adr/0012-close-reading-and-argument-evaluation-are-two-calls.md)).

Also `AttemptRecord` and `AttemptUsage` — one per call, kept on success and on
failure, holding outcome, request id, timing, and the token usage the response
reported including reasoning and cached-input tokens — and `AnalysisError`,
which carries a `kind`: `source_too_large`, `transport`, `refused`,
`incomplete`, or `invalid_after_correction`.

**The run-stopping rules live here and are deliberately narrow.** A refusal and
a truncated generation stop the run without spending the correction, since
neither is something corrective feedback can fix. A response with no usage
metadata is a failure rather than a zero, because reporting zero tokens for a
call that happened would corrupt the cost record. Nothing about analysis
*quality* stops a run.

**Consolidated from `pipeline.py` (476), `attempts.py` (61), `errors.py` (94).**
Six exception classes became one with a `kind` field — nothing ever caught the
subclasses individually. The response-metadata allowlist and its JSON-safety
helpers went: they recorded fields nobody read.

### `prompts.py` (283 lines)

`SYSTEM_PROMPT` — the close-reading instructions, written as an invitation to
read the document step by step as a first-time reader — plus the per-input-mode
layout instructions and the correction message. `EVALUATION_PROMPT` and
`build_evaluation_messages()` are the second call: the model's own evaluation of
the argument, kept in a prompt of its own so the close reading's restraint does
not apply to it. Almost entirely prompt text rather than
code, and **unchanged by the consolidation**: Phase 1 holds it fixed so input
format and model stay the only variables. ADR-0010 and ADR-0011 revised it
during Phase 1 and were superseded by ADR-0012, which moves the
argument evaluation to its own call and turns the close reading into a reading
path; only Barnett had run, and it is rerun under both calls.

### `inputs.py` (238 lines)

What the model receives. Attachment loading for a PDF or a crop, hashing exactly
the bytes that are sent, and the per-mode validation that rejects a mismatched
attachment set. Also the `⟦PREP-ANNOTATION …⟧` syntax marking material
preparation could not extract, and the check that source text carries no stray
delimiters.

### `cost.py` (64 lines)

Documented per-model rates and `calculated_cost()`, which multiplies them by the
usage a response actually reported. Cached input is billed at the cached rate and
subtracted from the full-rate charge. An unrecorded model raises rather than
guessing a rate. Every result says it is calculated and not confirmed billing.

**New in the consolidation.** The deleted pilot script had this tangled with
pre-call token projection and a spending guard; only the rate table and the
cost-from-actual-usage arithmetic were worth keeping.

### `config.py` (17 lines)

One `Settings` reading `.env`: API key, model, reasoning effort, max source
characters, optional output-token cap, optional retry override. The A/B matrix is
a change to two of these fields, which is why they are configuration.

---

## `scripts/`

Not installed, not shipped, not type-checked (`mypy src` covers `src/` only).

### `run_analysis.py` (470 lines)

One cell of the matrix: one article, one input method, one model. Writes
`analysis.json` (the close reading as the model returned it),
`argument_evaluation.json` (the model's own evaluation of the argument, from the
second call), and `run_record.json` (configuration, usage, calculated cost,
runtime, request ids, every attempt, for each call and in total) to
`outputs/ab_testing/<slug>/<config>/`. If the evaluation fails, the close
reading is still written and the record says so.

The record is built to be complete rather than convenient. Usage totals,
reasoning tokens included, are summed from every attempt that reported usage,
so a cell that failed after a billed first attempt still records what it cost.
It carries sha256 fingerprints of the system prompt, the format-specific
instructions, and the output schema, plus the git commit and whether `src/` or
`scripts/` had uncommitted changes, which is what makes "the prompt, schema, and
correction policy were identical" checkable from the records. Client retries are
off, so every request is an attempt the record shows. The cell directory is
created only once there is a record to write, and a cell that already holds an
analysis is refused rather than overwritten. Rerunning a failed cell keeps the
failed run's record as `failed_run_<n>.json`, since its tokens were billed.

An article with no figures, equations, or multi-level table headers produces no
crops. The runner sends prepared text alone, records `input_mode` and
`crops_sent`, and keeps the article in the experiment: the arm is the input
workflow, and the crop count is a property of the article.

Both arms take provenance from `data/research/sources.yaml`: the PDF arm reads
the manifest entry for its slug and refuses to run without one, and the text arm
reads the `provenance.json` preparation copied from it. The title and source
type go into the prompt, so a single source for them keeps the prompt identical
across arms, and the PDF arm's `analysis.json` carries the same full provenance
as the text arm's, including the `source_id` derived from the slug.

```bash
uv run python scripts/run_analysis.py --pdf data/research/ab_testing/<name>.pdf \
    --input pdf --model gpt-6.1-sol --effort medium --confirm-paid
```

```bash
uv run python scripts/run_analysis.py --slug <slug> --input text_crops \
    --model gpt-6-astra --effort low --confirm-paid
```

Replaces `analyze_pdf.py`, which handled only the PDF arm and recorded no cost.

### `prepare_sources.py` (793 lines)

PDF → cleaned text (`prepared_text.txt`), element crops, page images, and a
`prep_record.json`, plus the owner-confirmed `provenance.json` it reads from
`data/research/sources.yaml`. Two commands:
`prepare --slug` and `page --slug --page N`.

It extracts text and tables with `pymupdf4llm` in layout mode, corrects reading
order where block geometry shows paragraphs jumping between columns, removes
recurring headers and footers, joins line-break hyphens only where the
document's own vocabulary supports it, keeps page locators outside the text, and
declares — without any heuristic judging whether a figure "came out well" — the
three things this method cannot represent faithfully.

**Untouched by the consolidation, on purpose.** This pipeline was an assistant's
recommendation, not an established requirement, and it is one of the two input
options the experiment is testing. Changing it would change what that arm
produces. It will not be expanded before the comparison shows it is worth
keeping. If it loses, most of these 793 lines go.

---

## `tests/` — 89 tests

| File | Tests | Covers |
| --- | --- | --- |
| `preparation/test_prepare.py` | 27 | PDF extraction: reading order, hyphen joining, header removal, annotation placement, crop retention |
| `test_analysis.py` | 18 | The call path: the correction attempt, each run-stopping failure, attempt records, usage arithmetic, attachments resent on correction, and the evaluation call's own prompt and inputs |
| `test_inputs.py` | 11 | Per-mode attachment validation, that every mode sends the same analysis prompt, byte-exact hashing |
| `test_models.py` | 13 | Application-owned fields rejected from model content, attribution labels required, the evaluation schema holding only the model's judgment, a reading step with no claim, gap/annotation consistency, JSON round trip, a stable `source_id` per slug |
| `test_cost.py` | 5 | Cost from documented rates, cached input not double-charged, unknown model refused |
| `test_run_analysis.py` | 15 | The runner, offline: provenance from the manifest in both arms, a crop per gap, an article with no crops, a failed cell's record and cost, prompt and schema fingerprints, no overwrite, no empty cell, failed runs kept on rerun, both documents written, a failed evaluation keeping the close reading |

Supporting files: `preparation/conftest.py` loads the preparation script by file
path, since `scripts/` is not importable, and `preparation/pdf_fixtures.py`
builds small synthetic PDFs so the extraction tests need no real paper.

**Why these.** The preparation tests are the most valuable in the repository: a
reading-order bug invents sentences the authors never wrote, and nothing else
would catch it. The analysis tests exist because Phase 1 is a measurement
exercise — a lost attempt record or a miscounted token is a broken experiment,
not a cosmetic bug.

**What was deleted.** 21 tests asserted that specific phrases appear in
`SYSTEM_PROMPT` (`assert "not incidental color" in lowered`). They tested
wording rather than behavior, could not show the prompt *works* — only
evaluation can — and would break on every prompt revision, where the fix would
always be to update the assertion. Another ~25 tested Pydantic's own guarantees
(whitespace stripping, `extra="forbid"`, `default_factory`) once per model, six
times over; one test on `ResearchBaseModel` now covers the only one we configure.
The rest went with the code they covered.

---

## `data/research/`

16 source PDFs, three of them in `ab_testing/` as the experiment set, plus
`sources.yaml` and `notes/`.

`notes/` holds the researcher's own reading of an article, one Markdown file
per slug: what the source says, its key numbers with their context, and the
researcher's assessment of its argument, kept apart from what the source
states. Each is written before seeing any model analysis of that article, so it
is an independent reference to compare analyses against, and to check the
Phase 2 judge against. It is not model output and does not go under
`outputs/`, which is not in git.

`sources.yaml` currently holds **one** entry, for
`li_et_al_2025_making_ai_less_thirsty` — a collection article, not one of the
four. All four A/B articles need owner-confirmed entries before
`prepare_sources.py` can run on them. That is Phase 1's first task and the only
thing blocking it.

---

## `docs/`

`DESIGN.md` and `BUILD_PLAN.md` (below), this file, `prompt_log.md` and its
per-phase logs in `phases/`, and:

### `DESIGN.md` and `BUILD_PLAN.md`

One document split in two. `DESIGN.md` is what the system is — the three
agents and which of them sees a research question, the workflow contract and
the four rules that hold across every phase, the two-layer data model, and
what the system deliberately does not do. `BUILD_PLAN.md` is the order it
gets built in: six phases, their acceptance criteria, rubrics, and open
items.

They were one file until the architecture section had to be read past to
reach the current phase, and until it became unclear which document a change
to a rule belonged in. The split answers that: a rule that holds whatever
phase you are in is design, and anything with a phase number is the plan.

### `adr/` — 14 files

One architectural decision per record: `0001`–`0012`, plus `template.md` for
new ones and `README.md`, which indexes them and states the conventions.

All eight were back-filled on 2026-10-17 from decisions already made — the
`src/` layout, `statement_origin` as attribution rather than verification, the
model-content split, the exact `pymupdf4llm` pin, the removal of hard quality
gates, question-independence for analysis and synthesis, one `AnalysisError`
with a `kind`, and the decision to settle the input format by experiment.
Each carries the date the decision was made and the commit where it landed.

`0008` is the only one that is not `Accepted`. It is `Provisional`: it records
that the choice between a full PDF and prepared text plus crops is deferred to
the Phase 1 experiment, and states in advance what evidence settles it. When
Phase 1 reports, a new record states the outcome and supersedes it. It is also
why `prepare_sources.py` is frozen — changing it would change what one arm of
the experiment produces.

`0009`, the first record written when its decision was made rather than
back-filled, amends `0008`'s matrix: Sol at high effort is added so that model
and effort are not confounded, and `kanbur` leaves the experiment to keep the
run count near the original, for 18 analyses over three articles.

`0010` adds `argument_assessment` to the analysis schema and prompt: an
assessment of the document as a whole, because claim-by-claim assessment could
not see a conclusion that is announced early and developed only at the end.

`0011` proposed restoring the claims ADR-0010's runs folded together by giving
the model two ordered tasks in one call; tested on two cells, the claims
overshot.

`0012` supersedes both: the close reading and the argument evaluation are two
calls with two prompts and two documents, because the two tasks ask for
opposite stances and pulled on each other in one prompt.

**Why, given that this file already explains most of them.** The two documents
answer different questions and are kept apart on purpose. This file describes
the repository as it stands and is rewritten whenever the repository changes;
a record describes one choice at one moment, with the alternatives that lost
and what the choice cost, and is never rewritten. When a decision is reversed,
a new record supersedes the old one and the old one stays readable.

That immutability is the point. The README names architectural drift as a
thing that happened here: quotation matching became an acceptance gate across
many small changes, none of which chose it. A numbered record gives the next
such change something it has to contradict in writing.

### `ENGINEERING_DIRECTIVES.md`, with `CLAUDE.md` at the repository root

A pair, and only useful together. `ENGINEERING_DIRECTIVES.md` is ten general
directives for writing Python — contracts, data representation before control
flow, no speculative abstraction, complexity and allocation, explicit
invariants, traversal, contained state, policy apart from mechanism, tests of
behavior rather than trivia, and deliberate failure handling. Nothing in it is
specific to this project, by design: it is a baseline that would apply to any
Python repository.

`CLAUDE.md` is what Claude Code loads at the start of every session. It
imports the directives, states how to work here, and then points at the
documentation that does hold this project's specifics — the decision records,
this file, and the build plan.

**Why the pointer section is not redundant.** A general directive and a
project decision can disagree. Directive 10 says to distinguish invalid
external data from transient failure and handle expected failure explicitly;
applied to this codebase, a claim with no evidence item or a `verbatim`
quotation absent from the text reads as invalid data, and the reasonable move
is to raise. That is exactly the acceptance gate
[ADR-0005](adr/0005-no-hard-quality-gates.md) forbids, reached by following a
sound general principle — which is how v1 arrived there. `CLAUDE.md` names the
prohibition so the baseline cannot lead back into it.

---

## Dependencies and configuration

Three choices in `pyproject.toml` are worth knowing. `pymupdf4llm` is pinned to
an exact version, because its layout-mode behavior was verified against that
version and legacy mode silently drops tables. `required-environments` is pinned
to three platforms because `onnxruntime`, pulled in by PyMuPDF's layout support,
ships no recent Intel-macOS wheels and the lockfile would otherwise be
uninstallable. mypy runs strict but only over `src/`, which is why `scripts/` is
exercised by tests rather than by the type checker.

Six runtime dependencies: `langchain-core` and `langchain-openai` for the
Responses API call, `pydantic` and `pydantic-settings` for the schemas and
config, `pymupdf4llm` (pinned, because its layout-mode behavior was verified
against that exact version) for extraction, and `pyyaml` for the manifest. Four
dev dependencies: pytest, ruff, mypy, pre-commit. DeepEval is a Phase 2 addition
and is deliberately not installed yet.
