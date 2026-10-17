# ADR-0007 — One `AnalysisError` carrying a `kind`, not an exception hierarchy

- **Status:** Accepted
- **Date:** 2026-10-15
- **Landed in:** `39a64df`

## Context

v1 had six exception classes for analysis failures, in a 94-line `errors.py`.
The hierarchy was built on the assumption that callers would want to handle
the failures differently. None ever did. Every call site caught the base class
and recorded what happened; nothing in the repository caught a subclass
individually.

Meanwhile the thing callers actually needed from a failure — which failure it
was, in a form that could be written to a run record and counted — had to be
recovered from the exception's type name.

## Decision

One exception, `AnalysisError`, carrying:

- `kind`, a `Literal` of `source_too_large`, `transport`, `refused`,
  `incomplete`, `invalid_after_correction`
- the attempt records made before the failure, empty when the failure preceded
  any call
- the token usage the responses actually reported, zero when no response
  arrived — never a fabricated stand-in

Callers that need to distinguish failures match on `.kind`.

## Alternatives considered

- **Keep the hierarchy.** It is the conventional answer and it is what Python
  exceptions are for. It was costing six class definitions to express
  something no caller used, and the failure kind still had to be turned into a
  string for the run record.
- **Plain string error codes, no `Literal`.** Same ergonomics at the call
  site, no type checking. The `Literal` is what makes a new failure kind a
  mypy error at every exhaustive match rather than a silent fall-through.
- **An enum rather than a `Literal`.** Equivalent in safety; a `Literal` of
  strings serialises into the run record without a conversion step, and the
  run record is where these values are read.

## Consequences

Adding a failure mode is one `Literal` member plus whatever mypy then flags,
rather than a new class and a new place in the hierarchy to reason about.

The cost is that a caller cannot select one failure kind with `except`. It
must catch `AnalysisError` and filter on `.kind`, re-raising what it did not
want. This is acceptable because no caller does that today:
`scripts/run_analysis.py` catches `AnalysisError` once and records
`error.kind` into the run record without branching on it. If a caller ever
needs real per-kind control flow, that is the signal to revisit this — with a
record that supersedes this one.

`AttemptOutcome` is a separate `Literal` on the same reasoning: it describes
what one call produced (`valid`, `invalid_analysis`, `parse_error`, `refused`,
`incomplete`, `technical_failure`), while `kind` describes why the run ended.

## Notes

Back-filled 2026-10-17. Part of the Phase 0 consolidation that merged
`pipeline.py`, `attempts.py`, and `errors.py` into `analysis.py`; see
[REPOSITORY.md](../REPOSITORY.md) for the current shape of that module.
