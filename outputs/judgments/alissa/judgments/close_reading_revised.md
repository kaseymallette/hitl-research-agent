# Close-reading judgment

**Article:** `article.pdf` (Alissa, H. et al. "Using life cycle assessment to drive innovation for sustainable cool clouds." *Nature* 641, 331–338, 2025)

**Run judged:** `run/analysis.json` (26 steps, 164 claims, 74 support items)

**Reference list used:** `references/claims_reference.md`, as written

**Sampling seed:** `20261106` (Python `random.seed(20261106); random.sample(range(164), 30)`, claims indexed 0–163 in reading order)

**How the article was read:** text extracted with PyMuPDF 1.28 (`get_text`). Pages rendered as images to check Fig. 1, Fig. 4, the Methods Vcore equation and Extended Data Table 1 by eye. Extended Data Table 1 is printed as an image (no extractable text). Everything else, including the Fig. 4 bar-total labels and the Vcore equation, is in the text layer.

---

## A1. Attribution fidelity

Sampled claim indices: 0, 1, 2, 6, 12, 18, 19, 22, 28, 34, 35, 43, 51, 55, 59, 60, 61, 69, 71, 79, 83, 86, 103, 123, 128, 129, 132, 158, 159, 161. These 30 claims carry 15 support items.

| | Score 2 | Score 1 | Score 0 | Passage not found |
| --- | --- | --- | --- | --- |
| Claims (n = 30) | 29 (97%) | 1 (3%) | 0 | 0 |
| Support items (n = 15) | 14 (93%) | 1 (7%) | 0 | 0 |

**The two 1s**

- **Claim 0** (step 0, abstract; paraphrased). The article says climate action requires "accelerating the development of sustainable alternatives to energy- and water-intensive technologies, particularly for rapidly growing infrastructure such as data centres and cloud". The reading turns this into alternatives *for* "rapidly growing, energy- and water-intensive infrastructure such as cloud and data centres". That narrows the general claim to its "particularly" case. This one is borderline: the core sense survives, but the scope changed.
- **Claim 83, support 0** (step 12, Table 4 footnotes; paraphrased). The reading gives "comparable chip cooling for conventional PG25 cold plate and two-phase" for "tends to have the same cooling capability at the chip". It gives "dependence of two-phase performance on its boiling enhancement coating" for "Chip cooling for two-phase immersion will mostly depend on the boiling enhancement coating". The hedges "tends to" and "mostly" are dropped, and "chip cooling" is broadened to "performance".

**Notes on items scored 2**

- The five sampled `verbatim` claims (1, 12, 61, 103 and 158) match the article exactly. The only change is that superscript citation markers are left out, which the format handles separately in `citations`.
- Claim 19's support item records the article's concession ("cooling systems … have been extensively reviewed^13,14") as support for the novelty claim. The text is accurate and the citation is correct. Structurally, though, it is a contrast the author sets against the novelty claim, not evidence for it.
- The figure readings in the sample are correctly marked `paraphrased` and name their element: Fig. 1b (claim 28), Fig. 4 (claims 69 and 79), and Extended Data Table 1 (claims 159 and 161). I checked them against the page images. Fig. 1b does show a separate CDU. In Fig. 4 the fluid segments are too small to read and unlabelled, as the reading says. Under renewables, the GHG bars are mostly the server segment.
- No sampled claim records the model's own inference as the author's.

---

## A2. Coverage (against `claims_reference.md`)

| Type | In list | Caught with content | Caught without what it shows | Missed |
| --- | --- | --- | --- | --- |
| Abstract claims | 6 | 6 | — | 0 |
| Contributions | 9 | 9 | — | 0 |
| Section/subsection conclusions, main text | 11 | 11 | — | 0 |
| Section/subsection conclusions, Methods | 9 | 9 | — | 0 |
| Figures | 4 | 4 | 0 | 0 |
| Tables | 5 | 5 | 0 | 0 |

**Where each item is found**

- **Abstract:**
  - AB-1 → claim 0
  - AB-2 and AB-4 → claim 2 (merged)
  - AB-3 → claim 1
  - AB-5 → claim 3
  - AB-6 → claim 4
- **Contributions:**
  - C-1 and C-2 → claim 19
  - C-3 → claim 40
  - C-4 → claim 38. The repeated percentages are noted as a restatement in step 5's moves.
  - C-5 → claims 48 and 108
  - C-6 → claim 61, with the parametric grid/renewable comparison in steps 9–11
  - C-7 → claim 106
  - C-8 → claim 111
  - C-9 → claim 156
- **Main-text conclusions:**
  - S-1 → claims 5–19
  - S-2 → claims 20–23
  - S-3 → claims 24–38
  - S-4.1 → claims 39–45
  - S-4.2 → claims 46–57
  - S-4.3 → claim 58
  - S-5 → claims 62–71. The section conclusions S-5b and S-5h are claims 63 and 71.
  - S-6 → claims 72–82
  - S-7 → claims 84–104
  - S-8 → claims 105–108
  - S-9 → claims 109–111
- **Methods:**
  - M-1a–d → claims 112–116. The repeated scope and use-phase material is recorded as a restatement in step 17's moves.
  - M-1e → claims 117–119
  - M-1f → claims 120–124
  - M-1g → claims 125–126
  - M-1h → claims 127–130
  - M-2 → claims 131–137
  - M-3 → claims 138–141. M-3c, the confidential two-phase fluid data, was recorded earlier at claim 57.
  - M-4 → claims 142–146
  - M-5 → claims 147–155
- **Figures:**
  - F-1 → support items of claims 26, 28 and 29, one per panel. Step 8's meaning also notes the caption's polyethylene glycol against the model's propylene glycol.
  - F-2 → claim 36, support 1, covering all three panels
  - F-3 → claim 45, support 0, covering all three stages
  - F-4 → claim 78, support 0, with all 24 bar totals. The use-phase, server and fluid segments are read at claims 64, 69 and 79.
- **Tables:**
  - T-1 → claims 30–32, every cell for each technology
  - T-2 → claim 50, including "per MW of IT capacity"
  - T-3 → claims 59–60, every row
  - T-4 → claims 62 and 75 (both cases, all 18 values), and claim 83 (the footnote hedges and the a–c notes)
  - T-ED1 → claims 159–163, all five indicators. The reading keeps the table's repeated "60–79%" in the score-4 completeness cell "as printed".

**Where the reading stops:** it doesn't stop before the article. It runs to the end of the PDF, which goes past the list's endpoint: Data availability, Author contributions, Competing interests (step 24) and Extended Data Table 1 (step 25). Claims 157–158, on author roles and competing interests, fall outside the list's stated scope. They are accurate, but they aren't counted here.

**Found beyond the list** (each confirmed in the article):

- Claim 94: one-phase hydrocarbon oils are "recognized for their dielectric properties, low toxicity and low fluid loss" (p. 336). The list's S-7e records only the cons.
- Claim 96: after a total fluid loss to ground, contaminated soil is replaced with off-site soil (p. 336).
- Claim 102: the specific viscosity, flash-point and volatility guidance in the last selection bullet (p. 337). The list gives only the bullet's heading.
- Claim 10: the concession that data-centre energy use "has grown more slowly than the number of data centres and the equipment they house" (p. 331).

**Article-internal discrepancies the list notes, and whether the reading catches them**

- The abstract's water figure "52" against Table 4's 48%: caught, in the meanings of steps 9 and 11.
- The Fig. 1 caption's "polyethylene" against the PG25 model's propylene glycol: caught, in step 8's meaning.
- The Conclusions' "at least 15%" GHG reduction as a grid-case figure: caught. Step 15's moves call it "the grid-case minimum improvements", and claim 75 records the renewable "≥13%".
- Methods "most efficient" (claim 147) against main text "all … efficient" (claim 103): both are recorded verbatim, but the difference isn't pointed out.
- "More than 4,000" against "more than 10,000" PFAS: both are recorded (claims 148–149) without comment.

---

## A3. Strength of language — **2**

On the whole, the author's certainty, scope and units survive.

**Hedges and modals kept**

- "probably" (claim 22)
- "to our knowledge" (claim 19)
- "could ultimately outweigh" (claim 37)
- "may not have as low PUE" (claim 87)
- "might be impractical … may be effective" (claim 149)
- "conservatively modelled" (claim 123)
- "will restrict" (claim 104)

**Scope and units kept**

- "per Vcore per year" and "at least" (claim 105)
- "per MW of IT capacity" (claim 50)
- the "best-case" overclocking cap (claim 141)
- the grid/renewable distinction throughout
- the Table 4 disclaimer "We are not suggesting any of them are superior" (claim 83)

The author's strong statements are kept strong:

- "must prioritize" (claim 85)
- "will lead to marked reductions" (claim 84)
- "only fluids with low to zero values should be considered" (claim 101)

**Small lapses, in both directions and not systematic**

- Dropped hedges in the Table 4 footnote reading (claim 83, support 0).
- "can save ≥15%, 15% and 31%" recorded as "save at least…" (claim 62). The "≥" is spread to all three metrics, though Table 4's minimums do bear that out.
- "enable" softened to "helps" (claim 86).
- The narrowing in claim 0.
- Claim 64 adds "In the grid case" to the use-phase-dominance claim. The passage sits in the grid-baseline paragraph and Fig. 4 bears the qualifier out, but the qualifier is the reading's, not the author's.

A stricter reading of "wherever the article attached them" could score this 1. I score 2 because the lapses are isolated, minor, run in both directions, and none touches a headline number or a central conclusion.

---

## A4. Mechanical checks

Run across the whole reading, not only the sample.

| Check | Pass | Fail |
| --- | --- | --- |
| `verbatim` texts found in the extracted article text (18 claims; no support item is `verbatim`) | 18 | 0 |
| Numbers found in the extracted text (173 numeric tokens, 68 distinct) | 173 | 0 |
| `reference_entry` values matching the article's own reference list | 70 | 0 |

- **Verbatim matching:** done after normalizing whitespace, line-end hyphenation and quote marks. The only difference anywhere is the leaving-out of superscript citation numbers (for example claims 1 and 105).
- **Numbers written as words** were checked by hand, and all match:
  - "fifteenfold" (15-fold)
  - "one billion" (the article's "1 thousand million")
  - "six-year" and "eight inches" (6 and 8 in)
  - "one-third / two-thirds"
- **Null entries:** two `reference_entry` values are `null`, for the engineeringtoolbox.com and aquaclearllc.com URLs printed in the Methods text (claims 136 and 137). Those URLs aren't in the reference list, so null is correct. No reference was invented or completed.
- **Citation markers:** every `citation_text` matches a marker printed at that location. There is one placement slip: refs 2,12 print on the sentence recorded as claim 39 ("LCAs drive effective design…"), but they are attached as support to claim 41, the following sentence.

**Read from images, checked by eye and not counted above**

- **Extended Data Table 1** (claims 159–163; image only). All cut-offs and level descriptions match the image, including the score-4 completeness cell, which the reading rightly flags "as printed".
- **Fig. 4 totals** (claim 78, support 0). All 24 values match the printed labels: GHG 100/11, 85/9, 84/9, 79/9; energy 100/93, 85/79, 85/79, 80/74; water 100/45, 69/22, 55/9, 52/8. The reading says that segment values aren't labelled and doesn't estimate them.
- **Figs. 1–3.** The panel descriptions match the images.
- **Vcore equation** (claim 115). It is in the text layer: "1 Physical core = 2 Logical cores = 2 V_cores × a". The reading's paraphrase is correct.

---

## A5. Detail and readability

**Steps and coverage.** There are 26 steps, averaging about 6 claims each (range 3–11):

- Main text (8 pages): steps 0–16
- Methods (3 pages): steps 17–23
- Back matter: step 24
- Extended Data Table 1: step 25

The spread is even. Denser passages, such as the fluid and LCA-model paragraphs and the design-assumption rules, get shorter steps. Lighter ones, such as the recommendations and bulleted criteria, get longer steps. Figures and tables are read at the passage that calls them.

**Readability.** A reader could follow the article's argument from this reading alone. The `moves` fields name what the author is doing in plain argumentative terms: concession, restatement, definition, recommendation. Restatements are noted as moves rather than re-recorded, as in steps 5, 17 and 23.

The `meaning` fields are short and add real value:

- They separate the two comparisons in the renewable section.
- They flag the abstract's 52 against 48.
- They note the glycol inconsistency.
- They observe that per-Vcore results depend on capacity as well as cooling hardware.

These stay observational and don't become verdicts. One comes close: step 9's note on Vcores against server counts.

**Density and padding.** There is little padding. Some claims bundle several article sentences; claims 27, 120 and 127 are dense but still separable. Step 24's author-roles material is brief and outside what most uses of the reading need.

---

## Summary for the researcher

This is a faithful, complete close reading, and I'd expect it to hold up well as an input to a cross-source comparison.

**Strengths**

- **Clean attribution.** Every verbatim text, number and reference entry checks out against the article. No reference is invented. Image-derived values are handled correctly, as paraphrase that names its element, with no estimation of unlabelled segments.
- **Full coverage.** Coverage against the reference list is complete across every type. The reading also catches several items the list left out, and it reads every table cell and every Fig. 4 total.
- **Author's qualifiers preserved.** It keeps the grid/renewable distinction, "at least", "per Vcore per year", and the Table 4 "not suggesting any are superior" disclaimer.
- **Internal inconsistencies flagged.** It notices most of the article's own inconsistencies (abstract 52 vs 48, polyethylene vs propylene glycol, the grid basis of "at least 15%") without turning them into judgments.

**Weaknesses (small)**

- A handful of isolated wording shifts:
  - dropped hedges in the Table 4 footnote reading
  - "can save" becoming "save"
  - one abstract claim narrowed to its "particularly" case
  - a context-supplied "In the grid case" added to one claim
- One citation attached to the sentence after the one it's printed on.
- Two of the article's internal discrepancies are recorded on both sides but not pointed out: Methods "most efficient" vs main text "all … efficient", and 4,000 vs 10,000 PFAS.

None of these changes a headline result or the shape of the argument.
