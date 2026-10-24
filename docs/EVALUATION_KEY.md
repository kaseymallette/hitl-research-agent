# Evaluation Key

What each lettered run is, and what it cost. It is never given to the judge:
the judgment is blind, and its ranking is compared with cost and runtime here
afterwards.

Costs are calculated from the usage each run reported, per million tokens:
GPT-6.1 Sol at $2.00 input and $10.00 output, GPT-6 Astra at $10.00 input and
$50.00 output. They aren't confirmed billing.

Barnett's experiments run as a bracket, each eliminating a run:

| Experiment | Input | Runs |
| --- | --- | --- |
| 1 | PDF | GPT-6.1 Sol high vs. GPT-6.1 Sol medium |
| 2 | extracted text and crops | GPT-6.1 Sol high vs. GPT-6.1 Sol medium |
| 3 | PDF | the winner of 1 vs. GPT-6 Astra low |
| 4 | extracted text and crops | the winner of 2 vs. GPT-6 Astra low |
| 5 | the winners' own | the winner of 3 vs. the winner of 4 |

Experiment 5 answers the input-method question: the PDF, or extracted text
with crops.

Experiment 1 writes Barnett's reference lists, `claims_reference.md` and
`problems_reference.md`, and keeps them in
`exp1_barnett_pdf_sol_high_vs_medium/`. Experiments 2–5 copy them in and judge
against the same lists.

All of Barnett's runs come from
`outputs/ab_testing/barnett_itzhaki_2026_water_footprint_artificial_intelligence/adr_0013/`
and used the same instructions.

---

## Experiment 1 — Barnett, PDF input

Judgments: `outputs/judgments/exp1_barnett_pdf_sol_high_vs_medium/`

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

**Sources:**


- A — `pdf__gpt-6.1-sol-high/`: `analysis.json` and
  `argument_evaluation.json`, from the rerun recorded in
  `argument_evaluation_rerun_record.json`.
- B — `pdf__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation_2.json`, copied as `argument_evaluation.json`. Its first
  evaluation was written under an earlier prompt and isn't judged.

**Winner:**

---

## Experiment 2 — Barnett, extracted text and crops

Judgments: `outputs/judgments/exp2_barnett_text_crops_sol_high_vs_medium/`

The model was sent the article's extracted text, with crops of its figures and
tables, instead of the PDF. Both runs used the same model and the same
instructions, and differ only in reasoning effort.

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **A** | GPT-6.1 Sol | high | $0.239 · 5 min 23 s | $0.091 · 1 min 12 s | $0.330 |
| **B** | GPT-6.1 Sol | medium | $0.206 · 4 min 36 s | $0.077 · 48 s | $0.282 |

| Run | Input tokens | Output tokens | Reasoning tokens |
| --- | --- | --- | --- |
| **A** close reading | 12,992 | 21,659 | 2,031 |
| **A** evaluation | 31,201 | 2,832 | 1,034 |
| **B** close reading | 12,992 | 17,985 | 516 |
| **B** evaluation | 29,042 | 1,850 | 79 |

**Question for the comparison:** does the higher effort show in the readings
or the evaluations, and is any difference worth A's cost, about 17% more than
B's?

**Sources:**

- A — `text_crops__gpt-6.1-sol-high/`: `analysis.json` and
  `argument_evaluation.json`.
- B — `text_crops__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation.json`.

**Winner:**

---

## Experiment 3 — Barnett, PDF: the winner of 1 against GPT-6 Astra low

Judgments: `outputs/judgments/exp3_barnett_pdf_winner_vs_astra_low/`

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **?** | the winner of Experiment 1 | | | | |
| **?** | GPT-6 Astra | low | $0.892 · 3 min 30 s | $0.401 · 38 s | $1.293 |

GPT-6 Astra low's tokens: close reading 18,479 input, 14,145 output, 41
reasoning; evaluation 31,163 input, 1,794 output, 17 reasoning.

**Question for the comparison:** does GPT-6 Astra read or judge better, and is
any difference worth its cost, about four times GPT-6.1 Sol's?

**Sources:** the winner's files as in Experiment 1, and
`pdf__gpt-6-astra-low/`: `analysis.json` and `argument_evaluation.json`.

**Winner:**

---

## Experiment 4 — Barnett, extracted text and crops: the winner of 2 against GPT-6 Astra low

Judgments: `outputs/judgments/exp4_barnett_text_crops_winner_vs_astra_low/`

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **?** | the winner of Experiment 2 | | | | |
| **?** | GPT-6 Astra | low | $0.823 · 3 min 28 s | $0.348 · 55 s | $1.172 |

GPT-6 Astra low's tokens: close reading 12,992 input, 14,199 output, 92
reasoning; evaluation 25,680 input, 1,826 output, 45 reasoning.

**Question for the comparison:** does GPT-6 Astra read or judge better, and is
any difference worth its cost, three and a half to four times GPT-6.1
Sol's?

**Sources:** the winner's files as in Experiment 2, and
`text_crops__gpt-6-astra-low/`: `analysis.json` and
`argument_evaluation.json`.

**Winner:**

---

## Experiment 5 — Barnett: the winner of 3 against the winner of 4

Judgments: `outputs/judgments/exp5_barnett_pdf_vs_text_crops/`

| Run | Configuration | Input | Total |
| --- | --- | --- | --- |
| **?** | the winner of Experiment 3 | PDF | |
| **?** | the winner of Experiment 4 | extracted text and crops | |

**Question for the comparison:** which input method reads and judges the
article better, at what difference in cost and preparation?

**Winner:**
