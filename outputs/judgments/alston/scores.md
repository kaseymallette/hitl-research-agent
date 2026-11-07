# Alston: close-reading scores by revision

Each column is one judgment of the close reading, in `judgments/`, against the
same `references/claims_reference.md`.

| | Original | Revised 1 | Revised 2 |
| --- | --- | --- | --- |
| A1 claims supported as recorded | 93% | 93% | 97% |
| A1 support items | 96% | 94% | 100% |
| A2 missed or partial | 8 | 1 | 0 |
| A3 strength of language | 1/2 | 2/2 | 2/2 |
| A4 failures | 0 | 0 | 0 |

| Column | Judgment | Version judged |
| --- | --- | --- |
| Original | `close_reading.md` | `analysis.json`, the model's original (110 claims) |
| Revised 1 | `close_reading_revised.md` | `analysis_revised.json`: 4 softened claims restored, 18 missed claims added (contributions, five findings, §6 conclusion and section framings, mostly verbatim), Figures 2 and 7 read (128 claims) |
| Revised 2 | `close_reading_revised_2.md` | the same, with 3 dropped intensifiers and 2 small wording slips restored, the Figure 2 range corrected, and the first §5.1 summary sentence added (129 claims) |

All three samples use seed 20261107, over 110, 128 and 129 claims. Revised 1 and
2 share 28 of their 30 claims; the original's sample is a different set.

**Accepted:** `analysis_revised.json`, as judged in `close_reading_revised_2.md`.
