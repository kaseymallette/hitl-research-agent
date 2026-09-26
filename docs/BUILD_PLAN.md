# Build Plan

This document turns the roadmap in [README.md](../README.md) into an engineering
implementation plan. It is developed collaboratively, one phase at a time.

Each phase is specified with:

- **Goal** — what this phase achieves and why it matters to the overall system
- **Architectural Decisions** — choices made for this phase, with rationale
- **Technologies** — libraries/tools introduced or used in this phase
- **Implementation Tasks** — concrete units of work
- **Tests** — what must be verified, and how
- **Acceptance Criteria** — the observable conditions that mark the phase done

Only the current phase is filled in. Later phases are listed as placeholders
from the README roadmap and will be fleshed out in order, in discussion with
the project owner, once the prior phase is accepted.

---

## Phase 0 — Getting Started

### Goal

Stand up a working Python project skeleton and toolchain so that every later
phase starts from a known-good foundation: dependency management, package
layout, config/secrets handling, linting, type-checking, testing, and CI all
function end-to-end before any research logic is written.

### Architectural Decisions

- **Dependency & environment management: [uv](https://docs.astral.sh/uv/)**
  One tool handles the virtual environment, dependency resolution, and the
  lockfile (`uv.lock`), replacing the pip + venv + requirements.txt
  combination. Fast, single binary, minimal ceremony.

- **Python version: 3.12**
  Development is standardized on Python 3.12 using a `.python-version` file,
  while `pyproject.toml` declares `requires-python = ">=3.12,<3.13"`.
  CI also runs against Python 3.12 so local development and automated checks
  use the same interpreter version.

- **Package layout: `src/` layout + Hatchling**
  Application code lives at `src/hitl_research_agent/`, not at the repo root.
  This forces the package to be installed (via `uv`) rather than imported
  by accident from the working directory. Hatchling is used as the build
  backend for the installable `src/` package.

- **Configuration & secrets: `pydantic-settings` + `.env`**
  A single typed `Settings` object (subclassing `BaseSettings`) will be the
  one place that reads environment variables / `.env`. This provides typed,
  centralized configuration and fits the project's existing Pydantic-first
  design direction (structured research schemas in later phases). `.env` is
  git-ignored; `.env.example` documents expected variables without values.
  No real secret is required in Phase 0 because no LLM calls occur until
  Phase 2. `OPENAI_API_KEY` is therefore optional in the Phase 0 settings
  scaffold and becomes required only when a component actually needs OpenAI.

- **Linting / formatting / type-checking: Ruff + mypy**
  Ruff replaces flake8/isort/black (lint + format in one fast tool). mypy adds
  static type checking, which matters early because the project's core data
  model (Phase 1) will be Pydantic-heavy and benefits from catching schema
  mistakes at type-check time rather than at runtime.

- **Git hooks: pre-commit**
  Ruff and mypy run automatically on commit via `pre-commit`, so style/type
  issues are caught locally before they reach CI.

- **CI: GitHub Actions**
  A minimal workflow runs `ruff check`, `ruff format --check`, `mypy`, and
  `pytest` on every push/PR from Phase 0 onward, so the toolchain is enforced
  from the very first commit rather than retrofitted later.

- **Test framework: pytest**
  Standard choice for the ecosystem; works naturally with the `src/` layout.

- **Deferred dependencies: LangChain, DeepEval, OpenAI SDK**
  None of these are installed in Phase 0. There is no LLM or evaluation logic
  yet, so pulling them in now would add dependency weight with nothing to
  exercise it. They are introduced starting in Phase 2 (LangChain, OpenAI) and
  Phase 3 (DeepEval), when there is real behavior for them to support.

- **Phase 0 code scope: scaffolding + one smoke test**
  Phase 0 does not implement any research logic. It proves the full chain —
  `uv run pytest` executes, discovers the package, and passes — works before
  Phase 1 introduces real schemas.

### Technologies Introduced

| Tool | Purpose |
|---|---|
| `uv` | Virtual environment, dependency resolution, lockfile |
| `pydantic` / `pydantic-settings` | Data validation; typed settings from env/`.env` |
| `ruff` | Linting + formatting |
| `mypy` | Static type checking |
| `pre-commit` | Git hook runner for ruff + mypy |
| `pytest` | Test runner |
| GitHub Actions | CI |

### Implementation Tasks

1. Create `pyproject.toml`:
   - project metadata: `name = "hitl-research-agent"` (matches repo/README),
     importable module `hitl_research_agent`; `requires-python = ">=3.12,<3.13"`
   - `src/` layout build config using Hatchling as the build backend
     (`[build-system]` with `hatchling.build`)
   - dependency groups: runtime (`pydantic`, `pydantic-settings`) and dev
     (`pytest`, `ruff`, `mypy`, `pre-commit`)
   - `[tool.ruff]` and `[tool.mypy]` configuration
2. Create a `.python-version` file pinned to `3.12` so local interpreter
   selection matches `requires-python` in `pyproject.toml` and the CI version.
3. Run `uv sync` / `uv lock` to generate `uv.lock` and the local `.venv`.
4. Create package skeleton:
   - `src/hitl_research_agent/__init__.py`
   - `src/hitl_research_agent/config.py` — `Settings(BaseSettings)` class,
     with `OPENAI_API_KEY` as an optional field
5. Create `.env.example` documenting expected environment variables
   (starting with a placeholder for the future, optional `OPENAI_API_KEY`).
6. Confirm `.gitignore` covers `.venv/`, `.env`, `__pycache__/`, `.mypy_cache/`,
   `.ruff_cache/`, `.pytest_cache/` (extend existing `.gitignore` as needed).
7. Create `tests/` directory with smoke tests that:
   - import the package without error
   - construct `Settings` successfully with no `OPENAI_API_KEY` set
   - construct `Settings` with a test `OPENAI_API_KEY` and confirm it loads
8. Add `.pre-commit-config.yaml` wiring ruff (lint + format) and mypy as hooks;
   document `pre-commit install` in the README dev setup section.
9. Add `.github/workflows/ci.yml` running, on push and PR (pinned to
   Python 3.12): `uv sync`, `ruff check`, `ruff format --check`, `mypy src`,
   `pytest`.
10. Add a "Development Setup" section to `README.md` covering: installing
    `uv`, `uv sync`, `pre-commit install`, and how to run tests/lint locally.

### Tests

- Smoke test: package imports without error.
- Smoke test: `Settings` constructs successfully without `OPENAI_API_KEY`
  because no Phase 0 component requires it.
- Smoke test: `Settings` loads `OPENAI_API_KEY` correctly when a test value is
  supplied, proving `pydantic-settings` environment loading is wired up.

### Acceptance Criteria

- [x] `.python-version` and `pyproject.toml` agree on Python 3.12.
- [x] `uv sync` installs a working environment from a clean clone.
- [x] `uv run pytest` passes locally.
- [x] `uv run ruff check .` and `uv run ruff format --check .` pass.
- [x] `uv run mypy src` passes.
- [x] `pre-commit run --all-files` passes.
- [x] Pushing a commit/PR triggers GitHub Actions CI and it passes.
- [x] README documents how a new contributor sets up the dev environment.
- [x] No research/domain logic exists yet beyond the settings scaffold —
      Phase 0 stays scoped to toolchain and structure.

---

## Phase 1 — Research Data Model

### Goal

Define and validate the Pydantic schemas representing a single source's
structured research analysis — the shared vocabulary every later phase
(extraction, evaluation, review, synthesis, storage) builds on. Phase 1 is
schema definition and validation only: no LLM calls, no persistence, no I/O.

### Architectural Decisions

- **Composed sub-models, not one flat model**
  `SourceAnalysis` composes focused sub-models (`Provenance`, `Methodology`,
  `Claim`, `Evidence`, and the `InterpretedStatement` subclasses) rather than
  being one model with primitive-typed fields. This makes each piece
  independently testable and reusable — later phases (e.g. Phase 6
  cross-source synthesis) will want to compare `Claim`/`Evidence` instances
  across sources without depending on a single monolithic shape.

- **`statement_origin` discriminator applied to every interpretive field**
  The project's core principle — "model interpretation is kept separate from
  claims made directly by the source" — is enforced structurally, not just by
  convention. `research_problem`, `central_claims`, `assumptions`,
  `limitations`, `proposed_solutions`, and `open_questions` are all built on
  `InterpretedStatement`, which carries a `statement_origin: Literal
  ["author_stated", "model_inferred"]` field. `Methodology` carries the same
  field independently, since a source's methodology description is itself
  either reported by the source or reconstructed by the model.

- **Stable identifiers, generated now, random rather than content-addressed**
  `Provenance.source_id`, `Claim.id`, `Evidence.id`, and `SourceAnalysis.id`
  are all `UUID` fields with `Field(default_factory=uuid4)` — auto-generated,
  never caller-required. `source_id` is documented as reusable across
  re-analysis of the same source (distinguishing the source's identity from
  any one analysis of it), while `SourceAnalysis.id` and `analyzed_at` are
  fresh every time. IDs are random (UUID4), not content-addressed; a stable,
  content-based identity for recognizing "this is a revision of that claim"
  is deferred to Phase 4's revise/rerun design, not solved here.

- **Reusable `NonEmptyStr` type and `extra="forbid"` for strict validation**
  A shared `NonEmptyStr` (`Annotated[str, StringConstraints(strip_whitespace=
  True, min_length=1)]`) is applied to every required text field and to every
  optional text field whenever a value is provided, rejecting empty and
  whitespace-only input. A shared `ResearchBaseModel` base sets
  `model_config = ConfigDict(extra="forbid")` so every model rejects
  unrecognized fields. This matches the project's faithfulness/grounding
  principle: the schema itself refuses degenerate or malformed input rather
  than silently accepting it.

- **Two-axis evidence relationship: `evidence_form` and `relationship_to_claim`**
  `Evidence.evidence_form` (`"verbatim"` / `"paraphrased"`) captures how the
  evidence text was captured from the source. `Evidence.relationship_to_claim`
  (`"claim_grounding"` / `"direct_support"` / `"partial_support"` /
  `"contextual_support"`) captures how the evidence relates to its claim.
  `"claim_grounding"` is categorically distinct from the other three values —
  it means the source itself states or makes the claim (attribution) — and is
  not part of an ordered support-strength scale with them. Cross-field
  validators enforce the relationships between these fields and `Claim
  .statement_origin` (see Validation Rules below).

- **`Methodology` is structured but optional, with no closed type enum**
  `Methodology` has explicit fields (`summary`, `study_design`,
  `data_sources`, `sample_or_scope`, `analysis_methods`, `statement_origin`)
  rather than a single free-text blob, but `SourceAnalysis.methodology` is
  `Methodology | None`. Not every legitimate source (e.g. a news article or
  blog post) documents a methodology, and forcing a non-empty summary in
  those cases would mean inventing content that isn't there — a direct
  violation of the strict-validation principle above. No enum constrains
  `study_design`/`analysis_methods` in Phase 1; that's deferred until real
  extraction output shows what categories are worth closing.

- **`Provenance.source_type` covers ten categories**
  `"peer_reviewed_paper"`, `"preprint"`, `"government_report"`,
  `"government_policy"`, `"research_institute_report"`,
  `"technical_document"`, `"industry_report"`, `"news_article"`,
  `"blog_post"`, `"other"` — matching the project's planned source pool,
  including a distinct category for official policy/standards/guidance
  documents that aren't accurately classified as reports.

- **Timezone-aware timestamps via Pydantic's `AwareDatetime`**
  `Provenance.retrieved_at` (when the source was retrieved) and
  `SourceAnalysis.analyzed_at` (when this analysis result was created) are
  both `AwareDatetime`, rejecting naive datetimes. They are documented as
  recording distinct events — retrieval of the source vs. creation of a
  particular analysis of it — and both are application-supplied /
  application-generated, never model-produced.

- **Out of scope for Phase 1**
  No revision links, review status, evaluation results, or schema-version
  fields. These belong to later phases (Phase 4 human review, Phase 3
  evaluation) and are deliberately not guessed at here.

### Technologies

No new dependencies. Phase 1 uses only `pydantic`, already introduced in
Phase 0.

### Module Layout

```
src/hitl_research_agent/models/
  __init__.py       # re-exports the public models
  _base.py          # NonEmptyStr, ResearchBaseModel, STATEMENT_ORIGIN_DESCRIPTION
  provenance.py     # Provenance
  methodology.py    # Methodology
  interpreted.py    # InterpretedStatement + ResearchProblem/Assumption/
                     # Limitation/ProposedSolution/OpenQuestion
  claim.py          # Evidence, Claim
  analysis.py       # SourceAnalysis

tests/models/
  test_provenance.py
  test_methodology.py
  test_interpreted.py
  test_claim.py
  test_analysis.py
```

Import direction is a strict DAG: `_base` is a leaf; `provenance`,
`methodology`, and `interpreted` import only from `_base`; `claim` imports
`_base` and `interpreted`; `analysis` imports `_base`, `provenance`,
`methodology`, `interpreted`, and `claim`. `_base.py` is not re-exported from
`__init__.py` — its leading underscore marks it internal.

### Implementation Tasks

1. `models/_base.py` — `NonEmptyStr`, `ResearchBaseModel`,
   `STATEMENT_ORIGIN_DESCRIPTION`.
2. `models/provenance.py` — `Provenance`.
3. `models/methodology.py` — `Methodology`.
4. `models/interpreted.py` — `InterpretedStatement` and its five subclasses
   (`ResearchProblem`, `Assumption`, `Limitation`, `ProposedSolution`,
   `OpenQuestion`).
5. `models/claim.py` — `Evidence` and `Claim`, including their cross-field
   validators.
6. `models/analysis.py` — `SourceAnalysis`, composing the above.
7. `models/__init__.py` — re-export all public models.
8. `tests/models/` — one test file per model module (see Tests below).
9. Confirm `ruff check`, `ruff format --check`, `mypy src`, and `pytest` all
   pass against the new package.

### Validation Rules

- Every required text field, and every optional text field whenever a value
  is provided, uses `NonEmptyStr`: surrounding whitespace is stripped, and
  empty or whitespace-only values are rejected.
- Every model rejects unrecognized fields (`extra="forbid"`, inherited via
  `ResearchBaseModel`).
- List fields with defaults use `Field(default_factory=list)`; no field uses
  a bare mutable literal default.
- `SourceAnalysis.central_claims` and `Claim.evidence` are required fields
  (no default) with `min_length=1` — at least one item each.
- `Provenance.retrieved_at` and `SourceAnalysis.analyzed_at` are
  `AwareDatetime` — timezone-naive values are rejected.
- Cross-field validation on `Evidence`: `relationship_to_claim ==
  "claim_grounding"` is only valid when `evidence_form == "verbatim"`.
- Cross-field validation on `Claim`: an `author_stated` claim must include at
  least one `Evidence` item whose `relationship_to_claim` is
  `"claim_grounding"`; a `model_inferred` claim must not contain any
  `"claim_grounding"` evidence.
- Field documentation for `statement_origin`, `evidence_form`, and
  `relationship_to_claim` is encoded via `Field(description=...)` so it
  appears in Pydantic's generated JSON Schema, not as standalone string
  literals.

### Tests

**`tests/models/test_provenance.py`**
- `source_id` defaults to a unique UUID per instance.
- `source_id` can be explicitly reused across separately constructed
  `Provenance` instances (modeling re-analysis of the same source).
- New `source_type` values (`research_institute_report`,
  `technical_document`, `government_policy`) are accepted.
- `doi` and `publisher` are optional, and reject whitespace-only values when
  provided.
- `retrieved_at` rejects a timezone-naive datetime.
- `retrieved_at` is timezone-aware on a valid value (`utcoffset() is not
  None`).
- `source_authors` list defaults are independent across instances.

**`tests/models/test_methodology.py`**
- Empty/whitespace-only `summary` is rejected.
- Invalid `statement_origin` values are rejected.
- `data_sources`/`analysis_methods` list defaults are independent across
  instances.
- A fully populated `Methodology` constructs successfully.

**`tests/models/test_interpreted.py`**
- Parametrized across `ResearchProblem`, `Assumption`, `Limitation`,
  `ProposedSolution`, `OpenQuestion`:
  - empty/whitespace-only `text` is rejected;
  - an invalid `statement_origin` value is rejected;
  - valid construction succeeds.

**`tests/models/test_claim.py`**
- Whitespace-only `Evidence.text` is rejected; valid text is stripped.
- An unrecognized field on `Evidence` is rejected.
- `Claim.evidence=[]` raises a `ValidationError`.
- An `author_stated` claim without `claim_grounding` evidence is rejected.
- A `model_inferred` claim containing `claim_grounding` evidence is rejected.
- `Evidence` marked `claim_grounding` with `evidence_form="paraphrased"` is
  rejected.
- An `author_stated` claim with valid `claim_grounding` evidence constructs
  successfully.

**`tests/models/test_analysis.py`**
- `SourceAnalysis.methodology` is `None` when not provided.
- `SourceAnalysis.central_claims=[]` raises a `ValidationError`.
- `analyzed_at` defaults to a timezone-aware value (`utcoffset() is not
  None`).
- `analyzed_at` rejects a timezone-naive datetime.
- Separately constructed `SourceAnalysis` objects receive different
  automatically generated `id` values.
- A complete `SourceAnalysis` (with `ResearchProblem`) round-trips through
  `model_dump_json` / `model_validate_json` without data loss, preserving
  subclass identity.

### Acceptance Criteria

- [x] All models (`Provenance`, `Methodology`, `InterpretedStatement` and its
      five subclasses, `Evidence`, `Claim`, `SourceAnalysis`) are importable
      from `hitl_research_agent.models`.
- [x] `SourceAnalysis` composes `Provenance`, an optional `Methodology`, a
      `ResearchProblem`, one or more `Claim`s (each with ≥1 `Evidence`), and
      the four interpretive-statement lists.
- [x] Every interpretive field carries `statement_origin`; `Methodology`
      carries it independently.
- [x] All models reject unrecognized fields.
- [x] Required and provided-optional text fields reject empty/whitespace-only
      values and store the stripped value.
- [x] List fields use independent per-instance defaults — no shared mutable
      defaults.
- [x] `central_claims` and `Claim.evidence` each require at least one item.
- [x] `retrieved_at` and `analyzed_at` both reject timezone-naive datetimes
      and are documented as distinct events.
- [x] `Evidence.relationship_to_claim == "claim_grounding"` is only valid
      when `evidence_form == "verbatim"`.
- [x] An `author_stated` `Claim` requires ≥1 `claim_grounding` evidence item;
      a `model_inferred` `Claim` must not contain any.
- [x] `source_id` is documented as stable/reusable across re-analysis;
      `SourceAnalysis.id` and `analyzed_at` are fresh per analysis result and
      unique across instances.
- [x] `source_type` includes all ten finalized categories.
- [x] A complete `SourceAnalysis` round-trips through JSON without data loss,
      preserving subclass identity.
- [x] Full check suite passes: `pytest`, `ruff check`, `ruff format --check`,
      `mypy src`.
- [x] No extraction, evaluation, or storage logic exists yet — Phase 1 stays
      scoped to schema definition and validation.
- [x] No revision-link, review-status, evaluation-result, or schema-version
      fields exist yet.

## Phase 2 — Single-Source Analysis

### Goal

Use an LLM to convert one manually supplied source into a validated
`SourceAnalysis`, without receiving the human's research question and without
a `project_tag`. Manually supplied sources remain an implementation-stage
bridge until Phase 5 adds real discovery and ingestion. Phase 2 includes
argument reconstruction, evidence and citation extraction, assumptions,
limitations, and provisional assessments of whether the paper's reasons
support its conclusions, returned as JSON — presenting that analysis to a
reader is not part of Phase 2. Phase 3 evaluates the quality of our
analysis; Phase 4 implements the accept/reject/revise workflow. Those
automated evaluation and review workflows, research-store persistence,
source discovery, cross-source synthesis, RAG, and orchestration remain
later work. Saving development outputs and manually reviewing them are part
of Phase 2 validation, not the later research-store workflow.

### Architectural Decisions

- **Input: `SourceDocument`**
  `SourceDocument` holds `text` and a `Provenance`. It deliberately does not
  define or claim anything about the normalization process Phase 5 will
  eventually perform — it only states Phase 2's own input contract, which
  Phase 5 can satisfy however it ends up working.

- **Field ownership stays split between the model and the application**
  The model generates research content only: `research_problem`,
  `central_claims` (with their evidence), `methodology`, `assumptions`,
  `limitations`, `proposed_solutions`, and `open_questions`. The application
  supplies everything else: all of `Provenance`, `SourceAnalysis.id`,
  `SourceAnalysis.analyzed_at`, and every `Claim.id`/`Evidence.id`. The
  finalized Phase 1 models are not refactored to fit the LLM output format.

- **Three new extraction schemas, not a parallel model hierarchy**
  `Evidence` and `Claim` each carry one application-owned `id: UUID` field
  that has no legitimate value for the model to produce — that is the *only*
  reason either needs a twin. `ExtractedEvidence` and `ExtractedClaim`
  reproduce their fields minus `id`; `ExtractedAnalysis` is the container
  extraction schema, differing from `SourceAnalysis` only in using
  `list[ExtractedClaim]` and omitting `id`/`provenance`/`analyzed_at`. Every
  other Phase 1 content model — `Methodology` and the five
  `InterpretedStatement` subclasses (`ResearchProblem`, `Assumption`,
  `Limitation`, `ProposedSolution`, `OpenQuestion`) — is reused unchanged:
  none of them carry an application-owned field, and their optional
  (`X | None = None`) and defaulted (`Field(default_factory=list)`) fields
  both convert cleanly to OpenAI's strict-schema pattern (every property
  required; optionality expressed as nullability, not omission). `Provenance`
  is not part of the extraction schema at all — it is pure input.
  `ExtractedEvidence`/`ExtractedClaim` carry no cross-field validators of
  their own; Pydantic's `model_validator`s cannot be expressed in JSON Schema
  regardless of which model carries them, so validation happens once, in one
  place, when real `Claim`/`Evidence`/`SourceAnalysis` objects are assembled
  from the extracted data after the model call returns.

- **Return type: `AnalysisResult`**
  `analyze_source()` returns `AnalysisResult` — the completed `SourceAnalysis`
  plus `model`, `input_tokens`, `output_tokens`, and `attempt_count` — rather
  than a bare `SourceAnalysis`, so call-level facts have somewhere to live
  without adding schema-version or call-provenance fields to Phase 1. Token
  totals are summed across both calls whenever the one correction attempt
  fires. No further metadata is added without explaining why it's needed
  first.

- **Model and call configuration**
  Default model `gpt-6-astra` at `low` reasoning effort (both configurable
  via `Settings`), the OpenAI Responses API selected explicitly
  (`use_responses_api=True`) rather than relied on implicitly, and native
  structured output via `with_structured_output(ExtractedAnalysis,
  method="json_schema", strict=True, include_raw=True)`. `temperature`,
  `top_p`, and `top_logprobs` are omitted entirely rather than defaulted,
  since they are documented as incompatible with reasoning enabled — not
  merely unnecessary. `include_raw=True` is required, not optional: it is
  how token usage and refusal/incomplete status are recovered regardless of
  whether the model's output parses or validates successfully.

  This default was chosen after running the same paper, prompt, and schema
  through `gpt-6-sol` at `medium` and `high` reasoning and `gpt-6-astra` at
  `low` and `medium`, all without a correction attempt or failure. Astra at
  medium produced useful analysis too, but Astra at low expressed its
  `support_assessment` reasoning in language the project owner found easier
  to understand and act on. Since this is a human-in-the-loop tool, that
  usability difference — not measured accuracy, which none of these runs
  established — decided the default. The model and reasoning effort remain
  fully configurable via `Settings`; no automatic model routing is planned
  for Phase 2.

- **Source-size limit: 200,000 characters, checked before any model call**
  `SourceDocument.text` longer than 200,000 characters is rejected
  immediately with a clear error — no truncation, no chunking. The limit is
  sized to comfortably cover a single long-form report, which is what the
  MVP source types (papers, government/industry reports, articles) are
  expected to look like, not to sit just under any pricing or context-window
  boundary. It remains an unvalidated placeholder. The supplied paper is well below
  the limit; its successful runs do not validate the limit for large or
  representative MVP sources.
  A plain character count is used rather than an exact token count; adding a
  tokenizer dependency for more precision is deferred until real sources show
  the character estimate is actually too loose.

- **Deterministic verbatim-grounding check**
  Any `Evidence`/`ExtractedEvidence` with `evidence_form="verbatim"` must
  literally appear in the source text (case/whitespace-normalized substring
  match). This is a mechanical check, not a faithfulness *evaluation* — it
  belongs to producing a valid analysis, not to the broader evaluation work
  planned for Phase 3. `Evidence.locator` remains free-text, since manually
  supplied plain-text sources have no reliable pagination to point to more
  precisely.

- **Failure handling distinguishes four outcomes, not two**
  *Invalid analysis* — parses, but fails the verbatim-grounding check or
  Phase 1's own cross-field validation when real `Claim`/`Evidence`/
  `SourceAnalysis` objects are assembled — is the only outcome eligible for
  the one correction attempt: the specific failure is fed back to the model
  once, and if it still fails, `SourceAnalysisValidationError` is raised with
  both attempts' usage accumulated. *Refusal* (the response's `refusal`
  field is set) and *incomplete output* (`status="incomplete"`, e.g. the
  reasoning-plus-output budget was exhausted) each raise their own error
  immediately without consuming the correction attempt — neither leaves
  anything a retry could meaningfully correct. *Technical failure* (network
  error, timeout, rate limit, server error) never returns a response at all,
  so it carries no usage to record; it is handled by the API client's own
  transport-level retry, a separate and independently bounded budget from
  the one semantic correction attempt, and never produces an `AnalysisResult`.
  `AnalysisResult.input_tokens`/`output_tokens` are the exact sum of
  `usage_metadata` from every call that returned a response and was
  evaluated (never a fabricated value standing in for an unknown one), and
  `attempt_count` counts only those calls — both fields describe exactly
  what was observed, not a guarantee of what OpenAI billed if a response
  was generated but never received.

- **Output: JSON only**
  `analyze_source()` returns `AnalysisResult`; nothing renders it. A Markdown
  renderer (`extraction/report.py`) was built, used to review several
  development runs, and removed after the project owner rejected its
  quote-hiding behavior and asked that analytical quality be addressed before
  any presentation layer. No renderer replaces it; a presentation can be
  designed later if one is needed. Every saved `AnalysisResult` JSON from
  development runs is preserved for direct comparison.

- **Dependencies: `langchain-core` and `langchain-openai` only**
  Not the full `langchain` meta-package — Phase 2 needs `ChatOpenAI` and
  structured-output binding, nothing from chains/agents/retrievers. No direct
  tokenizer dependency or tokenizer-based size guard is added. `tiktoken`
  is present transitively in the lockfile; the guard uses character count.

- **Citations: a `Citation` model attached to `Evidence`**
  `Evidence.citations: list[Citation]` records what the source itself cites
  in connection with that evidence (`citation_text`, and `reference_entry`
  only when a matching entry exists in the source's own reference list —
  never invented). `Citation` carries no application-owned field, so the
  extraction-time `ExtractedEvidence` reuses it directly rather than needing
  a twin. This is a deliberate extension of a finalized Phase 1 file
  (`models/claim.py`), made because citation tracking is genuine research
  content Phase 1 was missing, not a Phase 2 convenience. A citation only
  means the source cites that work — Phase 2 performs no retrieval or
  verification of it.

- **`Claim.support_assessment`: a provisional, model-authored judgment of
  argument sufficiency**
  For a claim important to the argument, whose own wording makes a strong or
  consequential commitment (necessity, causal, generalizing, predictive, or
  prescriptive language), the model may add `support_assessment`: a
  passage-referenced judgment of whether the reasons offered across
  the source actually meet that claim's stated strength and scope. Most
  claims will not have one — selection is by importance and by what the
  claim's wording commits to, not by matching a keyword. The assessment must
  do real work, not return a bare label: state what the claim commits to,
  cite the specific supporting passages and locations, distinguish an
  announced aim from a developed argument, name any bridging assumption it
  identifies (added to `assumptions` as `model_inferred`, connected
  explicitly to the claim that needs it), and say plainly when the material
  is insufficient to decide rather than forcing a verdict. It must recognize
  well-supported claims as readily as gaps — the goal is calibrated
  judgment, not routine criticism. This is always the model's own analysis,
  never something the source states, and never a claim that a cited work has
  been verified; it is not mechanically checked the way grounding and
  citations are, so its presence in a result is not evidence of its quality.
  **`support_assessment: null` means the claim was not assessed — nothing
  more.** It is never a judgment that the claim is well-supported and never
  a claim that no issue exists; the schema, the prompt, and this document
  all define it the same way, so its absence on most claims is not
  interpretable as a clean bill of health for them.
  A second content extension of the Phase 1 models, for the same reason as
  citations: this is genuine analytical content the project's stated purpose
  (helping a human read critically) requires, not a Phase 2-only workaround.
  Passing the offline plumbing tests here is not evidence that a live model
  produces good assessments — that is unevaluated, and is Phase 3's job, not
  a Phase 2 acceptance requirement.

### Technologies Introduced

| Tool | Purpose |
|---|---|
| `langchain-core` | `Runnable`/chat-model abstractions the pipeline is written against |
| `langchain-openai` | `ChatOpenAI`, Responses API selection, native structured output |

### Module Layout

```
src/hitl_research_agent/extraction/
  __init__.py     # re-exports analyze_source, schemas, errors
  schemas.py       # SourceDocument, ExtractedEvidence, ExtractedClaim, ExtractedAnalysis
  prompts.py        # system prompt + human-message construction
  grounding.py        # evidence, citation-marker, and reference-entry checks
  pipeline.py           # analyze_source(): size guard, model call, retry, assembly
  errors.py              # SourceAnalysisError hierarchy

tests/extraction/
  test_schemas.py
  test_grounding.py
  test_pipeline.py
  test_prompts.py
```

`extraction` is named to avoid colliding with the existing
`models/analysis.py` module. It depends on `models` (reusing `Provenance`,
`Methodology`, the `InterpretedStatement` subclasses, `Claim`, `Evidence`,
`SourceAnalysis`) and on `config.Settings`; nothing in `models/` depends on
`extraction`.

### Implementation Tasks

1. `extraction/schemas.py` — `SourceDocument`, `ExtractedEvidence`,
   `ExtractedClaim`, `ExtractedAnalysis`.
2. `extraction/errors.py` — `SourceAnalysisError` base, plus
   `SourceAnalysisValidationError`, `SourceAnalysisRefusedError`,
   `SourceAnalysisIncompleteError`, `SourceAnalysisExtractionError`.
3. `extraction/grounding.py` — normalized substring checks for verbatim
   evidence, citation markers, and supplied reference entries.
4. `extraction/prompts.py` — the system prompt (question-independent
   reconstruction; `statement_origin`/`evidence_form`/`relationship_to_claim`
   semantics; citation capture; the `support_assessment` reading method) and
   a human-message builder (source text plus `source_title`/`source_type`
   framing from `Provenance`).
5. `extraction/pipeline.py` — `analyze_source(source: SourceDocument, *,
   model: Runnable | None = None) -> AnalysisResult`: enforces the
   200,000-character limit before any model call; constructs a default
   `ChatOpenAI` from `Settings` when `model` is not supplied; invokes with
   `include_raw=True`; classifies the outcome (invalid analysis / refusal /
   incomplete / technical failure); performs the one correction attempt for
   invalid analysis; assembles real `Claim`/`Evidence`/`SourceAnalysis`
   objects from the extracted data so Phase 1 validation runs; accumulates
   token usage into `AnalysisResult`.
6. Extend `config.Settings` with `openai_model: str = "gpt-6-astra"`,
   `openai_reasoning_effort: str = "low"`, and
   `max_source_characters: int = 200_000`, all overridable via environment.
7. `extraction/__init__.py` — re-export the analysis entry point, schemas,
   and error types.
8. `tests/extraction/` — one test file per concern (see Tests below), all
   exercised through an injected fake model.
9. Add `langchain-core` and `langchain-openai` to `pyproject.toml`.
10. Confirm `ruff check`, `ruff format --check`, `mypy src`, and `pytest` all
    pass against the new package.

### Validation and Failure-Handling Rules

- `SourceDocument.text` longer than `Settings.max_source_characters` raises
  before any model call; Phase 2 never truncates or chunks a source.
- The model call uses `method="json_schema"`, `strict=True`, and
  `include_raw=True`; `temperature`, `top_p`, and `top_logprobs` are never
  passed alongside `reasoning_effort`.
- Every `verbatim` evidence item is checked against the source text
  (case/whitespace-normalized substring match); a failed match is invalid
  analysis, not a separate failure category.
- Citation markers and nonempty reference entries must occur somewhere in
  the source after normalization. Failed matches enter the same one-correction
  path as failed quotations. These checks establish textual occurrence, not
  correct citation-to-claim attribution, argumentative support, or the truth
  of a cited work. Assessment prose and its passage references are not
  mechanically validated by these checks.
- Real `Claim`/`Evidence`/`SourceAnalysis` objects are constructed from the
  extracted data after every successful model call, so Phase 1's existing
  cross-field validators (`claim_grounding` ⇄ `verbatim`, `author_stated` ⇄
  grounding evidence, non-empty required lists) run unchanged; a
  `ValidationError` here is also invalid analysis.
- Invalid analysis gets exactly one correction attempt, with the specific
  validation or grounding failure fed back to the model. Refusal, incomplete
  output, and technical failure are each terminal on the first occurrence —
  none of them consume or extend the one correction attempt.
- Technical (transport-level) retries belong to the API client, are bounded
  independently of the one correction attempt, and never appear in
  `AnalysisResult` — a technical failure raises before any result is built.
- `AnalysisResult.input_tokens`/`output_tokens` sum `usage_metadata` from
  exactly the calls counted in `attempt_count`; no other value is added or
  assumed.

### Tests

**`tests/extraction/test_schemas.py`**
- `SourceDocument` rejects empty/whitespace-only `text`.
- `ExtractedEvidence`/`ExtractedClaim`/`ExtractedAnalysis` construct
  successfully from valid data and carry no `id` field.

**`tests/extraction/test_grounding.py`**
- Verbatim evidence text present in the source (after normalization) passes.
- Verbatim evidence text absent from the source fails.
- Paraphrased evidence is not checked against the source text.
- Matching is case- and whitespace-insensitive.
- Citation markers and provided reference entries must occur in the source;
  a marker may occur outside the attached evidence text.

**`tests/extraction/test_pipeline.py`**
- `Claim.support_assessment` and any assumption it names survive assembly
  into the final `SourceAnalysis` unchanged, and default to unset/empty when
  not provided. Plumbing only — proves the data flows through, says nothing
  about whether a live model can produce a sound assessment.
- Source text over `max_source_characters` raises before the injected model
  is ever invoked.
- A fake model returning valid extracted content on the first call produces
  an `AnalysisResult` with `attempt_count == 1` and correctly summed usage.
- A fake model returning invalid analysis (grounding or Phase 1 validation
  failure) on the first call and valid content on the second produces
  `attempt_count == 2` with usage summed across both calls.
- A fake model returning invalid analysis on both calls raises
  `SourceAnalysisValidationError` after exactly one retry — never more.
- A fake model returning a refusal raises `SourceAnalysisRefusedError`
  immediately, with no correction attempt.
- A fake model returning `status="incomplete"` raises
  `SourceAnalysisIncompleteError` immediately, with no correction attempt.
- A fake model raising a transport-level exception raises
  `SourceAnalysisExtractionError`, and no `AnalysisResult` is produced.
- `Settings.openai_model`, `openai_reasoning_effort`, and
  `max_source_characters` default to `"gpt-6-astra"`, `"low"`, and `200_000`
  respectively, and are overridable.

**Prompt tests**
- `test_prompts.py` checks the presence of extraction and assessment
  instructions; these tests do not measure live reasoning quality.
- Strict-schema and offline model-construction tests exercise compatibility
  without contacting the API. Model tests cover citations and assessments.

### Verification Status

Nine live calls exist on the Masri–Snoswell paper: development iterations
v1–v4 (predating `support_assessment`; v4 adds citation capture and is the
only one of the nine that used the one correction attempt), and four
model/reasoning comparison runs — `gpt-6-sol` at `medium` and `high`,
`gpt-6-astra` at `low` and `medium` — each including `support_assessment`
and each succeeding without a correction attempt. All nine established that
the pipeline runs end to end on this source; none produced a refusal or an
incomplete-output response, so that handling remains unverified against a
real captured response, and the 200,000-character cap remains an unvalidated
placeholder — this source used about 14% of it.

Whether `support_assessment` produces good analytical judgment — recognizing
a well-supported conclusion as readily as a real gap, on sources this project
hasn't seen — has not been rigorously evaluated. That evaluation was never
agreed as a Phase 2 requirement and is not treated as one here; it belongs
with Phase 3's evaluation work.

### Known Limitations and Later Evaluation Targets

Documented gaps to evaluate later, not omissions to fix inside Phase 2:

- **Analytical quality is not established.** Whether `support_assessment`
  reliably distinguishes well-supported claims from genuine gaps is
  unevaluated on any source. This is Phase 3's work, not an unmet Phase 2
  requirement.
- **Assessment selection is not shown to be consistent.** How many claims
  received a `support_assessment`, and which ones, varied across the six
  live runs that include this field, without a controlled comparison of why;
  nothing confirms this converges on the same claims for the same source
  across models, reasoning levels, or repeated runs.
- **Claim granularity varies substantially by model and reasoning effort** on
  the identical source and prompt — recorded runs produced between 18 and 30
  central claims. Whether that reflects genuine differences in what each
  configuration finds worth extracting, or unprincipled variation, is
  unresolved.
- **Only one source has been analyzed.** Every finding above comes from one
  ~28,000-character philosophy/AI-ethics preprint. Behavior on harder,
  longer, more technical, or differently structured papers is untested.
- **A future presentation must distinguish paraphrased evidence from direct
  quotations clearly.** `Evidence.evidence_form` already records this, but
  nothing renders it now that the report renderer has been removed. This is
  a requirement for whenever a presentation layer is designed, not a reason
  to build one now.

These belong to Phase 3's evaluation work and to a future presentation
design, not to additional Phase 2 features.

### Acceptance Criteria

- [x] `analyze_source(source: SourceDocument, ...) -> AnalysisResult` is
      implemented and importable from `hitl_research_agent.extraction`.
- [x] The application — never the model — supplies `Provenance`, every `id`
      field, and `SourceAnalysis.analyzed_at`/`id`.
- [x] Three extraction-only content schemas exist (`ExtractedEvidence`,
      `ExtractedClaim`, `ExtractedAnalysis`). `Citation` is a shared content
      model reused directly, not a fourth extraction-only schema.
      `SourceDocument` and `AnalysisResult` are input/output wrappers.
      Every other Phase 1 content model is reused
      unchanged. `Claim`/`Evidence` (Phase 1) have since been deliberately
      extended twice — `Evidence.citations` and `Claim.support_assessment` —
      each because it is genuine research content the schema was missing,
      documented as its own decision above rather than left unstated.
- [x] `SourceDocument.text` over `max_source_characters` (200,000 by default)
      raises before any model call; no truncation or chunking exists
      anywhere in Phase 2.
- [x] The extraction call is configured for the Responses API, `gpt-6-astra`
      (default, configurable), `low` reasoning (default, configurable),
      native structured output (`method="json_schema"`, `strict=True`), and
      omits `temperature`/`top_p`/`top_logprobs`. Verified by constructing
      the real `ChatOpenAI` + `with_structured_output` pipeline offline and
      inspecting the strict schema it generates (see Tests). Recorded live
      runs on the supplied paper exercised successful output, including a
      correction attempt in the v4 citations run; the four model/reasoning
      comparison runs (`gpt-6-sol` at `medium` and `high`, `gpt-6-astra` at
      `low` and `medium`) each succeeded without one. The default was chosen
      from that comparison for the usability of Astra-low's assessment
      language, not from a quality comparison. Live refusal/incomplete
      handling remains unverified.
- [x] Every `verbatim` evidence item is checked against the source text; a
      failed match is treated as invalid analysis.
- [x] Invalid analysis receives exactly one correction attempt with the
      specific failure fed back to the model; refusal, incomplete output,
      and technical failure each raise their own distinct exception without
      consuming that attempt.
- [x] Technical retries are handled separately from the one correction
      attempt and never contribute a fabricated token count.
- [x] `AnalysisResult` reports `model`, `input_tokens`, `output_tokens`, and
      `attempt_count` accurately, summed only across calls that returned a
      response.
- [x] All tests run against an injected fake model — no real network or API
      calls occur in the default test suite.
- [x] Full check suite passes: `pytest`, `ruff check`, `ruff format --check`,
      `mypy src`.
- [x] No automated analysis-quality evaluation, accept/reject review
      workflow, research-store persistence, source discovery, cross-source
      synthesis, chunking, or orchestration is implemented in Phase 2.
      Single-source analytical assessments are in scope; presenting them to
      a reader is not — Phase 2 returns JSON only.
- [x] `Claim.support_assessment` and any assumption it names survive
      extraction, assembly, and the saved analysis unchanged. The prompt
      instructs selection by importance and wording, not keyword matching.
      Data flow is verified offline; selection quality is not established
      by fixture tests. Whether the assessments themselves are analytically
      sound is unevaluated (see Known Limitations) — that evaluation is
      Phase 3's work, not a Phase 2 acceptance requirement.

### Phase 2 Status: Complete, With Documented Limitations

Phase 2 is complete: `analyze_source()` runs end to end against a real
source with the current default (`gpt-6-astra`, `low` reasoning), producing
a validated `SourceAnalysis` with claims, evidence, citations, and
provisional support assessments, entirely as JSON. All acceptance criteria
above are met. The items under Known Limitations and Later Evaluation
Targets are real, data-grounded observations from the recorded runs, carried
forward as Phase 3 evaluation work — they are not unmet Phase 2 requirements.
Phase 3 — Evaluation is next.

## Phase 3 — Evaluation

*To be planned.*

## Phase 4 — Human Review

*To be planned.*

## Phase 5 — Source Discovery and Ingestion

*To be planned.*

## Phase 6 — Cross-Source Synthesis

*To be planned.*

## Phase 7 — Research Knowledge Base and RAG

*To be planned.*

## Phase 8 — Retrieval Evaluation

*To be planned.*

## Phase 9 — LangGraph Orchestration

*To be planned.*
