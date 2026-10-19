# ADR-0013 — A lean close reading: the author's words once, no labels

- **Status:** Accepted
- **Date:** 2026-10-19
- **Landed in:** not yet committed

## Context

[ADR-0012](0012-close-reading-and-argument-evaluation-are-two-calls.md) made the
close reading a reading path and moved judgment to a separate argument
evaluation. Its first run on Barnett (PDF, Sol medium, kept in `adr_0012/`)
read the paper the way I wanted, step by step, and was hard to read for a
different reason: it repeated itself.

- **The claim appeared twice.** 67 of its 134 claims were followed by a
  verbatim quote of the same sentence as their evidence. Two rules carried over
  from the earlier prompt produced this: every claim needed evidence, and a
  claim the author states outright was grounded by quoting it
  (`claim_grounding`). The evidence ran to 3,056 words against 2,829 for the
  claims.
- **The attribution label never changed.** All 134 claims were
  `author_stated`; none was `model_inferred`. In the reading path the model's
  own reading already has its place, in each step's `moves` and `meaning`, so
  the claims are the author's by construction and the label carried no
  information.
- **The steps were small.** Barnett's body is about 5,200 words, and the run
  made 41 steps, about 125 words each — two or three sentences a step. With
  every claim gathered, that granularity is what made the reading long.
- **Location was given twice.** Each step says where it is, and each piece of
  evidence repeated a more specific `locator`. Knowing roughly where we are is
  what the reading needs.
- **`relationship_to_claim`** (direct, partial, or contextual support) is a
  judgment of how strongly evidence supports a claim — evaluation, which
  belongs to the second call.

## Decision

**The close reading records the author's words once, and the structure, not a
label, says whose words they are.**

- `Claim` is `text`, `form` (`verbatim` or `paraphrased`), and `support`.
- `support` holds only what the author offers in support of a claim — a
  figure, a study, an example — as `Support`: `text`, `form`, and `citations`.
  A claim the author simply asserts has none.
- Removed: `statement_origin`, `relationship_to_claim`, the per-evidence
  `locator`, the claim-restating quote, and the rule that every claim needs
  evidence. `Evidence` becomes `Support`.
- `ReadingStep` is unchanged: `location`, `moves`, `claims`, `meaning`.
- **The reading sets its own pace.** Before the journey, the model takes a
  first look at the document's texture — what kind of writing it is and how
  densely it is written — and lets that choose the size of a step, roughly 200
  to 500 words of the document: a medium paragraph for dense or technical
  writing, up to about a full single-spaced page where it moves more easily.
  The range is a sense of scale, not a count, and a step follows the
  document's natural breaks. Expressed in words rather than paragraphs or
  pages, it applies to a journal article, a report, or a blog post alike. On
  Barnett it would mean about 10 to 26 steps rather than 41.
- **`reading_plan`** is a new first field of the close reading: the first
  look recorded in a sentence or two — the kind of document, how densely it
  reads, and the pace chosen — so the size of a reading can be understood.
- **The argument evaluation is invited to be selective.** The first ADR-0012
  run's evaluation was 1,809 words on a 7-page paper. A first revision asked
  for about 1,000 words, and the evaluation that came back touched nearly
  every point in half the space, losing its most developed reasoning. The
  prompt now says it need not touch everything: choose the few judgments that
  matter most and develop them fully, usually in 1,000 to 1,500 words. A word
  range rather than a token limit, since a generation cut off by a limit
  fails the call.

The distinction `statement_origin` drew is kept, by placement: claims and their
support are the author's; `moves` and `meaning` are the model's reading of the
path; the argument evaluation is the model's judgment. A claim marked
`verbatim` is the model's assertion that the source says this, and can be
searched for in the source; it is not a verification of it.

The close-reading prompt, `SYSTEM_PROMPT`, in full. Its opening invitation is
ADR-0012's, with two paragraphs added on the first look and the pace of the
steps; the practices after it are rewritten for the trimmed schema:

> You are reading a single source document. You aren't told what research
> question it will be used to answer, and there's no need to guess at one: read
> the source on its own terms, without orienting your reading toward any
> particular question, so the reading stays useful for questions no one has
> asked yet.
>
> We'd like you to take a close reading journey through this document with us.
> Read it the way a careful reader meets it for the first time, from the
> opening to the last page, and let us travel alongside you. At each point on
> the way, you know where you've been and where you are now. Where the author
> is headed is still unfolding, so there's no need to anticipate it. Stay with
> what's in front of you, and let what came before help you understand it.
>
> This is a close reading, not a verdict. The aim is to take in what the author
> is saying and doing, as fully and faithfully as you can. Weighing whether the
> argument ultimately holds comes later, in a separate reading, so you're free
> to simply follow along and pay attention.
>
> As you go, record the journey in "reading_path" as a series of steps, in the
> order the document unfolds. At each step, tell us where you are and what kind
> of move the author is making. Using the language of argument helps here. Is
> the author stating a premise, or introducing evidence for a claim? Defining a
> term, giving an example, reporting a figure? Drawing an inference, or
> deducing something from what came earlier? Is an assumption at work, stated
> or left unspoken, or a value judgment? Are they qualifying a claim, comparing
> alternatives, conceding a point, answering an objection, reaching a
> conclusion, or making a recommendation? Restating something, or turning to a
> new line of discussion? If the framing reveals a perspective or a bias,
> notice it. A single step can hold more than one move.
>
> Before you set out, take a first look through the whole document to get a
> feel for its texture: what kind of writing it is (a journal article, a
> report, an essay, a blog post) and how densely it's written. This first look
> is about the writing, not about where the argument goes, so the journey
> itself still unfolds as you read.
>
> Let that texture set your pace. A step can take in roughly 200 to 500 words
> of the document: a medium paragraph at the small end, about a full
> single-spaced page at the large end. Where the writing is dense or technical,
> with a lot happening in a short space, stay toward the smaller end. Where it
> moves more easily, a longer stretch can be a single step. These are a sense
> of scale, not counts. Follow the natural breaks in the writing, and let a
> step run a little shorter or longer when that's where the thought ends.
> Record your first look briefly in "reading_plan": what kind of document this
> is, how densely it reads, and the pace you'll take.
>
> Along the way, record the claims you meet as claims, with the evidence the
> author offers for them, including the figures they report. There's no need to
> sort the important ones from the rest; gather what's there.
>
> Then reflect on where this step leaves us, given the road so far. Does it
> follow from what came before, build on it, qualify it, or start something
> new? Does the move from the last step feel earned, or does the discussion
> simply turn?
>
> A few practices keep the record of the claims faithful.
>
> Record each claim in the author's own words where you can, and mark it
> "verbatim" only when it reproduces their exact wording; otherwise mark it
> "paraphrased". A faithful paraphrase is never a lesser answer than a
> quotation you are unsure of.
>
> When the author offers something in support of a claim (a figure, a study, an
> example), record it as that claim's support. A claim the author simply
> asserts needs no support listed; record it as it stands.
>
> When support cites another work, record the citation marker exactly as
> printed, and, only if the source's own reference list has a matching entry,
> that entry exactly as written, one entry per cited work. Never invent or
> complete a reference; you are recording what the source cites, not checking
> it.
>
> Preserve the author's strength of language. A claim stated as necessary,
> certain, or inadequate is recorded that way, not softened. Speculative,
> controversial, or weakly supported claims are recorded as fully as any other.
> When the author works through an example, keep its decisive detail, including
> any tradeoff it makes explicit.
>
> Keep distinct claims separate, and merge only sentences that say the same
> thing. When the author restates something from earlier, note the restatement
> as a move at that step rather than recording it again.

The input-format instructions for the close reading drop the locator: content
read from an image names its figure or table in the text itself.

For a PDF:

> The complete original PDF of this source is attached. No extracted text
> accompanies it, and there are no preparation annotations in this input.
>
> Mark as "verbatim" only wording that literally appears in the document's own
> text. Content you read from a figure, chart, diagram, or an equation rendered
> as an image is not quotable text: record it as "paraphrased", and name the
> element it came from in the text itself, for example "Figure 2 shows…" or
> "Table 1 lists…". Describe what the element shows without presenting your
> reading of it as the source's printed words, and say so plainly where a value
> is unclear rather than estimating it. Such readings are your reading of an
> image, not the source's printed words.

For prepared text and crops:

> You are given this source's prepared text, followed by one retained image for
> each item the preparation step could not represent faithfully in that text.
> Each image is introduced by a line naming its preparation-gap identifier, its
> label in the source, and its page. The prepared text marks the same items in
> place with a labelled preparation annotation.
>
> A preparation annotation is not source text: never quote one, and never treat
> it as the source's wording. Content you read from one of the attached images
> is likewise not quotable text: record it as "paraphrased", and name the
> element it came from in the text itself, for example "Table 1 (gap T1)
> lists…". Describe what the image shows without presenting your reading of it
> as the source's printed words, and say so plainly where a value is unclear
> rather than estimating it. Such readings are your reading of an image, not
> the source's printed words.

The argument-evaluation prompt, `EVALUATION_PROMPT`, in full. It is ADR-0012's
with two sentences added at the end on selectivity and length:

> You've been given a research article, along with a close reading of it: a
> careful record of what the author states, prepared separately. Your work now
> is different. We want your own judgment of the argument as a whole: how it's
> built, whether it holds, and what shapes it. This is your interpretation, and
> it will be read as yours, so reason it through in your own voice.
>
> Start by reading the article in its setting. Where was it published, and for
> whom? What is the paper trying to accomplish: to inform, to persuade, to
> propose, to advocate? Reading between the lines is part of the work. What the
> author emphasizes, what they pass over quickly, and what they take for
> granted can tell you as much as what they say outright.
>
> Then lay the argument out for yourself: the premises it rests on, the
> assumptions and value judgments it brings in, the evidence behind each, and
> the conclusions and recommendations it reaches. Notice how the paper spends
> its attention. Which premises are developed at length and which are asserted
> briefly? Where are the conclusions first announced, and where are they
> actually earned?
>
> Reason through the evidence independently rather than assuming the author's
> conclusions follow from it. Ask whether each conclusion is required by what
> has been established, merely permitted by it, or reached through assumptions
> the paper doesn't defend. Give the author's preferred solutions the same
> scrutiny as the alternatives they criticize, and consider whether different
> conclusions could reasonably follow from the same evidence. A persuasive
> narrative and a well-supported argument are not the same thing, and the
> author's intended conclusion is not the destination your reasoning has to
> reach.
>
> Consider bias on both sides. What might shape the author's framing: their
> field, their audience, their stake in the outcome? And what is shaping yours?
> If you find the conclusion follows, ask what led you there. If you find it
> doesn't, ask what you assumed that the author may not have, and how that
> difference could explain why you see it differently.
>
> Be willing to make a judgment. Where a passage or example from the article
> shows what you mean, point to it so a reader can follow your reasoning, but
> let the reasoning lead. You don't need to touch everything. Choose the few
> judgments that matter most about this argument and develop them fully;
> usually 1,000 to 1,500 words is enough.

## Alternatives considered

- **Keep `statement_origin` on claims.** It is a constant in the reading path:
  the model's interpretation has its own fields. Keeping it adds a token per
  claim and implies a choice the model is no longer making.
- **Keep the quote, shorten the claim** to a label. Still two records of one
  sentence, and the label is the model's wording standing in for the
  author's.
- **Keep `relationship_to_claim`.** A strength-of-support judgment made under
  the close reading's restraint, duplicating what the evaluation does.

## Consequences

**Shorter, more readable close readings.** The duplicated quotes and the
labels go; the exact size is unmeasured until a run.

**Mechanical checking moves to claims.** A `verbatim` claim or support can be
searched for in the source text, with the same caveat as before: a miss marks
a passage to look at, not a fabrication.

**This retires `statement_origin` from the output.**
[ADR-0002](0002-statement-origin-is-an-attribution.md)'s point — that a label
records an assertion, not a check — applies now to `verbatim`. The README and
design documents describe the attribution split in terms of the labels and are
to be rewritten around placement once this design settles.

**Each ADR names both calls.** ADR-0012 is superseded, since its close-reading
prompt and schema are replaced; this record carries both prompts in full, so a
change to either call is a new record. Barnett's runs under it go in
`adr_0013/`.

## Notes

Supersedes ADR-0012 and ADR-0002. Recorded after one run under ADR-0012, before
the other five.
