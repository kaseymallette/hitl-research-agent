# Discourse analysis of legislation — instructions for an agent run

DRAFT for review. Use these instructions to analyze one legislative text on
the five CDA dimensions, in a fresh session that has not seen the close
reading being written.

## What you're given

- **The text:** `article.pdf` in the workspace, with its extracted text in
  `article.txt` (marked by page) and an image of each page in `pages/`. The
  extracted text doesn't show underlining or strikethrough, so check the page
  images wherever the document marks amended text.
- **Its source details:** `source.yaml` in the workspace.
- **The close reading:** `run/analysis.json`, a faithful record of what the
  document says, section by section. Use it to find your way; quote from the
  document itself.
- **The codebook:** `CODEBOOK.md`, for the five dimensions and their codes.
  Its coded excerpts are unverified examples from other states: they show how
  a code is applied, not what this document says.

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
You're analyzing one legislative document using critical discourse analysis. The close reading recorded what the document says; your work now is to read how it says it. Work on the five dimensions in CODEBOOK.md:

- LEX — Lexical choices and definitional framing: how the science of reading, and reading itself, are named, bounded, and defined.
- PRE — Presuppositions: what the document takes for granted, especially in findings, intent, and purpose language.
- FOS — Foregrounding and silencing: what the document centres, and what it leaves out where it defines or lists what instruction, preparation, or materials must include.
- SUB — Subject positioning: how teachers, students, parents, districts, publishers, and the state are constructed.
- INT — Intertextuality: which laws, frameworks, reports, research, organizations, or other states the document cites, adopts, or invokes.

Write one section per dimension. In each, record what you find as observations. Each observation gives:

- **Where:** the section and subsection, as the document numbers them.
- **Passage:** the document's exact words, in quotation marks. Quote only what the document prints; if you are reading amended text, quote it as it reads after the change, never struck-through words.
- **Code:** the codebook code that fits, with a qualifier if one applies, or "no code fits" if the observation matters but no code describes it.
- **Reading:** a few sentences on what the passage does discursively, and why it matters.
- **Certain or uncertain:** say "uncertain" when the passage could reasonably be read another way, and give the other reading.

For silencing, an absence counts only where the document defines or lists the area the topic belongs to. Quote that passage, name what is missing from it, and say what the passage addresses instead. Where a topic you might expect to be silenced is present, record it as a counter-example.

Stay with this document. Don't bring in facts about other states, outcomes, or the research literature unless the document itself names them; what the document does is the evidence. Where a dimension has little to observe, say so in a sentence rather than stretching. You don't need to record everything: choose the observations that matter most in each dimension and develop them.
```
