# Judgment: argument evaluation

**Article:** `article.pdf`. Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866, a "Making Waves" piece, 7 pages including references.

**Judged:** `run/argument_evaluation.md` (about 1,340 words), against the article alone.

**How I read the article:** I extracted the text with macOS PDFKit. Page rendering wasn't available, so I couldn't view the graphical abstract (an image). Table 1 and its footnotes came through as text and were checked.

---

## B1. Premise acceptability: **2**

The evaluation weighs the evidence behind the main conclusions and points to the passages each time:

- **Method and sample.** It notes that §2 names the kinds of sources consulted but gives "little basis for judging how representative the cases are." This holds up: §2 lists three source streams and says peer-reviewed sources were prioritized. It gives no inclusion criteria, no counts and no selection rule for cases.
- **Accounting boundaries.** It sets the withdrawal-versus-consumption caveat in §2 against how the figures are used later (§3, Table 1).
- **The two-thirds siting figure.** It says this counts sites built *or planned*. A site count measures neither water consumed nor added pressure in the dry season.
- **Colón.** The case shows that allocation continued during drought. It doesn't show how much the campus contributed to reservoir depletion.
- **Luleå.** The per-MW value in Table 1 is an estimate (footnote a: IT capacity not disclosed) and is based on withdrawal.
- **Heat recovery (§4.5).** The examples show the heat can be used, not that water is saved.

**Weakness: it says little about where the evidence comes from.** §2 says peer-reviewed work was prioritized, yet several load-bearing premises come from journalism:
- the two-thirds figure (Bloomberg, Nicoletti et al., 2025)
- Colón (In These Times, Alvarez, 2024)
- the Microsoft 42% and Google 15% shares and the Virginia bill (The Guardian, Barratt et al., 2025)

The evaluation hints at this ("the cited analysis," "in the account cited by the paper") but never weighs it. It also leaves alone the premise in §5.1 that the evaluation of applications is urgent "given that 73% of UK respondents were unfamiliar with 'digital pollution.'" That premise rests on the author's own survey, and an awareness gap doesn't bear on whether training runs are worth their water. These gaps keep B1 from being thorough, but the central conclusions are weighed, with passages cited.

## B2. Relevance of critique: **1**

Most criticisms attach to the claim as stated, qualifiers included:
- It credits the author with proposing "a spectrum rather than a ban," citing §5.1: "does not propose binary approval or prohibition."
- It quotes the §6.2 restriction on "severely-stressed watersheds" accurately.
- It sets the hedged §4.5 against the confident §6.2.

Three criticisms aim somewhat off the claim the author made:

1. **The opening numbers.** It says they "cannot carry the allocation argument." The author doesn't use them that way. §3 says itself that "aggregate comparisons understate the problem" and then turns to local budgets. The evaluation partly concedes this ("The better argument survives without it"), so this is a tension, not a straw man.
2. **The WUE ratio.** It says §6.2 "leaves unstated" that a WUE ratio "is not a volume." But §6.2 asks to extend reporting "to include on-site consumption, embedded water in electricity supply, and temporal variation." That reads as adding consumption figures alongside the ratio, not as reporting a ratio only. §5.3 also asks for facility locations, cooling configurations and electricity sources. The criticism targets a narrower proposal than the one in the article.
3. **Tiered governance.** It presents this as "the step §6.2 takes beyond" the concrete mechanisms (water budgets, impact assessments, preferential permitting). In both §5.1 and §6.2, those mechanisms are given *as* the means of carrying out the benefit-linked framework ("Concrete mechanisms include…"). The evaluation also drops "and local water availability" from §6.2's wording. There was a sharper point available, close to what the evaluation implies: none of the listed mechanisms actually measures societal benefit. As written, though, the structure of §6.2 is somewhat misdescribed.

None of these is the main criticism, so this is a 1, not a 0.

## B3. Sufficiency: **2**

The evaluation repeatedly separates evidence that permits a conclusion from evidence that requires it, and often says what would be needed:

- **"Systematic disregard" (§3.2).** It says what would be needed to tell disregard from an accepted trade-off: "the feasible alternative sites and how water figured in the choices."
- **Colón.** It "supports asking what happens to permits when supply contracts" but "does not establish how widespread the same failure is or whether cheap water was decisive."
- **Heat recovery.** Whether rewarding it saves water "depends on which heat source it actually displaces, the extra electricity needed to deliver it, and whether demand coincides with supply."
- **Benefit-based review.** It needs attribution, plus answers to "who judges benefit, against what alternative, and how they handle uncertainty."
- **Overall verdict.** It separates the strands: a strong case for local water availability and drought priorities, a plausible case for testing value judgments, and too little evidence for making those judgments the basis of governance.

**Gap: it never tests "not technological necessity" for sufficiency.** This is one of the article's headline conclusions:
- §5.1: AI's water footprint results "from deliberate policy and design choices, not technological necessity"
- §6.3: outcomes "reflect policy and siting choices, not technological necessity"

The evaluation does say the §4 examples show alternatives exist but "cannot rank the options," and that Luleå's volume can't establish comparable consumption. It doesn't connect that to the article's own §4 constraints: Natick discontinued, "high capital costs," "limited suitable sites," and dry cooling that "degrades in hot/dry climates where water-scarcity is acute." Those constraints sit uneasily with the inference that technology isn't the bottleneck. They are also in tension with §5's own claim that "limited deployment and scalability show that technology alone is insufficient."

**Internal slip in the evaluation's own reasoning.** In its §5.1 paragraph, it first says §6.1 concedes water can't be attributed "to particular models or training runs." It then endorses "mandatory water impact assessments for training runs above computational thresholds" as resting "on measurable resource costs." The compute threshold is measurable. The water impact of a training run is the very thing §6.1 says can't yet be attributed.

## B4. Unstated warrants and missing qualifiers: **2**

It finds the warrants and dropped qualifiers that matter, and says why each matters.

**Unstated warrants:**
- **Application review needs attribution.** Judging "which AI applications justify their water costs" (§5.1) assumes water can be attributed to applications. §6.1 says current methods can't do that. This is the strongest catch in the evaluation.
- **Site counts as water pressure.** The step from a count of sites in stressed regions to water pressure, and to "systematic disregard," goes undefended.
- **One facility's volume as proof of feasibility.** The step from one facility's withdrawal volume to the claim that 25 million liters "suffices for hyperscale operations" (§6.3) goes undefended too. Table 1 footnote a says the facility's IT capacity isn't disclosed.
- **Restricting construction as a proxy.** It assumes building in a stressed basin implies consumptive demand there. A low-water design breaks that link.

**Missing qualifiers:**
- **The highlight.** "Two-thirds of post-2022 data centers are located in water-stressed regions" drops the body's "about," "suggests" and "built or planned" (§3.2). §5.1 repeats it with only "approximately."
- **Heat recovery.** §6.2 says heat recovery would deliver "co-benefits across energy, climate, and water domains." §4.5 had said it "may yield indirect water savings," that it "may not reduce on-site water consumption," that "lifecycle analysis is needed," and that "most examples are pilot-scale."
- **"Severely."** It's undefined in §6.2.

**Missed:** the "not technological necessity" warrant (see B3), and the move from an awareness gap to urgency in §5.1. The criterion scores what it catches, and what it catches is central.

## B5. Self-attribution: **2**

Its judgments are clearly its own ("I would read," "a premise I share," "I would need to see"). It also states its framing and how it could mislead: "my own preference for rules that can be measured and audited … can hide unfairness: a measurable limit can still leave essential users with too little if existing allocations are taken for granted." It considers the author's framing through their engineering and sustainability affiliations and the setting of a water journal. Both hold up against the front matter.

Its own suggestions are marked as its own and not credited to the author: for example, "A credible local replenishment project could still help," and that cumulative review and drought conditions "follow more directly" from Colón.

**One gap in the bias discussion.** The prompt asked about the author's "stake in the outcome." The evaluation doesn't mention that the §5.1 awareness evidence is the author's own work (Tsoury and Barnett-Itzhaki, 2025; Barnett-Itzhaki and Tsoury, 2025).

## B6. Correctness

### Problems raised

| # | Problem the evaluation raises | Verdict | Passage |
|---|---|---|---|
| 1 | The highlights announce the policy program before the evidence | **Confirmed** for the highlights; graphical abstract not checked (image) | Highlights 3–5 (policy gaps, digital water sobriety, mandatory transparency) |
| 2 | §2 gives little basis for judging how representative the sources and cases are | **Confirmed** | §2: three source streams and a priority rule, no selection criteria or counts |
| 3 | The opening figures (500 ml per 10–50 responses, 4.2–6.6 bn m³ globally, U.S. projection) mix populations and scales, and make a conditional estimate sound like a property of a response | **Confirmed** | §1; §3.1 says "similar AI workloads can translate into vastly different local water burdens" |
| 4 | §3 compares U.S. data-center *consumption* with *global withdrawals* despite the §2 distinction, mixing boundaries of geography and accounting | **Confirmed** | §2 (withdrawal vs consumption; "most figures cited … reflect total withdrawals"); §3: 66 bn L "consumption" vs "approximately 4000 km³ of freshwater are withdrawn," "a small fraction of national or global withdrawals" (only a global figure is given) |
| 5 | The two-thirds figure is about sites built *or planned*, not water use, and doesn't establish "systematic disregard" | **Confirmed** | §3.2: "reveals systematic disregard," "built or planned since 2022" (Bloomberg); Highlight 2 drops "or planned" |
| 6 | Colón shows allocation continuing during drought but not the campus's contribution, how widespread the failure is, or that cheap water was decisive | **Confirmed** | §3.2 (no figure for the campus's use; "not unique to Mexico … many regions" given with no source); §6.3: "siting decisions prioritizing electricity costs" asserted |
| 7 | The §4 options can't be ranked on a common basis; Luleå's per-MW value is an estimate and based on withdrawal, so it can't show comparable consumption | **Confirmed** | Table 1 footnote a; §4.1 "withdraws only 6.7 million gallons"; §6.3 "25 million liters annually suffices for hyperscale operations." (The article itself calls for "integrated assessment" at the end of §4.) |
| 8 | §6.2 recommends heat-recovery incentives more confidently than the evidence in §4.5 warrants | **Confirmed** | §4.5 "may yield," "may not reduce on-site water consumption," "lifecycle analysis is needed," "pilot-scale" vs §6.2 "delivering co-benefits across energy, climate, and water domains" |
| 9 | Replenishment pledges don't match the timing and location of consumption | **Confirmed** (raised by the article, endorsed by the evaluation) | §5.2 "temporal and spatial mismatch" |
| 10 | §6.2's extension of WUE reporting leaves out that a ratio isn't a volume; managers need absolute volumes by source, withdrawal vs consumption | **Not confirmed** | §6.2 adds "on-site consumption" to WUE reporting; §5.3 asks for locations, configurations and sources. A ratio-only reading is possible but not the most natural one |
| 11 | "Severely-stressed" is undefined, and a construction ban doesn't track consumption, so how it treats low-water proposals is unclear | **Confirmed** | §6.2 "Restrict new construction in severely-stressed watersheds," no definition or exemption |
| 12 | Benefit-based review of applications lacks attribution of water to models and runs, and an account of who judges | **Confirmed** | §5.1 first dimension and spectrum paragraph; §6.1 "without attributing water costs to specific models, training runs" |
| 13 | The medical-versus-recreational contrast makes the judgment look easier than it is | **Confirmed** as a fair reading | §5.1 spectrum paragraph (only end-point examples, no criteria for the middle) |

**Tally:** 12 confirmed (one only in part, since the graphical abstract couldn't be checked), 1 not confirmed (#10), 0 wrong.

### Errors (statements about the article that it doesn't bear out)

1. **§6.2's structure misdescribed.** The evaluation calls tiered, benefit-linked governance "the step §6.2 takes beyond" the concrete mechanisms. §6.2 presents those mechanisms as the content of that framework ("Concrete mechanisms include …"), and §5.1 does the same. The paraphrase also drops "and local water availability."
2. **§6.2's reporting proposal narrowed** (item #10). Saying §6.2 "leaves unstated" that a ratio isn't a volume reads past "include on-site consumption."
3. **A small gloss in §5.2.** "An annual company balance" isn't the article's wording. §5.2 speaks of a mismatch between "continuous, localized consumption and seasonal, distributed replenishment." The paraphrase is reasonable but adds "annual."

No numbers are misread. Every figure, section reference and quotation I checked (500 ml per 10–50 responses; 4.2–6.6 bn m³ by 2027; "built or planned since 2022"; Table 1 footnote a; the three §6.2 reporting items; §6.1 on attribution; the §5.1 mechanisms; "Making Waves") matches the article.

### Problems I see that the evaluation doesn't raise (my own reading, not scored)

- **Arithmetic in §3.** "Roughly, two liters … per kWh" for a 1 MW facility gives about 17,500 m³ a year (8,760 MWh × 2 L/kWh), not the "approximately 25,500 cubic meters" stated. The 25,500 figure implies about 2.9 L/kWh, which fits Table 1's "2.0–3.0+" but not the two liters in the text. The same sentence calls the volume lost "through evaporative losses alone," while the line before says only "significant fractions" evaporate.
- **Possible citation mismatch in §5.3.** The claim that disclosure of "facility locations, cooling configurations, and electricity sources" is missing is cited to Jain (2025). The article's own reference entry for Jain is an IEEE Spectrum piece on AI in chip verification. That's a provenance problem visible from the article's own reference list.
- **Pledges cited to one company.** The "water positive" pledges of Google *and* Microsoft are cited to a Reuters piece whose listed title concerns Google only (Paresh, 2021).

---

## Summary for the researcher

**Strengths.** This is a careful, selective evaluation that is accurate about the article. It reads the article's figures, qualifiers and table footnotes closely. Its best findings would be useful to anyone comparing sources:
- The highlight's two-thirds figure drops "built or planned."
- §3 compares consumption with withdrawals.
- The Luleå per-MW figure is an estimate and based on withdrawal.
- §6.2 drops the hedges §4.5 put on heat recovery.
- Benefit-based review of applications assumes an attribution that §6.1 says doesn't exist.

It handles sufficiency well, saying what each piece of evidence permits and what would be needed for more, and its final verdict separates the strong, plausible and under-supported parts of the argument. Its own position and biases are stated plainly.

**Weaknesses.**
- **Two criticisms aim slightly off the article's claims:** the WUE-as-ratio point, and treating tiered governance as a step beyond the mechanisms that §5.1 and §6.2 present as its content.
- **It never tests one headline conclusion:** that the footprint reflects "policy and siting choices, not technological necessity." The article's own constraints on scaling in §4 bear directly on it.
- **It barely weighs provenance,** though key premises rest on journalism and on the author's own surveys.
- **One internal inconsistency:** it treats impact assessments for training runs as measurable right after citing §6.1 that runs can't yet be assigned water costs.

None of these is a factual error about the article's numbers. The three errors listed are misdescriptions of structure or wording, not invented claims.
