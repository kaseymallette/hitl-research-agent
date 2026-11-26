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

   Answered from the article alone. <One or two sentences on what kind of
   article it is and what it is about.>

   ## 1. How is the science of reading defined, and how is it enacted?

   **Short answer.** <A few sentences.>

   - **p. <printed page>.** "<the authors' exact words>"
     *Interpretation:* <your reading of what it shows about the question>

   ## 2. How is teachers' knowledge positioned?

   …

   ## 3. How are students positioned?

   …
   ```

   - Every point is a quotation: the article's exact words, copied character
     for character, in quotation marks. Do not paraphrase, summarize, shorten
     with ellipses, or correct the wording; a word broken across a line with a
     hyphen may be rejoined. Quote the shortest stretch that makes the point,
     usually one to three sentences.
   - Give every quotation the article's printed page. Where a page has no
     printed number, give the PDF page and say so.
   - The quotation is the article; the *Interpretation* line is your reading.
     Keep your words out of the quotation.
   - Say whose view a quotation is: the authors' own, or one the authors
     report, endorse, or dispute.
   - Content read from a figure, chart, or table printed as an image has no
     words to quote: describe it, name the element ("Table 2 shows…"), and say
     it is your description.
   - Where the article says little or nothing about a question, say so in the
     short answer, and quote what it does say, however little.

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
