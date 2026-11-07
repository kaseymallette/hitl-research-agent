# Judgment — close reading

**Article:** `article.pdf` (Katakam, Arzumanyan, Lin, Bahadur, "System-scale design and analysis of desalination systems for meeting water needs of data centers", *Water Research* 308 (2027) 126748; 20 pp.)

**Run judged:** `run/analysis.json`: 25 steps, 107 claims, 90 support items, 172 citation→reference pairs.

**Seed (A1 sample):** `20261107`. Drawn with Python `random.seed(20261107); sorted(random.sample(range(1, 108), 30))`. Claims are numbered C1–C107 in reading order across `reading_path`.

**How I read the article:** I extracted the text with `pypdf` 7.0.0 (Ghostscript `txtwrite` crashed on six pages). I rendered every page to PNG with Ghostscript at 110 dpi and checked Figs. 4, 5a–c, 6a–c and 7a–b by eye. I used `references/claims_reference.md` as written.

---

## A1. Attribution fidelity

Sampled claims: C5, C9, C10, C20, C22, C23, C24, C28, C31, C32, C37, C40, C43, C49, C52, C55, C57, C71, C72, C73, C78, C85, C87, C89, C94, C95, C97, C99, C100, C102.

| Score | Claims (n = 30) | Share | Support items (n = 24) | Share |
|---|---|---|---|---|
| 2 | 22 | 73% | 24 | 100% |
| 1 | 8 | 27% | 0 | 0% |
| 0 | 0 | 0% | 0 | 0% |

I found the passage for every sampled item. All 30 sampled claims and all 24 support items are marked `paraphrased`, so no `verbatim` marker in the sample could be dishonest.

**The 1s (supported but altered):**

- **C20 (p. 3, SIE).** The article says the new evaporator designs "substantially improve SIE's operational stability till zero-liquid discharge limits and salt-management practicality". The reading says they "improve stability". The intensifier is dropped.
- **C31 (p. 4, novelty).** The article claims "the first study to provide *such a detailed* process, thermodynamic and economic analysis *of these desalination technologies*". The reading says "the first data center-focused analysis of process, thermodynamics and economics over the full … range". Dropping both qualifiers widens the priority claim beyond what the author made.
- **C32 (p. 4, SWUI contribution).** The article says SWUI "links desalination recovery and data-center water demand to *regional water-scarcity implications*" and provides "a *standard* benchmark". The reading says it "links recovery and cooling demand with siting and brine strategy" and furnishes "a benchmark". The defining link to water scarcity is replaced, "standard" is dropped, and "novel" is lost.
- **C52 (p. 7, metric gap).** The article's absolute "no metric directly quantifies the practical implications of data center water footprint on regional water scarcity" becomes "WUE, energy and cost do not directly express local scarcity implications", which is narrowed to three metrics. The author's strong aside that evaporative cooling is "no longer being considered in any significant manner" is also dropped.
- **C71 (p. 10, recovery).** The article gives "75% reduction for MLD upper limit disposal" going "from seawater towards hypersaline cases" and names no endpoints. The reading assigns the figure to "the seawater-to-150,000 ppm comparison". That pairing is the model's own, and its own Fig. 4a values give 830 → 251, about 70%, not 75%. The ">900 L per 1,000 kg" correction of the printed unit is flagged honestly.
- **C73 (p. 11).** The article says lower recovery "would result in increased regional water stress … depending on the local climate and hydrological conditions". The reading says "regional stress implications conditional on local climate and hydrology". The direction (an increase) is lost.
- **C85 (p. 12, Fig. 5c text).** The article says these factors "significantly influence" water cost, and that cost is "strongly dependent on discount rate, plant life and MLD brine management cost". The reading says "important" and "also matter". Both are softened.
- **C100 (p. 16).** The article says "Case 3 sees *substantial* benefit". The reading says "Case 3 benefits". The intensifier is dropped.

**Notes on the 2s:**

- **C102** reads "SWUI = 7.2" as Case 1's average, which is how Fig. 7a labels the dashed line ("Average Direct Evaporative Cooling SWUI (Case 1)"), rather than as the "severe threshold". The reference list records this as a printed inconsistency (no. 7), so either reading is faithful.
- **S24.1** maps the single marker "(Yuan et al., 2023)" to both of the article's duplicate entries (2023a and 2023b). That is not invented; the article itself lists both.

## A2. Coverage (against `claims_reference.md`)

The reading runs from the front matter to the reference list (step 24). It does not stop early.

| Type | In list | Caught | Caught without what it shows/says | Missed |
|---|---|---|---|---|
| Highlights (H1–H5) | 5 | 4 (through their abstract counterparts) | 1 (H5) | 0 |
| Graphical abstract (GA1) | 1 | 1 | 0 | 0 |
| Abstract claims (AB1–AB12) | 12 | 11 | 0 | 1 (AB12) |
| Contributions (C1–C8) | 8 | 7 | 0 | 1 (C6) |
| Section/subsection conclusions (S1.1–S3.3m) | 59 | 56 | 2 (S3.1d, S3.3f) | 1 (S2.3e) |
| Overall conclusions (CO1–CO9) | 9 | 9 (CO1 and CO5 as noted restatements, per the prompt) | 0 | 0 |
| Figures (F1–F7) | 7 | 7 | 0 | 0 |
| Tables (T1) | 1 | 1 | 0 | 0 |

**Missed:**

- **AB12.** "Overall, this study establishes a detailed modeling framework for sustainability-driven assessment of desalination-integrated data center infrastructure." Not recorded in step 0.
- **C6.** The "Collectively … desalination-centered framework … that goes beyond prior studies restricted to data-center water-use projections or waste-heat-driven, technologically nascent desalination configurations" claim. The positioning against prior work is absent from step 5.
- **S2.3e.** "SWUI is a practical, easily applicable and unified metric". The section's concluding evaluative claim is not recorded. Only its pointers to the Supplementary Information are kept (S56.1).

**Caught without what it says:**

- **H5.** Recorded as "the Highlights flag SWUI above 7 with evaporative cooling" (S4.1). The claim that it "causes severe water stress" is missing.
- **S3.1d.** The numeric energy increases are recorded (C74). The author's generalization, "MLD and ZLD systems, while more sustainable, inherently demand higher energy", is not.
- **S3.3f.** The comparison of Case 3 against Case 2 and the WUI counterexample are recorded (C94). The author's claim that the results "clearly demonstrate the SWUI parameter's ability…" is not.

**Figures:** every figure is read, not just named:

- Fig. 4a–c: every cell value is given.
- Fig. 5a: flows, pressures and areas (it omits the 28.7 and 6.5 bar pump heads, the 180/440 m² preheaters and the 1.4×10³ m² evaporator–condenser).
- Fig. 5b: the pie shares.
- Figs. 5c and 6c: the spread ordering.
- Fig. 6a–b.
- Fig. 7a: the class bands and the dashed line.
- Fig. 7b: ranges per case.
- Fig. 3: shape only (rising bounds, fitted to 2028 and extrapolated). No values are given.

Table 1 is covered in full, including the footnotes (85 wells, the conventional-limit basis), across C62–C66.

**Found beyond the list (confirmed in the article):**

- **C41.** Parasitic energy "can be further mitigated using energy recovery devices (ERDs)" (p. 6).
- **S83.1.** The distinction between hybrid-normalized results and the process-normalized exergy shown in Fig. S3 (p. 12).
- **C105–C107.** The competing-interest, funding, supplementary-material and data-availability statements. The list excludes the back matter by design but names these same statements.

**Internal inconsistencies:** the reading itself flags seven of the twelve listed:

- the L/kg vs L/1000 kg units (C71, S92.1, S93.1)
- 50 K vs 50 °C (S63.1)
- TTD 0–5 K vs 0–10 K (S61.1)
- the "ZLD" pie labels on MLD cases (S84.1, S89.1)
- Case 1 "moderate" vs the Zero–Low band (C92)
- 753 / 754 / 753.7 (S103.1)
- the prose 12.9–22.3 vs the Fig. 7b cells (S102.1)

It does not connect the abstract's ">15%" cost rise (C3) to the cost decreases it records itself (C79). It also does not note 540 + 193 = 733 against 736.

## A3. Strength of language — **1 (inconsistent)**

Numbers, units, samples and scope conditions survive well:

- per-feed and per-endpoint values
- "for a given concentrate handling condition"
- "depending on local climate and hydrological conditions" (in the condition, though not the direction; see C73)
- the 0.5–3 bar and 30% recovery conditions on the validation (S42.1)
- "first-order" scoping of SWUI (C55, in substance)

Several strong statements are also kept intact:

- "will exacerbate scarcity" (C12)
- "would greatly ease" (C14)
- "cannot … effectively" (C18)
- "virtually eliminating" (C22)
- "negligible" (C97)

The author's emphatic certainty, however, is often flattened. Examples:

- "substantially improve" → "improve" (C20)
- "substantial benefit" → "benefits" (C100)
- "significantly influence / strongly dependent" → "important / matter" (C85)
- "highly sensitive" → "flags" (C90)
- "no metric" → three named metrics (C52)
- "standard benchmark" → "benchmark" (C32)
- "novel" dropped (C4, C32)
- "clearly highlights" / "clearly demonstrate" / "corroborating" dropped (C76, S3.3f, C101)

Most shifts go toward less confident, but not all. C31 widens the novelty claim, and C82 moves "up to 30% of the overall water cost" into "its RO cost discussion", which changes what the 30% is a share of. Because the shifts mostly concern emphasis and go both ways, I score this 1 rather than 0.

## A4. Mechanical checks

These were checked by script against the `pypdf` text, with figure values checked by eye.

**Verbatim texts.** 1 of 1 found: C107, "Data will be made available on request." (p. 18). No support item is marked verbatim. The reading is 106/107 paraphrased.

**Numbers.** There are 483 numeric tokens across claim and support texts:

- 397 matched the extracted text directly.
- 6 of the rest are text values the extraction mangled, so they pass: 10⁶ (×2) and 10³ (×3) superscripts, and "about 931", a rounding of the printed 931.2.
- 80 are readings of figures printed as images, reported separately below.

**Text failures: 0.**

**Figure and image readings.** All 80 values match the images:

- Fig. 4a–c: 45 values, plus 4 in S79.1
- Fig. 5a: 8 values
- Fig. 5b: 2 values
- Fig. 6a: 4 values
- Fig. 7b: 17 values

**Reference entries.** 172 of 172 `reference_entry` values (94 unique) match the article's reference list. The match is after normalizing extraction artifacts: "ñ" printed as "˜ n", and page headers splitting entries. No entry is invented or completed.

- 75 of 77 unique `citation_text` markers appear exactly as printed. The two exceptions, "(Onishi et al., 2017)" and "(Randon et al., 2020)", are split out of the printed combined marker "(Onishi et al., 2017; Onishi et al., 2017; Randon et al., 2020)".
- **Caveat:** two numeric markers in this author–year article, "USGS report[14]" (S67.1) and "WUI metric for data centers[1]" (S94.1), were assigned entries ("Survey et al., 2024" and "Neudorfer and Llera, 2025"). The entries exist verbatim and the assignments are plausible. But the article's list is not numbered, so the link is the model's inference, not a printed match.

## A5. Detail and readability (described)

The reading has 25 steps over 20 pages. The densest pages get smaller steps:

- Table 1 has a step of its own.
- §2.4 is split three ways.
- §3.1 is split into recovery, energy and cost.
- §3.3 has three steps.

The introduction (pp. 2–4) gets six steps and the conclusions one, so coverage is even relative to how much argument each part carries. Step locations are accurate, though steps 19–20 give page spans ("pp. 12–16", "pp. 14, 17") that interleave with figure pages.

Claims are compact and do not repeat each other. Restatements in the conclusions are handled as instructed (C104, S103.1). Moves fields are informative. Meaning fields are single sentences, often thin, but they do say how each step builds on the last.

A reader could follow the article's argument from this reading alone: the motivation, the gap, the models, the cost basis, the definition of SWUI and its stated limits, the results, and the siting comparison. They would miss some of the author's rhetorical force and the three items listed under A2.

---

## Summary for the researcher

**Strengths.** This is a careful, well-structured reading that would serve a cross-source comparison well on numbers and on structure:

- All 172 citation–reference pairs match the article's own list, with nothing invented.
- Every figure value it gives (80 read off images) matches the page.
- No sampled claim lacks support in its passage, and no `verbatim` marker is misused.
- Coverage of figures, Table 1 and section conclusions is near complete.
- It surfaces most of the article's internal inconsistencies (units, TTD range, pie labels, the Case 1 band, 753/754) without editorializing.

**Weaknesses.** Almost everything is paraphrased (106 of 107 claims), and the paraphrase is where fidelity slips. About a quarter of sampled claims (8 of 30) lose something the author attached:

- most often an intensifier or certainty marker ("substantially", "strongly", "clearly", "novel", "standard", "no metric")
- once a qualifier that widens the novelty claim (C31)
- once a specific comparison the author never named (C71)

None of these is an invented claim. All are fixable. A user quoting this reading for the author's degree of confidence should check against the article. Three of the author's own framing claims are absent: AB12, the "goes beyond prior studies" contribution (C6), and "SWUI is a practical, easily applicable and unified metric" (S2.3e). Two numeric citation markers were matched to entries by inference.

