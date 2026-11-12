# Judgment — argument evaluation

**Article:** `article.pdf` — Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866 ("Making Waves"), 7 pages.

**Judged:** `run/argument_evaluation.md` (about 1,250 words), against the article alone, on B1–B6.

**How the article was read:** as text pulled from the PDF with macOS PDFKit. Page images could not be rendered in this environment. The text of Table 1 and its footnotes came through and was checked. The graphical abstract is an image, so its content was **not** checked, and the evaluation's claim that the graphical abstract "announce[s] the policy program" is unverified. Section numbers below are the article's own.

---

## B1. Premise acceptability — **2** (at the low edge)

The evaluation weighs the evidence behind most of the central conclusions and names the passages:

- **The two-thirds statistic (§3.2).** It is a count of sites "built or planned" and "is not a measure of the water they consume or the pressure they add at the driest time of year." The article gives no consumption figures for these sites, so this holds.
- **Colón (§3.2).** It is a single account ("In the account cited by the paper") that shows a juxtaposition. It does not show how much the campus contributed to reservoir depletion.
- **Luleå (Table 1, footnote a).** The per-MW value is an estimate, the facility's IT capacity is undisclosed, and the volume is a withdrawal.
- **Heat recovery (§4.5).** The examples show feasibility but not water savings.
- **The opening figures (§1).** These are conditional estimates for different populations.

Gaps keep this from a clear 2:

- **Provenance is barely weighed.** §2 says peer-reviewed sources were prioritized. Yet the local-impact case rests on journalism and press sources: Bloomberg for the two-thirds figure, the Guardian (Barratt et al.) for the Microsoft and Google shares, the Texas Tribune, and In These Times for Colón. The headline projection is from an arXiv preprint (Li et al.). The evaluation says §2 "gives little basis for judging how representative the cases are" but does not take up this mismatch.
- **The economic premise goes unexamined.** The market-failure argument (§4.4, §5.1) carries the paper's step from "technology exists" to "policy reform is required." It rests on two figures with no citation: electricity is "typically 40–60% of total operating expenses," and dry cooling costs about "10–25%" more electricity. The evaluation never weighs either.
- **"Limited deployment" is not tested.** §5 says limited deployment shows "technology alone is insufficient," but the article never measures how limited deployment is. The evaluation does not ask.

## B2. Relevance of critique — **1**

Most criticisms attach to the claim as stated, and the qualifiers are kept. It catches that the body says "built or planned" where the highlights drop it. It credits the author for proposing "a spectrum rather than a ban," and it quotes "systematic disregard" accurately. Three criticisms aim at a claim somewhat broader than the one made:

- **Digital water sobriety (§5.1, §6.2).** The closing judgment says the paper offers too little evidence "to make those judgments the basis of a general permitting regime." The article proposes "tiered governance linking AI deployment decisions to demonstrated societal benefit." Its concrete mechanisms, though, are scarcity-adjusted pricing, impact assessments above compute thresholds, facility water budgets, and preferential permitting for *water-efficient technology*. None of them is benefit-based permitting. The "narrower response" the evaluation offers instead is: "enforceable limits on facility use according to local availability" and "require major projects to disclose and assess their impacts." That largely restates the article's own facility budgets "tied to real-time watershed conditions" and its "mandatory water impact assessments." The evaluation does not acknowledge this.
- **Disclosure (§6.2).** The evaluation argues that an annual WUE ratio is not enough and that watershed managers need volumes by season, with off-site electricity impacts. But §6.2 already proposes "extending WUE reporting requirements to include on-site consumption, embedded water in electricity supply, and temporal variation." §6.1 asks for protocols on "temporal resolution, and geographic granularity." The refinement that survives is narrower: absolute volumes by source, with withdrawal and consumption kept separate.
- **"Uniform siting restriction."** §6.2 restricts construction in "severely-stressed watersheds," not everywhere. The real point survives: the threshold is undefined, and the rule targets construction rather than consumption. "Uniform" overstates it.

None of these is a straw man. The main criticisms (the dropped qualifiers, Colón's limits, Luleå, heat recovery) all attach correctly.

## B3. Sufficiency — **2**

This is the evaluation's strongest criterion. It repeatedly separates what the evidence permits from what it requires, and it says what would be needed:

- **Systematic disregard.** "I would need to see the feasible alternative sites and how water figured in the choices."
- **Colón.** It "supports asking what happens to permits when supply contracts… It does not establish how widespread the same failure is."
- **Luleå.** "The disclosed volume alone cannot establish comparative consumption for equivalent computing service."
- **Heat recovery.** Water savings depend on "which heat source it actually displaces… and whether demand coincides with supply."
- **Siting.** The paper "does not establish when that threshold is met."
- **Digital water sobriety.** "The evidence permits a narrower response." It names what is missing: attribution, who judges benefit, and against what alternative.
- **Overall.** A "strong case" for local availability and drought priorities, and a "plausible case for testing" value judgments.

One gap: the evaluation does not ask whether the headline "technology alone is insufficient" (§5) follows from §4. It says only that the engineering survey "does the most to earn the move toward public oversight," and its reason (costs shift between domains) is its own, not the author's.

## B4. Unstated warrants and missing qualifiers — **2**

**Missing qualifiers it catches, with reasons they matter:**

- The highlights drop "or planned" and "suggests" from the Bloomberg figure. (§5.1 repeats the unqualified version; the evaluation doesn't mention that.)
- §6.2 drops §4.5's hedges ("may yield indirect water savings," "may not reduce on-site water consumption," "lifecycle analysis is needed," "most examples are pilot-scale").
- The bottle figure is presented as "a property of the response itself."

**Unstated warrants it catches:**

- A site count is taken to stand for water pressure.
- Siting in water-stressed regions is taken as evidence of "disregard" rather than a trade-off that was weighed.
- A withdrawal figure without a known capacity is taken to support "suffices for hyperscale operations" (§6.3).
- Someone is assumed to be able to judge "demonstrated societal benefit," and water is assumed attributable to workloads, which §6.1 concedes it is not.

**What it misses:**

- **The scalability warrant behind "not technological necessity."** §5.1 and §6.3 conclude that AI's water footprint reflects "policy and siting choices, not technological necessity." That needs the unstated premise that the showcase solutions generalize. §4 argues the opposite at every turn: Nordic sites are "geographically limited," subsea has "high capital costs… limited suitable sites" and Natick was discontinued, dry cooling "degrades in hot/dry climates," and heat recovery is "pilot-scale." The evaluation's "they cannot rank the options" gestures at this but never names the tension.

## B5. Self-attribution — **2**

The judgments are plainly the evaluation's own ("I would read…", "a premise I share", "I would need to see"). It states its own bias and how that bias could mislead: "my own preference for rules that can be measured and audited… can hide unfairness." It names the author's setting (engineering and sustainability affiliations, a water journal), and both affiliations check out on page 1. Nothing it concludes is put in the author's mouth. Its own reasoning ("Later sections show why that intuition misleads") is framed as inference from the author's material, not as the author's claim. One unacknowledged point, which does not lower the score: the author's stake through self-citation (Tsoury and Barnett-Itzhaki 2025; Barnett-Itzhaki and Tsoury 2025) isn't mentioned.

## B6. Correctness

### Problems raised: 13 in total — 11 confirmed, 2 partly confirmed, 0 not confirmed, 0 wrong

| # | Problem raised | Verdict | Passage |
|---|---|---|---|
| 1 | Opening figures mix populations and scales; the bottle estimate reads as unconditional | Confirmed | §1: "generating 10–50 medium-length responses consumes the equivalent of a 500 ml water bottle." No location or cooling conditions are given, though §3.1 says "similar AI workloads can translate into vastly different local water burdens." |
| 2 | §3 compares U.S. consumption with global withdrawals, mixing accounting and geographic boundaries | Confirmed | §3: "approximately 4000 km³ of freshwater are withdrawn… U.S. data center estimated annual water consumption of 66 billion liters… represents a small fraction." §2 itself draws the withdrawal/consumption distinction. The author concedes the point ("aggregate comparisons understate the problem"), so the error doesn't harm the author's case, which the evaluation also recognizes. |
| 3 | Highlights drop "or planned" from the two-thirds figure | Confirmed | Highlights: "Two-thirds of post-2022 data centers are located in water-stressed regions." §3.2: "A Bloomberg analysis suggests about two-thirds of data centers built or planned since 2022…" |
| 4 | A site count doesn't measure water consumed or seasonal pressure | Confirmed | §3.2 gives no consumption data for these sites. |
| 5 | "Systematic disregard" isn't separated from a trade-off that was considered | Confirmed, with a caveat | §3.2: "reveals systematic disregard for water availability constraints." Caveat: §5.1 offers an asserted mechanism (water "does not register as a material financial risk") that the evaluation doesn't engage. It is uncited, so the point stands. |
| 6 | Colón doesn't show the campus's contribution, how widespread the failure is, or that cheap water decided the siting | Confirmed | §3.2 gives no volumes. "This institutional rigidity is not unique to Mexico" is uncited. §6.3's "siting decisions prioritizing electricity costs" is not documented in §3.2. |
| 7 | The §4 examples can't rank options on a common basis | Confirmed | Each subsection lists trade-offs in different terms. The author concedes this in §4 ("No single siting or technology choice resolves all three tensions"), which the evaluation doesn't credit. |
| 8 | Luleå's per-MW figure is approximate and a withdrawal, so it can't show comparative consumption; the conclusion overreaches | Confirmed | Table 1, footnote a ("facility-specific IT capacity not publicly disclosed, so per-MW values are approximate"); §6.3: "Meta's Luleå facility demonstrates 25 million liters annually suffices for hyperscale operations." |
| 9 | §6.2 recommends heat-recovery incentives more confidently than §4.5 supports | Confirmed | §4.5: "may yield indirect water savings," "It may not reduce on-site water consumption," "lifecycle analysis is needed," "most examples are pilot-scale." §6.2: incentives "would accelerate deployment… delivering co-benefits across energy, climate, and water domains." |
| 10 | An annual WUE ratio isn't enough for watershed managers | Partly confirmed | §6.2 already extends WUE reporting to "on-site consumption, embedded water in electricity supply, and temporal variation." What survives is the call for absolute volumes by source, with withdrawal and consumption separated. |
| 11 | The siting restriction's threshold is undefined, and it doesn't distinguish proposals that use little freshwater | Confirmed, with a caveat | §6.2: "Restrict new construction in severely-stressed watersheds." "Severely" is undefined, and the rule targets construction, not consumption. Caveat: "uniform" overstates it, and §5.1 and §6.2 separately propose preferential permitting for water-efficient technology. |
| 12 | The contrast between medical and recreational uses makes the call too easy; there is no method of attribution; who judges benefit is unspecified | Confirmed | §5.1's spectrum. §6.1: "without attributing water costs to specific models, training runs." The article names no judge or procedure for "demonstrated societal benefit." |
| 13 | Too little evidence for benefit judgments as the basis of a general permitting regime; a narrower response suffices | Partly confirmed | §6.2: "tiered governance linking AI deployment decisions to demonstrated societal benefit." The article does propose linking deployment to benefit without evidence of feasibility. But the "narrower response" largely restates the article's own mechanisms (§5.1: "facility-level water budgets tied to real-time watershed conditions," "mandatory water impact assessments"). |

Not counted as a problem: the §5.2 point on replenishment pledges. There the evaluation endorses the author's own argument ("temporal and spatial mismatch") and adds that a credible local project could still help.

### Errors: no substantive misstatements; 3 minor imprecisions

1. **§2 is softened.** The evaluation says §2 "acknowledges that many cited figures are withdrawals." The article says "most figures cited in this review reflect total withdrawals unless otherwise specified."
2. **"Perspective" is the evaluation's label.** The article carries the "Making Waves" header but calls itself "a targeted review" and "this review" (§2). This is a reasonable characterization, not an error.
3. **Scope slightly enlarged.** "Uniform siting restriction" and "general permitting regime" are scored under B2 rather than counted again here.

All the numbers and passages it cites check against the text, apart from the graphical abstract, which wasn't verified:

- 4.2–6.6 billion m³ by 2027
- the bottle estimate for 10–50 responses
- "built or planned since 2022"
- Colón's trucked and bottled water while industrial allocations continued
- Table 1, footnote a
- §6.1 on attribution
- the WUE definition (annual site water divided by annual IT energy)
- the author's affiliations

### Problems in the article the evaluation doesn't raise (my own reading, not scored)

- **Arithmetic in §3.** "Roughly, two liters… per kWh… with significant fractions lost to evaporation. Consequently, even a modest one MW data center… consumes approximately 25,500 cubic meters annually through evaporative losses alone." At 2 L/kWh, 1 MW running all year gives about 17,500 m³ even if *all* of it evaporated. 25,500 m³ implies about 2.9 L/kWh, all evaporated. Table 1 repeats the 25,500 figure.
- **Unreconciled U.S. projections.** §1 says U.S. data centers will use "up to 280 billion liters per year by 2028." §3 says hyperscale facilities will use "between 60 and 124 billion liters" in 2028, after accounting for 84% (with colocation) in 2023. The article doesn't say how these relate.
- **The scalability tension (see B4).** "Not technological necessity" (§5.1, §6.3) against the scalability constraints in §4.
- **Uncited economic figures (see B1).** The opex share and the dry-cooling energy penalty carry the market-failure argument.
- **A non sequitur in §5.1.** It calls the evaluation of applications "urgent given that 73% of UK respondents were unfamiliar with 'digital pollution'," citing the author's own survey. Public unfamiliarity doesn't bear on whether particular workloads justify their water.
- **A citation that looks mismatched.** §5.3 supports "disclosure of facility locations, cooling configurations, and electricity sources… remain missing" with Jain (2025). Going by its reference entry, that is an IEEE Spectrum article on AI in chip verification.

---

## Summary for the researcher

This evaluation is selective, well sourced to section and table, and unusually disciplined about sufficiency. Its best work:

- It catches the highlights dropping "or planned."
- It shows that §6.2's heat-recovery recommendation drops §4.5's hedges.
- It shows that §6.3's Luleå claim rests on an approximate withdrawal figure the article's own footnote qualifies.
- It separates what the Colón case does establish (drought priorities are a fair question) from what it doesn't (prevalence, causation).

It makes no factual errors about the article. All 13 problems it raises are borne out at least in part. Its self-attribution is clear, and it states its own bias toward rules that can be audited.

The weaknesses:

- **The digital-water-sobriety critique is aimed somewhat wide.** The alternative it recommends is largely the article's own list of mechanisms.
- **The disclosure point overlooks what §6.2 already proposes.**
- **The paper's central economic premise goes unexamined.** The market-failure argument rests on uncited opex and energy-penalty figures, and the evaluation never weighs them. Nor does it weigh the journalism-heavy sourcing behind the local-impact claims.
- **It misses the scalability tension.** The tension between "not technological necessity" and §4's scalability limits is the most consequential unstated warrant in the paper, and it is left unnamed.

None of these undermines its conclusions, but a reader should not treat its endorsement of the local-allocation argument as having tested the economic premise.
