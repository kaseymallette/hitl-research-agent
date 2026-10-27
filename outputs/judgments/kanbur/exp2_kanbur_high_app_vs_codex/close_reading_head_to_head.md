# Close readings, head to head: run A vs run B

**Article:** Kanbur BB, Wu C, Duan F. "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system." *Int J Energy Res.* 2020;44:10453–10470.

**Files compared**

| Run | File | `id` | Steps | Claims | Support items | Claims marked verbatim |
| --- | --- | --- | --- | --- | --- | --- |
| A | `runs/A/analysis.json` | `b050b54f-75ac-4a51-be4e-eceacaea58e8` | 42 | 167 | 104 | 0 |
| B | `runs/B/analysis.json` | `fa401e5e-ea12-498b-9ccb-24aa8aa410fa` | 37 | 158 | 111 | 2 |

**How I compared them.** I read the article (text extracted with Ghostscript `txtwrite`; figures checked against the reference list's descriptions and the extracted labels), `references/claims_reference.md`, and every step, claim and support item in both runs. As the rubric allows, I didn't rescore each criterion. I used A1–A5 as the grounds for comparison and checked every claim instead of a seeded sample of 30. No other judgment and no argument evaluation was opened.

Both readings run from the Summary to Appendix C, so neither stops early. Both are careful, scope-aware readings. They differ mostly at the edges, listed below.

---

## 1. What each caught that the other missed (against `claims_reference.md`)

### Caught by A, missed by B

- **The enumerated contributions C-a, C-b, C-d.** A records all four contributions (C5.0–C5.3): "not previously investigated", "first use of two-phase immersion waste heat for desalination", the "new alternative… especially for low DC cooling loads" (C-b), the matrix's hedged usefulness (C-c), and the optimization objectives and constraints (C-d). B records only C-c (B C4.4). It treats the rest as "restat[ing] the novelty and methods already announced in the Summary" (B step 4, moves and meaning). The Summary doesn't contain them. The novelty claims ("has not been investigated before", "first time") and the three-objective statement first appear in Section 1. So B never records the article's central novelty claim as a claim. The Conclusion repeats it ("It was the first time…", S5.0a), and B mentions it there only in the moves text.
- **Table 1's actual values (T1).** A gives every current/reference value pair and every relative difference at 40–70 °C (A C18.0–C18.1). A also notes that the second and third column groups carry the same printed header "q^T (W/m²K)" and refuses to guess which flux each one is. B gives only the relative differences (B C14.1 support).
- **Table 3's auxiliary equations (T3).** A lists the printed auxiliaries, including the anomalous "c3 = u3" in the permeate-pump row, and labels them as readings (A C21.1). B gives only a general paraphrase of the table (B C19.3).
- **S5.1, "The hybrid system can be efficiently operated for the low data center cooling loads."** A records it (A C33.1), with the "satisfying performances" grounds as support. B folds it into a recommendation (B C31.1) and loses the claim itself.
- **S1.9, "satisfying steady performance"** of the 21 kW prior setup (A C4.0). B C4.1 keeps the 21 kW but drops the result.
- **Appendix coefficients.** A transcribes the A1–A3, B1–B9 and C1–C3 expressions and notes that G₁ᵢ is used but never defined. B describes their structure and also notes the missing G₁ᵢ. Under the reference's scope, appendices aren't a source of claims, so this matters only for A5 detail.

### Caught by B, missed by A

- **AB6**, the three-aspect assessment "concerning the unique exergy-cost matrix of the original design." B C0.3 has it. A's Summary step has no counterpart; A's C5.2 picks up the matrix only at the contributions.
- **S2.2, the immersion setup "was experimentally operated and verified in our previous work."** B C5.4 has it; A step 6 omits it.
- **S3.2c, the cooling side's prior validation.** B records it as a claim with both citations (B C15.0). A mentions it only in a meaning field (A step 15).
- **Separation of abstract claims.** B keeps AB7, AB8, AB9 and AB10 as separate claims (B C0.4–C0.7). A merges them in pairs (A C0.4, C0.5), against the prompt's "keep distinct claims separate." Every item is present in A, so this is a granularity difference, not a coverage miss.
- **Figure 8's axis.** B states the 3.719–3.727 year axis that magnifies the bars (B C27.0). A says only "narrowly scaled axis around 3.72 years."

### Caught by both

AB12's 5.12 vs 5.13 cm² discrepancy. The COP ratio of 2.15× in the results vs 1.5× in the Conclusion (S4a.2 / C-5.1). The water-rate drop of "nearly 65%" vs the Conclusion's 1.85× (S4b.1 / C-5.2). Eq 24 printed identical to Eq 22. The c_w unit printed as "m³/h". Figure 5B's colour scale starting at 27.20 while the text says 27.3%. Figure 6's surfaces rising with membrane area against the prose. All the stated scope limits: S3.1d, S3.2d, S4d.2, S4f.2, S4h.5.

### Missed by both

- **C-5.5's rewording.** The Conclusion says feasible "for further real-scale demonstrations"; the abstract says "for real applications." Both runs mention the feasibility restatement only in moves or meaning, and neither notes the change of wording.
- **C-5.6's changed explanation.** The Conclusion attributes the DCMD's minimum levelized cost to "lower exergetic costs." Section 4 gives lower *capital* costs (S4g.3). Neither run records the Conclusion's reason.
- **Figure 9's "$/h" axis labels** against the text's SGD/h.

---

## 2. Where each is wrong and the other isn't

### A

- **A C27.0 smooths over the GOR/PR contradiction.** The article says GOR and PR "have the highest values at the minimum membrane area, 5 cm²," and then that "the maximum GOR and PR values are nearly 14 times higher than the GOR and PR values of the minimum membrane area." A gives the second half as "nearly fourteen times the values at **the other end of the area comparison**." That replaces the author's wording with a version that removes the self-contradiction. A does record the figure's opposite trend (C27.1) and says prose and figure differ. But the contradiction *inside* the prose is hidden, and the claims reference marks this passage (S4d.1) as one a reading most needs to get right. Under A1 this is at best a 1, an altered claim. Arguably it's a 0, since it isn't what the author said.
- **No verbatim at all.** That isn't wrong under A1, because every `paraphrased` marker is honest. But the prompt asks for "the author's own words where you can," and A never quotes the author, not even plain sentences like the Summary's efficiency figures. That leaves A4's verbatim check with nothing to test.

### B

- **B C14.1 makes up Table 1 column labels.** It reports differences "for total heat flux" and "for vapor heat flux." The table prints both column groups with the same header, "q^T (W/m²K)." Those labels are B's own inference, presented as a reading of the table. A explicitly declines to make that inference.
- **B C4 dismisses the contributions as restatements.** As above, B calls three contributions restatements of the Summary when the Summary doesn't contain them. That's a misdescription of the article's structure, and it causes B's biggest coverage gap.
- **B C28.4 softens "dramatically increase" to "increase strongly".** A keeps "dramatically" (A C30.5).
- **B's ref 30/32/39 entries print "Lienhard V JH".** The extracted reference list reads "Lienhard VJH," as A has it. This is a spacing difference only, and it may come from the extractor, so I don't count it as a failure.

### Shared softenings (not differences)

Both drop "clearly" from "clearly infer… very good agreement" (S3.2b). Both drop "seems" from "seems sufficient" for the payback method (S3.3c). Both phrase these as "the authors infer/call" or "considered/regard," which keeps the attribution but lowers the certainty marker.

---

## 3. The criteria as grounds

| Criterion | A | B | Edge |
| --- | --- | --- | --- |
| **A1 Attribution fidelity** | No claim is the run's own inference posing as the author's. Markers are honest (all paraphrased). One significant alteration (C27.0, the GOR wording), plus the two shared softenings. | Markers are honest; both verbatim quotes are exact. One invented reading (C14.1, the Table 1 labels), one softening (C28.4), plus the shared softenings. GOR/PR contradiction recorded exactly as the author makes it (C25.0). | Even. B is better on the most delicate passage (S4d.1); A is better on Table 1. |
| **A2 Coverage** | Contributions 4/4. Abstract 11/12 (AB6 missing). Figures 10/10 read. Tables 3/3 read in full. Misses S2.2, the C-5.5 wording change and C-5.6. | Contributions 1/4 (C-a, C-b, C-d missed). Abstract 12/12. Figures 10/10 read. T1 partly read (differences only, labels invented), T3 read only in general terms. Misses S5.1, the C-5.5 wording change and C-5.6. | **A**, mainly on the contributions. |
| **A3 Strength of language** | Hedges and scope limits survive almost everywhere ("may", "can", "as far as we know", "crucial", "dramatically"). Two shared drops. | Same pattern, plus "dramatically" → "strongly." | A, slightly. Neither shows a one-directional shift. |
| **A4 Mechanical checks** | Verbatim: 0 to check. Numbers: all 349 numeric tokens in claims and support found in the text. Reference entries: 68/68 match the article's list (3 confirmed by eye where the two-column layout interleaves). Image readings (Figs 5B, 6, 8; Eqs; Table 3) correctly marked paraphrased. | Verbatim: 2/2 exact (confirmed by eye; one runs across interleaved columns). Numbers: all 317 found. Reference entries: 74/74 match, with the spacing note above. Image readings correctly marked paraphrased, except the Table 1 labels. | Even. B has more to check and passes. A is clean but gives no verbatim to test. |
| **A5 Detail and readability** | 42 steps, even across the main text. Four steps go to references, two with no claims, which is mild padding. A reader could follow the argument from claims and meaning alone. Highest numerical detail (tables, appendices). | 37 steps, even. References consolidated into one step. Splits multi-citation support into one item per cited work, closer to the prompt. Equally followable, slightly leaner. | Even. A is more detailed, B tighter. |

On the number check: it confirms each number appears somewhere in the article text. It doesn't confirm that a number is attached to the right passage. I checked that by hand for every result value in Sections 4 and 5 in both runs, and found no misplaced number in either.

---

## 4. Verdict

**Run A is better, by a modest margin.**

The deciding ground is **A2 coverage of the enumerated contributions.** A records all four. B records one, and wrongly writes off the other three as restatements of the Summary, so the article's own "first time / not investigated before" novelty claim never appears as a claim anywhere in B. A also reads Tables 1 and 3 in full and as printed. B's reading of Table 1 adds column labels the table doesn't print. That is a small A1/A4 fault, and exactly what the prompt warns against when it says to describe an element "without presenting your reading of it as the source's printed words."

B's strengths are real and keep the margin small. B records the GOR/PR passage faithfully where A smooths it. B covers the abstract completely and keeps its claims separate, and it uses exact quotation correctly where A uses none. If a later reader needed to find the article's internal inconsistencies from the close reading alone, B would serve slightly better on S4d.1. A would serve better on the tables. On attribution, strength of language and mechanics, the two are close to even. The contributions gap is the largest difference, which is why the verdict goes to A.

## 5. Order check

- **Reading A first, then B.** A sets the baseline: full contributions, full tables, appendix detail. Reading B against it, the missing contributions and the made-up Table 1 labels stand out. B's better handling of S4d.1 and its complete abstract partly offset them. **Verdict: A.**
- **Reading B first, then A.** B sets the baseline: an exact GOR/PR record, complete abstract claims, two correct verbatim quotes. Reading A against it, A's C27.0 smoothing, merged abstract claims, missing AB6 and absence of quotation stand out. But A then shows three contributions, the full Table 1 values, Table 3's auxiliaries and S5.1, none of which B has. Those outweigh what B gains. **Verdict: A, narrowly.**

The verdict holds in both orders, so it isn't a tie. The margin is smaller when B is read first, which matches calling it modest.
