# ADR-0010 — Every analysis carries a whole-document argument assessment

- **Status:** Superseded by [ADR-0012](0012-close-reading-and-argument-evaluation-are-two-calls.md)
- **Date:** 2026-10-18
- **Landed in:** `1e0f20d`

## Context

The first Phase 1 article, `barnett_itzhaki_2026_water_footprint_artificial_intelligence`,
was analyzed in all six configurations and compared against my own notes,
written before I saw any analysis. The six analyses reconstructed the
methodology and the central claims accurately and invented no numbers. None of
them made the critique I found most important: that the paper's real thesis —
the policy and justification argument — is announced in the abstract but
developed only at the end, after a long technical section that serves mostly as
setup, and that the abstract names semiconductor manufacturing as one of three
water pathways the body never analyzes.

That was not a lapse by the models. The prompt asked for assessment only one
claim at a time: `support_assessment` judges whether the reasons offered for a
single claim meet that claim's own wording. Nothing asked how the conclusions
follow across claims and sections, what premises they need, or how the
document's organization develops them, and the schema had no field for a
judgment about the document as a whole. The prompt's instruction to reconstruct
the argument "on its own terms" and not to "invent an objection the passages
you found do not themselves raise" pushed further against a critique tied to
no single passage.

That level is the one I most need. What I want from an analysis is a map of the
paper before I read it — where the argument is, what carries it, what it rests
on — and a claim-by-claim reading cannot provide it.

## Decision

**`ExtractedAnalysis` gains one required field, `argument_assessment`: a prose,
passage-grounded assessment of the document as a whole, always the model's own
judgment.** It is the last field, so the model writes it after reconstructing
the claims it assesses. `SYSTEM_PROMPT` gains two paragraphs directing it:

> In "argument_assessment", assess the document as a whole. Assess the
> reasoning connecting the source's central findings to its main conclusions
> and recommendations, even when those connections span multiple claims or
> sections. Identify the premises needed for those conclusions to follow,
> including any value judgments. Explain which premises the source supports,
> which it states without support, and which remain implicit. Distinguish
> whether a recommendation is justified from whether its implementation is
> adequately specified. Always assess this central reasoning; keep assessments
> of secondary claims selective.
>
> Examine how the document's organization supports its reasoning. Distinguish
> where its main conclusions are announced, where the supporting arguments are
> developed, and where the conclusions are restated, and describe how much of
> the document each part occupies. Assess whether that development adequately
> supports the conclusions and whether the body delivers the scope promised by
> the abstract and introduction. Identify substantive gaps with specific
> passages; do not treat section placement or length alone as evidence of
> weakness.

The field carries no `statement_origin`. Like `support_assessment`, it is the
model's assessment by definition, so there is nothing to attribute.

## Alternatives considered

- **Leave the prompt alone and record the gap as a Phase 2 finding.** Keeps
  Phase 1's prompt untouched, but defers the fix until after the collection's
  configuration is chosen, and Phase 2 would then evaluate a prompt Phase 3
  does not use.
- **Prompt text only, with the critique landing in existing fields.** Without a
  field of its own, a whole-document judgment scatters across
  `support_assessment`, `assumptions`, and `limitations` — roughly what the
  Barnett analyses already did — and `limitations` reads as limitations of the
  study, not of its argument.
- **A structured field** (separate lists of premises, gaps, sections).
  Premature: one article does not show which structure the assessment needs,
  and prose is what I read.
- **The reasoning paragraph alone.** It covers the chain from findings to
  conclusions, including the value judgments the Barnett framework rests on,
  but not organization or promised scope — half of the critique that prompted
  this.
- **Organization without describing proportion**, judging it only. With the
  guard against treating length as weakness, a model would most likely say
  nothing about proportion at all. Describing how much of the document each
  part occupies is the map; the guard keeps that description from becoming a
  verdict on its own.

## Consequences

**The prompt and schema change before Phase 1 is complete.** Only Barnett has
run. Its six analyses predate this record, and their run records carry the old
prompt and schema fingerprints; Barnett is rerun under this prompt so that all
18 Phase 1 cells share one prompt and schema. The runner refuses a cell that
already holds an analysis, so the earlier cells must be moved or deleted first.

**This is not a quality gate.** The field is required in the schema in the same
way `research_problem` is: a response missing it does not fit the schema and
gets the one correction attempt. A thin, wrong, or overcritical assessment is
still an analysis and is returned as one
([ADR-0005](0005-no-hard-quality-gates.md)).

**Outputs get longer and cost more.** By how much is unmeasured until the
rerun.

**It rests on one article.** The change is worded as general questions — how
the conclusions follow, what they rest on, how the document develops them —
not as a search for the specific flaw Barnett has. Whether it generalizes is
for katakam and lei, and my notes on them, to show; this is the kind of change
the README warns can accumulate one step at a time.

**Phase 2 has something new to evaluate.** The argument-reconstruction and
argument-assessment axes now have a whole-document judgment to score, and it is
the field most at risk of reading as the judge's or the model's taste.

## Notes

Recorded on the day the decision was made, after Barnett's first six cells and
before any other Phase 1 cell ran. Both paragraphs of the prompt text were
drafted with Chat; the second was revised to describe proportion as well as
judge development.

Superseded by ADR-0012, which moves the whole-document assessment out of the
close reading into a separate call.
