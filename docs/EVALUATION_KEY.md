# Evaluation Key

The blind comparisons, results, and costs for Phase 2's two articles:
[**Barnett**](#barnett-tournament-overview) and
[**Kanbur**](#kanbur-tournament-overview).
This key is never given to the judge; model identities, cost, and runtime are
considered afterwards.

## Barnett tournament overview

**Overall winner: GPT-6.1 Sol medium with PDF input.**

Selected from the six Barnett configurations. The final favors PDF for its
cleaner source representation and lack of an extraction/preparation step;
its close reading won with the letters both ways, and the argument
evaluations are treated as tied because their verdict followed the letter. This is the overall selection for this experiment, with the
judging limitations described below.

The **PDF** and **Extract** (text and crops) divisions use the same seeds.
In each, Sol high (2) plays Sol medium (3); the winner faces Astra low (1),
which has a bye. The division champions meet in the final.

![Tournament bracket: Sol medium wins both divisions, and Sol medium on the PDF wins the final.](assets/evaluation-bracket.svg)

## Kanbur tournament overview

Kanbur runs the same model, GPT-6.1 Sol, three ways: through the **API**, the
ChatGPT **App** in work mode, and **Codex**. The two divisions are reasoning
efforts, **Medium** and **High**. In each division, App (2) plays Codex (3); the winner faces API (1), which has
a bye. The division champions meet in the final, which answers the effort
question for this article: medium or high.

![Kanbur tournament bracket: Codex wins both divisions, and Codex medium defeats Codex high in Experiment 5 to become tournament champion.](assets/kanbur-evaluation-bracket.svg)

**Overall winner: GPT-6.1 Sol medium through Codex.**

Codex won every round. The API didn't win either semifinal; both were close,
and Codex runs within the subscription where the API costs $0.55–0.64 a run.
In the final, Codex medium beat Codex high on both the close reading and the
evaluation with the letters both ways, the first Kanbur verdicts that held
whichever run was A.

## Barnett results

Sol medium won both divisions, then its PDF run won the final. The overall
winners below account for the detailed findings, cost, preparation, and the
role of close readings in later synthesis—not just the individual verdicts.

| Experiment | Close-reading winner | Evaluation winner | Overall winner |
| --- | --- | --- | --- |
| [1 · PDF first round](#experiment-1--pdf-first-round) | Sol high, narrowly | Sol medium, narrowly | **Sol medium** |
| [2 · Extract first round](#experiment-2--extract-first-round) | Sol high, narrowly | Sol medium, clearly | **Sol medium** |
| [3 · PDF semifinal](#experiment-3--pdf-semifinal) | Sol medium, modestly | Astra low, narrowly | **Sol medium** |
| [4 · Extract semifinal](#experiment-4--extract-semifinal) | Sol medium, modestly | Astra low, narrowly | **Sol medium** |
| [5 · Final](#experiment-5--final) | PDF, narrowly, both orders | Tie (followed the letter) | **Sol medium, PDF** |

## Kanbur results

| Experiment | Close-reading winner | Evaluation winner | Overall winner |
| --- | --- | --- | --- |
| [1 · Medium first round](#kanbur-experiment-1--medium-first-round) | Codex, narrowly | Codex, narrowly | **Codex** |
| [2 · High first round](#kanbur-experiment-2--high-first-round) | App, narrowly (solos favor Codex) | Codex, narrowly | **Codex** |
| [3 · Medium semifinal](#kanbur-experiment-3--medium-semifinal) | Codex, narrowly | API, narrowly | **Codex** |
| [4 · High semifinal](#kanbur-experiment-4--high-semifinal) | Codex, narrowly (solos favor API) | Tie | **Codex** |
| [5 · Final](#kanbur-experiment-5--final) | Codex medium, narrowly, both orders | Codex medium, narrowly, both orders | **Codex medium** |

## Barnett judging notes

These are the head-to-head verdicts; disagreements with solo judgments are
noted in the experiment details.

**The verdicts mostly follow the letters.** In Experiments 1–4, every
close-reading head-to-head chose run A and every evaluation head-to-head chose
run B, whichever configuration was under each letter. Experiment 5 ran each
head-to-head with the letters both ways. Its evaluation went to B in all four
sessions, two in each order. Its close reading went to the PDF both times, as
A and as B, the only Barnett verdict that held with the letters swapped. The
order check in each session can't catch letter bias, because the judge knows
the letters in both readings. So the verdicts alone don't show that one
configuration is better; each selection rests on cost and on findings
confirmed in the runs themselves, which don't depend on the judge.

Model names are shortened below: Sol is
GPT-6.1 Sol and Astra is GPT-6 Astra. Costs are estimates from reported usage;
[Barnett run records and pricing assumptions](#barnett-run-records) follow Experiment 5.

## Experiment 1 — PDF first round

**Matchup:** (2) Sol high vs. (3) Sol medium.

**Overall winner:** **B — (3) GPT-6.1 Sol medium** — advances to the PDF semifinal

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

**Overall winner:** **B — (3) GPT-6.1 Sol medium** — advances to the Extract semifinal

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

**Overall winner:** **A — (3) GPT-6.1 Sol medium** — PDF division champion, advances to the final

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

**Overall winner:** **A — (3) GPT-6.1 Sol medium** — Extract division champion, advances to the final

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

**Matchup:** PDF champion vs. Extract champion: Sol medium on the PDF vs. Sol
medium on extracted text and crops.

**Overall winner:** **GPT-6.1 Sol medium, PDF** — champion

The PDF narrowly wins the close reading in both letter positions: as A in
session AB and as B in session BA. The evaluation is a tie, since its verdict
went to whichever run was B in every session. The extracted text is 7%
cheaper per run ($0.282 vs. $0.302) but needs a preparation step, and it
leaves artifacts of that preparation in the reading. The PDF reading has none
of them, and close readings are what Phase 3's synthesis uses.

Same model, same effort, same instructions: only the input differs. Both runs
were judged alone in earlier experiments (the PDF run in Experiments 1 and 3,
the text run in 2 and 4), so this experiment has only the head-to-heads, each
run twice with the letters swapped.

| Run | Session AB | Session BA | Input | Total |
| --- | --- | --- | --- | --- |
| GPT-6.1 Sol medium (winner of Experiment 3) | **A** | **B** | PDF | $0.302 |
| GPT-6.1 Sol medium (winner of Experiment 4) | **B** | **A** | extracted text and crops | $0.282 |

### Detailed findings

**Close readings: PDF, narrowly, in both sessions.**

| Session | A | B | Verdict |
| --- | --- | --- | --- |
| AB | PDF | text | **A** (PDF), narrowly |
| BA | text | PDF | **B** (PDF), narrowly |

Both judges read every claim in both runs, not a sample. The scores below are
session AB's; session BA's counts agree.

| | PDF | text |
| --- | --- | --- |
| A1, every claim | no 0s, about four at 1 | one 0, about three at 1 |
| A2, coverage | everything on the list; graphical abstract in `meaning` | everything but the graphical abstract; one research priority only in `meaning` |
| A3, strength of language | 1 | 1, closer to 2 |
| A4, verbatim · numbers · references | 13/13 · 97/97 · 64/64, clean | 16/17 · 101/101 · 64/64, damaged markers |
| Steps · claims | 25 · 117 | 26 · 109 |

Both sessions found the same faults, all confirmed in the runs:

- **The text run carries artifacts of its prepared input.** Citation markers
  and entries hold extraction debris ("(Holzle, ¨ 2022)",
  "(Yanez-Barnuevo, 2025˜ )"), where the PDF run prints "Hölzle" correctly.
  Table 1's support items say "gap T1" and "read from the retained image",
  though the table is printed as text. Its reading plan describes an
  "interrupted methodological passage" the PDF doesn't have, and that
  misplaces one §2 claim. And it never mentions the graphical abstract.
- **The text run marks the cut "Digital water sobriety challenges…" sentence
  `verbatim`,** the only 0 in either reading, the same fault found in
  Experiments 2 and 4.
- **The PDF run softens or strengthens §4.2.** It drops the "once-through or
  open-loop" condition from the curtailment claim, turns "raise ecological
  questions" into "can coexist with", and drops "if widely scaled". The text
  run's claim text broadens the curtailment risk too, but its support puts
  the condition back. These are the PDF run's known faults from Experiments
  1 and 3.
- **Each records something the other leaves in `meaning`.** The PDF run
  records all five §6.1 research priorities and §5.1's reporting dimension
  ("mandatory facility-level WUE") as claims. The text run keeps both halves
  of Table 1's footnote b and records the §3 prose's 25,500 m³ figure.

Both judges weighed the text run's misquotation and the false statements
about the article's layout as heavier than the PDF run's qualifier shifts.
Both called the margin small. Because the PDF won as A and as B, this verdict
doesn't follow the letter. It is the only head-to-head in Barnett that won in
both positions.

**Argument evaluations: a tie.** The evaluation head-to-head was run four
times. The first session with each letter order is kept in the judgments
folder.

| Session | A | B | Verdict |
| --- | --- | --- | --- |
| AB, 1 (kept) | PDF | text | **B** (text), modest margin |
| AB, 2 | PDF | text | **B** (text), narrowly |
| BA, 1 | text | PDF | **B** (PDF), narrowly |
| BA, 2 (kept) | text | PDF | **B** (PDF), narrowly |

The sessions agree on what each evaluation found and differ only on how much
it counts:

- **Found only by the text run:** P13 (the 25,500 m³ arithmetic) and P21
  (data-center figures used as AI figures), both Major, plus P8 and P9.
- **Found only by the PDF run:** P16 (Table 1's values without a capacity
  denominator), P23 (the unreproducible method and source mix), P24 (two
  misfitting citations), P29, and P18 in part, plus P5 tied to §4.5's own
  caveat.
- **Relevance:** the PDF run again calls the framework "rationing", which the
  article rejects; the text run engages its graduated form.
- **Shared:** no factual errors in either.

These are the same two evaluations judged in Experiments 1–4, and the same
finds were credited to them there. The kept BA session calls the margin close
to a tie for a researcher who weights numerical checks heavily.

**Bottom line.** With the evaluations tied, the close reading decides it, and
it is the one verdict that held with the letters swapped. The input points the
same way on what the judge can't sway: the prepared text needs a preparation
step that took manual fixes in Phase 1, it costs the reading accuracy about
the article itself (its layout, its markers, its graphical abstract), and it
saves $0.02 a run. The PDF wins.

## Barnett run records

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

**Sources and letter assignments**

- `pdf__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation_2.json`, copied as `argument_evaluation.json`, the same
  files as Experiment 1's B and Experiment 3's A. A in session AB, B in
  session BA.
- `text_crops__gpt-6.1-sol-medium/`: `analysis.json` and
  `argument_evaluation.json`, the same files as Experiment 2's B and
  Experiment 4's A. B in session AB, A in session BA.

Each judgment is named by its session: `close_reading_head_to_head_AB.md`
and `_BA.md`, `evaluation_head_to_head_AB.md` and `_BA.md`.

---

## Kanbur judging setup

All runs read the PDF. The question across the tournament, from
[ADR-0017](adr/0017-experiment-2-api-against-the-app-with-the-primer.md) and
[ADR-0020](adr/0020-codex-joins-experiment-2.md), is whether the API adds
anything over the App and Codex, which report no per-run cost.

Kanbur has no full set of researcher notes, so its reference lists are written
fresh in Experiment 1 (prompts 1 and 5) and reused in Experiments 2–5. The
judging follows Barnett's in Experiments 1–4, six judgments each. Barnett's
head-to-head verdicts followed the letters, so Experiment 5 runs each of its
two head-to-heads twice, with the letters swapped the second time: 4
judgments there, 28 in all.

## Kanbur experiment 1 — Medium first round

**Matchup:** (2) App vs. (3) Codex, both at medium effort.

**Overall winner:** **B — (3) Codex, medium** — advances to the Medium semifinal

Codex narrowly wins both the close reading and the evaluation. Both
head-to-head verdicts hold in both reading orders. Neither run reports a
cost, so the findings decide it. Codex reads every figure, where the App
names four without saying what they show. Its evaluation adds two problems
the App's misses and makes no factual error, where the App's misreads
Table 2's pump price. The App's advantages are narrower: it keeps the
abstract's "for real applications" and finds P5, a Major problem Codex
misses.

Both runs read the complete PDF at medium effort and differ only in how
they were run.

| Run | Configuration | Close reading | Argument evaluation |
| --- | --- | --- | --- |
| **A** | App, work mode, medium | not reported | not reported |
| **B** | Codex, medium | about 7–8 min | about 3 min |

### Detailed findings

**Close readings: B, narrowly.**

| | A (App) | B (Codex) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 97% at 2, 3% at 1 | 97% at 2, 3% at 1 |
| A2, contributions (4) | 3 caught, 1 in part | 4 caught, 1 reframed |
| A2, abstract claims (12) | 11 caught | 9 caught, 1 in part, 2 missed |
| A2, figures (10) | 7 read, 3 named only | 9 read, 1 named only |
| A3, strength of language | solo 2, head to head 1 | 1 |
| A4, verbatim · numbers · references | 2/2 · 311/311 · 47/47 | 0/0 · 318/318 · 47/47 |
| Steps · claims | 46 · 147 | 36 · 151 |

Each reading has faults the other doesn't, all confirmed in the runs:

- **A changes Table 1's units.** Its support says the heat-flux columns are
  "in W/m²"; the table prints "W/m²K". That's a silent correction the
  prompt forbids. A also drops the literature gap's "as far as we know".
- **A reads fewer figures.** For Figures 4 and 10 it gives only what they
  plot, not what they show; the trends in its claims come from the prose.
  B reads every figure but Figure 3, and its readings agree with the
  reference list's by-eye checks, including Figure 8's slight rise with
  area.
- **B drops the abstract's scope.** "Economically feasible for real
  applications" becomes "evidence of economic feasibility", so the shift
  to the Conclusion's "for further real-scale demonstrations" is lost. A
  keeps it. B also changes contribution (b): the article's "new alternative
  to the data center cooling systems" becomes "a new clean-water-producing
  alternative".
- **B keeps more of what the article prints.** It records both halves of
  the self-contradictory GOR/PR sentence, Table 3's printed "c3 = u3", and
  "the PP is assumed constant". A smooths the GOR/PR sentence and misses the
  other two.

A also gives every Table 1 value, where B gives only the differences, and
catches AB1 and AB6, which B misses. The head-to-head decided on figure
readings and contributions, which are whole categories, against A's
specific items. The solo sessions are closer: the same A1 score, and A at 2
on A3 where B is at 1.

**Argument evaluations: B, narrowly.** Against the 23-problem list:

- **Found only by B:** P8 (chemical exergy dropped in a desalination
  system) and P7 (SI read as evidence of sustainability). B also gives
  fuller versions of P2 (the flat payback against a fifteenfold change in
  water output) and P4: since flux doesn't depend on area, Eq. 24 would
  rise with area, while Figure 5B falls. That rules out Eq. 24 as the
  quantity computed.
- **Found only by A:** P5 (the text puts the GOR and PR peaks at the
  smallest area, against Eqs. 22–23), a Major problem. A also turns P1's
  revenue gap into a payback of about 980 years.
- **Errors:** A writes "Table 2 lists a pump price of SGD 950" for one
  added pump; the row is "Feed and permeate pumps", one price for both. So
  its 980 years is about twice too high. A hedges this, and its conclusion
  stands either way. B has no errors.
- **Shared:** P1, P3, P13 and P22, and P16 in part. Neither finds P10
  (levelized costs far above the cost inputs), the other Major problem.

The solo sessions agree on the shape: each run finds 5 of the 7 Major
problems; A has 7 found and 3 partial, B 8 found and 3 partial.

**Implications for later comparisons.**

- Barnett's close-reading head-to-heads always chose A. This one chose B,
  so that verdict isn't simply the letter. The evaluation verdict went to B,
  as every Barnett evaluation did, so it rests on the findings above.
- B's dropped "for real applications" is the same kind of fault as Sol
  medium's dropped open-loop condition in Barnett: a scope condition lost
  from a headline claim. Watch for it in Experiment 3.

## Kanbur experiment 2 — High first round

**Matchup:** (2) App vs. (3) Codex, both at high effort.

**Overall winner:** **B — (3) Codex, high** — advances to the High semifinal

The App narrowly wins the close-reading head-to-head and Codex narrowly wins
the evaluation; both verdicts hold in both reading orders. That is the same
split by letter as every Barnett round before the final, so neither verdict
counts on its own. The solo sessions lean the other way on the close
reading: Codex scores higher on attribution and strength of language. Neither
run reports a cost. Codex's evaluation makes no factual error and covers
more of the list; the App's misreads Table 2's pump price again, as in
Experiment 1. That decides it for Codex, narrowly.

Both runs read the complete PDF at high effort and differ only in how they
were run.

| Run | Configuration | Close reading | Argument evaluation |
| --- | --- | --- | --- |
| **A** | App, work mode, high | not reported | not reported |
| **B** | Codex, high | about 7–8 min | about 3 min |

### Detailed findings

**Close readings: A, narrowly, in the head-to-head; the solos favor B.**

| | A (App) | B (Codex) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 87% at 2, 13% at 1 | 97% at 2, 3% at 1 |
| A2, contributions (4) | 4 caught | 2 caught, 2 thinned (C-a, C-b) |
| A2, abstract claims (12) | 11 caught | 12 caught |
| A2, figures (10) | 8 read, 2 thinned | 9 read, 1 thin (F10) |
| A3, strength of language | 1 | 2 |
| A4, verbatim · numbers · references | 0/0 · 349/349 · 68/68 | 2/2 · 317/317 · 74/74 |
| Steps · claims | 42 · 167 | 37 · 158 |

Each reading has one fault that matters, both confirmed in the runs:

- **A rewrites the self-contradictory GOR/PR sentence.** The article says GOR
  and PR are highest at the minimum area, then that the maximum values are
  "nearly 14 times higher than the GOR and PR values of the minimum membrane
  area." A gives the second half as "nearly fourteen times the values at the
  other end of the area comparison", which removes the contradiction. The
  App medium run smoothed the same sentence in Experiment 1. B records both
  halves as printed.
- **B writes off the contributions as restatements.** Its step 4 says "the
  four contributions restate the novelty and methods already announced in
  the Summary." The Summary doesn't make them, so the article's "not
  investigated before" and "first time" claims never appear as claims. A
  records all four.

A also reads Tables 1 and 3 in full, including Table 3's printed "c₃ = u₃".
B labels Table 1's column groups "total heat flux" and "vapor heat flux",
though both are printed "q^T (W/m²K)". B keeps all twelve abstract claims
separate, where A merges four into two, and it quotes `verbatim` where A
never does. A's solo session found four sampled claims at 1 (a hedge lost
on "leakage potential", "clearly" dropped, "can" turned into "should", and the
GOR/PR sentence) against B's one. The head-to-head decided on the
contributions.

**Argument evaluations: B, narrowly.** Against the 23-problem list:

- **Found only by B:** P2 as the list states it (a flat payback against
  water output that varies with load and area), the cost-rate mechanism in
  P13 ("Hourly water cost is not cost per unit of net water produced"),
  part of P14 (the optimum area's false precision), and P21 stated as a
  missing comparison. It also anchors P4 to Figures 5B and 6A.
- **Found only by A:** P22 taken into the economics: only pump electricity
  is costed, so a chiller's energy and cost would belong in the assessment.
- **Errors in A:** it applies Table 2's 950 SGD to "the additional permeate
  pump", though the row prices the feed and permeate pumps together, and
  builds an O&M check on that reading. It also says "the results" give ε and
  GOR different area behaviour, when the text gives them the same and only
  the figures differ. B has no errors.
- **Shared:** P1, P3, P4, P8 and much of P13. Both miss P5 and P10, the two
  numerical Majors.

The solo sessions put the two closer: A 6 found and 5 partial, B 4 found, 3
found in part and 5 partial, with each touching 5 of the 7 Major problems.
The head-to-head counts B about 1½ problems ahead.

**Implications for later comparisons.**

- The App's runs share two faults across efforts: both smooth the GOR/PR
  sentence, and both evaluations read Table 2's pump price as one pump.
- Codex's two close readings each lose part of the contributions: medium
  reframed contribution (b), and high drops (a) and (b) as claims.
- Both head-to-heads here chose the letters Barnett's did, close reading A
  and evaluation B, so Experiment 4 should lean on confirmed findings and the
  solos as well.

## Kanbur experiment 3 — Medium semifinal

**Matchup:** winner of Experiment 1 vs. (1) API, at medium effort.

**Overall winner:** **A — (3) Codex, medium** — Medium division champion, advances to the final

Codex narrowly wins the close reading and the API narrowly wins the
evaluation; both verdicts hold in both reading orders, and both judges call
their margin close to a tie. It is Barnett's split by letter again, close
reading to A and evaluation to B. With the two this close, the experiment's
own question decides it. [ADR-0020](adr/0020-codex-joins-experiment-2.md)
asks whether Codex reads as well as the API, since it "could analyze the
collection without the API's per-call cost". Here it does: the API's edge in
the evaluation is one Minor problem, and Codex's close reading covers more of
the article, which is what Phase 3 synthesizes. The API costs $0.551 a run;
Codex runs within the subscription.

Codex reuses Experiment 1's winning run (B).

| Run | Configuration | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- |
| **A** | Codex, medium (winner of Experiment 1) | about 7–8 min | about 3 min | not reported |
| **B** | API, medium | $0.349 · 3 min 31 s | $0.202 · 52 s | $0.551 |

### Detailed findings

**Close readings: A, narrowly.**

| | A (Codex) | B (API) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 93% at 2, 7% at 1 | 97% at 2, 3% at 1 |
| A2, contributions (4) | 4 caught | 3 caught, C-a thinned |
| A2, abstract claims (12) | 10 caught, 1 thinned, 1 missed | 10 caught, 1 thinned, 1 missed |
| A2, tables (3) | 3 read | 2 read, T3 named only |
| A3, strength of language | 1 | 1 |
| A4, verbatim · numbers · references | 0/0 · 123/123 · 47/47 | 2/2 · 124/124 · 47/47 |
| Steps · claims | 36 · 151 | 34 · 129 |

The two readings take the same path and catch the same inconsistencies in
the article. The differences, confirmed in the runs:

- **A covers more.** It records S4g.4, the thermoeconomic section's
  conclusion that levelized costs rise with the load and depend on the
  exergetic costs, which the reference list marks as one to catch. It
  records contribution (a), "neither this hybrid design nor the use of
  two-phase immersion cooling waste heat for desalination has previously been
  investigated". It reads Table 3, including its printed "c3 = u3", and says
  what Figures 7 and 10 show. B names Table 3 and those two figures without
  reading them, and has no claim for contribution (a)'s "not investigated
  before".
- **B keeps more of the author's strength.** It keeps the abstract's
  "economically feasible for real applications" and "seems sufficient". A
  drops both, the first as in Experiment 1, and turns the Conclusion's future
  work from "can be investigated" and "can be experimentally tested" into
  "should".
- **B has shifts of its own.** It drops "may be" from the authors' reason for
  the flat payback, and writes that water "provides an economic benefit that
  can offset the additional expenditure", where the article says water's
  value "can be used to understand whether" the hybrid is feasible.

Both judges score A3 at 1. The solo sessions put B ahead on A1 by one claim
in 30. The head-to-head decided on coverage of displayed elements and
section conclusions, and says a researcher weighing strength of language
first could call it a tie.

**Argument evaluations: B, narrowly.** Against the 23-problem list:

- **Found only by B:** P23 in full, the only run in Kanbur to find it so far:
  Eq. 13 "cannot independently predict flux when those outlet flows are
  themselves unknown". B also partly finds P14 and states P13's cost-rate
  point: "Minimizing SGD/hour is not equivalent to minimizing cost per cubic
  metre".
- **Found only by A:** the reason the reported ε can't come from Eq. 24, since
  flux doesn't depend on area, and more of P7 (substituting SI for ε needs a
  relationship shown beyond these trends).
- **Shared:** P1, P2, P3, P4, P8 and P22, and much of P13. Both miss P5 and
  P10, the two numerical Majors, as both Experiment 2 runs did.
- **Errors:** none in either. B prices "the additional permeate pump" at the
  950 SGD that covers both pumps, but hedges it.

The solos agree it is close: A finds 11 of the 23 at least in part, B 13,
each with 5 of the 7 Majors.

**Implications for later comparisons.**

- Codex medium's lost "for real applications" now shows in two
  head-to-heads. Its "can" → "should" habit is new here.
- Experiments 2 and 3 both split by letter the way Barnett did. Experiment
  5's two sessions with the letters swapped should show whether that's the
  judge or the runs.

## Kanbur experiment 4 — High semifinal

**Matchup:** winner of Experiment 2 vs. (1) API, at high effort.

**Overall winner:** **A — (3) Codex, high** — High division champion, advances to the final

Codex narrowly wins the close reading, and the evaluation is a tie: the judge
leaned to the API in one reading order but not the other, which the rubric
records as a tie. The close-reading solos lean the other way, toward the API
on attribution, strength of language and contributions, so the close reading
is near even too. As in Experiment 3,
[ADR-0020](adr/0020-codex-joins-experiment-2.md)'s question decides it:
Codex reads as well as the API at high effort, and the API costs $0.643 a run
where Codex runs within the subscription. Codex's close reading also keeps the
article's GOR/PR contradiction, which the API's hides.

Codex reuses Experiment 2's winning run (B).

| Run | Configuration | Close reading | Argument evaluation | Total |
| --- | --- | --- | --- | --- |
| **A** | Codex, high (winner of Experiment 2) | about 7–8 min | about 3 min | not reported |
| **B** | API, high | $0.400 · 6 min 2 s | $0.243 · 2 min 28 s | $0.643 |

### Detailed findings

**Close readings: A, narrowly, in the head-to-head; the solos favor B.** The
judge read every claim in both runs, not a sample.

| | A (Codex) | B (API) |
| --- | --- | --- |
| A1, solo (30 sampled claims) | 90% at 2, 10% at 1 | 97% at 2, 3% at 1 |
| A2, contributions (4) | 2 caught, 2 thinned (C-a, C-b) | 4 caught |
| A2, figures (10) | 9 read, 1 thin (F10) | 8 read, 2 thin (F6, F10) |
| A3, strength of language | 1 | 2 |
| A4, verbatim · numbers · references | 2/2 · 343/343 · 47/47 | 4/4 · 316/316 · 47/47 |
| Steps · claims | 37 · 158 | 37 · 173 |

The two readings take nearly the same path and flag the same four
inconsistencies in the article. The differences, confirmed in the runs:

- **B hides the GOR/PR contradiction.** It gives the article's "nearly 14
  times higher than the GOR and PR values of the minimum membrane area" as
  "a nearly fourteenfold difference … between the membrane-area extremes",
  and declines to read Figure 6, keeping the prose's "membrane-area
  preference … as stated". The App smoothed the same sentence in both of its
  runs. A records both halves and says "they point in different directions",
  then reads Figure 6's surfaces rising with area.
- **A reads more of the figures.** It says what Figures 4, 5, 6, 8 and 9 show
  where B names them, including Figure 5B's colour scale starting at 27.20
  against the prose's 27.3%.
- **A loses the contributions and invents Table 1's labels,** the same faults
  found in Experiment 2: "not investigated before" and "first time" stay in
  `moves`, and the column groups are called "total" and "vapor" heat flux
  though both are printed "qT (W/m²K)".
- **B keeps more of the article's own claims and strength words:** all four
  contributions, every Table 1 value, Table 3's "c3 = u3", "pivotal role",
  "critical importance", "dramatically", and S5.1's "can be efficiently
  operated" quoted `verbatim`. A drops "pivotal role" and "critical
  importance" and softens "dramatically".

The head-to-head weighed B's GOR/PR rewording as the more consequential
fault, since it removes the article's main internal inconsistency, and said a
researcher weighting contributions and strength of language first could
prefer B.

**Argument evaluations: a tie.** Against the 23-problem list:

- **Found only by B:** the validation's circularity (P16): matching
  Reference 31 after taking the membrane inputs from it "is primarily
  evidence that the borrowed submodel has been implemented consistently". A
  instead treats Table 1 as the paper's strongest evidence. B also gives the
  fuller P4 argument (Eq. 24's A_m multiplier against ε falling with area)
  and develops the cold permeate supply (P22) further.
- **Found only by A:** the missing comparison with other uses of the heat
  (P21): the choice of desalination "rests largely on precedents and a
  research gap", and "No comparative assessment resolves that question".
- **Shared:** P1, P4, P8, P13 and P22 in full; P2, P3, P7, P14 and P18 in
  part. The payback arithmetic is nearly identical (3.72 years of water
  revenue repays about 23 SGD). Both miss P5 and P10.
- **Errors:** none in A. B says "The authors acknowledge that distinction"
  about a broader point than the one the authors concede, a loose sentence
  rather than a misstatement.

The solos lean slightly to A: A has 8 found and 4 partial, B 6 found and 5
partial, each with 4 of the 7 Majors found and P2 in part.

**Implications for later comparisons.**

- Codex's two runs keep the GOR/PR contradiction visible; the App's two runs
  and API high hide it. Codex medium and high also both lose part of the
  contributions, and both drop or soften strength words.
- This evaluation head-to-head is the first in Kanbur that didn't choose B,
  and its close reading is the third in a row to choose A.
- The final is Codex medium against Codex high, so it answers the effort
  question for Codex.

## Kanbur experiment 5 — Final

**Matchup:** Medium champion vs. High champion: Codex medium (winner of
Experiment 3) vs. Codex high (winner of Experiment 4).

**Overall winner:** **GPT-6.1 Sol medium through Codex** — champion

Codex medium wins both head-to-heads in both sessions: as A in session AB
and as B in session BA. Every margin is narrow, but none of the four verdicts
followed the letter. Higher effort doesn't buy a better reading or
evaluation of this article, and the two take about the same time.

Both runs were judged alone in Experiments 3 and 4, so this experiment has
only the head-to-heads, each run in two sessions with the letters swapped.

| Session | A | B | Close reading | Evaluation |
| --- | --- | --- | --- | --- |
| AB | Medium champion | High champion | **A** (medium), narrowly | **A** (medium), narrowly |
| BA | High champion | Medium champion | **B** (medium), narrowly | **B** (medium), narrowly |

A configuration wins a head-to-head only if it wins both sessions. If the
sessions split, each verdict followed its letter, and the head-to-head is a
tie, decided on the findings both sessions confirm in the runs.

| Run | Session AB | Session BA | Close reading | Argument evaluation |
| --- | --- | --- | --- | --- |
| Codex, medium (winner of Experiment 3) | **A** | **B** | about 7–8 min | about 3 min |
| Codex, high (winner of Experiment 4) | **B** | **A** | about 7–8 min | about 3 min |

### Detailed findings

**Close readings: medium, narrowly, in both sessions.** Both judges decided
on the same difference, and both called the margin small enough that a
researcher could call it a tie.

- **Medium records the article's novelty claims; high doesn't.** Medium has
  all four contributions, including "neither this hybrid design nor the use
  of two-phase immersion cooling waste heat for desalination has previously
  been investigated", and the Conclusion's "first time" and "for further
  real-scale demonstrations". High's step 4 calls the contributions a
  restatement of the Summary, which doesn't contain them, so they never
  become claims. Found in Experiments 2 and 4 too.
- **High adds Table 1 labels the table doesn't print** ("total" and "vapor"
  heat flux, where both columns are headed "q^T (W/m²K)"). Medium records the
  duplicate header and Table 3's "c3 = u3" as printed.
- **High has the abstract's side.** It records AB1, AB6 and "economically
  feasible for real applications", which medium drops, as it did in
  Experiments 1 and 3. Each run keeps one half of the abstract-to-Conclusion
  scope shift; neither sets the two side by side.
- **Medium misframes contribution (b)** as DCMD being "a new
  clean-water-producing alternative", where the article says "a new
  alternative to the data center cooling systems". Found in Experiments 1
  and 3.
- **Both keep the GOR/PR contradiction and read Figure 6 rising with area**,
  the thing the App's runs and API high hid.

**Argument evaluations: medium, narrowly, in both sessions.** Against the
23-problem list:

- **Found only by medium:** the validation's circularity (P16): the DCMD
  check "uses the same reference that supplies important module
  characteristics", where high calls Table 1 "meaningful support". Medium's
  P4 rests on the model itself: flux doesn't depend on area, so Eq. 24 must
  rise with area while Figure 5B falls. High's rests on Figure 6A, which the
  article's text contradicts (P5). Medium also challenges the advice to use
  SI in place of ε (P7) and notes the cost equations' missing time
  conversions.
- **Found only by high:** the explicit bound for P1 (3.72 years of the
  water's value repays only about 22.8 SGD), the cost-rate mechanism behind
  the small-area optimum (P13), and the optimum's false precision (part of
  P14).
- **Shared:** P1–P4, P8, P13 and P22; both miss P5 and P10.
- **Errors:** none in medium. Session AB found one small imprecision in
  high: it sets Table 2's 950 SGD, which covers both pumps, against the added
  pumping equipment. Session BA found none.

**Bottom line.** For the second article in a row, Sol medium is the
configuration selected, and here the verdicts back it with the letters both
ways. Its known faults are the scope conditions it drops from headline
claims: "for real applications" here, the open-loop condition in Barnett.

## Kanbur run records

### Cost and usage

Only the API reports usage. Its costs use the same GPT-6.1 Sol rates as
Barnett's. The App reports nothing. Codex, on the ChatGPT Pro plan, reports no
tokens: its four sessions took the times above and used about 1% of the weekly
limit. The API runs also wrote a primer, which isn't judged and isn't in these
costs.

| API run | Input tokens | Output tokens | Reasoning tokens |
| --- | --- | --- | --- |
| Medium close reading | 72,234 | 20,466 | 283 |
| Medium evaluation | 90,992 | 2,012 | 120 |
| High close reading | 72,234 | 25,545 | 1,988 |
| High evaluation | 94,366 | 5,449 | 3,624 |

### Shared setup and run sources

The article is `data/research/ab_testing/kanbur_et_al_2020_desalination_integrated_data_center_cooling.pdf`.
All runs are in
`outputs/ab_testing/kanbur_et_al_2020_desalination_integrated_data_center_cooling/`.
Judgments go in `outputs/judgments/kanbur/`, with the reference lists in
`references/` and each experiment's judgments in its own folder.

The runs came out in different shapes. The API's files are JSON with an id and
a provenance block, while the App's and Codex's are a bare `analysis.json` with
no id and an `argument_evaluation.md`. Side by side, a judge could tell the API
run apart and couldn't record an id for the others. So the judging folders use
uniform copies in `outputs/judgments/kanbur/runs/<configuration>/`: each run
as `analysis.json` (`id` and `content`) and `argument_evaluation.json` (`id`,
`analysis_id`, and `content.evaluation`), with no provenance. The API copies
keep their original ids; the App and Codex copies have ids assigned here. The
content is unchanged, and the originals are untouched.

| Copy | Original | `analysis.json` id | Argument evaluation id |
| --- | --- | --- | --- |
| `runs/api_medium/` | `adr_0017/pdf__gpt-6.1-sol-medium/` | `7f044bce-0cae-4472-a887-d01646c0092e` | `9d417ada-ee4c-4172-9a85-9dd108361e4f` |
| `runs/api_high/` | `adr_0017/pdf__gpt-6.1-sol-high/` | `2a82aff3-14e1-4c82-a830-1c9118ce5847` | `e5f3697e-2fdd-4056-9060-e9bb430465d0` |
| `runs/app_medium/` | `adr_0017/app__gpt-6.1-sol-medium-work/` | `5698e6b9-8d5f-4379-84d8-875a9247895c` | `279c062d-f752-4114-bf60-dcc9e9d058f0` |
| `runs/app_high/` | `adr_0017/app__gpt-6.1-sol-high-work/` | `b050b54f-75ac-4a51-be4e-eceacaea58e8` | `354aac17-6f8d-4355-8ab3-74e9ca6841da` |
| `runs/codex_medium/` | `adr_0020/codex__gpt-6.1-sol-medium/` | `3686ad7a-7dc2-4c56-a379-39e00b79c243` | `8dd71213-5808-4dd1-adf8-9191fe4640c0` |
| `runs/codex_high/` | `adr_0020/codex__gpt-6.1-sol-high/` | `fa401e5e-ea12-498b-9ccb-24aa8aa410fa` | `dd922c0a-e4a0-40f2-a411-13b0a541f3fe` |

### Setting up a kanbur judging folder

1. Copy in `RUBRIC.md`, `prompts/`, and the article as `article.pdf`.
2. For each letter, copy the run's two files, `analysis.json` and
   `argument_evaluation.json`, from `outputs/judgments/kanbur/runs/<configuration>/`
   into `runs/A/` or `runs/B/`. Copy only the files: the copies' folder names
   say which configuration they are.
3. Never copy Codex's `run_note.md`. It says how Codex read the PDF and names
   its configuration.
4. **Experiment 1:** start with an empty `references/` and run all eight
   prompts; prompts 1 and 5 write kanbur's reference lists. Copy
   `references/` back to `outputs/judgments/kanbur/references/`.
5. **Experiments 2–4:** copy `outputs/judgments/kanbur/references/` in as
   `references/`, skip prompts 1 and 5, and run the other six.
6. **Experiment 5:** both runs were judged alone in Experiments 3 and 4, so
   run only prompts 4 and 8, the two head-to-heads, in two sessions. Session
   AB puts the Medium champion under A; session BA swaps the letters. Name
   each judgment by its session: `close_reading_head_to_head_AB.md` and
   `_BA.md`, `evaluation_head_to_head_AB.md` and `_BA.md`.
7. Record the letters in this key, and check the ids each judgment records
   against the table above.
8. Copy only `judgments/` back, into the experiment's folder below.

| Experiment | Judgments folder |
| --- | --- |
| 1 | `outputs/judgments/kanbur/exp1_kanbur_medium_app_vs_codex/` |
| 2 | `outputs/judgments/kanbur/exp2_kanbur_high_app_vs_codex/` |
| 3 | `outputs/judgments/kanbur/exp3_kanbur_medium_winner_vs_api/` |
| 4 | `outputs/judgments/kanbur/exp4_kanbur_high_winner_vs_api/` |
| 5 | `outputs/judgments/kanbur/exp5_kanbur_medium_vs_high/` |
