# ADR-0009 — Phase 1 runs three model configurations over three articles

- **Status:** Accepted for Barnett (Experiment 1); its choice of katakam is superseded by [ADR-0014](0014-kanbur-replaces-katakam.md), and its matrix for the other articles by [ADR-0015](0015-phase-1-as-three-experiments.md)
- **Date:** 2026-10-17
- **Landed in:** `eaa3114`

## Context

[ADR-0008](0008-compare-pdf-against-prepared-text.md) set Phase 1 as a 2 × 2
over four articles: full PDF against prepared text plus crops, crossed with
GPT-6.1 Sol at medium effort and GPT-6 Astra at low effort, for 16 analyses.

Before any cell ran, I asked whether the comparison should include Sol at high
effort as well. The two configurations in the 2 × 2 differ in two things at
once, the model and the reasoning effort. If Astra low produced better analyses
than Sol medium, the experiment could not say whether Astra is the better model
or Sol was simply given too little reasoning. The question Phase 2 has to
answer is which configuration to analyze the collection with, and Sol at a
higher effort is a candidate the 2 × 2 never tested: possibly as good as Astra,
at Sol's rates, which are a fifth of Astra's ($2.00/$10.00 against
$10.00/$50.00 per MTok input/output).

Adding a third configuration across four articles would have meant 24
analyses. ADR-0008 had kept the experiment to four articles because that was
what the budget and the human scoring effort support, and the binding cost is
the scoring: every analysis is one more the judge scores in Phase 2 and one
more candidate for the human-scored sample.

## Decision

**Phase 1 is a 2 × 3 over three articles: 18 analyses.**

| | GPT-6.1 Sol, medium effort | GPT-6.1 Sol, high effort | GPT-6 Astra, low effort |
| --- | --- | --- | --- |
| **Full PDF** | 3 analyses | 3 analyses | 3 analyses |
| **Extracted text + crops** | 3 analyses | 3 analyses | 3 analyses |

The articles are `barnett_itzhaki_2026_water_footprint_artificial_intelligence`
(7 pages), `katakam_et_al_2027_desalination_systems_data_center_water_needs`
(20 pages), and `lei_et_al_2025_water_use_data_center_workloads` (60 pages).

`kanbur_et_al_2020_desalination_integrated_data_center_cooling` leaves the
experiment. It and `katakam` are both about desalination for data center
water, so the experiment was carrying two articles on one topic, and `katakam`
is the more recent of the two (2027 against 2020). Dropping `kanbur` keeps the
page spread the four were chosen for: `barnett` remains the cheap case for the
PDF arm and `lei` the stress case. Its PDF moves from
`data/research/ab_testing/` to `data/research/`, so the folder holds exactly
the experiment set. It stays in the research collection and is analyzed in
Phase 3 with the chosen configuration.

The third configuration's slug follows the existing pattern:
`pdf__gpt-6.1-sol-high` and `text_crops__gpt-6.1-sol-high`.

Everything else in ADR-0008 stands: the input format is decided by measurement
rather than argument, the criteria that settle it are the ones it states, the
prompt, schema, correction policy, and question-independence are held fixed
across every cell, an article with no crops still runs as a `text_crops` cell,
and `prepare_sources.py` stays frozen until the outcome is recorded.

## Alternatives considered

- **Keep the 2 × 2.** Cheapest, and already specified, but it leaves model and
  effort confounded, so a win for Astra would not distinguish the model from
  the effort setting.
- **Add Sol high across all four articles (24 analyses).** The fullest design,
  at half again the judge cost and half again the analyses competing for the
  human-scored sample, against the limit ADR-0008 named.
- **Add Sol high on the PDF arm only (20 analyses).** Fewer cells, but an
  unbalanced design that cannot see an input-by-effort interaction — the
  interaction ADR-0008 kept the 2 × 2 to observe, since a lower-effort run may
  depend more on clean, well-ordered text.
- **Run the 2 × 2, then Sol high only if Astra wins.** Sol high matters to the
  choice only in that case. But the extra cells would run later, possibly
  against a changed API, and a comparison across run dates is weaker than one
  made together.
- **Drop `barnett` or `lei` instead.** Either loses one end of the page-count
  range, which is where the PDF arm's cost differs most from the text arm's.
- **Drop `katakam` instead of `kanbur`.** Equally good on page count, but keeps
  the older of the two desalination articles.

## Consequences

**Model and effort can be separated within Sol.** Sol medium against Sol high
isolates effort; Sol high against Astra low compares the models with Sol given
more reasoning. The design still cannot separate Astra's model from Astra's
effort, since Astra runs at one setting.

**The run count stays close to the original.** 18 analyses rather than 16, so
the Phase 2 judge cost and the human scoring load change little.

**Sol high's cost is unknown until it runs.** Reasoning tokens are billed at
the output rate, and how many more Sol uses at high effort than at medium has
not been measured. The existing cost projection does not cover it.

**Each cell rests on three articles, not four.** ADR-0008 already called four
articles an initial comparison rather than a conclusion. Three is thinner: one
unusual article moves a cell's result more, and the record of the outcome
should say so.

**The documents that describe the matrix have to follow.** README's A/B
section and roadmap, and BUILD_PLAN's Phase 1 tables, slugs, cost paragraph,
and acceptance criteria, describe the 2 × 2 over four articles, as does the
`pdf:` path for `kanbur` in `data/research/sources.yaml`.

## Notes

Recorded on the day the decision was made, before any Phase 1 cell ran.

Adding Sol high and dropping `kanbur` are recorded together rather than as two
records because they were not independent: the third article was cut to pay
for the third configuration.

This record amends ADR-0008's matrix and does not supersede it. ADR-0008 holds
the input-format question open, and the record that states Phase 1's outcome
supersedes both.

ADR-0014 reverses the choice between katakam and kanbur: katakam shares
Barnett's journal, so kanbur replaces it. The matrix and configurations here
stand.

ADR-0015 keeps this matrix for Barnett only, as Experiment 1, and gives kanbur
and lei experiments of their own.
