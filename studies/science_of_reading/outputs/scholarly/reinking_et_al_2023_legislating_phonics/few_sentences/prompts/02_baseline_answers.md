# Baseline answers (Method A) — instructions for an agent run

Use these instructions to answer the study's three questions from one
article, the second call of the scholarly harness: Method A, the baseline.
You answer from the article alone. `scripts/run_scholarly.py` runs
them in a folder of their own.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`.

Open only the files named here. Work from the article: don't look up the
works it cites or check its claims against outside sources.

## The three questions

1. **How is the science of reading defined, and how is it enacted?**
2. **How is teachers' knowledge positioned?**
3. **How are students positioned?**

Read the whole article, beginning to end, including the abstract, notes,
tables, and figure captions, before you answer.

## What to write

1. **`02_baseline_answers.md`**, in this shape:

   ```markdown
   # <short citation>: baseline answers

   <full citation, from the article and source.yaml>

   Answered from the article alone. <What kind of article it is and what
   it is about.>

   ## 1. How is the science of reading defined, and how is it enacted?

   ### <A key point, in your own words>

   - **p. <printed page> · <whose view>.** "<the authors' exact words>"

   ### <The next key point>

   …

   ## 2. How is teachers' knowledge positioned?

   …

   ## 3. How are students positioned?

   …
   ```

   - Build each answer from key points: the points someone who knows the
     article would need to make to answer the question fully. Give each key
     point a heading in your own words, and put under it every quotation from
     the article that is evidence for it.
   - Keep each answer to a few sentences: a few key points, each with the
     quotations that are its evidence.
   - Don't interpret the evidence: no interpretation lines or commentary on
     what a quotation shows. The heading says what the key point is; the
     quotations under it show where the article says it. Every entry under a
     heading is a quotation: the article's exact words, copied character for
     character, in quotation marks. Do not paraphrase, summarize, shorten with
     ellipses, or correct the wording; a word broken across a line with a
     hyphen may be rejoined.
   - Give every quotation the article's printed page. Where a page has no
     printed number, give the PDF page and say so.
   - Label whose view each quotation is: the authors' own, or one the authors
     report, endorse, or dispute.
   - Content read from a figure, chart, or table printed as an image has no
     words to quote: describe it, name the element ("Table 2 shows…"), and say
     it is your description.
   - Where the article says little or nothing about a question, say so, and
     quote what it does say, however little.

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
