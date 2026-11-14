Article: `article.pdf` — Ceres, *Water Behind the Watts: The Hidden Risk of Powering Data Centers* (August 2026).

Seed: **20261111**. Claims were flattened in reading-path order, preserving their order within each step, and sampled with Python `random.Random(20261111).sample(range(115), 30)`. The table below sorts the resulting sample into document order. Claim and step numbers are one-based; PDF pages mean physical pages, not printed footer numbers.

## A1. Attribution fidelity

**Claims: 28/30 at 2 (93.3%); 2/30 at 1 (6.7%); 0/30 at 0 (0%).** All 30 passages were located. The sample contains **12 support items: 12 at 2, none at 1 or 0**. Support scores are separate from claim scores; an accurate support item does not repair an altered claim. All sampled claims and support items are marked `paraphrased`.

| Claim | Step.claim | PDF page | Claim score | Support scores | Evidence |
| --- | --- | --- | --- | --- | --- |
| 6 | 3.2 | 2 | 2 | — | The Executive Summary explicitly says electricity-generation water should enter the policy conversation. |
| 10 | 4.2 | 3 | 2 | — | The visible overview gives 78% of electricity and over 90% thermal generation in Ohio, Georgia, and Virginia. The paraphrase retains the generation denominator. |
| 15 | 5.2 | 3 | 2 | — | Finding 5 states the majority's purchased-electricity risk gap, the internal-cooling focus, and the few companies disclosing indirect water. |
| 19 | 6.3 | 5 | 2 | 2 | The background projects a 72% share of total U.S. data center water consumption in 2030 despite improved cooling and reclaimed water. The support describes that projection without changing it. |
| 21 | 7.2 | 5 | 2 | — | The water-risk subsection describes facilities in stressed regions obtaining water-intensive power from stressed regions, compounding risk. |
| 24 | 7.5 | 5 | 2 | 2 | Operational constraints from shortages or community concerns are explicit; coal/nuclear curtailment and drought-reduced hydropower are the report's examples. |
| 26 | 8.1 | 5–6 | 2 | — | The assessment discussion lists plant technology, cooling, fuel, water sources, seasonality, basin stress, and drought. |
| 33 | 9.2 | 7 | 2 | 2 | Data Analysis identifies 3,907 active plants, the 1 MW threshold, and 1,434 water-dependent plants excluding saltwater/brackish use; EIA forms and Figure 1 are identified there. |
| 35 | 9.4 | 7 | 2 | 2 | The method explicitly applies EPRI's 2024 state electricity shares and assumes same-state electricity sourcing. |
| 37 | 10.1 | 7 | 2 | — | The final methods paragraph contrasts permanent local loss with the full volume needed for operation and calls withdrawals a strong risk indicator. |
| 41 | 11.2 | 8 | 2 | 2 | The rendered comparison graphic confirms all six annual billion-gallon volumes and all three multiples. The support correctly distinguishes state data center withdrawals from city water use. |
| 45 | 13.2 | 10 | 2 | — | The prose gives 1,434/3,907 plants, 37%, and 1,142/1,467 TWh, almost 78%, with a 2024 basis. |
| 47 | 13.4 | 10 | 2 | 2 | The prose explicitly gives California's 57% and Ohio's 95% thermal shares. Figure 3 supports the described contrasts and water-source categories; adjacent prose also identifies battery storage among minimal-water facilities. |
| 57 | 16.2 | 13 | 2 | — | The state comparison gives California's 66% stressed-basin generation and limited drought, and describes Ohio as having drought exposure but few plants facing stress. That plant/generation wording comes from the article. |
| 59 | 16.4 | 13 | 2 | 2 | The article explicitly qualifies annual and seasonal variation and gives California's 2021 low-reservoir hydropower example. |
| 61 | 17.2 | 14 | 2 | — | The California case gives about 39% of hydropower water in medium-high to extremely high stress basins in 2024. |
| 62 | 17.3 | 14 | 2 | — | The case identifies evaporation, drought, storage requirements, and river-flow requirements as possible generation constraints. |
| 72 | 19.5 | 15 | 2 | 2 | The producer discussion reports NRG's 77% withdrawal reduction through cooling towers and coal-to-gas transition. The support faithfully describes that example. |
| 75 | 21.1 | 16 | 2 | 2 | The opening paragraph names Amazon, Microsoft, and Apple as direct-water target/strategy examples. |
| 79 | 22.1 | 17 | 1 | — | The prescribed assessment dimensions are accurate. But “will improve evaluation and mitigation” strengthens the report's narrower promise: assessments support better evaluation and inform more effective mitigation strategies. It converts assistance to strategy development into an outcome claim. |
| 82 | 23.2 | 17 | 2 | — | The recommendation calls for collaboration with producers on supplier-region stress/drought and support for existing mitigation efforts. |
| 84 | 23.4 | 17 | 1 | — | The collaborative methodology/database recommendation is supported, but “this will provide” an accessible standardized approach strengthens the article's “will support” such an approach. The difference is small but changes the strength of the promised result. |
| 88 | 25.1 | 18 | 2 | — | The first policymaker bullet calls for standardized direct/embedded-water reporting to improve consistent access to risk/impact information. |
| 89 | 25.2 | 18 | 2 | — | The next bullet calls for lower-water technologies and conservation to scale savings and sustain resilience for all users. |
| 97 | 27.2 | 19 | 2 | 2 | Scope and selection give 5,230 plants, 3,907 active, 1,434 retained, the listed exclusions, and the 2024 EIA forms. |
| 102 | 28.2 | 19 | 2 | 2 | Water risk characterization maps plant coordinates to WRI Aqueduct 4.0 baseline annual watershed stress. |
| 103 | 28.3 | 19 | 2 | 2 | The appendix names the USDM institutions, 2024 weekly categories, 53 periods, multiband raster, and three-month D1 threshold. |
| 105 | 29.1 | 19–20 | 2 | — | The limitations explicitly state directional estimates, self-reporting to EIA, and lack of independent verification. |
| 113 | 31.2 | 21 | 2 | — | All four lead-author names and their job titles match the acknowledgments. |
| 114 | 31.3 | 21 | 2 | — | Editorial/design credits and Bluerisk strategic support/review match the final page. |

The PDF's hidden duplicate overview text was not treated as evidence against the reading. The rendered page 3 supports electricity shares of 66% and 44%; the conflicting extracted plant-count wording and 46% are not the visible finding.

## A2. Coverage

Counts use `02_claims_reference.md` as written. “Caught” means the content is recorded somewhere in the reading, including support and explicit restatement moves; it does not require repetition at every location. Coverage is separate from fidelity: an altered qualifier can still leave a reference item caught.

| Reference type | Inventory | Caught with content | Caught without what it shows | Missed |
| --- | --- | ---: | ---: | ---: |
| Contributions/results | C01–C05 | 5 | 0 | 0 |
| Abstract-like Executive Summary claims | A01–A08 | 8 | 0 | 0 |
| Section/subsection claims and conclusions | S01–S39, S30a–S30b | 41 | 0 | 0 |
| Recommendations, including section premise | R00–R17 | 18 | 0 | 0 |
| Appendix claims and qualifications | M01–M11 | 11 | 0 | 0 |
| Final back matter | B01–B02 | 2 | 0 | 0 |
| Figures and analytical graphics | F01–F06 | 6 | 0 | 0 |
| Tables | None in article | 0 | 0 | 0 |

The conclusion-related subtotal is **72/72**, comprising the S, R, M, and B groups. The reference's unnumbered overall conclusion is also covered through its constituent findings, recommendations, and qualifications; it is not counted again as an independent item.

Evidence for the mapping:

- Steps 2–3 cover the Executive Summary, supplemented by the later assessment/collaboration recommendations for A06. Steps 4–5 record all five enumerated findings, later developed in steps 11–21.
- Steps 6–10 cover S01–S16, including the national consumption projection, cooling tradeoff, renewable procurement constraints, methods, and exclusions. Steps 11–21 cover S17–S39 plus S30a–S30b. AEP and Dominion's figures and disclosure gaps appear as support in step 20; Meta's disclosure appears as support in step 21. Their placement does not make them omissions.
- Steps 22–26 cover R00–R17: the introduction identifies the turn to practical prescriptions and every one of the 17 stakeholder bullets is represented. Steps 27–30 cover M01–M11; step 31 covers B01–B02.
- F01 is read in step 5 as a categorized plant-location map. F02 is read in step 11 as state-versus-city annual volumes and multiples. F03 is read in step 12 as current values and four growth scenarios. F04 is read in step 13 as generation shares by water/technology category. F05 is read in step 14 as total fleet withdrawals divided between hydropower and thermal generation. F06 is read in steps 15–16 as generation exposed to stress, drought, and their intersection. None is merely named.

**Missed items: none.** The reading reaches PDF page 21, including the appendix limitations through page 20 and the final acknowledgments. It does not stop at the main-text endpoint on page 18. The inventory's illustrative photographs introduce no additional analytical findings requiring separate figure counts.

**Found beyond the list:** Step 4 records the overview's plain-language definition of water stress as demand close to or exceeding supply, confirmed on rendered PDF page 3. The reference records the stress categories but does not separately inventory this definition. Step 31 also preserves the authors' job titles, confirmed on page 21; these are additional provenance details within B02, not a new research result. The reference list was not changed.

## A3. Strength of language

**Score: 1 — inconsistent, with small local shifts rather than a systematic change of certainty.**

The reading preserves the important qualifications across most of the document: the conditional 4.1–7.6 trillion-gallon scenario range; estimated withdrawals versus consumption; the 2024 snapshot; the distinction between percentages of plants and generation; national versus seven-state figures; the in-state allocation assumption; reported versus modeled inputs; and the geographic limits on applying fleet estimates to individual facilities. Step 20 retains the concession that broader producer planning *may* capture data center demand. Step 21 correctly retains Oracle's announced change and expected benefit.

The two sampled recommendation claims identified under A1 strengthen enabling language into more direct outcomes. Outside the sample, step 18.1 softens the California/Illinois case page's statement that most Illinois nuclear capacity is concentrated in the northwest into “much capacity.” Step 19.1 also narrows “Texas's Vistra” disclosing its plants to Vistra disclosing “Texas power plants”; the article's possessive identifies the producer and does not expressly restrict the disclosed assets to Texas. These are local qualifier/scope changes, not grounds for describing the whole reading as uniformly more or less confident.

## A4. Mechanical checks

I extracted the PDF text with **Ghostscript `txtwrite`** and rendered pages directly with Ghostscript for visual checks. No external sources or cited works were consulted. Counts below cover every claim and support `text` field, not just the A1 sample. Location labels, the reading plan, moves, meaning, and citation-label metadata are excluded from the numeric count so that document navigation is not confused with attributed numerical content.

| Check | Pass | Fail | Interpretation |
| --- | ---: | ---: | --- |
| Texts marked `verbatim` found in extracted article text | 0 | 0 | There are no verbatim fields: all 115 claims and 51 support items are paraphrased. Exact-quotation fidelity is therefore not exercised. |
| Numeric occurrences in ordinary claim/support text | 135 | 0 | Every numeral token occurs in the extracted article text. Comma grouping is normalized; units, denominators, and meaning require the semantic checks above. |
| Non-null reference entries matching the article's reference list | 0 | 0 | All 79 citation objects have null `reference_entry`. The article has no formal reference list; null entries are appropriate, not failures. |

For reproducibility, numeric tokens were extracted using `\d[\d,]*(?:\.\d+)?`; matches were compared after removing commas. This includes years, figure numbers, and numerals within identifiers such as D1. A numerical match is a presence check, not proof that a claim attributes it correctly.

**Image-derived material checked separately:** Four explicit quantitative transcriptions, at steps 11.2, 12.2, 14.5, and 15.3, contain **89 numeral occurrences**, including figure identifiers and D1. They were excluded from the 135 text-check occurrences. Their **84 data values**—nine city-comparison volumes/multiples, 35 scenario values, 16 withdrawal-component values, and 24 exposure percentages—match the rendered graphics. The remaining five numeral occurrences are Figure 2 identifiers twice, Figure 4 once, Figure 5 once, and D1 once. No image-only value was counted as an extracted-text failure.

All six analytical displays were inspected visually. The map and Figure 3's qualitative categories and contrasts are substantively captured, and the numerical chart transcriptions retain their units and ordering. Figure 3's printed minimal-water legend names solar/wind, whereas the support description also includes battery/storage from the adjacent prose; this is a small source-placement imprecision, not a fabricated generation category. There are no article tables or image-rendered equations requiring separate checks. All visual readings are marked `paraphrased` and identify their source element. The rendered overview was also checked to resolve its conflicting text layer.

These reference-entry counts do not certify every `citation_text` as an exact hyperlink anchor. They establish that no bibliography entry was invented or completed; the supplied labels generally function as inline source cues.

## A5. Detail and readability

The reading has **31 steps, 115 claims, and 51 support items**. After a claim-free cover step, the steps contain two to six claims apiece. Coverage is continuous through the summary, overview, map, background, methods, findings, two case studies, stakeholder recommendations, appendix, and back matter. The pacing gives separate attention to technology comparisons, graphics, disclosure examples, and limitations. The short city-comparison and final-methods steps follow natural breaks rather than omitting intervening material.

A reader could follow the report's argument from the reading alone: rapid demand growth creates indirect water dependency; generation mix determines its scale; local stress and drought shape exposure; disclosures and strategies leave gaps; recommendations address those gaps; the appendix specifies the estimates' limits. The meaning fields usually keep the model's interpretation separate from the attributed claims. Repeated headline findings are generally handled as restatements while new details are added.

Some support fields provide little independent evidential detail, saying that a paragraph cites a projection or that a company supplies an example. Other fields, especially AEP/Dominion and the cooling discussion, preserve concrete evidence well. The long numerical chart strings are complete but cumbersome to consult, and several claims bundle distinct propositions despite the prompt's instruction to keep distinct claims separate. These are limitations of organization and evidential bookkeeping, not coverage gaps.

The reading supplies a comprehensive, mostly faithful record suitable for a researcher to inspect against the report. Its strongest features are complete appendix and visual coverage, preservation of the withdrawal/consumption distinction, and careful handling of the overview's conflicting extraction. Its weaknesses are small shifts in outcome language and scope, occasional bundling, and support fields that sometimes repeat or describe a claim instead of recording additional evidence. The A1 sample found no unsupported claims; that sampled result should not be read as a certification of every attribution in the document.
