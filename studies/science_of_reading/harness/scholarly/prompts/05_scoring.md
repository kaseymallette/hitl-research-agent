# Scoring — instructions for an agent run

Use these instructions to score two sets of answers to the study's three
questions against the article's claims reference, the fifth call of the
scholarly harness. `scripts/run_scholarly.py` runs them in a folder of their
own.

The harness tests whether answering with a close reading gives better answers
than answering from the article alone.

- **Method A, Baseline** (`02_baseline_answers.md`): the questions answered
  from the article alone.
- **Method B, Close Reading** (`04_close_reading_answers.md`): the questions
  answered from the article and a close reading of it.
- **Null hypothesis:** Method B is no better than Method A.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`.
- **The claims reference:** `01_claims_reference.md`, every claim in the
  article, quoted exactly and numbered **R1**, **R2**, …, written from the
  article alone without knowing the questions. A `disputing` entry has a
  "whose words" line saying whether the quotation is the other side's view
  or the authors' own words.
- **The two sets of answers:** `02_baseline_answers.md` and
  `04_close_reading_answers.md`.

Open only the files named here. Work from the article: don't look up the
works it cites or check its claims against outside sources.

## The three questions

1. **How is the science of reading defined, and how is it enacted?**
2. **How is teachers' knowledge positioned?**
3. **How are students positioned?**

## How to score

1. **Relevant claims.** Go through the claims reference and mark each claim
   with the question or questions it bears on, or none. The claims that bear
   on a question are that question's relevant claims. Where you find a
   relevant passage in the article that the reference leaves out, add it,
   quoted exactly with its page, as **R+1**, **R+2**, …, and count it as a
   relevant claim.
2. **Recall.** For each method and each question: of the relevant claims, how
   many does the answer use? List the ones it uses and the ones it misses, by
   R number. A `disputing` claim counts as used only if the answer
   attributes it as its whose-words line does.
3. **Precision.** For each method and each question: go through every
   quotation the answer uses and say whether it is
   - **exact:** the article's exact words, checked against the article's
     text with a tool where you can;
   - **a real claim:** matching a claim in the reference (give its R number);
   - **relevant:** bearing on the question it is used for;
   - **correctly attributed:** where it matches a `disputing` claim, the
     answer says whose view the words are, as the claim's whose-words line
     does. An answer that presents the other side's view as the authors' own
     fails, even though the words are exact.

   A quotation counts toward precision only if it is all four. List every
   quotation that fails, with what is wrong and, where it is inexact, the
   article's actual words.

Score both methods the same way, and report everything you find. Don't leave
anything out because an answer does badly.

## What to write

1. **`05_scoring.md`**, with:
   - the article's citation;
   - the relevant claims for each question, by R number;
   - a table of results:

     | Question | Method | Relevant claims | Used | Recall | Quotations | Exact, real, relevant, attributed | Precision |
     | --- | --- | --- | --- | --- | --- | --- | --- |

     with a row per question per method, and a total row per method;
   - for each method and question, the relevant claims it missed and the
     quotations that failed, each with what is wrong;
   - a short paragraph on whether Method B beat Method A on recall and on
     precision, and whether the null hypothesis stands for this article.

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
