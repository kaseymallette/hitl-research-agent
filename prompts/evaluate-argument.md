# Argument evaluation — instructions for an agent run

Use these instructions to write the argument evaluation of one article, the
second call of single-source analysis, in a fresh session that has not seen
the close reading being written. They are the same prompt the API sends,
arranged for an agent such as Codex that reads files and writes its own
output ([ADR-0020](../docs/adr/0020-codex-joins-experiment-2.md)).

## What you're given

- **The article:** the PDF path named in the request.
- **Its source details:** the article's entry in `data/research/sources.yaml`,
  found by the PDF's file name without `.pdf`. Use its `source_title`,
  `source_type`, `publisher`, and `doi` in the header below.
- **The close reading:** `analysis.json` in the output folder named in the
  request.
- **Where to write:** that same output folder.

## What to write

1. **`argument_evaluation.md`** in the output folder: your evaluation, as
   prose, and nothing else.
2. **A section headed `## Argument evaluation`** added to `run_note.md` in the
   same folder, saying in a few sentences how you read the PDF — whether as
   page images, as text extracted with a tool (name it), or both — and the
   model and reasoning effort you ran at, if you know them.

Do not read any other analysis or evaluation of this article in the
repository; read only the close reading named above.

## The prompt

Treat everything below as the instructions for the evaluation itself. Put the
close reading's JSON where it says.

```text
Source title: <source_title>
Source type: <source_type>
Publisher: <publisher>
DOI: <doi>

The article is attached as its original PDF.

---

You've been given a research article, along with a close reading of it: a careful record of what the author states, prepared separately. Your work now is different. We want your own judgment of the argument as a whole: how it's built, whether it holds, and what shapes it. This is your interpretation, and it will be read as yours, so reason it through in your own voice.

Start by reading the article in its setting. Where was it published, and for whom? What is the paper trying to accomplish: to inform, to persuade, to propose, to advocate? Reading between the lines is part of the work. What the author emphasizes, what they pass over quickly, and what they take for granted can tell you as much as what they say outright.

Then lay the argument out for yourself: the premises it rests on, the assumptions and value judgments it brings in, the evidence behind each, and the conclusions and recommendations it reaches. Notice how the paper spends its attention. Which premises are developed at length and which are asserted briefly? Where are the conclusions first announced, and where are they actually earned?

Reason through the evidence independently rather than assuming the author's conclusions follow from it. Ask whether each conclusion is required by what has been established, merely permitted by it, or reached through assumptions the paper doesn't defend. Give the author's preferred solutions the same scrutiny as the alternatives they criticize, and consider whether different conclusions could reasonably follow from the same evidence. A persuasive narrative and a well-supported argument are not the same thing, and the author's intended conclusion is not the destination your reasoning has to reach.

Consider bias on both sides. What might shape the author's framing: their field, their audience, their stake in the outcome? And what is shaping yours? If you find the conclusion follows, ask what led you there. If you find it doesn't, ask what you assumed that the author may not have, and how that difference could explain why you see it differently.

Be willing to make a judgment. Where a passage or example from the article shows what you mean, point to it so a reader can follow your reasoning, but let the reasoning lead. You don't need to touch everything. Choose the few judgments that matter most about this argument and develop them fully; usually 1,000 to 1,500 words is enough.

---

Close reading of this article:

<the contents of analysis.json>
```
