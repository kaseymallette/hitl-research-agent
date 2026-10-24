# ADR-0017 — Experiment 2: the API against the app on GPT-6.1 Sol, with the primer

- **Status:** Accepted
- **Date:** 2026-10-24
- **Landed in:** not yet committed

## Context

[ADR-0015](0015-phase-1-as-three-experiments.md) set Experiment 2 on kanbur as
a 2 × 3: medium and high effort, each run through the API with GPT-6.1 Sol,
through the ChatGPT app with GPT-6.1 Sol in work mode, and through the app with
GPT-6 in regular chat. It also had me write my notes on each article first, as
the independent reference for judging the runs.

I began kanbur's notes and stopped after three of its 21 steps. The paper is
written for energy-research specialists, and an hour went to terms it never
explains. That reading is what showed the system needed a primer — background
on an article's field to read before it — which
[ADR-0016](0016-a-primer-before-the-reading.md) added. Finishing kanbur's
notes without that background would take hours and record mostly what I did
not understand. What the reading contributed is the finding itself: a reader
new to a field needs the primer before the paper, and the system should
provide it.

Nothing has run for Experiment 2.

## Decision

**Experiment 2 is a 2 × 2 on kanbur's PDF: the API against the app, both with
GPT-6.1 Sol, at medium and high effort, each run making all three calls.**

| | API, GPT-6.1 Sol | App, GPT-6.1 Sol, work mode |
| --- | --- | --- |
| **Medium effort** | 1 | 1 |
| **High effort** | 1 | 1 |

- **Each run makes three calls, in order:** the primer, the close reading, and
  the argument evaluation. Each is its own call — a new chat in the app — and
  the primer is not given to the other two, as ADR-0016 requires.
- **The app runs** keep memory off and my instructions for Sunny on, and follow
  [docs/PROMPTS.md](../PROMPTS.md): the primer and the evaluation as their
  prompts are written, and the close reading with the one format instruction
  the app needs.
- **GPT-6 in regular chat is dropped.** It changed the model and the mode
  together, and the question this experiment can answer cleanly is the one the
  same model on both sides allows: whether the app, with Sunny, reads and
  judges as well as the API.
- **My notes on kanbur are suspended.** The three steps already written stay
  in the workbook, and the runs are judged without a complete independent
  reading.

Runs are saved in `outputs/ab_testing/<slug>/adr_0017/`, as
`pdf__gpt-6.1-sol-<effort>/` for the API and
`app__gpt-6.1-sol-<effort>-work/` for the app. Each holds `primer.md`,
`analysis.json`, and the argument evaluation — `argument_evaluation.json` from
the API, `argument_evaluation.md` from the app — and, for the API, the run and
primer records.

## Alternatives considered

- **Keep the 2 × 3.** The GPT-6 column cannot separate the model from the mode,
  and two more runs by hand.
- **Finish kanbur's notes first, without the primer.** Keeps an independent
  reference, at the cost of hours spent recording what I did not understand —
  the problem the primer exists to solve.
- **Leave the primer out of the experiment.** It would still be written for me,
  but the comparison would not show whether the app writes a better or worse
  primer than the API, which is part of whether the app can replace it.

## Consequences

**Experiment 2 has no full independent reference.** Without my notes, the runs
are compared with each other, against the article itself, and through the
mechanical checks — verbatim text, numbers, citations. That shows where the API
and the app differ and where either is wrong on what the article states. It
cannot show which reading of the argument is better against a judgment of my
own, beyond kanbur's first three steps.

**The primer joins the comparison.** The API and the app each write one, so
the experiment shows whether the primers differ in what they explain and how
well. Neither primer reaches the close reading or the evaluation.

**API against app compares the same model.** A difference comes from the app —
Sunny's instructions, the app's own hidden instructions, work mode, its
handling of the PDF — not from the model.

**The app reports no usage or cost.** Its runs have no run or primer records.

## Notes

Supersedes ADR-0015's design for Experiment 2, and, for Experiment 2 only,
ADR-0016's rule that an experiment article's primer is read after my notes.
ADR-0015's Experiments 1 and 3 stand.
