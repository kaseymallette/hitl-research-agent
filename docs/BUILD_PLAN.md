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

*To be planned.*

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
