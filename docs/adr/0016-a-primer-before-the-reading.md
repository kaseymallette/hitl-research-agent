# ADR-0016 — A primer on the article's field, for me to read first

- **Status:** Accepted
- **Date:** 2026-10-24
- **Landed in:** not yet committed

## Context

Reading kanbur for Experiment 2, I spent an hour on its first three sections,
and much of it went to terms the article never explains: exergy, membrane
distillation, payback periods, a cost in Singapore dollars per hour. The paper
is written for specialists in energy research. Without that background I could
record its numbers — a 64.5% thermal efficiency, a 3.72-year payback — but not
tell whether they were high, low, or ordinary. My evaluation of its abstract
was a list of questions: relative to what?

That is the problem I had in my philosophy master's, where the reading came
before the lecture: without a map of what matters, every detail looks like it
might, and I read everything at full depth or waited to be told where to look.
The close reading and the argument evaluation help after I have read an
article. Neither tells me, before I start, what the field takes for granted.

I considered a third part of single-source analysis that would integrate the
close reading and the critique into one readable document, and decided that
what I need first is something else: background I can read before the article.

## Decision

**A primer is written for an article on request: background on its field, for
me to read before the article. It is a separate step, not part of the analysis,
and it is never given to the close reading or the argument evaluation.**

The primer explains the concepts and terms the article relies on without
explaining them, what its units measure and what typical values look like in
the field, and where the article sits among the approaches it builds on or
competes with. It leaves the article's own argument for me to meet and does
not judge it.

- `scripts/write_primer.py` runs it on an article's PDF, with GPT-6.1 Sol at
  medium effort by default, and writes `outputs/primers/<slug>/primer.md` with
  a record of its usage and cost.
- `primer.md` opens by saying what it is: the model's general knowledge,
  written to read before the article, unchecked.
- The analysis runs, their prompts, and their records are unchanged.

The prompt, `PRIMER_PROMPT`, in full:

> Before we read this article closely, we'd like your help getting our
> bearings. Picture a reader who is curious and capable but new to this field.
> They'll read the article next, and they want to understand what it's talking
> about when they get there.
>
> Explain the concepts and terms the article relies on without stopping to
> explain them: what each means in plain language, and why it matters for a
> paper like this.
>
> Help the reader know what to compare the numbers against. Say what the units
> measure, and what typical or reference values look like in this field, so a
> figure like an efficiency, a cost, or a scale can be read as high, low, or
> ordinary. Where you aren't sure what's typical, say so.
>
> Place the article in its field: what kind of work it is, the problem it
> belongs to, and the main approaches it builds on or competes with.
>
> This is background, not a summary or a verdict. Leave the article's own
> argument for the reader to meet, and don't judge whether it's right. Because
> this draws on your general knowledge rather than the article itself, write it
> as your own explanation, the way you'd brief a colleague before a meeting. A
> page or two is plenty.

## Alternatives considered

- **Integration as a third analysis call,** combining the close reading and
  the critique into one readable document. Useful, and it may come back, but
  it answers what an article says once I have read it, not what I need to
  know before I start.
- **Give the primer to the argument evaluation too,** so the critique can ask
  "relative to what?" with context. The critique would inherit the primer's
  framing and any of its errors, and the experiments compare the analysis as
  it stands. If it is tried, it is an experiment of its own.
- **Give it to the close reading.** The close reading records what the author
  says; outside background would blur that.

## Consequences

**The primer brings in knowledge from outside the article.** Everything else
in an analysis works from the article. The primer draws on the model's general
knowledge, which cannot be checked against the article, so a mistaken "typical
value" reads as confidently as a correct one. I accept that. It is a reading
aid, held to the standard of a colleague's briefing, not of evidence: I read
it, I keep what helps, and the article and the analysis are where claims get
checked.

**Reading the primer first changes my notes.** For an article I read for my
research, that is the point. For an experiment article, my notes are the
independent reference the analyses are judged against, so the primer comes
after them. Kanbur's notes were begun without one, so Experiment 2 stays as
designed.

**It stays question-independent.** The primer explains the article's field, not
what I am looking for, so it receives no research question
([ADR-0006](0006-analysis-and-synthesis-never-receive-the-question.md)).

**It is cheap and optional.** One call on the article, a page or two out, run
only when I want one.

## Notes

Recorded during Experiment 2, before any of its runs.

For Experiment 2 only, ADR-0017 makes the primer part of each run and suspends
my notes on kanbur, so the rule that an experiment article's primer is read
after my notes does not apply there. The primer is still never given to the
close reading or the evaluation.
