# ADR-0020 — Codex joins Experiment 2 as a third way of running the prompts

- **Status:** Accepted
- **Date:** 2026-10-24
- **Landed in:** not yet committed

## Context

Experiment 2 compared two ways of running the same prompts on kanbur with
GPT-6.1 Sol: through the API, and by hand in the ChatGPT app
([ADR-0017](0017-experiment-2-api-against-the-app-with-the-primer.md)). The
app's readings checked out as well as the API's and cost nothing beyond the
subscription, but every call meant pasting a long prompt and the article into
a new chat and saving the answer by hand.

Codex, the coding agent I already use on this project, is a third way: it can
read the prompt and the article from the repository and write its output where
it is told, with no pasting, and it reports its own usage. If it reads as well,
it could analyze the collection without the API's per-call cost or the app's
manual work.

## Decision

**Experiment 2 gains a Codex column: GPT-6.1 Sol at medium and high effort,
running the close reading and the argument evaluation from instruction files in
`prompts/`.**

| | API | App, work mode | Codex |
| --- | --- | --- | --- |
| **Medium effort** | 1 | 1 | 1 |
| **High effort** | 1 | 1 | 1 |

- **`prompts/close-reading.md`** and **`prompts/evaluate-argument.md`** hold the
  same prompt text the API sends, with the source header filled from
  `data/research/sources.yaml`, the close reading's JSON format instruction as
  in the app, and instructions on what to write and where. A test fails if
  their prompt text stops matching `prompts.py`.
- **Each call is its own Codex session,** so the evaluation does not inherit the
  close reading's context, as the API's second call does not. The primer is not
  run.
- **Each run says how it read the PDF.** Both instruction files ask Codex to
  record, in `run_note.md`, whether it viewed the PDF's pages as images,
  extracted its text with a tool, or both, and whether it could see the
  figures, tables, and equations as printed.
- **Usage is recorded by hand:** Codex's token counts for each session are
  copied into `run_note.md`.

Runs are saved in `outputs/ab_testing/<slug>/adr_0020/codex__gpt-6.1-sol-<effort>/`:
`analysis.json`, `argument_evaluation.md`, and `run_note.md`.

**Phase 1 is reopened** until the two Codex runs are in.

## Alternatives considered

- **Leave Codex out.** Phase 1 was complete. But the experiment's question is
  how to run the prompts for the collection, and Codex is the option that
  removes the manual work.
- **Run Codex through the API's code** (`run_analysis.py`). That would be the
  API with Codex as the operator, not a different way of reading.
- **Replace `docs/PROMPTS.md` with `prompts/`.** `PROMPTS.md` explains the
  prompts to a reader; the files in `prompts/` instruct an agent. Both are kept,
  and both are checked against the code.

## Consequences

**How Codex reads the PDF may change what it is compared on.** The API and the
app send the PDF itself, page images included. A coding agent may extract the
PDF's text with a tool instead, in which case its run is closer to the prepared
text arm than to the PDF arm, and it may miss what exists only as an image —
kanbur's equations among them. `run_note.md` records which, and the comparison
is read with it.

**Codex's usage is not the API's.** It reports tokens per session under its
own plan, so its numbers sit beside the API's run records rather than being
priced by `cost.py`.

**The prompts now exist in three forms** — the code, the readable
`PROMPTS.md`, and the agent files in `prompts/` — kept identical by tests.

## Notes

Adds a column to ADR-0017's design; the API and app columns stand.
