**Article:** `article.pdf` — Herrera et al., “Sustainable AI infrastructure: A scenario-based forecast of water footprint under uncertainty.”

**Seed:** `20261112`. I flattened the JSON's claims in reading-path order, numbered them 1–156, and selected 30 without replacement using Python `random.Random(20261112).sample(range(1, 157), 30)`. The sorted sample is 5, 7, 24, 28, 30, 31, 46, 49, 53, 54, 60, 63, 64, 78, 84, 88, 91, 98, 106, 111, 112, 122, 127, 129, 130, 134, 139, 149, 152, 156. Each sampled claim's support items were also assessed. Below, `step.claim` identifies JSON positions; `S1` identifies the first support item. I extracted all 12 PDF pages with PDFKit and visually inspected rendered pp. 4–6, 8, and 10 for the figures, schematics, algorithm, and tables on those pages. Only the requested source files were consulted; the reference inventory was used unchanged.

**A1 — Attribution fidelity.** Claims: **28/30 at 2 (93.3%); 2/30 at 1 (6.7%); 0/30 at 0 (0%)**. Support items: **15/15 at 2 (100%); none at 1 or 0**. No sampled passage was unlocatable. These support scores assess the support statements against their passages; faulty bibliographic fields are separately counted under A4.

| Claim ID / JSON position | Claim score | Support scores | Evidence against the located passage |
| --- | --- | --- | --- |
| 5 / 1.5 | 2 | — | P. 1 highlights and abstract identify cooling, electricity sourcing, siting, alternative technologies, and compute/efficiency sensitivity. |
| 7 / 2.1 | 1 | S1: 2 | P. 1 introduction supplies 70%, 26%, and about 14%, but describes economic gains as “up to roughly $15 trillion.” The reading retains “roughly” and drops the upper-bound condition. PwC attribution is correct. |
| 24 / 4.3 | 2 | S1: 2 | P. 2 names server efficiency/utilisation, grid water use, cooling type, and climate, citing Lei et al. (2025). The reference field is defective, but the support statement identifies the cited review correctly. |
| 28 / 5.3 | 2 | — | P. 2 explicitly calls the scenarios a realistic range grounded in technological and policy trends. |
| 30 / 5.5 | 2 | — | P. 2 connects the forecast horizon with SDGs/net-zero commitments and planning in water-stressed regions. |
| 31 / 6.1 | 2 | S1: 2 | P. 2, §2 opening, explicitly links greater AI computation to cooling and water, citing Cowls et al. |
| 46 / 8.6 | 2 | — | P. 3, §2.1 close, states the conditional environmental escalation and disproportionate scarcity impacts; the preceding paragraph calls for efficiency, cooling, and water-management improvements. |
| 49 / 9.3 | 2 | S1: 2; S2: 2 | P. 3, §2.2 says the framework follows and extends Li et al.; Eq. (1) sums the three named components. |
| 53 / 10.2 | 2 | S1: 2 | P. 3 ties EWIF to regional energy mix and calls solar/wind almost water-free in its fossil/nuclear comparison. |
| 54 / 10.3 | 2 | S1: 2 | P. 3 treats manufacturing water as fixed and amortised; Eq. (4) and its definitions give T × W / T₀. |
| 60 / 11.3 | 2 | S1: 2 | P. 4, §3 describes air cooling's increasing inadequacy, water-based liquid coolants, and immersion's water benefit and adoption barriers, citing Jones/Gao and Evans. |
| 63 / 11.6 | 2 | S1: 2 | P. 4, §3.1 gives 10%–30% higher total energy relative to evaporative cooling, conditional on ambient temperature/humidity, citing Li et al. |
| 64 / 12.1 | 2 | S1: 2 | P. 4, §3.2 gives prevalence, relative water abundance, and thermal efficiency, with Kim/Chu and Huang citations. |
| 78 / 14.1 | 2 | — | P. 5, §4 opening links infrastructure, incentives, renewables, water stress, and competition with agriculture/residents. |
| 84 / 15.3 | 2 | S1: 2 | P. 6 China bullet gives over three billion cubic metres annually by 2030, northern scarcity, and cooling/renewables policy, citing He et al. |
| 88 / 16.2 | 2 | — | P. 6 climate paragraph supplies BWh/BSh, the named regions, and the temperature/humidity/freshwater explanation. |
| 91 / 17.1 | 2 | — | P. 6, §5 opening identifies missing high-resolution data and rapid technological change. |
| 98 / 18.4 | 2 | — | P. 7, §5.1 explicitly assigns EWU a fixed annual improvement rate associated with manufacturing and supply chains. |
| 106 / 20.2 | 2 | — | P. 7 Monte Carlo paragraph gives high uncertainty, complex interaction, and ranges rather than single forecasts. |
| 111 / 21.3 | 2 | — | P. 8, Algorithm 1 lines 18–22 display the two operational products, division by 10⁹, embodied addition, and stored means/intervals. Correctly paraphrased. |
| 112 / 21.4 | 2 | — | P. 7, §5.1 close explicitly places spatial disaggregation outside current scope. |
| 122 / 24.1 | 2 | S1: 2 | P. 8, §6.1 states operational dominance, WUE/PUE responsiveness, and embodied relevance with shorter refresh cycles, invoking the Appendix. |
| 127 / 25.3 | 2 | — | P. 9, §6.2 explicitly distinguishes deterministic interactions from independent probabilistic inputs. |
| 129 / 25.5 | 2 | — | P. 9, §6.2 recommends capturing nonlinear effects and identifies real-time monitoring/dynamic Bayesian modelling as promising. |
| 130 / 26.1 | 2 | S1: 2 | P. 9, §6.3 predicts intensifying conflicts and reports possible utility/regulator restrictions during drought or peak demand. |
| 134 / 27.2 | 1 | S1: 2 | P. 9 says international standards “could also help prevent” clustering. “Could prevent” slightly strengthens their preventive sufficiency. The EU/US precedents and citations are correctly attributed. |
| 139 / 27.7 | 2 | S1: 2 | P. 9 recommendation requires metric disclosure and cites United Nations (2019). |
| 149 / 30.3 | 2 | — | P. 10 CRediT statement supports Herrera's roles and the coauthors' differing combinations; the reading does not assign every role to every coauthor. |
| 152 / 31.2 | 2 | — | P. 10, Fig. A.7 visually confirms signed bars, WUE > EWIF > PUE > embodied ranking, and the printed “EWE” label. Endpoints have no numerical data labels. |
| 156 / 32.1 | 2 | — | P. 10 Data availability states that supporting data/code are openly available at the recorded repository. |

**A2 — Coverage (counts, not a score).** For conclusions I use all 83 S/AP entries in the inventory's section/subsection/Appendix category, including their supporting claims and recommendations. This is an inventory-entry count, not a count of independent conclusions. A claim repeated later in `moves` counts as caught, as the reading instructions require restatements there instead of duplicated claim fields.

| Reference-list type | Caught with substantive content | Named without what it shows | Missed |
| --- | ---: | ---: | ---: |
| Contributions: H1–H3 and C1–C5 | 8/8 | 0 | 0 |
| Abstract claims: A1–A8 | 8/8 | 0 | 0 |
| Section/subsection conclusions and claims: S/AP entries | 83/83 | 0 | 0 |
| Figures: F1–F7 | 7/7 | 0 | 0 |
| Tables: T1–T3 | 3/3 | 0 | 0 |

There are no wholly missed entries. Contributions and abstract claims appear in steps 1, 5, and 17–24; the later concluding recapitulations are explicitly recorded in steps 29–30. Section coverage follows §§1–7 and includes the Appendix in step 31. Steps 8, 11–12, 14, 23, and 31 actually read the seven figures; steps 13, 22, and 31 give the tables' contents. All six equations and Algorithm 1 are additionally represented in steps 9–10 and 18–21. Step 32 reaches the data-availability statement and the references on pp. 11–12, so there is no premature stopping point.

“Caught” does not mean every descriptive detail in each composite inventory entry is reproduced. For example, step 8 omits the Fig. 1 caption's printed petaFLOP exponent and does not enumerate every domain; step 31 gives the sensitivity ranking without estimating bar endpoints. Both nevertheless explain what those figures show. The latter choice follows the prompt's instruction to avoid estimating unclear visual values. The reading preserves the substantive distinctions between the Fig. 6 scale and Table 2, and between Fig. A.7 and Table A.3.

No additional substantive claim was identified as falling outside the reference inventory. The annual or biannual reassessment proposal (21.5) and the conditional probability interpretation of the interval (20.4) are covered by S5.1h and S5.1g, respectively. The inventory remains unchanged.

**A3 — Strength of language: 1 (inconsistent, with small local shifts).** Most scope, units, and certainty survive: blue-water exclusions (9.2), the lack of full Bayesian inference (17.4), deterministic efficiencies (18.2), zero compute growth under sustainable transformation (19.3), the 2030–2050 sevenfold comparison (22.4), independent inputs (25.3), unmodelled waste heat (28.1), and the conditional 95% reduction relative to BAU (30.1). However, 2.1 drops the economic projection's “up to,” and 27.2 turns standards that could help prevent clustering into standards that could prevent it. These are local strengthenings, not a systematic shift across the document.

**A4 — Mechanical checks (pass/fail counts).** Checks covered the complete reading, not just the A1 sample. PDFKit extracted the article text; comparisons normalised Unicode compatibility forms and whitespace. Bibliographic checks additionally respected complete-entry boundaries and the work identified by the citation marker: substring presence alone is insufficient.

| Check | Pass | Fail | Separate image check |
| --- | ---: | ---: | --- |
| Texts marked `verbatim` | 1 | 0 | None |
| Numeric-token occurrences in claim/support text | 152 | 0 | 1 visually supported occurrence |
| Non-null reference-entry occurrences | 79 | 6 | None |

The sole verbatim passage is 24.2, the sentence about water sustainability and energy decarbonisation, found in §6.1, p. 8.

For reproducibility, numeric counts are lexical checks of digit sequences, allowing internal commas/decimal points, in the 156 claim texts and 74 support texts; they exclude locations, moves, meanings, citations, and reference entries. They include element identifiers and years, count repeated occurrences, and do not treat a power written as `10^9` as a single token. Of 153 token occurrences, 152 are present in extracted text, allowing comma removal for thousands. The remaining `0.04` in 23.2 describes Fig. 6's displayed values as below that bound; the rendered chart supports it. It is an image-based paraphrase, not an extraction failure. Token presence is only a mechanical check; A1 separately assesses contextual fidelity.

The six reference failures are three distinct malformed entries:

- **2.3.S1, 11.1.S1, and 18.1.S1:** `(Masanet et al., 2020)` is paired with an entry beginning “Masanet, E., 2025. The water use of data center workloads…”. This is the tail of the Lei et al. (2025) entry, beginning at its final author's name, rather than the complete Masanet et al. (2020) entry. The latter is “Recalibrating global data center energy-use estimates,” *Science* 367, 984–986, on p. 11.
- **4.3.S1:** the Lei et al. (2025) entry ends after “Lei, N., Lu, J., Shehabi, A.,”. P. 11 continues with Masanet, year, title, journal, and DOI. A fragment is not a matching complete entry.
- **3.2.S1 and 10.2.S1:** each Lin et al. (2024) reference field contains the complete Lin entry followed by the separate Masanet et al. (2020) entry. This violates the required one-entry-per-work boundary.

Thus 60/63 distinct reference-field strings pass and 3/63 fail; counting their repeated uses gives 79/85 passes and 6/85 failures. All 85 strings occur as text substrings, illustrating why a substring-only test would miss these extraction/boundary errors. None requires consulting an outside source to diagnose.

Separately, visual inspection confirms all seven figure descriptions, the table contents on pp. 5 and 10, and Algorithm 1's arithmetic and iteration structure. Table 2's values are available in extracted text on p. 7. Figure, table, equation, and algorithm readings are marked `paraphrased` and name their elements. The reading appropriately retains Fig. 4's cooling tower, Fig. 6's small printed decimal scale, and Fig. A.7's “EWE” label, rather than silently replacing them with expectations drawn from the prose or tables.

**A5 — Detail and readability (description, not a score).** There are **32 steps, 156 claims, and 74 support items**. Five steps cover the introduction, five cover drivers/accounting, three cover cooling, three cover geography, seven cover forecasting/results, five cover discussion, two cover conclusions/disclosures, one covers the Appendix, and one covers availability/references. The denser methods receive suitably finer treatment. Reading order follows the argument while identifying figures printed on subsequent pages. The three-component framework, cooling trade-offs, regional vulnerability, scenario assumptions, numerical outcomes, limitations, and recommendations can be followed from the reading alone. Explicit restatement notes generally avoid padding the claim list. Some support fields merely say that a work was cited rather than recording additional evidence, and several claims combine distinct propositions, especially 1.4–1.5 and 2.1; this reduces granularity without obscuring the main progression.

For the researcher, this is a comprehensive and predominantly faithful record of the article, particularly strong on methodological qualifications, units, scenario boundaries, and visual details that disagree with other printed elements. The principal weakness is bibliographic reliability: six reference fields contain truncated, misassociated, or concatenated entries despite the reading's assertion that entries were matched. Small local increases in certainty also warrant correction. The substantive coverage is extensive; the reference fields should be checked before using the reading to trace cited support across sources.
