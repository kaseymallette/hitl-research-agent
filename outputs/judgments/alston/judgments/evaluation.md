# Judgment: argument evaluation

**Article:** `article.pdf`. Alston, Love & Haider, "Data Center Cooling Choices Shift Water Impacts Across the Grid: An Integrated Water-Energy Model for Sustainable Data Center Development" (arXiv:2609.25437v1 [eess.SY], 12 pp. including Appendix A).

**Judged:** `run/argument_evaluation.md` (1,190 words), against the article alone, on B1–B6. I didn't open the close reading, the claims reference list, or any other judgment.

**How I read the article:** I extracted the text with Ghostscript (`txtwrite`). I rendered the figures as page images and read Figures 3, 4, 6 and 8 by eye at 300 dpi, because the evaluation makes claims about them.

---

## B1. Premise acceptability — **2**

The evaluation weighs where the evidence behind each central conclusion comes from, and says where in the article that evidence is:

- **Cooling tradeoff (Table 2).** It notes that both stand-alone configurations use the "upper endpoints of simulated performance ranges". The article says this in §3.2: "upper endpoints of their respective midsize data center performance ranges [20], representing worst-case configurations", and §2.1.4 says the ranges are simulated. The evaluation concludes that these endpoints "do not establish the difference between two designs serving the same real site and workload."
- **Hybrid result.** It ties the hybrid's ranking to the efficiency chosen for each mode and to the fixed daily temperature and humidity rule. It cites the 25% economizer share (Table 3) and the authors' own admission in §5.2 that the control logic is simplified.
- **Dispatch.** It names three weaknesses. The four-bus, four-corridor grid has line limits set heuristically so congestion doesn't dominate (§3.1.1). Marginal costs are set per technology (Appendix A, Table A.2). The monthly WCI values are reported or imputed (§2.2.4).
- **Depletion.** It reads equations (11)–(13) closely enough to see that gross supply is fixed. It also notes that facilities and generators are assigned to basins by location, which the authors admit in §5.2.

It doesn't take up two weaker inputs: the article mixes datasets from different years (2019 hydrology per ref [31], 2023 load and weather, 2024 generators), and it uses the median of other plants of the same technology when a plant's WCI is missing (§2.2.4). Neither gap leaves a central conclusion unexamined.

## B2. Relevance of critique — **1**

Most of the criticisms are aimed at claims the authors actually make, with their qualifiers:

- The cooling critique is framed "for the assumptions used". It credits the result with a break-even margin before qualifying it.
- The criticism of average grid factors is aimed at Finding 2 and Recommendation 2 as worded.
- The Figure 8 point is aimed at the specific example the authors give in §4.5.

Two criticisms go after a stronger claim than the article makes:

1. **"Exactly which places."** The thesis sentence says the authors make "a weaker case that their Michigan model can tell a planner *exactly* which places will bear that burden." The authors do claim spatial attribution: the abstract says the model "resolves where and when water is consumed", and §4.5 names basin 04050002. But they also hedge: "The resulting depletion estimates indicate regional patterns; more detailed accounting of local water supply and use is needed to assess the risks to specific water regions" (§5.2). §4.3 attributes the unchanging spatial pattern to the four-bus grid. The evaluation's body argument is properly scoped ("To treat a particular basin as a likely recipient would take evidence…"). The framing sentence drops the authors' qualifier, and the evaluation never says the authors already concede the four-bus limit.
2. **Siting.** "It does not establish that the new sites face less water risk" is aimed fairly at §4.3's "reduced the impact of the data center build out". However, the authors say the same thing themselves in §5.1, Recommendation 3: "Distributing data center compute is therefore not automatically a better outcome, since the affected subbasins carry different baseline conditions." The evaluation presents the point as a correction and doesn't credit the authors' qualifier.

Neither is a straw man. The main critiques land on what the authors said.

## B3. Sufficiency — **2**

This is the evaluation's strongest criterion. For each central conclusion it says whether the evidence requires the conclusion or only permits it, and what would close the gap:

- **Cooling tradeoff.** It works out how close the result is to reversing. For the extra electricity to wipe out the direct water saving, it would need about 6.4 m³ of indirect water per extra MWh; the modeled figure is about 1.5. I checked these: 6.24 / 0.98 = 6.37 and 1.43 / 0.98 = 1.46, from Table 2. So the headline result holds under the stated inputs. Because those inputs are upper endpoints, it says what's still needed: "site-specific performance curves".
- **Average intensities cannot capture indirect impacts.** It says the claim is permitted, not required. Figure 3 shows monthly variation that a single annual factor can't reproduce. But the paper never computes a monthly or annual average-factor estimate to compare against. What's needed: "A comparison of the incremental mix and its water intensity with monthly and annual average-factor estimates."
- **Impacts beyond the site / basin attribution.** "The four-bus model is enough to show why an off-site pathway matters." Naming particular basins would take robustness checks across dispatch costs, network constraints and plant WCIs.
- **Siting reduces impact.** Sufficient for a max-burden objective, not for a lower-risk claim.
- **Depletion as risk.** "Can flag places and months for inquiry". It notes there's no threshold that triggers a shortage.
- **Need for integrated modeling.** It says the paper never tests whether a simpler estimate would be accurate enough for a regional inventory.

## B4. Unstated warrants and missing qualifiers — **2**

It finds the warrants the conclusions depend on that the authors never state, and says why each matters:

- **Plant WCI as a marginal rate.** Multiplying the change in output by a plant's monthly average WCI (eq. 8) assumes each extra MWh consumes water at that average rate. The authors question this for hydro (§3.1.2) but never for thermoelectric plants.
- **Which plants respond.** The dispatch identifies "the generators that respond", but costs are set per technology. Within a technology every plant has the same cost, and nuclear and natural gas are both $23/MWh in Table A.2. So the plant the solver picks may be arbitrary even though the plants' water intensities differ. This warrant sits under the paper's central claim to identify the responding generators, and the article doesn't discuss it.
- **Location-based basin assignment and fixed gross supply** in eqs. (6), (11) and (12).
- **Design endpoints as stand-ins for real designs.**
- **Depletion share as risk**, with no threshold.

It also finds missing qualifiers. The cooling result holds only "for the assumptions used". The ranking among the three configurations depends on which objective you minimize. And annual and monthly views give different rankings, which it shows with Figure 8.

What it doesn't catch is listed below, under "Problems the evaluation doesn't raise". Since the evaluation was asked to be selective, those omissions don't lower the score.

## B5. Self-attribution — **2**

The evaluation's judgments are plainly its own throughout ("I would use the three cases…", "I would take the reporting recommendation far enough to…"). It states its own framing and possible bias: "My own preference for checking local and seasonal exposure makes the maps persuasive to me; it also makes me wary of reading detailed maps as evidence that the underlying allocations are precise." It names what may shape the authors' framing: the engineering purpose, the Graham Sustainability Institute grant, and treating development as something to plan rather than question. It labels its closing reporting proposal as going beyond the paper ("The paper shows why those questions belong in the decision. It leaves the answers… open"). I found no place where its view could be mistaken for the authors'.

## B6. Correctness

### Problems raised

| # | Problem the evaluation raises | Verdict | Where in the article |
|---|---|---|---|
| 1 | Figure 4 shows the total generation mix, not the incremental response. The paper never compares its incremental method with average-factor estimates, so how much simpler methods miss is never measured. | **Confirmed** | Fig. 4 caption ("Monthly total generation mix"). §4.2 text ("serve total electric load on the system (baseline + facility load)"). No average-factor estimate is computed anywhere. Finding 2 / Rec. 2 are asserted from monthly variation alone. |
| 2 | The stand-alone air-cooled and water-cooled cases use the upper endpoints of simulated ranges, which don't establish a real design difference. | **Confirmed** | §3.2 ("upper endpoints… representing worst-case configurations"). §2.1.4 ("simulated ranges"). §5.2 ("estimated ranges rather than the true values of specific facilities"). |
| 3 | The hybrid's ranking depends on the efficiency chosen for each mode and how often the economizer runs. The 25% economizer share comes from a fixed rule, and §5.2 says mixing outdoor and return air could allow more. | **Confirmed** | §3.2: the hybrid uses lower endpoints for air mode and upper for water mode, while the stand-alone air-cooled case uses upper endpoints. Table 3 (Annual 25%). §5.2 on mixing outdoor and return air. |
| 4 | Air cooling minimizes modeled water volume and the hybrid minimizes electricity, so choosing between them takes a judgment the paper doesn't make. | **Confirmed** | Table 2 (total water 6.12 vs 7.19; electricity 2.76 vs 4.06 TWh). §5.1 Rec. 1 states no decision rule. |
| 5 | Marginal costs are set per technology, so plants with different WCI can tie, and the solver's choice among them is arbitrary. | **Confirmed** (as a structural concern; the article neither tests nor discusses it) | Appendix A, Table A.2 (one cost per carrier; nuclear = natural gas = $23/MWh). Table A.3 (WCI differs by carrier). §2.2.4 (WCI is plant-specific). |
| 6 | Applying a plant's monthly average WCI to its added output assumes each extra MWh consumes water at that rate. The authors raise this distinction only for hydro. | **Confirmed** | Eq. (8). §3.1.2 hydro argument ("WCI is the rate of water consumption per unit of power produced…"). |
| 7 | Naming particular basins as recipients would need robustness checks on dispatch costs, network constraints and WCIs. The four-bus grid has limits set so congestion doesn't dominate. | **Confirmed** | §3.1.1 (6,000 MW limits "selected heuristically… to prevent transmission congestion from dominating"). §4.3 and §5.2 acknowledge the four-region limit. The article has no sensitivity analysis. |
| 8 | Relocating the facilities lowers the largest basin increase (6.74 → 2.78 pp) with about the same total consumption, but doesn't show the new sites face less water risk. | **Confirmed**, but the authors make the same point themselves and the evaluation doesn't say so | §4.3, Table 2 (124.11 vs 124.13 million m³). §5.1 Rec. 3 ("not automatically a better outcome"). |
| 9 | Figure 8 undercuts the paper's annual comparison. Basin 04100002 looks less concerning than 04050002 by annual total, yet reaches almost 50% depletion in September. | **Confirmed** | §4.5 gives 04100002 as a large increase that "may not result in a significant impact". Fig. 6: annual totals about 4.26% vs about 5.9%. Fig. 8, middle panel: September bar about 48% (baseline about 33% plus direct). 04050002 peaks around 30% in August. This is a real internal tension in the article. |
| 10 | Depletion is only a proxy: gross supply is held fixed, consumption is assigned by location, and no threshold says when depletion means a shortage. | **Confirmed** | Eqs. (6), (11) and (12) use the same baseline supply S in both cases. §2.3 assigns facilities and generators to basins by location. §5.2 ("may misallocate consumption if the water is actually sourced from a different subbasin"). No threshold is defined anywhere. |
| 11 | The paper never tests whether a simpler estimate would be accurate enough for a regional inventory. | **Confirmed** | Same evidence as #1. The §5.1 summary ("must move towards integrated water–energy models") rests on no error comparison. |
| 12 | Whether to build, who bears the burden, and supply-chain impacts are outside the analysis. | **Confirmed** (a scope observation, not a flaw) | §2 excludes Scope 3 explicitly. No distributional analysis. |

**Tally:** 12 problems raised, 12 confirmed, 0 not confirmed, 0 wrong. On #8 the evaluation doesn't credit the authors' own caveat.

### Errors

Clear-cut errors: **none found.** I checked every number and factual description against the text, tables and figures:

- Table 2 differences: 6.24 million m³, 0.98 TWh, 1.43 million m³.
- Break-even ratios: about 6.4 vs about 1.5.
- Siting: 6.74 → 2.78 pp. Eq. (13) defines the change in pp, and Fig. 8 labels it "pp".
- 25% economizer share; four buses and four corridors.
- Nearly identical statewide consumption.
- Figure 3: indirect water varies by month while power stays constant. Visible in the figure: water-cooled indirect runs from about 0.29 to about 0.48 million m³/month.
- Figure 4 shows the total mix. Figure 8 shows about 48% in September for 04100002.
- Eqs. (11)–(13) hold supply fixed. §5.2 admits supply may come from another basin.
- The eess.SY category and the funding source.

One overstatement, borderline: the opening says the authors claim the model can tell a planner "exactly" which places bear the burden. That's stronger than the authors' hedged §5.2 ("indicate regional patterns"). See B2.

### Problems the evaluation doesn't raise (my own reading, not scored)

- **The abstract's "~50%" figure isn't traced.** The abstract says indirect water intensity "varies by approximately 50% across months". The main text never gives this number or shows how it was computed. It can only be roughly inferred from Figure 3.
- **Generalization from one region.** §5.1 Rec. 1 says "the same cooling configuration can produce different water outcomes in a different grid region". Only one region (Michigan) is modeled, so this is inferred, not shown.
- **Priority claim.** §5.2 says "the first to connect facility cooling configuration, grid dispatch, and subbasin-level water depletion". The related-work section (§1.1) doesn't establish this.
- **Mismatched data years.** The datasets come from 2019 (hydrology), 2023 (load and weather) and 2024 (generators). §5.2 acknowledges this only in general terms. Monthly coincidence results, such as Figure 8's late-summer peaks, rely on these years lining up.

---

## Summary for the researcher

**Strengths.** This is a careful, accurate and selective evaluation:

- I found no factual errors, and all twelve problems it raises hold up against the article.
- Its sufficiency reasoning is the best part. The break-even calculation on Table 2 is correct and goes beyond the article.
- It catches two problems that are easy to miss and important. First, setting dispatch costs per technology undercuts the paper's central claim to identify the responding generators. Second, Figure 8 contradicts the paper's own §4.5 example of a basin whose annual increase "may not" be significant.
- For each claim it says what would be needed to establish it.
- It keeps its own voice separate from the authors' and states its own bias.

**Weaknesses.**

- It overstates what the authors claim once: "exactly which places".
- It presents two points as corrections when the authors already concede them: the siting caveat (§5.1 Rec. 3) and the four-bus spatial limit (§4.3, §5.2). A reader could come away thinking the paper is less self-aware than it is.
- It doesn't take up the untraced "~50%" monthly-variation figure in the abstract, the mixed data years, or the "first to connect" priority claim.

None of these weaknesses affects the soundness of its central judgments.
