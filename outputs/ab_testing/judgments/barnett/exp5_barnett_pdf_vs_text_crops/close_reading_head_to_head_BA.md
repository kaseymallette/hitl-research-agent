# Close readings, head to head — runs A and B

**Article:** Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866.

| Run | `id` |
|---|---|
| A | `182e2233-37de-4fde-b637-d787f5cc0fef` |
| B | `b52aa04e-d9f7-4e11-8e78-fbab1dd1da59` |

**How I worked.** I read the article from text extracted with PyMuPDF and viewed the page-1 graphical abstract as an image. I used `references/claims_reference.md` as written. I didn't read any other judgment or either run's argument evaluation. The mechanical checks below were run with a script over the extracted text. It normalizes whitespace, soft hyphens and diacritics, and compares reference entries as letters and digits only, because the PDF breaks URLs across lines. Per the rubric, I didn't rescore A1 from a random 30-claim sample for this comparison. Instead I checked every place where the two runs differ against the passage.

---

## Shape of the two readings

| | A | B |
|---|---|---|
| Steps | 26 | 25 |
| Claims (verbatim) | 109 (17) | 117 (13) |
| Support items | 46 | 55 |
| Reference entries given | 64 | 64 |

The two readings are very alike. They break the article at nearly the same points, from Highlights/Abstract through §6.3 plus the back matter. Each gives one step per §4 subsection. They word many claims almost the same way, and both keep the article's order. A splits §2 into two steps and puts Table 1 together with the WUE definition. B gives §2 one step and Table 1 a step of its own, with one claim per table row. Neither pads. A reader could follow the article's argument from either one alone.

---

## Mechanical checks (A4)

| Check | A | B |
|---|---|---|
| Verbatim texts found in the article | 16 / 17 | 13 / 13 |
| Numbers found in the article's text | 101 / 101 | 97 / 97 |
| Reference entries matching the article's list (in substance) | 64 / 64 | 64 / 64 |
| Entries or markers carrying text-extraction debris | 10 entries, 4 citation markers | 0 |

- **A's verbatim failure (C18.2).** A gives *"Digital water sobriety challenges the assumption that AI expansion should proceed without considering water constraints"* as verbatim. The article reads *"Digital water sobriety, analogous to frameworks in climate and energy policy, challenges the assumption…"* (§5.1). A cut the inserted clause without marking the cut. Under A1 that's a 0: a `verbatim` text that isn't the author's wording.
- **A's garbled references.** Ten of A's `reference_entry` values and four `citation_text` markers carry stray diacritic glyphs where the extraction displaced them. Examples: `(Yanez-Barnuevo, 2025˜ )`, `(Holzle, ¨ 2022)`, `(Swinhoe, 2023;H¨olzle, 2022)`, `Deschˆenes`, `Lathuilli`ere`, `Guti´ ´errezMontenegro`. They identify the right works, but they aren't the entries "exactly as written" in the printed article. B gives the same 64 entries with the printed spelling (Hölzle, Yañez-Barnuevo, Lathuillière, Vögele).
- **Images.** The only image-based element is the graphical abstract. Neither run reads a value from an image, since it contains no numbers. Table 1 is printed as text, so its numbers count in the text checks above. Both runs' Table 1 numbers pass.

---

## What each caught that the other missed (against `claims_reference.md`)

Coverage of the reference types is otherwise the same. Both catch C1–C6, AB1–AB7, H1–H2 verbatim (H3–H5 only through the abstract and body equivalents), CO1–CO26, and all six rows of T1 with footnotes. Neither records §5.2's restated Google 25% and Microsoft 42% figures, or §6.2's mechanism list, as claims. Both mention them in `meaning` as repetitions, which the instructions allow.

**Caught by B, missed by A**

- **F1, graphical abstract.** B's step 1 describes it: it links AI expansion and data centers to three water pathways, then branches to technical solutions and policy responses. That matches the image. B gives this in `meaning` rather than as a paraphrased claim, and it doesn't list the contents of the two branch boxes. So it's caught, but thinly. A never mentions the graphical abstract.
- **CO17, all five research priorities.** B records all five §6.1 priorities as claims, including ecological monitoring of lakeside and subsea systems (C22.4). A records four. It mentions the ecological-monitoring priority only in `meaning`, as a restatement.
- **§5.1's third dimension (part of C1 / CO12).** B records it as a claim (C17.2): *"demanding transparent reporting, including mandatory facility-level WUE metrics."* A's step 18 records the "challenges the assumption" sentence, the urgency, and the siting market failure. It leaves out the reporting dimension and says only in `meaning` that the three dimensions "are restated".

**Caught by A, missed by B**

- **CO23's scope condition on curtailment risk.** The article applies the forced-curtailment risk to *"Data centers employing once-through or open-loop cooling"* (§4.2). The paragraph before describes closed-loop installations. A keeps the condition in its support item: "The author applies analogous constraints specifically to once-through or open-loop data-center cooling." B's C12.4 and its support drop the condition entirely. They give the risk to "natural-water cooling" in general.
- **The prose 25,500 m³/yr figure for a 1 MW facility (§3).** A records it as support (C7.1). B's step 6 `meaning` says the prose "repeats the table's 25,500 m³ annual example", but B never records the §3 sentence as a claim. It appears in B only through Table 1 (C5.1).
- **Table 1 footnote b, in full.** A gives both halves: returned water has negligible evaporative loss, yet thermal pollution still occurs through discharge. B's C5.3 keeps only the first half ("water is returned to its source"). The thermal side shows up in B only through the row's "5–8 °C thermal discharge" trade-off.

---

## Where each is wrong and the other isn't

**A**

1. **C18.2:** a `verbatim` text with an unmarked cut (see A4). This is A's one A1-0 among the claims checked.
2. **Step 4 misdescribes the article's layout.** Its `location` reads "including its continuation printed after the Section 3 heading". Its `meaning` and the `reading_plan` say the methods passage is "interrupted" or "split". In the article, §2 runs continuously into the §3 heading on p. 2. The split was in A's input, not the article, and A reports it as a feature of the source.
3. **Input artifacts leak into the record.** Three support items say "Table 1 (gap T1), read from the retained image". Table 1 is printed as text, and "gap T1" is a label from A's preparation, not the article's.
4. **Garbled citation markers and entries** (see A4).
5. **C13.3's claim text broadens scope:** "Natural-water-body cooling can expose data centers to forced curtailment." Its own support item restores the once-through/open-loop condition, so A's record as a whole is right. The claim text read alone, though, says more than the author does.

**B**

1. **C12.4 drops a scope condition.** "Natural-water cooling can create operational and financial risk from thermal-discharge limits" extends a risk the author limits to once-through and open-loop systems. It reaches the closed-loop systems the same subsection introduces as the main case. Nothing in B restores the condition. Under A1 that's a 1: supported, but with the scope condition dropped.
2. **C17.2 rewords slightly:** "challenges unconstrained AI expansion" for the author's "challenges the assumption that AI expansion should proceed without considering water constraints". It's marked `paraphrased` and is close, but it turns a challenge to an assumption into a challenge to the expansion. Minor.

**Wrong in both (so not a difference):** C13.1 (A) and C12.1 (B) both give §4.2's closed-loop coupling as something that "can eliminate" consumptive withdrawals. The article says "eliminating", unhedged, then qualifies the systems in the next sentence. Both add the same small hedge.

---

## Strength of language (A3)

The two runs are alike, and both are close to a 2. They keep "Projections suggest… could reach", "If this increase in AI use continues", Bloomberg's "suggests about two-thirds… built or planned", the inference in "suggesting economic or operational constraints" about Natick, Espoo's "expected", "may not reduce on-site water consumption", and the strong claims at full strength ("systematic disregard", "inadequate", "governance failure, not technical constraint", "irreversibly deepens"). B's `meaning` fields flag the status of several claims well. They note that the application ranking is the author's value judgment rather than an empirical assessment, that Virginia's bill is only proposed, and that the power-plant curtailment is an analogy, not something observed at the named sites. Each run has one scope slip on the same §4.2 curtailment risk. In B the slip goes unrepaired. In A the claim text slips but its support repairs it.

---

## Verdict

**B is the better close reading, narrowly.**

The reasons, by criterion:

- **A1 (attribution fidelity).** A has the only `verbatim` failure found. B has the more serious scope slip (C12.4). Taken alone that slip would favour A. But A's own claim text broadens the same scope, and A is saved only by its support item. On balance this criterion is close to level, with A's unmarked cut in a quotation the clearer breach of the rubric's line between a 1 and a 0.
- **A2 (coverage).** B catches F1, which A misses entirely. B also records the fifth research priority and the third digital-water-sobriety dimension as claims. A's edge is footnote b and the prose 25,500 m³ figure, both of which B still carries through Table 1 in part. B covers more.
- **A4 (mechanical).** Numbers and reference content are level. B's verbatim texts all pass, and its citation markers and entries are clean. A's carry extraction debris that a downstream user would have to clean before citing.
- **A5 (detail and readability).** The two are about equal in length and evenness. B's one-claim-per-row Table 1 is easier to use. A's record also carries false statements about the source's layout and preparation labels ("gap T1", "retained image", "prepared text"), which a reader could take for facts about the article.

The gap is small. Most of each reading is interchangeable with the other, and B's dropped once-through/open-loop condition is the single most substantive distortion in either run. B wins on more criteria with fewer errors overall, but not by a wide margin.

## Order check

- **Reading A first, then B.** With A as the baseline, B's differences show up mostly as gains: the graphical abstract, the complete §6.1 list, the reporting dimension, a clean quotation, and clean citations. B's one loss is the dropped curtailment scope. **Verdict: B.**
- **Reading B first, then A.** With B as the baseline, A's scope repair on §4.2 and its fuller footnote b stand out first, and they favour A. But A then shows the unmarked quotation cut, the missing graphical abstract, the missing fifth priority and third dimension, and the layout misdescription and preparation labels. Its claim text at C13.3 also repeats the broadening that it later repairs. **Verdict: B.**

The verdict held in both orders: **B, narrowly.** One caveat: both passes were made in one session by one reader, so they aren't fully independent. The order check guards against anchoring on whichever run comes first, but it doesn't replace a second reader.
