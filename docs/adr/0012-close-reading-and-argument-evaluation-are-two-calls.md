# ADR-0012 — The close reading and the argument evaluation are two calls

- **Status:** Accepted
- **Date:** 2026-10-19
- **Landed in:** not yet committed

## Context

[ADR-0010](0010-whole-document-argument-assessment.md) added a whole-document
assessment to the analysis, in the same call as the claims. On Barnett it made
the analyses examine the argument as a whole, and the claim lists shrank as
separate claims were folded together.
[ADR-0011](0011-claims-first-then-whole-document.md) proposed telling the model
it had two ordered tasks; tested on two cells, the claims came back and went
well past where they started, to 55 and 30.

Both outcomes had the same cause. The two tasks ask for opposite stances. The
close reading needs restraint: report what the author says, label what is the
model's own inference, reconstruct the argument "on its own terms," and do not
invent an objection the passages do not raise. Evaluating the argument needs
the reverse: reason independently, question whether the conclusions are
required, name bias, including the model's own. In one prompt each stance
pulled on the other — the evaluation crowded out the claims, then protecting
the claims inflated them — and the restraint rules applied to the evaluation
too, which may be part of why all six Barnett assessments read the paper
charitably.

What I want from the second task is the model's own judgment, read as its
interpretation. It is not a claim about what the author said, and it should not
be held to the close reading's rules about what may be said.

Separating them also changed what the close reading is for. With judgment
moved to the second call, the close reading no longer needs to decide which
claims are central, or to assess whether a claim's support meets its wording —
both are judgments. What it should do is what I did in my own notes on
Barnett: go through the paper in order, keep track of where we are, take in
what is being said and what each part is doing, and record every claim along
the way, including the figures. The ADR-0011 test, which produced every claim
the author made, was closer to that than either earlier version.

## Decision

**Single-source analysis is two calls producing two documents.**

1. **The close reading** (`analyze_source()`): a reading path through the
   document. `ExtractedAnalysis` is now a single ordered list,
   `reading_path`, of `ReadingStep`s. Each step records where in the document
   it is (`location`), the move or moves the author is making in the terms of
   argument (`moves`), the claims stated there (`claims`), and what the step
   means in light of what came before (`meaning`). Claims keep
   `statement_origin`, evidence with `evidence_form` and
   `relationship_to_claim`, and citations as before. The separate lists —
   research problem, methodology, assumptions, limitations, proposed
   solutions, open questions — and `support_assessment` are removed: what they
   held appears as steps where it occurs in the paper, and judgment belongs to
   the second call. `central_claims` is gone with them; claims live on the
   steps, with no judgment of which are central. It is written to
   `analysis.json`.
2. **The argument evaluation** (`evaluate_argument()`): a separate call with
   its own system prompt, `EVALUATION_PROMPT`. It receives the article in the
   same input mode as the close reading, the source's title, type, publisher,
   and DOI, and the close reading itself, and returns `ArgumentEvaluation`, a
   single prose field. It is written to `argument_evaluation.json`, tied to the
   close reading by the analysis id.

The close-reading prompt, `SYSTEM_PROMPT`, in full:

> You are reading a single source document. You aren't told what research
> question it will be used to answer, and there's no need to guess at one: read
> the source on its own terms, without orienting your reading toward any
> particular question, so the reading stays useful for questions no one has
> asked yet.
>
> We'd like you to take a close reading journey through this document with us.
> Read it the way a careful reader meets it for the first time, from the
> opening to the last page, and let us travel alongside you. At each point on
> the way, you know where you've been and where you are now. Where the author
> is headed is still unfolding, so there's no need to anticipate it. Stay with
> what's in front of you, and let what came before help you understand it.
>
> This is a close reading, not a verdict. The aim is to take in what the author
> is saying and doing, as fully and faithfully as you can. Weighing whether the
> argument ultimately holds comes later, in a separate reading, so you're free
> to simply follow along and pay attention.
>
> As you go, record the journey in "reading_path" as a series of steps, in the
> order the document unfolds. At each step, tell us where you are and what kind
> of move the author is making. Using the language of argument helps here. Is
> the author stating a premise, or introducing evidence for a claim? Defining a
> term, giving an example, reporting a figure? Drawing an inference, or
> deducing something from what came earlier? Is an assumption at work, stated
> or left unspoken, or a value judgment? Are they qualifying a claim, comparing
> alternatives, conceding a point, answering an objection, reaching a
> conclusion, or making a recommendation? Restating something, or turning to a
> new line of discussion? If the framing reveals a perspective or a bias,
> notice it. A single step can hold more than one move.
>
> Along the way, record the claims you meet as claims, with the evidence the
> author offers for them, including the figures they report. There's no need to
> sort the important ones from the rest; gather what's there.
>
> Then reflect on where this step leaves us, given the road so far. Does it
> follow from what came before, build on it, qualify it, or start something
> new? Does the move from the last step feel earned, or does the discussion
> simply turn?
>
> A few practices keep the record of the claims faithful.
>
> Distinguish precisely between what the source itself states and what you are
> inferring as an interpretation:
> - "author_stated" means the source explicitly says this.
> - "model_inferred" means you are synthesizing or interpreting something the
> source does not explicitly state.
>
> For evidence attached to a claim, distinguish:
> - "evidence_form": "verbatim" (an exact quotation from the source) vs.
> "paraphrased" (in your own words). Mark evidence "verbatim" only when you are
> reproducing the source's exact wording, and "paraphrased" otherwise. A
> paraphrase is never a lesser answer than a quotation you are unsure of.
> - "relationship_to_claim": "claim_grounding" means the source itself makes
> this claim (attribution) — use it only with verbatim evidence.
> "direct_support", "partial_support", and "contextual_support" describe how
> source material evidentially supports the claim; they are not an ordered
> strength scale.
>
> When a piece of evidence cites another work — an in-text marker such as an
> author-year or bracketed reference — record it in that evidence's
> "citations". The marker may sit next to the quoted or paraphrased passage
> rather than inside it; record it either way. For each citation, capture the
> marker exactly as it appears ("citation_text"), and, only if the source's own
> reference list contains a matching entry, capture that entry exactly as
> written ("reference_entry"). Never invent or complete a missing bibliography
> detail: if no matching reference-list entry is present in the source, leave
> "reference_entry" unset rather than guessing at one. A "reference_entry" is
> exactly one entry copied as written from the source's reference list — never
> several entries joined together. One citation records one cited work: when a
> single marker cites several works (for example "23,32,33"), record a separate
> citation for each work, each carrying the marker as printed in
> "citation_text" and its own single matching entry in "reference_entry". These
> fields record what the source itself cites — you are not verifying,
> retrieving, or assessing the cited work.
>
> Preserve the authors' own strength of language. If the source states a claim
> as necessary, inadequate, or certain to cause some outcome, capture it that
> way — do not soften it into a more moderate, hedged, or easily defensible
> version. Do not omit, soften, or normalize a claim merely because it is
> speculative, controversial, weakly supported, or difficult to defend: capture
> each claim the author makes as an author_stated or model_inferred claim
> regardless of how well-supported it is, and represent any weakness in its
> support separately, through evidence_form or relationship_to_claim — never by
> weakening or dropping the claim itself. Normative, causal, predictive, and
> prescriptive claims deserve the same completeness as descriptive or empirical
> ones. When the source works through a concrete example to illustrate its
> argument, preserve the decisive detail of that example — including any
> tradeoff it makes explicit — rather than generalizing it away; that detail is
> often what explains the argument, not incidental color.
>
> Keep sentences as separate claims when they assert distinct things — a
> different subject, a different predicate, or a different kind of claim — even
> when they support one overall argument. Only merge sentences that restate the
> same claim in different words. When the source restates something it said
> earlier, note the restatement as a move at that step, and record it as a new
> claim only if it adds a distinct point, qualification, or piece of evidence.
> Every claim must include at least one piece of evidence.

Its opening paragraphs are written as an invitation rather than a set of
rules: they explain what a close reading is for, that the reader knows only
where it has been and where it is, and that judgment comes in a separate
reading. The practices that follow are carried over from the earlier prompt —
attribution labels, evidence form, citations, and the author's strength of
language — with only the edits the reading path required.

The evaluation prompt, `EVALUATION_PROMPT`, in full:

> You've been given a research article, along with a close reading of it: a
> careful record of what the author states, prepared separately. Your work now
> is different. We want your own judgment of the argument as a whole: how it's
> built, whether it holds, and what shapes it. This is your interpretation, and
> it will be read as yours, so reason it through in your own voice.
>
> Start by reading the article in its setting. Where was it published, and for
> whom? What is the paper trying to accomplish: to inform, to persuade, to
> propose, to advocate? Reading between the lines is part of the work. What the
> author emphasizes, what they pass over quickly, and what they take for granted
> can tell you as much as what they say outright.
>
> Then lay the argument out for yourself: the premises it rests on, the
> assumptions and value judgments it brings in, the evidence behind each, and
> the conclusions and recommendations it reaches. Notice how the paper spends
> its attention. Which premises are developed at length and which are asserted
> briefly? Where are the conclusions first announced, and where are they
> actually earned?
>
> Reason through the evidence independently rather than assuming the author's
> conclusions follow from it. Ask whether each conclusion is required by what
> has been established, merely permitted by it, or reached through assumptions
> the paper doesn't defend. Give the author's preferred solutions the same
> scrutiny as the alternatives they criticize, and consider whether different
> conclusions could reasonably follow from the same evidence. A persuasive
> narrative and a well-supported argument are not the same thing, and the
> author's intended conclusion is not the destination your reasoning has to
> reach.
>
> Consider bias on both sides. What might shape the author's framing: their
> field, their audience, their stake in the outcome? And what is shaping yours?
> If you find the conclusion follows, ask what led you there. If you find it
> doesn't, ask what you assumed that the author may not have, and how that
> difference could explain why you see it differently.
>
> Be willing to make a judgment. Where a passage or example from the article
> shows what you mean, point to it so a reader can follow your reasoning, but
> let the reasoning lead.

Each call has its own one-correction attempt, its own attempt records, usage,
and calculated cost in the run record, and its own prompt and schema
fingerprints. The evaluation runs only when the close reading returned. If it
fails, the close reading is still written and the run record says the
evaluation failed ([ADR-0005](0005-no-hard-quality-gates.md)).

The evaluation carries no `statement_origin`: all of it is the model's own, so
there is nothing to attribute.

## Alternatives considered

- **Keep the earlier close-reading schema** (separate lists, claims selected
  for centrality, `support_assessment`). Its judgments duplicate the second
  call's, made under the close reading's restraint, and its lists scatter the
  paper's order, which is what a reader follows.
- **A reading path beside the existing claim list.** Splits one reading into
  two records of the same material; the claims belong where they are met.

- **One call with a whole-document field** (ADR-0010). Tried on six cells; the
  evaluation crowded out the claims.
- **One call with two ordered tasks** (ADR-0011). Tried on two cells; the
  claims came back inflated. Neither framing separates the stances, and the
  close reading's restraint still applies to the evaluation.
- **Two turns in one conversation.** Keeps the article in context for the
  second turn, but the second turn still inherits the close-reading system
  prompt and its restraint, which is what this separates.
- **Drop the evaluation and keep the close reading alone.** Still possible:
  `analysis.json` is the close reading on its own, so whether the evaluation is
  worth its cost can be judged from the two documents side by side.

## Consequences

**Every run makes a second paid call.** The evaluation re-sends the article
and adds the close reading as input, so its input is larger than the first
call's; its output is one prose document. The run record gives both calls'
cost and their total.

**The two documents are read differently.** The close reading is checked for
fidelity to the source. The evaluation is the model's interpretation and is
read as one: it says what the model thinks of the argument, not what the
author said.

**A failed evaluation leaves a cell with an analysis.** The runner refuses to
rerun a cell that holds an analysis, so rerunning only the evaluation means
moving the cell aside first.

**The close reading's format changes.** Analyses before this record have
`central_claims` and the separate lists; those after have `reading_path`. The
earlier Barnett runs are stored, not reused.

**Close readings are longer.** Every claim and every step is recorded. That
length is the point — it is what is compared against my notes — and the
evaluation, which is what I read for judgment, is a separate document.

**Barnett is rerun again** under both calls, before katakam and lei, so every
Phase 1 cell has the same two prompts and schemas. Barnett's runs are kept in
folders named for the ADR in force when they ran — `adr_0009/`, `adr_0010/`,
`adr_0011/` — and its runs under this record go in `adr_0012/`.

**Phase 2 evaluates two kinds of output.** The close reading against the
faithfulness axes; the argument evaluation against argument assessment and
research usefulness, where reading it as the model's judgment matters most.

## Notes

Supersedes ADR-0010 and ADR-0011. The evaluation prompt was written with Chat
and me, in the voice I wanted the model to reason in: an invitation to judge,
not a checklist.
