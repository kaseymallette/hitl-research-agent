Article file: `article.pdf` — Lei et al., *The Water Use of Data Center Workloads: A Review and Assessment of Key Determinants*. The reference inventory identifies the source as `lei_et_al_2025_water_use_data_center_workloads.pdf`.

Seed: **20261107**. Sampled 30 of the run's 111 claims, without replacement, using Python `random.Random(20261107).sample(range(111), 30)`, then sorted the selected indices into document order. Each claim's attached support was checked separately. Below, `step.claim` and `S1`, etc. use one-based JSON array positions; global claim numbers are also one-based. Page numbers in the evidence table are PDF pages, including the repository cover.

## A1. Attribution fidelity

**Claims: score 2 — 29/30 (96.7%); score 1 — 1/30 (3.3%); score 0 — 0/30 (0%).**

**Attached support: score 2 — 28/28 (100%); score 1 — 0/28; score 0 — 0/28.** No sampled passage was unlocatable. These are separate distributions, not an average or a pooled claim-and-support score.

| Global claim | JSON position | Claim score | Support scores, in order | Article evidence and finding |
| --- | --- | --- | --- | --- |
| 5 | 2.1 | 2 | 2, 2 | p. 3, §1, lines 2–5: services and operating resource requirements; both cited groups are attached to the corresponding statements. |
| 9 | 3.1 | 2 | 2, 2 | pp. 3–4: operator adoption and simplicity; Facebook/Scaleway and Meta citations are present. |
| 10 | 3.2 | 2 | 2 | pp. 3–4: onsite and combined onsite/offsite water are each divided by IT electricity. |
| 20 | 5.3 | 2 | 2 | p. 6, lines 5–7: extension to other tests, including MLPerf, retains the sufficient-data condition. |
| 22 | 6.2 | 2 | — | p. 7, lines 6–12: upstream fuel/equipment and generation-stage consumption categories. |
| 23 | 6.3 | 2 | 2 | p. 7, Eq. (1) and definition: onsite plus facility electricity times grid WCF; freshwater consumption per generated kWh. |
| 24 | 6.4 | 2 | 2 | pp. 7–8, Eqs. (2)–(3): the common server factor and PUE denominator are correctly distinguished. |
| 28 | 7.3 | 2 | 2 | p. 9, lines 2–8: utilization/year LLKR models, annual efficiency variation, SPECpower provenance. |
| 31 | 8.3 | 2 | 2 | p. 10, lines 1–12: all ten archetypes, including both liquid-cooling arrangements and conditional backup. |
| 32 | 8.4 | 2 | — | p. 10, lines 12–15: supplemental cooling activates when primary methods cannot maintain setpoints, typically in extreme weather. |
| 37 | 10.1 | 2 | 2 | pp. 11–13, §3.1/Fig. 2: 2023 assumption, generally joint determinants, and compensation example. The support correctly distinguishes the prose's A/B assignment from the actual plotted panels and coordinates. |
| 40 | 10.4 | 2 | 2 | p. 12, lines 5–7, and Fig. S5.3, p. 48: refresh improvement operates across utilization levels as newer servers improve. |
| 43 | 11.2 | 2 | 2 | p. 14, lines 1–6/Fig. 3: equal facility water with opposing WUE-site/server-efficiency combinations; A/B orientation is correct. |
| 49 | 13.1 | 2 | 2 | pp. 16–18, §3.4/Fig. 5: broad technology-specific regions combine climate, operations and server workload efficiency. |
| 52 | 13.4 | 2 | — | p. 17, lines 7–10: the listed technologies can reduce both intensities, with substantial electricity reduction from adiabatic cooling. |
| 55 | 14.2 | 2 | 2 | pp. 19–20, §3.5/Fig. 6(a–b), and Eq. (4): horizontal extent, indirect uplift and all eight printed WCF values are faithfully paraphrased. |
| 57 | 14.4 | **1** | — | p. 20, lines 1–4: operational improvement is limited by climate/cooling, whereas low-WCF power is a more general approach that is **not constrained** by cooling implementation, but by grid options. “Less dependent on cooling technology” weakens that categorical distinction. The grid constraint survives. |
| 71 | 19.2 | 2 | — | p. 28, lines 5–12: potential bill/carbon benefits and the authors' strong-evidence inference for policy and operating measures. |
| 72 | 19.3 | 2 | — | p. 28, lines 13–18: SPECpower representativeness concerns and possible underestimation of upper water-use bounds retain their uncertainty and direction. |
| 73 | 19.4 | 2 | 2 | p. 28, lines 18–23: future GPU/storage/network scope and omitted variation in generation-weighted U.S. WCFs; Lee citation present. |
| 78 | 20.4 | 2 | — | pp. 29–32: online SI/data/code pointer followed by references; no external repository content is claimed. |
| 85 | 23.2 | 2 | 2 | pp. 36–37, S2/Fig. S2.1: idle zero, utilization/vintage trends, widening efficiency gap and nonlinear surfaces. |
| 89 | 25.1 | 2 | 2 | pp. 40–41, Table S3.1: elevated liquid-system temperatures, economizer/dry-cooler operation, tower consumption, wet-mode precooling and backup types. |
| 90 | 25.2 | 2 | 2 | pp. 41–42, Table S3.1 note: conditional backup and naming convention for air-cooled IT. |
| 94 | 27.2 | 2 | 2, 2, 2 | pp. 44–45, S4/Table S4.1: correct source ordering, upstream/generation/total rows and hydro N/A. The support preserves the table's 0.0148 wind total and separately identifies Fig. 6(b)'s 0.011. |
| 98 | 29.1 | 2 | 2 | pp. 47–48, S5/Fig. S5.3: generally shorter refresh helps, less than utilization/hardware changes, especially at low utilization; panels, utilization levels and efficiency-endpoint bands are correctly described. |
| 100 | 30.1 | 2 | 2 | pp. 49–50, S6/Fig. S6.1: climate and operating-efficiency differences within the specified cooling archetype and within a climate. |
| 102 | 30.3 | 2 | — | p. 51, S6: all five water-cooled-chiller configurations plus the liquid/dry-cooler case form the higher-water cluster, with the stated evaporation mechanisms. |
| 104 | 31.1 | 2 | 2, 2 | p. 52, lines 8–16: two heat-rejection systems, three equipment scenarios and the two corresponding cooling-literature citation groups. |
| 105 | 31.2 | 2 | 2, 2 | pp. 53–55, S6/Table S6.1/Fig. S6.3: small annual differences; the authors' ordering is distinguished from its weak visual discernibility. Temperature ranges and differing panel scales match. |

The sampled claims and support are all marked `paraphrased`, appropriately including visual and equation readings. Descriptions of discrepancies in Fig. 2 and Table S4.1/Fig. 6 are traceable observations of the document, not invented repairs to the authors' results. The one verbatim claim falls outside the random sample and is checked under A4.

## A2. Coverage

Counts use the supplied reference inventory unchanged. “Caught” means the substantive claim or visual content is represented somewhere in the reading; it does not require a duplicate claim when the conclusion restates earlier material. Coverage is independent of the fidelity adjustment under A1.

| Reference type | Caught with substance | Named without what it shows | Missed | Evidence |
| --- | ---: | ---: | ---: | --- |
| Enumerated contributions | 4/4 | 0 | 0 | C01–C04: step 17's three claims cover the four contributions; its final claim combines the parametric-analysis and server-workload-efficiency contributions. Earlier methods/results supply their determinant detail. |
| Abstract claims | 7/8 | 0 | 1 | A01–A07: step 1 covers context/purpose, the three magnitudes, the full determinant ordering and tailored combinations. **A08 is missed as an explicit claim** that the analysis fills critical knowledge gaps by identifying determinants and exploring achievable minima under site constraints. Those topics recur separately, but the abstract's self-assessment is not recorded. |
| Conclusions, main text | 49/49 | 0 | 0 | M01a–M14h: steps 2–20 cover the inventory's substantive conclusions and methodological claims. Restatements in M13 are represented by earlier claims and step 17's recapitulation/contributions. |
| Conclusions, SI | 10/10 section groups | 0 | 0 | S01–S10: steps 21–34 include each section, including all three S6 topics and S10's provenance inventory. Counted by the reference's ten section headings, rather than treating its multi-bullet summaries as additional sections. |
| Figures | 20/20 | 0 | 0 | F01–F08: steps 5, 10–16; F09–F20: steps 23, 26, 28–33. Each figure has an account of its content, trend, mechanism or comparison. |
| Tables | 6/6 | 0 | 0 | T01: step 21; T02: steps 24–25; T03: step 26; T04: step 27; T05: step 31; T06: step 34. |

The reading reaches the final SI bibliography on PDF p. 60. It does not stop at the main text: the final scientific material, S10/Table S10 on PDF pp. 58–59, is included. Figure coverage is substantive without being exhaustive: for example, Fig. 1's calculation structure is read without transcribing every determinant box, and Fig. 8's ranking and overlapping top-three intervals are described without estimating unlabeled indices.

Found beyond the list: step 8.1 preserves §2.3's claim that the metrics are sporadically reported and poorly understood by sustainability analysts (PDF p. 9, lines 10–14); step 22.1 preserves S2's quarterly database updates and vendor/organization submissions (PDF p. 35, lines 2–5). These details are confirmed in the article but not explicitly inventoried as such in the reference list. The acknowledgements and reproducibility pointer in step 20 are also accurate, although the inventory expressly excludes that apparatus from its scientific conclusions.

## A3. Strength of language

**Score: 1 — inconsistent, with localized softening rather than a systematic directional shift.**

Most scope and certainty survive: the sufficient-data condition on MLPerf extension (5.3), U.S.-average WCF basis and geographic limitation (9.2), 2023 newest-server assumption and “generally”/“usually” in the joint-factor result (10.1), approximately 40% diminishing-return threshold (10.3), low-WCF exceptions (15.2 and 33.1), and the possible upper-bound underestimation from benchmark selection (19.3). The reading also retains strong recommendations, including workload efficiency as the “most effective” strategy under grid/climate constraints (18.2), and the authors' “strong evidence” policy inference (19.2).

The sampled 14.4 softens the absence of a cooling-implementation constraint to reduced dependence. Elsewhere, 12.4 says favorable climates and efficient operation “tend to yield” low PUE/WUE-site, where §3.3 states that these conditions “result in” low values (PDF p. 15, lines 13–15). These are small but real departures from the requested strength. They coexist with extensive preservation of the authors' qualifications and do not support a score of 0.

## A4. Mechanical checks

I extracted all 60 pages with `pypdf`, parsed the JSON, and checked quotations, numeric strings and bibliography entries programmatically. PDF pages were also rendered with `pypdfium2` and the relevant visuals inspected. Normalization removed layout whitespace and manuscript line/page numbers and used Unicode NFKC; it did not rewrite wording, punctuation, reference titles or numeric precision. Line numbers attached directly to line-wrapped URLs were removed as page apparatus, preserving the URL's hyphens.

| Check | Pass | Fail | Separate visual checks / denominator |
| --- | ---: | ---: | --- |
| Verbatim claim/support texts | 1 | 0 | Only step 1.4 uses `verbatim`; the complete sentence is present in the abstract, PDF p. 2, lines 22–23. |
| Distinct digit-written numeric forms found in extracted text | 64 | 0 | 13 further forms are absent from extracted text and confirmed visually below; 77 distinct forms checked in total. |
| Reference-entry occurrences matching the article's bibliographies | 127 | 0 | These represent 52 distinct non-null reference strings; all 52 match. No entry is null. |

For the numeric count, the unit is a **distinct written numeric form**, not an occurrence: `1.17` and `1.170` remain different forms. The inventory covers claim/support text, including percentages, quantile numbers, years and climate-code digits; it excludes location strings, element/equation identifiers, citation metadata, the benchmark's name/year, and the DOE contract identifier. Numbers written as words are assessed for meaning in the reading, not counted as digit strings. A matching numeric string alone cannot establish its context; the passage and visual comparisons above check those contexts.

The 13 visual-only forms are six Fig. 6(b) labels—**1.170, 2.200, 2.900, 4.280, 6.800, 11.090** (PDF p. 20, step 14.2 S1)—and seven percentages in raster Table S.1—**50.0, 33.3, 25.0, 20.0, 16.7, 14.3, 12.5** (PDF p. 34, step 21.2 S1). All 13 pass visual comparison and are excluded from text-match failures. The remaining Fig. 6(b) values, 0.011 and 0.034, were also visually confirmed, even though those strings occur elsewhere in extracted text. Table S.1's 100% is an honest paraphrase of printed 100.0%, and its equal-share interpretation matches the rows.

Visual readings throughout are marked `paraphrased` and name the relevant element. Checks confirm the Fig. 2 A/B panel assignments and coordinates; Fig. 3's equal-water example; Figs. 4–7's regions and tradeoffs; Fig. 8's overlapping top-three confidence intervals; the SI response surfaces, scenario flowchart, boxplots and refresh bands; Table S6.1's 2–32/2–40/2–45 °C ranges; and the S7/S8/S9 examples. Equation readings are also paraphrased and identified: the main-text multiplicative decomposition and fleet model, including Eq. (5)'s printed 3.6, and S1–S3's regression/kernel setup are represented correctly. No image-derived wording is falsely presented as a quotation.

The run appropriately preserves location-specific disagreements instead of completing or correcting the source: wind is 0.011 in Fig. 6(b) and 0.0148 in Table S4.1; Fig. S7.1's caption reverses the efficiency/extrema correspondence; and Fig. S8.1's legend includes nuclear and labels the highest series hydro despite prose naming geothermal. Step 14.3 attributes the 34-fold and 4.5-fold examples specifically to the prose; it does not claim to derive those ratios from the image. The latter distinction matters because the displayed C/D separation does not visually support a 4.5-fold ratio.

## A5. Detail and readability

The reading contains **34 steps, 111 claims and 114 support items**: 20 steps through the main manuscript and its closing apparatus, followed by 14 through the supplement. It follows source order and covers every substantive section. Technical density varies more than the stated short-step plan suggests: step 8 takes in ten cooling systems plus climates and quantiles, step 14 covers all of §3.5 and three figure panels, and step 31 combines multiple liquid-cooling comparisons. Nevertheless, their claim/support divisions keep these stretches navigable.

A reader can reconstruct the argument: inadequacy of electricity-denominated WUE for workload comparison; the server workload multiplier; joint climate/cooling/operation effects; upstream electricity-water effects; conditional strategies; and data/boundary limitations. The separate moves and meanings generally explain transitions without judging the argument. Support items frequently say only that a cited work supplies a model or example, rather than preserving its substantive evidentiary detail, so the JSON is better at tracing provenance and conclusions than independently reconstructing every model input. It also bundles distinct claims, including three abstract magnitude claims in 1.2 and two enumerated contributions in 17.3. Some SI repetition is justified by added assumptions, uncertainty and visual detail rather than padding.

For the researcher: this is a broadly comprehensive and highly faithful reading, particularly useful for preserving workload units, geographic boundaries, cooling tradeoffs and conflicts between prose and figures. The seeded sample contains no unsupported claim or support item, and the quotation and reference checks pass. Its main limitations are localized softening, omission of the abstract's explicit knowledge-gap/minima self-assessment, and compression of distinct claims and supporting detail. These findings inform review of the analysis; they do not constitute an acceptance decision.
