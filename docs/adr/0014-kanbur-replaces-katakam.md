# ADR-0014 — Kanbur replaces katakam as the third experiment article

- **Status:** Accepted
- **Date:** 2026-10-19
- **Landed in:** not yet committed

## Context

[ADR-0009](0009-phase-1-matrix-three-configurations-three-articles.md) cut the
experiment from four articles to three, keeping
`katakam_et_al_2027_desalination_systems_data_center_water_needs` and dropping
`kanbur_et_al_2020_desalination_integrated_data_center_cooling`. The two cover
the same subject, desalination for data-center water, and katakam was chosen
as the more recent.

That choice left two of the three articles in the same journal. Katakam
(`10.1016/j.watres.2026.126748`) and Barnett (`10.1016/j.watres.2026.125866`)
are both in Elsevier's *Water Research*. Kanbur (`10.1002/er.5677`) is in
Wiley's *International Journal of Energy Research*. Nothing had yet run on
katakam: only Barnett had been prepared and analyzed.

## Decision

**The experiment articles are Barnett, kanbur, and lei.** Kanbur takes
katakam's place; the 2 × 3 matrix of ADR-0009 is unchanged.

| Article | Journal | Pages |
| --- | --- | --- |
| `barnett_itzhaki_2026_water_footprint_artificial_intelligence` | *Water Research* (Elsevier) | 7 |
| `kanbur_et_al_2020_desalination_integrated_data_center_cooling` | *International Journal of Energy Research* (Wiley) | 18 |
| `lei_et_al_2025_water_use_data_center_workloads` | *Resources, Conservation and Recycling* (Elsevier) | 60 |

Kanbur's PDF moves into `data/research/ab_testing/` and katakam's back to
`data/research/`, with both `pdf:` paths updated in `sources.yaml`. Kanbur
already has an owner-confirmed entry there. Katakam stays in the research
collection.

## Alternatives considered

- **Keep katakam.** More recent, and the same subject, but two of three
  articles from one journal narrows what the experiment can say about
  analyzing a collection drawn from many venues.
- **Replace lei or Barnett instead.** Either loses one end of the page-count
  range the experiment depends on for the PDF arm's cost.

## Consequences

**Three journals, and two kinds of paper.** Barnett is a review and policy
argument; kanbur builds its argument from its own thermoeconomic and
thermodynamic modeling, so the close reading and the argument evaluation meet
a paper whose evidence is its own calculations.

**The page spread holds.** Kanbur is 18 pages against katakam's 20, so
Barnett at 7 and lei at 60 remain the cheap and stress cases for the PDF arm.

**The subject is older.** Kanbur is from 2020; katakam from 2026. The
experiment compares configurations, not the state of the field, so recency is
not what it measures.

**Nothing is rerun.** No analysis of katakam existed.

## Notes

Supersedes ADR-0009's choice of article only. ADR-0009's matrix, its
configurations, and the reasons for them stand.
