# Close readings, head to head — runs A and B

**Article:** Kanbur, Wu, Duan, "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system," *Int J Energy Res* 2020;44:10453–10470.

**Read for this session:** `RUBRIC.md`, `prompts/close-reading.md`, `article.pdf` (text extracted with macOS PDFKit, figures checked against the reference list's descriptions), `references/claims_reference.md`, `runs/A/analysis.json`, `runs/B/analysis.json`. No other judgment or argument evaluation was opened.

## Run ids

| Run | `id` |
| --- | --- |
| A | `5698e6b9-8d5f-4379-84d8-875a9247895c` |
| B | `3686ad7a-7dc2-4c56-a379-39e00b79c243` |

## Shape of the two readings

| | A | B |
| --- | --- | --- |
| Steps | 46 (38 on Summary–Section 5; 8 on nomenclature, acknowledgments, references, appendices) | 36 (33 on Summary–Section 5; 3 on apparatus) |
| Claims / support items | 147 / 66 | 151 / 88 |
| `verbatim` claims / support | 2 / 0 | 0 / 0 |
| Where it stops | End of Appendix C (whole document) | End of Appendix C (whole document) |

Both runs follow the article in order. Both paraphrase almost everything. Neither stops early.

## Mechanical checks (A4), both runs

I checked these with a script against the extracted text. For entries and verbatim strings, whitespace and line-break hyphens were normalized. For numbers, digit groups printed with a thin space (e.g. "10 495.00") were joined.

| Check | A | B |
| --- | --- | --- |
| Verbatim texts found in article | 2 / 2 (abstract opening sentence; acknowledgment) | 0 / 0 (none marked) |
| Numbers found in article text | 311 / 311 | 318 / 318 |
| Reference entries matching the article's list | 47 / 47 unique entries (65 uses) | 47 / 47 unique entries (74 uses) |
| Citation numbers mapped to the right entry | All checked uses correct; both reproduce the article's own duplicate title for refs 16/17 | Same; B also notes the 16/17 duplicate and "cooing" in ref 25 as source peculiarities |

Neither run invented or completed a reference. On this criterion they are effectively tied.

Image readings are reported separately, since they are paraphrases. Both runs mark them as paraphrased and name the element. Both read Figure 6 against the prose's "highest at the minimum membrane area." Both runs report the plotted surfaces rising toward *larger* area, which matches the reference's F6 note. B's reading of Figure 8 ("small increase with membrane area" on a 3.719–3.727 axis) matches F8. A gives the axis range but declines to read a direction. Neither run notes that Figure 9's axes are labelled $/h while the text reports SGD/h.

## What each caught that the other missed (A2, against `claims_reference.md`)

### Caught by A, missed or weakened by B

- **AB1**: the framing premise that waste-heat management "has a significant share in the energy-efficient operations of the data centers." A records it verbatim (C1.1). B has no claim for it.
- **AB6**: the method statement that the system is assessed thermodynamically, economically and thermoeconomically, using a system-specific exergy-cost matrix. A records it (C1.4). B's Summary step has no claim for it; it appears only in B's `meaning`.
- **AB10's scope**: A keeps "economically feasible **for real applications**" (C1.6). B's C1.4 drops the scope ("evidence of economic feasibility"). That matters because the Conclusion words the same result as feasible "for further real-scale demonstrations."
- **T1 values**: A gives every current/reference pair in Table 1 (U and both flux columns at 40–70 °C), along with the relative differences. All values check against the table. B gives only the relative differences.

### Caught by B, missed or weakened by A

- **C-b, the second half**: the contribution "brings a new alternative to the data center cooling systems, especially for low DC cooling loads." B records it (C5.2), slightly misdirected (see below). A merges contributions (a) and (b) into one novelty claim (C6.1) and drops this sentence. A also drops (a)'s "clean water production can be achieved."
- **S1.3**: the analogy's conclusion, that the combination "has also a strong potential for the real-scale systems." B records it (C3.4). A keeps only the "can be efficiently combined / sufficient energy" half (C4.2).
- **S1.6's hedge**: "as far as we know." B keeps it (C3.6, "as far as the authors know"). A drops it and turns "usually" into "largely" (C4.4).
- **C-5.5**: the Conclusion's version of feasibility, "for further real-scale demonstrations." B records it as a claim (C33.1). A treats the payback bullet as a pure restatement in `meaning`, so the shift in wording from the abstract is lost.
- **S4d.1, both halves**: B records both contradictory halves of the GOR/PR sentence explicitly ("highest at the minimum membrane area" and "maximum … nearly 14 times the values at the minimum area") and says it keeps both as printed (C27.1). A's C30.1 smooths the second half into "differ by nearly a factor of 14 across the membrane-area range," which hides the conflict. A does still record the figure reading separately.
- **S4f.2**: "the PP is assumed constant." B records it (C29.4); A covers the hedge but not this sentence.
- **T3**: B records the auxiliary relations, including the printed "c3 = u3" on the permeate-pump line, and keeps it as printed (C21.2 support). A describes Table 3 only in general terms.
- **Figures read, not just named**: B reads what F4 (water rises with both area and heat), F5B (ε favors small area and high load), F7 (high-load series outside lower-load series), F9B (ordering of the three costs) and F10 (both fronts rising, water-cost front below product-cost front) show. A names F4, F5B, F7 and F10 but doesn't say what they show; for F9B its *claim* gives the ordering but its support only names the chart.

### Missed by both

- **C-5.3**'s "drastically affected" (exergy efficiency vs membrane area) is not recorded by either run.
- **C-5.6**'s reason: the Conclusion attributes DCMD's lowest levelized cost to "lower exergetic costs," while Section 4 (S4g.3) gives lower capital cost. Both runs file the bullet as a restatement in `meaning` and miss the change.
- **C-5.1**'s "crucially increased" heat and mass fluxes is not recorded as a claim by either run (both record its COP half).
- Both runs flag the COP (2.15× vs 1.5×), water (≈65% vs 1.85×) and membrane-area (5.12 vs 5.13 cm²) discrepancies. Both keep each number at its own location without reconciling them, as the reference list asks.

### Coverage tally

| Type | A: caught / without what it shows / missed | B: caught / without what it shows / missed |
| --- | --- | --- |
| Contributions (4) | 2 / 2 (C-a, C-b partial) / 0 | 4 / 0 / 0 (C-b slightly misdirected) |
| Abstract claims (12) | 11 / 0 / 1 (AB2's "reduce the cost drawback" aim) | 10 / 0 / 2 (AB1, AB6) |
| Overall conclusions (8) | 3 recorded as claims (C-5.1 COP, C-5.2, C-5.7); 5 treated as restatements, of which C-5.5 and C-5.6 are not pure restatements | 4 recorded (C-5.1 COP, C-5.2, C-5.5, C-5.7); 4 as restatements, C-5.6 not a pure one |
| Figures (10) | 6 read (F1, F2, F3, F5A, F6, F9A), F8 axis only; 4 named only (F4, F5B, F7, F10); F9B ordering via claim | 10 read (F8 with direction) |
| Tables (3) | T1 full values, T2 full, T3 general | T1 differences only, T2 full, T3 with printed auxiliary relations |

Both catch the section conclusions the reference singles out. These are S1.10, S2.3, S2.5, S3.1d, S3.2b, S3.2d, S3.3c, S3.3f, S3.4d, S3.5c, S4a.1, S4b.1–2, S4c.1–2, S4d.1, S4e.3, S4f.1–2, S4g.3–4 and S4h.2–5.

## Where each is wrong that the other isn't (A1, A3)

I didn't draw a formal seeded A1 sample here, because the per-run sessions do that. Instead I read every claim and support item in both runs against its passage. The errors that separate the runs are these.

### A

- **T1 units altered.** The support for C17.2 says the flux columns are "in W/m²." The table prints both flux columns as "q^T (W/m²K)." This is a silent correction of the printed unit, which the prompt asks runs not to make. Score 1.
- **Hedge dropped.** C20.3 has "The authors regard simple payback as sufficient," while the article says it "seems sufficient." (B makes the same error; see below.) C4.4 drops "as far as we know." Score 1 each.
- **S4d.1 smoothed.** C30.1 rewrites the self-contradictory 14× clause into a neutral "differ by a factor of 14 across the range." Score 1.
- **Run's own observations in support fields.** C4.2 ("no data center-specific calculation is presented at this point"), C30.2 ("numerical pump-curve data are not supplied") and C38.1 ("grounded in … calculated outcomes rather than an integrated-system experiment") are the run's own remarks, but they sit where the author's evidence belongs.

### B

- **AB10's scope stripped.** C1.4 drops "for real applications." The abstract claim is the strongest feasibility statement in the article, and B weakens it. Score 1.
- **C-b misdirected.** C5.2 says the authors "present direct contact membrane distillation as a new clean-water-producing alternative," but the article says the first-time use "brings a new alternative to the data center cooling systems." The object of "alternative" has changed. Score 1.
- **Hedge dropped.** C17.4 "Simple payback is considered sufficient," also dropping "seems." This is shared with A.
- **Loose attribution.** C8.1's support attaches the feed and permeate velocities to Reference 31. The article cites Reference 31 for the DCMD heat and mass transfer characteristics and the membrane properties; the velocities are stated by the authors. Score 1.
- **Run's own observations in support fields.** These include C3.3 ("without reproducing their performance calculations"), C6.5 ("rather than an experiment of this hybrid"), and the cross-references in the C32.2, C32.3 and C33.2 supports. Most are flagged as the run's reading, but they still sit in support. B does this slightly more often than A.

Neither run records its own inference as a *claim*. Neither has a 0-level error, meaning an invented claim or a false verbatim. On A3, both are inconsistent rather than one-directional. A is better on AB10's scope. B is better on S1.3's "strong potential," S1.6's "as far as we know," and the S4d.1 contradiction. Both soften S3.3c. I'd put both at 1. B's lapses touch fewer of the author's strength markers, but its one lapse is on the article's headline feasibility claim.

## Detail and readability (A5)

A covers the main text in 38 steps and B in 33, both fairly evenly; each lingers appropriately on the modeling equations. A spends 8 steps on apparatus, three of them reference-list steps with no claims. That is accurate but adds little. B handles the same material in 3 steps.

B's supports often give the displayed equation in paraphrased form (Eqs 5–7, 13, 14, 18–26, 36), marked as readings. This makes the model easier to follow from the reading alone. A describes equations in words, which is faithful but harder to check.

Someone could follow the article's argument from either reading. B's is somewhat more self-sufficient on the results section because it reads the figures.

## Verdict

**B is the better close reading, by a modest margin.**

On coverage (A2), B records all four contributions as distinct claims. It also catches S1.3's "strong potential" and C-5.5's changed feasibility wording, keeps both halves of the GOR/PR contradiction, records Table 3's printed auxiliaries, and reads all ten figures where A only names four of them. A's coverage advantages are narrower: AB1, AB6 and the full Table 1 values.

On strength of language (A3), B keeps more of the article's hedges. Its main lapse (AB10's scope) is real, but A has a matching set of smaller lapses, including a unit change in Table 1.

The mechanical checks (A4) are a tie. On attribution (A1), both runs have only 1-level alterations, of similar number. On A5, B is tighter and makes the argument easier to follow.

Where A is better, it is on specific items: AB10's scope, AB1/AB6, and full Table 1 values. Where B is better, it is on whole categories: figure readings, contributions, and conclusion wording that changes from the body. That is why the verdict goes to B.

## Order check

- **A first, then B.** A reads as careful and faithful, with a complete Table 1 and conservative figure handling. Reading B afterwards, its added figure readings, its separate contributions, C-5.5, and the S1.3 and S1.6 hedges outweigh what it loses (AB1, AB6, AB10's scope). Verdict: B.
- **B first, then A.** B sets the baseline. A then adds AB1, AB6, AB10's scope and the Table 1 values. But it reads four figures less, merges two contributions, misses C-5.5's wording, smooths S4d.1, and changes Table 1's units. Verdict: B.

The verdict held in both orders: B is better. The margin is modest, and a researcher spot-checking should look first at figure handling (where B's advantage is clearest) and at AB10/C-5.5 (where each run gets one half right).
