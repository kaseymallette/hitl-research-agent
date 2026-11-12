# Close reading judgment — run A

- **Run:** A
- **File judged:** `runs/A/analysis.json`, `id` **182e2233-37de-4fde-b637-d787f5cc0fef**
- **Seed:** **20261025**
- **Reference list:** `references/claims_reference.md`, used as written.
- **Article text:** extracted from `article.pdf` with Ghostscript (`txtwrite`), then split back into its two columns with a small script. Passages that the column split garbled (the abstract, column bleeds, references that run across columns or pages) were checked by eye against the raw extraction.

**Claim numbering.** Claims are numbered C0–C108 in file order, counting from 0 across all 26 steps (step numbers also start at 0). Support items are numbered S0, S1, … within each claim. Run A has **26 steps, 109 claims, 46 support items and 64 citation links**. Every support item is marked `paraphrased`.

**How the sample was drawn.** `random.seed(20261025); sorted(random.sample(range(109), 30))` in Python 3 over the 0-based claim indices gave:
5, 6, 7, 9, 10, 17, 18, 25, 28, 43, 45, 46, 48, 49, 52, 54, 56, 61, 73, 74, 76, 79, 80, 86, 88, 92, 99, 100, 103, 106.

---

## A1. Attribution fidelity

**Claims (n = 30): score 2 — 28 (93%); score 1 — 2 (7%); score 0 — 0 (0%).**
**Support items on the sampled claims (n = 8): score 2 — 7 (88%); score 1 — 1 (12%); score 0 — 0 (0%).**

| # | Step / location | Form | Claim (abridged) | Claim | Support |
|---|---|---|---|---|---|
| C5 | 0 Abstract | para | "Digital water sobriety" links application justification, water-conscious siting, facility-level transparency | 2 | — |
| C6 | 0 Abstract | verb | "Achieving water-sustainable AI demands not merely…" | 2 (exact) | — |
| C7 | 1 §1 ¶1 | para | AI seems intangible and costless; every interaction produces waste heat needing water-intensive cooling | 2 | — |
| C9 | 1 §1 ¶3 | para | Three components; chip fabrication "thousands of liters per wafer" | 2 | S0: **1** |
| C10 | 1 §1 | verb | "This work focuses on operational water consumption for cooling…" | 2 (exact) | — |
| C17 | 3 §2 | verb | "Peer-reviewed sources were prioritized over the other two sources." | 2 (exact) | — |
| C18 | 3 §2 | verb | "This work does not perform an independent water footprint calculation…" | 2 (exact) | — |
| C25 | 5 §3 | para | WUE definition, L/kWh or m³/MWh | 2 | S0 (Higgins): 2 |
| C28 | 6 §3 | para | Cooling water use is substantial and accelerating with LLM/AI growth | **1** | S0 (Mytton; 2 L/kWh; 25,500 m³): 2 |
| C43 | 11 §4 intro | para | Substantial reductions technically achievable; each approach has trade-offs | 2 | — |
| C45 | 11 §4.1 | para | Hydropower not water-free; belongs in lifecycle assessment | 2 | S0 (Scherer & Pfister): 2 |
| C46 | 11 §4.1 | para | Cold-climate trade-offs: flexibility, transmission, backup cooling | 2 | — |
| C48 | 12 §4.2 | para | Closed-loop coupling to water bodies eliminates consumptive withdrawals | 2 | S0 (Hamina; Qiandao 17 °C/35 m/WUE<0.2/>90%): 2 |
| C49 | 12 §4.2 | para | Low consumptive use and favourable WUE leave ecological questions open | **1** | S0 (5–8 °C; no monitoring data): 2 |
| C52 | 13 §4.3 | para | Subsea facilities use seawater as a passive heat sink, with no freshwater consumption | 2 | S0 (Hainan, 400–800 servers, WUE 0): 2 |
| C54 | 13 §4.3 | para | List of potential subsea impacts | 2 | — |
| C56 | 13 §4.3 | para | Capital cost, maintenance, sites, regulation constrain subsea | 2 | — |
| C61 | 14 §4.4 | para | Non-potable costs; reclaimed water varies by region; dry cooling degrades in hot/dry climates | 2 | — |
| C73 | 17 §5.1 | para | Concentration reflects a market failure (drivers listed; water underpriced) | 2 | — |
| C74 | 17 §5.1 | para | Companies externalize costs; persists absent regulatory correction | 2 | — |
| C76 | 18 §5.1 | verb | "Digital water sobriety does not propose binary approval…" | 2 (exact) | — |
| C79 | 18 §5.1 | para | Water governance may offer structural advantages | 2 | — |
| C80 | 18 §5.1 | para | Effective DWS will require political will and enforceable regulation | 2 | — |
| C86 | 20 §5.2 | para | Voluntary, unstandardized WUE reporting obscures facility impacts | 2 | — |
| C88 | 21 §5.3 | para | Transparency severely limited; operators withhold data as commercially sensitive | 2 | — |
| C92 | 22 §6.1 | para | Benchmark datasets would enable targeted optimization | 2 | — |
| C99 | 23 §6.2 | para | Tiered DWS governance linking deployment to benefit and local availability | 2 | — |
| C100 | 23 §6.2 | para | Heat-recovery incentives would deliver co-benefits | 2 | — |
| C103 | 24 §6.3 | verb | "Computational infrastructure consuming public water during drought…" | 2 (exact) | S0 (Colón epitomizes governance failures): 2 |
| C106 | 25 CRediT | para | Sole author holds the listed CRediT roles | 2 | — |

**The scores below 2:**

- **C28 (1).** The article says demand is "accelerating sharply in the AI era" (§3, p. 3). The run gives "is accelerating", dropping "sharply". It also leaves out that the sentence is about data centers collectively *withdrawing* "billions of liters" at the global scale. That drops the withdrawal framing the article itself stresses in §2.
- **C49 (1).** The article: "These systems **may** have low consumptive water use and favourable WUE, but they raise ecological questions…" (§4.2, p. 4). The run states the low consumption and favourable WUE as given ("Low consumptive use and favorable WUE leave…"). The author's hedge is gone.
- **C9 S0 (1).** The run says the Yañez-Barnuevo citation supports the paragraph's "three-part account". In the article the citation is attached only to the last clause, chip fabrication consuming "thousands of liters per wafer" (§1, p. 2). The citation is real; the run stretches what it covers.

**Borderline cases scored 2.** C52 extends "eliminating freshwater consumption entirely" from the Hainan facility to subsea facilities as a class. Table 1 (Subsea: WUE 0, consumption 0) and §6.3 ("China's subsea installations achieve zero freshwater consumption") support that. C88's "because" links two adjacent sentences that the article plainly means to read together.

**Outside the sample** (not counted above, but relevant to A3 and A4): C23, C40, C50, C60, C71 and C77 would each score below 2. They are described under A3, and C71 under A4.

---

## A2. Coverage

Counted against `claims_reference.md`. The reading runs from the highlights to the back matter (CRediT, competing interests, data availability), so it does not stop before the article does.

| Type | On list | Caught with what it says | Caught without what it says / partial | Missed |
|---|---|---|---|---|
| Contributions (C1–C6) | 6 | 6 | 0 | 0 |
| Highlights (H1–H5) | 5 | 4 | 1 (H3) | 0 |
| Abstract claims (AB1–AB7) | 7 | 6 | 0 | 1 (AB4) |
| Conclusions (CO1–CO26) | 26 | 24 | 2 (CO17, CO23) | 0 |
| Figures (F1) | 1 | 0 | 0 | 1 (F1) |
| Tables (T1) | 1 | 1 | 0 | 0 |
| **Total** | **46** | **41** | **3** | **2** |

**Where each item was caught.**

- **Contributions.**
  - C1: step 0 C5, step 17.
  - C2: C10.
  - C3: C15–C17.
  - C4: C18, C23, C24.
  - C5: step 5 C27.
  - C6: steps 22–23.
- **Highlights.** Highlights and abstract share one step (step 0), and highlights are merged with the matching abstract sentences.
  - H1: C2.
  - H2: C3, recorded verbatim.
  - H4: C5.
  - H5: C5, with C97.
- **Conclusions.** All 26 are caught.
  - §1 and §3: CO1 at C14; CO2 at C31–C34; CO3 at C35–C36; CO4 at C37, keeping "systematic disregard"; CO5 at C38; CO6 at C39–C42.
  - §4: CO7 at C43; CO8 at C66–C67; CO9 at C69. The subsection conclusions CO22–CO26 fall at steps 11–15, each with its trade-offs, scalability limits and examples.
  - §5: CO10 at C70; CO11 at C73–C74; CO12 at C75–C77; CO13 at C78–C80; CO14 at C81 and C83; CO15 at C84–C86; CO16 at C87–C90.
  - §6: CO17 at step 22; CO18 at C97–C100; CO19 at C101–C102; CO20 at C103; CO21 at C104–C105.
- **Table.** T1 is read with what it shows, at step 5 S0–S2: all six rows, their WUE and per-MW values, example facilities and trade-offs, and footnotes a, b and c attached to the right rows.

**What is missed or partial:**

- **F1, the graphical abstract (missed).** It is not mentioned anywhere in the reading: not in `reading_plan`, step 0, or any move or meaning.
- **AB4 (missed).** The abstract's own sentence, "Many data centers are located in water-stressed regions," isn't recorded. Step 0 records the highlight version instead (C3: "Two-thirds of post-2022 data centers…"). That is a different, more specific claim, so the abstract's sentence is lost rather than merged.
- **H3 (partial).** "Technical solutions exist but deployment remains limited **by policy gaps**." C4 records the abstract's version, "deployment remains limited", without the highlight's stated cause.
- **CO17 (partial).** Four of the five research priorities are recorded as claims (C91–C96). The fifth, ecological impact monitoring, appears only in the step's `meaning`. The author's framing, that the priorities "remain major bottlenecks", isn't recorded.
- **CO23 (partial).** §4.2 is covered in full, but the curtailment risk is recorded at claim level with its scope widened (see C50 under A3). The support item restores the restriction.

Smaller gaps: CO18's concrete mechanisms are noted only in step 23's `meaning` (they are recorded as claims at C77). The §5.1 phrase "especially when training runs consume hundreds of thousands of liters in water-stressed regions for limited social benefit" isn't recorded.

---

## A3. Strength of language — **1**

The author's certainty mostly survives, and often with care. The shifts that do occur are small and go in both directions, so this is an inconsistent pattern rather than a systematic one. It sits at the strong end of 1.

**Kept:**
- "Projections suggest… could" (C2).
- The conditional "If this increase in AI use continues" (C8 S1: "Conditional on continued growth").
- "suggesting economic or operational constraints" for Natick; the meaning explicitly flags this as the author's inference (C53).
- "is expected to supply" for the planned Espoo region (C62 S1).
- "potentially shifting rather than eliminating" for SMRs (C69).
- "may not reduce on-site water consumption" (C64).
- Strong wording kept as strong: "systematic disregard" (C37), "remain inadequate" (C84), "severely limited" (C88), "irreversibly deepens" (C105), "not merely voluntary corporate commitments" (C80).

**Shifted — stronger than the article:**
- **C49:** the hedge "may have low consumptive water use" is dropped (A1 above).
- **C50:** the claim reads "Natural-water-body cooling can expose data centers to forced curtailment…". The article confines this risk to "Data centers employing **once-through or open-loop** cooling from natural water bodies" (§4.2, p. 4), and it described its own examples as closed-loop. The support item restores the restriction, but the claim field widens the scope.
- **C23:** adds a causal "because": most cited figures reflect withdrawals *because* reporting conflates withdrawal and consumption. The article joins the two with "and" (§2, p. 2).
- **C40:** moves the modal. The article says concessions "are granted… based on availability assessments that **may not** reflect current hydrological conditions". The run gives concessions that "**may** rest on availability assessments that **do not** reflect current hydrology". The run also drops "in Mexico, as in many jurisdictions".

**Shifted — weaker than the article:**
- **C28:** "accelerating sharply" becomes "accelerating" (A1 above).
- **C60:** water "priced **far** below its scarcity value in most jurisdictions" becomes "generally priced below scarcity value".
- **C77:** "**mandatory** water impact assessments for training runs exceeding defined computational thresholds" becomes "water-impact assessments for training above computational thresholds". The EIA analogy is also dropped.

These are 7 shifts among 109 claims. None is large, but they show that conditions and qualifiers do not survive everywhere the article attached them.

---

## A4. Mechanical checks

**Verbatim texts: 16 pass, 1 fail (of 17).** All 17 are claims; no support item is marked verbatim.
- 12 matched the extracted text automatically. Four more (C2, C6, C101, C103) failed the automatic match only because of column interleaving or page breaks. Checked by eye against the raw extraction, all four are exact.
- **Fail: C71.** "Digital water sobriety challenges the assumption that AI expansion should proceed without considering water constraints." The article reads "Digital water sobriety**, analogous to frameworks in climate and energy policy,** challenges the assumption…" (§5.1, p. 5). The inserted clause is removed with no ellipsis, so the text marked verbatim is not the author's exact wording. Under A1 this would score 0, though it is an unmarked elision, not invented wording.

**Numbers: 101 pass, 0 fail.** Every number string in claim and support texts (101 occurrences) appears in the article's extracted text. Context was checked separately under A1. One small detachment outside the sample: C102 S0 says "approximately 25 million liters", where §6.3 says "25 million liters annually" with no "approximately".

**Reference entries: 64 of 64 citation links resolve to the correct entry in the article's own reference list (44 distinct entries). 0 are invented, 0 are null, and none cites a work missing from the list.** 53 links matched automatically. The other 11 (Shehabi et al. 2024, Google 2025, Alvarez 2024, van Vliet et al. 2012) span columns or pages in the extraction and were confirmed by eye.

**Character-level fidelity is weaker.** The entries carry artifacts from text extraction rather than the text as printed:
- 27 links carry entries with stray, detached diacritics: "Yanez-Barnuevo, M., 2025. Data centers and water consumption. ˜ https…", "Lathuilli`ere", "Deschˆenes", "Holzle, U., 2022. … ¨ https".
- Some URLs are split by spaces at their line breaks ("htt ps://", "goog le-2025").
- Four `citation_text` values carry the same glyph artifacts: "(Yanez-Barnuevo, 2025˜ )", "(Swinhoe, 2023;H¨olzle, 2022)" twice, and "(Holzle, ¨ 2022)". The article prints "(Yañez-Barnuevo, 2025)" and "(Hölzle, 2022)".
- Eight Table 1 `citation_text` values drop the space after the semicolon, e.g. "(Mytton, 2021;Shehabi et al., 2024)".

The right works are identified every time. These are fidelity slips, not invented or completed references.

**Readings of image elements: none to check.** The graphical abstract is the article's only image-based element, and the run does not read it (A2). Table 1 is printed as text, so its values were checked with the numbers above. All Table 1 readings are correctly marked `paraphrased` and name the table.

---

## A5. Detail and readability

**Steps.** 26 steps over a 7-page article (about 6 pages of main text), roughly 200–350 words of article per step. That is within the prompt's 200–500 range and suits how densely the article reads. Coverage is even:

| Article part | Steps |
|---|---|
| Highlights and abstract | 1 |
| §1 | 2 |
| §2 | 2 |
| §3, with the WUE definition and Table 1 | 4 |
| §3.2 | 2 |
| §4 (one per subsection, plus the synthesis) | 6 |
| §5 | 5 |
| §6 | 3 |
| Back matter | 1 |

No section is padded, and none is compressed into one oversized step. Restatements are noted as moves rather than recorded again, as the prompt asks:
- Step 20 notes that the reclaimed-water and Microsoft percentages recur.
- Step 23 notes that the §5.1 mechanisms are repeated.
- Step 24 notes that Luleå and Colón are reused.

**Claims and the run's own reading are kept apart.** The `meaning` fields are substantive and do real work. They track the withdrawal/consumption distinction through the Google example (step 6), the collection-versus-rejection distinction in liquid cooling (step 8), and the reading of "systematic disregard" as the author's interpretation over the cited percentages (step 9). They also catch the shift in §6.2 from water-conscious siting to restricting construction (step 23). The run's own reading stays in `moves` and `meaning`; claim fields hold the author's claims, apart from the small inferences listed under A3.

**Can a reader follow the argument from the reading alone?** Yes. The arc is clear: invisibility, then magnitude, then AI's distinctiveness, then scope and metrics, then local concentration and institutional failure, then technical options and their trade-offs, then governance, then resource justice.

**Weaknesses in presentation:**
- Highlights and abstract share one step without being told apart. That is where H3's cause and AB4 were lost.
- Step 3's location says the method passage continues "printed after the Section 3 heading". In the article, §2's method paragraph continues at the top of p. 2's right column, before §3 begins. This describes the run's prepared input, not the article. Its `reading_plan` says it worked from a "prepared text" with a "retained image" of Table 1, and the label "gap T1" leaks from that preparation into step 5.
- The graphical abstract is absent.

---

## Summary

Run A is a faithful, well-paced and very complete close reading:
- 93% of sampled claims score 2, and none scores 0.
- Every number traces to the article.
- Every citation points to the right entry in the article's own reference list.
- Every contribution, every section conclusion and Table 1 are covered.
- Its `meaning` fields are a real strength: they follow the article's own distinctions (withdrawal versus consumption, on-site versus lifecycle water, inference versus report) and keep the run's reading clearly apart from the author's claims.

Its weaknesses are small but real:
- **Strength of language shifts in both directions.** About seven claims (two of them in the sample) lose a hedge, an intensifier or a scope condition. The most consequential is C50, which widens the curtailment risk from once-through and open-loop systems to natural-water-body cooling in general.
- **One verbatim claim (C71) has an unmarked elision.**
- **Citations reproduce extraction artifacts** rather than the text as printed.
- **Three things on the reference list are missed:** the graphical abstract, the abstract's own "many data centers" sentence, and the highlight's attribution of limited deployment to policy gaps.
