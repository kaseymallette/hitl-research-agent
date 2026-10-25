# Evaluation Key

What each lettered run is, and what it cost. It is never given to the judge:
the judgment is blind, and its ranking is compared with cost and runtime here
afterwards.

Costs are calculated from the usage each run reported, per million tokens:
GPT-6.1 Sol at $2.00 input and $10.00 output, GPT-6 Astra at $10.00 input and
$50.00 output. They aren't confirmed billing.

Barnett's experiments run as a bracket, each eliminating a run:

| Experiment | Input | Runs | Winner |
| --- | --- | --- | --- |
| 1 | PDF | GPT-6.1 Sol high vs. GPT-6.1 Sol medium | **GPT-6.1 Sol medium** |
| 2 | extracted text and crops | GPT-6.1 Sol high vs. GPT-6.1 Sol medium | **GPT-6.1 Sol medium** |
| 3 | PDF | GPT-6.1 Sol medium (winner of 1) vs. GPT-6 Astra low | |
| 4 | extracted text and crops | GPT-6.1 Sol medium (winner of 2) vs. GPT-6 Astra low | |
| 5 | the winners' own | the winner of 3 vs. the winner of 4 | |

Experiment 5 answers the input-method question: the PDF, or extracted text
with crops.

Experiment 1 writes Barnett's reference lists, `claims_reference.md` and
`problems_reference.md`, kept once in `outputs/judgments/barnett/references/`. Experiments
2–5 copy them in and judge against the same lists. Each experiment's own folder
under `barnett/` holds only its six judgments.

All of Barnett's runs come from
`outputs/ab_testing/barnett_itzhaki_2026_water_footprint_artificial_intelligence/adr_0013/`
and used the same instructions.

Each judgment records the `id` at the top of the file it judged. Check it
against this table to confirm the right file went under each letter. The ids
say nothing about how a run was made, so they stay blind.

| Run folder | `analysis.json` id | Argument evaluation id |
| --- | --- | --- |
| `pdf__gpt-6.1-sol-high/` | `bee567c1-d264-4806-a1f7-40a5bb43e01c` | `5b3c4998-8652-4bb3-aeb1-e651b988dd16` |
| `pdf__gpt-6.1-sol-medium/` | `b52aa04e-d9f7-4e11-8e78-fbab1dd1da59` | `b35af235-25d9-4f75-897a-3a2b33ac6625` (`argument_evaluation_2.json`) |
| `pdf__gpt-6-astra-low/` | `58057f58-eb36-44ca-bdc6-f8a84ac4f6a6` | `5ec263ff-886b-4a8b-bf36-a2f967ffbdf3` |
| `text_crops__gpt-6.1-sol-high/` | `56377890-9bfb-469c-8786-ece6a6ea5348` | `21ca21e5-73fa-4d0c-a75a-0d9f9171417f` |
| `text_crops__gpt-6.1-sol-medium/` | `182e2233-37de-4fde-b637-d787f5cc0fef` | `77671eb8-5439-4e76-9125-78ebd96dba09` |
| `text_crops__gpt-6-astra-low/` | `cb4cc7f2-e7a3-4b12-862c-4db104ab494a` | `52123ee9-3f08-4980-8a3d-7b5e9b27b204` |

---

## Experiment 1 — Barnett, PDF input

Judgments: `outputs/judgments/barnett/exp1_barnett_pdf_sol_high_vs_medium/`

### Winner: **B — GPT-6.1 Sol medium**

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

### Why B won

Each run narrowly won one document, and
each verdict held in both reading orders. The higher effort didn't show
consistently, so B's lower cost decides it.

**Close readings: A, narrowly.**

| | A (high) | B (medium) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 97% at 2, 3% at 1 | 87% at 2, 13% at 1 |
| A1, head to head (15 each, same seed) | 15/15 at 2 | 15/15 at 2 |
| A2, section conclusions (26) | 23 caught, 3 in part | 26 caught |
| A3, strength of language | 1 | 1 |
| A4, mechanical checks | clean | clean |
| Steps · claims | 25 · 135 | 25 · 117 |

Each reading has one weakness that matters, both confirmed in the runs:

- **B drops a scope condition.** In §4.2 the article limits the curtailment
  risk to "once-through or open-loop" cooling. B applies it to all
  natural-water cooling, including the closed-loop systems the section
  describes. A keeps the condition.
- **A leaves out the hopeful half of the thesis.** The article says in §4,
  §5, §6, and the closing that water-sustainable AI is achievable. A records
  none of these as a claim and keeps only the limitation each is paired with.
  B records it in §4 and the closing.

The head-to-head weighed B's scope error more heavily, and found that A
follows the prompt's rules more closely: it records the graphical abstract as
paraphrased support, keeps distinct claims separate, and copies citation
markers as printed. The margin is arguably closer than the head-to-head says:
A's omission is a pattern across the article and concerns half its central
claim, where B's is one error, and the solo coverage counts favor B.

**Argument evaluations: B, narrowly.** Against the 34-problem list, in the
head-to-head:

- **Found only by B:** P3 (limited deployment blamed on policy gaps without
  evidence, Major), P28 (reform concluded necessary without showing
  alternatives fail), P29 (corporate pledges dismissed by assertion), P24
  (two citations that don't fit their claims, Jain 2025 and the aquifer study
  of another basin), and P31 (descriptive evidence to a normative ranking),
  stated more exactly than A.
- **Found only by A:** P21 (data-center figures used as AI figures, Major and
  pervasive), P9, and P12. A also credits the article's disclaimer of
  prohibition, where B's "rationing" drifts toward a position the article
  rejects.
- **Shared:** no factual errors beyond both dropping "U.S." from the §3
  comparison. Neither checks any of the article's numbers, so P13's
  arithmetic is found by neither.

The two solo sessions graded at different strictness: A's counted 9 found and
8 partial, B's 15 found and 4 partial, crediting B with problems the
head-to-head calls partial. The solo counts overstate B's lead; the
head-to-head, reading both in one session, still favors B.

**Bottom line.** The results split one each way, on narrow margins. A's reasoning
tokens (1,552 against 249 on the close reading) didn't buy a reliably better
document, and A costs about 16% more. The case for A is that Phase 3's
synthesis reads only close readings, so a close-reading edge could count for
more; but A's edge is narrow, and its missing "achievable" claims would enter
the claims store too.

---

## Experiment 2 — Barnett, extracted text and crops

Judgments: `outputs/judgments/barnett/exp2_barnett_text_crops_sol_high_vs_medium/`

### Winner: **B — GPT-6.1 Sol medium**

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

### Why B won

The same split as Experiment 1: A narrowly
won the close readings and B won the evaluations, each verdict holding in both
reading orders. B's evaluation lead is wider here, and B costs less.

**Close readings: A, narrowly.**

| | A (high) | B (medium) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 90% at 2, 10% at 1 | 83% at 2, 17% at 1 |
| A1, head to head (every item) | no 0s, 1 claim at 1 | 1 claim at 0, 3 at 1 |
| A2, section conclusions (26) | 25 caught, 1 in part | 25 caught, 1 in part |
| A3, strength of language | 2 (borderline 1) | 1 |
| A4, verbatim · references | 11/11 · 65/66 | 16/17 · 64/64 |
| Steps · claims | 23 · 133 | 26 · 109 |

Each reading has faults the other doesn't, all confirmed in the runs:

- **B marks a cut sentence `verbatim`.** "Digital water sobriety challenges the
  assumption…" drops the author's "analogous to frameworks in climate and
  energy policy" with no ellipsis, the only 0 in either reading. A records the
  same sentence as paraphrased.
- **B drops the scope condition on the curtailment risk again.** Its claim
  applies the risk to all natural-water cooling; the article limits it to
  "once-through or open-loop" systems. A keeps the condition. B made the same
  error in Experiment 1.
- **A drops an author from a reference entry.** Its Pfister et al. (2017) entry
  leaves out "Döll, P."; B's includes him.
- **A files a duplicated §2 claim under §3,** and fills about a dozen support
  items with its own description of how the argument links up, once
  strengthening the author ("decisive").

A also keeps H3's "limited by policy gaps" and CO12's EIA analogy, which B
misses; B keeps the condition on the 2027 projection ("If this increase in AI
use continues"), which A drops, and follows the article's breaks more closely.
The head-to-head decided on A1, where only B has a 0.

**Argument evaluations: B, by a clear margin.** Against the 34-problem list:

- **Found only by B:** P13, the article's one checkable arithmetic error (1 MW
  at 2 L/kWh is 17,520 m³ a year, not 25,500; confirmed), and P21,
  data-center figures used as AI figures. Both are Major. B also finds P8 (the
  urgency argument from unfamiliarity with a term, which is self-cited) and
  partly P3.
- **Found only by A:** P16 (Table 1's per-MW values with no capacity
  denominator) and partly P29, plus sharper versions of P6, P7, and P31
  that both runs found.
- **Shared:** no factual errors in either. A has two slight overreaches
  (disclosure metrics, replenishment) that B doesn't. Both praise §3's scale
  comparison without seeing that it sets U.S. consumption against global
  withdrawals (P15).

The solo sessions agree: B touches all nine Major problems and misses none,
while A misses P13 and P21. Solo totals are close (A 9 found and 7 partial, B
10 and 7) because A's finds sit in Moderate and Minor problems.

**Bottom line.** Higher effort again bought a slightly more faithful close reading
and a weaker evaluation. B's evaluation finds two Major problems A misses,
including the only number either run checks, and A costs about 17% more.

**For later experiments.**

- B's dropped open-loop condition appears with both input methods, so it
  looks like a habit of Sol medium rather than an accident of one run.
- Both runs here describe artifacts of the prepared text as if they were the
  article: a "displaced" §2 sentence, and Table 1 as an image when it is
  printed as text. Neither reads the graphical abstract, which both PDF runs
  in Experiment 1 at least described. This bears on Experiment 5's
  input-method question.

---

## Experiment 3 — Barnett, PDF: the winner of 1 against GPT-6 Astra low

Judgments: `outputs/judgments/barnett/exp3_barnett_pdf_winner_vs_astra_low/`

### Winner: *to be decided*

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **?** | GPT-6.1 Sol (winner of Experiment 1) | medium | $0.214 · 5 min 2 s | $0.088 · 1 min 3 s | $0.302 |
| **?** | GPT-6 Astra | low | $0.892 · 3 min 30 s | $0.401 · 38 s | $1.293 |

GPT-6 Astra low's tokens: close reading 18,479 input, 14,145 output, 41
reasoning; evaluation 31,163 input, 1,794 output, 17 reasoning.

**Question for the comparison:** does GPT-6 Astra read or judge better, and is
any difference worth its cost, about four times GPT-6.1 Sol's?

**Sources:** the winner's files as in Experiment 1, and
`pdf__gpt-6-astra-low/`: `analysis.json` and `argument_evaluation.json`.

---

## Experiment 4 — Barnett, extracted text and crops: the winner of 2 against GPT-6 Astra low

Judgments: `outputs/judgments/barnett/exp4_barnett_text_crops_winner_vs_astra_low/`

### Winner: *to be decided*

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **?** | GPT-6.1 Sol (winner of Experiment 2) | medium | $0.206 · 4 min 36 s | $0.077 · 48 s | $0.282 |
| **?** | GPT-6 Astra | low | $0.823 · 3 min 28 s | $0.348 · 55 s | $1.172 |

GPT-6 Astra low's tokens: close reading 12,992 input, 14,199 output, 92
reasoning; evaluation 25,680 input, 1,826 output, 45 reasoning.

**Question for the comparison:** does GPT-6 Astra read or judge better, and is
any difference worth its cost, three and a half to four times GPT-6.1
Sol's?

**Sources:** the winner's files as in Experiment 2, and
`text_crops__gpt-6-astra-low/`: `analysis.json` and
`argument_evaluation.json`.

---

## Experiment 5 — Barnett: the winner of 3 against the winner of 4

Judgments: `outputs/judgments/barnett/exp5_barnett_pdf_vs_text_crops/`

### Winner: *to be decided*

| Run | Configuration | Input | Total |
| --- | --- | --- | --- |
| **?** | the winner of Experiment 3 | PDF | |
| **?** | the winner of Experiment 4 | extracted text and crops | |

**Question for the comparison:** which input method reads and judges the
article better, at what difference in cost and preparation?
