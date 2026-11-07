# Judgment — close reading

**Article:** `article.pdf` (Alston, Love, Haider, "Data Center Cooling Choices Shift Water Impacts Across the Grid," arXiv:2609.25437v1)
**Run judged:** `run/analysis.json` (26 steps, 128 claims, 77 support items, 56 citation→reference pairs)
**Reference list used:** `references/claims_reference.md`, used as written (main text + Appendix A)
**Seed:** `20261107` (Python `random.seed(20261107); random.sample(range(128), 30)` over claims flattened in reading order)

**Method.** I extracted the article text with macOS PDFKit (via Swift), plus a Ghostscript `txtwrite` pass to cross-check. In this PDF, Tables 1–3 and A.1–A.3 are text and can be extracted. Figures 1–8 are raster images and so are Equations (1)–(14) as typeset. I rendered pp. 3, 7, 8 and 9 to PNG and checked every figure reading in the run by eye. The verbatim, number and reference checks were scripted (normalised for whitespace, curly quotes and line-break hyphenation), and I inspected every failure by hand.

---

## A1. Attribution fidelity (30 sampled claims, 16 support items)

| Score | Claims | Share | Support items | Share |
|---|---|---|---|---|
| 2 | 28 | 93% | 15 | 94% |
| 1 | 2 | 7% | 1 | 6% |
| 0 | 0 | 0% | 0 | 0% |

Per-claim scores (index = position in flattened claim list; step/claim are 0-based):

| # | Step.claim | Form | Claim | Support | Note |
|---|---|---|---|---|---|
| 4 | 0.4 | verbatim | 2 | — | Exact abstract sentence. |
| 8 | 0.8 | para | 2 | — | AB11; faithful. |
| 9 | 1.0 | para | 2 | 2 | Near-verbatim truncation, honestly marked paraphrased; [8] correct. |
| 19 | 1.10 | para | 2 | 2 | Withdrawal/consumption definitions; [12] correct. |
| 21 | 1.12 | para | 2 | — | Depletion rationale and "same increase → different risk" kept. |
| 22 | 2.0 | para | 2 | 2, 2, 2 | §1.1 lineage; "regional water availability" rendered "local", a negligible shift. |
| 23 | 2.1 | verbatim | 2 | — | Exact. |
| 27 | 2.5 | verbatim | 2 | — | Exact. |
| 30 | 2.8 | verbatim | 2 | — | Contribution C2, exact. |
| 31 | 2.9 | verbatim | 2 | — | Contribution C3, exact. |
| 36 | 3.4 | para | 2 | 2 | IT- vs facility-load representations; Eqs. (1)–(3) read correctly. |
| 39 | 4.1 | para | 2 | — | IT cooling vs heat rejection distinction. |
| 42 | 5.2 | para | 2 | 2, 2 | ReEDS [19], NSRDB 4 km GHI [18] correct. "Assumed to be dispatched up to" becomes "can run up to", a very minor loss of the word "assumed". |
| 51 | 7.3 | para | 2 | — | USGS consumption categories and availability definition. |
| 54 | 8.1 | para | 2 | — | Matches the "only the change…" note under Eq. (8). |
| 56 | 8.3 | para | 2 | 2 | "Same gross-supply denominator" is a reading of Eqs. (11)–(12), both over S_h,m, so it is supported. Change in pp × 100 is correct. |
| 70 | 12.0 | para | 2 | 2 | 2,700 / 1,400 / 525 = 4,625 MW; FracTracker [6]. |
| 71 | 12.1 | para | 2 | 2 | "Likely for AI training" hedge kept; DOE medians [20]. |
| 77 | 13.1 | para | 2 | — | Five findings, wording near-exact. Drops the author's "critical" (rhetorical label, not scored down). |
| 87 | 15.0 | para | 2 | — | Constant direct use; month-length variation attributed as the author does. |
| 88 | 15.1 | para | 2 | 2 | "Varies substantially" kept. Figure 3 reading checked: evaporative indirect ≈0.34 (Jun) vs ≈0.40 (Jul) million m³, consistent with the reading. |
| 93 | 16.3 | para | **1** | 2 | The article says magnitude "varied substantially" across configurations; the claim keeps the ranking (air-cooled largest, hybrid smallest) but drops "substantially". Figure 5 reading (common pp scale, values unlabeled) is correct. |
| 97 | 17.2 | para | 2 | 2 | 0.81–1.5 and the four regions correct. The unit is rendered as pp where the text prints "%" (see A4). |
| 100 | 18.0 | para | **1** | 2 | The article says depletion "varies **substantially** month to month"; the claim says only "varies". Figure 8 labels (6.74 / 2.58 / 1.48 pp) checked on the image. |
| 103 | 18.3 | para | 2 | — | Understate/overstate kept. |
| 108 | 20.2 | para | 2 | **1** | The claim is fine ("may" → "can"). The support says relocation reduces concentration "without reducing **direct** consumption"; the article says "without reducing **total** consumption", and "can reduce" becomes "reduces". Both statements are true per Table 2, but the author's wording and scope are changed. |
| 116 | 23.0 | para | 2 | — | Four-region limitation; sub-hourly work as "ongoing". |
| 118 | 23.2 | para | 2 | — | "May misallocate" → "can be wrong": the hedge is preserved in substance. |
| 120 | 24.0 | verbatim | 2 | — | CO1, exact. |
| 123 | 24.3 | verbatim | 2 | — | CO4, exact. |

I found no 0s in the sample. Outside the sample, I also read every other claim against the article and found no misattribution: claim and support fields hold the author's content, and the model's commentary stays in `moves` and `meaning`. The two borderline cases are both descriptive glosses, not inferences presented as the author's:
- Step 13.0 calls prior approaches "established ways of estimating off-site consumption", where the article says only that prior work "relied on" them.
- Step 15's support adds that Figure 4 "displays the total mix rather than a separate stack of incremental generation". This is accurate: the text says Figure 4 plots "total electric load."

## A2. Coverage (against `claims_reference.md`)

The reading runs from the title page through Appendix A (p. 12), so it covers the whole span the list defines.

| Type | In list | Caught | Caught without what it shows / partial | Missed |
|---|---|---|---|---|
| Enumerated contributions (C1–C3) | 3 | 3 (all verbatim) | 0 | 0 |
| Abstract claims (AB1–AB11) | 11 | 11 | 0 | 0 |
| Enumerated findings (FN1–FN5) | 5 | 5 (in one claim, step 13) | 0 | 0 |
| §6 conclusions (CO1–CO4) | 4 | 4 (all verbatim) | 0 | 0 |
| §5.1 summary (CO5) | 1 | 0 | 1 | 0 |
| Recommendations (R1–R5) | 5 | 5 | 0 | 0 |
| Section/subsection conclusions (S1–S39, SA) | 40 | 40 | 0 (minor omissions noted below) | 0 |
| Figures (F1–F8) | 8 | 8 | 0 | 0 |
| Tables (T1–T3, TA.1–TA.3) | 6 | 6, values read in full | 0 | 0 |

Notes on partials and small omissions:
- **CO5:** only the second sentence ("Impact assessments and tracking must move towards integrated … models…") is recorded (step 21.2). The first sentence, "facility-level analysis and consumption volumes cannot accurately capture data center impacts", is not recorded as a claim. Its substance survives in the R4/R5 claims.
- **Abrupt merges in the abstract:** AB2+AB3 are merged into one claim (0.1), and so are AB4+AB5 (0.2). The content is kept, but AB5's "misattributing the spatial impacts" is reduced to the factual attribution.
- **§4 opening (list §3a, unnumbered):** the statements that prior approaches "suppress the temporal impacts and misattribute the spatial impacts" and that the findings "have direct consequences for how … [footprints] should be assessed, sited, and reported" are not recorded.
- **S20:** "This calculation links the Energy System to the Water System" appears only in `meaning`.
- **S27:** "The WCI metric is more accurate in capturing the change in resource operations" is not recorded explicitly. The hydro argument around it is (step 10.3).
- **S35:** "While the largest impacts remain concentrated around the proposed facilities" is dropped from the Scenario 2 claims.
- **S38:** the opening "impacts arise from interactions between cooling configuration, electricity demand, grid dispatch, and existing hydrologic conditions" is folded into the "therefore" conclusion (step 19.1).
- **Figures:**
  - F1 is read only generically ("diagrams the facility, energy and water systems and identifies the inputs and outputs").
  - F6 is described structurally (eight ranked subbasins, baseline/direct/indirect stacks), but its printed totals (7.27, 4.26, 5.88, 2.57, 2.65, 1.69, 1.48, 1.55) are not read.
  - The other figures are read with their substance: F2 ranges, F3 hybrid May vs August, F4 baseload vs load-following, F5 common scale, F7 a–d, F8 labels and the Jul–Sep pattern.

**Found beyond the list (confirmed in the article):**
- Step 1.0: the growth premise.
- Step 1.1: the US largest share [8].
- Step 1.2: 192 TWh / 4.7% in 2024 [23].
- Step 1.3: Scope 1/Scope 2 definitions [14].
- Step 12.3: the latency rationale for the alternate siting case (§3.3).
- Step 24.4: the funding statement (Acknowledgments, p. 11). The list excludes Acknowledgments, so this is outside the list's scope rather than a coverage gain.

## A3. Strength of language — **2**

**What survives.** Conditions, scope, samples, units and the author's certainty survive almost everywhere, including all the hedges the reference list flags:
- "may overlook" (0.7)
- "generally prioritizes" → "generally favor" (10.1)
- "Generally, configurations with lower direct water…" (13.2, verbatim)
- "likely reflects the four-bus, four-line grid" (16.4)
- "heuristically" line limits (9.2–9.3)
- "worst cases" upper endpoints (11.1)
- the illustrative-only disclaimer for Scenario 2 (12.5, verbatim)
- "may misrepresent" (20.0)
- "may estimate … while misidentifying" (2.4)
- "first to connect" priority claim (22.0)

Strong claims are kept strong: "cannot resolve", "must consider", "should require … rather than annualized", and "cannot substitute for water risk".

**The exceptions are few and not systematic:**
- **Softened:** "substantially" dropped twice (16.3, 18.0); "five critical findings" → "five findings" (13.1); "assumed to be dispatched" → "can run" (5.2).
- **Strengthened:** "can reduce" → "reduces", with total → direct consumption (20.2 support); "relied on" → "established ways" (13.0).

These run in both directions, mostly concern intensifiers rather than hedges or scope conditions, and amount to a handful among 128 claims. I score 2, at the edge. A stricter reader treating every dropped intensifier as a stripped qualifier would score 1.

## A4. Mechanical checks

| Check | Pass | Fail | Notes |
|---|---|---|---|
| Verbatim texts found in the article's text | 20 | 0 | One ("This efficiency gain comes with more complex and climate-dependent operations.") matches only when the line-break hyphen in "climate- dependent" is kept as a real hyphen. It is the author's exact wording. |
| Numbers found in the article's text | 212 | 0 | Numeric tokens in claim and support texts, excluding the 5 image readings below. Caveat: this is a substring check, so it proves presence, not that the number is attached to the right quantity. My A1 reading of the sample and my read-through of all steps checked context and found every number attached to the right quantity. |
| Reference entries matching the article's reference list | 56 | 0 | Two entries ([31] USGS, [3] Bertolacini) failed the automated check only because the extraction splits a URL at a real hyphen and a word at a soft hyphen in the same entry. Inspected by hand, both are exact. Every entry is assigned to the correct citation number. No reference is invented or completed. All citation markers appear in the text as printed. |

**Image readings (checked by eye, not counted as failures):**
- **Figure 2** (step 4): DX and air-cooled chillers have the highest PUE ("roughly 1.75–2.25 for small facilities") and near-zero WUE; IT liquid cooling and large-scale configurations are near PUE 1.1; PUE falls with size. All consistent with the image. One imprecision: "water-cooled chillers or water-cooled economizers have … WUE of roughly 2–3.5" fits the water-cooled chillers and the waterside economizers. However, the midsize "airside economizer (water-cooled chiller)" box sits around 1.2–1.5. The reading says "exact endpoints are not labeled", which is accurate.
- **Figure 3** (steps 14, 15): hybrid direct use is smaller in May (≈0.14) than in August (≈0.30); evaporative indirect use is higher in July than in June. Both correct.
- **Figure 4** (step 15): steady nuclear and hydro, varying gas, total mix not incremental. Correct.
- **Figure 5** (step 16): common pp scale; values unlabeled. Correct.
- **Figure 7** (steps 17, 19):
  - (a) dark increase at the clustered SE sites near the top of the 0–7.5 scale; (b) lighter and spread around three sites. Correct.
  - (c, d) highest in southern Lower Michigan, darkest in the southwest, the two maps much alike. Correct.
- **Figure 8** (step 18): panel labels 6.74 / 2.58 / 1.48 pp read exactly, with HUC IDs; indirect component strongest Jul–Sep in 04050002. Correct.
- **Equations (1)–(14)** are read as paraphrase, correctly and without fabricated notation.

All image readings are marked `paraphrased`, and each names its element.

**Unit note.** For the Scenario 2 depletion changes (6.74, 2.58, 0.81–1.5, 2.78), the reading writes "percentage points" where the §4.3 prose prints "%". This agrees with Eq. (13) and the Figure 8 labels, so it is a defensible normalisation, not an error. A reader comparing it with the article's prose should know the unit was changed.

## A5. Detail and readability

- **Steps.** There are 26 steps; the reading plan declares a smaller pace for the dense method sections.
- **Distribution.** The steps are spread evenly over the article:
  - pp. 1–2 (abstract, intro, related work): 3 steps
  - §2 method (pp. 2–5): 6 steps, split at subsystem boundaries as planned
  - §3 case study: 4 steps
  - §4 results (pp. 6–9): 7 steps
  - §5 discussion and limitations: 4 steps
  - conclusion: 1 step
  - Appendix A: 1 step
- **Step size.** Step sizes track the article's natural breaks. The only lumped steps are the abstract (one step, nine claims, appropriate for its density) and the §4 opening merged with §4.1's annual comparison.
- **Readability.** A reader could follow the article's argument from the reading alone: gap → model → Michigan setup → five findings → recommendations → limitations. The `moves` fields name argumentative moves accurately, for example "Qualifies the hybrid result", "Defines the counterfactual" and "Claims novelty".
- **Meaning fields.** These are short and mostly earn their place, such as the note that subtracting the baseline "avoids counting existing thermoelectric use twice". A few are generic ("The appendix supplies numerical detail behind the implementation").
- **Restatement.** The prompt asked that restatements be noted as moves rather than recorded again, and the reading only partly does this. Step 24's `moves` says "Restates", but CO3 (which restates C1–C3) is recorded again as a claim, and the abstract and contribution claims overlap. This is minor and does not pad the reading.
- **Odd inclusions.** The funding sentence is recorded as a claim, and the "References" step adds nothing beyond the location.

---

## Summary for the researcher

**Strengths.**
- **Exact quotes and references.** The mechanical record is clean: all 20 verbatim texts are the author's exact wording, all 56 reference entries are copied exactly and mapped to the right numbers, and no references are invented.
- **Faithful image readings.** Readings of figures and equations are properly marked as paraphrased, named by element, and match the images. Where values are unlabeled, the reading says so instead of estimating.
- **Coverage.** It catches every enumerated contribution, abstract claim, finding, recommendation and section conclusion on the list, and every table with its full values.
- **Qualifiers.** It preserves the qualifiers that matter most for downstream comparison: worst-case endpoints, the heuristic four-bus grid, "likely" for the spatial similarity, and the illustrative-only status of Scenario 2.
- **Attribution.** Claims and the model's commentary are cleanly separated.

**Weaknesses.**
- **Dropped intensifiers.** "Substantially" (twice) and "critical" are lost. One support item restates the relocation result with a changed scope ("direct" for "total") and drops the word "can".
- **Coverage gaps.**
  - The first sentence of the §5.1 summary is not recorded.
  - The §4 opening's "suppress/misattribute" framing is not recorded.
  - Figure 6's printed totals are not read.
- **Changed unit.** The pp-for-% change, though correct by Eq. (13), departs from the article's prose and should be known to anyone quoting the numbers.

None of these is an invented or unsupported claim. All are fixable. For a cross-source comparison, the reading looks reliable as a record of what this article says, with the caveat to check the few softened magnitude words against the article where they matter.
