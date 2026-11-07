# Legislation workspace

DRAFT for review. The workspace for one legislative text: a close reading, a
discourse analysis on the five CDA dimensions, and a judgment of each.
`scripts/workspace.py load` builds it from `evaluations/` with the legislation
files in place of the article ones.

```
README.md                    this file: the Codex prompts
RUBRIC.md                    the legislation rubric
CODEBOOK.md                  the five CDA dimensions and their codes
source.yaml                  the document's details
scores.md                    the scores, filled in by prompts 3 and 5
prompts/
  close-reading.md
  discourse-analysis.md
article.pdf                  the legislative text
article.txt                  its text, marked by page
pages/                       an image of each page
run/                         analysis.json (prompt 1), discourse_analysis.md (prompt 4), run_note.md
references/                  claims_reference.md, from prompt 2
judgments/                   close_reading.md (prompt 3), discourse_analysis.md (prompt 5)
```

## For each document

1. `uv run python scripts/workspace.py load <slug>`
2. For the pilot, code the document yourself before opening
   `run/discourse_analysis.md`, so the two codings stay independent.
3. Run prompts 1–5 in order, each in a new Codex session, on GPT-6.1 Sol at
   medium effort. Skim the provisions list against the document before
   prompt 3: the judge uses it as written.
4. Add the **Accepted:** lines to `scores.md` once you decide.
5. `uv run python scripts/workspace.py save`

---

## 1. Close reading

```
Follow prompts/close-reading.md. The document is article.pdf, and its source
details are in source.yaml. Write analysis.json and run_note.md to run/.
```

## 2. Provisions reference

```
Hi! You're writing a reference list for judging a close reading of a
legislative text. Please start by reading RUBRIC.md, which explains the
setup, and especially its section "The provisions reference list".

This session reads the document (article.pdf, with its text in article.txt and an image of each page in pages/) on its own and writes the document's
provisions to references/claims_reference.md, as the rubric describes. A
later session judges the close reading against your list as written, so take
care that it's complete.

Please open only RUBRIC.md, article.pdf, article.txt, and pages/. Don't open anything in run/,
prompts/, or judgments/.
```

## 3. Evaluate close reading

```
Hi! You're judging a close reading of a legislative text. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the reading followed.

Read the document (article.pdf, with its text in article.txt and an image of each page in pages/) and references/claims_reference.md, the reference list an
earlier session wrote from the document. Use it as written; don't change it.

Then open run/analysis.json and judge it against the document and the list
on A1–A5. Write the judgment to judgments/close_reading.md.

Then add your scores to scores.md in the close reading table. Leave the
Accepted line for me.

Please open only these files and scores.md. Don't read
run/discourse_analysis.md or anything in judgments/.
```

## 4. Discourse analysis

```
Follow prompts/discourse-analysis.md. The document is article.pdf, its source
details are in source.yaml, the close reading is run/analysis.json, and the
codebook is CODEBOOK.md. Write discourse_analysis.md to run/ and add your
section to run/run_note.md.
```

## 5. Evaluate discourse analysis

```
Hi! You're judging a discourse analysis of a legislative text. Please start
by reading RUBRIC.md, which explains the setup and the criteria,
prompts/discourse-analysis.md, which holds the instructions the analysis
followed, and CODEBOOK.md.

Read the document (article.pdf, with its text in article.txt and an image of each page in pages/), then open run/discourse_analysis.md and judge it against
the document on B1–B5. Write the judgment to judgments/discourse_analysis.md.

Then add your scores to scores.md in the discourse analysis table. Leave the
Accepted line for me.

Please open only these files and scores.md. Don't read run/analysis.json,
references/claims_reference.md, or anything in judgments/.
```
