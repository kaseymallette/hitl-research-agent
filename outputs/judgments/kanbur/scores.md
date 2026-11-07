# Kanbur: scores

The original judgments come from the Phase 2 A/B testing, Experiment 1, where
this run (Codex, GPT-6.1 Sol medium) was run B. They used
`docs/AB_TESTING_RUBRIC.md`, with the problems list, so B6 below counts the
list's problems the evaluation found, not the problems it raised. The revised
close reading was judged with `docs/RUBRIC.md`.

## Close reading by revision

Each column is one judgment of the close reading, in `judgments/`, against
`references/claims_reference.md`.

| | Original | Revised 1 |
| --- | --- | --- |
| A1 claims supported as recorded | 97% | 100% |
| A1 support items | 95% | 100% |
| A2 missed or partial | 5 | 0 |
| A3 strength of language | 1/2 | 2/2 |
| A4 failures | 0 | 0 |

| Column | Judgment | Version judged |
| --- | --- | --- |
| Original | `close_reading.md` | `analysis.json`, the model's original (151 claims) |
| Revised 1 | `close_reading_revised.md` | `analysis_revised.json`: 5 missed or partly caught items added, 8 softened or misattributed wordings restored, Figure 3 read for what it shows, three of the model's notes moved out of claim and support fields; 10 claims verbatim (160 claims) |

The original's sample uses seed 20261026 over 151 claims and the revision's
seed 20261107 over 160, so they are different sets. The original's A2 counts the abstract claims
missed (AB1, AB6) and the items caught with a loss (AB10, conclusion C-5.6,
Figure 3); the judgment also notes smaller losses in four section conclusions
and in contribution (b). No claim or support item in the original is verbatim.

**Accepted:** `analysis_revised.json`, as judged in `close_reading_revised.md`.

## Argument evaluation by revision

Each column is one judgment of the argument evaluation, in `judgments/`. The
original was judged against the article and `references/problems_reference.md`
under the A/B testing rubric; Revised 1 against the article alone under
`docs/RUBRIC.md`, like the other articles.

| | Original | Revised 1 |
| --- | --- | --- |
| B1 premise acceptability | 2/2 | 2/2 |
| B2 relevance of critique | 2/2 | 1/2 |
| B3 sufficiency | 2/2 | 2/2 |
| B4 unstated warrants and missing qualifiers | 2/2 | 2/2 |
| B5 self-attribution | 2/2 | 2/2 |
| B6 problems | 8 of the list's 23 found (3 more partly) | 13/13 raised, confirmed |
| B6 errors | 0 (1 minor imprecision) | 0 |

| Column | Judgment | Version judged |
| --- | --- | --- |
| Original | `evaluation.md` | `argument_evaluation.md`, the model's original |
| Revised 1 | `evaluation_revised.md` | `argument_evaluation_revised.md`: the fouling sentence corrected (fouling is a modeling assumption, not listed future work) |

Revised 1's B2 of 1 is for two criticisms aimed wider than the article: that
the sustainability index gives no evidence about environmental impacts, which
the article never claims it does, and the contrast with "an unconditional
engineering optimum", where the article already makes the optimum depend on
the decision-maker and on low loads. The text the judge cites is unchanged from
the original; the old rubric didn't score it down.

**Accepted:** `argument_evaluation_revised.md`, as judged in `evaluation_revised.md`.
