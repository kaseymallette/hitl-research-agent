# Discourse analysis of a scholarly article — instructions for an agent run

DRAFT for review. Use these instructions to analyze one scholarly article on
the five CDA dimensions, in a fresh session that has not seen the close
reading being written. They adapt `prompts/legislation/discourse-analysis.md`
to scholarly articles.

## What you're given

- **The article:** `article.pdf` in the workspace, with its extracted text in
  `article.txt` (marked by page) and an image of each page in `pages/`.
  Figures, tables, and equations printed as images appear only in the page
  images.
- **Its source details:** `source.yaml` in the workspace.
- **The close reading:** `run/analysis.json`, a faithful record of what the
  article says, step by step. Use it to find your way; quote from the article
  itself.
- **The codebook:** `CODEBOOK.md`, for the five dimensions and their codes.
  Its codes were written for state legislation, and it has no examples yet.

## What to write

1. **`discourse_analysis.md`** in `run/`: your analysis, as described below,
   and nothing else.
2. **A section headed `## Discourse analysis`** added to `run/run_note.md`,
   saying in a few sentences how you read the PDF and the model and reasoning
   effort you ran at, if you know them.

Open only `article.pdf`, `article.txt`, `pages/`, `source.yaml`,
`run/analysis.json`, and `CODEBOOK.md`.

## The prompt

```text
You're analyzing one scholarly article using critical discourse analysis. The close reading recorded what the article says; your work now is to read how it says it. Work on the five dimensions in CODEBOOK.md:

- LEX — Lexical choices and definitional framing: how the science of reading, and reading itself, are named, bounded, and defined.
- PRE — Presuppositions: what the article takes for granted, especially in how it frames the problem, states its rationale, and draws implications.
- FOS — Foregrounding and silencing: what the article centres, and what it leaves out where it defines or lists what the science of reading, reading instruction, or its evidence includes.
- SUB — Subject positioning: how teachers, students, parents, researchers, schools, and policymakers are constructed.
- INT — Intertextuality: which research, traditions, frameworks, reports, policies, or organizations the article cites, builds on, contests, or invokes.

The codebook's codes were written for legislation. Apply a code where the article's passage shows what the code's definition describes; where an observation matters and no code describes it, say "no code fits".

Write one section per dimension. In each, record what you find as observations. Each observation gives:

- **Where:** the section heading and page, as the article prints them.
- **Passage:** the article's exact words, in quotation marks. Quote only what the article prints as text, not your reading of a figure or table. Where the passage is the article quoting another author, say so.
- **Code:** the codebook code that fits, with a qualifier if one applies, or "no code fits" if the observation matters but no code describes it.
- **Reading:** a few sentences on what the passage does discursively, and why it matters.
- **Certain or uncertain:** say "uncertain" when the passage could reasonably be read another way, and give the other reading.

For silencing, an absence counts only where the article defines or lists the area the topic belongs to. Quote that passage, name what is missing from it, and say what the passage addresses instead. Where a topic you might expect to be silenced is present, record it as a counter-example.

Stay with this article. Don't bring in facts about the works it cites, other research, or legislation unless the article itself states them; what the article does is the evidence. Whether its research is sound is not part of this analysis. Where a dimension has little to observe, say so in a sentence rather than stretching. You don't need to record everything: choose the observations that matter most in each dimension and develop them.
```
