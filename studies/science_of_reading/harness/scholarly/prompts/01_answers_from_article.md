# The three questions, from the article alone — instructions for an agent run

Use these instructions to answer the study's three questions from one
article, the first call of the scholarly harness. You answer from the article
alone, before any close reading of it exists. `scripts/run_scholarly.py` runs
them in a folder of their own.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`.

Open only the files named here. Work from the article: don't look up the
works it cites or check its claims against outside sources.

## The three questions

1. **How is the science of reading defined?**
2. **How is teachers' knowledge positioned?**
3. **How are students positioned?**

Read the whole article, beginning to end, including the abstract, notes,
tables, and figure captions, before you answer.

## What to write

1. **`01_answers_from_article.md`**, in this shape:

   ```markdown
   # <short citation>: the three questions, from the article

   <full citation, from the article and source.yaml>

   Answered from the article alone. <One or two sentences on what kind of
   article it is and what it is about.>

   ## 1. How is the science of reading defined?

   **Short answer.** <A few sentences.>

   - **p. <printed page>.** <What the article says.>
     *Interpretation:* <your reading of what it shows about the question>

   ## 2. How is teachers' knowledge positioned?

   …

   ## 3. How are students positioned?

   …
   ```

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

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
