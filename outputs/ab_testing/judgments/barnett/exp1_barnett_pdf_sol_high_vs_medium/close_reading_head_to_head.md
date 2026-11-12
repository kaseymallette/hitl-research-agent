# Close readings, head to head — runs A and B

**Article:** Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866.

**ids:** A `bee567c1-d264-4806-a1f7-40a5bb43e01c` · B `b52aa04e-d9f7-4e11-8e78-fbab1dd1da59`

**Read for this session:** `RUBRIC.md`, `prompts/close-reading.md`, `article.pdf` (text extracted with Ghostscript `txtwrite`; this extraction interleaves the two columns, so passages were located by reading, not by string search alone), `judgments/claims_reference.md`, `runs/A/analysis.json`, `runs/B/analysis.json`. I did not open any other judgment or either argument evaluation.

**Scope used:** as the reference list sets it: highlights, graphical abstract, abstract, and main text through §6.3. Both runs also add a final step on the declarations and reference list, which lies outside that scope and isn't counted for or against either run.

---

## Shape of the two readings

| | A | B |
|---|---|---|
| Steps | 25 | 25 |
| Claims | 135 | 117 |
| Support items | 65 | 55 |
| `verbatim` claims | 12 | 13 |
| Where it stops | End of article (declarations + references) | Same |

The two readings break the article into almost identical steps. They differ only in that A puts the WUE definition in the Table 1 step, while B gives Table 1 its own step and starts §3 in the next one. The difference in claim count comes almost entirely from **A splitting compound sentences that B merges**. Examples: the U.S. 2014/2023/84%/2028 figures (A C39–C41, B C36), the four digital-water-sobriety mechanisms (A C99–C102, B C88), the trade-off and scalability paragraphs of §4.1 and §4.4 (A C61–C62 and C76–C80, B C56 and C70–C72), and the two ends of the application spectrum (A C96–C97, B C86). The prompt asks to "keep distinct claims separate," so A's extra claims aren't padding. They follow the instruction, and they make each claim easier to cite on its own. Neither run repeats itself or pads its `meaning` fields.

---

## A1 spot check (both runs, same seed)

The head-to-head doesn't require a full rescore. To compare the two on the same footing, I drew 15 claims from each run with `random.Random(20261024).sample` and scored each against its passage.

- **A** (C5, C16, C20, C23, C41, C45, C46, C50, C79, C87, C89, C103, C129, C132, C135): 15/15 scored 2. Every attached support item also scored 2.
- **B** (C3, C8, C10, C12, C23, C25, C40, C68, C72, C76, C84, C93, C96, C99, C111): 15/15 scored 2. Every attached support item also scored 2. B C23 adds a "because" that links withdrawal-based figures to conflated reporting. The article implies that link with "However, it is noted…", so I let it stand at 2.

The sample doesn't separate the runs. The differences below come from reading both runs in full against the article.

## A4 mechanical checks (both runs)

- **Numbers:** each run uses 62 distinct numbers in its claims and support. All 62 appear in the article's text for both runs. Neither run contains a number that isn't in the article.
- **Verbatim:** A has 12 of 12 exact and B has 13 of 13 exact. Because the column interleaving breaks automated matching, I checked each one against the article by hand. Neither run marks anything `verbatim` that isn't the author's wording.
- **Reference entries:** each run has 54 citation–entry pairs. All match the article's reference list, and the two runs' entries are identical (the only differences are Unicode normalization). Neither run invented or completed a reference. There's one small difference in `citation_text`: **A** records the Walton marker as printed, "(0.066 km³, Walton, 2025)", while **B** shortens it to "Walton, 2025". Both runs make the same small slip on the Stockholm/Espoo item: they put the Stockholm figures (which have no citation in the article) in one support item with the Espoo figures under the Espoo (2022) citation.
- **Image-based element (graphical abstract):** **A** records two `paraphrased` support items that name the graphical abstract (step 1: the three water pathways, and the solutions/policy branches). By eye, both match the image as the reference list describes it. **B** describes the graphical abstract only in its `meaning` field and records no claim or support item for it.

---

## What each caught that the other missed (against `claims_reference.md`)

Both runs catch all six contributions (C1–C6), all seven abstract claims (AB1–AB7), all six Table 1 rows with their footnotes (T1), and every conclusion CO1–CO26 at least in substance. The differences are at the edges:

**Caught by A, missed or only partly caught by B**

- **H3**, "Technical solutions exist but deployment remains limited **by policy gaps**." A C6 records it. B C5 records only the abstract's "deployment remains limited" (AB5), so the highlight's causal attribution to policy gaps is missing from B.
- **F1 (graphical abstract) as recorded content.** A records what it shows as paraphrased support naming the element, which is how the prompt asks image readings to be handled. B mentions it only in `meaning`, so the reading belongs to the run rather than appearing as a record of the source. Count it as caught by A and caught only in passing by B.
- **CO23, curtailment risk compounded by climate change.** A C66 records "a risk compounded by the increasing frequency and intensity of heat waves." B omits it.
- **CO8, carbon in the energy–water trade-off.** A C85 keeps "increases electricity demand and associated carbon emissions." B C77 shortens it to "energy versus water efficiency."
- **C4, the pointer to §6.1.** A C27 keeps that the comprehensive assessment "remains a research priority." B C24 drops it.
- **CO26, shifting water demand.** A C83 keeps "it can shift water demand within the energy system." B C75 keeps only "may not reduce on-site water use."

**Caught by B, missed or only partly caught by A**

- **CO7, first half.** B C52 has "substantial water reductions are technically achievable, but all carry trade-offs…". A C57 records only the trade-off half. The §4 claim that reductions are achievable is missing from A.
- **CO16, "yet transparency remains severely limited."** B C98 keeps it. A records the Virginia bill and the withholding of data (C113–C114) but not the author's verdict that transparency is "severely limited."
- **CO21, "Water-sustainable AI is achievable."** B C115 states it outright. A C133 has it only implicitly, inside the political-will question.
- **CO6 and §4.2 verbatim anchors.** B records "Neither facility has published independent long-term ecological monitoring data despite multi-year operation" (C59) and the C2 scope sentence (C12) verbatim. A records both faithfully as paraphrase. This affects precision, not coverage.

**Missed by both:** the "technical solutions demonstrate that water-efficient AI infrastructure is achievable" half of **CO10** (§5 intro). Both runs (A C90, B C81) record only "technology alone is insufficient."

---

## Where each is wrong that the other isn't

**B only**

- **Scope condition dropped in §4.2 (CO23).** The article limits the curtailment risk to "Data centers employing **once-through or open-loop** cooling from natural water bodies." A C65 keeps this. B C60 widens it to "Natural-water cooling can create operational and financial risk from thermal-discharge limits." The section's own examples are *closed-loop* systems, so B's version applies the risk to the systems the author leaves out of it. This is the most consequential fidelity slip in either reading (A1 = 1, A3).
- **Citation marker shortened** ("Walton, 2025" instead of the printed marker). Minor (A4).

**A only**

- **Added scope in A C10:** "AI-related water consumption is substantial **at both the training and response-generation stages**." The article says only "This consumption is substantial." The stage-by-stage framing is the run's inference from the support figures, placed in the author's claim (A1 = 1). It's small and consistent with the evidence, but it is an addition.
- **Condition dropped in A C11:** the 280 billion L U.S. projection loses the article's "If this increase in AI use continues." A keeps "projected," so the claim stays hedged. B C10 keeps the condition. A1 = 1.
- **Hedge thinned in A C3:** "Projections suggest" is dropped, though "could" survives. B C3 records the full sentence verbatim. Borderline.
- **A C92 support slightly misdescribes the link:** it says the author "relates this awareness gap to training runs consuming hundreds of thousands of liters." In the article, the training-run clause qualifies the *evaluation* dimension, and the awareness statistic is the reason that evaluation is urgent. This is a minor misreading of how the parts connect.

On **A3** neither run is systematically shifted. A has three small hedge or scope slips, each mild, and none changes what a claim applies to. B has one slip that does widen what a claim covers. I'd put both at the high end of A3 = 1 or the low end of 2. The single scope change in B weighs a little more than A's three mild slips.

---

## Verdict

**Run A is better, narrowly.**

- **A1 / A3:** the sampled claims tie (15/15 at 2 for both). In full, B's one scope change (once-through/open-loop) is a more consequential error than A's minor hedge drops and its one added "both stages" scope.
- **A2:** close to even. A catches H3 and records F1 properly, and keeps several qualifiers B leaves out (climate compounding, carbon, the §6.1 pointer). B catches the "technically achievable" half of CO7, "transparency remains severely limited," and the explicit "achievable" in the closing. On counted items (highlights, figures), A comes out a little ahead.
- **A4:** both are clean: no invented or mismatched references, no false verbatim, no number missing from the article. A follows the prompt's instruction on image content (record it as paraphrased content that names the element), while B leaves the graphical abstract in `meaning`. A also records the Walton marker exactly as printed.
- **A5:** the steps are the same. A's extra 18 claims come from following "keep distinct claims separate," not from repetition. B is more compact, but its merged claims bundle separate figures and proposals into single items that are harder to cite.

The margin is small. Both readings are faithful, complete, and mechanically clean, and either would serve the larger collection. A's edge comes from following the prompt's own rules more closely (image readings recorded, distinct claims kept separate, markers as printed) and from not making a scope error like B's §4.2 slip.

## Order check

- **A first, then B:** A's handling of the graphical abstract, its kept once-through/open-loop condition, and its finer claim separation set the baseline. Read against that, B's merged claims and its widened §4.2 risk stand out, while B's gains (the CO7 first half, "severely limited," the verbatim hedges) are real but smaller. **Verdict: A, narrowly.**
- **B first, then A:** B reads as tighter and more careful with hedges: the verbatim "Projections suggest…", the kept conditional on the U.S. projection. Read against B, A's "both stages" addition and its missing CO7 first half stand out. But A's recorded graphical abstract, H3, and kept §4.2 scope condition still outweigh those once both are weighed on the criteria. **Verdict: A, narrowly.**

**The verdict held in both orders: A, by a narrow margin.**
