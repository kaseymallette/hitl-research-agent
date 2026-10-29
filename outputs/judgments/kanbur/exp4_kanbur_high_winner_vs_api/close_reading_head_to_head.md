# Close readings, head to head — runs A and B

**Article:** Kanbur, Wu, Duan, "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system," *Int J Energy Res* 2020;44:10453–10470.

**Read for this session:** `RUBRIC.md`, `prompts/close-reading.md`, `article.pdf` (text extracted with PyMuPDF; Figure 6–8 page also viewed as an image), `references/claims_reference.md`, `runs/A/analysis.json`, `runs/B/analysis.json`. No other judgment or argument evaluation was opened.

| Run | `id` |
| --- | --- |
| A | `fa401e5e-ea12-498b-9ccb-24aa8aa410fa` |
| B | `2a82aff3-14e1-4c82-a830-1c9118ce5847` |

Every claim and support item in both runs was read in full, so no A1 sample or seed was drawn. Step labels below (A14, B27, …) are 0-based indexes into each run's `reading_path`.

---

## Shape of the two readings

The two readings are very alike. Each has 37 steps in nearly the same order, runs from the Summary through the Appendices, marks almost everything `paraphrased`, records the same citation markers, and flags the same four inconsistencies within the article:

- COP is 2.15× in Section 4 but 1.5× in the Conclusion.
- Water output falls "nearly 65%" in Section 4 but grows "1.85 times" in the Conclusion.
- The Summary gives 5.12 cm² where Section 4 gives 5.13 cm².
- Eq 24 is printed with the same right-hand side as Eq 22.

| | A | B |
| --- | --- | --- |
| Steps | 37 | 37 |
| Claims | 158 | 173 |
| Support items | 111 | 86 |
| Verbatim claims | 2 | 4 |

The differences are in the details. A reads the figures and records the article's own claims (contributions, strength words) less fully. B records the claims and Table 1 more fully but mostly names the figures without reading them.

---

## What each caught that the other missed (A2, against `claims_reference.md`)

### Caught by A, missed or only named by B

| Ref | What A has | What B has |
| --- | --- | --- |
| **F6** (GOR/PR surfaces) | A25 C25.1 reads the surfaces as rising with membrane area. Checked by eye against p. 10465, and correct. C25.0 sets the two prose statements side by side and says they "point in different directions". | B27 names Figure 6, then says in its meaning that the prose "is not replaced by an inferred reading of the surface plots". The figure is named but not read. |
| **F4** (water surface) | Reads the highest production at the largest area and load. | Names the surface only. |
| **F5** (efficiencies) | Reads 5A as bars rising with load and 5B as ε higher toward high load and small area. Notes that the colour scale's lowest label (27.20) differs from the prose minimum (27.3) and keeps both without reconciling them. | Names 5A and 5B without reading them. |
| **F8** (payback) | Reads the axis (3.719–3.727) and a slight increase with area. | Reads the axis and says "small area-dependent variation", with no direction. |
| **F9** (levelized costs) | Reads 9A as almost flat across area and rising with load, and 9B as a widening gap. | Names both panels. |
| **S5.0b** | Records the hedged "results can be useful for real-scale operations in future studies" (A30 C30.2). | Not recorded as a claim. |

### Caught by B, missed or partial in A

| Ref | What B has | What A has |
| --- | --- | --- |
| **C-a, C-b** (novelty contributions) | B5 C5.0–C5.1 record "has not been investigated before" and "first time" use for desalination as claims. | Records only C-c (A4 C4.4). The novelty claims appear only in A4's `moves`, so A misses two of the four enumerated contributions as claims. The "first time" claim in the Conclusion (S5.0a) is also unrecorded in A. |
| **C-d** | Recorded in full with its bounds (C5.3). | Reached only later, through the Section 3.5 objectives (A20). |
| **T1** (validation table) | Reads every current, reference and relative-difference value in Table 1. Notes that two column headers are both printed "qT". | Reads the relative differences only (and see the label error below). |
| **T3** (balance equations) | Notes the permeate-pump auxiliary equation printed as "c3 = u3". | Summarises T3 generally. |
| **S1.1** | Records "pivotal role" (B1 C1.2). | Gives the 40% figure without the conclusion drawn from it. |
| **S1.4** | Records "critical importance" (B2 C2.3). | Gives the SDG link without the strength word. |
| **S1.9** | Records "satisfying steady performance" (B4 C4.0). | Not recorded. |
| **S5.1** | Records the closing ground verbatim, "The hybrid system can be efficiently operated for the low data center cooling loads.", with "satisfying performances" as its support (B33). | Gives the recommendations without the claim they rest on. |

### Missed by both

- **C-5.5.** Neither records how the Conclusion rewords feasibility, from "for real applications" in the Summary to "for further real-scale demonstrations".
- **C-5.6.** Neither records that the Conclusion's reason for the DCMD's lowest cost ("lower exergetic costs") differs from the capital-cost reason in Section 4.
- **C-5.3, C-5.4, C-5.8.** Both treat these only as restatements in `moves`/`meaning`. "Drastically affected" in C-5.3 survives in neither.
- **Equation numbering.** Neither notes that the prose calls Eqs 28–30 "(31)–(33)".
- **F9 axis units.** Neither notes the "$/h" axis label against SGD/h in the text.
- **F10.** Both name Figure 10 only.

Neither reading stops early. Both cover the whole main text and also the Nomenclature, references and Appendices A–C.

---

## Where each is wrong and the other isn't (A1, A3)

### A

- **Invented Table 1 labels (A14 C14.1 support).** A calls the second and third quantities "total heat flux" and "vapor heat flux". The table prints both as "qT (W/m²K)". These labels are the run's interpretation presented as a reading of the table. The values are right. This is the most serious attribution fault in A.
- **"Dramatically" softened (A28 C28.4).** A renders it as "increase strongly". This is a strength shift, scored 1.
- **"Critical importance" and "pivotal role" dropped** from the S1.4 and S1.1 claims (A3 C3.0, A1 C1.4). Both scored 1.
- **Small additions:** "measured" in A10 C10.5, and "clearly infer" dropped in A14. These are minor.

### B

- **The GOR/PR contradiction is smoothed over (B27 C27.1).** The article says "the maximum GOR and PR values are nearly 14 times higher than the GOR and PR values of the minimum membrane area". B gives this as "a nearly fourteenfold difference … between the membrane-area extremes". That drops the direction, which is the very thing that contradicts B's preceding claim (C27.0, "highest values at the minimum membrane area"). This is the article's main internal inconsistency, and B never reads Figure 6, which would settle it. B's reader comes away thinking the article says small membranes maximise GOR/PR, with no sign of the conflict. Scored 1, and the more consequential of the two runs' faults.
- **"Adopted experimentally" (B11 C11.1)** garbles "the experimental correlation was withdrawn from Reference 31". Scored 1.
- **Run inferences placed in support items:**
  - B28 C28.2 says the authors infer SI's interchangeability "from the parallel trends in Figures 5B and 7". The passage cites no Figure 5B.
  - B31 C31.2 calls Figures 5B and 9B "opposing performance implications". The article says only "significant impact".
  - B25 C25.3 gives the daily range as spanning "the membrane-area and cooling-load domain". The article says "according to the applied membrane area".
- **Hedge strengthened.** B5 C5.2 has "may be useful" where the article has "can be useful". This is minor, and A has the same move ("potentially useful").
- **"Clearly infer" dropped** in B15, as in A.

### Attribution and strength, net

Neither run has a fabricated claim or a false verbatim. Most claims in both would score 2. A's 1s and 0s are a table mislabel and a few dropped strength words. B's are one significant distortion (GOR/PR) plus several small run-glosses in support items.

On **A3**, B is more consistent. It keeps "critically", "pivotal", "dramatically" and "may not", and both runs keep "as far as we know", "seems", "may" and "can". A is mostly faithful but softens or drops three strength words in one direction (less confident). Neither is systematically shifted, so both sit at about 1–2, with B a little higher.

---

## A4. Mechanical checks (both runs)

Each run's verbatim texts, numbers and `reference_entry` values were checked with a script against the PyMuPDF-extracted text, normalising whitespace, ligatures and line-break hyphens.

| Check | A | B |
| --- | --- | --- |
| Verbatim texts found in the article | 2 / 2 | 4 / 4 |
| Numbers found in the article's text | 343 / 343 | 316 / 316 |
| Reference entries matching the article's reference list | 74 uses, 47 unique; all 47 match | 73 uses, 47 unique; all 47 match |

**Reference-entry note.** Eight entries first showed as misses in both runs. Each was a real printed hyphen at a line end (e.g. "674-691", "Al-Hinai", "SEMI-THERM") that the normaliser had stripped. Checked by hand, all match.

**Printed oddities kept faithfully by both:**

- ref 17's title duplicating ref 16's;
- refs 10 and 29 sharing the DOI er.1663;
- "c_w = 2.74 m³/h".

**Readings from images (checked by eye, not counted as failures):**

- A's Figure 6 reading (surfaces rise with area) and Figure 8 reading (slight increase with area) match the page.
- A's note that the Figure 5B colour bar's lowest label is 27.20 matches the extracted label.
- B's Figure 8 axis range is correct.
- Both marked every image reading `paraphrased`.

---

## A5. Detail and readability

- **Segmentation.** Both have 37 steps with near-identical breaks and even coverage. The densest results paragraphs get about one step per figure in each.
- **Claims and support.** B splits results into more claims (e.g. five claims for Figure 3, against A's four). A attaches more support items and more figure readings.
- **Back matter.** A spends five steps on it (three for the appendices alone), which is mildly padded. B uses three, one of which (B35, the references) has no claims.
- **Meaning fields.** Both are good, and a reader could follow the article's argument from either alone. A's `meaning` fields more often say what a step does and does not establish (e.g. A14: agreement "for that separated calculation, rather than for the full proposed hybrid"). B's are similar in quality (e.g. B15, B23).

---

## Verdict

**A is narrowly better.**

- **Figures.** A reads them where the prompt asks for it, and five of its readings (F4, F5, F6, F8, F9) add what the figure shows where B only names it.
- **The key inconsistency.** On the article's central internal inconsistency (GOR/PR against membrane area), A records both prose statements with their directions, reads the figure, and keeps all three apart. B's rewording removes the direction and so hides the conflict. For a researcher using the reading downstream, this is the most consequential difference.
- **What B does better.** B records the enumerated contributions, Table 1 and the article's strength words more completely (A2 contributions, T1; A3). A's missing contributions C-a and C-b, and its invented Table 1 labels, are real faults.
- **Weighing.** B's faults touch a result claim and a figure the article itself contradicts. A's touch the contributions list (whose content A does give in `moves`) and column labels on otherwise correct values. That is why A edges ahead.

The margin is small. A researcher who weighted A2 contributions and A3 most heavily could reasonably prefer B.

## Order check

- **A read first.** A sets the baseline: figure readings, the GOR/PR conflict kept visible, a few softened strength words, contributions only in `moves`. B then looks like an improvement on contributions, Table 1 and strength words, but a step back on figures and on GOR/PR fidelity. Verdict: A, narrowly.
- **B read first.** B sets the baseline: full contributions, strong verbatim handling, full Table 1, figures named. A then adds figure content B lacks and exposes B's flattening of the GOR/PR claim. A's Table 1 label error and missing contributions count against it, but they don't outweigh losing what the figures show and an article inconsistency. Verdict: A, narrowly.

**The verdict held in both orders: A, by a narrow margin.**
