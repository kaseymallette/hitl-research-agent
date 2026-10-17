# ADR-0003 — Identifier, provenance, and timestamp stay out of the schema sent to the model

- **Status:** Accepted
- **Date:** 2026-09-25
- **Landed in:** `ed45638`

## Context

A saved analysis needs three things the model has no legitimate value for: an
identifier, the source's provenance, and when the analysis was produced. If
those fields appear in the schema handed to the API, the model will fill them
— structured output asks it to — and it will fill them plausibly. A
hallucinated UUID looks exactly like a real one. A hallucinated
`analyzed_at` is a valid timestamp. The usual mitigation is to overwrite the
model's values after the call, which works until one overwrite is missed, and
a missed overwrite is undetectable by inspection.

## Decision

Two layers, kept apart.

- **`ExtractedAnalysis`** is the schema sent to the API. Every field in it is
  content the model is allowed to supply: research problem, claims,
  methodology, assumptions, limitations, proposed solutions, open questions.
  It holds no identifier, no provenance, and no timestamp.
- **`SourceAnalysis`** wraps that content with `id`, `provenance`, and
  `analyzed_at`, which the application sets.

`ResearchBaseModel` sets `extra="forbid"`, so a model that invents a field
fails loudly instead of having it dropped.

## Alternatives considered

- **One flat model, with the application overwriting the owned fields after
  the call.** Rejected for the reason above: correctness depends on an
  overwrite that is invisible when it is missing.
- **One flat model, with the owned fields validated as absent.** Closer, but
  it spends a validation failure on something the schema can simply not ask
  for — and it still shows the model fields it must not fill.
- **A parallel `Extracted*` class for every nested type** (`ExtractedClaim`,
  `ExtractedEvidence`, …) to strip identifiers at each level. This was built
  in v1 and removed in the Phase 0 consolidation (`39a64df`): the nested UUIDs
  were never read anywhere, so the duplicate classes and the 40-line function
  that copied between them were cost with no return. The split belongs at the
  top level only.

## Consequences

Nothing application-owned can be hallucinated, because the model is never
shown a place to put it. The API schema is also smaller, which is a secondary
benefit, not the reason.

The cost is two types where one would read more simply, and a wrapping step
between the call returning and the result being saved. Anyone reading
`models.py` has to hold the distinction to understand why `Claim` has no `id`.

`test_models.py` asserts that application-owned fields are rejected from model
content, so the boundary is checked rather than merely intended.

## Notes

Back-filled 2026-10-17. Related:
[ADR-0002](0002-statement-origin-is-an-attribution.md) — the other place where
a field's meaning is narrower than its name suggests.
