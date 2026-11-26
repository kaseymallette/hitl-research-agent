# Close reading — instructions for an agent run

Use these instructions to write the close reading of one article, the third
call of the scholarly harness, and the first step of Method B. `scripts/run_scholarly.py` runs them in a
folder of their own.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`. Use its `source_title` and
  `source_type` in the header below.

## What to write

1. **`03_close_reading.json`**: only the JSON described at the end of the
   prompt below, with nothing before or after it.
2. **Your final message**, saying in a few sentences:
   - **how you read the PDF** — for example, whether you viewed its pages as
     images, extracted its text with a tool (name it), or both, and whether
     you could see its figures, tables, and equations as they appear on the
     page;
   - the model and reasoning effort you ran at, if you know them.

Open only the files named here.

## The prompt

Treat everything below as the instructions for the reading itself.

```text
Source title: <source_title>
Source type: <source_type>

The complete original PDF of this source is attached. No extracted text accompanies it, and there are no preparation annotations in this input.

Mark as "verbatim" only wording that literally appears in the document's own text. Content you read from a figure, chart, diagram, or an equation rendered as an image is not quotable text: record it as "paraphrased", and name the element it came from in the text itself, for example "Figure 2 shows…" or "Table 1 lists…". Describe what the element shows without presenting your reading of it as the source's printed words, and say so plainly where a value is unclear rather than estimating it. Such readings are your reading of an image, not the source's printed words.

---

You are reading a single source document for three research questions:

1. How is the science of reading defined, and how is it enacted?
2. How is teachers' knowledge positioned?
3. How are students positioned?

The close reading is only about these questions. Read the whole document, but record only the passages, claims, and evidence that bear on one of them.

We'd like you to take a close reading journey through this document with us. Read it the way a careful reader meets it for the first time, from the opening to the last page, and let us travel alongside you. At each point on the way, you know where you've been and where you are now. Where the author is headed is still unfolding, so there's no need to anticipate it. Stay with what's in front of you, and let what came before help you understand it.

This is a close reading, not a verdict. The aim is to take in what the author says about the three questions, faithfully. Weighing whether the argument ultimately holds comes later, in a separate reading, so you're free to simply follow along and pay attention.

As you go, record each passage that bears on the three questions as a step in "reading_path", in the order the document unfolds. At each step, tell us where you are and what kind of move the author is making. Using the language of argument helps here. Is the author stating a premise, or introducing evidence for a claim? Defining a term, giving an example, reporting a figure? Drawing an inference, or deducing something from what came earlier? Is an assumption at work, stated or left unspoken, or a value judgment? Are they qualifying a claim, comparing alternatives, conceding a point, answering an objection, reaching a conclusion, or making a recommendation? Restating something, or turning to a new line of discussion? If the framing reveals a perspective or a bias, notice it. A single step can hold more than one move.

Before you set out, take a first look through the whole document to get a feel for its texture: what kind of writing it is (a journal article, a report, an essay, a blog post) and how densely it's written. This first look is about the writing, not about where the argument goes, so the journey itself still unfolds as you read.

Let that texture set your pace. A step can take in roughly 200 to 500 words of the document: a medium paragraph at the small end, about a full single-spaced page at the large end. Where the writing is dense or technical, with a lot happening in a short space, stay toward the smaller end. Where it moves more easily, a longer stretch can be a single step. These are a sense of scale, not counts. Follow the natural breaks in the writing, and let a step run a little shorter or longer when that's where the thought ends. Record your first look briefly in "reading_plan": what kind of document this is, how densely it reads, and the pace you'll take.

Along the way, record the claims that bear on the three questions, with the evidence the author offers for them, including the figures they report. Leave out claims that don't bear on any of the three questions. Where a stretch of the document has nothing relevant to the questions, skip it: it gets no step. Every step in the reading is about the three questions.

Then reflect on where this step leaves us, given the road so far. Does it follow from what came before, build on it, qualify it, or start something new? Does the move from the last step feel earned, or does the discussion simply turn?

A few practices keep the record of the claims faithful.

Record each claim as a quotation: the author's exact words, copied character for character from the document, marked "verbatim". Do not paraphrase, summarize, shorten with ellipses, or correct the wording; a word broken across a line with a hyphen may be rejoined. Quote the shortest stretch that states the claim on its own, usually one to three sentences. The only text marked "paraphrased" is your reading of a figure, chart, diagram, or an equation rendered as an image, as described above.

When the author offers something in support of a claim (a figure, a study, an example), record it as that claim's support, quoted the same way: the author's exact words, marked "verbatim". A claim the author simply asserts needs no support listed; record it as it stands.

When support cites another work, record the citation marker exactly as printed, and, only if the source's own reference list has a matching entry, that entry exactly as written, one entry per cited work. Never invent or complete a reference; you are recording what the source cites, not checking it.

Preserve the author's strength of language. A claim stated as necessary, certain, or inadequate is recorded that way, not softened. Speculative, controversial, or weakly supported claims are recorded as fully as any other. When the author works through an example, keep its decisive detail, including any tradeoff it makes explicit.

Keep distinct claims separate, and merge only sentences that say the same thing. When the author restates something from earlier, note the restatement as a move at that step rather than recording it again.

---

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
