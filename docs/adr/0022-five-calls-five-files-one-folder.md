# ADR-0022 — An article's single-source analysis is five Codex calls, run by one script, writing five files to one folder

- **Status:** Accepted
- **Date:** 2026-11-11
- **Landed in:** not yet committed

## Context

The seven articles in the collection were analyzed and judged in the Codex
app, one pasted prompt per session, from `evaluations/README.md`. The five
calls — the close reading, the claims reference, the close reading's
judgment, the argument evaluation, and its judgment — wrote to three places:
`outputs/analyses/<slug>/` for the runs, `outputs/judgments/<article>/` for
the claims list, judgments and scores, and, for kanbur,
`outputs/ab_testing/`. The prompts for calls 2, 3 and 5 lived in a README and
an older copy in `docs/JUDGING_PROMPTS.md`, and `evaluations/` was a template
copied out of the repository by hand, with copies of the rubric and prompts
kept in sync by a test.

A run could not be reproduced from the repository. Nothing recorded the
model or effort of each session, and the separation between sessions was a
request in the prompt: Lei's run note says both analysis calls ran in one
session and wrote files under other names. Revisions added
`_revised`, `_revised_2` files and score columns by hand.

The ChatGPT app ships a Codex CLI whose `codex exec` runs a session
non-interactively on the ChatGPT sign-in, so the sessions can be scripted
without paying for the API ([ADR-0021](0021-codex-sol-medium-on-the-pdf-for-the-collection.md)).

## Decision

**`scripts/run_single_source.py <slug>` runs an article's five calls, each as
its own `codex exec` session on GPT-6.1 Sol at medium effort, and each writes
one file to `outputs/analyses/<slug>/`:**

```
01_close_reading.json
02_claims_reference.md
03_close_reading_judgment.md
04_argument_evaluation.md
05_argument_judgment.md
```

- The script holds every session's request, so it is the record of how an
  article was run. The analysis prompts stay in `prompts/` and the criteria
  in `docs/RUBRIC.md`, both staged into the sessions that read them.
- Each session runs in a temporary folder holding only the files its call
  reads, and only its one output file is copied back.
- A revision edits 01 or 04 in place from its judgment (`--revise`), and the
  judgment is rerun (`--only`), overwriting its file. Git keeps the earlier
  versions. There are no revision files and no score bar: whether and how
  often to revise is my decision.
- Only a technical failure stops a call — Codex erroring or timing out, the
  file not written, or a close reading that is not JSON
  ([ADR-0005](0005-no-hard-quality-gates.md)).
- No API key is passed to Codex, so it never bills per token.

## Alternatives considered

- **Keep running in the Codex app.** No cost difference, but every prompt is
  pasted, every file copied, and nothing enforces the file names or the
  separation between sessions.
- **The API path in `run_analysis.py`.** Enforced schema and exact usage, but
  billed per run on top of the ChatGPT plan, and it has no judging calls.
- **A file per revision and a scores table.** What the first seven articles
  did; it made more than five files per article and needed hand-kept columns.
- **A score threshold that triggers revision automatically.** Not decided:
  how much to spend on revising is open, and a bar is a short step from a
  quality gate.

## Consequences

**The five files are the whole record in the repository.** The model and
effort are fixed in the script, not proven per run; Codex's event log and
final message, which include token usage and how the PDF was read, go to
`.codex_runs/<slug>/` and are not committed.

**A revision's history is git's.** Commit before `--revise` to keep the
version being revised; the scores of earlier versions are in earlier
commits of the judgment, not in a table.

**Isolation keeps files out of a session's way; it doesn't lock them.**
Codex's `workspace-write` sandbox limits writes, not reads, so a session
could still read the repository by absolute path if it went looking.

**The first seven articles stay in the old layout.** `evaluations/` and
`docs/JUDGING_PROMPTS.md` are removed, and `outputs/collection.yaml` still
points at their files.

## Notes

Supersedes the output layout in
[ADR-0021](0021-codex-sol-medium-on-the-pdf-for-the-collection.md); its model,
effort, and PDF input stand.

2026-11-11: the first seven articles were moved into the five-file layout as
well, with their accepted versions renamed 01–05 and `outputs/collection.yaml`
pointed at them. Their earlier versions, run notes, and score tables are in
git history. Barnett's and kanbur's Phase 2 tournaments, and the prepared
text they were tested on, moved under `outputs/ab_testing/`.
