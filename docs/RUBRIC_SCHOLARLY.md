# Rubric for scholarly articles

DRAFT for review. This combines [RUBRIC.md](RUBRIC.md)'s close-reading
criteria with [RUBRIC_LEGISLATION.md](RUBRIC_LEGISLATION.md)'s
discourse-analysis criteria, for scholarly articles.

You're judging one analysis of one scholarly article, written by a language
model: a close reading and a discourse analysis on the five CDA dimensions. A
researcher will read your judgment while deciding whether to accept the
analysis into a research collection, where it feeds a comparison across
sources. Your judgment informs that decision; it doesn't make it, and the
researcher checks it against their own reading.

The judging is split into sessions, and you're doing one of them. The prompt
that started this session says which. Read the whole rubric, then use the
sections your session needs.

This rubric reports; it never withholds. There are no thresholds and no pass
mark. An analysis that does badly is still judged in full, and the judgment
says what is wrong with it.

You are judging whether the analysis is faithful to the article. Whether the
article's research is sound is not part of the judgment.

---

## What's in the folder

```
RUBRIC.md                      this file
CODEBOOK.md                    the five CDA dimensions and their codes
article.pdf                    the article
article.txt                    its text, marked by page
pages/                         an image of each page
prompts/                       the instructions the analysis followed
  close-reading.md
  discourse-analysis.md
run/
  analysis.json                the close reading
  discourse_analysis.md        the discourse analysis
references/
  claims_reference.md          the article's own claims
judgments/                     where every judgment is written
```

Open only the files your prompt names. Another session's judgment may already
be in `judgments/`; leave it unread, so each judgment stays independent.

Work from the article. Don't look up the works it cites or check its findings
against outside sources; the analysis wasn't asked to either.

### The close reading

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

---

## The sessions

| Session | Reads | Scores | Writes |
| --- | --- | --- | --- |
| 1. Claims reference list | the article alone | — | `references/claims_reference.md` |
| 2. Close reading | the article, `claims_reference.md`, `analysis.json` | A1–A5 | `judgments/close_reading.md` |
| 3. Discourse analysis | the article, `CODEBOOK.md`, `discourse_analysis.md` | B1–B5 | `judgments/discourse_analysis.md` |

The discourse-analysis session never reads the close-reading judgment or the
reference list.

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

Score the close reading against the article on A1–A5, or the discourse
analysis on B1–B5, as your session says.

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

Check these against `article.txt`, the article's extracted text, with a tool
where you can. Report readings of figures, tables, and equations printed as
images separately: a value read off an image is correctly `paraphrased` and
won't appear in the extracted text, so check it against the image by eye and
don't count it as a failure.

### A5. Detail and readability

Described, not scored: the number of steps, how evenly they cover the article,
and whether a reader could follow the article's argument from the reading
alone. Length isn't merit. A longer reading that repeats itself or pads a step
is worse than a shorter one that covers the same ground.

---

## B. Discourse analysis

Judged against the article alone, using `CODEBOOK.md` for what each dimension
and code means. The codebook was written for legislation; a code fits where
the article's passage shows what its definition describes. You are judging
whether each observation is grounded in the article, not whether its
interpretation is the one you would give: the reading is the researcher's to
weigh.

### B1. Grounding

Scored per observation.

- **2** — the passage is at the location given, quoted exactly, and shows
  what the observation says it shows.
- **1** — the passage is there and relevant, but the quotation is altered or
  the reading claims more than the passage carries.
- **0** — the passage isn't in the article, isn't the article's wording, is
  another author's words presented as the article's own, or doesn't show what
  the observation says.

Report the share of observations at each score, per dimension and overall.

### B2. Silencing

For each absence the analysis claims: is the topic actually absent from the
passage it cites, and from the rest of the article? Count confirmed and not
confirmed, and name each one not confirmed with where the topic appears.

### B3. Codes

Counted, not scored: observations whose code fits as the codebook defines it,
observations whose code doesn't fit (name the better code, or "no code
fits"), and observations marked "no code fits". The last are reported for the
researcher, as they may show where the codebook needs a code.

### B4. Errors

Every statement about the article that the article doesn't bear out: a claim
misdescribed, a section or page misplaced, a fact about a cited work, other
research, or legislation presented as if the article said it. Name each.

### B5. Coverage

Described, not scored: the number of observations in each dimension, any
dimension left thin with or without a reason, and anything in the article you
think a dimension should have caught. Say that the last is your own reading.

---

## Not judged

Persuasiveness, effectiveness, clarity of prose, and tone, of the analysis or
of the article. Agreement on these is poor even among trained annotators, so a
score would be noise that gets quoted as if it meant something.
