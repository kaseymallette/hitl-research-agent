# Close readings, head to head — runs A and B

**Article:** Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866.

| Run | `id` | Steps | Claims | Support items | Citations |
|---|---|---|---|---|---|
| A | `b52aa04e-d9f7-4e11-8e78-fbab1dd1da59` | 25 | 117 | 55 | 64 |
| B | `182e2233-37de-4fde-b637-d787f5cc0fef` | 26 | 109 | 46 | 64 |

**How this was judged.** I read the article (text pulled out with PyMuPDF, page layout checked by block position) and `claims_reference.md`, then read every claim and support item in both runs. I didn't sample: the runs are close enough that a 30-claim sample could miss the few places where they differ. Verbatim texts, numbers and reference entries were checked by script against the extracted text after normalizing spacing, diacritics and line-break hyphens. Following the rubric, A1–A5 are the grounds for the comparison, not a full rescore.

**Overall picture.** The two readings are very much alike. They use the same step boundaries, almost every claim is recorded the same way, and both have the same habit of putting a description of the citation ("The author cites…") in the support slot instead of the evidence itself. The differences are few and small, and they are listed below.

---

## What each caught that the other missed (against `claims_reference.md`)

### Caught by A, missed by B
- **F1, the graphical abstract.** A's step 1 describes it in `meaning`: AI expansion and data centers lead to three water pathways, which then branch into technical solutions and policy responses. That is accurate, though it sits in `meaning` rather than as a paraphrased claim. B never mentions the graphical abstract. This is the only reference item one run covers and the other misses entirely.
- **CO17, the ecological-monitoring research priority.** A records it as a claim (C22.4). B mentions it only in step 23's `meaning` ("restated as another of the five priorities"), so B's claims list only four of the five priorities.
- **A smaller point of reading.** A's step 9 `meaning` notes that the body states the two-thirds figure more carefully than Highlight H2 does ("built or planned since 2022", from a Bloomberg analysis). The reference flags exactly this difference. B records both versions but doesn't point out the gap.

### Caught by B, missed by A
- **CO23's scope condition on the curtailment risk.** The article applies the forced-curtailment risk only to "once-through or open-loop cooling" (§4.2, p. 4), while the systems that section describes are closed-loop. B keeps this: C13.3's support says "The author applies analogous constraints specifically to once-through or open-loop data-center cooling." A's C12.4 states the risk for "natural-water cooling" in general and drops the condition. The reference singles this condition out.
- **AB3 in the body, with its condition.** In §1 the 4.2–6.6 billion m³ projection depends on "If this increase in AI use continues." B records it as support with the condition intact ("Conditional on continued growth in AI use…"). A records only the U.S. 280-billion-litre figure as the claim and mentions the global figure only as a "restated" projection inside a support item about citations.
- **CO23's "raise ecological questions."** B keeps the author's framing: "leave unresolved ecological questions about warming plumes, stratification, and cumulative effects" (C13.2). A turns the questions into possible effects: "can coexist with warming plumes, altered stratification, and cumulative ecological impacts" (C12.2), and it also drops "if widely scaled."

### Missed by both
- **H3's attribution.** "Deployment remains limited **by policy gaps**." Both runs record only the abstract's version, "deployment remains limited," which leaves out the cause the highlight names.
- **H5 as a separate highlight.** Both fold it into the digital-water-sobriety claim.
- **CO22's "located south of the Arctic Circle"** and **CO23's explicit mention of EU temperature-limit regulations.** Both runs cover the regulatory analogy only indirectly.
- **"Five interconnected research priorities remain major bottlenecks."** Neither run records this framing sentence from §6.1 as a claim.

Everything else on the reference list (C1–C6, H1–H2, H4, AB1–AB7, CO1–CO26, T1 with all six rows and its three footnotes) is caught by both runs, with what it shows. Both readings go to the end of the article, including the back matter.

---

## Where each is wrong that the other isn't

### Run A
1. **C12.4 drops a scope condition (A1 = 1, A3).** As described above, A states the curtailment risk for natural-water-body cooling in general, though the article limits it to once-through and open-loop systems. A's own `meaning` for that step correctly calls the power-plant comparison an analogy, but the claim it records still overstates the risk's scope.
2. **C12.2 changes the claim's force (A1 = 1).** "Raise ecological questions about" becomes "can coexist with," and "if widely scaled" is dropped. The result is more definite than the article.
3. **C14.2 adds a hedge (minor).** "Other facilities reduce pressure on potable supplies" becomes "can reduce pressure." B keeps the author's indicative.
4. **C14.4 drops qualifiers (A1 = 1).** "Priced far below its scarcity value in most jurisdictions" becomes "priced below its scarcity value," losing both "far" and the jurisdictional qualifier. B loses "far" too but keeps the jurisdiction qualifier as "generally."

### Run B
1. **A verbatim text that isn't verbatim (A1 = 0, A4 fail).** C18.2 is marked `verbatim`: "Digital water sobriety challenges the assumption that AI expansion should proceed without considering water constraints." The article's sentence is "Digital water sobriety, **analogous to frameworks in climate and energy policy,** challenges the assumption…" (§5.1, p. 5). The clause is removed without an ellipsis. Nothing is invented, but the quotation is not the author's exact wording, and the analogy it drops is the one the author uses to frame the whole concept. This is the only verbatim failure in either run. (A paraphrases the same sentence, C17.2, and also leaves out the analogy, but A doesn't present its version as a quotation.)
2. **Step 4's location describes a layout the article doesn't have.** B's location reads "Section 2, review-method passage, including its continuation printed after the Section 3 heading," and its `reading_plan` says the "prepared text contains an interrupted methodological passage." In the PDF, Section 2 runs from the lower left column to the top of the right column, and the Section 3 heading comes after it (p. 2). No part of Section 2 is printed after the Section 3 heading. This mistake comes from B's input text, not the article. It also led B to move "This work does not perform an independent water footprint calculation" (C4.4) ahead of the scope definitions, where the article places it after them.
3. **Damaged citation markers and reference entries (A4).** Four `citation_text` values carry stray characters from text extraction: "(Yanez-Barnuevo, 2025˜ )", "(Swinhoe, 2023;H¨olzle, 2022)" twice, and "(Holzle, ¨ 2022)". Many `reference_entry` values contain displaced diacritics, spaces at line breaks inside URLs ("https://www.ve rtiv.com…"), and a lost hyphen ("LBNL2001637"). Every entry still matches the article's reference list once normalized, so none is invented. They just aren't the entries "exactly as written." A's markers and entries are clean, with diacritics read correctly (Yañez-Barnuevo, Hölzle, Döll, Núñez).
4. **Pipeline labels in the record.** Table 1's support items begin "Table 1 (gap T1), read from the retained image…" "Gap T1" is an internal annotation, not something in the article. Marking the table readings `paraphrased` is harmless (Table 1 is printed as text, so they could have been quoted), but the label shouldn't be in the record.

Neither run invents a claim, cites a figure that doesn't exist, misreads a number, or invents or completes a reference.

---

## Grounds by criterion

| Criterion | A | B | Edge |
|---|---|---|---|
| **A1 Attribution fidelity** (all claims read, not sampled) | No 0s. About four 1s (C12.2, C12.4, C14.4; C17.3 softens "critical awareness gap" to "limited," and B does the same). | One 0 (C18.2, the verbatim elision). About three 1s (C14.4 drops "far," C18.3 the same "awareness" softening, and C13.3's claim generalizes, though its support restores the scope). | Roughly even. A has no 0s; B has fewer 1s. |
| **A2 Coverage** | Everything on the reference list, plus F1 in `meaning`; all five §6.1 priorities as claims. | Everything except F1; one §6.1 priority only in `meaning`. | **A** |
| **A3 Strength of language** | Inconsistent, so 1: most qualifiers survive, but the curtailment scope and the "questions" framing in §4.2 shift toward more certainty. | Inconsistent, so 1, but closer to 2: §4.2's scope and framing survive and the §1 projection keeps its condition; "far below" is lost. | **B**, slightly |
| **A4 Mechanical checks** | Verbatim 13/13; numbers 97/97; reference entries 64/64 matched, 0 null, clean. | Verbatim 16/17; numbers 101/101; reference entries 64/64 matched, 0 null, but 4 damaged citation markers and many entries carrying extraction artifacts. | **A** |
| **A5 Detail and readability** | 25 steps evenly spread over the article. Table 1 is split into six row-level claims, easy to follow. Its `meaning` notes on repetition and on evidence types (withdrawal vs. consumption, planned vs. operating) are consistently useful. | 26 steps, also even. Table 1 is packed into one claim with three dense supports. One step's location is wrong, and the pipeline labels leak. Its `meaning` notes are as perceptive as A's (e.g., on the quotation marks around "Waterless", the Natick inference, and the attribution gap in §6.1). | **A**, slightly |

Neither reading is padded. A's extra claims come mostly from separating Table 1's rows and splitting compound statements, not from repetition.

---

## Verdict

**Run A is the better close reading, by a narrow margin.**

A is ahead on three of the five criteria. It covers more (the graphical abstract, all five research priorities as claims), its mechanical record is cleaner (every verbatim exact, citation markers and reference entries clean), and it has no error of the kind the rubric treats as worse than a softening. The rubric deliberately keeps a 1 and a 0 apart: B's C18.2 presents an edited sentence as the author's exact words, and A has nothing comparable.

B's advantage is real, though, and it sits on substance rather than form. B keeps the once-through/open-loop condition and the "raise questions" framing in §4.2, and the conditional form of the §1 projection. These are exactly the kinds of qualifiers A3 exists to protect, and the reference list flags the first one explicitly. A reader relying on A's §4.2 alone would believe the curtailment risk applies to the closed-loop systems the section describes.

So A wins mostly on completeness and record-keeping, and B is the slightly more faithful reader of qualifiers. I chose A because B's problems include an actual misquotation and a misdescribed location, while A's are fixable softenings and strengthenings. The margin is small enough that a researcher who weighs A3 above A2 and A4 could reasonably choose B.

## Order check

- **Reading A first, then B.** A's §4.2 shifts register first as weaknesses. B then turns out to keep those qualifiers but to fail a verbatim check, misdescribe step 4's location, miss F1, and carry damaged citation markers. **Verdict: A, narrowly.**
- **Reading B first, then A.** B's handling of the §4.2 scope and the §1 condition makes a strong first impression, and A's C12.2 and C12.4 then stand out as A3 failures. Even so, coming to A second makes B's C18.2 elision and step 4 location error more visible by contrast (A paraphrases the same sentence honestly and places "does not perform an independent calculation" where the article does), along with A's clean markers and its coverage of F1. **Verdict: A, narrowly.**

**The verdict held in both orders.** Because the margin is narrow and the deciding points are few, the choice of configuration should not rest on this one article.
