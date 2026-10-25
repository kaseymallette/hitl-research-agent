# Evaluation Key

Barnett's blind comparisons, results, and costs. This key is never given to
the judge; model identities, cost, and runtime are considered afterwards.

## Tournament overview

The **PDF** and **Extract** (text and crops) divisions use the same seeds.
In each, Sol high (2) plays Sol medium (3); the winner faces Astra low (1),
which has a bye. The division champions meet in the final.

![Tournament bracket: Sol medium wins both divisions and advances to the undecided final.](assets/evaluation-bracket.svg)

Sol medium advances from both divisions. Every completed matchup split the
close-reading and argument-evaluation verdicts; the overall selections below
also account for cost and the role of close readings in later synthesis.

| Experiment | Close-reading winner | Evaluation winner | Overall selection |
| --- | --- | --- | --- |
| [1 · PDF first round](#experiment-1--pdf-first-round) | Sol high, narrowly | Sol medium, narrowly | **Sol medium** |
| [2 · Extract first round](#experiment-2--extract-first-round) | Sol high, narrowly | Sol medium, clearly | **Sol medium** |
| [3 · PDF semifinal](#experiment-3--pdf-semifinal) | Sol medium, modestly | Astra low, narrowly | **Sol medium** |
| [4 · Extract semifinal](#experiment-4--extract-semifinal) | Sol medium, modestly | Astra low, narrowly | **Sol medium** |
| [5 · Final](#experiment-5--final) | Pending | Pending | **To be decided** |

These are the head-to-head verdicts; disagreements with solo judgments are
noted in the experiment details. Model names are shortened below: Sol is
GPT-6.1 Sol and Astra is GPT-6 Astra. Costs are estimates from reported usage;
[run records and pricing assumptions](#run-records) are at the end.

## Experiment 1 — PDF first round

**Matchup:** (2) Sol high vs. (3) Sol medium.

Winner: **B — (3) GPT-6.1 Sol medium** — advances to the PDF semifinal

Sol high narrowly wins the close reading; Sol medium narrowly wins the
evaluation. Both verdicts hold in both reading orders. Higher effort does
not produce a consistently better result, and Sol high costs about 16% more.
Phase 3 synthesizes only close readings, which could favor Sol high, but its
edge is narrow and its missing “achievable” claims would enter the claims
store too.

Both runs receive the complete PDF and differ only in reasoning effort.

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **A** | GPT-6.1 Sol | high | $0.249 · 5 min 24 s | $0.102 · 1 min 16 s | $0.351 |
| **B** | GPT-6.1 Sol | medium | $0.214 · 5 min 2 s | $0.088 · 1 min 3 s | $0.302 |

### Detailed findings

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

## Experiment 2 — Extract first round

**Matchup:** (2) Sol high vs. (3) Sol medium.

Winner: **B — (3) GPT-6.1 Sol medium** — advances to the Extract semifinal

Sol high narrowly wins the close reading, but Sol medium clearly wins the
evaluation, finding two Major problems Sol high misses—including the only
number either run checks. Both verdicts hold in both reading orders, and
Sol high costs about 17% more.

Both runs receive extracted text and figure/table crops and differ only in
reasoning effort.

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **A** | GPT-6.1 Sol | high | $0.239 · 5 min 23 s | $0.091 · 1 min 12 s | $0.330 |
| **B** | GPT-6.1 Sol | medium | $0.206 · 4 min 36 s | $0.077 · 48 s | $0.282 |

### Detailed findings

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

**Implications for later comparisons.**

- B's dropped open-loop condition appears with both input methods, so it
  looks like a habit of Sol medium rather than an accident of one run.
- Both runs here describe artifacts of the prepared text as if they were the
  article: a "displaced" §2 sentence, and Table 1 as an image when it is
  printed as text. Neither reads the graphical abstract, which both PDF runs
  in Experiment 1 at least described. This bears on Experiment 5's
  input-method question.

## Experiment 3 — PDF semifinal

**Matchup:** (3) Sol medium vs. (1) Astra low.

Winner: **A — (3) GPT-6.1 Sol medium** — PDF division champion, advances to the final

Sol medium wins the close reading by a modest margin; Astra low narrowly
wins the evaluation. Both verdicts hold in both reading orders. Astra costs
4.3 times as much ($1.293 vs. $0.302), and its evaluation edge is too small
to justify that premium. Phase 3 synthesizes only close readings, where Sol
medium leads; the judge says the evaluations could reasonably be seen as
close to even.

Sol medium reuses Experiment 1’s winning PDF run (B).

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **A** | GPT-6.1 Sol (winner of Experiment 1) | medium | $0.214 · 5 min 2 s | $0.088 · 1 min 3 s | $0.302 |
| **B** | GPT-6 Astra | low | $0.892 · 3 min 30 s | $0.401 · 38 s | $1.293 |

### Detailed findings

**Close readings: A, by a modest margin.**

| | A (Sol medium) | B (Astra low) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 90% at 2, 10% at 1 | 83% at 2, 17% at 1 |
| A2, section conclusions (26) | 25 caught, 1 in part | 24 caught, 2 in part |
| A3, strength of language | 1 | 1 |
| A4, verbatim · numbers · references | 13/13 · 97/97 · 64/64 | 5/5 · 91/91 · 53/53 |
| Steps · claims | 25 · 117 | 21 · 93 |

- **A drops the scope condition on the curtailment risk,** the same error as
  in Experiment 1: it applies the risk to all natural-water cooling, where the
  article limits it to "once-through or open-loop" systems. B keeps the
  condition. This is A's only substantive alteration.
- **B has three smaller alterations, all confirmed in the runs.** It drops
  "capacity for" from Hainan's 400–800 servers, so a capacity reads as a
  deployed count. It turns Colón's "raise… environmental justice dimensions"
  into an asserted injustice. And it files the uncited Lule River hydropower
  figure under the Zhang (2024) citation.
- **B compresses Table 1,** one of the article's six stated contributions. It
  records the WUE and consumption values but leaves out the example-facility
  and trade-off columns. It is also partial on §4.1's Nordic conclusion (CO22)
  and the abstract's list of four technologies (AB5). A reads all of these in
  full.
- **B merges distinct claims more often,** against the prompt, and quotes
  `verbatim` less (5 quotes against A's 13). B catches H3's "limited by policy
  gaps", which A misses.

**Argument evaluations: B, narrowly.** Against the 34-problem list:

- **Found only by B:** P13, the 25,500 m³ arithmetic (Major, worked correctly;
  confirmed), and P9, tying application-level governance to the article's own
  §6.1 admission that the accounting doesn't exist. B also argues P1–P3 from
  §4's own constraints, where A states the same verdict without the
  derivation.
- **Found only by A:** P5 (the §4.5 heat-recovery hedge dropped in §6.2), P15
  in a concrete passage (Luleå's withdrawal figure reused as "suffices for
  hyperscale"), and a second citation mismatch (the aquifer study of another
  basin). A also partly touches P14 and P21, which B misses.
- **Relevance:** A again describes the framework as "rationing" and
  "officials classifying every application", where the article rejects
  binary bans. B credits that qualifier and shows why its objection survives
  it. B2: B at 2, A at 1.
- **Shared:** no factual errors in either. Neither fully finds P21
  (data-center figures used as AI figures).

The solo counts agree: B finds 6 of the 9 Major problems and partly finds 1;
A finds 4 and partly finds 3.

**Implications for later comparisons.**

- Sol medium's dropped open-loop condition is in both of its close readings,
  PDF and text, and every session that judged them found it. Expect it in
  Experiment 4.
- Sol medium's evaluation lost B2 points here for the "rationing" framing, the
  same drift noted in Experiment 1.

## Experiment 4 — Extract semifinal

**Matchup:** (3) Sol medium vs. (1) Astra low.

Winner: **A — (3) GPT-6.1 Sol medium** — Extract division champion, advances to the final

Sol medium wins the close reading by a modest margin; Astra low narrowly
wins the evaluation. Both verdicts hold in both reading orders. Astra costs
4.2 times as much ($1.172 vs. $0.282), and its thin evaluation edge is not
supported by the solo judgments.

Sol medium reuses Experiment 2’s winning Extract run (B).

| Run | Model | Reasoning effort | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- | --- |
| **A** | GPT-6.1 Sol (winner of Experiment 2) | medium | $0.206 · 4 min 36 s | $0.077 · 48 s | $0.282 |
| **B** | GPT-6 Astra | low | $0.823 · 3 min 28 s | $0.348 · 55 s | $1.172 |

### Detailed findings

**Close readings: A, by a modest margin.**

| | A (Sol medium) | B (Astra low) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 93% at 2, 7% at 1 | 93% at 2, 7% at 1 |
| A2, section conclusions (26) | 26 caught | 24 caught, 2 in part |
| A3, strength of language | 1 | 2 |
| A4, verbatim · numbers · references | 16/17 · 101/101 · 64/64 | 7/7 · 91/91 · 53/53 |
| Steps · claims | 26 · 109 | 20 · 84 |

- **A repeats its two known faults.** It drops the "once-through or
  open-loop" condition on the curtailment risk, though its support item
  restores it, and it marks the cut "Digital water sobriety challenges…"
  sentence `verbatim`. It also attaches the Yañez-Barnuevo citation to the
  whole footprint where the article attaches it to the wafer figure.
- **B keeps the open-loop condition but loses the article's close.** It has
  no claim for §6.3's "policy and siting choices, not technological
  necessity" (CO19), keeps only the last sentence of the Colón diagnosis
  (CO20), and attaches the Luleå and subsea contrast to the Colón verdict
  instead. Confirmed in the run.
- **B's own alterations:** it drops "Projections suggest" from the abstract's
  projection, and turns Colón's "raise… environmental justice dimensions"
  into "create environmental-justice failures" (confirmed), the same
  strengthening Astra made with the PDF in Experiment 3.
- **B merges distinct claims,** including §3.1 and §3.2 into one step past the
  prompt's pace. B catches H3's "limited by policy gaps" and the fifth
  research priority, which A misses.

The solo sessions are closer than the head-to-head: both readings score 93%
at 2 on A1, and the solo session put Astra at 2 on A3 and Sol medium at 1.
The head-to-head decided on coverage of the article's closing conclusions.

**Argument evaluations: B, narrowly.** Against the 34-problem list:

- **Found only by B:** P16 (Table 1's values without a capacity
  denominator), P18 (the dropped "or planned"), P24 (the Jain citation), P12,
  and P29, plus fuller versions of P5, P27, and P31.
- **Found only by A:** P21 (data-center figures used as AI figures) and P3
  (policy assumed to be the barrier), both Major, plus P8 and the measurement
  half of P9.
- **Shared:** both work P13's arithmetic correctly (17,520 m³). No factual
  errors in either. Both praise §3's scale comparison without seeing that it
  sets U.S. consumption against global withdrawals.

The judge calls the margin thin and resting on breadth more than severity:
B finds more listed problems, A finds more Major ones, and weighing only Major
problems would make them even. The solo sessions lean the other way: A's
found all nine Major problems at least in part and scored 2 on B2, while
B's missed P3 and scored 1 on B2.

**Implications for later comparisons.**

- Experiment 5 compares two runs whose faults are now well documented: Sol
  medium's PDF reading (Experiments 1 and 3) and its text reading
  (Experiments 2 and 4). Both drop the open-loop condition, so that error
  won't separate them.
- Both readings in this experiment again describe artifacts of the prepared
  text as the article's: the split §2 method passage, and neither reads the
  graphical abstract.

## Experiment 5 — Final

**Winner: to be decided.**

| Run | Configuration | Input | Total |
| --- | --- | --- | --- |
| **?** | GPT-6.1 Sol medium (winner of Experiment 3) | PDF | $0.302 |
| **?** | GPT-6.1 Sol medium (winner of Experiment 4) | extracted text and crops | $0.282 |

**Question for the comparison:** which input method reads and judges the
article better, at what difference in cost and preparation?

## Run records

### Pricing assumptions

Costs are calculated from the usage each run reported, per million tokens:
GPT-6.1 Sol at $2.00 input and $10.00 output, GPT-6 Astra at $10.00 input and
$50.00 output. They aren't confirmed billing.

### Shared setup and run IDs

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

### Experiment 1 records

Judgments: `outputs/judgments/barnett/exp1_barnett_pdf_sol_high_vs_medium/`

**Sources and letter assignments**

- A — `pdf__gpt-6.1-sol-high/`: `analysis.json` and
  `argument_evaluation.json`, from the rerun recorded in
  `argument_evaluation_rerun_record.json`.
- B — `pdf__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation_2.json`, copied as `argument_evaluation.json`. Its first
  evaluation was written under an earlier prompt and isn't judged.

**Token usage**

| Run | Input tokens | Output tokens | Reasoning tokens |
| --- | --- | --- | --- |
| **A** close reading | 18,479 | 21,158 | 1,552 |
| **A** evaluation | 36,665 | 2,892 | 1,034 |
| **B** close reading | 18,479 | 17,678 | 249 |
| **B** evaluation | 34,488 | 1,925 | 85 |

### Experiment 2 records

Judgments: `outputs/judgments/barnett/exp2_barnett_text_crops_sol_high_vs_medium/`

**Sources and letter assignments**

- A — `text_crops__gpt-6.1-sol-high/`: `analysis.json` and
  `argument_evaluation.json`.
- B — `text_crops__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation.json`.

**Token usage**

| Run | Input tokens | Output tokens | Reasoning tokens |
| --- | --- | --- | --- |
| **A** close reading | 12,992 | 21,659 | 2,031 |
| **A** evaluation | 31,201 | 2,832 | 1,034 |
| **B** close reading | 12,992 | 17,985 | 516 |
| **B** evaluation | 29,042 | 1,850 | 79 |

### Experiment 3 records

Judgments: `outputs/judgments/barnett/exp3_barnett_pdf_winner_vs_astra_low/`

**Sources and letter assignments**

- A — `pdf__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation_2.json`, copied as `argument_evaluation.json`, the same
  files as Experiment 1's B.
- B — `pdf__gpt-6-astra-low/`: `analysis.json` and `argument_evaluation.json`.

**Token usage**

GPT-6 Astra low's tokens: close reading 18,479 input, 14,145 output, 41
reasoning; evaluation 31,163 input, 1,794 output, 17 reasoning.

### Experiment 4 records

Judgments: `outputs/judgments/barnett/exp4_barnett_text_crops_winner_vs_astra_low/`

**Sources and letter assignments**

- A — `text_crops__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation.json`, the same files as Experiment 2's B.
- B — `text_crops__gpt-6-astra-low/`: `analysis.json` and
  `argument_evaluation.json`.

**Token usage**

GPT-6 Astra low's tokens: close reading 12,992 input, 14,199 output, 92
reasoning; evaluation 25,680 input, 1,826 output, 45 reasoning.

### Experiment 5 records

Judgments: `outputs/judgments/barnett/exp5_barnett_pdf_vs_text_crops/`
