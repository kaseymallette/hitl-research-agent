# ADR-0018 — Three agents: single-source analysis, synthesis, and a research assistant

- **Status:** Accepted
- **Date:** 2026-10-24
- **Landed in:** not yet committed

## Context

The system was designed around three agents: single-source analysis, synthesis
across sources, and a literature review agent that would take a research
question and propose articles. The literature review agent was the only part
meant to see a research question.

Two things have changed since. Single-source analysis became two readings, the
close reading and the argument evaluation
([ADR-0012](0012-close-reading-and-argument-evaluation-are-two-calls.md)), and
the evaluation turned out to be a different kind of document: the model's
judgment, read as its interpretation. And reading kanbur produced something the
design had no place for — a primer on an article's field, written for me to
read before the article ([ADR-0016](0016-a-primer-before-the-reading.md)).
What I need from a third agent is help reading, not help finding.

For finding articles, I collected the 16 in this pilot myself, and I plan to
pilot Consensus, a tool built for finding research, for that work later.

## Decision

**The system has three agents.**

| Agent | Works on | Produces |
| --- | --- | --- |
| **Single-source analysis** | one article | the close reading and the argument evaluation |
| **Synthesis** | the accepted close readings | a comparison of what the authors claim, across sources |
| **Research assistant** | one article | a conceptual framework for reading it — the primer — and, planned, guided questions about the article |

- **Synthesis reads only close readings.** It compares what authors claim. The
  argument evaluation is the model's judgment of one article's argument; it
  stays a separate document for my review and for evaluating the model's
  reasoning, and never becomes part of what "the sources say."
- **The research assistant serves me as a reader.** Its first capability is the
  primer, already built. Its second, guided questions, is about the article —
  questions to read it with — and is designed after Phase 1, so Experiment 2's
  primers are written by one prompt throughout.
- **Finding articles is outside the system.** The literature review agent is
  removed. For this pilot I found the articles; later I will try Consensus.

**No part of the system receives the research question.** With the literature
review agent gone, every agent is question-independent. The research question
stays with me, and with whatever tool I use to find articles.
[ADR-0006](0006-analysis-and-synthesis-never-receive-the-question.md)'s rule for
analysis and synthesis now covers the research assistant too.

## Alternatives considered

- **Keep the literature review agent.** It would duplicate a purpose-built tool,
  and it was the one place a research question could shape what the system
  produces.
- **Synthesize across evaluations as well as close readings.** That would let
  synthesis compare the model's judgments of different arguments, but it would
  put model judgment alongside author claims in one comparison, the blending
  the design exists to prevent.
- **Make the primer part of single-source analysis.** The primer draws on the
  model's general knowledge rather than the article, and serves me rather than
  the collection; it belongs with a reading aid, not with the analysis.

## Consequences

**The system is presented as a pipeline and a companion.** Single-source
analysis and synthesis build the research collection. The research assistant
was developed alongside, because of what I needed while reading.

**Guided questions are planned, not built.** Their prompt is drafted with me,
like the others, after Phase 1.

**The README, DESIGN, and the phases change.** The agent tables lose the
literature review agent and gain the research assistant, and the build plan's
phases follow ([ADR-0019](0019-four-phases-head-to-head-evaluation.md)).

## Notes

Recorded after Experiment 2's API runs and before its app runs.
