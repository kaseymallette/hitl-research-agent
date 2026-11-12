# Close-reading judgment

Article file: `article.pdf` — Pengfei Li et al., “Making AI Less ‘Thirsty’,” printed pp. 54–61.

Sampling seed: **20261107**. Flatten claims in `reading_path` order, then within each step in array order; number them C1–C114. Sample without replacement using Python `random.Random(20261107).sample(range(114), 30)`, then sort and add one for reporting. The sample is C5, C9, C10, C20, C22, C23, C24, C28, C31, C32, C37, C40, C43, C49, C52, C55, C57, C71, C72, C73, C78, C85, C89, C93, C94, C101, C103, C104, C105, C108. All 24 support items belonging to these claims were checked separately.

Locations below use printed article pages. Step/claim identifiers such as 9.1 mean the ninth step's first claim. The fixed claims reference was used unchanged. Only the five authorized input files were read; the argument evaluation and existing judgments were not opened. PDF text was extracted with pypdf, and rendered pages were inspected for the illustrations, figures, table, equations, and reference-list layout.

## A1. Attribution fidelity

**Sampled claims: score 2 = 29/30 (96.67%); score 1 = 1/30 (3.33%); score 0 = 0/30 (0%).** No sampled passage was unlocatable. **Sampled support items: score 2 = 24/24 (100%); score 1 = 0; score 0 = 0.** All sampled claims and supports are marked `paraphrased`, honestly. Support scores concern their stated content and attribution; many are descriptions of the article's citations rather than substantive evidence summaries.

| Claim | Step.claim | Claim score | Support scores, in order | Passage and finding |
| --- | --- | ---: | --- | --- |
| C5 | 1.5 | 2 | None | p. 54, opening paragraph: conditional sustainability/social-conflict warning and limited, unevenly distributed freshwater. |
| C9 | 2.4 | 2 | 2, 2 | p. 54, corporate growth paragraph: approximately 20%/17% and 34%/22%, correct periods and Google/Microsoft citations. |
| C10 | 2.5 | 2 | 2 | p. 54: 2028 onsite consumption could double or quadruple, approximately 150–280 billion L; citation 25. |
| C20 | 4.4 | 2 | None | p. 56: urgency framed by scarcity, drought, infrastructure, and avoiding water stresses that outweigh benefits. |
| C22 | 5.1 | 2 | None | p. 56, roadmap: holistic water-and-carbon approach, reinforced by its closing necessity claim. |
| C23 | 5.2 | 2 | None | p. 56, roadmap: method includes operational and embodied water. |
| C24 | 5.3 | 2 | 2 | p. 56: GPT-3 size, U.S. Microsoft scenario, 5.4 million L total and 700,000 L onsite. Support correctly distinguishes citation 4 for the model from the authors' water estimate. |
| C28 | 6.1 | 2 | 2 | pp. 56–57, withdrawal definition: sources, uses, temporary/permanent removal and normal hydropower exclusion; citation 22. |
| C31 | 6.4 | 2 | 2 | p. 57: downstream availability and watershed scarcity; citation 22. |
| C32 | 6.5 | 2 | 2, 2 | p. 57: distinct WWF/WCF and default WCF convention; citations 5,23 and 27 retained. |
| C37 | 7.5 | 2 | 2 | p. 57, Figure 1 and caption: onsite cooling-tower/heat-exchanger pathway, offsite power-plant water, illustrative AI icons. Image confirms the paraphrase. |
| C40 | 8.3 | 2 | None | p. 57, cooling towers: withdrawal includes make-up for evaporation and discharge; consumption is evaporation only. |
| C43 | 9.1 | **1** | 2 | p. 57, assisted outside-air cooling: the article requires evaporation for excessive heat, then says water is also needed for humidity control in dry air. The reading extends “evaporation is still needed” to humidity control, specifying a mechanism the passage does not explicitly attach to that condition. The broader claim and citation 14 remain supported. |
| C49 | 10.1 | 2 | 2 | p. 58: thermoelectric power among top withdrawal/consumption sectors in many countries; citation 23. |
| C52 | 10.4 | 2 | 2, 2 | p. 58: U.S. averages about 43.8 L/kWh withdrawal and 3.1 L/kWh consumption; citations 32 and 23 correctly separated. |
| C55 | 11.2 | 2 | None | p. 58, scope 3: ultrapure wafer water, plant cooling and potentially hazardous discharge. |
| C57 | 11.4 | 2 | 2, 2 | p. 58: scope 3 obscure but likely significant; citation 7 and Apple's 99% supply-chain example, citation 2. |
| C71 | 14.4 | 2 | None | p. 59: annualized WUE and estimated server energy permit a rough estimate. |
| C72 | 15.1 | 2 | 2 | p. 59, case opening: article's ChatGPT description and full 175-billion-parameter GPT-3 case; citation 4. |
| C73 | 15.2 | 2 | None | p. 59: embodied water excluded because public scope-3 data are unavailable. |
| C78 | 15.7 | 2 | 2, 2 | p. 59, training: 3.14 versus 4.35 L/kWh, undisclosed actual site, alternative Microsoft sites, Singapore/Taiwan exclusions; citations 23 and 25. |
| C85 | 17.3 | 2 | 2 | p. 59, inference: official 0.4 kWh/100 pages, approximately 0.004 kWh/page; the article itself prints citation 4. |
| C89 | 18.2 | 2 | 2 | p. 60, Figure 2b and caption: Virginia, five days from April 4, 2022, hourly series and Pearson 0.06; calculation basis and citations 23,32,33 match. |
| C93 | 19.3 | 2 | 2 | p. 60: chosen 3.14 L/kWh conservative against recent 4.35 L/kWh; citation 25. |
| C94 | 20.1 | 2 | 2 | p. 60: later models could consume more for the same request, especially reasoning, without official resource information. The unusual printed citations 3,26 are faithfully preserved. |
| C101 | 21.5 | 2 | 2 | pp. 60–61: limited embodied-water data motivate scope-3 research and stewardship; Apple citation 2. |
| C103 | 22.2 | 2 | None | p. 61: midnight and/or a more water-efficient datacenter offered as an example. |
| C104 | 22.3 | 2 | None | p. 61: some informed, water-conscious users may shift inference; information and willingness remain conditional. |
| C105 | 23.1 | 2 | None | p. 61: following abundant solar energy is preferable for carbon reduction. |
| C108 | 23.4 | 2 | 2 | p. 61: non-substitutability corroborates earlier findings; citations 10,25 match. |

## A2. Coverage

Counts use the reference's inventory units; repeated conclusions count as caught when their content is recorded earlier and their recurrence is identified in the conclusion step, as the reading instructions require.

| Type | Reference units | Caught with substance | Caught without what they show | Missed |
| --- | ---: | ---: | ---: | ---: |
| Contributions: prose roadmap K1–K6 | 6 | 6 | 0 | 0 |
| Formally labeled abstract claims | 0 | 0 | 0 | 0 |
| Opening/deck summary S1, reported separately | 1 | 1 | 0 | 0 |
| Section/subsection content and conclusions C01–C40 | 40 | 40 | 0 | 0 |
| Numbered figures F1–F2 | 2 | 2 | 0 | 0 |
| Tables T1 | 1 | 1 | 0 | 0 |

There is no labeled abstract or formally enumerated contribution list. K1–K6 are the reference's six prose-roadmap units, all represented in step 5. C01–C06 appear in steps 1–5; C07–C16 in steps 6–11; C17–C22 in steps 12–14; C23–C29 in steps 15–20; C30–C35 in steps 21–23; and C36–C40 in step 24's recap moves/meaning together with the previously recorded claims and its explicit priority claim.

F1 receives a substantive reading at 7.5. All three F2 panels are read at 18.1–18.3, including the Virginia/date restriction, correlation, regional comparison and fuel categories. Counting panels separately gives **3 caught, 0 merely named, 0 missed**. Unnumbered art V1 is also described in step 3's meaning: **1 caught, 0 merely named, 0 missed**.

T1 is substantively caught, but selectively transcribed. Step 16 records all 18 rows' training totals, request totals and requests per bottle, the complete U.S.-average row, India's zero-onsite example, units and projected-facility markers. It omits most other rows' PUE/WUE/EWIF inputs and onsite/offsite component values, and does not explicitly state that offsite exceeds onsite in every row. These are limitations of detail, not a merely named or wholly missed table.

**Missed inventory units: none.** The reading reaches the substantive endpoint, Conclusion on p. 61, and continues through funding, references, biographies and license. No substantive author claim beyond the reference inventory was found. Step 25 adds apparatus details outside that inventory. Its count/classification of the 33 references is an accurate reader observation placed among claims, rather than an explicit proposition asserted in the article; this is a minor attribution-boundary issue outside the random sample and does not change the reported A1 distribution.

## A3. Strength of language

**Score: 1 — inconsistent in a narrow instance, with no systematic directional shift.** C43 makes the dry-air humidity-control mechanism more specific than the passage does, as detailed under A1. Most conditions, units, scope and certainty survive well: the U.S.-only 2028 comparison remains contingent on the forecast (3.5); corporate quantities remain datacenter-wide, with colocation excluded (2.2 and step 2's meaning); scope 2 stays location-based (3.6); scope 3 remains “likely” significant (11.4); the practical method remains rough (14.4); and the case excludes embodied water and acknowledges the unknown training site (15.2, 15.7). Later-model use remains “could,” per-request reductions “may,” and aggregate growth “likely” (20.1–20.3). Scheduling examples and willing-user participation remain conditional (22.2–22.3), and water–carbon conflict remains potential (23.2–23.3). The isolated mechanism shift should not be read as pervasive inflation of the article's conclusions.

## A4. Mechanical checks

These are full-run checks, separate from the A1 sample. The checked text population is every claim's and support item's `text` field: **114 claims plus 80 supports = 194 texts**. Locations, moves, meaning, reading plan and bibliographic strings are excluded from the numeric-text denominator; references are audited separately.

| Check | Pass | Fail | Basis |
| --- | ---: | ---: | --- |
| Texts marked `verbatim` | 0 | 0 | None of the 194 texts uses that marker; all are `paraphrased`. This is not evidence of tested quotation accuracy. |
| Numeric-token occurrences in ordinary claim/support text | 126 | 0 | Found in extracted article text after normalizing thousands separators. Count includes years, model/scope numbers and identifiers as well as quantitative values. |
| Numeric-token occurrences in figure/table/equation-reading claim/support groups | 98 | 0 | Reported separately: all are also present in this PDF's text layer. Rendered visual content was checked as described below. |
| Reference-entry occurrences | 86 | 0 | 33 distinct entries, all matching the article's own reference list; no null entries. |

The numeric check uses digit sequences with optional comma grouping and decimal fractions; ranges contribute their endpoints. It is a presence check, not proof that every matched token has the right unit or attribution. A1 supplies contextual checking for the sample. Totals across both numeric groups are **224 passes, 0 failures**.

For references, Unicode compatibility normalization and removal of whitespace accommodate line and URL wrapping without correcting bibliographic content. **85/86 occurrences, covering 32/33 distinct entries, match automatically.** The remaining Karimi entry (8.5, support 2; reference 11) crosses from the bottom of the middle column to the top of the right column on p. 61; its two extracted fragments are separated by the extractor's reading order. Inspection of the rendered page confirms the entry as recorded, making the final count 86/86 and 33/33. Printed oddities such as “LarochelleH.” and the capitalization in the Solomon title have not been silently repaired.

Visual checks: F1's pathways and illustrative icons agree with 7.5; V1 agrees with step 3's description; F2's three panels agree with 18.1–18.3. The 0.06 correlation is printed in the caption, not estimated from a curve. All **66 table-cell numeric occurrences transcribed in step 16** agree with Table 1, including the U.S.-average split, every location's three selected outputs, and the five selected India inputs/components. The 500 mL denominator and July 2023 projection qualification also agree. The offsite weighted average (13.1), operational sum with PUE on the offsite term (13.4), embodied allocation (14.2) and total sum (14.3) agree with the equations on pp. 58–59. These visual/equation readings are correctly marked paraphrased and identify their source elements; none is counted as a quotation or an extraction failure.

## A5. Detail and readability

The reading has **25 steps**, with 114 claims and 80 support items. Five steps cover the opening/roadmap; six cover background; three develop the accounting method; six cover the case study and Figure 2; three cover recommendations; one handles the conclusion and one the apparatus. Coverage remains continuous through the article's end. Short technical and visual steps are reasonable, though the many small steps and extensive numerical lists make the treatment more granular than its announced usual 200–500-word pace.

A reader could reconstruct the main argument: overlooked water use and growth motivate separate withdrawal/consumption accounting; three scopes lead to operational/embodied equations; a bounded GPT-3 scenario illustrates scale and location dependence; reporting and scheduling follow, qualified by water–carbon tradeoffs. Moves and meaning usually explain these connections without putting the model's judgments into author-claim fields. The distinction between the official per-page energy estimate and the authors' assumed per-request energy is particularly useful. Support fields often identify a cited work instead of reproducing the substantive evidence, leaving some claim–evidence connections distributed across neighboring claims. There is also avoidable repetition of the EWIF comparison and transparency/holistic-sustainability framing, although the concluding recap is appropriately treated as restatement. Table transcription is lengthy but still selective, as noted under A2.

For the researcher: this is a broadly faithful, comprehensive record, especially strong on accounting boundaries, uncertainty, the inference assumption and visual evidence. The sampled claims contain one small mechanism overstatement and no unsupported inventions; the mechanical checks find no numeric or bibliographic mismatches. Its principal limitations are selective table detail, support fields that frequently record provenance rather than evidence, a small apparatus observation placed among author claims, and some repetition. These findings inform the collection decision without supplying a pass threshold or substituting for the researcher's reading.
