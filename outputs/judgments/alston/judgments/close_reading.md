# Judgment — close reading

**Article:** `article.pdf` — Alston, Love & Haider, "Data Center Cooling Choices Shift Water Impacts Across the Grid: An Integrated Water-Energy Model for Sustainable Data Center Development" (arXiv:2609.25437v1, 12 PDF pages).

**Run judged:** `run/analysis.json` (26 steps, 110 claims, 77 support items, 56 citations).

**Judged against:** the article and `references/claims_reference.md` (used as written). The list covers the main text and Appendix A, so this judgment does too.

**Seed:** `20261107`. Sample drawn with Python `random.seed(20261107); random.sample(range(110), 30)` over the claims numbered 0–109 in reading order (step by step, claim by claim). Sampled claim indices: 4, 8, 9, 19, 21, 22, 23, 27, 30, 31, 36, 39, 42, 48, 51, 54, 56, 70, 71, 72, 77, 84, 88, 93, 96, 97, 98, 100, 103, 105.

**How the article was read:** no PDF text extractor was installed (no `pdftotext`, PyMuPDF or pypdf), so I worked from the PDF's text layer as loaded by the file reader, plus the page images for figures, equations and Table 1. The mechanical checks in A4 compare against that text layer, by hand, not with a script.

---

## A1. Attribution fidelity

| Score | Claims (n = 30) | Support items (n = 26) |
|---|---|---|
| 2 | 28 (93%) | 25 (96%) |
| 1 | 2 (7%) | 1 (4%) |
| 0 | 0 (0%) | 0 (0%) |

Every sampled passage was found, so none is unscored.

**Claims scored 1**

- **#4 (step 0, abstract).** The run says "Air cooling nearly halves total water consumption relative to evaporative cooling *in the modeled comparison* while increasing electricity demand and raising indirect consumption by roughly one-third." The article states it without a scope limit ("Air-cooled data centers nearly halve…"). The run adds a hedge the author didn't use, and it drops the clause the sentence builds to, "shifting the water footprint from the facility to generators on the grid."
- **#8 (step 1, §1).** The article's "The exponential growth of data centers" becomes "Rapid global data center growth." That softens the author's characterization.

**Support item scored 1**

- **#100 S0 (step 22, §5.2).** The article says the fixed thresholds "significantly simplif[y]" real controls. The run says only that they "omit controls such as mixing cold, humid outside air with return air." The author's "significantly" is gone.

**Sampled claims scored 2.** These were checked against: §1 for #9 and #19; §1.1 for #21 and #22; §1.2 for #23; §2.1 for #27; §2.1.4 for #30 and #31; §2.2.3 for #36; §2.2.4/Eq. 5 for #39; §2.3 for #42; Eqs. 11–12 for #48; §3.1.1 for #51; §3.1.2/Table 1 for #54, with all five support items correct; §3.1.3 for #56; §4.1/Table 2 for #70 and #71; Table 3 for #72; §4.2/Fig. 4 for #77; §4.3 for #84 and #88; §5.1 for #93, #96, #97 and #98; §5.2 for #103 and #105. Hedges in these claims survive, for example "may approximate volume while misidentifying" (#22) and "generally remain fixed" (#27, from the article's "primarily remain fixed").

**Outside the sample (noted, not counted)**

- Claim #2 (abstract) merges two abstract claims, AB4 and AB5. It also turns the author's flat "attribute indirect consumption to the facility's location … misattributing the spatial impacts" into "*can* attribute indirect water use to the wrong hydrologic regions," which is softer.
- Claim #81 ("The two siting cases have nearly identical statewide water totals") is the run's own summary of Table 2, not a sentence the author writes. It is accurate, but it is the model's reading placed in a claim field. It is borderline under the rubric's misattribution rule.

## A2. Coverage (against `claims_reference.md`)

| Type | In list | Caught | Caught without what it shows | Recorded only as a restatement | Missed |
|---|---|---|---|---|---|
| Enumerated contributions (C1–C3) | 3 | 0 | — | 3 | 0 |
| Abstract claims (AB1–AB11) | 11 | 10 | — | — | 1 |
| Overall conclusions (FN1–5, CO1–5) | 10 | 6 | — | 4 | 0 |
| Recommendations (R1–R5) | 5 | 5 | — | — | 0 |
| Section/subsection conclusions (S1–S39, SA) | 40 | 38 (5 of them partial) | — | — | 2 |
| Figures (F1–F8) | 8 | 6 | 2 | — | 0 |
| Tables (T1–T3, TA.1–TA.3) | 6 | 6 | 0 | — | 0 |

The section-conclusion row splits as follows: 33 caught in full, 5 caught in part (S1, S2, S5, S33, S35), and 2 missed (S8, S25), for 40.

**Contributions.** At §1.2 the run records only claim #23 (the model and its Michigan application). The step's `meaning` says "The contribution bullets restate the preview in that language," and the three bullets are not recorded. Their content does appear elsewhere: C1 in #1, #4 and #12; C2 in #5 and #76; C3 in #6 and #84. The normative part of C1, that cooling choices "must be evaluated across both the facility and the specific generators responding to its load," is never recorded as such. #93 comes closest.

**Abstract.** AB1 is #0. AB2 and AB3 are #1, merged, and AB3's "water–energy trade-offs" wording is lost. AB4 and AB5 are #2, merged and softened (see A1). AB6 is #3, AB8 is #4, AB9 is #5, AB10 is #6 with its "may overlook" kept, and AB11 is #7. **Missed: AB7** (the model is applied to cooling selection and to proposed Michigan developments). It is absent from step 0, though #23 covers the same ground at §1.2.

**Overall conclusions.** The §4 introduction's list of five findings is noted only in `moves` ("Restates the gap as five findings to be developed"). Each finding is still recorded where the article develops it: FN1 in #68–#71, FN2 in #76, FN3 in #78 and #84, FN4 in #89, FN5 in #90. CO5 is caught in #98, though its first sentence ("facility-level analysis and consumption volumes cannot accurately capture data center impacts") is only implied by #96–#97.

**§6 Conclusion (CO1–CO4): no claims recorded.** Step 24's only claim is the acknowledgments sentence (#106). Its `moves` call the conclusion a restatement, which the prompt allows. CO3 and CO4 largely repeat the abstract (#4–#7). CO1's framing, that assessment "requires accounting for both direct … and indirect water consumption," is not recorded in those words anywhere.

**Section conclusions missed or only partly caught**

- **S8, missed.** §1.2: "existing approaches cannot resolve which generators respond to added demand, nor the hydrologic regions in which that response's consumption and depletion occur."
- **S25, missed.** §3 opening: the scenarios "illustrate its ability to evaluate different elements of data center development." Minor.
- **S33, partial.** §4.1's general claim is not recorded: "Generally, configurations with lower direct water consumption … reduce total modeled water consumption, while increasing the relative contribution of indirect water use." Only the specific Table 2 comparisons are. The sentence "This efficiency gain comes with more complex and climate-dependent operations" appears only in `moves`.
- **S1 and S2, partial.** "Critically, Scope 2 consumption links energy and water impacts" and "Together, these three metrics determine the water impact of a data center facility" are not recorded. #11–#13 give the definitions without these framing claims.
- **S5, partial.** The "same fundamental limitation" of prior work (an averaged mix rather than the responding generators) is implied in #20 and stated in the step's `meaning`, but never recorded as a claim.
- **S35, partial.** "The demonstrated water–energy tradeoff has spatial implications … cooling configuration selection also changes the spatial impacts" is only approximated by #78.

**Figures**

- **Caught with what they show:**
  - F1 (#24 S0). Generic, but it names the three systems.
  - F3 (#73 S0, #76 S0). Hybrid direct is lower in May than in August; indirect is higher in July than in June.
  - F4 (#77 S0). Steady nuclear and hydro, varying gas, and a note that the figure shows the total mix rather than the increment.
  - F5 (#79 S0 with #79). Common scale, similar geography, air-cooled largest.
  - F6 (#82 S0, #83 S0). The ranking and the three stacked components are given, but the printed bar totals (7.27, 4.26, 5.88 …) are not read.
  - F8 (#86–#88 S0).
- **Caught without what they show:**
  - **F2** (#30 S0). It says only that the figure "plots separate PUE and WUE ranges" and that endpoints are unlabeled. It gives no reading of which configurations are high or low on either axis.
  - **F7** (#85 S0, #90 S1). It says panels (a)–(b) "compare the increase maps" and that (a)–(d) "show how the geography of increase differs from the geography of total depletion." It doesn't say what the maps show: concentration near the Southeast sites in (a), dispersal in (b), and high-baseline subbasins in the south and southwest in (c)–(d).

**Tables.** All six are read with their values:
- T1 in #54 S0–S4. The zeros for batteries and hydro are correct against the image (see A4).
- T2 in #68–#71 and #81.
- T3 in #72 S0, all 13 rows.
- TA.1 in #107 S0, with the shares in #52.
- TA.2 in #108 S0.
- TA.3 in #109 S0.

**Found beyond the list** (each confirmed in the article):
- #8–#10, the introduction's scale claims: growth "with continued expansion … expected" [8], the U.S. holding the largest share [8], and 192 TWh / 4.7% in 2024 [23].
- #16, the withdrawal-versus-consumption definition [12].
- #62, the facilities are "likely for AI training workloads."
- #64, the latency rationale for the two siting cases (inference near users, training farther away).
- #106, the funding statement.

**Where the reading stops.** It doesn't stop early. It runs through §6 and Appendix A, and step 24 acknowledges the reference list.

## A3. Strength of language — **1**

Most of the author's certainty and scope survive. Necessity language is kept: "must consider" (#94), "must move toward" (#98), "requires integrated models" (#93), "cannot substitute" (#97). Hedges are kept: "may overlook" (#6), "may misrepresent" (#92), "likely reflects the four-bus, four-line grid" (#80), "generally favor" (#53), "could represent" (#64), and the §3.3 "illustrative analysis" disclaimer, quoted verbatim (#66). Units, conditions and scenario scope also survive: "upper endpoints … to represent worst cases" (#58), the 27 °C / 70% joint rule (#60), median values for Scenario 2 (#62), and the 0.03% indirect contribution (#82).

The departures all lean softer:
- "exponential" becomes "rapid" (#8).
- "in the modeled comparison" is added to an unqualified abstract claim (#4).
- "attribute … misattributing" becomes "can attribute" (#2).
- "significantly simplifies" loses its intensifier (#100 S0).

No strengthening was found. Four softenings across 110 claims is too few to call systematic, but there are enough of them, all pointing the same way, to rule out a 2.

One unit change was checked and is not a fault. The run gives the §4.3 and §4.5 depletion changes in percentage points (6.74, 2.58, 0.81–1.5, 2.78 pp), where the prose prints "%". That follows the article's own Eq. 13 and the Figure 8 labels, so it is faithful.

## A4. Mechanical checks

| Check | Pass | Fail |
|---|---|---|
| Verbatim texts found in the article text | 2 | 0 |
| Numbers found in the article text (distinct values, not counting figure, table, equation and reference labels) | about 105 | 0 |
| Reference entries matching the article's reference list | 33 | 0 |

- **Verbatim.** Only 2 of 110 claims, and none of the 77 support items, are marked `verbatim`. Both match exactly: #66 (the §3.3 "illustrative analysis" sentence) and #106 (the acknowledgments sentence).
- **Numbers.** Every value matches the text or its text-layer tables. That covers Table 2 (all 25 cells used), Table 3 (all 26 percentages), Tables A.1–A.3, the §3.1.2 capacity shares, the line parameters (6,000 MW, 0.10 Ω, 0.01 Ω), the mode-switch thresholds (27 °C, 70%), the facility sizes (200 MW; 2,700 / 1,400 / 525 / 4,625 MW), the depletion figures (6.74, 2.58, 0.81–1.5, 2.78, 1.48, 4.4, 0.03), and 192 TWh / 4.7%. The years 2010–2020 and 2019 (#42 S0) come from reference entry [31], not the body text, and the run says so.
- **References.** All 33 entries in the article's list are cited at least once, and each `reference_entry` reproduces its entry. For multi-work markers ([9, 10, 21], [10, 11, 17, 20], [7, 12, 27], [17, 25], [21, 22], [22, 33], [28, 29]) there is one entry per work, and each maps correctly. Line-break hyphens in three URLs ([26], [31], [32]) are resolved one plausible way; I count these as matches. No reference was invented, and every citation marker matches the marker at the passage cited.

**Readings of images (checked by eye, not counted above)**

- **Table 1** (#54 S4). The text layer shows "10" for batteries, conventional hydro and pumped storage, because the footnote superscript "¹" runs into the "0". The run's "zero … based on technology operation" is correct against the page image.
- **Figure 8** (#82 S0, #86 S0). The annual-increase labels on the panels (6.74, 2.58, 1.48 pp) match the image.
- **Figures 2–8.** The qualitative readings match the images. Examples: July indirect above June in Fig. 3, the gas share varying in Fig. 4, air-cooled darkest in Fig. 5, the indirect peak in Aug–Sep in Fig. 8.
- **Equations 1–14.** The run paraphrases them and names each one. The paraphrases are accurate, including Eq. 13's ×100 conversion to pp and Eq. 8 applying only the change in generation.

## A5. Detail and readability (described, not scored)

**Shape.** 26 steps over 11 text pages:
- Steps 0–2: abstract and introduction.
- Steps 3–8: model.
- Steps 9–12: Michigan implementation and the two scenarios.
- Steps 13–19: results.
- Steps 20–23: recommendations and limitations.
- Step 24: conclusion.
- Step 25: Appendix A.

The pace matches the plan: smaller steps where the methods are dense (§2.2.4, §2.3 and §2.4 each get their own step), and larger ones in the discussion. Coverage is even, with one exception: the conclusion step carries no claims.

**Readability.** A reader could follow the article's argument from this reading alone. The steps run in order, each `moves` field states the rhetorical work plainly, and the `meaning` fields connect each step to the one before. For example, step 8 explains that keeping only the dispatch difference avoids double-counting thermoelectric use, and step 15 explains why the fixed-load cases isolate grid-driven variation. Claims are compact, and nothing is padded or repeated.

**Weaknesses**

- Many support items describe a citation rather than the evidence. For example, #21 S0 reads "The concession is accompanied by a citation on hourly emissions accounting," and #17 S0 reads "The cited depletion study supports the distinction." This is accurate, but it adds little.
- With only 2 verbatim claims, almost nothing in the reading can be quoted directly in a cross-source comparison.
- A few distinct claims are merged (#1, #2).

## Summary for the researcher

This is an accurate, well-paced close reading with very few errors.

**Strengths**
- In the 30-claim sample, no claim misrepresents the article. Two are slightly softened, and one support item drops an intensifier.
- Every number checked matches.
- All 33 references are reproduced without invention, and markers map one entry per work.
- All six tables are read in full, and the Table 1 footnote trap is handled correctly from the image.
- The author's hedges and necessity language mostly survive.
- The reading runs from the abstract through Appendix A, in steps a reader can follow.

**Weaknesses**
- Its departures all lean softer: "exponential" becomes "rapid," and qualifiers are added to two abstract claims.
- It records framing claims only as restatements:
  - the three §1.2 contributions;
  - the §4 list of five findings;
  - the whole §6 Conclusion, where the only claim recorded is the funding acknowledgment;
  - the general §4.1 statement that lower-direct-water configurations generally reduce total consumption.
- Figures 2 and 7 are named without a reading of what they show.
- It uses almost no verbatim text.

**For the cross-source comparison:** the content is reliable. If that comparison depends on the article's own headline wording (contributions, findings, conclusion), those claims will need to be taken from the article or from the reference list, not from this run.
