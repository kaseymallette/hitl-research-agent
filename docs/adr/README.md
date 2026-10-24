# Architecture Decision Records

One file per architectural decision: what was decided, what else was on the
table, and what it cost.

Numbers are allocation order — the order the records were written — and are
never reused or reshuffled. Each record carries the date its decision was
made, which is the date to read it by. That is why 0008 is dated before 0006
and 0007: it was written later. The table below is in date order.

## Why this exists

From [README.md](../../README.md#development-approach-and-lessons):

> The architecture drifted without my deciding it should. No single step chose
> to turn quotation matching into a hard acceptance gate, but it arrived there
> across many small changes that each looked reasonable at the time, and the
> direction was only visible in aggregate.

That is the failure these records are for. Once a decision is written down with
a number, a change that contradicts it has to say so: either it cites the
record and stays inside it, or it supersedes the record with a new one. Drift
becomes a visible act at the moment it happens rather than something only
legible in aggregate, months later.

## Conventions

**Records are immutable.** A record is not edited after it is accepted, except
to mark it superseded. A decision that gets reversed produces a *new* record
that supersedes the old one and says why the reversal happened. The wrong turn
stays readable, for the same reason nothing is rewritten in the
[prompt log](../PROMPT_LOG.md): the record of how the thinking moved is the
point.

Repairing a link whose target moved is not an edit to the record. The
reasoning is what must not change.

**One decision per record.** If two things were decided together and either
could be reversed without the other, they are two records.

**A record is for a decision that constrains later work.** Whether to pin a
dependency exactly, whether a label means verification, whether a check may
stop a run. Not for an implementation detail with an obvious right answer, and
not for anything the type checker already enforces.

**Write a new record when a decision is made, not afterward.** The eight below
were back-filled on 2026-10-17, which is why each one carries both the date the
decision was made and the commit where it landed. Back-filling is a one-time
catch-up, not the procedure.

**A record can hold a question open.** 0008 is `Provisional`: it records the
decision to settle the input format by experiment rather than by argument, and
states in advance what evidence will settle it. When Phase 1 reports, a new
record states the outcome and supersedes it. A decision deferred on purpose is
still a decision, and writing it down is what stops it drifting closed.

### How these relate to the other documents

| Document | Holds | Tense |
| --- | --- | --- |
| **ADRs** (here) | one decision each, with its alternatives and costs | past: what was decided, when |
| [DESIGN.md](../DESIGN.md) | what the system is and the rules it holds to | present: the stable contract |
| [REPOSITORY.md](../REPOSITORY.md) | what every file currently is and why it exists | present: current state |
| [BUILD_PLAN.md](../BUILD_PLAN.md) | the phases, in engineering detail | future: what is planned |
| [PROMPT_LOG.md](../PROMPT_LOG.md) | the prompts given to the assistants, and what came back | past: how the work went |

The overlap to watch is with `REPOSITORY.md`. That document describes the
repository as it stands and is rewritten as the repository changes; an ADR
describes a choice at a moment and is not. When they disagree, the repository
inventory is the state and the ADR is the history — and the disagreement is
itself worth looking at, because it usually means a decision was reversed
without a record.

## The records

| # | Decision | Date | Status |
| --- | --- | --- | --- |
| [0001](0001-src-layout-for-the-package.md) | The package lives under `src/`, so tests exercise the installed build | 2026-08-26 | Accepted |
| [0002](0002-statement-origin-is-an-attribution.md) | `statement_origin` records an attribution, not a verification | 2026-09-12 | Superseded by 0013 |
| [0003](0003-application-owned-fields-stay-out-of-the-model-schema.md) | Identifier, provenance, and timestamp stay out of the schema sent to the model | 2026-09-25 | Accepted |
| [0004](0004-pin-pymupdf4llm-exactly.md) | `pymupdf4llm` is pinned to an exact version | 2026-10-13 | Accepted |
| [0005](0005-no-hard-quality-gates.md) | Only a technical failure stops a run; analysis quality never does | 2026-10-15 | Accepted |
| [0008](0008-compare-pdf-against-prepared-text.md) | Compare sending the full PDF against prepared text plus crops | 2026-10-15 | **Provisional** |
| [0006](0006-analysis-and-synthesis-never-receive-the-question.md) | Single-source analysis and synthesis never receive the research question | 2026-10-15 | Accepted |
| [0007](0007-one-analysis-error-with-a-kind.md) | One `AnalysisError` carrying a `kind`, not an exception hierarchy | 2026-10-15 | Accepted |
| [0009](0009-phase-1-matrix-three-configurations-three-articles.md) | Phase 1 runs three model configurations over three articles | 2026-10-17 | Accepted for Barnett; superseded in part by 0014 and 0015 |
| [0010](0010-whole-document-argument-assessment.md) | Every analysis carries a whole-document argument assessment | 2026-10-18 | Superseded by 0012 |
| [0011](0011-claims-first-then-whole-document.md) | Claims first, then the whole document: test one call before two turns | 2026-10-18 | Superseded by 0012 |
| [0012](0012-close-reading-and-argument-evaluation-are-two-calls.md) | The close reading and the argument evaluation are two calls | 2026-10-19 | Superseded by 0013 |
| [0013](0013-lean-close-reading.md) | A lean close reading: the author's words once, no labels | 2026-10-19 | Accepted |
| [0014](0014-kanbur-replaces-katakam.md) | Kanbur replaces katakam as the third experiment article | 2026-10-19 | Accepted |
| [0015](0015-phase-1-as-three-experiments.md) | Phase 1 runs as three experiments, one per article | 2026-10-20 | Accepted for Experiment 1; superseded in part by 0017 and 0019 |
| [0016](0016-a-primer-before-the-reading.md) | A primer on the article's field, for me to read first | 2026-10-24 | Accepted |
| [0017](0017-experiment-2-api-against-the-app-with-the-primer.md) | Experiment 2: the API against the app on GPT-6.1 Sol, with the primer | 2026-10-24 | Accepted |
| [0018](0018-three-agents-analysis-synthesis-research-assistant.md) | Three agents: single-source analysis, synthesis, and a research assistant | 2026-10-24 | Accepted |
| [0019](0019-four-phases-head-to-head-evaluation.md) | Four phases, two experiment articles, and a head-to-head evaluation | 2026-10-24 | Accepted |
| [0020](0020-codex-joins-experiment-2.md) | Codex joins Experiment 2 as a third way of running the prompts | 2026-10-24 | Accepted |

New records start from [template.md](template.md).
