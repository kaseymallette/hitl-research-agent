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

- [ ] `.python-version` and `pyproject.toml` agree on Python 3.12.
- [ ] `uv sync` installs a working environment from a clean clone.
- [ ] `uv run pytest` passes locally.
- [ ] `uv run ruff check .` and `uv run ruff format --check .` pass.
- [ ] `uv run mypy src` passes.
- [ ] `pre-commit run --all-files` passes.
- [ ] Pushing a commit/PR triggers GitHub Actions CI and it passes.
- [ ] README documents how a new contributor sets up the dev environment.
- [ ] No research/domain logic exists yet beyond the settings scaffold —
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
  independently testable and reusable — later phases (e.g. Phase 5
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

- [ ] All models (`Provenance`, `Methodology`, `InterpretedStatement` and its
      five subclasses, `Evidence`, `Claim`, `SourceAnalysis`) are importable
      from `hitl_research_agent.models`.
- [ ] `SourceAnalysis` composes `Provenance`, an optional `Methodology`, a
      `ResearchProblem`, one or more `Claim`s (each with ≥1 `Evidence`), and
      the four interpretive-statement lists.
- [ ] Every interpretive field carries `statement_origin`; `Methodology`
      carries it independently.
- [ ] All models reject unrecognized fields.
- [ ] Required and provided-optional text fields reject empty/whitespace-only
      values and store the stripped value.
- [ ] List fields use independent per-instance defaults — no shared mutable
      defaults.
- [ ] `central_claims` and `Claim.evidence` each require at least one item.
- [ ] `retrieved_at` and `analyzed_at` both reject timezone-naive datetimes
      and are documented as distinct events.
- [ ] `Evidence.relationship_to_claim == "claim_grounding"` is only valid
      when `evidence_form == "verbatim"`.
- [ ] An `author_stated` `Claim` requires ≥1 `claim_grounding` evidence item;
      a `model_inferred` `Claim` must not contain any.
- [ ] `source_id` is documented as stable/reusable across re-analysis;
      `SourceAnalysis.id` and `analyzed_at` are fresh per analysis result and
      unique across instances.
- [ ] `source_type` includes all ten finalized categories.
- [ ] A complete `SourceAnalysis` round-trips through JSON without data loss,
      preserving subclass identity.
- [ ] Full check suite passes: `pytest`, `ruff check`, `ruff format --check`,
      `mypy src`.
- [ ] No extraction, evaluation, or storage logic exists yet — Phase 1 stays
      scoped to schema definition and validation.
- [ ] No revision-link, review-status, evaluation-result, or schema-version
      fields exist yet.

## Phase 2 — Single-Source Analysis

*To be planned.*

## Phase 3 — Evaluation

*To be planned.*

## Phase 4 — Human Review

*To be planned.*

## Phase 5 — Cross-Source Synthesis

*To be planned.*

## Phase 6 — Research Knowledge Base and RAG

*To be planned.*

## Phase 7 — Retrieval Evaluation

*To be planned.*

## Phase 8 — LangGraph Orchestration

*To be planned.*
