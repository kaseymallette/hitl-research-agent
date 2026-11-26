# The three questions, from the article and its close reading — instructions for an agent run

Use these instructions to answer the study's three questions from one article
and its close reading, the third call of the scholarly harness.
`scripts/run_scholarly.py` runs them in a folder of their own.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`.
- **Its close reading:** `02_close_reading.json`, a reading of the article
  from start to finish. `reading_path` is a list of steps in the article's
  order; each step has a `location`, the author's `moves`, the author's
  `claims` (each marked `verbatim` or `paraphrased`, with its `support`), and
  the reading's `meaning`. Claims and support are the author's; moves and
  meaning are the close reading's.

Open only the files named here. Work from the article: don't look up the
works it cites or check its claims against outside sources.

## The three questions

1. **How is the science of reading defined?**
2. **How is teachers' knowledge positioned?**
3. **How are students positioned?**

Use the close reading to find what bears on each question, then check each
point against the article on its page. The article decides: where the close
reading and the article disagree, answer from the article and say what the
close reading got wrong. Where the article says something relevant that the
close reading does not record, include it and say that the close reading
leaves it out.

## What to write

1. **`03_answers.md`**, in this shape:

   ```markdown
   # <short citation>: the three questions

   <full citation, from the article and source.yaml>

   Answered from the article and its close reading (`02_close_reading.json`).
   Every point gives the article's printed page and the close reading claim it
   comes from (**CR 35.2** = step 35, claim 2). <One or two sentences on what
   kind of article it is and what it is about.>

   ## 1. How is the science of reading defined?

   **Short answer.** <A few sentences.>

   - **p. <printed page> · CR <step>.<claim>.** <What the article says.>
     *Interpretation:* <your reading of what it shows about the question>

   ## 2. How is teachers' knowledge positioned?

   …

   ## 3. How are students positioned?

   …
   ```

   - Number steps and claims from 1, in the order they appear in the close
     reading. Where the close reading marks a claim `verbatim`, write
     `(35.2 verbatim)` after the reference. Where a point is not a claim in
     the close reading, say where it is instead ("CR 5, moves only") or that
     it is not recorded.
   - Give every point the article's printed page (or pages). Where a page has
     no printed number, give the PDF page and say so.
   - Keep what the article says apart from your interpretation of it. The
     point itself reports the article; the *Interpretation* line, where you
     add one, is your reading. Leave it out where the point speaks for itself.
   - Say whose view a point is: the authors' own, or one the authors report,
     endorse, or dispute. When the authors characterize the other side, say
     that it is their characterization.
   - Quote only the article's exact words, in quotation marks with the page.
     Otherwise paraphrase. Content read from a figure, chart, or table printed
     as an image is your reading of it: name the element ("Table 2 shows…").
   - Keep the article's strength of language: don't soften or strengthen it.
   - Where the article says little or nothing about a question, say so in the
     short answer, and give what it does say, however little.
   - End with a section headed `## Where the close reading and the article
     differ`, listing each point the close reading left out, misread, or
     marked `verbatim` when the wording is not the article's. Write "None
     found" if there are none.

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
