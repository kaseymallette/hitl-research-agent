# ADR-0001 — The package lives under `src/`, so tests exercise the installed build

- **Status:** Accepted
- **Date:** 2026-08-26
- **Landed in:** `535cae7`

## Context

The project starts as a Python package with a test suite that will grow
alongside it. Python's default import behaviour puts the working directory on
`sys.path`, so a flat layout lets tests import the package straight from the
repository whether or not it is installed, and whether or not the packaging
configuration would actually ship it. A module left out of the wheel, or a
data file the build does not include, passes every test and fails on first
install.

## Decision

The package lives at `src/hitl_research_agent/`. The directory name is the
import name, and the only way to import it is through the editable install
(`uv sync`), because `src/` is not itself importable. `pyproject.toml` ships
exactly that directory
(`[tool.hatch.build.targets.wheel] packages = ["src/hitl_research_agent"]`),
and mypy is pointed at the package name with `mypy_path = "src"` rather than
at a path.

## Alternatives considered

- **Flat layout** — package directory at the repository root. Simpler, one
  less level of nesting, and no install step needed before running tests. It
  loses the property the layout is for: tests would stop telling us whether
  the installed build is complete.
- **Flat layout plus a packaging smoke test** — build the wheel in CI and
  import from it. This recovers the guarantee but as an extra check that can
  be skipped or go stale, rather than as the default path every test already
  takes.

## Consequences

Every test import goes through the installed package, so the test suite is
also a check that the build is complete.

The cost is that anything outside the package is not importable either, and
`scripts/` is outside it on purpose — it is not shipped. The preparation tests
therefore cannot `import prepare_sources`; `tests/preparation/conftest.py`
loads the script by file path instead. That indirection exists because of this
decision.

`mypy src` likewise covers only the package. `scripts/prepare_sources.py` is
793 lines and is not type-checked; it is exercised by its 27 tests instead.
That is a real gap, accepted knowingly rather than overlooked.

## Notes

Back-filled 2026-10-17. Current state of the layout is in
[REPOSITORY.md](../REPOSITORY.md); the configuration is in `pyproject.toml`.
