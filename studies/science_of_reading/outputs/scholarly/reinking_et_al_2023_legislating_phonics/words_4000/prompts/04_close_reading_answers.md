# Close Reading answers (Method B) — instructions for an agent run

Use these instructions to answer the study's three questions from one article
and its close reading, the fourth call of the scholarly harness: Method B,
answering with the close reading.
`scripts/run_scholarly.py` runs them in a folder of their own.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`.
- **Its close reading:** `03_close_reading.json`, a reading of the article
  from start to finish. `reading_path` is a list of steps in the article's
  order; each step has a `location`, the author's `moves`, the author's
  `claims` (each marked `verbatim` or `paraphrased`, with its `support`), and
  the reading's `meaning`. Claims and support are the author's; moves and
  meaning are the close reading's.

Open only the files named here. Work from the article: don't look up the
works it cites or check its claims against outside sources.

## The three questions

1. **How is the science of reading defined, and how is it enacted?**
2. **How is teachers' knowledge positioned?**
3. **How are students positioned?**

Use the close reading to find what bears on each question, then check each
point against the article on its page. The article decides: where the close
reading and the article disagree, answer from the article.

## What to write

1. **`04_close_reading_answers.md`**, in this shape:

   ```markdown
   # <short citation>: Close Reading answers

   <full citation, from the article and source.yaml>

   Answered from the article and its close reading (`03_close_reading.json`).
   Every quotation gives the article's printed page and the close reading
   claim it comes from (**CR 35.2** = step 35, claim 2). <What kind of
   article it is and what it is about.>

   ## 1. How is the science of reading defined, and how is it enacted?

   ### <A key point, in your own words>

   - **p. <printed page> · CR <step>.<claim> · <whose view>.** "<the authors' exact words>"

   ### <The next key point>

   …

   ## 2. How is teachers' knowledge positioned?

   …

   ## 3. How are students positioned?

   …
   ```

   - Number steps and claims from 1, in the order they appear in the close
     reading. Where a quotation is not a claim in the close reading, say where
     it is instead ("CR 5, moves only") or that it is not recorded.
   - Give every quotation the article's printed page (or pages). Where a page
     has no printed number, give the PDF page and say so.
   - Label whose view each quotation is: the authors' own, or one the authors
     report, endorse, or dispute. When the authors characterize the other
     side, label it as their characterization.
   - Build each answer from key points: the points someone who knows the
     article would need to make to answer the question fully. Give each key
     point a heading in your own words, and put under it every quotation from
     the article that is evidence for it.
   - Keep the whole answer, all three questions together, under 4,000 words:
     key points, each with the quotations that are its evidence.
   - Don't interpret the evidence: no interpretation lines or commentary on
     what a quotation shows. The heading says what the key point is; the
     quotations under it show where the article says it. Every entry under a
     heading is a quotation: the article's exact words, copied character for
     character, in quotation marks. Do not paraphrase, summarize, shorten with
     ellipses, or correct the wording. Where the close reading's text is not
     the article's exact wording, quote the article, not the close reading.
   - Content read from a figure, chart, or table printed as an image has no
     words to quote: describe it, name the element ("Table 2 shows…"), and say
     it is your description.
   - Where the article says little or nothing about a question, say so, and
     quote what it does say, however little.

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
