# Close readings, head to head — runs A and B

**Article:** Kanbur, Wu, Duan, "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system," *Int J Energy Res* 2020;44:10453–10470.

**Read for this session:** `RUBRIC.md`, `prompts/close-reading.md`, `article.pdf` (I extracted the text with pypdf and rendered Table 1 as an image to check its headers), `references/claims_reference.md`, `runs/A/analysis.json`, `runs/B/analysis.json`. I did not open any other judgment or any argument evaluation.

## Run ids

| Run | `id` |
| --- | --- |
| A | `3686ad7a-7dc2-4c56-a379-39e00b79c243` |
| B | `fa401e5e-ea12-498b-9ccb-24aa8aa410fa` |

## Shape of the two readings

| | A | B |
| --- | --- | --- |
| Steps | 36 | 37 |
| Claims | 151 | 158 |
| Support items | 88 | 111 |
| Claims marked `verbatim` | 0 | 2 |
| Support items marked `verbatim` | 0 | 0 |
| Where it stops | Appendices A–C (end of article) | Appendices A–C (end of article) |

The two readings are very close. They break the article at almost the same points, record nearly the same claims in the same order, and both flag the article's internal inconsistencies (2.15× vs 1.5× COP; the nearly 65% drop vs 1.85×; 5.12 vs 5.13 cm²; Eq 24 printed the same as Eq 22; the GOR/PR area wording against Figure 6). Both leave those inconsistencies unresolved, which is what the prompt asks for. The differences are at the margins, so this comparison is mostly about those margins.

## What each caught that the other missed (against `claims_reference.md`)

### Caught by A, missed by B

- **C-a and C-b, the novelty contributions.** A4 C0 records that "neither this hybrid design nor the use of two-phase immersion cooling waste heat for desalination has previously been investigated," and A4 C1 records contribution (b)'s low-load alternative (with a framing slip; see below). B4 records only C-c, the exergy-cost matrix (B4 C4). Its `moves` say "the four contributions restate the novelty and methods already announced in the Summary," but the Summary never says "first time" or "has not been investigated before," and it never mentions the low-load emphasis. I found no claim in B that records the article's novelty claim. C-d (optimization objectives and bounds) is caught later in B20, so B gets 2 of 4 contributions where A gets 4.
- **S5.0a, "It was the first time combining the desalination unit with the two-phase liquid-immersion cooling operation."** A31 C0 records it. B30 treats it as restatement in `moves` and records no claim.
- **C-5.5, the conclusion's feasibility wording.** A32 C0: "economically feasible for further real-scale demonstrations." B31 mentions "restate economic feasibility" in `moves` only. The reference flags the shift between this wording and the abstract's "for real applications" (AB10). A records the conclusion's version and B records the abstract's, so neither run puts both in front of the reader.
- **Table 3's printed auxiliary "c3 = u3"** on the permeate-pump row. A20 records it as printed. B19 summarizes Table 3 without it.
- **Figure 10 read for direction.** A30 says the frontiers rise (cost increases with exergy efficiency) and that the water-cost frontier lies below the product-cost frontier, which matches F10. B29 says only "separate Pareto point sets and two labeled trade-off points."
- **S4f.1 stated as a claim.** A28 C0 puts "around 3.72 years, much shorter than the assumed 20-year system life" in the claim. B27's claims never state 3.72 years or the comparison with the 20-year life. The number appears only in its `meaning` and in the Figure 8 axis reading.
- **C-5.7 in full.** A32 C1 gives 2.69–5.33 SGD/h and 64.6–127.9 SGD/day. B31 C0 gives the daily figures as a claim and the hourly range only in support.
- **Reference-list oddities.** A34 notes that entries 16 and 17 print the same title under different authors, and that entry 25 prints "cooing." That isn't required, but it's accurate and useful for the "never complete a reference" rule.

### Caught by B, missed by A

- **AB1**, the framing premise that waste-heat management "has a significant share in the energy-efficient operations." B0 C0 records it. A0 doesn't.
- **AB6**, the abstract's method claim (thermodynamic, economic and thermoeconomic assessment via the design's own exergy-cost matrix). B0 C3 records it. A0 doesn't, though A records the matrix later as C-c (A4 C2).
- **AB10's scope, "for real applications."** B0 C7 keeps it. A0 C3 shortens it to "evidence of economic feasibility" (see errors).
- **Figure 5B's colour scale against the prose.** B24 notes that the scale's lowest label is 27.20 while the text gives a 27.3% minimum, and keeps both. That's a real printed discrepancy, and A doesn't mention it.
- **Projection status of the 70 TWh figure.** B1 C1 support says it is "a near-future projection, rather than a measured 2020 result," which keeps the article's "near-future projections" qualifier. A1 C0 support also says "a projection," so this is a small edge at most.
- **Two exact quotations.** B0 C4 and B15 C1 (the S3.2d concession that the hybrid can't yet be validated) are both verbatim and both check out. A marks nothing as verbatim, though the prompt asks for the author's own words "where you can." That isn't a fidelity fault, since every A marker is honest, but A gives up exact wording at the places where the article's strength of language matters most.

### Coverage by reference category

| Type | A caught | B caught | Notes |
| --- | --- | --- | --- |
| Contributions (4) | 4 (C-b altered) | 2 (C-c, C-d) | B misses C-a and C-b. |
| Abstract claims (12) | 10 | 12 | A misses AB1 and AB6; AB10 is shortened. |
| Overall conclusions (8) | C-5.1, 5.2, 5.5, 5.7 as claims; 5.3, 5.4, 5.6, 5.8 named as restatements | C-5.1, 5.2, 5.7 as claims; 5.3–5.6, 5.8 named as restatements | Neither records C-5.6's "lower exergetic costs" reason as a claim, so neither surfaces its conflict with S4g.3's capital-cost reason. |
| Key section conclusions listed in the reference | All | All except the novelty strand | Both catch S1.10, S2.3, S2.5, S3.1d, S3.2b, S3.2d, S3.3c, S3.3f, S3.4d, S3.5c, S4a–S4h. |
| Figures (10) | 10, all read | 10, all read | A reads F10 more fully; B notes F5B's 27.20 label. Neither notes that F9's axes say "$/h" while the text says SGD/h. |
| Tables (3) | 3 | 3 | A reads T3 more closely. B's T1 reading adds labels (below). |

## Where each is wrong that the other isn't

### A

1. **A4 C1 misframes contribution (b).** The article says this "brings a new alternative to the data center cooling systems, especially for low DC cooling loads." A writes "They present direct contact membrane distillation as a new clean-water-producing alternative, especially at low cooling loads." That changes what the new alternative is an alternative to. It is supported but altered, an A1 score of 1.
2. **A0 C3 drops the abstract's scope.** "the authors take its reported 3.72-year payback as evidence of economic feasibility" loses "for real applications." The reference marks that phrase as the stronger of the article's two feasibility wordings, so dropping it softens the abstract (A1 1, A3).

### B

1. **B14's reading of Table 1 adds column identities the table doesn't print.** B says Table 1 lists relative differences "for total heat flux … and for vapor heat flux." I rendered the table: both flux columns are headed "q^T (W/m²K)," the same symbol and the same (odd) unit, and nothing names one of them "vapor." B's labels are a plausible inference, but they're recorded as what the table lists and the duplicate header isn't mentioned. A14 records the duplicate header as printed. Under A1 this is a 1, not a 0, because the numbers themselves are right.
2. **B4's `moves` mischaracterizes the contributions paragraph** as a restatement of the Summary. That's the run's own reading, not a claim field, so it isn't a misattribution. It is the reason B drops the novelty claims, though, so it counts as a reading error with a coverage cost.

Neither run puts its own inference into a claim field anywhere I checked. Both attribute the authors' inferences ("the authors infer…", "according to the authors") and keep their own interpretation in `meaning`.

## Criteria as grounds

- **A1 (attribution fidelity).** I compared the parallel steps claim by claim rather than drawing a fresh 30-claim sample; the rubric doesn't require rescoring in this session. Both runs score 2 on the great majority of claims. Each has one or two claims at 1, listed above, and I found no claim at 0 in either. All 2 of B's `verbatim` markers are honest. A has no `verbatim` markers.
- **A2 (coverage).** This is the main difference between the runs. B is more complete on the abstract (12/12 against A's 10/12). A is more complete on the enumerated contributions (4/4 against B's 2/4) and on the conclusion's own wording (S5.0a, C-5.5). The novelty claim is the article's headline claim: it appears as contributions (a) and (b) and again in the Conclusion. Missing it costs more than missing AB1 (a framing premise) and AB6 (a method note A records elsewhere).
- **A3 (strength of language).** The pattern is the same in both: hedges survive ("may not be efficient," "as far as we know," "can be useful," "may be due to"), and so do strong words ("crucial," "pivotal," "very good agreement"). Both soften the same few spots: "dramatically increase" becomes "strongly"; "seems sufficient" becomes "considered/regarded as sufficient"; "clearly infer" is dropped. A also softens AB10. Both runs sit at the upper end of 1, with A very slightly weaker.
- **A4 (mechanical checks).**

  | Check | A | B |
  | --- | --- | --- |
  | Verbatim texts found in the article | 0 / 0 | 2 / 2 |
  | Numbers in claim and support text found in the article | 215 / 215 | 228 / 228 |
  | Reference entries matching the article's list | 74 / 74 | 74 / 74 |

  My script flagged 11 entries per run, the same 11 in both. Each was a line-wrap hyphenation artifact of my normalizer (e.g. "674-⏎691"), and I confirmed every one by eye against the printed list. Both runs copy entry 17 exactly as printed, though it carries entry 16's title. Image readings checked by eye: both runs read Figure 6 as rising toward larger area and Figure 8 as a slight rise with area on a 3.719–3.727 axis, and both match the page. B's Table 1 labels are the one image reading in either run that adds something not printed.
- **A5 (detail and readability).** Both are evenly paced, and either one alone would let a reader follow the article's argument. B has 23 more support items, but most of the extra ones split citations one per item or say "this paraphrases Equation N." That makes B more granular but adds little substance. B also spends three steps on the appendices where A uses one. A's `meaning` fields track the argument's turns slightly more pointedly (for example, that the move to desalination is analogical, and that the optimum depends on the equal-weight rule). B's do the same work in plainer terms. On readability they're roughly equal.

## Verdict

**A is better, by a narrow margin.**

The decisive difference is A2 coverage of the article's central contribution claim. A records the novelty contributions (a) and (b), the Conclusion's "first time" claim, and the Conclusion's narrower feasibility wording. B leaves out all three, because it read the contributions paragraph as a restatement of the Summary when the Summary contains none of those claims. B's advantages are real but smaller: the two abstract claims A drops, AB10's scope, the Figure 5B 27.20/27.3 discrepancy, and two correct quotations. On A1 each run has about one altered claim of comparable weight: A's misframed contribution (b), and B's unprinted Table 1 labels. A3, A4 and A5 come out essentially even.

The margin is small. A researcher who weights abstract completeness above enumerated contributions could reasonably call it a tie.

## Order check

- **Reading A first, then B.** A sets the baseline as a complete, all-paraphrase reading. Against it, B's omission of contributions (a) and (b) and of the Conclusion's "first time" and "further real-scale demonstrations" stands out. B's abstract completeness, verbatim quotes and F5B note register as smaller gains. Verdict: A, narrowly.
- **Reading B first, then A.** B sets the baseline as a complete abstract with two exact quotations and very granular citations. Against it, A's missing AB1 and AB6 and its total lack of quotation stand out first. Then the contributions paragraph comes up, and A has the novelty claims that B never recorded. A also has the T3 anomaly, the fuller F10 reading, and the duplicate q^T header recorded correctly where B added labels. The contribution gap still outweighs the abstract gap. Verdict: A, narrowly.

**The verdict held in both orders:** A is better, by a narrow margin.
