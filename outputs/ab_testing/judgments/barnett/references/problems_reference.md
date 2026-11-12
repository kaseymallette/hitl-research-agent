# Problems reference list

**Article:** Barnett-Itzhaki, Z. (2026). "The water footprint of artificial intelligence: Emerging solutions and governance imperatives." *Water Research* 299, 125866 ("Making Waves" piece, 7 pages).

**Written from:** `RUBRIC.md` and `article.pdf` only. P31–P34 were added in a second pass, prompted by the researcher's own reading notes. Each was checked against the article and is included only because the article's text supports it. The passages are the article's, and the reasoning stands on them alone. Notes the article did not bear out were not added.

**Scope:** The whole article: highlights, abstract, Sections 1–6, and Table 1 with its footnotes. The graphical abstract is an image that repeats the abstract's structure, and I found nothing in it that adds a claim. The reference list was used only to check whether a citation, as the article itself lists it, fits the claim it supports. No cited work was looked up. Page numbers are the printed page numbers (1–7).

**How to use this list:** The problems are grouped by kind and numbered P1–P34. The numbers are fixed IDs, not positions: within each group, items are ordered by severity, so numbers can appear out of sequence. Within each group the more consequential ones come first, and each is tagged **Major**, **Moderate**, or **Minor**. Major problems bear on the article's central conclusions: (a) that AI's water footprint is large and growing, (b) that technical solutions exist and outcomes reflect "policy and siting choices, not technological necessity", and (c) that "digital water sobriety" and mandatory transparency are the needed response. An evaluation finds a problem when it identifies the same defect in the same passage, or in a passage the defect also appears in. It doesn't need to use the same wording.

---

## A. Conclusions that don't follow from, or contradict, the article's own evidence

**P1. "Not technological necessity" contradicts the article's own account of technical constraints. Major.**
- Passages: §5.1, p. 5 ("AI's water footprint results from deliberate policy and design choices, not technological necessity"). §6.3, p. 6 ("outcomes reflect policy and siting choices, not technological necessity"; "represents governance failure, not technical constraint"). §6.3, p. 7 ("Water-sustainable AI is achievable").
- Against: §4 intro, p. 3 ("each approach presents trade-offs, scalability constraints, or unresolved ecological questions"). Every §4 subsection lists technical or geographic limits: Nordic sites "geographically limited" (§4.1), "limited suitable sites" (§4.3), dry cooling "degrades in hot/dry climates where water-scarcity is acute" (§4.4), heat recovery "mostly pilot-scale" (§4.5). Also §4.5, p. 5: "No single siting or technology choice resolves all three tensions simultaneously".
- Problem: The article sets out real physical, geographic and energy–water trade-offs, then concludes that the footprint is a matter of choice rather than constraint. Showing that some sites can operate with little water doesn't show that AI at current scale can do so everywhere. The conclusion needs an unstated warrant: that the constraints the article itself lists can be removed by governance.

**P2. Two demonstrations are generalized to "hyperscale" feasibility. Major.**
- Passage: §6.3, p. 6: "Meta's Luleå facility demonstrates 25 million liters annually suffices for hyperscale operations, while China's subsea installations achieve zero freshwater consumption, suggesting outcomes reflect policy and siting choices".
- Problems:
  - Table 1 footnote a says Luleå's "facility-specific IT capacity not publicly disclosed". So the article has no basis for saying 25 million L "suffices" for any given scale of operation.
  - The 25.4 million L is a *withdrawal* figure (§4.1, "withdraws only 6.7 million gallons"), not consumption.
  - Luleå relies on a cold climate that §4.1 says is geographically limited.
  - The subsea centre houses "400–800 AI servers" (§4.3), which is not hyperscale. Microsoft discontinued its own subsea project (§4.3). Subsea scalability is "constrain[ed]" (§4.3).
  - "Zero freshwater consumption" ignores the shift to power-plant water that the article itself raises (Table 1 footnote c; §4.4).

**P3. The claim that deployment is "limited by policy gaps" is asserted, not shown. Major.**
- Passages: Highlights ("deployment remains limited by policy gaps"). Abstract ("their deployment remains limited"). §5 intro, p. 5 ("their limited deployment and scalability show that technology alone is insufficient").
- Problems:
  - The article never measures deployment: it gives no share of capacity using any of the §4 technologies.
  - It attributes limited deployment to policy, yet its own §4 offers technical, economic and geographic reasons: capital cost, climate, energy penalty, site availability.
  - "Limited … scalability" is a technical limit. Citing it as evidence that *governance* is the missing piece undercuts P1's conclusion rather than supporting it.

**P31. The article turns a sustainability question into a moral judgment about which AI uses deserve water, and its premises don't reach that conclusion. Major.**
- Passages: The conclusion is the article's own stated contribution and recurs throughout:
  - Abstract: "digital water sobriety" links "evaluation of which AI applications justify freshwater consumption" with siting and transparency.
  - Highlights: the framework "links AI evaluation to water constraints".
  - §5.1, p. 5: its first dimension is "evaluating which AI applications justify their water costs". It ranks applications "along a spectrum of societal justification". Medical diagnostics, climate modelling and drug discovery "may warrant significant resource expenditure". Recreational image generation, marketing content and "low-stakes conversational queries" are "difficult to justify".
  - §6.2, p. 6: "linking AI deployment decisions to demonstrated societal benefit".
  - §6.3, p. 6: "the central question shifts from marginal efficiency to resource justice: how much 'intelligence' per liter of water is justified". The article's last paragraph turns on "whose water it consumes".
- Problems:
  1. **Descriptive premises lead to a normative conclusion with no bridge.** The evidence in §1–§4 is all descriptive: how much water cooling uses, where data centres are, and what each technology costs and trades off. None of it concerns what any AI application delivers or whether that is worth its water. To get from "AI uses water, sometimes in stressed places" to "applications should be ranked and governed by societal worth", the article needs a normative premise. It only asserts one, once, without defending it: "digital water sobriety recognizes freshwater as a finite common resource requiring equitable allocation" (§5.1). Even granted, that premise supports fair allocation of water among *users of water* (agriculture, households, industry). It doesn't support ranking *AI applications against one another* by their value.
  2. **The value ranking has no criteria and no evidence.** Which applications have "substantial, broadly shared benefits" and which have "more diffuse societal value" is stated, not shown. The article gives no criterion for societal benefit, says nothing about who would judge it, and gives no data on what share of AI water use goes to the low-value uses it names. So it can't show that evaluating applications would change water outcomes at all (see P27).
  3. **It cuts against the article's own explanation of the problem.** The article argues that AI's footprint "results from deliberate policy and design choices, not technological necessity" (§5.1). It says Luleå and the subsea centres show outcomes "reflect policy and siting choices" (§6.3). If the footprint can be avoided by where and how computing is cooled, the article needs to say why water use must *also* be justified application by application. It doesn't. The reasons it gives are agriculture's food value (§3) and competition with agricultural and domestic needs in stressed watersheds (§5.1). Both support the siting rules it proposes separately, not a test of each application's worth.
  4. **The test can't be carried out on the article's own account.** §6.1 says current methods can't attribute water "to specific models, training runs, or architectural choices", so application-level water costs can't yet be known (see P9).
  5. **Its support for urgency doesn't bear on it.** The only evidence offered for why the evaluation is "urgent" is public unfamiliarity with the term "digital pollution" (P8).
- Scope note, for judging fairly: The article judges *applications* (uses of AI), not *who* may use AI. It also says the framework "does not propose binary approval or prohibition of specific applications; rather, it advocates a graduated governance approach" (§5.1). An evaluation that attacks a claim about restricting particular people, or an outright ban, is aiming at a claim the article didn't make. An evaluation finds P31 when it identifies the unsupported move from water-use evidence to a judgment of which applications are worth their water.

**P6. Location in water-stressed regions is read as "systematic disregard" and "market failure". Major.**
- Passages: §3.2, p. 3 ("the spatial distribution of AI infrastructure reveals systematic disregard for water availability constraints"). §5.1, p. 5 ("This concentration reflects a market failure: siting decisions are driven by electricity cost, network latency, tax incentives, and land availability").
- Problems:
  - The evidence is one Bloomberg statistic, introduced with "suggests". No base rate is given: how much of the land, population, or grid capacity in those countries lies in water-stressed regions.
  - The article offers no evidence about what data-centre siting decisions are actually driven by.
  - It doesn't consider that facilities in stressed regions may use low-water cooling.
  - "Reveals systematic disregard" infers intent and motive from a location pattern.

**P4. The abstract says waste heat recovery reduces on-site water demand; §4.5 says it may not. Moderate.**
- Passage: Abstract: "technologies, including cold-climate siting, natural water body cooling, waterless designs, and waste heat recovery, can reduce on-site demand".
- Against: §4.5, p. 4: waste heat recovery "may not reduce on-site water consumption, instead, it can shift water demand within the energy system so lifecycle analysis is needed".
- Problem: This is a direct internal contradiction.

**P5. The heat-recovery policy recommendation is more confident than the evidence. Moderate.**
- Passage: §6.2, p. 6: incentives for district heating "would accelerate deployment of system-level solutions that displace fossil thermal generation and associated water use, delivering co-benefits across energy, climate, and water domains."
- Against: §4.5 says net water benefit needs lifecycle analysis and that "most examples are pilot-scale". §6.1 says cross-city evidence on costs and integration "remains limited". §4.5's own claim was hedged ("this may yield indirect water savings").
- Problem: The hedge is dropped and water co-benefits are asserted as an outcome.

**P7. The Colón case is generalized into the article's model of governance failure. Moderate.**
- Passages: §3.2, p. 3 (the Colón narrative). §6.3, pp. 6–7 ("The Colón case epitomizes governance failures: siting decisions prioritizing electricity costs over hydrological constraints…").
- Problems:
  - The case rests on one piece of investigative journalism (Alvarez, 2024).
  - It establishes that the data centre was sited during a drought. It gives no evidence that Microsoft prioritized electricity costs, and no figure for the data centre's share of local water use relative to agriculture or other industry.
  - The causal link ("industrial water allocations continue serving data center cooling" while communities use trucked water) is reported, not shown.
  - In §6.3 the single case stands for a general pattern.

**P8. The urgency of evaluating AI applications is justified by public unfamiliarity with a term. Moderate.**
- Passage: §5.1, p. 5: "This evaluation is urgent given that 73% of UK respondents were unfamiliar with 'digital pollution' (Tsoury and Barnett-Itzhaki, 2025)".
- Problems:
  - This is a non sequitur. Unfamiliarity with a term doesn't make it urgent to evaluate which AI applications justify their water use.
  - The same section then cites "weak correlations between digital pollution knowledge and willingness to adopt sustainable practices" (Barnett-Itzhaki and Tsoury, 2025). That finding undercuts awareness as the lever, so the article's two uses of awareness pull in opposite directions.
  - Both studies are the author's own. "Studies show" is supported by one citation.

**P9. The proposed training-run assessments need accounting the article says doesn't exist. Moderate.**
- Passages: §5.1, p. 5 and §6.2, p. 6 propose "mandatory water impact assessments for training runs exceeding defined computational thresholds".
- Against: §6.1, p. 6: "Current methodologies measure facility-level consumption without attributing water costs to specific models, training runs, or architectural choices".
- Problem: The article doesn't acknowledge that its central mechanism depends on an unsolved measurement problem. Nor does it say how "demonstrated societal benefit" (§5.1, §6.2) would be measured or who would judge it.

**P10. The claimed "structural advantages" of water governance contradict the article's own case and transparency findings. Moderate.**
- Passage: §5.1, p. 5: water impacts are "inherently local and immediately visible to affected communities … municipal authorities already exercise direct control over allocation decisions."
- Against:
  - §3.2: in Mexico concessions are granted by a *national* agency (CONAGUA) and, once granted, "are rarely subject to reallocation during drought". The article calls permitting systems in "many regions" rigid.
  - §1: AI's footprint is "largely invisible to end users".
  - §5.2–5.3: aggregate disclosure "obscures facility-specific impacts" and "transparency remains severely limited".
- Problem: The claimed visibility and municipal control are contradicted by the article's own example and its argument for mandatory disclosure.

**P11. Section 6 says governance frameworks have been "shown" to work. Moderate.**
- Passage: §6 intro, p. 5: "The technical solutions and governance frameworks shown in the previous sections demonstrate that water-efficient AI is achievable through both technological innovation and policy intervention."
- Problem: The previous sections *propose* governance frameworks. They give no evidence that any has worked. The one regulatory example is a "proposed" Virginia bill (§5.3), and §5.1 notes that analogous climate and biodiversity frameworks "encountered significant implementation challenges".

**P32. The policy recommendations don't carry the trade-offs Section 4 identifies. Moderate.**
- Passages: §4.5, p. 5 closes Section 4 with three unresolved trade-offs (financial–environmental, energy–water, regional), "underscoring the need for integrated assessment across water, energy, and carbon dimensions."
- Against: The recommendations that follow are almost all water-only. §5.1 and §6.2 propose "scarcity-adjusted water pricing", "preferential permitting for operators adopting water-efficient cooling technologies", "facility-level water budgets", and to "Restrict new construction in severely-stressed watersheds".
- Problems:
  - Favouring water-efficient (dry) cooling raises electricity use "by approximately 10–25%" along with "associated carbon emissions" (§4.4, §4.5).
  - Restricting construction in water-stressed regions runs into the regional trade-off: §4.5 says the regions with high solar irradiance "tend to be arid and water-scarce".
  - The article never says how its policies would weigh water against energy and carbon, which is the integrated assessment it had just called for. Only the heat-recovery incentive claims benefits across several domains, and that claim is itself overstated (P5).
- Section 4 ends without resolving the trade-offs, and Section 5 opens by saying the technical solutions "demonstrate that water-efficient AI infrastructure is achievable" (see P1). The recommendations are presented as following from that technical analysis, but they don't engage the constraints it established.

**P34. The policy demands aren't connected to any evidence about policy, and the article leaves its own implementation objections unanswered. Moderate.**
- Passages: Abstract ("demands … fundamental policy reform"). §5.1, p. 5 and §6.2, p. 6 list the proposed mechanisms: scarcity-adjusted pricing, mandatory water impact assessments, facility-level water budgets, preferential permitting, siting restrictions, mandatory facility-level disclosure. §6.3, p. 6 ("represents governance failure").
- Problems:
  1. **Governance failure is concluded without examining governance.** The article mentions existing policy only in passing: Virginia's "proposed" disclosure bill and "similar initiatives emerging in Europe and the western United States" (§5.3, the latter uncited), EU limits on discharge temperature (§4.2), and Mexico's concession system (§3.2). It never says whether any data-centre water rules exist and have failed, or what became of the Virginia bill. The evidence for "governance failure" is one case and an asserted market failure (P6, P7). The article moves from what companies do (§5.2) straight to a list of demands, with no account of the policy record in between.
  2. **It raises objections to its own proposals and doesn't answer them.** §5.1 says analogous climate and biodiversity frameworks "encountered significant implementation challenges, including free-rider problems, jurisdictional fragmentation, and industry resistance". It calls them "a cautionary precedent", then says only that "sustained political will and enforceable regulatory mechanisms" are needed. It never says who would implement or enforce the mechanisms, at what level of government, or how thresholds and "demonstrated societal benefit" would be set. Nor does it say how its proposals avoid the problems it has just named. (Its claim that municipal authorities already control allocation conflicts with its own Mexico case; see P10.)
  3. **It doesn't use its own best evidence that regulation works.** §4.4 reports that for thermal power plants in arid regions, "regulatory mandates have driven dry cooling adoption despite similar energy penalties". That is a precedent of policy overcoming the very cost incentive the article blames for evaporative cooling. It would link the technical analysis to the policy case, but the article never returns to it in §5–§6.
- Fair-judging note: This is a short "Making Waves" perspective piece, and it doesn't owe a detailed implementation plan. The problem is not the absence of a plan as such. It is that the conclusions are stated as established ("demands … fundamental policy reform", "governance failure", frameworks "shown" to make water-efficient AI achievable; see P11). The article gives no evidence on how policy has performed and leaves its own stated objections unanswered. An evaluation finds P34 if it identifies the missing link between the demands and any evidence about policy, or the unanswered implementation obstacles. Related: P9 (assessments that can't yet be measured), P28 (necessity of reform).

**P12. "Qualitatively different" is concluded from quantitative differences. Minor.**
- Passage: §1, p. 2: "These distinctions establish that AI infrastructure presents a qualitatively different water challenge from general-purpose cloud computing".
- Problems:
  - Points (a)–(c) are all differences of degree: more power, continuous load, higher density. "Establish" overstates.
  - Point (b) is uncited and weak. Continuous high utilization raises total energy, but it doesn't raise water per unit of energy, and conventional data centres also run cooling continuously.
  - Higher rack density pushes facilities toward liquid cooling. §3.1 says liquid cooling can achieve very low WUE with dry coolers, which cuts against the implication that density means more water.

---

## B. Numbers that don't add up or are inconsistent

**P13. The 25,500 m³ figure doesn't follow from the stated 2 L/kWh. Major (numerical).**
- Passage: §3, p. 3: "Roughly, two liters of water are required to dissipate heat generated by components consuming one kWh … with significant fractions lost to evaporation (Mytton, 2021). Consequently, even a modest one MW data center facility consumes approximately 25,500 cubic meters annually through evaporative losses alone."
- Arithmetic: 1 MW × 8,760 h = 8,760 MWh. At 2 L/kWh that is about **17,520 m³/yr**, and that is total water, not evaporative loss alone. Getting 25,500 m³ needs about 2.9 L/kWh at full load around the clock.
- The text's own qualifier makes it worse: if only "significant fractions" are lost to evaporation, evaporative loss is below 17,520 m³.
- The same ~25,500 appears in Table 1 as the "representative" evaporative value, against a WUE range of 2.0–3.0+ (17,520–26,280 m³). So the representative value sits at the top of its own range.

**P14. The headline global projection is out of scale with the article's own U.S. figures, and its scope is undefined. Major.**
- Passages: Highlights, Abstract, §1 p. 2: AI's global footprint "could reach 4.2–6.6 billion cubic meters annually by 2027".
- Against: U.S. data centres consumed 66 billion L (0.066 billion m³) in 2023 (§3) and are projected at "up to 280 billion liters" (0.28 billion m³) by 2028 (§1).
- Arithmetic:
  - The global AI figure for 2027 is roughly **64–100×** total U.S. data-centre consumption in 2023.
  - It is roughly **15–24×** the U.S. projection for 2028.
- Problem: The article never reconciles these numbers. It never says what the 4.2–6.6 billion m³ includes (on-site only, or electricity-related water too; withdrawal or consumption). That is a scope mismatch with its stated focus on "operational blue water consumption" (§2), yet the figure is the article's headline evidence of scale.
- The figure is also restated in the highlights without the conditional "If this increase in AI use continues" (§1), which is itself vague: no increase has been described before it.

**P15. Withdrawal and consumption are conflated, against the article's own caveat. Major.**
- Passage: §2, p. 2 stresses the distinction and warns that "most figures cited in this review reflect total withdrawals unless otherwise specified".
- Problems: The text nonetheless uses consumption language for figures that are withdrawals, or of unstated type, and compares across the two.
  - §3, p. 3 compares U.S. data-centre "consumption" (66 billion L) with global "withdrawals" (4,000 km³) to call it "a small fraction". The two metrics differ, and so do the geographies: U.S. against global.
  - Luleå's 25.4 million L is introduced as a withdrawal (§4.1). It later becomes what "suffices for hyperscale operations" (§6.3). It is also used to derive a consumption-based per-MW value and a WUE in Table 1 (footnote a).
  - §3.2 sets Microsoft's "water consumption" (42%) beside Google's "water use" (15%) as if comparable.
  - The abstract and highlights call the projection a "footprint" and the article speaks of AI "consum[ing]" water, without saying which metric the figures are.
- Consequence: Many of the article's magnitudes cannot be interpreted on the basis the article itself says matters.

**P16. Table 1's free-air values can't be derived from the data stated. Moderate.**
- Passage: Table 1, free-air row: WUE "<0.3" and "<1,000" m³/yr per MW, both marked with footnote a: "Estimated from Meta Luleå reported withdrawal of 25,400 m³/yr; facility-specific IT capacity not publicly disclosed, so per-MW values are approximate."
- Problem: With IT capacity and energy unknown, neither a per-MW value nor a WUE can be estimated from a single facility total. The figures aren't "approximate"; they rest on an undisclosed assumption about capacity. They also feed a consumption metric (WUE is defined in §3 as site water *used*) from a withdrawal figure. The <1,000 m³/MW bound equals WUE ≈ 0.11, so it implies Luleå is over 25 MW, which is never stated.

**P18. The water-stress statistic hardens as it is repeated. Moderate.**
- Passages: §3.2, p. 3: "A Bloomberg analysis suggests about two-thirds of data centers built or planned since 2022 are [in] water-stressed regions". Highlights: "Two-thirds of post-2022 data centers are located in water-stressed regions". §5.1, p. 5: "approximately two-thirds of post-2022 data centers are in water-stressed areas."
- Problem: The hedge ("suggests"), the approximation, and "or planned" are dropped. Planned facilities are not "located" anywhere yet. The statistic's strength grows each time it appears.

**P19. Corporate figures said to "confirm" a concentration they don't confirm. Moderate.**
- Passage: §3.2, p. 3: "Corporate sustainability reports confirm this concentration: approximately 42% of Microsoft's water consumption occurs in water-stress regions, and 15% of Google's water use is concentrated in high water-scarcity areas (Barratt et al., 2025)."
- Problems:
  - The figures describe existing corporate water use, not the post-2022 build pattern they are said to confirm.
  - Google's 15% points away from a two-thirds concentration.
  - The categories differ ("water-stress" against "high water-scarcity").
  - The source cited is a Guardian article (Barratt et al., 2025, per the reference list), not the "corporate sustainability reports" the sentence names.

**P17. The U.S. 2028 projections are not reconciled. Minor.**
- Passages: §1, p. 2: "U.S. data centers alone projected to consume up to 280 billion liters per year by 2028 (Li et al., 2024; Shehabi et al., 2024)". §3, p. 3: "Projections for 2028 indicate hyperscale facilities alone will consume between 60 and 124 billion liters (Shehabi et al., 2024)".
- Problems:
  - Hyperscale and colocation were 84% of 2023 consumption. Even at its upper bound of 124 billion L, the hyperscale figure would be only about 44% of the 280 billion total, and the article doesn't explain the gap.
  - The projection range is also stated with certainty ("will consume").
  - The same 66 billion L 2023 figure is cited to Shehabi et al. in one paragraph and to Walton (2025) in the next.

**P20. The GPT-3 estimate is generalized into a pattern. Minor.**
- Passage: §5.1, p. 5: "training runs consume hundreds of thousands of liters in water-stressed regions for limited social benefit".
- Problem: The only training figure in the article is one estimate for one model: GPT-3, about 700,000 L (§1). Nothing in the article places that run in a water-stressed region or assesses its social benefit. The plural, the location, and the benefit judgment are all added.

---

## C. Data-centre figures stand in for AI

**P21. General data-centre evidence is used as evidence about AI. Major.**
- Passages: Throughout §3 and §3.2. Examples: U.S. data-centre water 2014–2023; Google's total withdrawals; the "two-thirds of data centers" statistic; Texas's "over 400 data centers"; Microsoft and Google corporate shares; the Colón data-centre campus.
- Problem: These figures cover all data-centre or all corporate water use, and the article doesn't say what share is due to AI. They are nonetheless presented as evidence of "AI's water footprint" and of "the spatial distribution of AI infrastructure" (§3.2). §6.1 concedes that no AI-specific water accounting exists ("without attributing water costs to specific models, training runs"). The article's claims about AI's footprint therefore rest on an unstated assumption that data-centre water use is AI water use.

**P22. "Most substantial" portion is asserted while indirect water is admitted to be poorly quantified. Moderate.**
- Passage: §1, p. 2: "This work focuses on operational water consumption for cooling, as it constitutes the most substantial and directly manageable portion."
- Against: §6.1, p. 6: indirect water "embedded in electricity generation and semiconductor manufacturing remains poorly quantified".
- Problem: The article cannot claim on-site cooling is the largest component while saying the other components are poorly quantified. The claim is unsupported, and it justifies the article's entire scope.

**P33. The abstract names three water pathways; the article examines one, and semiconductor water hardly appears. Minor.**
- Passage: Abstract: "AI infrastructure consumes freshwater through evaporative cooling, indirect water use in electricity generation, and water-intensive semiconductor manufacturing."
- Against:
  - Semiconductor manufacturing gets one sentence in the body (§1, p. 2: "chip fabrication processes consume thousands of liters per wafer"). It is then placed out of scope (§1, §2) and named as a research priority (§6.1).
  - Electricity-related water is also out of scope (§2), though it is touched on in §4 (hydropower evaporation, the shift to power plants under dry cooling, SMRs).
- Problems:
  - The article does state its scope, so this isn't an unexplained omission. But the abstract presents all three pathways as the subject, gives no sign that two are excluded, and pairs them with a headline figure whose scope is undefined (P14).
  - A reader of the abstract would take the conclusions to cover all three pathways, but they rest on on-site cooling evidence alone.
  - The scope choice is itself justified by an unsupported claim (P22).

---

## D. Evidence quality, method, and citation fit

**P23. The method is underspecified and doesn't match the evidence actually used. Moderate.**
- Passage: §2, p. 2: a "targeted review" of three streams; "Peer-reviewed sources were prioritized over the other two sources."
- Problems:
  - No search terms, inclusion criteria, or source counts are given, so selection can't be assessed.
  - Many load-bearing claims come from non-peer-reviewed sources. Examples: the headline projection (Li et al., 2024, listed as an arXiv preprint); the two-thirds statistic (Bloomberg); the Colón case (In These Times); the corporate shares (Guardian); the Texas projection (Texas Tribune); the WUE definition (an Equinix blog); and the technology claims (vendor sites for ZutaCore and Deep Green).
  - The stated prioritization isn't reflected in the evidence that carries the argument.

**P24. Cited sources don't match the claims, judged by the article's own reference list. Moderate.**
- §5.3, p. 5: "Comprehensive understanding requires disclosure of facility locations, cooling configurations, and electricity sources, data that remain missing or aggregated (Jain, 2025)." Jain (2025) is listed as "From bottleneck to breakthrough: AI in chip verification…" (IEEE Spectrum), which by its title is unrelated to data-centre water disclosure.
- §3.2, p. 3: the claim that CONAGUA concessions may not reflect current conditions is cited to de Lourdes Corral-Bermudez et al. (2019). That study is listed as concerning aquifer overexploitation in Laguna de Santiaguillo, Durango, a different basin and topic from data-centre allocations in Colón.
- §5.2, p. 5: "Google and Microsoft have pledged to become 'water positive' by 2030 … (Paresh, 2021)". The cited source is listed as "Google to replenish 20% more water than it uses by 2030", which covers Google only, not Microsoft.
- §3, p. 3: Texas "projected to consume nearly 3% of statewide water supply by 2030 (Martinez, 2025)". The source's listed title says state planners "don't know how much they will need", which sits uneasily with a precise projection. **Lower confidence:** this is inferred from the title only.

**P25. Key quantitative claims are uncited. Moderate.**
- §1, p. 2: point (b), the continuous near-100% GPU utilization and its consequence for water.
- §4.3, p. 4: "Initial assessments report minimal thermal effects (<1 °C temperature rise)".
- §4.4, p. 4: dry cooling raises electricity use "by approximately 10–25%". Electricity is "typically 40–60% of total operating expenses". Water is "priced far below its scarcity value in most jurisdictions". The economic-incentive argument in §4.4, §4.5 and §5.1 rests on these.
- §5.1, p. 5: the "analogous" climate and biodiversity governance frameworks and their "implementation challenges".
- §5.3, p. 5: "similar initiatives emerging in Europe and the western United States".

**P26. Natural-water-body cooling terminology is confused. Minor.**
- Passages: §4.2, p. 4 describes "closed-loop heat exchangers, eliminating consumptive withdrawals". Alibaba "pipes 17 °C water from 35 m depth", which draws and returns lake water. Table 1 footnote b says "Closed-loop systems return water to source". §4.2's trade-offs then discuss "once-through or open-loop cooling".
- Problems:
  - §2 attributes the return-to-source, thermal-pollution behaviour to *once-through* systems. The article applies "closed-loop" to systems that withdraw and discharge water.
  - "Consumptive withdrawals" mixes the two concepts §2 says must be kept apart.
  - It is unclear which regulatory constraints apply to which systems.

---

## E. Unstated warrants and value judgments presented as findings

**P27. The ranking of AI applications by societal value is asserted without criteria or evidence. Moderate.**
- Passages: §3, p. 3: "unlike agricultural water consumption, which supports food production for large populations, data center water use serves digital services whose societal necessity varies widely". §5.1, p. 5: medical diagnostics, climate modelling and drug discovery against "recreational image generation, automated marketing content, or low-stakes conversational queries".
- Problems:
  - These value rankings carry the framework, but the article gives no criterion for societal benefit and no data on how water use divides among these uses.
  - The comparison with agriculture assumes all agricultural water serves high-value needs, an assumption it doesn't state.

**P28. Policy reform is concluded to be required without showing that alternatives fail. Moderate.**
- Passages: Abstract: "Achieving water-sustainable AI demands not merely technological optimization but fundamental policy reform". §5 intro: "requires robust governance frameworks".
- Problem: The necessity claim rests on P3, limited deployment attributed to policy without evidence, and P6, an asserted market failure. The article doesn't consider whether price signals, rising scarcity, or the corporate commitments it dismisses as "inadequate" (§5.2) could achieve the same ends, or what evidence would show they can't. The evidence permits policy reform as one option; it doesn't establish that reform is required.

**P29. Corporate pledges are dismissed by assertion. Minor.**
- Passage: §5.2, p. 5: "Corporate responses to water concerns remain inadequate"; replenishment credits "fail to address the temporal and spatial mismatch".
- Problem: The mismatch argument is plausible but uncited. The article gives no evidence on how the pledges are actually carried out or what they achieve. The same section also reports reclaimed-water use at more than 25% of Google sites, without weighing that against "inadequate".

**P30. Overstatement and loose descriptions. Minor.**
- §4.5, p. 5: "Currently most examples are pilot-scale". This sits beside Stockholm's scheme heating about 30,000 apartments and Espoo's planned supply of about 40% of district heat for about 250,000 customers. Neither is pilot-scale, so the characterization is at least loose.
- §4.3, p. 4: Natick was discontinued "despite technical success, suggesting economic or operational constraints". This is hedged speculation, but §6.3 leans on subsea as a demonstrated pathway without carrying the caveat (see P2).
- §3, p. 3: global data centres "withdraw billions of liters of water per year". This understates the article's own figures: Google alone withdraws more than 20 billion L, and U.S. data centres consume 66 billion L. It doesn't mislead the argument's direction, but it shows imprecise handling of magnitudes.

---

## Not problems (checked and found consistent)

These were checked so that later sessions don't count them as errors when an evaluation flags them:
- 6.7 million gallons ≈ 25.4 million L ≈ 25,400 m³. The conversion is correct.
- 66 billion L = 0.066 km³. Correct.
- 10–50 responses per 500 ml means 10–50 ml per response. Consistent with §1.
- The thermal discharge of 5–8 °C is the same in Table 1, §4.2 and §6.1.
- Google's 20 billion L is correctly labelled a withdrawal, with consumption "not separately disclosed" (§3).
