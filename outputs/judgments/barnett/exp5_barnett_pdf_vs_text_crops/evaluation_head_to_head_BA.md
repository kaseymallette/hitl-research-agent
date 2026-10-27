# Argument evaluations, head to head: run A vs run B

**Article:** Barnett-Itzhaki (2026), "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299, 125866.

**Files compared**
- Run A: `runs/A/argument_evaluation.json`, `id` **77671eb8-5439-4e76-9125-78ebd96dba09**
- Run B: `runs/B/argument_evaluation.json`, `id` **b35af235-25d9-4f75-897a-3a2b33ac6625**

**Read for this session:** `RUBRIC.md`, `prompts/evaluate-argument.md`, `article.pdf` (all 7 pages, as page images and text), `references/problems_reference.md`, and the two evaluations. No other judgment and no close reading was opened.

**Shape of the two runs.** The two are close in length (about 1,450 words for A and 1,600 for B) and in structure. Each places the piece as a "Making Waves" agenda-setting article, credits the move from global totals to watershed-level assessment, faults the step from location data to "systematic disregard", questions the Colón attribution, the Luleå "suffices for hyperscale" claim and the "not technological necessity" conclusion, and criticises the application ranking as intuitive categories rather than a decision procedure. The differences lie in what each adds beyond that shared core.

---

## 1. What each caught that the other missed

A problem counts as found when the run identifies the same defect in the same passage, as the reference list's "How to use" note defines it. "Partial" means the run names the passage and part of the defect.

### Found by both (with differences in depth)

| Problem | Run A | Run B |
| --- | --- | --- |
| **P1** "not technological necessity" vs §4 constraints (Major) | Found. "The preceding sections show that both matter… establishes possibility, not universal substitutability." | Found. Closing: "the article's own survey shows that physical constraints, uncertain impacts, and unresolved trade-offs remain part of the problem." |
| **P2** Luleå/subsea → hyperscale (Major) | Partial: IT capacity undisclosed, so no denominator. | Partial, fuller: also calls it the "absolute **withdrawal** figure" and says it shows "reported operation under particular conditions". Neither run uses the subsea "400–800 servers" point. |
| **P3** deployment "limited by policy gaps" (Major) | Partial: "Nor does the existence of limited deployment establish how much additional deployment regulation could reasonably achieve." | Found: "It does not establish… that policy gaps principally explain limited adoption." |
| **P31** descriptive premises → normative ranking of applications (Major) | Found: "a proposal worth debating, not a conclusion established by the review", plus missing workload-level accounting (P31.4). | Found, sharper. It separates "constraining environmental harm" (which "follows substantially from the evidence") from "ranking the purposes", which "requires additional normative and administrative justification" (P31.1). It notes that pricing, budgets and cumulative-impact rules can work "without officials classifying every application" (close to P31.3), and that shared models complicate attribution (P31.4, partial). |
| **P6** location read as "systematic disregard" (Major) | Found: location ≠ disregard; a dry-cooled facility in a stressed region could use less water. Also mentions "confident diagnoses of market failure". | Found, fuller: names the missing "relevant geographic baseline" (the base-rate point) and the planned/operating distinction. |
| **P14** headline 4.2–6.6 bn m³ projection (Major) | Partial: assumptions not unpacked and comparability with the cooling figures not shown. | Partial: "without explaining enough of the underlying scenario". Neither run does the arithmetic against the U.S. figures (64–100×). |
| **P15** withdrawal vs consumption conflated (Major) | Found, in general terms. | Found, in general terms ("A methodological caveat cannot fully repair a narrative…"). Neither names the §3 consumption-vs-global-withdrawal comparison. |
| **P7** Colón generalized (Moderate) | Found: the case gives no quantified contribution and no counterfactual. | Found, the same, plus the institutional citation (see P24). |
| **P27** value ranking without criteria (Moderate) | Found. | Found. |
| **P28** reform shown to be "required" (Moderate) | Partial: political will is not shown to be "the decisive remaining obstacle". | Partial: does not show "application-level rationing is the necessary remedy", or that the remaining obstacle is "chiefly political will". |
| **P32** policies ignore §4 trade-offs (Moderate) | Partial: low-WUE permitting could reward burden-shifting to electricity. | Found: the same point, plus "The article's own integrated-assessment principle should govern its recommendations", which is the reference list's exact defect. |
| **P5** heat-recovery recommendation overconfident (Moderate) | Partial: "need demonstrated system benefits". | Found: ties the recommendation to §4.5's own admission that recovery "may not reduce on-site consumption". |
| **P34** demands unconnected to policy evidence (Moderate) | Partial: "who evaluates benefit… how decisions are challenged"; "comparative cost and implementation evidence". | Partial: "regulation—also needs scrutiny regarding implementation, enforcement, and actual hydrological outcomes." Neither uses §4.4's dry-cooling mandate precedent or the unanswered "cautionary precedent" in §5.1. |

### Caught by A only

- **P13, the 25,500 m³ arithmetic (Major, numerical).** A works it out: 8.76 million kWh × 2 L/kWh = 17,520 m³, and 25,500 m³ implies about 2.9 L/kWh. This is the reference list's calculation exactly. It is the only numerical check in either run.
- **P21, data-centre figures standing in for AI (Major).** "Evidence about data centers generally cannot isolate AI's incremental burden when the paper itself identifies AI-specific attribution as an unresolved research problem." B only gestures at this when it lists "all-data-center statistics" among figures that aren't comparable. It never says that the article's AI conclusions rest on non-AI data.
- **P8, urgency from unfamiliarity with a term (Moderate).** "Unfamiliarity with 'digital pollution' does not independently establish urgency." A also notes that the studies are self-cited.
- **P9, training-run assessments need accounting that doesn't exist (Moderate).** A notes that "the necessary workload-level accounting does not yet exist", linked to the §6.1 admission.
- **Found by A and not on the list, confirmed against the article:** the proposed assessments apply to "training runs exceeding defined computational thresholds" (§5.1) and "large-scale training" (§6.2). A observes that this would miss aggregate inference demand and invites splitting training below the threshold. The article's mechanisms are indeed scoped to training only, so the criticism is accurate and attaches to the proposal as stated.

### Caught by B only

- **P23, method underspecified and evidence mix (Moderate).** "No reproducible selection procedure or explicit quality assessment", and a differentiated treatment of journalism, corporate sources and vendor sources.
- **P24, citation fit (Moderate), two of its four items.** Jain (2025) is titled as an article on AI chip verification, and the Corral-Bermudez aquifer study "concerns another Mexican basin". Both match the article's own reference list.
- **P16, Table 1's free-air values can't be derived (Moderate).** "Table 1 offers normalized annual use and WUE estimates while acknowledging that the facility's IT capacity is undisclosed… readers cannot reproduce the comparison."
- **P29, corporate pledges dismissed by assertion (Minor).** "The mismatch is a valid test that such initiatives must pass, not proof that every initiative fails it."
- **P18, the water-stress statistic hardens (Moderate), partial.** B notes that "planned and operating facilities also represent different levels of realized demand", which is the "or planned" component. It does not trace the hedge being dropped across the highlights and §5.1.

### Missed by both

P4 (abstract vs §4.5 on heat recovery), P10 (water governance's "structural advantages" contradicted), P11 ("shown" governance frameworks), P12 ("qualitatively different"), P14's arithmetic, P17, P19, P20, P22 ("most substantial" portion), P25 (uncited quantitative claims), P26, P30 and P33.

---

## 2. Where each is wrong that the other isn't

I checked every factual statement in both runs about the article's text, numbers and citations against the PDF. **Neither run makes an error under B6:** no misread number, no misdescribed passage, and no quotation that isn't in the article. A's arithmetic is correct. B's two citation-fit claims are correct by the article's own reference list.

Smaller slips, each touching B2 (relevance of critique):

- **A:** "It does not establish that political will is the decisive remaining obstacle **in every setting**." The article's claim is general ("results from deliberate policy and design choices, not technological necessity", §5.1), so the added "every setting" is a fair reading rather than a straw man. I record it only as a slight widening of the claim.
- **B:** It describes the framework as "application-level **rationing**" and as "ranking the purposes for which resources **may be used**", and imagines "officials classifying every application". The article explicitly "does not propose binary approval or prohibition" and advocates "a graduated governance approach linking resource costs to demonstrated societal benefit" (§5.1). B's wording leans a little toward the stronger claim the reference list's P31 scope note warns about. B elsewhere engages the graduated version correctly ("require demonstrable benefits for any exceptional allocation"), so this is a wording drift, not a misdirected main criticism. A handles this point more carefully: "Its graduated approach is more plausible than binary prohibition."

On balance B has the slightly larger B2 slip, but both runs stay at or near the top of the scale.

---

## 3. Grounds on B1–B6

- **B1, premise acceptability.** **B is stronger.** B weighs the provenance of the evidence: the review method, journalism against vendor and corporate sources, two citations that don't fit, and the non-derivable Table 1 values. A weighs the evidence behind the location, Colón and Luleå claims, and checks one calculation. It never asks where the evidence comes from or how good it is, apart from noting that the awareness studies are self-cited.
- **B2, relevance.** **Roughly even.** A is slightly cleaner on the graduated framework.
- **B3, sufficiency.** **Even.** Both state what each central conclusion would need. A asks for consumption, water sources, seasonal operation, permit conditions, and comparative cost and implementation evidence. B adds a geographic baseline, project-level evaluation of replenishment, and a counterfactual allocation at Colón.
- **B4, unstated warrants.** **Split.** A catches the warrant that data-centre water is AI water (P21), a Major one. B pins down the warrant between the descriptive evidence and the normative ranking more precisely (P31.1, P31.3), and catches the unapplied integrated-assessment principle (P32).
- **B5, self-attribution.** **Even, both strong.** Each states its own preference for measurable, administrable rules and says how that might underweight the author's point about allocation. A explicitly endorses the ethical premise as its own view. B separates the author's affiliations from any improper stake and notes the declared absence of competing interests.
- **B6, correctness.**
  - **Neither run makes an error.**
  - **A has two Major findings unique to it:** P13 and P21.
  - **B covers more of the list overall:** about 19 problems against about 17, counting partials. Its unique finds are all Moderate or Minor (P23, P24, P16, P29, P18 in part).
  - **On Major problems both found, B is fuller:** it adds the withdrawal point to P2, the base rate to P6, and the descriptive-to-normative bridge to P31, and it states P3 directly.

---

## 4. Verdict

**Run B is better, narrowly.**

**For B:**
- It is clearly ahead on B1. It is the only run that asks whether the evidence deserves belief at the level of method and source, and its two citation-fit findings are concrete and correct.
- It treats the article's distinctive contribution, the move from water-use evidence to a ranking of AI applications (P31), with more precision.
- It applies the article's own integrated-assessment principle back to the recommendations (P32, P5). That is a better instance of the prompt's "give the author's preferred solutions the same scrutiny."
- It covers more of the reference list.

**For A:**
- It holds the two most consequential findings that B lacks. The P13 arithmetic is a hard, checkable error in a key scaling claim, and P21 undercuts the article's first central conclusion that AI's footprint is large.
- It is slightly more careful not to overstate the framework.

If a configuration's value lay mainly in catching numerical errors, A would win. On the rubric's criteria taken together, B's advantages on B1 and in the depth of its shared findings outweigh A's two unique Majors, but not by much.

---

## 5. Order check

- **Reading A first, then B.** A's arithmetic check and its data-centre-vs-AI warrant set the bar, and B at first reads as less rigorous about numbers. Reading on, B covers method and sourcing, which A never touches, and its P31 and P32 treatment is tighter. Verdict: **B, narrowly.**
- **Reading B first, then A.** B's sourcing critique and its separation of "harm control" from "ranking purposes" set the bar, and A at first looks thinner on evidence quality. A then contributes P13, P21, P8 and the threshold-gaming point, which narrows the gap without closing it, because B's broader coverage and B1 lead remain. Verdict: **B, narrowly.**

**The verdict held in both orders.** The margin is small in each, and it rests mostly on B1 and on depth of treatment rather than on raw counts. A researcher weighting numerical verification heavily could reasonably read it as close to a tie.
