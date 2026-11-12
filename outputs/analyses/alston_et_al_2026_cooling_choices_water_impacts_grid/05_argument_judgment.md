# Judgment: argument evaluation

**Article:** `article.pdf` — Alston, Love, and Haider, "Data Center Cooling Choices Shift Water Impacts Across the Grid: An Integrated Water-Energy Model for Sustainable Data Center Development" (arXiv:2609.25437v1, eess.SY)

**Evaluated:** `run/argument_evaluation.md`

**How the article was read:** The text was extracted with Ghostscript (`txtwrite`). The extraction interleaves the two columns but is complete. Pages 5–9 were also rendered as images so Table 2, Table 3, Figure 3, Figure 7, and Figure 8 could be checked by eye. Figure 8 was rendered at 300 dpi to read the September bar. As the session instructions required, I did not open `analysis.json`, the claims reference list, or any other judgment.

---

## B1. Premise acceptability: **2**

The evaluation weighs the evidence behind each central conclusion and points to the passage it means.

- **Cooling tradeoff (Table 2):** It notes that Scenario 1 uses the "upper endpoints" of the DOE performance ranges (§3.2), and that those ranges are simulated rather than measured (§2.1.4). It concludes that this shows a tradeoff for the assumptions used, not a difference between real designs.
- **Hybrid's advantage:** It ties the result to the fixed temperature and humidity rule and the 25% economizer share (Table 3). It also cites the authors' own note in §5.2 that mixing outdoor and return air could allow more winter economizer use.
- **Dispatch:** It names three sources for the dispatch results:
  - the four-bus grid with heuristic corridor limits (§3.1.1)
  - marginal costs set per technology rather than per plant (Appendix A, Table A.2)
  - monthly water intensities that are either reported or imputed (§2.2.4)
- **Depletion metric:** It notes that Eqs. (11)–(13) hold supply fixed, and that facilities and generators are assigned to subbasins by location (§2.3, §5.2).

Gaps in provenance it doesn't weigh:

- The datasets come from different years: USGS hydrology from 2019, county load and weather from 2023, and EIA generator data from 2024. §5.2 flags this mismatch itself.
- The Scenario 2 hourly load profile comes from ref. [3], which the reference list marks as "Report funded by CloudHQ, LLC."
- The cooling configurations of the three Scenario 2 facilities are assumed, as §3.3 says.

These gaps don't change the score, since the evidence behind the main conclusions is weighed with passages.

## B2. Relevance of critique: **2**

Each criticism addresses a claim the authors actually made, with its qualifiers.

- **Cooling result:** The evaluation accepts the result "for the assumptions used," which is the claim the paper's §3.2 supports. It doesn't attack a broader claim.
- **Siting:** It quotes §4.3 accurately ("reduced the impact of the data center build out"). It then sets that against the authors' own Recommendation 3, quoted exactly: "not automatically a better outcome, since the affected subbasins carry different baseline conditions."
- **Spatial precision:** It aims at the paper's claims to resolve "where and when water is consumed" (abstract) and to show that other methods "misattribute" consumption (§4.3). It also credits the paper's own concession that the depletion estimates "indicate regional patterns" (§5.2).
- **Decision rule:** It presents the missing decision rule, and the distributional and Scope 3 questions, as lying outside the paper's scope (§2), not as failures of a claim the paper made.

## B3. Sufficiency: **2**

For each central conclusion, the evaluation says whether the evidence reaches it and what would be needed if it doesn't.

- **Cooling:** It computes a break-even rate. The extra electricity would need about 6.4 m³ of indirect water per extra MWh to erase the direct saving, compared with about 1.5 m³/MWh in the model. So the evidence requires the direction of the result under these inputs, but the inputs don't establish a comparison of real designs. What's needed: site-specific performance curves.
- **Average grid factors fall short (§4.2):** Figure 3 supports the claim that monthly intensity varies. But no average-factor estimate is ever computed, so the size of what simpler methods miss isn't shown. What's needed: a comparison against monthly and annual average-factor estimates.
- **Specific basins:** The four-bus model is enough to show that an off-site pathway exists. It isn't enough to name particular receiving basins. What's needed: a check that the result holds under changes to dispatch costs, network limits, and water intensities.
- **Siting:** Spreading the facilities out reduces the largest single increase, but that doesn't establish lower water risk.
- **Depletion as risk:** Depletion is a screen, and the paper gives no threshold at which shortage would occur.

## B4. Unstated warrants and missing qualifiers: **2**

The evaluation finds warrants the conclusions depend on and says why each matters.

1. **Average rate treated as marginal.** The model applies a plant's average monthly water intensity to each added MWh (Eqs. 5 and 8). The evaluation notes that the authors question this assumption for hydro (§3.1.2) but not for thermoelectric plants.
2. **Ties in cost.** Costs are set per technology, so the least-cost solution can pick one plant over another with a different water intensity for no reason in the objective.
3. **Depletion stands in for risk.** Supply is held fixed, sources are assigned by location, and there is no shortage threshold.
4. **Endpoints stand in for designs.** Points on simulated performance ranges are treated as if they described real designs.

It also finds conclusions that lack the qualifiers the evidence calls for:

- the §4.3 claim that siting "reduced the impact," which holds only for the largest single-basin increase
- the headline cooling result, which leaves out that the inputs are worst-case
- the claim that simpler methods "cannot capture" the paper's findings, which was never tested

**My own reading, not scored:** One warrant the evaluation doesn't name is that the model treats Michigan's grid as closed. No imports or exports appear anywhere in the article, so every added MWh is met by in-state generators. That assumption underlies the subbasin attribution in §4.3 and §4.5.

## B5. Self-attribution: **2**

The evaluation's judgments are marked as its own ("I would use the three cases…", "I would take the reporting recommendation…"). It states its own bias directly: its preference for local and seasonal exposure makes the maps persuasive to it, and also makes it wary of reading them as precise. It names the authors' setting (an engineering field, a University of Michigan Graham Sustainability Institute grant) and their framing of development as something to plan and improve. Every statement about the authors' position is tied to a section or quote, and checking those found none of the evaluation's own conclusions credited to the authors.

## B6. Correctness

### Problems raised

| # | Problem the evaluation raises | Verdict | Passage |
|---|---|---|---|
| 1 | The paper argues more strongly for asking "where and when" than for pinpointing the basins affected, and concedes this itself | Confirmed | §5.2 Water System: estimates "indicate regional patterns"; more detailed local accounting is needed |
| 2 | Figure 4 shows the total generation mix, not the plants whose output changed, and no average-factor estimate is computed to show what simpler methods miss | Confirmed | §4.2 says Figure 4 plots "baseline + facility load"; §4 claims "five critical findings that these simplified approaches cannot capture" but never runs those approaches |
| 3 | The cooling comparison rests on the upper endpoints of simulated DOE ranges, not real designs | Confirmed | §2.1.4 ("simulated ranges"); §3.2 ("upper endpoints… representing worst-case configurations") |
| 4 | The hybrid's ranking depends on the efficiencies chosen for each mode and on a simplified economizer rule (25% use) | Confirmed | §3.2 (lower endpoints for air-cooled mode, upper for water-cooled mode); Table 3 (annual 25%); §5.2 DCF System (mixing return air) |
| 5 | Air cooling minimizes total water; hybrid minimizes electricity; choosing between them takes a further judgment | Confirmed | Table 2: air-cooled total 6.12 Mm³ is the lowest; hybrid at 2.76 TWh uses the least electricity |
| 6 | Costs set per technology let plants with different water intensities tie in cost, so which plant the dispatch picks is arbitrary | Confirmed | §2.2.1 groups generators at each plant by technology; Table A.2 sets costs per carrier. Nuclear and natural gas are both priced at $23/MWh, which strengthens the point. |
| 7 | A plant's average monthly intensity is applied to each added MWh, though the paper argues the marginal case for hydro | Confirmed | Eqs. (5) and (8); §3.1.2 hydro argument |
| 8 | The four-bus grid limits which basins can be identified, and the paper tests no alternative dispatch assumptions | Confirmed | §3.1.1; §4.3 ("highly aggregated grid model"); §5.2 Energy System. The article contains no such test. |
| 9 | §4.3 says siting "reduced the impact," which is in tension with Recommendation 3 | Confirmed | §4.3 last paragraph; §5.1 Rec. 3, quoted exactly |
| 10 | Figure 8: basin 04100002, offered as a low-impact example, reaches nearly 50% total depletion in September | Confirmed by eye | §4.5 names 04100002 as a case where "a large increase in depletion may not result in a significant impact." Figure 8's middle panel peaks at about 48% in September on a 0–50 axis, above the August peak of about 30% in 04050002, the basin §4.5 uses as its high-impact example. |
| 11 | Depletion is a proxy: supply is fixed, sources are assigned by location, and no shortage threshold is given | Confirmed | Eqs. (11)–(13); §2.3 assigns subbasins by polygon; §5.2 Water System (water may be sourced from another subbasin) |
| 12 | Whether to build, who bears the burden, and supply-chain impacts lie outside the analysis | Confirmed | §2 excludes Scope 3; no section addresses distribution |
| 13 | The paper never tests whether a simpler estimate would be accurate enough for a regional inventory | Confirmed | Same gap as #2 |

13 raised, 13 confirmed, 0 not confirmed, 0 wrong.

### Errors

None found. Every number was checked against Table 2 and the text:

- direct saving 6.45 − 0.21 = 6.24 Mm³
- extra electricity 4.06 − 3.08 = 0.98 TWh
- extra indirect water 5.91 − 4.48 = 1.43 Mm³
- break-even 6.24/0.98 ≈ 6.4 m³/MWh, against 1.43/0.98 ≈ 1.5 m³/MWh in the model
- largest increase 6.74 → 2.78
- 25% economizer use
- statewide totals 124.11 vs 124.13 Mm³

All are correct. The evaluation reports 6.74 → 2.78 in "percentage points," while the §4.3 text writes "%." This is consistent with Eq. (13) and Figure 8's "pp" labels, so it isn't an error. The quotes from §5.2 and Recommendation 3 match the article's wording.

### Problems in the article the evaluation doesn't raise (my own reading, not scored)

- The model treats Michigan's grid as closed, with no imports or exports (see B4).
- The abstract says indirect water intensity "varies by approximately 50%… across months." The body text gives no number that backs this 50% figure.
- The datasets come from different years (2019, 2023, and 2024).
- The Scenario 2 load profile comes from a source funded by a data center firm (ref. [3]).

---

## Summary for the researcher

This is a strong evaluation. It chooses a few judgments that matter and develops each against specific passages. Its best contributions:

- the break-even calculation, which shows how far the cooling result is from being reversed rather than just restating it
- the point that per-technology costs make the choice among plants, and so the mapped water impacts, arbitrary
- the Figure 8 reading, which uses the paper's own monthly figure against its §4.5 annual example

Every problem it raises holds up against the article, and I found no factual errors. It consistently credits the authors' own concessions instead of presenting them as discoveries, and it keeps its view separate from theirs. Its main weakness is what it leaves out:

- the closed-grid assumption, which bears directly on the spatial-attribution conclusion
- the mixed data years
- the funding source of the Scenario 2 load profile

None of these omissions makes what the evaluation does say wrong.
