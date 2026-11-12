# Judgment — close reading (A1–A5)

**Article:** `article.pdf`. Katakam, Arzumanyan, Lin, Bahadur, "System-scale design and analysis of desalination systems for meeting water needs of data centers", *Water Research* 308 (2027) 126748. 20 pages.

**Run judged:** `run/analysis.json` (25 steps, 122 claims, 89 support items, 170 citation records).

**Seed:** `20261107`. Python `random.seed(20261107); random.sample(all_claim_ids, 30)`, drawn over every claim in reading order (`C<step>.<claim>`, both 0-based).

**How I checked:** I took the article text out with `pypdf` and checked every verbatim, number and reference entry against it by script. Dashes, quote marks and whitespace were normalised, and I allowed for extraction artifacts such as `Ya˜ nez` for Yañez, the `fl` ligature, and a reference entry split by a page footer. I rendered pp. 9–17 with PyMuPDF and checked figure readings by eye against Figs. 3–7. I used `references/claims_reference.md` as written. I did not open `run/argument_evaluation.md` or anything else in `judgments/`.

---

## A1. Attribution fidelity

Each sampled claim and support item was scored against the passage its step's `location` names. I found every passage.

| Score | Claims (n = 30) | Support items (n = 22) |
| --- | --- | --- |
| 2 | 28 (93%) | 20 (91%) |
| 1 | 2 (7%) | 2 (9%) |
| 0 | 0 (0%) | 0 (0%) |

### Per-claim scores

| ID | Form | Claim | Support | Note |
| --- | --- | --- | --- | --- |
| C0.4 | para | 2 | S0: 2 | Abstract SWUI claims (novel, 2023–2030 rise, −40%) are faithful. S0 accurately reports Highlight H5, but the author doesn't offer it as evidence for this claim. It's a placement problem (A5), not an attribution one. |
| C1.2 | para | 2 | — | "would count as direct use" became "counts as direct use". Here "would" is conditional on such cases, not a hedge. |
| C1.3 | para | 2 | S0: 2 | PUE/WUE definitions as printed (p. 3). Citations as printed. |
| C3.0 | para | 2 | S0: 2 | RO "cannot effectively treat … >50,000 ppm … with substantial freshwater recovery" is kept, with its causes. |
| C3.2 | para | 2 | S0: 2 | SIE "substantially improve … operational stability till zero-liquid discharge limits" is kept. The three "Ding et al., 2026" citations are matched to 2026a/b/c in the right order. |
| C3.3 | para | 2 | S0: 2, S1: 2 | Conventional discharge "poses ecological risks", and MLD "minimizing disposal volumes and reducing contamination potential" (pp. 3–4). |
| C3.4 | para | 2 | S0: 2 | ZLD claim is faithful. "particularly attractive" became "attractive", which is trivial. |
| C4.3 | para | **1** | S0: **1** | **Hedge added.** The article says "These studies further rely on simplified first-principle models…" categorically (p. 4). The reading has them "often" simplify, carrying the "often" from the later cost-exclusion clause over the whole claim. **Support:** "The authors contrast limited or low recovery operating points with their intended sweep" is the model's framing. The passage makes no contrast with the study's own sweep. The citations are correct. |
| C4.6 | verb | 2 | — | Exact (p. 4). |
| C5.0 | para | 2 | S0: 2 | Single feed/recovery, and the Tucker et al. criticisms, are as printed. Citation text: see A4 (one printed group split). |
| C5.5 | para | 2 | — | Pre-/post-treatment and concentrate costs "each updated for present-day costs". "holistically" was dropped, which is immaterial. |
| C5.8 | para | **1** | — | **Certainty softened.** The article says facility-specific data "will extend the present system-level integration … and improve the translational water-stress impact evaluation models" (p. 4). The reading says they "could extend … and improve". |
| C6.2 | para | 2 | S0: 2 | Eq. (3) is read as printed (ratio × 1000 / ρp). |
| C7.5 | para | 2 | S0: 2 | 2.5% / 4.8% / <0.06 kWh/m³, and the 0.5–3 bar, 30% → ~75,000 ppm conditions, are all kept (p. 6). |
| C8.2 | para | 2 | S0: 2 | Intercooling PR optimisation and the 5% allowance on Winp and on every heat exchanger (p. 6). |
| C9.3 | para | 2 | S0: 2 | MVC capex/opex items, including the pretreatment exclusion in the hybrid, and the TTD sweep (p. 7). |
| C12.1 | para | 2 | S0: 2 | Every Table 1 RO/MVC value matches, including "50 K" as printed. |
| C12.2 | para | 2 | S0: 2 | Every Table 1 techno-economic value matches. |
| C12.3 | para | 2 | S0: 2 | Every Table 1 cost parameter matches. |
| C13.3 | para | 2 | S0: **1** | The claim is a fair summary of the WUE-range justification (p. 10). **Support:** "The authors use the LBNL profiles rather than assigning a measured facility-specific WUE" adds a contrast the passage doesn't draw. |
| C15.3 | para | 2 | S0: 2 | "highly sensitive", "about 50–400%", "almost an order of magnitude" and "clearly highlights" are all kept (p. 11). |
| C16.2 | para | 2 | S0: 2 | The 91,000 ppm WC dip and the 50,000 ppm analogue (p. 11). The support values (300→547 L, $11.1→$10.8) were checked against Fig. 4a/c by eye and are correct. |
| C17.0 | para | 2 | — | The two worked cases and why they were chosen (p. 11). |
| C18.1 | para | 2 | S0: 2 | The Monte Carlo text ranking is reproduced, as is "corroborates". The Fig. 5c reading is correct by eye. |
| C20.1 | para | 2 | S0: 2 | "mainly due to rising WUE" and Case 1 "only reaches moderate" are kept. The printed "931.2 L/kg-feed" is given as "about 931 L/1,000 kg", and the unit change is disclosed in the step's `meaning`. The Fig. 7b range of 1.0–2.2 is correct. |
| C20.4 | verb | 2 | — | Exact (p. 14). |
| C22.0 | para | 2 | — | The caveats are faithful (p. 16). "do not imply that seawater withdrawal depletes" became "does not thereby deplete", which is close. The clause "the significance of which depends on the local water stress" was dropped. |
| C22.2 | para | 2 | S0: 2 | Ranking "preserved across all three formulations, corroborating…" (p. 16). |
| C23.0 | para | 2 | — | The PW feeds are recorded as printed ("50,000 and 90,000 ppm"). |
| C23.3 | para | 2 | — | Near-verbatim, honestly marked paraphrased. |

### Attribution problems outside the sample

These are not scored, but they're relevant to A3 and to the researcher.

- **C22.3** misattributes a number to the prose. The article says "only brackish water desalination in Case 1 maintained SWUI below the severe water stress threshold (SWUI = 7.2)" (p. 16). The reading says "the prose reports average SWUI of 7.2 for Case 1, below the severe cutoff". The 7.2-as-Case-1-average reading comes from Fig. 7a's dashed line, not the prose. It also smooths over the article's own inconsistency, where 7.2 is called "severe" while Fig. 7a puts severe at 9+ (claims list, inconsistency 7). Sampled, this would score 1.
- **C21.2** is strengthened. "This suggests that the increased energy requirements … would be negligible" (p. 15) became "The authors infer that extra energy and carbon from MLD/ZLD are negligible".
- **C5.7** is strengthened. "the resulting SWUI-based framework further enables identification of application-specific trade-offs" (p. 4) became "the SWUI-based framework identifies application-specific trade-offs".
- **C0.0** loses "commensurately" in "commensurately increases freshwater requirements" (AB1).

---

## A2. Coverage (against `claims_reference.md`)

The reading runs from the Highlights to the end of the reference list (pp. 1–20). It doesn't stop before the article does.

| Type | In list | Caught | Caught without what it shows | Missed |
| --- | --- | --- | --- | --- |
| Highlights (H1–H5) | 5 | 5 | 0 | 0 |
| Graphical abstract (GA1) | 1 | 1 | 0 | 0 |
| Abstract claims (AB1–AB12) | 12 | 12 | 0 | 0 |
| Contributions (C1–C8) | 8 | 8 | 0 | 0 |
| Section/subsection conclusions (S1.1–S3.3m) | 59 | 59 | 0 | 0 |
| Overall conclusions (CO1–CO9) | 9 | 9 | 0 | 0 |
| Figures (F1–F7) | 7 | 7 | 0 | 0 |
| Tables (T1, with footnotes) | 1 | 1 | 0 | 0 |

**Nothing on the list is missed.** Some items are caught only in part or in merged form:

- **Highlights.** H4 is recorded verbatim (C0.2) and H5 as a support item (C0.4 S0). H1–H3 aren't recorded as highlights, but their content is caught through the abstract claims (C0.1, C0.4).
- **Contribution C5.** The SWUI case studies "capturing the combined effect of cooling technique, local saline water conditions, geographic water stress, and brine disposal strategy" are merged into C5.7, which says only "Applied to three scenarios through 2030". The four factors are dropped. C5.7 also merges contributions C4, C5 and C7 into one claim.
- **S2.4g.** CEPCI normalisation is caught (C12.4). The note that membrane properties are similar to recent modelling and pilot studies is not.
- **S2.3c.** The interpretation is caught (C10.3), but the author's own label "a first-order water utilization intensity metric" is dropped.
- **S3.3m.** The values are caught (C22.3), but the author's concluding sentence ("This underscores the intensified water stress impact…") is not. The 7.2 threshold is reinterpreted, as described above.
- **CO6 and CO7.** These are caught only as a restatement ("The conclusion restates the rise in projected SWUI with WUE and the joint role of regional stress and recovery", C23.4), not as the authors' claims.
- **Figures.** All seven are read, and Figs. 4 and 7b are read in full. All 42 Fig. 4 cell values and every Fig. 7b range and cell cited match the image. Fig. 3 is read for its shape (rising, fitted to 2028, extrapolated) but not its values. Fig. 5a/6a give the key flows, salinities and areas; pump ΔP 28.7 bar, booster 6.5 bar, interstage 665 kg / 52,500 ppm and the Fig. 5a evaporator area are left out. Fig. 1's freshwater destinations ("Energy" and "Agricultural Sectors") aren't mentioned.

**Found beyond the list** (all confirmed in the article):

- C7.4: parasitic energy "can be further mitigated using energy recovery devices (ERDs)" (p. 6).
- C12.4: "evaporator material-related effects specific to MVC were included in the analytical framework" (p. 10).
- C24.0–C24.2: the back-matter statements (no competing interests, UT Energy Institute grant, "Data will be made available on request"; p. 18). The list puts these outside its scope but records the same statements.

---

## A3. Strength of language — **1**

Most of the reading keeps the authors' strength and conditions. It keeps:

- the absolute modals and intensifiers: "cannot", "will exacerbate", "increases drastically", "clearly highlights", "inherently demand", "almost an order of magnitude";
- the authors' hedges: "would result in increased regional water stress … depending on the local climate", "suggesting an optimal operating point";
- units and scope conditions throughout, with the article's printed oddities kept and flagged: 50 K, L/kg-feed, 90,000 ppm, the "ZLD" pie labels.

A handful of claims are shifted, in both directions:

- **Strengthened:** C5.7 ("enables identification" → "identifies") and C21.2 ("suggests … would be negligible" → "infer … are negligible").
- **Softened:** C5.8 ("will extend" → "could extend"), C4.3 ("often" added), C7.2 S0 (the article's "substantial corroboration" became "corroboration"), and C0.0 ("commensurately" dropped).
- **Misplaced:** C22.3 attaches the number 7.2 to a different quantity than the prose does.

The shifts are few out of 122 claims, small, and don't run one way, so this isn't the systematic drift that would score 0. But the rubric's 2 asks that strength survive "wherever the article attached them", and these cases fall short of that.

---

## A4. Mechanical checks

| Check | Pass | Fail | Notes |
| --- | --- | --- | --- |
| Verbatim texts found in the article text | 12 | 0 | All 12 verbatims are claims. All 89 support items are paraphrased. |
| Numbers found in the article text | 372 | 0 | 449 numeric tokens in claims and support. 371 match the extracted text directly. One ("about 931 L/1,000 kg") rounds the printed 931.2 and says so with "about", so it passes. The other 77 are image readings, reported below. |
| Reference entries matching the article's reference list | 167 | 0 | 170 citation records. All 167 non-null entries match an entry as printed (mismatches were only extraction artifacts). The 3 nulls are correct: `[14]` and `[1]` are numeric citations in an author–year article with no numbered list, and one "Ding et al., 2026" in §2's opening is ambiguous between 2026a/b/c, so null is conservative, not invented. No invented or completed reference was found. |

**Image readings, checked by eye against the rendered pages (77 values, not counted as failures):**

| Source | Values | Result |
| --- | --- | --- |
| Fig. 4a–c (C14.0, C15.0, C16.0, C16.2 support) | 46 | All correct |
| Fig. 5a/5b (C17.1, C17.3, C18.0 support) | 12 | All correct |
| Fig. 6a (C19.0 support) | 4 | All correct |
| Fig. 7b (C20.2, C21.0, C22.3 support) | 15 | All correct |

All of these are marked `paraphrased` and name the figure. The qualitative readings of Fig. 3, Fig. 5c and Fig. 6c also match the plots.

**Citation text (not a scored count).** Every `citation_text` appears in the article except one group. The printed "(Onishi et al., 2017; Onishi et al., 2017; Randon et al., 2020)" (p. 4) is split into "(Onishi et al., 2017)" twice and "(Randon et al., 2020)". The prompt asked for markers "exactly as printed".

---

## A5. Detail and readability (described, not scored)

**Steps and spread.** There are 25 steps over 20 pages:

| Part | Steps | Pages |
| --- | --- | --- |
| Front matter | 1 | p. 1 |
| Introduction | 5 | pp. 2–4 |
| Methods and Table 1 | 8 | pp. 4–10 |
| Results | 9 | pp. 10–17 |
| Conclusions | 1 | pp. 17–18 |
| Back matter | 1 | pp. 18–20 |

Step size stays in the prompt's range and follows section breaks. Locations are precise (page, section, figure panel).

**Claims.** Each step averages about 5 claims. They are mostly careful paraphrases, and the reading is rarely padded or repetitive. Some distinct claims are merged into one record, which the prompt asked against:

- C0.1 combines AB2–AB4.
- C5.7 combines contributions C4, C5 and C7.
- C10.0 combines the metric gap with the four-part critique of WUI.

**Support items.** These are the weakest part. Roughly half are generic citation carriers ("The article cites…", "The authors draw the comparison from US data center energy reports"). Their descriptions of what a cited work is about are often taken from the reference titles, not from the article's text. Two place an element as support for a claim it doesn't support: Highlight H5 under the abstract SWUI claim (C0.4), and the graphical abstract under the scope claim (C0.1).

**Moves and meaning.** `moves` is terse but accurate. `meaning` is usually a single sentence. It rarely does the reflection the prompt asked for, on whether a step follows from, qualifies or merely turns from the last one. It does, usefully and in the right field, flag several of the article's internal inconsistencies:

- TTD 0–5 K vs 0–10 K
- 50 K vs 50 °C
- L/kg vs L/1000 kg
- the "ZLD" labels on MLD pies
- Case 1 "moderate" vs Fig. 7b's zero–low values
- 90,000 vs 91,000 ppm
- 753 / 754 / 753.7 L
- Fig. 7b cells vs prose averages

It doesn't note others the article contains:

- the 7.2 vs 9+ severity threshold, which it smooths over instead;
- the abstract's "WC rise >15%" against the cost decreases in Fig. 4c;
- "up to 30%" pre-/post-treatment against Fig. 5b;
- the text vs plot ordering in Fig. 5c.

Noting these wasn't required.

**Readability.** A reader could follow the article's argument from this reading alone. It goes from the energy–water framing, to the literature gap, then the RO/MVC models and costing, the SWUI definition, the results across feeds and endpoints, the two worked cases, the SWUI site comparison, and finally the conclusions.

---

## Summary for the researcher

**Strengths.** For a cross-source comparison, this reading's claims are dependable.

- Attribution fidelity is high: 93% of sampled claims and 91% of support items score 2, and none score 0.
- Every verbatim is exact, every reference entry matches the article's list, and no reference is invented.
- Coverage of the claims list is complete, from the highlights to the conclusions, all figures and Table 1.
- The figure readings are unusually thorough and fully correct: every cell of Fig. 4 and the Fig. 7b values check out against the images.
- Several of the article's own internal inconsistencies are recorded as printed and flagged in the model's `meaning` fields, not silently corrected.

**Weaknesses.** These are minor and fixable:

- A few strength shifts in both directions, the clearest being "will extend" → "could extend", "enables identification" → "identifies", and "suggests … would be negligible" → "infer … are negligible".
- One misattribution: the 7.2 severity threshold is recast as Case 1's average SWUI and attributed to the prose. This also hides an inconsistency in the article.
- Some merged contribution claims, one of which drops the four factors in contribution C5.
- Support items that are often generic citation carriers, and twice misplaced.
- Thin step-to-step reflection.

None of these affects the article's headline numbers or conclusions as recorded. If the reading is accepted, the researcher should take claims C5.7, C5.8, C21.2 and C22.3 back to the article's wording before quoting them.
