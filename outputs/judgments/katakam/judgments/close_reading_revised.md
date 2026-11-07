# Judgment — close reading (`run/analysis.json`)

**Article:** `article.pdf` — Katakam, Arzumanyan, Lin, Bahadur, "System-scale design and analysis of desalination systems for meeting water needs of data centers," *Water Research* 308 (2027) 126748.

**Seed:** `20261107`. All 113 claims were numbered in reading order as `C{step}.{claim}` (steps 0–24). The sample is Python `random.seed(20261107); random.sample(range(113), 30)`.

**Sampled claims:** C0.4, C1.3, C1.4, C3.1, C3.3, C3.4, C4.0, C4.4, C5.2, C5.3, C6.0, C7.0, C7.3, C8.3, C9.2, C10.0, C10.2, C13.0, C13.1, C13.2, C15.0, C17.0, C18.0, C19.0, C19.2, C20.4, C21.1, C21.3, C22.2, C23.0 (with their 24 support items).

**How I checked:** I extracted the PDF text with `pypdf` and checked verbatim texts, numbers and reference entries against it with scripts. I rendered pp. 10, 12, 13, 15, 16 and 17 as images and checked the figure readings (Figs. 4, 5a–b, 6a–c, 7a–b) by eye. I did not open the Supplementary Information, which is not in the PDF.

---

## A1. Attribution fidelity

| | Score 2 | Score 1 | Score 0 |
|---|---|---|---|
| Claims (n = 30) | 25 (83%) | 5 (17%) | 0 (0%) |
| Support items (n = 24) | 22 (92%) | 2 (8%) | 0 (0%) |

I found the passage for every sampled item. All 5 sampled `verbatim` claims (C0.4, C5.3, C20.4 and others) are the author's exact words. No sampled claim records the model's own inference as the author's.

**Claims scored 1:**

- **C3.1** (p. 3): The article says thermal processes are "typically feed salinity-insensitive". The reading has "typically less sensitive to feed salinity". This softens the claim from insensitive to less sensitive.
- **C4.4** (p. 4): The article states a research need: the influence of desalination parameters "needs to be quantified", and the bidirectional impacts "remain largely unexplored". The reading drops the "largely unexplored" gap. It also turns the converse direction into an assertion: cooling WUE "determine[s] freshwater demand".
- **C19.2** (p. 14): "further validating the hypothesis and cost-optimization approach" becomes "further support for the importance of TTD". The author's certainty is lowered.
- **C21.1** (p. 15): It adds a hedge, "lower *modeled* water stress", where the article says "decreased water-stress impact". It also drops the author's framing that these are "previously un-analyzed tradeoffs".
- **C21.3** (p. 15): It drops "substantially overestimating the sustainable operation of data centers" and the scope "especially for… high freshwater recoveries (such as Case 1. And Case 3.)". It inserts "modeled" again, and "cannot be obtained" becomes "would not distinguish".

**Support items scored 1:**

- **S6.0.0** (p. 5): The text, "distinguish emerging alternatives from the commercial choices", describes only the first citation group. The second group (Thiel 2015; Tucker 2024) supports a different sentence, the energy-efficiency claim. A single printed "Ding et al., 2026" is also resolved to all three Ding 2026 entries (a, b and c).
- **S13.0.0** (p. 9): The text is accurate. But the numeric marker "[14]" is resolved to the USGS entry. The article's reference list is author–year and unnumbered, so no entry matches "[14]" (by position, the 14th entry is Bartholomew 2018). The match is the model's inference from "USGS report". The prompt asked for a reference entry only where the list has a matching one.

**Outside the sample (noted, not scored):** C20.1 is a claim field that includes the model's own observation: "its Figure 7b projections… all lie in the figure's zero-to-low category". The observation is correct, since it is listed inconsistency #8. But it sits in a field reserved for the author's claims. Several support fields also carry the model's commentary, including S11.4.0, S12.1.0, S14.0.0, S18.0.0, S19.2.0, S20.1.0, S20.2.0, S22.3.0 and S23.0.0 (for example, "The prose drops the 1,000 from the unit in places"; "these are scenario cells rather than the prose's average comparison"). The wording makes clear these are observations about the text, and each one I checked is accurate. Still, they break the positional separation the rubric relies on. A downstream comparison that pulls `claims` and `support` as "the author's" would carry them along.

## A2. Coverage (against `claims_reference.md`)

The reading runs to the end of the article, including the end matter and references. It does not stop early.

| Type | In list | Caught | Caught without what it shows / partial | Missed |
|---|---|---|---|---|
| Highlights + graphical abstract | 6 | 5 | 0 | 1 (H4) |
| Abstract claims | 12 | 12 | 0 | 0 |
| Contributions | 8 | 7 | 1 (C2) | 0 |
| Section/subsection conclusions | 59 | 58 | 1 (S1.7) | 0 |
| Overall conclusions (§4) | 9 | 5 | 2 (CO4, CO8) | 2 (CO1, CO5) |
| Figures | 7 | 7 | 0 | 0 |
| Tables | 1 | 1 | 0 | 0 |

**Notes:**

- **H4** ("MLD and ZLD based treatment increase energy and cost by >12%") is not recorded. Only the abstract's ">12% and >15%" is (C0.2). H5 is caught as S0.3.0, and the graphical abstract as S0.1.0.
- **C2** (RO, MVC and hybrids optimized across all feeds and disposal regimes, with FR, SEC, second-law efficiency and WC quantified for each) is not recorded where the article states it as a contribution (step 5). Its content appears only in C0.1 and the methods steps.
- **S1.7**: the "largely unexplored" and "significant research gaps remain" claims are lost (see C4.4 above).
- **§4 Conclusions** is the weakest step: two claims for nine list items.
  - CO1 (scope, including the printed "50,000 and 90,000 ppm" PW feeds) is not recorded.
  - CO5 (SWUI was formulated and calculated for three data centers) is not recorded.
  - CO4 restates the PW case's yield only. The seawater case is mentioned without its numbers, and neither "dominated by" attribution is recorded.
  - CO8 is recorded without its comparative claim that "previous WUE/WUI-based frameworks could not capture" this.
- **Figures:** all seven are read with what they show. Fig. 4 has all 42 cells. Figs. 5a and 6a have the stream values. Figs. 5b and 6b have the main slices. Figs. 5c and 6c have the ranking. Fig. 7a has the classes and the 7.2 line, and Fig. 7b has the ranges. Fig. 3 is read only qualitatively (both bounds rising, fitted to 2028 and extrapolated, with no values). Fig. 1 leaves out the "Energy/Agricultural Sectors" outputs.
- **Table 1** is recorded in full across C12.0–C12.3, including the footnotes (85 USGS wells, the basis for the 70,000 ppm conventional limit, and CEPCI normalization).

**Found beyond the list (confirmed in the article):**

- C2.4: other wastewater sources (textile effluents, mining brines, power-plant blowdowns), p. 3.
- C7.4: energy recovery devices can mitigate parasitic energy, p. 6.
- C24.0–C24.2: end-matter statements. The list excludes these from scope but notes them.

**Internal inconsistencies:** the reading flags 7 of the list's 12 by itself:

- the units (L/kg against L/1000 kg)
- 50 K against 50 °C
- TTD 0–5 against 0–10 K
- the "ZLD" pie labels
- 753 / 753.7 / 754
- Case 1 "moderate" against Fig. 7b's zero–low values
- the 7.2 average against the Fig. 7b cells

It misses these:

- the hybrid total of 733 against 736
- the abstract's ">15%" WC rise against Fig. 4c's WC decreases
- the conclusions' "90,000 ppm"
- the "up to 30%" pre/post-treatment share against Fig. 5b
- the 7.2 "severe threshold" against the 9+ class boundary

On the last one, C22.3 silently resolves the ambiguity by reading 7.2 as Case 1's value, "below the severe cutoff".

## A3. Strength of language — **1**

Most of the time it preserves the author's strength. It uses attribution ("the authors say…", "which the authors characterize…") to carry strong wording without endorsing it. For example, "will exacerbate scarcity" (C1.7), "substantially improve" (C3.2), "clearly highlights" (C15.3, C17.2), "would greatly ease" (C2.1), and the quoted "practical, easily applicable and unified metric" (C10.5). Units, numbers and scope conditions are kept with care. It even keeps the article's mislabelled units and flags them.

The slips are not random. Four of the five A1 1s, plus C0.3 outside the sample ("can cut SWUI by 40%" where the abstract has "reduces SWUI by 40%"), move toward *less* certainty. Examples are insensitive → less sensitive, validating → support, the inserted "modeled", the dropped "substantially overestimating" and "previously un-analyzed", and "drastically" missing from C15.0. C4.4 goes the other way. The pattern is mild and inconsistent rather than systematic. But a researcher comparing sources should know that the reading tends to tone down the article's self-promotional intensifiers about SWUI.

## A4. Mechanical checks

| Check | Pass | Fail |
|---|---|---|
| Verbatim texts found in the article text (all 6: C0.4, C5.3, C5.5, C15.1, C20.4, C24.2) | 6 | 0 |
| Numbers in claim/support text found in the article text | 378 of 379 | 0 (1 apparent miss is the DOI split by the tokenizer; present on inspection) |
| Reference entries matching the article's reference list (172 entries, 94 distinct; normalized for line breaks and punctuation) | 172 | 0 |
| Null reference entries | 0 | — |
| Citation markers (`citation_text`) found as printed | all | 0 |

**Readings of figures (checked by eye, all `paraphrased` and naming the figure):** 72 numeric values in S14.0.0, S15.0.0, S16.0.0, S16.2.0, S17.1.0, S17.3.0, S18.0.0, S19.0.0, S20.1.0, S20.2.0, S21.0.0 and S22.3.0. They cover Figs. 4a–c, 5a–b, 6a and 7b, and **all 72 match the images**. The qualitative readings of Fig. 5c and 6c rankings and of Fig. 3 agree with the plots.

**Reference caveats:** the entries pass the string match, but three citation resolutions are the model's inference rather than a match the list provides:

- "[14]" is resolved to the USGS entry (S13.0.0).
- "[1]" is resolved to Neudorfer & Llera (S20.3.0). The list is unnumbered; entry 1 by position is Al-Amoudi.
- A single "Ding et al., 2026" is resolved to all three 2026 entries (S6.0.0).

The first two are plausible from context but are completions, which the prompt ruled out.

## A5. Detail and readability

There are 25 steps, 113 claims and 90 support items over 18 pages of main text plus end matter. The steps follow the article's own breaks:

- Introduction: 6 steps (pp. 2–4)
- Methods: 8 steps (pp. 4–10, with Table 1 given its own step)
- Results: 10 steps (pp. 10–17)
- Conclusions: 1 step
- End matter: 1 step

Coverage is even except for the conclusions, where a dense page gets two claims. The pace matches the reading plan (shorter steps through equations and figure-heavy results).

A reader could follow the argument from the reading alone. It goes from the gap, to the technology choice, to the RO and MVC models, the cost model, SWUI, the inputs, the results by metric, the worked cases and the SWUI cases. The `moves` fields name the argumentative actions accurately. The `meaning` fields are one sentence each and sometimes generic ("The table fixes the conditions under which…"), but they do link each step to the previous one.

Two things lower the record's usefulness:

- About a third of the support items only say what kind of work is cited ("The article cites seawater desalination and membrane modeling work"). They don't say what the author draws from it, so the support carries little content.
- The model's commentary sits in claim and support fields (see A1).

There is no repetition or padding.

---

## Summary for the researcher

This is a careful, accurate close reading.

**Strengths:**

- There are no 0-scored claims in the sample.
- All verbatim quotations, every reference entry and all 72 figure values I checked are correct.
- The abstract, figures, Table 1 and section conclusions are covered almost completely.
- It reads the multi-panel figures cell by cell, which a text-only reading could not do.
- It flags several of the article's own inconsistencies without penalizing or "fixing" the author.

**Weaknesses that matter for a cross-source comparison:**

1. The §4 Conclusions step is thin. CO1 and CO5 are missing, and CO4 and CO8 are only partly recorded.
2. There is a mild but one-directional tendency to soften the authors' certainty about SWUI's advantages and the framework's validation (5 of 30 sampled claims, plus C0.3).
3. The model's own observations appear inside `claims` (C20.1) and in several `support` fields. They are accurate and clearly worded, but a pipeline that treats those fields as the author's words would misattribute them.
4. Two numeric citation markers were resolved to reference entries by inference.

Each of these could be fixed with targeted edits. None suggests invented content.
