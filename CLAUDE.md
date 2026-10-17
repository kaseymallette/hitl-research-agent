# Claude Code Instructions

## Engineering baseline

Follow @docs/ENGINEERING_DIRECTIVES.md when implementing, refactoring, or reviewing code. Apply only directives relevant to the change. Do not add patterns, comments, tests, or documentation merely to demonstrate compliance.

## Working in this repository

- Inspect the relevant implementation, callers, tests, and contracts before proposing changes. Preserve established behavior unless the task explicitly changes it.
- Prefer the smallest coherent change that solves the stated problem. Reuse existing structures and conventions; avoid speculative generalization and opportunistic rewrites.
- For consequential design choices, briefly explain the proposed approach and material tradeoffs before implementation. Raise ambiguities that would change correctness or architecture rather than inventing requirements.
- Treat internal invariants as contracts. Validate untrusted inputs at boundaries and keep error handling proportional to actual failure modes.
- Add or update focused tests for behavior that changes, including relevant boundary and failure cases. Run the appropriate checks and report what passed, failed, or could not be run. Never imply tests were run when they were not.
- In the final summary, state what changed, why, and any unresolved risks. Keep reasoning concise; do not produce a directive-by-directive compliance report.

## Change boundaries

Do not alter public interfaces, persistent data formats, external API behavior, or major architectural boundaries as incidental cleanup. Flag those changes explicitly and explain their impact before proceeding.

Project-specific commands, constraints, and architectural decisions belong in their existing repository documentation, not in this shared baseline. The section below points to where they live.

## This project

Checks: `uv run pytest` · `uv run ruff check . && uv run ruff format --check .` · `uv run mypy src`

Architectural decisions are recorded in [docs/adr/](docs/adr/) and are binding. Read the relevant ones before changing the analysis path, the output schema, or input handling. [docs/REPOSITORY.md](docs/REPOSITORY.md) says why each file exists; [docs/BUILD_PLAN.md](docs/BUILD_PLAN.md) has the phases.

**The one hard prohibition** ([ADR-0005](docs/adr/0005-no-hard-quality-gates.md)): only a technical failure may stop a run. A thin analysis, a claim with no evidence item, a `verbatim` quotation that does not match the source text — these are reported to the researcher, never withheld. Do not add validation that blocks a result on analysis quality, however reasonable it looks. Directive 10 above treats invalid external data as a thing to handle explicitly; model output that is poor is not invalid data, and this is the boundary where that distinction matters.
