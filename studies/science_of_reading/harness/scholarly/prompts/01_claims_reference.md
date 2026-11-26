# Claims reference — instructions for an agent run

Use these instructions to list every claim in one article, the first call of
the scholarly harness. The list is the answer key: a later session scores two
sets of answers against it, so it must be complete. You work from the article
alone and aren't told the questions, so the list favors neither set.
`scripts/run_scholarly.py` runs them in a folder of their own.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`.

Open only the files named here. Work from the article: don't look up the
works it cites or check its claims against outside sources.

## What to list

Read the whole article, beginning to end, including the abstract, notes,
tables, and figure captions. List **every claim** the article makes, in the
order they appear: every claim in the abstract, every claim in the body, the
conclusion of every section and subsection, the article's overall
conclusions, and every claim in the notes. Don't decide which claims matter;
list them all.

For each claim:

- **The quotation:** the article's exact words, copied character for
  character. Do not paraphrase, summarize, shorten with ellipses, or correct
  the wording; a word broken across a line with a hyphen may be rejoined.
  Quote the shortest stretch that states the claim on its own, usually one to
  three sentences.
- **Page:** the printed page, or the PDF page where there is no printed
  number, saying which.
- **Voice:** `author` (the authors' own view), `attributed` (another source's
  view the authors report), `endorsing` (another source's view the authors
  adopt), or `disputing` (another source's view the authors reject or
  qualify).
- **Whose words:** for a `disputing` claim, say in plain words whose view
  the quotation states: the other side's view, which is not the authors'
  ("not the authors' view: <whose view>"); the authors' own words arguing
  against or reporting it ("the authors' own words, arguing against <whom>");
  or the authors' words quoting the other side directly (say which words are
  the other side's).
- **Evidence:** the evidence the authors give for it, quoted exactly the same
  way, with its citation as printed. Leave it out where the claim is simply
  asserted.

A figure or table printed as an image has no words to quote: give it an entry
that names it and describes what it shows ("Figure 2 shows…"), marked as your
description.

## What to write

1. **`01_claims_reference.md`**, with the article's citation, then one
   numbered entry per claim (**R1**, **R2**, …) in this shape:

   ```markdown
   **R12** · p. 116 · author
   > "<the article's exact words>"

   Evidence: "<the article's exact words>" (<citation as printed>)
   ```

   A `disputing` entry adds its whose-words line after the voice:

   ```markdown
   **R30** · p. 106 · disputing · whose words: not the authors' view: <whose view>
   ```

   End with the number of claims listed and where the list stops (the main
   text only, or the notes too).

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
