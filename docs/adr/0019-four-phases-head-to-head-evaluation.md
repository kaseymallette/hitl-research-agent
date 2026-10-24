# ADR-0019 — Four phases, two experiment articles, and a head-to-head evaluation

- **Status:** Accepted
- **Date:** 2026-10-24
- **Landed in:** not yet committed

## Context

The build plan had seven phases: review and redesign, A/B testing, DeepEval,
the research collection, synthesis, literature review, and RAG. Phase 1 was to
run three experiments, one per article
([ADR-0015](0015-phase-1-as-three-experiments.md)), and Phase 2 to build
DeepEval rubrics for eight behavioral axes, apply them through a judge model,
and check the judge against my own scoring.

Two experiments are now run or nearly run: Barnett's six (Experiment 1) and
kanbur's four ([ADR-0017](0017-experiment-2-api-against-the-app-with-the-primer.md)),
whose app runs remain. The work has taken longer than planned, and the plan
was carrying more than this pilot needs. DeepEval meant designing metrics, a
judge pipeline, and its calibration before any answer came out. Lei, the third
article, would be a third experiment designed from the first two. Literature
review is removed ([ADR-0018](0018-three-agents-analysis-synthesis-research-assistant.md)),
and RAG serves synthesis.

## Decision

**The build plan has four phases after Phase 0.**

| Phase | What it does |
| --- | --- |
| **0. Review and redesign** | complete |
| **1. A/B testing** | Experiment 1 on Barnett (complete) and Experiment 2 on kanbur. There is no Experiment 3. |
| **2. Evaluation** | a head-to-head judgment of both experiments by Claude, checked by me, and the choice of how to analyze the collection: model, effort, input method, and API or app |
| **3. Synthesis** | analyze the rest of the collection with that choice, and accept or reject each analysis; build a claims store from the accepted close readings; synthesis across sources from it; and RAG on the same store when the collection outgrows a single call or I want to ask the collection questions |
| **4. Research assistant** | the primer, already built, and guided questions about the article |

**Lei leaves the experiment set.** Its PDF moves from
`data/research/ab_testing/` to `data/research/`, and it is analyzed with the
rest of the collection in Phase 3.

**Phase 2 is a head-to-head judgment, not DeepEval.** For each experiment,
Claude reads the article and every run side by side and writes one judgment:

- **Close readings:** how many of the article's claims and figures each run
  caught or missed, how faithfully each is recorded against the article —
  qualifiers kept, nothing invented — and how detailed and readable each is.
- **Argument evaluations:** whose reasoning holds up, what each found that the
  others did not, and where each is wrong.
- **Primers** (Experiment 2): accuracy and usefulness for a reader new to the
  field.
- **A ranking with reasons,** beside each run's cost.

Judgments are saved apart from the analyses, as `outputs/judgments/<slug>.md`.
I spot-check them — at least one article's ranking against my own reading.

**The input-method question is settled in Phase 2,** from Barnett, where both
methods ran, rather than in a third experiment.
[ADR-0008](0008-compare-pdf-against-prepared-text.md) stays open until then,
and `prepare_sources.py` stays until it is answered.

## Alternatives considered

- **Keep DeepEval and the eight axes.** A fuller instrument, but its design and
  calibration would take longer than the experiments it evaluates, for a pilot
  of two articles.
- **Run Experiment 3 on lei.** It would test the input method on the longest
  article, where it matters most for cost. Barnett already compares the two
  methods, and a third experiment would delay everything after it.
- **Synthesis before evaluation.** Synthesis needs a collection analyzed in one
  configuration, which evaluation chooses.

## Consequences

**Claude is not a blind judge.** It helped design these prompts and has read my
views on the articles, so its judgment carries that context. It is a different
model from the one judged, so it is not grading its own work. One judge, run
once, guides a choice rather than proving it, and an evaluation I have not
checked is not evidence; my spot-check is what makes it usable.

**The README's evaluation design no longer describes a planned instrument.**
Its failure modes still name what the head-to-head looks for; the axes and the
DeepEval procedure go.

**The build plan is rewritten around these phases.** Until then, it describes
the earlier plan.

**ADR-0015's Experiment 3 is superseded.** Its Experiment 1 stands, and its
Experiment 2 was superseded by ADR-0017.

## Notes

Supersedes the seven-phase plan, ADR-0015's Experiment 3, and the planned
DeepEval phase. Recorded with ADR-0018.
