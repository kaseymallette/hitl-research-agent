# Design

What the system is and the rules it holds to.

This document is the stable part. The phases that build it are in
[BUILD_PLAN.md](BUILD_PLAN.md), why each file exists is in
[REPOSITORY.md](REPOSITORY.md), and the decisions behind these rules — with the
alternatives they beat and what they cost — are in [adr/](adr/).

A change to this document contradicts a decision record or needs a new one.

---

## The three agents

| Agent | Input | Output | Question-aware? |
| --- | --- | --- | --- |
| **Single-source analysis** | one article | a close reading as structured JSON, and the model's own evaluation of the argument | No — never receives a research question |
| **Synthesis** | several accepted analyses | a cross-source comparison | No |
| **Literature review** | an explicit research question | candidate articles with stated relevance | Yes — this is the only question-aware agent |

Single-source analysis stays question-independent so that an analysis produced
today remains usable for a question asked later, and so that no analysis is
shaped toward a conclusion the researcher is looking for. Synthesis compares
what the sources say to each other, not to a question. Only the literature
review agent reads the research question, and it only proposes; the researcher
selects.

## Workflow contract

```
article + prompt → model → JSON → separate evaluation → accept · reject · revise · rerun
```

Four rules hold across every phase:

1. **Evaluation is separate from production.** Quality assessment never runs
   inside the analysis call and never decides whether the JSON is returned.
2. **No hard quality gates.** Only a technical failure — an API error, an
   unreadable response, output that cannot be parsed into the schema — stops a
   run. A paraphrase instead of a quotation, a claim with no evidence item, a
   thin analysis: these are reported by evaluation and human review, never
   grounds for withholding the result. v1 accumulated such gates and they were
   removed deliberately; they are not to be restored.
3. **Model interpretation stays labelled.** `author_stated` vs.
   `model_inferred` is carried on every claim in the close reading — so what the
   authors state stays separable from what the model reads into them. Evidence
   carries a second, independent split: `verbatim` vs. `paraphrased`. The
   argument evaluation is the model's interpretation throughout and is stored
   as its own document, so it needs no label to be read as one.
4. **The human operates a gate, not a reading chair.** Analysis and evaluation
   end at a four-state decision — **accept, reject, revise, rerun** — and only
   accepted analyses enter the research collection. This is a runtime boundary
   rather than a phase: Phase 2 exercises it on the judge's own output, Phase 3
   on what enters the collection, Phase 4 on syntheses. What the researcher
   needs in front of them to make that decision — the analysis, its citations,
   the evaluation scores, and the evaluation's explanations — is therefore a
   requirement on how analyses and evaluations are stored, not a later
   presentation concern.

## Repository layout

The annotated tree is in [README.md](../README.md#repository-structure), kept in
one place so it cannot drift. Two conventions matter to the design: data folders
are named by role rather than by phase number, so renumbering a phase never
moves source material; and analyses and evaluations are stored separately, so an
analysis is never conflated with the judgment of it and either can be
regenerated without the other.

---

## The analysis data model

An analysis has two layers. `ExtractedAnalysis` is the schema sent to the
model and holds only content the model may supply. `SourceAnalysis` wraps it
with the three things the application owns and a model has no legitimate value
for: `id`, `provenance`, and `analyzed_at`
([ADR-0003](adr/0003-application-owned-fields-stay-out-of-the-model-schema.md)).

Two labels travel with the model's content and are independent of each other.
`statement_origin` (`author_stated` / `model_inferred`) records what the model
asserts about where a statement came from — not that anything has been checked
([ADR-0002](adr/0002-statement-origin-is-an-attribution.md)). `evidence_form`
(`verbatim` / `paraphrased`) describes the form of an evidence text rather than
who is committed to its content. A faithful paraphrase is `author_stated` and
`paraphrased` at once, and is not a weaker answer than a quotation the model
was unsure of.

Single-source analysis is two calls
([ADR-0012](adr/0012-close-reading-and-argument-evaluation-are-two-calls.md)). The first is the
close reading above. The second gives the model the article and that close
reading and asks for its own judgment of the argument: whether the conclusions
follow, what they rest on, and what bias shapes the author's framing and the
model's reading. It is stored as its own document, `ArgumentEvaluation`, tied to
the close reading by its id. It carries no `statement_origin`, because all of it
is the model's interpretation and is read as such.

The types are in `src/hitl_research_agent/models.py`.
[README.md](../README.md#what-an-analysis-records-and-what-needs-checking)
explains what they mean for someone reading an analysis, and
[REPOSITORY.md](REPOSITORY.md) describes the module.

---

## What the system does not do

- **Analysis works from the supplied article.** It records the citations the
  article prints, but does not retrieve the cited works or verify their
  findings. Its assessment of an argument rests on what the article provides.
- **Evaluation never runs inside the analysis call** and never decides whether
  a result is returned. Rules 1 and 2 above are the same statement from two
  directions.
- **The input format is not settled.** Whether the model receives a full PDF
  or prepared text plus crops is decided by the Phase 1 experiment
  ([ADR-0008](adr/0008-compare-pdf-against-prepared-text.md)), and
  `scripts/prepare_sources.py` is frozen until it is.
