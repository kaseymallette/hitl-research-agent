# Evaluation Key

What each lettered run is, and what it cost. It is never given to the judge:
the judgment is blind, and its ranking is compared with cost and runtime here
afterwards.

Costs are calculated from the usage each run reported, at $2.00 per million
input tokens and $10.00 per million output tokens. They aren't confirmed
billing.

---

## Experiment 1 — Barnett, PDF input

Judgments: `outputs/judgments/barnett_pdf_sol_high_vs_medium/`

The article was sent to the model as the complete PDF. Both runs used the same
model and the same instructions, and differ only in reasoning effort.

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **A** | GPT-6.1 Sol | high | $0.249 · 5 min 24 s | $0.102 · 1 min 16 s | $0.351 |
| **B** | GPT-6.1 Sol | medium | $0.214 · 5 min 2 s | $0.088 · 1 min 3 s | $0.302 |

| Run | Input tokens | Output tokens | Reasoning tokens |
| --- | --- | --- | --- |
| **A** close reading | 18,479 | 21,158 | 1,552 |
| **A** evaluation | 36,665 | 2,892 | 1,034 |
| **B** close reading | 18,479 | 17,678 | 249 |
| **B** evaluation | 34,488 | 1,925 | 85 |

**Question for the comparison:** does the higher effort show in the readings
or the evaluations, and is any difference worth A's cost, about 16% more than
B's?

**Sources:** in the project repository, under
`outputs/ab_testing/barnett_itzhaki_2026_water_footprint_artificial_intelligence/adr_0013/`:

- A — `pdf__gpt-6.1-sol-high/`: `analysis.json` and
  `argument_evaluation.json`, from the rerun recorded in
  `argument_evaluation_rerun_record.json`.
- B — `pdf__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation_2.json`, copied as `argument_evaluation.json`. Its first
  evaluation was written under an earlier prompt and isn't judged.
