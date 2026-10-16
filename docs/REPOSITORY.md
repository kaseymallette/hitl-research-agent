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

### `models.py` (302 lines)

Every research type, in one module, in two layers:

- **`ExtractedAnalysis`** is the schema sent to the API — research problem,
  claims, methodology, assumptions, limitations, proposed solutions, open
  questions. Every field is content the model may supply.
- **`SourceAnalysis`** wraps that content with the three things the application
  owns and a model has no legitimate value for: `id`, `provenance`, `analyzed_at`.

Inside the model's content: `Claim` (text, `statement_origin`, evidence,
optional `support_assessment`), `Evidence` (text, locator, citations,
`evidence_form`, `relationship_to_claim`), `Citation`, `Methodology`, and a
single `Statement` type used for the research problem, assumptions, limitations,
proposed solutions, and open questions.

Also here: `Provenance`; `SourceDocument`, the analysis input contract, carrying
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

### `analysis.py` (448 lines)

`analyze_source()`: build the messages, call the model, accept one correction
attempt if the output does not fit the schema, return an `AnalysisResult`.

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

### `prompts.py` (220 lines)

`SYSTEM_PROMPT` — the analysis instructions — plus the per-input-mode layout
instructions and the correction message. Almost entirely prompt text rather than
code, and **unchanged by the consolidation**: Phase 1 holds it fixed so input
format and model stay the only variables.

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

### `run_analysis.py` (273 lines)

One cell of the matrix: one article, one input method, one model. Writes
`analysis.json` (the analysis as the model returned it) and `run_record.json`
(configuration, usage, calculated cost, runtime, request ids, every attempt) to
`outputs/ab_testing/<slug>/<config>/`.

An article with no figures, equations, or multi-level table headers produces no
crops. The runner sends prepared text alone, records `input_mode` and
`crops_sent`, and keeps the article in the experiment: the arm is the input
workflow, and the crop count is a property of the article.

```bash
uv run python scripts/run_analysis.py --pdf data/research/ab_testing/<name>.pdf \
    --title "..." --input pdf --model gpt-6.1-sol --effort medium --confirm-paid
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

## `tests/` — 73 tests

| File | Tests | Covers |
| --- | --- | --- |
| `preparation/test_prepare.py` | 27 | PDF extraction: reading order, hyphen joining, header removal, annotation placement, crop retention |
| `test_analysis.py` | 16 | The call path: the correction attempt, each run-stopping failure, attempt records, usage arithmetic, attachments resent on correction |
| `test_inputs.py` | 11 | Per-mode attachment validation, that every mode sends the same analysis prompt, byte-exact hashing |
| `test_models.py` | 10 | Application-owned fields rejected from model content, attribution labels required, gap/annotation consistency, JSON round trip |
| `test_cost.py` | 5 | Cost from documented rates, cached input not double-charged, unknown model refused |
| `test_run_analysis.py` | 4 | The runner's input handling against real preparation output: confirmed provenance, a crop per gap, and an article with no crops |

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

16 source PDFs, four of them in `ab_testing/` as the experiment set, plus
`sources.yaml`.

`sources.yaml` currently holds **one** entry, for
`li_et_al_2025_making_ai_less_thirsty` — a collection article, not one of the
four. All four A/B articles need owner-confirmed entries before
`prepare_sources.py` can run on them. That is Phase 1's first task and the only
thing blocking it.

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
