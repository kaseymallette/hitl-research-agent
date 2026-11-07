# Close-reading judgment

**Article:** `article.pdf` (Alissa et al., "Using life cycle assessment to drive innovation for sustainable cool clouds", *Nature* 641, 331–338, 2025)
**Run judged:** `run/analysis.json`
**Reference list used:** `references/claims_reference.md`, used as written and not changed
**A1 sample seed:** `20261106` (Python `random.seed(20261106)`, then `random.sample(range(164), 30)` over the claims in document order)

**How I checked it:** I extracted the PDF text with PyMuPDF 1.28 (`get_text()` per page). I rendered PDF p.2 (Fig. 1), p.7 (Fig. 4) and p.13 (Extended Data Table 1, a raster image with no extractable text) and checked them by eye. The mechanical checks in A4 ran as a script over the extracted text, after normalising whitespace, line-break hyphens and quote/dash characters.

**Run size:** 26 steps, 164 claims, 74 support items, 72 citation entries.

---

## A1. Attribution fidelity

Every claim in the sample has a location I could find in the article.

| Score | Claims (n = 30) | Support items (n = 14) |
| --- | --- | --- |
| 2 | 28 (93%) | 13 (93%) |
| 1 | 2 (7%) | 1 (7%) |
| 0 | 0 (0%) | 0 (0%) |

### Sampled claims

Score is listed as claim score / support scores. "—" means the claim has no support items.

| # | Step.claim | Form | Score | Note |
| --- | --- | --- | --- | --- |
| 1 | 0.0 | para | **1** / 2 | Scope narrowed. The article says alternatives to "energy- and water-intensive technologies, particularly for rapidly growing infrastructure such as data centres and cloud". The reading has alternatives "for rapidly growing, energy- and water-intensive infrastructure", so a general claim about technologies becomes a claim about infrastructure. Ref. 1 is correct. |
| 2 | 0.1 | verb | 2 / 2 | Exact wording apart from the stripped superscript "2". Ref. 2 is correct. |
| 3 | 0.2 | para | 2 / — | Faithful merge of the abstract's scope sentence (VMs to grid) with its ecosystem sentence ("to provide adoption guidelines"). |
| 4 | 1.1 | para | 2 / 2 | Refs 3–5 are correct. |
| 5 | 2.0 | verb | 2 / — | "Strong action is necessary." This is exact. |
| 6 | 2.6 | para | 2 / — | Matches "considers the impact … on the efficiency and performance" and the life-stage list. |
| 7 | 2.7 | para | 2 / 2 | Keeps "to the authors' knowledge", the hyperscale qualifier and the three metrics. Refs 13 and 14 support "extensively reviewed". |
| 8 | 3.2 | para | 2 / 2 | Keeps "will probably". Refs 16 and 17 are correct. |
| 9 | 4.4 | para | 2 / 2 | Fig. 1b checked by eye: a tank, a separate coolant distribution unit, and mineral oil in the caption. Ref. 25 is correct. |
| 10 | 5.4 | para | 2 / — | Keeps the causal chain to total cost of ownership and embodied carbon. |
| 11 | 5.5 | para | 2 / 2 | The article attributes the retrofit demonstration to Intel and cites ref. 22. The reading matches. |
| 12 | 6.4 | para | 2 / — | |
| 13 | 7.5 | para | 2 / 2 | 22% coal and 38% gas. "Contribute the most" is kept. Ref. 35 is correct. |
| 14 | 8.0 | para | 2 / — | |
| 15 | 8.4 | para | 2 / — | Table 3 values are all correct: capacity 3/6/6, overclocking 20/10/20, PUE and server power −3/−6/−6, Vcores 28/25/36. |
| 16 | 8.5 | para | 2 / — | Table 3 counts are all correct: compute servers 6/13/13; JBOD, head nodes and networking 10/13/13. "Identical" is rendered as constant shares. |
| 17 | 9.0 | verb | 2 / — | Exact. |
| 18 | 10.2 | para | 2 / 2 | The Fig. 4 reading says plainly that segment values aren't labelled. |
| 19 | 10.4 | para | 2 / 2 | "Are possible" becomes "could". The water-stressed example is correct. |
| 20 | 12.0 | para | 2 / 2, 2 | "Highlights the need" becomes "making … necessary". This is close in strength. The Fig. 4 renewable GHG bars are mostly server segment, which I confirmed by eye. Ref. 41 is correct. |
| 21 | 12.4 | para | 2 / **1** | The claim keeps the "not suggesting any … superior" hedge and the sensitivity caveat. In the support item, footnote c says two-phase chip cooling "will **mostly** depend on the boiling enhancement coating". The reading has "dependence of two-phase **performance**". This drops "mostly" and widens chip cooling to performance. |
| 22 | 13.2 | para | 2 / — | Keeps "ensure". "Most notable" becomes "largest", a small change. |
| 23 | 14.9 | verb | 2 / — | Exact. This is the main-text version, which correctly differs from the Methods version recorded at step 23. |
| 24 | 18.6 | para | **1** / — | Qualifier dropped. The memory datasheet "was not **publicly** available". The reading says "the datasheet was unavailable". The SSD one-third and two-thirds split is correct. |
| 25 | 19.3 | para | 2 / — | The data hierarchy and the three proxies are correct. |
| 26 | 19.4 | para | 2 / — | |
| 27 | 20.1 | para | 2 / — | The PUE definition, load factor and conservative utilisation assumption are correct. |
| 28 | 24.2 | verb | 2 / — | Exact (competing-interests statement). |
| 29 | 25.0 | para | 2 / 2 | Extended Data Table 1 reliability row matches the image. Ref. 51 is correct ("Adapted from ref. 51"). |
| 30 | 25.2 | para | 2 / — | Temporal row (<3, <6, <10, <15, unknown or >15) matches the image. |

No sampled claim records the model's own inference as the author's. The run's own observations sit in `meaning`, where they belong. Examples are the PG25 vs polyethylene-glycol mismatch, the 52 vs 48 water figure and the Table 3 Vcore pattern.

---

## A2. Coverage, counted against `claims_reference.md`

The list covers the main text, the Methods and Extended Data Table 1. **The reading covers all of this.** It runs in order from p.1 to p.13 and adds the back matter.

| Type | In list | Caught with content | Caught without what it shows | Missed |
| --- | --- | --- | --- | --- |
| Abstract claims | 6 (AB-1–6) | 6 | — | 0 |
| Contributions | 9 (C-1–9) | 9 | — | 0 |
| Section conclusions, main text | 11 units (S-1–S-9) | 11 | — | 0 |
| Section conclusions, Methods | 9 units (M-1a–d, M-1e–h, M-2–M-5) | 9 | — | 0 |
| Figures | 4 (F-1–4) | 4 | 0 | 0 |
| Tables | 5 (T-1–4, T-ED1) | 5 | 0 | 0 |

### How each item was caught

- **Abstract.** AB-2 and AB-4 are merged into one claim (step 0.2), with nothing lost.
- **Contributions.**
  - C-1 and C-2 are at step 2.7.
  - C-3 is verbatim at step 6.1.
  - C-4 is at steps 0.3 and 5.8.
  - C-5 is at steps 7.2 and 15.3.
  - C-6 is verbatim at step 9.0, and the renewable scenario is at step 7.8.
  - C-7 is verbatim at step 15.1.
  - C-8 is at step 16.2 with ref. 45.
  - C-9 is at step 24.0 with ref. 52.
- **Figures.**
  - Fig. 1: all three panels and their caption examples are described.
  - Fig. 2: all panels are described.
  - Fig. 3: all three life-cycle stages are described.
  - Fig. 4: all 24 bar totals are listed and match the image.
- **Tables.**
  - Table 1: all three columns and all four rows, spread across the support items in step 5.
  - Table 2: in full.
  - Table 3: in full, including the "identical" rows.
  - Table 4: both electricity cases and the footnotes.
  - Extended Data Table 1: all five indicator rows. For Completeness score 4, the reading writes "as printed" where the image repeats 60–79% for the shorter period. That is an honest note, not a guess.

### Partial catches

- **S-1e.** The reading has "further gains require understanding cooling alternatives" but drops the tail "which can be provided by LCA".
- **S-6c (ranking reversal).** Caught in full at step 11.4.
- **Methods versus main text.** The reading records both the main-text and Methods versions of the PFAS paragraph (S-7g and M-5a). This is right, because they differ: "all … offer efficient cooling" against "immersion cooling offers the **most** efficient". It doesn't flag that difference in a `meaning`, though.
- **"More than 4,000" against "more than 10,000".** It records both figures (steps 23.1 and 23.2) without comment.

### Found beyond the list

I confirmed each of these in the article:

- "Strong action is necessary." (p.331, step 2.0).
- "As cloud-service demands increase, so must data centre capacities and heat mitigation strategies." (p.332, step 3.0).
- The author-contributions and competing-interests statements (p.12, steps 24.1–24.2). The list excludes these by design.
- The two in-text URLs for dry-bulb temperature and cycles of concentration (p.10). The run correctly gives these `reference_entry: null`.

---

## A3. Strength of language: **1**

The author's certainty mostly survives. These all come through intact:

- "to our knowledge"
- "will probably"
- "≥13%" against "at least 15%"
- "at the very least" in the worked Vcore example
- "was found to be an ideal comparison unit"
- "must prioritize"
- "only fluids with low to zero values"
- "will restrict"
- the Table 4 footnote hedge ("We are not suggesting any of them are superior …")

The quantitative claims keep their units, cases (grid or renewable) and ordering throughout.

Some conditions were still stripped or shifted, in both directions:

**Softened**

- **AB-6, step 0.4.** "This comprehensive approach **demonstrates** the transformative potential" becomes "The authors **see** this approach as having transformative potential". The abstract's strongest claim is turned into an attitude.

**Strengthened**

- **S-7c, step 13.4.** Two-phase immersion "**could** have high heat transfer at the chip and lower PUE" becomes "**can** combine high chip heat transfer with low PUE".
- **M-4a, step 22.0.** "In part because standard deviation is not accounted for" drops "in part", which makes the stated reason the only reason.
- **Table 4 footnote c, step 12.4 support.** "Mostly" is dropped (see A1 #21).

**Scope altered**

- **AB-1, step 0.0.** Technologies narrowed to infrastructure (see A1 #1).
- **Memory datasheet, step 18.6.** "Publicly" is dropped (see A1 #24).
- **Step 9.3.** The claim adds the scope "In the grid case" to the author's "for all cooling technologies". Fig. 4 does bear this out, but it is the reader's narrowing placed inside a claim field.
- **Step 2.4.** The "which can be provided by LCA" link is lost (S-1e).

These slips are few, small, and run in both directions, so there is no systematic tilt toward more or less confidence. They are enough that conditions don't survive "wherever the article attached them". This is a 1 at the high end.

---

## A4. Mechanical checks

| Check | Pass | Fail | Notes |
| --- | --- | --- | --- |
| Verbatim claim texts found in the article text | 18 | 0 | 15 matched on the first pass. The other 3 (steps 0.1, 6.0 and 15.0) differ only by omitting inline superscript citation markers ("analysis²", "system²,¹²", "outcomes⁴⁴"), and match once the markers are removed. No support item is marked verbatim. |
| Numbers in claim and support text found in the article text | 215 | 0 | 216 numeric tokens in total. The one not in extracted text, "59", is an image reading (see below). This check confirms each number appears in the article; I verified context by hand only for the sampled claims and the tables. |
| Reference entries matching the article's reference list | 70 | 0 | Out of 72 citation entries. The other 2 are `null` and correct: they are in-text URLs with no list entry (step 20). Multi-reference markers ("3–5", "23–25", "30–34") are expanded one entry per cited work, each correctly matched. Ref. 27 and ref. 48 (the two Boyd entries, printed slightly differently) are each copied exactly. Nothing is invented or completed. |

### Image readings, checked by eye

- **Fig. 4 (p.7).** All 24 bar totals in step 11.6 support match the printed labels. The reading says which segments are visible and that segment values aren't labelled.
- **Extended Data Table 1 (p.13, raster image).** All five rows in step 25 match the image, including the completeness bands (>80%, 60–79%, 40–59%, <40%) and the "as printed" note on the repeated 60–79%. These are correctly marked `paraphrased` and attributed to the table.
- **Fig. 1 (p.2).** Panel contents match: the CDU in panels a and b, the vapour and condenser in panel c, and the caption examples.
- **Methods Vcore equation (p.9).** The equation is set partly as text. It is marked `paraphrased` and named ("The Vcore equation in Methods …"), and the reading matches the printed form.

No image reading is marked `verbatim`.

---

## A5. Detail and readability

- **Steps:** 26 steps holding 164 claims (2.8–11 claims a step, mean 6.3). The reading plan names the document type and density and says it will take shorter steps for dense model assumptions. The step sizes follow that plan.
- **Distribution:**
  - About 8 printed pages of main text get 17 steps (0–16).
  - About 3 pages of Methods get 7 steps (17–23).
  - Data availability and back matter get 1 step (24).
  - Extended Data Table 1 gets 1 step (25).
- **Evenness:** Coverage is even. No section is skipped or compressed into a single line, and the dense passages get their own steps: Table 3, the renewable-energy switch, and the design assumptions. The two steps that fold in back matter (16 and 24) are light by design.
- **Repetition:** Low. Restatements are mostly handled as moves rather than re-recorded. Examples are the Methods restating scope, metrics and the grid mix (step 17 "Revisits …") and the restated headline percentages at step 5. Where the article repeats a claim with different wording, the reading records both versions, which is useful for comparing them.
- **Meaning fields:** Short, they track how the argument moves, and they don't pad. A few do useful reader's work: the propylene/polyethylene-glycol mismatch, that the abstract's 52% is a remaining Fig. 4 index rather than a Table 4 saving, and that grid-air serves as the common index for both electricity cases. None of these is presented as the author's claim.
- **Can the argument be followed from the reading alone?** Yes. A reader could trace the argument from motivation, through the technologies and the LCA design, to the grid and renewable results, the design trade-offs, and then the recommendations and caveats. The Methods steps make the model's dependence on Table 3's assumed overclocking and capacity factors visible.

---

## Summary for the accepting researcher

**Strengths**

- Coverage is complete: every abstract claim, contribution, section conclusion, figure and table on the reference list is caught with its content. The reading continues through the Methods and the Extended Data table.
- The mechanical record is clean:
  - all 18 verbatim texts are exact, apart from omitted superscript citation markers;
  - every number appears in the article;
  - all 70 reference entries match the article's list, with nulls only where the article has no entry.
- Figure and table readings are correctly marked as paraphrase and named, and are accurate against the images, including a value the image prints oddly.
- Claim fields hold the author's claims. The reader's own observations, several of them useful for cross-source comparison, are kept in `meaning`.

**Weaknesses**

- The main weakness is a scattering of small strength-of-language and scope slips, roughly one in ten claims on the evidence of the sample, in both directions.
- The most consequential is the abstract's "demonstrates the transformative potential", recorded as the authors merely "seeing" that potential.
- Others are dropped qualifiers ("in part", "mostly", "publicly") and one "could" turned into "can".
- The reading also records, without comment, two internal inconsistencies that a comparison across sources might want flagged: the main text and Methods differ on whether immersion is "most" efficient, and on 4,000 against 10,000 PFAS substances.

None of these is an invented or misattributed claim, and all are fixable by tightening individual paraphrases. If those phrasings matter for the collection, check them against the article before relying on them.
