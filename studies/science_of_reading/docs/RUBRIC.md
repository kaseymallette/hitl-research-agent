# Rubric

You're judging one analysis of one academic article: a close reading and an
argument evaluation, both written by a language model. A researcher will read
your judgment while deciding whether to accept the analysis into a research
collection, where its close reading feeds a comparison across sources. Your
judgment informs that decision; it doesn't make it, and the researcher checks
it against their own reading.

The judging is split into three sessions, and you're doing one of them. The
prompt that started this session says which: the claims reference list, the
close reading, or the argument evaluation. Read the whole rubric, then use the
sections your session needs.

This rubric reports; it never withholds. There are no thresholds and no pass
mark. An analysis that does badly is still judged in full, and the judgment
says what is wrong with it.

---

## What's in the folder

```
RUBRIC.md                      this file
article.pdf                    the article
prompts/                       the instructions the analysis followed
  close-reading.md
  evaluate-argument.md
run/
  analysis.json                the close reading
  argument_evaluation.md       the argument evaluation
references/
  claims_reference.md          the article's own claims
judgments/                     where every judgment is written
```

Open only the files your prompt names. Another session's judgment may already
be in `judgments/`; leave it unread, so each judgment stays independent.

Work from the article. Don't look up the works it cites or check its findings
against outside sources; the analysis wasn't asked to either.

### The two documents in the run

**The close reading** (`analysis.json`) is a reading of the article from start
to finish, recording what the author says without judging it:

- `reading_plan` — the first look: what kind of document it is, how densely it
  reads, and the pace it chose.
- `reading_path` — a list of steps, in the article's order. Each step has:
  - `location` — where in the article the step is.
  - `moves` — what the author is doing there: stating a premise, giving
    evidence, defining a term, drawing an inference, conceding a point.
  - `claims` — the author's claims, each with `text`, a `form` of `verbatim`
    (the author's exact words) or `paraphrased`, and `support`: the evidence
    the author offers, each with its own `text`, `form`, and `citations`
    (`citation_text` as printed, and `reference_entry` from the article's own
    reference list, or null).
  - `meaning` — the reading's reflection on where the step leaves the
    argument.

Claims and support are the author's. Moves and meaning are the model's
reading. That separation is by position: a claim field holding the model's own
inference is a misattribution.

The close reading was asked to keep the author's strength of language — not
softened, not strengthened — to mark `verbatim` only exact wording, to record
a reading of a figure or an equation printed as an image as `paraphrased`,
naming the element, and never to invent or complete a reference.

**The argument evaluation** (`argument_evaluation.md`) is the model's own
judgment of whether the article's argument holds: what it rests on, whether
the conclusions follow, and what bias shapes the author's framing and the
model's own reading. It was written from the article and the close reading,
asked to be selective rather than exhaustive, and to point to the article when
it makes a judgment.

`prompts/` holds the exact instructions the analysis followed. Read the file
for what you're judging before you open the run.

---

## The sessions

| Session | Reads | Scores | Writes |
| --- | --- | --- | --- |
| 1. Claims reference list | the article alone | — | `references/claims_reference.md` |
| 2. Close reading | the article, `claims_reference.md`, `analysis.json` | A1–A5 | `judgments/close_reading.md` |
| 3. Argument evaluation | the article, `argument_evaluation.md` | B1–B6 | `judgments/evaluation.md` |

The close-reading session never reads the argument evaluation, and the
evaluation session never reads the close reading or the reference list. The
evaluation is judged against the article alone.

## The claims reference list

Written once per article, in a session of its own, from the article alone, so
the analysis doesn't shape it. The close-reading session uses it as written
and doesn't change it.

It lists the article's own claims: every enumerated contribution, every claim
in the abstract, the conclusion of every section and subsection as well as the
article's overall conclusions, and every figure and table, each with what it
shows and where it is. Say where the article ends for this purpose: the main
text, or the appendices too.

The list is an inventory of what the article marks as its claims, not a
judgment of what matters most. Where the list and the article disagree, the
article decides.

## Judging the run

Score the run against the article on the criteria for what you're judging:
A1–A5 for the close reading, B1–B6 for the argument evaluation.

For A1, sample 30 claims, drawn at random with a seed you record, or take
every claim if the run has fewer. Score each sampled claim with its support
items.

Write, in this order: the article's file name, the seed (for the close
reading), each criterion's score or counts with the evidence for it, and a
short paragraph on the analysis's main strengths and weaknesses, written for
the researcher deciding whether to accept it.

---

## A. Close reading

### A1. Attribution fidelity

Scored per sampled claim and per support item, against the passage the step's
`location` points to. You find the passage yourself; where you can't, say so
rather than scoring 0.

- **2** — the passage supports it, and the `verbatim` or `paraphrased` marker
  is honest: `verbatim` is the author's exact wording.
- **1** — supported but altered: a scope condition softened, a number detached
  from its unit or context, a hedge dropped or added.
- **0** — the passage doesn't support it, a `verbatim` text isn't the author's
  wording, or the model's own inference is recorded as the author's claim.

Report the share of claims at each score, never a mean. A 1 and a 0 stay
apart on purpose: a softened claim is a fixable reading and an invented one
isn't.

### A2. Coverage

Counted against `claims_reference.md`, not scored. For each type —
contributions, abstract claims, conclusions, figures, tables — report how many
were caught, caught without what they show (a figure named but not read), and
missed. Name what was missed. Say where the reading stops if it stops before
the article does.

Where the reading records one of the article's claims that the list left out,
and you confirm it in the article, note it as found beyond the list. The list
itself stays as it is.

### A3. Strength of language

The document-level pattern behind A1's 1s.

- **2** — conditions, samples, scope, units, and the author's certainty
  survive wherever the article attached them.
- **1** — inconsistent: some kept, some stripped or shifted.
- **0** — systematically shifted in one direction: the reading is more
  confident than the article, or less.

### A4. Mechanical checks

Pass and fail counts, not a score:

- verbatim texts found in the article's text
- numbers found in the article's text
- reference entries matching the article's own reference list

Check these against the article's extracted text, with a tool where you can.
Report readings of figures, tables, and equations printed as images
separately: a value read off an image is correctly `paraphrased` and won't
appear in the extracted text, so check it against the image by eye and don't
count it as a failure.

### A5. Detail and readability

Described, not scored: the number of steps, how evenly they cover the article,
and whether a reader could follow the article's argument from the reading
alone. Length isn't merit. A longer reading that repeats itself or pads a step
is worse than a shorter one that covers the same ground.

---

## B. Argument evaluation

### B1. Premise acceptability

Does it judge whether the evidence offered is worthy of belief — method,
provenance, sample — and point to the text when it does?

- **2** — weighs the evidence behind the central conclusions, with passages.
- **1** — weighs some of it, or calls the evidence weak or strong without
  showing where.
- **0** — takes the evidence at face value.

### B2. Relevance of critique

Does each criticism attach to the claim the author made?

- **2** — every criticism addresses the author's claim as stated, qualifiers
  included.
- **1** — mostly, with a criticism aimed at a broader or weaker claim than the
  one made.
- **0** — its main criticism is of a claim the author didn't make. A straw man
  scores 0 however well it's argued.

### B3. Sufficiency

Does it distinguish evidence that requires the conclusion from evidence that
only permits it?

- **2** — says, for the central conclusions, whether the evidence is enough to
  reach them, and what would be needed if not.
- **1** — raises sufficiency for some conclusions, or only in general terms.
- **0** — treats relevant evidence as if it settled the conclusion.

### B4. Unstated warrants and missing qualifiers

The evaluation was asked to be selective, not to reconstruct the whole
argument, so this scores what it catches, not how many parts of an argument it
names.

- **2** — finds the warrants the conclusions depend on that the author never
  states, and the conclusions stated without the qualifier the evidence calls
  for.
- **1** — finds some, or names them without saying why they matter.
- **0** — finds none where the article has them.

### B5. Self-attribution

- **2** — its judgments are plainly its own, it states its framing and where
  its own reading may be biased, and nothing it concludes is presented as the
  author's position.
- **1** — mostly, with a judgment that reads as the author's or a bias left
  unacknowledged.
- **0** — its view and the author's can't be told apart.

### B6. Correctness

Counted, not scored, with no reference list: check each against the article.

- **Problems raised:** each problem the evaluation finds in the article's
  argument, and whether the article bears it out — confirmed, not confirmed,
  or wrong. Name the passage either way.
- **Errors:** every statement it makes about the article that the article
  doesn't bear out — a number misread, a claim the author didn't make, a
  passage misdescribed. Name each.

You may note a problem you see in the article that the evaluation doesn't
raise, but say that it is your own reading, not a fault the evaluation is
scored on.

---

## Not judged

Persuasiveness, effectiveness, clarity of prose, and tone. Agreement on these
is poor even among trained annotators, so a score would be noise that gets
quoted as if it meant something.

---

## Theoretical foundations

The criteria are the ones used to choose the analysis configuration, where
they compared runs head to head; their sources and how they were adapted are
in [AB_TESTING_RUBRIC.md](AB_TESTING_RUBRIC.md#evaluation-rubric-theoretical-foundations-and-development).
Here they are applied to one analysis at a time, as absolute judgments rather
than comparisons.

Two things change. Only the close reading has a reference list, since it is
an inventory of what the article marks as its claims. The argument evaluation
is checked against the article directly, because a list of problems in the
argument would be the judge's own opinion, and scoring against it would
measure agreement with the judge rather than correctness.
