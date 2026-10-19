# ADR-0011 — Claims first, then the whole document: test one call before two turns

- **Status:** Superseded by [ADR-0012](0012-close-reading-and-argument-evaluation-are-two-calls.md)
- **Date:** 2026-10-18
- **Landed in:** `dc41c33`

## Context

[ADR-0010](0010-whole-document-argument-assessment.md) added
`argument_assessment`, a whole-document assessment, to every analysis. Rerun on
Barnett, it did what it was for: all six analyses now describe how the
document is organized and how its conclusions follow.

The claim lists got shorter. Astra low on the PDF went from 21 claims to 16,
and Sol high on the text from 33 to 25. The losses were not random. The
separate claims for each cooling approach — cold-climate siting, natural water
bodies, subsea, waterless, reclaimed water — were folded into one general claim
that the approaches are achievable but constrained, and some distinct points
were merged or dropped, including the low-water-price incentive, which now
appears only inside the assessment. Output length did not grow, so the model
was not running out of room; it chose to compress.

Two causes are likely. The ADR-0010 prompt says "keep assessments of secondary
claims selective," which a model can read as being selective about claims
rather than about assessments. And with a field for the big-picture analysis,
the claim list is treated as less important.

Each configuration has run once before ADR-0010 and once after, so how much
the claim count varies between two runs of the same prompt is unknown. Some of
the drop may be ordinary variation.

There are two ways to make the whole-document assessment supplement the claims
rather than replace them:

- **One call, two tasks.** Tell the model, in the one request it already gets,
  that it has two tasks in order — analyze the claims, then assess the whole
  document — and that the second must not replace the first. A prompt change
  only, at no extra cost per run. It nudges the model; it cannot guarantee the
  claims come back.
- **One conversation, two turns.** Turn 1 asks for the claims with the
  instructions in place before ADR-0010; turn 2, in the same conversation,
  asks for the whole-document assessment, building on turn 1. The claims
  return by construction. It costs more per run — though a cached input prefix
  should keep it well under double — and needs real code: two requests, a
  schema split, an attempt record and correction attempt per turn, and a
  decision about turn 2 failing after turn 1 succeeds.

## Decision

**Try one call with two tasks first, and test it before rerunning anything
else. Build two turns only if the test shows one call is not enough.**

The prompt change, drafted for approval before any paid run:

1. Add, after the opening paragraph of `SYSTEM_PROMPT`:

   > Your work has two tasks, done in order. Task 1: analyze the individual
   > claims — capture the distinct substantive claims, their evidence,
   > important qualifications, and, where a claim's importance and wording
   > call for it, an assessment of its support. Task 2: in
   > "argument_assessment", assess the whole document, using your Task 1
   > reconstruction to examine how its conclusions follow, how its argument is
   > organized, and whether the body delivers the scope it promises. Task 2
   > supplements Task 1. It must not replace distinct claims, or their
   > assessments, with broad discussion in "argument_assessment": extract
   > claims as completely as you would if there were no Task 2.

2. In the ADR-0010 paragraph, replace "Always assess this central reasoning;
   keep assessments of secondary claims selective." with "Always assess this
   central reasoning." Which claims get a `support_assessment` is already
   governed by the claim-assessment instructions earlier in the prompt.

Everything else in ADR-0010 stands: the field, its place last in the schema,
and both of its paragraphs otherwise unchanged.

**The test.** Rerun the two Barnett cells that lost the most claims, Sol high
on the text and Astra low on the PDF, about $0.70 together. Outputs go in a new
`adr_0011/` folder beside `adr_0009/` and `adr_0010/`.

**What counts as the claims coming back:**

- each claim count is back near its before-ADR-0010 level (33 and 21);
- the cooling approaches appear again as separate claims, each with its own
  trade-off;
- the low-water-price incentive is a claim of its own;
- `argument_assessment` still assesses the whole document, including its
  organization.

**If they come back,** this record is accepted, Barnett's other four cells are
rerun under the same prompt, and Phase 1 continues with katakam and lei. **If
they do not,** the two-turn design is built under its own ADR, and this record
is marked superseded by it.

## Alternatives considered

- **Accept the shorter claim lists.** Most of the substance survives in merged
  claims or the assessment, at no cost. But the per-technology trade-offs are
  what the analyses are compared against my notes on, and Phase 2's coverage
  scoring would count them as missing.
- **Build two turns now.** Certain to restore the claims, but it is the larger
  change, and one call may be enough. Testing the cheap option first means two
  turns, if it comes to that, is built knowing it is needed.
- **Measure run-to-run variation first.** Would show whether the drop is real
  before fixing it. The test above answers most of the same question, since a
  rerun under a prompt that targets the cause shows whether the claims respond.

## Consequences

**Barnett is rerun a third time** if the test passes, so its analyses are
spread across three folders until Phase 1 is complete. The folders record the
history; the cells in the last one are the Phase 1 result.

**Two runs are a small sample.** A claim count back near its earlier level is
evidence the wording works, not proof, for the same reason the drop itself
may partly be variation.

**ADR-0010's prompt text changes.** That record quotes the prompt word for
word, and this one supersedes the one sentence it replaces.

## Notes

The two-task framing was suggested by Chat. Proposed the day the claim loss was
found, after Barnett's six cells under ADR-0010 and before any other cell ran.

The test ran on the two cells: the claims came back and overshot, to 55 and 30.
Superseded by ADR-0012, which separates the close reading and the argument
evaluation into two calls rather than choosing between this and two turns.
