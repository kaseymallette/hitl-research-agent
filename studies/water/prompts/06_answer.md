# Answer — instructions for an agent run

Use these instructions to answer one of the water experiment's research
questions from retrieved material, in a fresh session. The same prompt is used
for both approaches (original documents and structured analyses);
only the retrieved items differ. `scripts/answer.py` runs it in a folder of its
own.

## What you're given

- **`retrieved.md`**: the question, the list of sources, and the retrieved
  items.

## What to write

1. **`answer.md`**: your answer, as Markdown, and nothing else.
2. **Your final message**, saying in a sentence or two the model and
   reasoning effort you ran at, if you know them.

Open only `retrieved.md`. Don't run other commands or look for other files.

## The prompt

Treat everything below as the instructions for the answer itself.

```text
You've been given a research question and material retrieved from a collection of articles on the water use of AI and data centers. Answer the question from this material alone, the way a researcher would in a section of a paper: explain, compare, and weigh what the articles show, rather than listing it.

The material comes as numbered items, [E1], [E2], and so on. Each names the article it comes from and what kind of item it is:

- Article text: a passage from the article itself. This is what the article says.
- Close reading: a step-by-step reconstruction of part of the article's argument, prepared separately by a model: what the article claims, how it supports each claim, and what it cites. It is a reading of the article, not the article's own words.
- Claims reference: an inventory of the article's claims, paraphrased by a model.
- Argument evaluation: a model's judgment of the article's argument, such as whether its evidence supports its conclusions. It is the evaluator's view, not the article's position.

You may be given any mix of these kinds. Credit what an article claims to that article, whether you learned it from its text, its close reading, or its claims reference. When you draw on an argument evaluation, present it as an assessment of the article, never as something the article says.

Cite every claim you take from the material with the items it rests on, in brackets after the claim: [E3], or [E3, E7]. Name the articles in your prose by author and year, from the list of sources. Don't cite an item for something it doesn't say.

Use only this material. Don't add facts, figures, or sources from your own knowledge. Where the material is thin, conflicting, or silent on part of the question, say so rather than filling the gap: what the collection does not establish is part of the answer. Where the articles disagree, set out the disagreement and, if the material shows it, what explains it.

Write prose, with headings only where they help. Usually 600 to 1,000 words is enough.
```
