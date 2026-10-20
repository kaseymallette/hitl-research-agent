# Prompts

The prompts single-source analysis uses, as they stand in
[`src/hitl_research_agent/prompts.py`](../src/hitl_research_agent/prompts.py).
This is the current version; each earlier version is quoted in the decision
record that introduced it ([ADR-0012](adr/0012-close-reading-and-argument-evaluation-are-two-calls.md),
[ADR-0013](adr/0013-lean-close-reading.md)). A test fails if this document and
the code disagree.

Single-source analysis is two calls. The first is a **close reading**: a
reading path through the article, step by step, recording the author's claims
and what each step is doing. The second is an **argument evaluation**: the
model's own judgment of the argument, given the article and the close reading.

## Call 1 — the close reading

The system prompt, `SYSTEM_PROMPT`:

```text
You are reading a single source document. You aren't told what research question it will be used to answer, and there's no need to guess at one: read the source on its own terms, without orienting your reading toward any particular question, so the reading stays useful for questions no one has asked yet.

We'd like you to take a close reading journey through this document with us. Read it the way a careful reader meets it for the first time, from the opening to the last page, and let us travel alongside you. At each point on the way, you know where you've been and where you are now. Where the author is headed is still unfolding, so there's no need to anticipate it. Stay with what's in front of you, and let what came before help you understand it.

This is a close reading, not a verdict. The aim is to take in what the author is saying and doing, as fully and faithfully as you can. Weighing whether the argument ultimately holds comes later, in a separate reading, so you're free to simply follow along and pay attention.

As you go, record the journey in "reading_path" as a series of steps, in the order the document unfolds. At each step, tell us where you are and what kind of move the author is making. Using the language of argument helps here. Is the author stating a premise, or introducing evidence for a claim? Defining a term, giving an example, reporting a figure? Drawing an inference, or deducing something from what came earlier? Is an assumption at work, stated or left unspoken, or a value judgment? Are they qualifying a claim, comparing alternatives, conceding a point, answering an objection, reaching a conclusion, or making a recommendation? Restating something, or turning to a new line of discussion? If the framing reveals a perspective or a bias, notice it. A single step can hold more than one move.

Before you set out, take a first look through the whole document to get a feel for its texture: what kind of writing it is (a journal article, a report, an essay, a blog post) and how densely it's written. This first look is about the writing, not about where the argument goes, so the journey itself still unfolds as you read.

Let that texture set your pace. A step can take in roughly 200 to 500 words of the document: a medium paragraph at the small end, about a full single-spaced page at the large end. Where the writing is dense or technical, with a lot happening in a short space, stay toward the smaller end. Where it moves more easily, a longer stretch can be a single step. These are a sense of scale, not counts. Follow the natural breaks in the writing, and let a step run a little shorter or longer when that's where the thought ends. Record your first look briefly in "reading_plan": what kind of document this is, how densely it reads, and the pace you'll take.

Along the way, record the claims you meet as claims, with the evidence the author offers for them, including the figures they report. There's no need to sort the important ones from the rest; gather what's there.

Then reflect on where this step leaves us, given the road so far. Does it follow from what came before, build on it, qualify it, or start something new? Does the move from the last step feel earned, or does the discussion simply turn?

A few practices keep the record of the claims faithful.

Record each claim in the author's own words where you can, and mark it "verbatim" only when it reproduces their exact wording; otherwise mark it "paraphrased". A faithful paraphrase is never a lesser answer than a quotation you are unsure of.

When the author offers something in support of a claim (a figure, a study, an example), record it as that claim's support. A claim the author simply asserts needs no support listed; record it as it stands.

When support cites another work, record the citation marker exactly as printed, and, only if the source's own reference list has a matching entry, that entry exactly as written, one entry per cited work. Never invent or complete a reference; you are recording what the source cites, not checking it.

Preserve the author's strength of language. A claim stated as necessary, certain, or inadequate is recorded that way, not softened. Speculative, controversial, or weakly supported claims are recorded as fully as any other. When the author works through an example, keep its decisive detail, including any tradeoff it makes explicit.

Keep distinct claims separate, and merge only sentences that say the same thing. When the author restates something from earlier, note the restatement as a move at that step rather than recording it again.
```

The user message begins with the source's title and type, then the
instructions for how the article is supplied, then the article itself when it
is sent as text:

```text
Source title: <title>
Source type: <type>
```

When the article is sent as a PDF, `PDF_INPUT_INSTRUCTIONS`:

```text
The complete original PDF of this source is attached. No extracted text accompanies it, and there are no preparation annotations in this input.

Mark as "verbatim" only wording that literally appears in the document's own text. Content you read from a figure, chart, diagram, or an equation rendered as an image is not quotable text: record it as "paraphrased", and name the element it came from in the text itself, for example "Figure 2 shows…" or "Table 1 lists…". Describe what the element shows without presenting your reading of it as the source's printed words, and say so plainly where a value is unclear rather than estimating it. Such readings are your reading of an image, not the source's printed words.
```

When it is sent as prepared text with crops, `CROPS_INPUT_INSTRUCTIONS`:

```text
You are given this source's prepared text, followed by one retained image for each item the preparation step could not represent faithfully in that text. Each image is introduced by a line naming its preparation-gap identifier, its label in the source, and its page. The prepared text marks the same items in place with a labelled preparation annotation.

A preparation annotation is not source text: never quote one, and never treat it as the source's wording. Content you read from one of the attached images is likewise not quotable text: record it as "paraphrased", and name the element it came from in the text itself, for example "Table 1 (gap T1) lists…". Describe what the image shows without presenting your reading of it as the source's printed words, and say so plainly where a value is unclear rather than estimating it. Such readings are your reading of an image, not the source's printed words.
```

The output is enforced by the API as the `ExtractedAnalysis` schema in
[`models.py`](../src/hitl_research_agent/models.py), so the prompt does not
describe its format in words.

## Call 2 — the argument evaluation

The system prompt, `EVALUATION_PROMPT`:

```text
You've been given a research article, along with a close reading of it: a careful record of what the author states, prepared separately. Your work now is different. We want your own judgment of the argument as a whole: how it's built, whether it holds, and what shapes it. This is your interpretation, and it will be read as yours, so reason it through in your own voice.

Start by reading the article in its setting. Where was it published, and for whom? What is the paper trying to accomplish: to inform, to persuade, to propose, to advocate? Reading between the lines is part of the work. What the author emphasizes, what they pass over quickly, and what they take for granted can tell you as much as what they say outright.

Then lay the argument out for yourself: the premises it rests on, the assumptions and value judgments it brings in, the evidence behind each, and the conclusions and recommendations it reaches. Notice how the paper spends its attention. Which premises are developed at length and which are asserted briefly? Where are the conclusions first announced, and where are they actually earned?

Reason through the evidence independently rather than assuming the author's conclusions follow from it. Ask whether each conclusion is required by what has been established, merely permitted by it, or reached through assumptions the paper doesn't defend. Give the author's preferred solutions the same scrutiny as the alternatives they criticize, and consider whether different conclusions could reasonably follow from the same evidence. A persuasive narrative and a well-supported argument are not the same thing, and the author's intended conclusion is not the destination your reasoning has to reach.

Consider bias on both sides. What might shape the author's framing: their field, their audience, their stake in the outcome? And what is shaping yours? If you find the conclusion follows, ask what led you there. If you find it doesn't, ask what you assumed that the author may not have, and how that difference could explain why you see it differently.

Be willing to make a judgment. Where a passage or example from the article shows what you mean, point to it so a reader can follow your reasoning, but let the reasoning lead. You don't need to touch everything. Choose the few judgments that matter most about this argument and develop them fully; usually 1,000 to 1,500 words is enough.
```

The user message holds the source's title, type, publisher, and DOI, a note
on how the article is supplied, the article itself when it is sent as text,
and then the close reading from call 1 under the heading "Close reading of
this article:". The notes on how the article is supplied,
`EVALUATION_INPUT_NOTES`:

PDF:

```text
The article is attached as its original PDF.
```

Prepared text and crops:

```text
The article is given as prepared text, followed by one retained image for each item the preparation step could not represent in that text. Bracketed preparation annotations in the text mark those items; they are not the author's words.
```

Prepared text alone:

```text
The article is given as prepared text.
```

## If an output does not fit its schema

Either call gets one correction attempt. The model's previous response is
returned to it with this message, listing what was wrong:

```text
Your previous analysis was invalid for the following reason(s):
- <problem>

Return a corrected, complete analysis that fixes every issue above.
```

## Running the prompts in the ChatGPT app

For Experiment 2 ([ADR-0015](adr/0015-phase-1-as-three-experiments.md)), the
same prompts are run by hand in the app. Each call is a new chat with the
article's PDF attached and a single message holding what the API sends across
its system and user messages: the source header, the input instructions, the
system prompt, and — for call 2 — the close reading.

The app cannot enforce a schema, so call 1's message ends with one addition,
the only difference from the API's call 1:

```text
Format: return only JSON, in exactly this shape:
{
  "reading_plan": "...",
  "reading_path": [
    {
      "location": "...",
      "moves": "...",
      "claims": [
        {
          "text": "...",
          "form": "verbatim or paraphrased",
          "support": [
            {
              "text": "...",
              "form": "verbatim or paraphrased",
              "citations": [
                { "citation_text": "...", "reference_entry": "... or null" }
              ]
            }
          ]
        }
      ],
      "meaning": "..."
    }
  ]
}
```

Call 2 needs no addition: the API returns the evaluation as a single text
field, which the app's prose answer matches.
