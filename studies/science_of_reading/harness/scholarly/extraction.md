# Extraction of one scholarly article — instructions for an agent run

DRAFT, version 0. Use these instructions to extract passages from one
scholarly article in the workspace, for the extraction protocol in
`docs/EXTRACTION_PROTOCOL.md`. This is not coding: no codes, no
interpretation of the passage beyond saying why it answers the question.

## What you're given

- **The article:** `article.pdf`, with its extracted text in `article.txt`
  (marked by page) and an image of each page in `pages/`.
- **Its source details:** `source.yaml`.
- **Where to write:** `run/extractions.csv` and a section headed
  `## Extraction` in `run/run_note.md`.

Open only `article.pdf`, `article.txt`, `pages/`, and `source.yaml`.

## The four questions

Read the whole article, beginning to end, including the abstract, notes,
tables, and figure captions. Extract every passage that answers one of
these questions:

1. **Definition.** How does the article explicitly or implicitly
   conceptualize the science of reading? Include passages that define the
   term, say what it includes or excludes, say what kind of thing it is (a
   body of research, a method, a movement, a set of practices), or use it in
   a way that shows what the authors take it to mean, even without defining
   it.
2. **Knowledge claims.** What claims does the article make about reading,
   reading development, and reading instruction?
3. **Evidence.** What evidence supports those claims, and what
   qualifications or limitations accompany them? Include the studies,
   data, reviews, or reasoning offered, and every hedge, limit, or
   counter-consideration attached to a claim.
4. **Operationalization.** What implications, recommendations, or
   expectations for instructional practice are articulated? Include what
   teachers, schools, teacher preparation, curricula, or policy should or
   should not do, and how the science of reading is said to be (or not be)
   put into practice.

A passage can answer more than one question; give it one row per question
it answers. When in doubt whether a passage is relevant, include it and say
why in `note`. Missing a relevant passage is worse than including a
marginal one.

## What a passage is

- **The passage** is the shortest stretch of the article's own words that
  answers the question on its own: usually one to three sentences. Copy it
  exactly as printed, character for character, except that a word broken
  across a line with a hyphen is rejoined. Do not paraphrase, shorten with
  ellipses, or correct it.
- **Location:** the PDF page (`pdf_page`, counting the PDF's pages from 1),
  the page number printed on it (`printed_page`), and the nearest section
  heading above it (`section`), as printed.
- **Context:** the sentence immediately before (`context_before`) and
  immediately after (`context_after`), copied exactly. Leave one empty if
  the passage starts or ends a section.
- **Voice:** who makes the claim.
  - `author`: the article's authors assert it in their own voice.
  - `attributed`: the authors report it as another scholar's or source's
    claim, view, or finding (with a citation, a name, or "researchers have
    argued…"), without adopting it.
  - `author_endorsing`: the authors assert it themselves and support it with
    a citation.
  - `author_disputing`: the authors report someone else's claim in order to
    reject or qualify it.
- **Attributed to:** for any voice other than `author`, the citations or
  names exactly as printed in or next to the passage (for example
  `Gough & Tunmer, 1986`), separated by `; `. Empty for `author`.
- **Relates to:** for an evidence row, the `id` of the knowledge-claim or
  operationalization row it supports or qualifies. Empty otherwise.
- **Note:** one short sentence on why the passage answers the question.

Content read only from a figure, chart, or table printed as an image is not
quotable text. If it answers a question, put your description in `passage`,
start it with `[Figure 2]` or `[Table 1]`, and say so in `note`.

## The file

`run/extractions.csv`: UTF-8, comma-separated, every field in double
quotes, with this header row and one row per passage per question, in the
order the passages appear in the article:

```
id,question,passage,pdf_page,printed_page,section,context_before,context_after,voice,attributed_to,relates_to,note
```

- `id`: `P001`, `P002`, … in order. A passage answering two questions keeps
  one id per row (`P014`, `P015`).
- `question`: `definition`, `knowledge_claim`, `evidence`, or
  `operationalization`.

In `run/run_note.md`, under `## Extraction`, say in a few sentences how you
read the PDF (text, page images, or both), the number of rows per question,
any part of the article you could not read, and the model and reasoning
effort you ran at, if you know them.
