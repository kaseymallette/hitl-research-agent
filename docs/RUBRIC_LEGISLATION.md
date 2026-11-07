# Rubric for legislation

DRAFT for review. This adapts [RUBRIC.md](RUBRIC.md) to legislative texts.

You're judging one analysis of one legislative text, written by a language
model: a close reading and a discourse analysis on the five CDA dimensions. A researcher will
read your judgment while deciding whether to accept the reading into a
research collection, where it feeds a comparison across sources. Your
judgment informs that decision; it doesn't make it, and the researcher checks
it against their own reading.

The judging is split into sessions, and you're doing one of them. The prompt
that started this session says which. Read the whole rubric, then use the
sections your session needs.

This rubric reports; it never withholds. There are no thresholds and no pass
mark. A reading that does badly is still judged in full, and the judgment
says what is wrong with it.

You are judging whether the reading is faithful to the document. Whether the
legislation is good policy, or whether it represents research accurately, is
not part of the judgment.

---

## What's in the folder

```
RUBRIC.md                      this file
CODEBOOK.md                    the five CDA dimensions and their codes
article.pdf                    the legislative text
prompts/                       the instructions the analysis followed
  close-reading.md
  discourse-analysis.md
run/
  analysis.json                the close reading
  discourse_analysis.md        the discourse analysis
references/
  claims_reference.md          the document's own provisions
judgments/                     where every judgment is written
```

Open only the files your prompt names. Another session's judgment may already
be in `judgments/`; leave it unread, so each judgment stays independent.

Work from the document. Don't look up the laws or sources it cites, or check
its findings against outside sources; the reading wasn't asked to either.

### The close reading

**The close reading** (`analysis.json`) is a reading of the document from
start to finish, recording what it says without judging it:

- `reading_plan` — the first look: what kind of legislative text it is, how
  it is organized, and the pace the reading chose.
- `reading_path` — a list of steps, in the document's order. Each step has:
  - `location` — where in the document the step is, by section and
    subsection.
  - `moves` — what the document is doing there: defining a term, stating a
    finding, requiring, prohibiting, permitting, assigning authority,
    funding, setting a deadline or a consequence, amending other law.
  - `claims` — the document's provisions, each with `text`, a `form` of
    `verbatim` (the exact words) or `paraphrased`, and `support`: the basis
    the document offers for it, such as a finding or a named source, each
    with its own `text`, `form`, and `citations` (`citation_text` as printed,
    and `reference_entry`, which is null unless the document prints a full
    entry).
  - `meaning` — the reading's reflection on where the step leaves the
    document.

Provisions and support are the document's. Moves and meaning are the model's
reading. That separation is by position: a claim field holding the model's own
inference is a misattribution.

The reading was asked to keep the document's strength of language (shall,
must, may, should; open and closed lists), to keep who must act and under what
conditions, to record amended text as it reads after the change and never
struck-through text as a provision, to mark `verbatim` only exact wording, and
never to invent or complete a citation.

---

## The sessions

| Session | Reads | Scores | Writes |
| --- | --- | --- | --- |
| 1. Provisions reference list | the document alone | — | `references/claims_reference.md` |
| 2. Close reading | the document, `claims_reference.md`, `analysis.json` | A1–A5 | `judgments/close_reading.md` |
| 3. Discourse analysis | the document, `CODEBOOK.md`, `discourse_analysis.md` | B1–B5 | `judgments/discourse_analysis.md` |

The discourse-analysis session never reads the close-reading judgment or the
reference list.

## The provisions reference list

Written once per document, in a session of its own, from the document alone,
so the reading doesn't shape it. The close-reading session uses it as written
and doesn't change it. It keeps the file name `claims_reference.md`, since a
legislative text's claims are its provisions.

It lists, each with where it is:

- **Definitions:** every defined term, with its definition.
- **Findings and purpose:** every statement of findings, intent, or purpose.
- **Requirements:** every "shall" or "must", with who must act.
- **Prohibitions:** everything the document forbids.
- **Permissions:** every "may", "should", or encouragement.
- **Authority:** every duty or power given to a body, such as a state agency,
  a board, a district, or an outside organization.
- **Criteria and lists:** every standard, list, or set of components the
  document sets, and whether the list is open or closed.
- **Consequences:** every consequence or accountability measure, such as
  retention, reporting, intervention, or notification.
- **Exceptions:** every exemption, waiver, or exception.
- **Funding and timing:** every appropriation, deadline, and effective date.
- **Named sources:** every other law, organization, report, or body of
  research the document names or cites.
- **Amendments:** where the document marks amended text, what it adds and
  what it strikes.

Say where the document ends for this purpose: the operative text only, or
fiscal notes, summaries, and appendices too.

The list is an inventory of what the document contains, not a judgment of
what matters most. Where the list and the document disagree, the document
decides.

## Judging the run

Score the close reading against the document on A1–A5, or the discourse
analysis on B1–B5, as your session says.

For A1, sample 30 provisions, drawn at random with a seed you record, or take
every provision if the reading has fewer. Score each sampled provision with
its support items.

Write, in this order: the document's file name, the seed, each criterion's
score or counts with the evidence for it, and a short paragraph on the
reading's main strengths and weaknesses, written for the researcher deciding
whether to accept it.

---

## A. Close reading

### A1. Attribution fidelity

Scored per sampled provision and per support item, against the passage the
step's `location` points to. You find the passage yourself; where you can't,
say so rather than scoring 0.

- **2** — the passage supports it, and the `verbatim` or `paraphrased` marker
  is honest: `verbatim` is the document's exact wording.
- **1** — supported but altered: a "shall" recorded as a "may" or the
  reverse, an open list recorded as closed or the reverse, a condition, grade
  range, or date dropped.
- **0** — the passage doesn't support it, a `verbatim` text isn't the
  document's wording, the duty is assigned to the wrong body, struck-through
  text is recorded as a provision, or the model's own inference is recorded
  as the document's provision.

Report the share of provisions at each score, never a mean. A 1 and a 0 stay
apart on purpose: a weakened provision is a fixable reading and an invented
one isn't.

### A2. Coverage

Counted against `claims_reference.md`, not scored. For each type in the
reference list, report how many were caught, caught without their content (a
definition named but not given), and missed. Name what was missed. Say where
the reading stops if it stops before the document does.

Where the reading records a provision that the list left out, and you confirm
it in the document, note it as found beyond the list. The list itself stays
as it is.

### A3. Strength of language

The document-level pattern behind A1's 1s.

- **2** — modal force (shall, must, may, should), open and closed lists,
  conditions, who must act, grades, and dates survive wherever the document
  attached them.
- **1** — inconsistent: some kept, some stripped or shifted.
- **0** — systematically shifted in one direction: the reading makes the
  document more binding than it is, or less.

### A4. Mechanical checks

Pass and fail counts, not a score:

- verbatim texts found in the document's text
- numbers found in the document's text: section numbers, grades, ages, dates,
  and amounts
- citations matching the document as printed: other laws and named
  organizations or reports

Check these against the document's extracted text, with a tool where you can.
Report readings of tables or other elements printed as images separately: a
value read off an image is correctly `paraphrased` and won't appear in the
extracted text, so check it against the image by eye and don't count it as a
failure.

### A5. Detail and readability

Described, not scored: the number of steps, how evenly they cover the
document's sections, and whether a reader could follow what the document does
from the reading alone. Length isn't merit. A longer reading that repeats
itself or pads a step is worse than a shorter one that covers the same ground.

---

## B. Discourse analysis

Judged against the document alone, using `CODEBOOK.md` for what each
dimension and code means. You are judging whether each observation is
grounded in the document, not whether its interpretation is the one you would
give: the reading is the researcher's to weigh.

### B1. Grounding

Scored per observation.

- **2** — the passage is at the location given, quoted exactly, and shows
  what the observation says it shows.
- **1** — the passage is there and relevant, but the quotation is altered or
  the reading claims more than the passage carries.
- **0** — the passage isn't in the document, isn't the document's wording,
  is struck-through text, or doesn't show what the observation says.

Report the share of observations at each score, per dimension and overall.

### B2. Silencing

For each absence the analysis claims: is the topic actually absent from the
passage it cites, and from the rest of the document? Count confirmed and not
confirmed, and name each one not confirmed with where the topic appears.

### B3. Codes

Counted, not scored: observations whose code fits as the codebook defines it,
observations whose code doesn't fit (name the better code, or "no code
fits"), and observations marked "no code fits". The last are reported for the
researcher, as they may show where the codebook needs a code.

### B4. Errors

Every statement about the document that the document doesn't bear out: a
provision misdescribed, a section misnumbered, a fact about another state or
the research literature presented as if the document said it. Name each.

### B5. Coverage

Described, not scored: the number of observations in each dimension, any
dimension left thin with or without a reason, and anything in the document you
think a dimension should have caught. Say that the last is your own reading.

---

## Not judged

Persuasiveness, effectiveness, clarity of prose, and tone, of the reading or
of the legislation. Agreement on these is poor even among trained annotators,
so a score would be noise that gets quoted as if it meant something.
