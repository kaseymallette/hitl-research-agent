# Rubric

You're judging several analyses of one article. Each analysis came from the
same instructions, run with a different model configuration or input method.
Your judgment helps choose which configuration to use for a larger collection
of articles. It guides that choice; it doesn't prove it, and a researcher
checks it against their own reading.

The judging is split into separate sessions, and you're doing one of them.
The prompt that started this session says which: one run's close reading, one
run's argument evaluation, every run's close readings or evaluations head to
head, or the primers. Judging each run alone first, in its own session, keeps
its scores tied to the article rather than to whichever run was read before
it. Read the whole rubric, then use the sections your session needs.

This rubric reports; it never withholds. There are no thresholds and no pass
mark. A run that does badly is still judged in full, and the judgment says
what is wrong with it.

---

## What's in the folder

```
article.pdf
runs/
  A/
    analysis.json              the close reading
    argument_evaluation.*      the argument evaluation, .json or .md
    primer.md                  background on the field, in some runs only
  B/
  …
prompts/                       the instructions the runs followed, if included
judgments/                     where every session writes
```

Open only the files your prompt names. Other sessions' judgments may already
be in `judgments/`; leave them unread unless your prompt gives them to you, so
each judgment stays independent.

The runs are labelled by letter, and you aren't told which configuration
made each one or what it cost, so you judge only what each wrote. Cost and
runtime are weighed against your judgment afterwards, outside it.

Work from the article. Don't look up the works it cites or check its findings
against outside sources; the runs weren't asked to either.

### The three documents in a run

**The close reading** (`analysis.json`) is a reading of the article from start
to finish, recording what the author says without judging it:

- `reading_plan` — the run's first look: what kind of document it is, how
  densely it reads, and the pace it chose.
- `reading_path` — a list of steps, in the article's order. Each step has:
  - `location` — where in the article the step is.
  - `moves` — what the author is doing there: stating a premise, giving
    evidence, defining a term, drawing an inference, conceding a point.
  - `claims` — the author's claims, each with `text`, a `form` of `verbatim`
    (the author's exact words) or `paraphrased`, and `support`: the evidence
    the author offers, each with its own `text`, `form`, and `citations`
    (`citation_text` as printed, and `reference_entry` from the article's own
    reference list, or null).
  - `meaning` — the run's reflection on where the step leaves the argument.

Claims and support are the author's. Moves and meaning are the run's reading.
That separation is by position: a claim field holding the run's own inference
is a misattribution.

The close reading was asked to keep the author's strength of language — not
softened, not strengthened — to mark `verbatim` only exact wording, to record
a reading of a figure or an equation printed as an image as `paraphrased`,
naming the element, and never to invent or complete a reference.

**The argument evaluation** is the run's own judgment of whether the
article's argument holds: what it rests on, whether the conclusions follow,
and what bias shapes the author's framing and the run's own reading. It was
asked to be selective rather than exhaustive, and to point to the article
when it makes a judgment.

**The primer**, where there is one, is background on the article's field for
a reader new to it, written before the reading. It's allowed imperfections;
it's judged on whether it helps.

If `prompts/` is in the folder, read it before the runs. It holds the exact
instructions the runs followed.

---

## The sessions

| Session | Reads | Scores | Writes |
| --- | --- | --- | --- |
| Close reading, first run | the article, then run A's `analysis.json` | the claims reference list, then A1–A5 | `claims_reference.md`, `close_reading_A.md` |
| Close reading, each further run | the article, `claims_reference.md`, that run's `analysis.json` | A1–A5 | `close_reading_<run>.md` |
| Close readings, head to head | the article, `claims_reference.md`, every run's `analysis.json` | comparison and ranking | `close_reading_head_to_head.md` |
| Evaluation, first run | the article, then run A's argument evaluation | the problems reference list, then B1–B6 | `problems_reference.md`, `evaluation_A.md` |
| Evaluation, each further run | the article, `problems_reference.md`, that run's argument evaluation | B1–B6 | `evaluation_<run>.md` |
| Evaluations, head to head | the article, `problems_reference.md`, every run's argument evaluation | comparison and ranking | `evaluation_head_to_head.md` |
| Primers, where runs have them | the article, every run's `primer.md` | P, and a ranking | `primers.md` |

The close-reading sessions never read an argument evaluation, and the
evaluation sessions never read a close reading. Each is judged against the
article alone.

## The reference lists

Each list is written once, by the first session that needs it, from the
article alone and before that session opens any run, so no run shapes it.
Later sessions use it as written and don't change it.

- **`claims_reference.md` — the article's own claims.** Every enumerated
  contribution, every claim in the abstract, every conclusion, and every
  figure and table, each with what it shows and where it is. Say where the
  article ends for this purpose: the main text, or the appendices too.
- **`problems_reference.md` — problems in the argument.** Where the article's
  reasoning fails, contradicts itself, or doesn't add up, each with the
  passage.

## Judging one run

Score the run against the article and the reference list, on the criteria
for what you're judging: A1–A5 for a close reading, B1–B6 for an argument
evaluation.

For A1, sample 30 claims, drawn at random with a seed you record, or take
every claim if the run has fewer. Score each sampled claim with its support
items.

Write, in this order: the run's letter, the seed (for a close reading), each
criterion's score or counts with the evidence for it, and a short paragraph
on the run's main strengths and weaknesses.

## Comparing head to head

With every run in front of you, write:

- **What each caught that the others missed.** For close readings, against
  `claims_reference.md`. For evaluations, against `problems_reference.md`; a
  problem a run found that isn't on the list, and that you confirm against
  the article, is recorded here as found by that run, and the list itself
  stays as it is.
- **Where each is wrong** that the others aren't.
- **A ranking,** best to worst, with reasons drawn from the criteria.
- **Close calls.** Where two runs are close, compare just those two, twice,
  once in each order, and record whether the verdict held. A verdict that
  flips with the order is a tie.

You don't need to rescore every criterion; use them as the grounds for the
comparison.

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
  wording, or the run's own inference is recorded as the author's claim.

Report the share of claims at each score, never a mean. A 1 and a 0 stay
apart on purpose: a softened claim is a fixable reading and an invented one
isn't.

### A2. Coverage

Counted against the reference list of the article's own claims, not scored.
For each type — contributions, abstract claims, conclusions, figures, tables —
report how many were caught, caught without what they show (a figure named
but not read), and missed. Name what was missed. Say where the reading stops
if it stops before the article does.

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

Counted, not scored:

- **Problems found:** which problems on your list the evaluation found, and
  which it missed.
- **Errors:** every statement it makes about the article that the article
  doesn't bear out — a number misread, a claim the author didn't make, a
  passage misdescribed. Name each.

What a run found that no other did is recorded in the head-to-head session,
once every run is read.

---

## P. Primer

Where a run has one:

- **Accuracy:** errors about the field, named, and whether any would mislead a
  reader of this article.
- **Usefulness:** whether a reader new to the field could follow the article
  after reading it — the terms it explains, and the ones the article needs
  that it leaves out.

---

## Not judged

Persuasiveness, effectiveness, clarity of prose, and tone. Agreement on these
is poor even among trained annotators, so a score would be noise that gets
quoted as if it meant something.
