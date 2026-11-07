# Katakam: scores

## Close reading by revision

Each column is one judgment of the close reading, in `judgments/`, against the
same `references/claims_reference.md`.

| | Original | Revised 1 | Revised 2 |
| --- | --- | --- | --- |
| A1 claims supported as recorded | 73% | 83% | 93% |
| A1 support items | 100% | 92% | 91% |
| A2 missed or partial | 6 | 7 | 0 |
| A3 strength of language | 1/2 | 1/2 | 1/2 |
| A4 failures | 0 | 0 | 0 |

| Column | Judgment | Version judged |
| --- | --- | --- |
| Original | `close_reading.md` | `analysis.json`, the model's original (107 claims, 1 verbatim) |
| Revised 1 | `close_reading_revised.md` | `analysis_revised.json`: 8 softened or reworded claims restored to the author's wording, 3 missed items added and 3 partial ones completed (113 claims, 6 verbatim) |
| Revised 2 | `close_reading_revised_2.md` | the same, with 5 more softened claims restored, H4, contribution C2 and the §1 gap added, the conclusions recorded in full, the model's notes moved from claim and support fields into `meaning`, and three inferred citation matches set to null (122 claims, 12 verbatim) |

All three samples use seed 20261107, over 107, 113 and 122 claims, so each is a
different set. Revised 1's A2 counts a different set of items from the
original's: H4, CO1 and CO5 missed, and C2, S1.7, CO4 and CO8 partial. The
first judge had accepted CO1 and CO5 as restatements.

Revised 2's A3 of 1 is for a few shifts in both directions: "will extend"
became "could extend" (C5.8), "often" was added (C4.3), "enables
identification" became "identifies" (C5.7, from Revised 1), "suggests … would
be negligible" became "infer … are negligible" (C21.2), and the prose's 7.2
"severe water stress threshold" was recast as Case 1's average (C22.3).

**Accepted:** `analysis_revised.json`, as judged in `close_reading_revised_2.md`.

## Argument evaluation by revision

Each column is one judgment of the argument evaluation, in `judgments/`, against
the article alone.

| | Original |
| --- | --- |
| B1 premise acceptability | 2/2 |
| B2 relevance of critique | 2/2 |
| B3 sufficiency | 2/2 |
| B4 unstated warrants and missing qualifiers | 2/2 |
| B5 self-attribution | 2/2 |
| B6 problems raised, confirmed | 11/11 |
| B6 errors | 0 |

| Column | Judgment | Version judged |
| --- | --- | --- |
| Original | `evaluation.md` | `argument_evaluation.md`, the model's original |

**Accepted:** `argument_evaluation.md`, as judged in `evaluation.md`.
