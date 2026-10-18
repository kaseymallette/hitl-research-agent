# ADR-0006 — Single-source analysis and synthesis never receive the research question

- **Status:** Accepted
- **Date:** 2026-10-15
- **Landed in:** `0fd1ccf`

## Context

The system has three agents and one research question at a time. The obvious
design passes the question to every agent: an analysis that knows what is
being asked can emphasise the relevant material and skip the rest, which is
cheaper and reads as more useful.

Two things argue against it. An analysis shaped toward a question is only
usable for that question, and the collection is meant to outlive any single
question — the pilot study's 16 articles are a starting point for an
investigation that will keep asking new things of the same sources. And an
agent that knows what is being looked for is an agent that can find it: the
risk is not fabrication so much as emphasis, a claim promoted because it bears
on the question rather than because it bears on the source's argument.

## Decision

| Agent | Receives the question? |
| --- | --- |
| Single-source analysis | No |
| Synthesis | No |
| Literature review | Yes — and it only proposes candidates |

Single-source analysis describes the source. Synthesis compares what the
sources say to each other, not to a question. Only the literature review agent
reads the research question, and its output is candidate articles with stated
relevance, which the researcher selects from.

## Alternatives considered

- **Pass the question to analysis.** Cheaper and more immediately relevant
  output, at the cost of analyses that cannot be reused and an analysis step
  that is partly looking for an answer.
- **Pass the question to synthesis only,** on the grounds that comparison
  needs a frame. The frame synthesis needs is the sources themselves — what
  they agree on, where they conflict, how their methods differ — and that
  frame is question-independent.
- **Pass the question as context but instruct the model to ignore it for
  selection.** An instruction not to use information the model has been given
  is not a boundary that can be verified.

## Consequences

An analysis produced today stays usable for a question asked next year. Phase
3's collection and Phase 6's retrieval both depend on this; retrieval across
analyses is only worth building if the analyses are not already filtered to
one question.

The cost is that every analysis contains material irrelevant to whatever is
currently being asked, which means more tokens per analysis and more to read.
Relevance filtering moves downstream, to retrieval and to the researcher.

`tests/test_inputs.py::test_every_mode_sends_the_same_analysis_prompt` checks
the related invariant that the analysis prompt does not vary by input mode.

## Notes

Back-filled 2026-10-17. Stated in the agent table in
[README.md](../../README.md) and in [DESIGN.md](../DESIGN.md).
