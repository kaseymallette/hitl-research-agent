# Repository Inventory

Every file in the repository, what it is for, and whether it earns its place.
Written at the end of Phase 0 so the whole codebase can be reviewed at once.

Totals: **1,675 lines** of application code in `src/`, **958 lines** of
scripts, **2,506 lines** of tests running **169 tests**. The test-to-code ratio
is the thing most worth arguing about, and there is a section on it at the end
with a specific recommendation.

---

## Application code — `src/hitl_research_agent/` (1,675 lines)

This is the importable package. The directory name is the import name, and the
`src/` wrapper exists so the package can only be imported through the editable
install rather than from the working directory — which means the tests exercise
what would actually ship.

### `config.py` (17 lines)

One `Settings` class reading `.env` and the environment: API key, model,
reasoning effort, max source characters, optional output-token cap, optional
retry override.

**Why it exists:** the whole A/B matrix is a change to two of these fields. If
model and effort were hard-coded anywhere, Phase 1 would need code changes per
cell instead of configuration.

### `models/` (267 lines, 8 files) — the research data model

What an analysis *is*, as validated Pydantic types. Every field that can hold
either the source's position or the model's carries `statement_origin`.

| File | Lines | Holds |
| --- | --- | --- |
| `_base.py` | 16 | `ResearchBaseModel` (rejects unknown fields), `NonEmptyStr`, the shared `statement_origin` description |
| `analysis.py` | 31 | `SourceAnalysis` — the top-level object: provenance, research problem, claims, methodology, assumptions, limitations, proposed solutions, open questions, `analyzed_at` |
| `claim.py` | 65 | `Claim` and `Evidence`, including `evidence_form`, `relationship_to_claim`, and `support_assessment` |
| `citation.py` | 30 | `Citation` — the in-text marker as printed, and the matching reference entry if one is present |
| `interpreted.py` | 32 | `InterpretedStatement` and the five single-field types built on it: research problem, assumption, limitation, proposed solution, open question |
| `methodology.py` | 16 | `Methodology` — design, data sources, scope, analysis methods |
| `provenance.py` | 49 | `Provenance` — title, authors, date, type, DOI, publisher, URL, retrieval time, plus `source_id` so re-analyses of one source are recognizable |
| `__init__.py` | 28 | The public surface |

**Why eight files for 267 lines:** they are split by concept rather than by
size, and `claim.py` is the only one anyone reads often. Merging them into one
`models.py` of about 240 lines would be defensible. Nothing depends on the split.

**Why so many single-field types:** `Assumption`, `Limitation`,
`ProposedSolution`, `OpenQuestion`, and `ResearchProblem` are identical —
`text` plus `statement_origin`. They exist as separate types so the schema sent
to the model names them, and so a function taking a `Limitation` cannot be
handed an `OpenQuestion`. The cost is five class definitions doing nothing else.

### `extraction/` (1,391 lines, 9 files) — the single-source analysis agent

| File | Lines | Does |
| --- | --- | --- |
| `pipeline.py` | 476 | `analyze_source()`: build messages, call the model, classify the outcome, allow one correction attempt if the output does not fit the schema, assemble a `SourceAnalysis`, record every attempt. The only place an API call happens |
| `schemas.py` | 245 | The model-facing schema (`ExtractedAnalysis` and friends — the data model minus every application-owned field like `id`), `SourceDocument` (the input contract), `AnalysisResult` (what comes back), and the three `ANALYSIS_SCOPE` strings |
| `prompts.py` | 220 | `SYSTEM_PROMPT` — the analysis instructions — plus the per-input-mode layout instructions and the correction message |
| `attachments.py` | 175 | Loading a PDF or a crop, hashing the exact bytes sent, and rejecting an attachment set that does not match the declared input mode |
| `errors.py` | 94 | The failure taxonomy: too large, refused, incomplete, parse error, validation error. Each carries the usage spent before it failed |
| `annotations.py` | 62 | The `⟦PREP-ANNOTATION …⟧` syntax marking material preparation could not extract, and the check that source text contains no stray delimiters |
| `attempts.py` | 61 | `AttemptRecord` and `AttemptUsage`: outcome, request id, timing, token usage including reasoning and cached-input tokens |
| `__init__.py` | 58 | The public surface, re-exporting what callers use |

**Why `pipeline.py` is 476 lines:** about 180 of those are the four outcome
branches — refusal, incomplete generation, unparseable output, schema-invalid
content — each of which appends an attempt record *before* raising, so a
failure still reports what it cost. That is the machinery Phase 1's cost and
runtime measurement depends on. The rest is one call path plus one correction.

**Why `schemas.py` duplicates the data model:** `ExtractedAnalysis` mirrors
`SourceAnalysis` without `id`, `provenance`, or `analyzed_at`, because those are
application-owned and a model has no legitimate value to supply for them. The
duplication is deliberate: it is what stops a model from inventing a UUID or a
retrieval timestamp. It also means adding a field means editing two files.

**Why the prompt is 220 lines:** nearly all of it is `SYSTEM_PROMPT`, which
grew one instruction at a time as v1 found extraction failures — scan the
conclusion, don't soften claims, don't merge distinct claims, record citations
as printed. It has never been shortened or tested for whether every instruction
still earns its tokens. Phase 1 holds it fixed, so that question belongs to
Phase 2.

---

## Scripts — `scripts/` (958 lines)

Not part of the package: not installed, not shipped, and not type-checked
(`mypy src` only covers `src/`).

### `prepare_sources.py` (793 lines)

PDF → cleaned text, element crops, page images, and a preparation record.
Reads `data/research/sources.yaml` for owner-confirmed provenance. Two
commands: `prepare --slug` and `page --slug --page N`.

What the 793 lines actually do: extract text and tables with `pymupdf4llm` in
layout mode; correct reading order where block geometry shows a run of
paragraphs jumping between columns; remove recurring headers and footers; join
line-break hyphens only where the document's own vocabulary supports it; keep
page locators outside the text; render a crop for every figure, equation, and
multi-level table header, and a page image for every page; and declare, without
any heuristic deciding whether a given figure "came out well," the three things
this method cannot represent faithfully.

**Why it is the largest file in the repository:** PDF extraction is genuinely
hairy, and this is the part where silent corruption would do the most damage —
a column-order mistake invents sentences the authors never wrote. It is also
the one file whose behavior is worth its 416 lines of tests.

**Why it is a script and not a module:** it is run by hand, per source, and
produces artifacts rather than being imported. If Phase 3 needs it in a
pipeline, it moves into `src/`.

### `analyze_pdf.py` (165 lines)

Sends one PDF through `analyze_source()` with the analysis prompt and writes
`analysis.json` plus a `run_record.json` holding model, usage, timing, request
ids, and per-attempt outcomes. Requires `--confirm-paid`.

**Why it exists:** it is the complete v2 workflow for one article — article plus
prompt, to model, to readable JSON. Phase 1 grows it into the matrix runner.

---

## Tests — `tests/` (2,506 lines, 169 tests)

No `__init__.py` anywhere: pytest collects by path. The directories mirror the
package's internal structure, minus the package-name level, because test modules
are never imported by name.

| File | Tests | Lines | Covers |
| --- | --- | --- | --- |
| `preparation/test_prepare.py` | 27 | 416 | PDF extraction: reading order, hyphen joining, header removal, annotation placement, crop retention, refusal on reserved characters |
| `extraction/test_pipeline.py` | 22 | 629 | The call path: one attempt, the correction attempt, each failure classification, attempt records, usage arithmetic |
| `extraction/test_prompts.py` | 21 | 132 | That specific phrases appear in `SYSTEM_PROMPT` |
| `extraction/test_input_modes.py` | 20 | 437 | Attachment validation, message assembly per input mode, what a result records about its own input |
| `models/test_claim.py` | 14 | 138 | `Claim` and `Evidence` field behavior |
| `extraction/test_schemas.py` | 9 | 146 | `SourceDocument`'s validator tying in-text annotations to declared gaps |
| `extraction/test_preparation_gaps.py` | 8 | 172 | Gaps and the scope statement surviving a JSON round trip |
| `models/test_provenance.py` | 8 | 67 | `Provenance` fields |
| `models/test_analysis.py` | 6 | 68 | `SourceAnalysis` assembly |
| `models/test_citation.py` | 5 | 36 | `Citation` fields |
| `test_config.py` | 5 | 39 | `Settings` defaults and overrides |
| `models/test_methodology.py` | 4 | 35 | `Methodology` fields |
| `extraction/test_annotations.py` | 3 | 61 | Annotation syntax and reserved-character rejection |
| `models/test_interpreted.py` | 3 | 41 | The interpreted-statement base |
| `preparation/conftest.py` | — | 18 | Loads the preparation script by file path, since `scripts/` is not importable |
| `preparation/pdf_fixtures.py` | — | 71 | Builds small synthetic PDFs so the extraction tests need no real paper |

### On the test count

169 tests for ~2,600 lines of code is high, and not all of it is earning its
keep. Three groups, in descending order of value:

**Worth keeping (about 86 tests).** `test_prepare.py`, `test_pipeline.py`,
`test_input_modes.py`, and `test_schemas.py` cover logic where a silent bug
would corrupt research data or lose the cost record Phase 1 depends on. The
preparation tests are the most valuable in the repository: they are the only
thing standing between a reading-order bug and sentences the authors never
wrote.

**Low value (21 tests).** All of `test_prompts.py`. These assert that exact
phrases appear in the prompt — `assert "not incidental color" in lowered`. They
test wording, not behavior, and they do not check that the prompt *works*; only
an evaluation can do that. Every future prompt revision breaks them, and the
correct response will always be to update the assertion, which means they can
only ever cost time. They are a changelog written as a test suite.

**Partly redundant (about 25 of the 40 model tests).** `test_whitespace_only_text_rejected`,
`test_text_is_stripped`, `test_unexpected_field_rejected`, and
`test_*_default_to_an_empty_list` test Pydantic's own guarantees —
`StringConstraints`, `extra="forbid"`, `default_factory` — once per model, six
times over. One test establishing that `ResearchBaseModel` rejects unknown
fields and strips strings would cover all of them. One test also asserts on a
field's *description* text, which is the same mistake as `test_prompts.py`.

**Recommendation, for your decision:** delete `test_prompts.py` entirely and
collapse the per-model library-behavior tests into a handful on
`ResearchBaseModel`. That would take 169 tests to roughly 110 while losing no
coverage of anything this project actually implements. I have not done it.

---

## Data — `data/research/`

16 source PDFs, four of them in `ab_testing/` as the experiment set, plus
`sources.yaml`.

`sources.yaml` is the provenance manifest and currently holds **one** entry,
for `li_et_al_2025_making_ai_less_thirsty` — a collection article, not one of
the four. All four A/B articles need owner-confirmed entries before
`prepare_sources.py` can run on them. This is Phase 1's first task and the only
thing blocking it.

---

## Documentation — `docs/`

| File | For |
| --- | --- |
| `BUILD_PLAN.md` | The phases in engineering detail: Phase 0's audit record, Phase 1 specified in full, Phases 2–6 at goal level |
| `REPOSITORY.md` | This file |
| `prompt_log.md` | Index of the per-phase prompt logs |
| `prompt_logs/phase_1.md` … `phase_6.md` | One template per phase, for the prompts given and what came back |

---

## Project configuration

| File | For |
| --- | --- |
| `pyproject.toml` | Dependencies, the `src/` package declaration, Ruff (line length 100; E, F, I, UP, B), mypy (strict, `src` only), and a `required-environments` pin because `onnxruntime` ships no recent Intel-macOS wheels |
| `uv.lock` | The resolved dependency set |
| `.python-version` | 3.12, matching `requires-python` and CI |
| `.pre-commit-config.yaml` | Ruff, formatting, and mypy on commit |
| `.github/workflows/ci.yml` | The same four checks plus pytest, on push to main and on every pull request |
| `.env` / `.env.example` | `OPENAI_API_KEY`. `.env` is gitignored |
| `.gitignore` | Secrets, caches, virtualenvs, editor and OS files |

Six runtime dependencies: `langchain-core` and `langchain-openai` for the
Responses API call, `pydantic` and `pydantic-settings` for the schemas and
config, `pymupdf4llm` (pinned, because its layout-mode behavior was verified
against that exact version) for extraction, and `pyyaml` for the manifest.
Four dev dependencies: pytest, ruff, mypy, pre-commit. DeepEval is named in the
README as a Phase 2 addition and is deliberately not installed yet.
