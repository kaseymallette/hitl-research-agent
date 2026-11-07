# Close reading of legislation — instructions for an agent run

DRAFT for review. Use these instructions to write the close reading of one
legislative text: an enacted statute, a bill, a state board rule, or an
executive order. They adapt `prompts/close-reading.md` to legislation and
keep its output format, so the reading has the same shape as a reading of an
article.

## What you're given

- **The text:** `article.pdf` in the workspace, with its extracted text in
  `article.txt` (marked by page) and an image of each page in `pages/`. You
  don't need PDF tools of your own. The extracted text doesn't show
  underlining or strikethrough, so check the page images wherever the
  document marks amended text.
- **Its source details:** `source.yaml` in the workspace. Use its
  `source_title` and `source_type` in the header below.
- **Where to write:** `run/` in the workspace.

## What to write

1. **`analysis.json`** in `run/`: only the JSON described at the end of the
   prompt below, with nothing before or after it.
2. **`run_note.md`** in `run/`, with a section headed `## Close reading`
   saying, in a few sentences:
   - **how you read the PDF** — for example, whether you viewed its pages as
     images, extracted its text with a tool (name it), or both, and whether
     you could see formatting such as struck-through or underlined text;
   - the model and reasoning effort you ran at, if you know them.

Open only `article.pdf`, `article.txt`, `pages/`, and `source.yaml`.

## The prompt

Treat everything below as the instructions for the reading itself.

```text
Source title: <source_title>
Source type: <source_type>

The complete original PDF of this source is in the workspace, with its extracted text and an image of each page. There are no preparation annotations in this input.

Mark as "verbatim" only wording that literally appears in the document's own text. Content you read from a table, chart, or other element rendered as an image is not quotable text: record it as "paraphrased", and name the element it came from in the text itself, for example "The table in section 4 lists…". Describe what the element shows without presenting your reading of it as the source's printed words, and say so plainly where a value is unclear rather than estimating it.

---

You are reading a single legislative document: a statute, a bill, a rule, or an executive order. You aren't told what research question it will be used to answer, and there's no need to guess at one: read the document on its own terms, without orienting your reading toward any particular question, so the reading stays useful for questions no one has asked yet.

We'd like you to take a close reading journey through this document with us. Read it the way a careful reader meets it for the first time, from the opening to the last page, and let us travel alongside you. At each point on the way, you know where you've been and where you are now. Stay with what's in front of you, and let what came before help you understand it.

This is a close reading, not a verdict. The aim is to take in what the document says and does, as fully and faithfully as you can. Whether it is good policy, or whether it represents any body of research accurately, is not part of this reading.

As you go, record the journey in "reading_path" as a series of steps, in the order the document unfolds. At each step, tell us where you are, by section and subsection as the document numbers them, and what the document is doing there. Legislative language has its own moves. Is it stating findings or a purpose? Defining a term? Requiring something (shall, must), prohibiting something, or permitting or encouraging it (may, should)? Assigning a duty or authority to someone: a state agency, a board, a district, a teacher, an outside organization? Setting criteria, a list, or a standard? Funding something, setting a deadline or an effective date, or attaching a consequence such as retention, reporting, or intervention? Creating an exception or a waiver? Amending, repealing, or cross-referencing other law? If the framing reveals a perspective or a bias, notice it. A single step can hold more than one move.

Before you set out, take a first look through the whole document to get a feel for it: what kind of legislative text it is (an enacted statute, a bill and its stage, a rule, an executive order, guidance), how it is organized, and how densely it reads. Record this first look briefly in "reading_plan", with the pace you'll take.

Let the document's own divisions set your pace. A step usually takes in one section or subsection. Where a section is long, split it at its subsections; where several short provisions do one thing together, they can be a single step. Legislative text is dense, so a step will rarely cover more than about a page.

Along the way, record the document's provisions in "claims": each definition, finding, requirement, prohibition, permission, assignment of authority, criterion, deadline, and consequence. There's no need to sort the important ones from the rest; gather what's there.

When the document offers a basis for a provision (a finding, a stated purpose, research or a report it names, an organization's standard it adopts), record that as the provision's support. A provision the document simply enacts needs no support listed; record it as it stands.

Then reflect on where this step leaves us, given the road so far. Does it build on what came before, carry it out, qualify it, or start something new?

A few practices keep the record faithful.

Record each provision in the document's own words where you can, and mark it "verbatim" only when it reproduces the exact wording; otherwise mark it "paraphrased". A faithful paraphrase is never a lesser answer than a quotation you are unsure of.

Preserve the document's strength of language. "Shall" and "must" are not "may" or "should"; "is prohibited" is not "is discouraged". Keep who is required to act, the conditions attached, the grades or ages covered, and the dates. A list introduced by "including" is open; a list introduced by "limited to" or given without qualification is closed. Keep that difference.

Where the document marks amended text, such as struck-through words for deletions and underlined or capitalized words for additions, record the language as it reads after the change, and note in "moves" that the provision changes existing law. Never record struck-through text as the document's provision. If you cannot tell whether text is struck through, say so.

When a provision cites other law or an outside source (another section of code, a federal act, a named organization, a report), record the citation exactly as printed in "citation_text". Legislative texts rarely have a reference list, so "reference_entry" is null unless the document itself prints a full entry for the cited work. Never invent or complete a citation.

Keep distinct provisions separate, and merge only sentences that say the same thing. When the document repeats a provision, note the repetition as a move at that step rather than recording it again.

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
