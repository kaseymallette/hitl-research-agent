# Close readings, head to head — runs A and B

**Article:** Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866.

| Run | `id` | Steps | Claims | Support items | Verbatim items |
|---|---|---|---|---|---|
| A | `182e2233-37de-4fde-b637-d787f5cc0fef` | 26 | 109 | 46 | 17 |
| B | `cb4cc7f2-e7a3-4b12-862c-4db104ab494a` | 20 | 84 | 44 | 7 |

**How I checked.** I extracted the article text with Ghostscript (`txtwrite`) and rebuilt the two-column order with a short script. I read the article in full and compared both runs against `claims_reference.md` (IDs C, H, AB, CO, F, T below are that list's). I checked every verbatim item, every number and every `reference_entry` in both runs by script, then looked by hand at each failure. I read no other judgment and no argument evaluation.

**Shared input artifact.** Both runs say they worked from a "prepared text" in which the §2 method passage was split. Both read the fragments as one method description and neither treats the split as an argumentative turn, so the artifact counts against neither. A's step location for it ("its continuation printed after the Section 3 heading") describes their input, not the printed article. In the PDF the continuation sits at the top of p. 2's right column, before the §3 heading.

---

## What each caught that the other missed (A2, against `claims_reference.md`)

| Type | A | B |
|---|---|---|
| Contributions C1–C6 | 6/6 | 6/6 |
| Highlights H1–H5 | 4 caught, 1 partial: H3's "limited by policy gaps" is replaced by the abstract's "deployment remains limited" | 5/5: C5 keeps "limited by policy gaps" |
| Abstract AB1–AB7 | 6/7. AB4 ("Many data centers…") is not recorded separately and is folded into the H2 highlight. AB3 and AB7 are kept verbatim. | 6/7. AB4 is folded the same way. AB3 drops "Projections suggest". AB7 is merged into the C1/digital-water-sobriety claim (C6). |
| Conclusions CO1–CO26 | 26/26. The CO17 ecological-monitoring priority appears only in `meaning`, not as a claim. | 24 caught, 2 partial (CO19, CO20); CO6 compressed |
| Figures F1 (graphical abstract) | missed | missed |
| Table T1 | caught: all six rows, all three footnotes, row citations attached | caught: all six rows and all three footnotes, no citations attached |

Both readings run through to the end of the article (§6.3), plus the CRediT, interest and data statements.

**Caught by A, missed or only partly caught by B:**
- **CO19:** §6.3's "Technical pathways exist… suggesting outcomes reflect policy and siting choices, not technological necessity." A records it as a claim (C103) with the Luleå "25 million liters… suffices" figure and the subsea example as support. B has no such claim. Its only trace is a paraphrased support item under the Colón claim (C79), so the inference and the Luleå sufficiency figure are lost.
- **CO20:** "The Colón case epitomizes governance failures," with its three-part diagnosis (siting that puts electricity costs first, disclosure that hides local impacts, frameworks treating water as unlimited). A records the diagnosis as C104's support. B keeps only the final verbatim sentence.
- **CO6:** A records Colón's institutional mechanism as four separate claims (C40–C43): the institutional mechanism, CONAGUA, legal standing that outlasts scarcity, and "not unique to Mexico." B folds all of it into one synthesized claim (C30) plus support. The point survives, but the steps of the author's argument do not.
- **CO9:** A keeps "merit further assessment." B drops it.
- **Table 1 citations:** A attaches each row's printed citations. B's table support items carry none.

**Caught by B, missed or only partly caught by A:**
- **H3:** "deployment remains limited by policy gaps," the highlight's attribution of the limit to policy. B keeps it. A gives only the abstract's unattributed "limited."
- **CO17, fifth priority:** B records the ecological-impact-monitoring research priority as a claim (C71). A mentions it only in `meaning`, so A's claim record lists four of the five priorities.

The net balance on coverage favours A. Its two gains are both §6.3 closing conclusions; B's two are a highlight phrase and one research priority.

## Where each is wrong that the other isn't (A1, A3)

I compared the two runs claim by claim wherever they record the same passage. Faithful renderings shared by both runs aren't listed.

**A only:**
1. **Scope stripped from the curtailment claim (§4.2, A C51).** The claim reads "Natural-water-body cooling can expose data centers to forced curtailment…". The article confines this risk to "Data centers employing once-through or open-loop cooling," whereas the section's own examples are closed-loop. A's support item restores the condition ("applies analogous constraints specifically to once-through or open-loop"), but the claim field widens it. B's C37 keeps the condition in the claim. This is A1 = 1.
2. **Citation attached to the wrong scope (§1, A C10).** A's support says Yañez-Barnuevo is cited "for its three-part account" of the footprint. The article attaches that citation only to "thousands of liters per wafer." B attaches it correctly.
3. **Verbatim with a silent elision (§5.1, A C72).** A gives "Digital water sobriety challenges the assumption…" as verbatim. The article reads "Digital water sobriety, analogous to frameworks in climate and energy policy, challenges…". The appositive is removed without marking, so the text is not exact wording. This is A1 = 0 on the verbatim test, though the meaning is intact.

**B only:**
1. **Hedge dropped (abstract, B C3).** "AI's global water footprint could reach 4.2–6.6 billion…" omits "Projections suggest." "Could" survives, and B's §1 step calls the forecast "conditional," but the abstract claim is firmer than printed. This is A1 = 1.
2. **Strengthened and synthesized claim (§3.2, B C30).** "Rigid water-allocation institutions create environmental-justice failures when industrial allocations persist through drought." The article says such allocation failures "raise fundamental environmental justice dimensions." B's claim is its own synthesis of three sentences and is stronger than the article's wording. This is A1 = 1, bordering on the run's inference sitting in a claim field.
3. **Support misattached (§6.3, B C79).** The Luleå/subsea contrast is offered as support for "…represents governance failure, not technical constraint." In the article that contrast supports a different sentence, the CO19 inference above, while the Colón verdict rests on the three-part diagnosis B omits.
4. **Merges of distinct claims.** C6 merges AB6 with AB7, and C9 merges the three footprint components with the scope statement. The prompt asks for distinct claims to be kept separate. Nothing is falsified, but the verbatim AB7 sentence becomes paraphrase.

**A3 (strength of language).** Both runs preserve the author's certainty well overall: "establish," "systematic disregard," "remain inadequate," "severely limited," "will persist absent regulatory correction," the "suggesting" on Natick, the "expected" on Espoo, and "governance failure, not technical constraint." Neither shifts systematically in one direction. A's single lapse is scope (C51). B's lapses run slightly toward firmer wording (C3, C30, the lost "merit further assessment"). I'd put both at 2 with minor exceptions, A marginally cleaner.

## Mechanical checks (A4)

| Check | A | B |
|---|---|---|
| Verbatim texts found in article | 16 / 17 (fail: C72, silent elision) | 7 / 7 |
| Numbers found in article text | 101 / 101 | 91 / 91 |
| `reference_entry` matching article's reference list | 64 / 64 non-null; 0 null | 53 / 53 non-null; 0 null |
| Readings of image elements | none; the graphical abstract is unread | none; the graphical abstract is unread |

Six of A's verbatim items and three of B's first failed the substring check. Each was a column or page break in the extraction, or a dropped trailing citation, and each passed on inspection. Both runs map citations to the same reference entries; the garbled `citation_text` strings ("Holzle, ¨ 2022", "Yanez-Barnuevo, 2025˜") are identical in both and come from the extraction. Table 1 is printed as text, so its values count as text numbers and all of them check out. Both runs mark Table 1 readings `paraphrased` and name the table, as instructed.

B is cleaner here, but on a much smaller verbatim base. A attempted 2.4× as many exact quotations and got one wrong.

## Detail and readability (A5)

A gives the article 26 steps against B's 20. A splits where the argument splits: §3.2's spatial evidence and the Colón case are separate steps, as are §5.1's framework, application spectrum, and awareness/values paragraphs, and §5.2 and §5.3. B combines §3.1 and §3.2 into one step (about 600 words, past the prompt's upper scale for dense text) and §5.2–5.3 into another. Neither pads; A's extra 25 claims are mostly separated sentences that B merged, not repetition. Both `meaning` fields track continuity well and flag restatements (the repeated Microsoft 42% and Google 25% figures, and the §6.2 mechanisms restated from §5.1). A's are slightly more precise about where the argument turns, for example the heat-collection versus heat-rejection distinction in §3.1. A reader could follow the argument from either. With A, a reader could also rebuild the steps of the Colón and §6.3 arguments; with B, only their conclusions.

---

## Verdict

**Run A is the better close reading, by a modest margin.**

- **Coverage (A2):** A captures every section conclusion as a claim, including the two §6.3 conclusions (CO19, CO20) that close the article's argument and that B reduces or misplaces. B's advantages (H3's "policy gaps," the fifth research priority as a claim) are smaller.
- **Attribution (A1):** both have about three altered items. A's are a scope widening that its own support corrects, one misattached citation, and one inexact verbatim. B's are a dropped hedge, a strengthened synthesized claim, and a misattached support item, plus merges of distinct claims. These roughly cancel, with A's being slightly more contained, since A's errors don't change the author's position.
- **Strength of language (A3):** comparable, and A is marginally cleaner.
- **Mechanics (A4):** B is perfect on a small verbatim base; A has one failure in 17. Numbers and references are flawless in both.
- **Detail (A5):** A's finer steps preserve the internal structure of the author's arguments where B compresses it, without padding.

B's main strength is economy and scope accuracy on the curtailment claim. Its main weakness is merging: where it compresses, the author's own steps (Colón's mechanism, the §6.3 inference) turn into B's summary of them.

## Order check

- **Reading A first, then B:** with A's separated claims as the baseline, B's merges stand out as losses (CO6, CO19, CO20, AB7), and its gains are H3 and one research priority. Verdict: A.
- **Reading B first, then A:** with B's compact reading as the baseline, A adds the §6.3 inference and Colón's diagnosis, while B's correctly scoped C37 shows up A's C51 slip and A's C72 elision. Those slips don't outweigh the missing conclusions. Verdict: A.

The verdict held in both orders: **A**, by a modest margin.
