# ADR-0005 — Only a technical failure stops a run; analysis quality never does

- **Status:** Accepted
- **Date:** 2026-10-15
- **Landed in:** `1269a28`

## Context

v1 accumulated acceptance gates one step at a time. A grounding check added to
catch one failure became a condition the next step had to satisfy, and
quotation matching ended up deciding whether an analysis was returned at all.
No single change chose that. It arrived across many small changes that each
looked reasonable, and the direction was visible only in aggregate.

The gate was also measuring the wrong thing. A failure to find a quotation in
the extracted text is weak evidence of anything: PDF extraction, markdown
formatting, line-break hyphenation, and OCR all break exact matching on text
the source genuinely contains. And a faithful paraphrase is `author_stated`
while appearing nowhere in the document, so the check cannot see it at all.
The gate withheld correct analyses and passed incorrect ones.

## Decision

Only a technical failure stops a run:

- an API or transport error
- a refusal
- a truncated generation
- output that will not parse into the schema, after one correction attempt
- a source too large to send
- a response that reports no usage metadata

Nothing about analysis *quality* withholds a result. A paraphrase instead of a
quotation, a claim with no evidence item, a missing evidence label, a thin
analysis: all of these are reported and handed to the researcher. Evaluation
reports; it does not gate.

The missing-usage case belongs on this list and is worth naming: it is a
technical failure, not a quality judgment. Recording zero tokens for a call
that happened would corrupt the cost record, and the cost record is the
experiment's output.

## Alternatives considered

- **Keep the gate with a tunable threshold.** There is no principled value to
  tune it to, and the failure it produces — withholding a correct analysis —
  is worse than the one it prevents, because a withheld analysis is never
  reviewed and a weak one is.
- **Gate only on `verbatim` evidence,** where a text search is at least
  meaningful. This still fails on extraction artifacts, and it creates an
  incentive for the model to mark evidence `paraphrased` to avoid the check.
- **Warn and withhold** — return nothing but explain why. The researcher
  cannot judge what they cannot see.

## Consequences

The researcher sees weak analyses. That is the intended outcome: the human
decision — accept, reject, revise, rerun — is the gate, and it cannot operate
on output that was withheld.

There is no automatic protection against a poor analysis reaching review. The
cost of this decision is paid in the researcher's time, deliberately.

The stop list above lives in `analysis.py` and is deliberately short. Adding
to it is a change to this decision and needs a record that supersedes this
one.

A refusal and a truncated generation stop the run *without* spending the
single correction attempt, since neither is something corrective feedback can
fix.

## Notes

Back-filled 2026-10-17. Stated as rule 2 of the workflow contract in
[DESIGN.md](../DESIGN.md). Related:
[ADR-0002](0002-statement-origin-is-an-attribution.md), which rejects the same
text-matching reasoning at the schema level.
