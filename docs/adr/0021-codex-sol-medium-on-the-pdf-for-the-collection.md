# ADR-0021 — The collection is analyzed by Codex, on GPT-6.1 Sol at medium effort, from the PDF

- **Status:** Accepted
- **Date:** 2026-11-06
- **Landed in:** not yet committed

## Context

Phase 2 judged both experiments head to head
([ADR-0019](0019-four-phases-head-to-head-evaluation.md)), with the results in
[EVALUATION_KEY.md](../EVALUATION_KEY.md). Barnett's bracket went to Sol
medium on the PDF: Sol high was not better, Astra low cost about four times as
much without reading better, and the PDF beat prepared text in the one
close-reading verdict that held with the letters swapped. Kanbur's bracket
went to Sol medium through Codex: Codex won every round, narrowly, and its
final against Codex high held with the letters both ways. The API runs cost
$0.55–0.64 each on kanbur; Codex ran within the ChatGPT Pro plan, four
sessions using about 1% of a week.

Phase 3 needed one configuration for the collection.

## Decision

**Single-source analysis for the collection runs in Codex, on GPT-6.1 Sol at
medium effort, with the PDF as input, from the instruction files in
`prompts/`.**

- Each call is its own Codex session — the close reading, then the argument
  evaluation — as in Experiment 2.
- Each article's output goes to `outputs/analyses/<slug>/`: `analysis.json`,
  `argument_evaluation.md`, and `run_note.md`.
- The input-method question is settled for the PDF.
  [ADR-0008](0008-compare-pdf-against-prepared-text.md) is superseded.

This is the configuration for now. The API path stays in the code.

## Alternatives considered

- **The API, Sol medium, PDF.** Barnett's winner, with an enforced schema,
  exact usage and cost, and settings the run record proves. It lost kanbur's
  semifinal narrowly and costs per run where Codex does not.
- **The ChatGPT app.** Lost to Codex at both efforts, and every call is pasted
  and saved by hand.
- **High effort.** Did not beat medium on either article.
- **Prepared text with crops.** Lost Barnett's final, needs a preparation step
  that took manual fixes, and lost every figure on kanbur.

## Consequences

**What the API guaranteed is now on me.** Codex's output is not checked
against the schema, it reports no tokens or cost, and it cannot confirm the
model or effort it ran at beyond the label requested. A malformed
`analysis.json` is a technical failure and the session is rerun
([ADR-0005](0005-no-hard-quality-gates.md)); nothing else stops a run.

**The choice rests on one article for Codex.** Barnett never ran in Codex, and
every kanbur margin was narrow. It is the choice for now, not a finding.

**The judge has not yet been checked against my own reading**, which
ADR-0019 makes the condition for treating its verdicts as evidence.

**`prepare_sources.py` and its tests can be removed**, along with the
`prepared_text` input modes, now that the PDF is chosen.

**Two Codex sessions per article.** Fifteen articles need running — the
fourteen in `data/research/` and Barnett — with kanbur's Codex medium run
reused.

## Notes

Supersedes [ADR-0008](0008-compare-pdf-against-prepared-text.md). Completes
Phase 2's choice under ADR-0019.
