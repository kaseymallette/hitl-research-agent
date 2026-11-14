# Claims reference list

**Article:** `article.pdf` — Garrett Alston, Nancy Love, Rabab Haider, "Data Center Cooling Choices Shift Water Impacts Across the Grid: An Integrated Water-Energy Model for Sustainable Data Center Development," arXiv:2609.25437v1 [eess.SY], 21 Sep 2026. 12 PDF pages.

**Written from:** `RUBRIC.md` and `article.pdf` only.

**Where the article ends for this purpose:** the main text (Sections 1–6, PDF pp. 1–10) **and** Appendix A (PDF p. 12). Appendix A is included because the main text points to it for the dispatch merit order (§3.1.2) and annualized WCI, and it contains three numbered tables. Acknowledgments and the reference list (p. 11) are excluded.

**Locations** are given as section number and PDF page (the PDF has no printed page numbers; p. 1 is the title page). The PDF is two-column.

**Conventions.** Quoted text is the article's exact wording (checked against text extracted from the PDF; hyphenation from line breaks removed). Unquoted text is a paraphrase. Figures are raster images; their readings below are paraphrased from the image and marked "read off the figure" where a value is not printed in the text. Where the list and the article disagree, the article decides.

**Counts:** 3 enumerated contributions (C1–C3); 11 abstract claims (AB1–AB11); 5 enumerated findings in §4 (FN1–FN5); 5 enumerated recommendations in §5.1 (R1–R5); section/subsection conclusions S1–S39; 8 figures (F1–F8); 6 tables (T1–T3, TA.1–TA.3).

---

## 1. Enumerated contributions (§1.2, pp. 2)

§1.2 frames the contribution as: "we present an integrated water–energy model that connects facility operations, grid dispatch, and water subbasin conditions to evaluate the water and energy impacts of data center development." "We then use the integrated model to evaluate the impacts of facility siting, cooling configuration, and computing workload on water risk, which we define as a depletion-based metric at the subbasin level." The model is "built using publicly available real-world data," and is "used to simulate data center growth in the state of Michigan." The enumerated items follow "Our case studies show:"

- **C1.** "Reducing direct cooling consumption can increase electricity demand and indirect consumption, highlighting why cooling choices must be evaluated across both the facility and the specific generators responding to its load."
- **C2.** "Indirect water intensity varies across months as the responding generators change, revealing temporal differences that are obscured by applying a fixed regional electricity water-intensity factor."
- **C3.** "Assigning direct and indirect consumption to their respective subbasins reveals depletion increases beyond the data center sites that would be missed by evaluating both components using only the facility's hydrologic boundary."

Related unenumerated contribution claim (§5.2, p. 10): the model "is the first to connect facility cooling configuration, grid dispatch, and subbasin-level water depletion for assessing data center sustainability." (A priority claim; not among the enumerated contributions.)

## 2. Abstract claims (p. 1)

- **AB1.** Data centers "are being developed at an unprecedented pace, yet their energy and water impacts, and the spatial and temporal distribution of these impacts, remain poorly characterized."
- **AB2.** Data centers consume water for cooling (direct) and through electricity generation (indirect).
- **AB3.** "Decisions on siting and cooling technology result in water–energy trade-offs that extend impacts beyond the facility's location."
- **AB4.** Existing assessment frameworks rely on facility efficiency metrics and average grid water intensity factors, "suppressing the temporal impacts of data center load and generation availability."
- **AB5.** Existing frameworks "attribute indirect consumption to the facility's location rather than to the generators (and corresponding hydrologic regions) that respond to the added load, misattributing the spatial impacts of data center loads."
- **AB6.** The authors develop a computational model of the data center–energy–water nexus linking facility cooling and electricity demand with hourly economic dispatch, generator-level water consumption, and monthly subbasin depletion; built on open-source data, it "resolves where and when water is consumed, and where this consumption compounds existing water risk or creates new risk."
- **AB7.** The model is applied to cooling technology selection and to proposed developments in Michigan.
- **AB8.** "Air-cooled data centers nearly halve total water consumption relative to evaporative cooling, but increase electricity demand and raise indirect water consumption by roughly one-third, shifting the water footprint from the facility to generators on the grid." (Body figures: total −44%, indirect +32%, electricity +32%; §4.1, Table 2.)
- **AB9.** "Indirect water intensity also varies by approximately 50% across months with the generators supplying the added load." (Note for the judge: the ~50% figure is not stated numerically anywhere in the body; §4.2 says indirect consumption "varies substantially" and gives the July-vs-June example. Figure 3 is visually consistent with variation of that order but the article does not compute it.)
- **AB10.** "Mapping these changes to subbasins reveals depletion increases beyond the data center sites, in regions that facility-level reporting may overlook." (Hedged: "may overlook".)
- **AB11.** "These results show that data center water and energy impacts cannot be assessed in isolation, motivating the need for integrated modeling to inform siting, design, and reporting practices."

## 3. Overall conclusions

### 3a. The five enumerated findings (§4 intro, p. 6)

Applying the model to the Michigan case studies "reveals five critical findings that these simplified approaches cannot capture":

- **FN1.** "Cooling configuration results in a water–energy tradeoff" (developed in §4.1)
- **FN2.** "Average grid water intensities cannot capture the true indirect water impacts" (§4.2)
- **FN3.** "Data center impacts extend beyond the facility site" (§4.3)
- **FN4.** "Annualized reporting obscures the underlying system conditions" (§4.4)
- **FN5.** "Water consumption magnitude alone cannot determine water risk" (§4.5)

The §4 intro also states that prior approaches "suppress the temporal impacts and misattribute the spatial impacts of data center loads," and that the findings "have direct consequences for how the water and energy footprint of data center developments should be assessed, sited, and reported."

### 3b. Section 6 Conclusion (p. 10)

- **CO1.** Assessing data center water–energy impacts "requires accounting for both direct water consumption at the facility and indirect water consumption from electricity generation."
- **CO2.** The study presents an integrated data center–energy–water model linking facility cooling, grid dispatch, and subbasin depletion.
- **CO3.** "The results show that cooling configuration shifts water consumption from the facility to electricity generation, that indirect water intensity varies monthly as the responding generators change, and that facility siting redistributes impacts across the region."
- **CO4.** "Together, these findings demonstrate that energy and water impacts cannot be assessed in isolation, and that sustainable data center development requires integrated water–energy models to assess impacts and support decision making in siting, design, and reporting practices."

### 3c. §5.1 summary statement (p. 10)

- **CO5.** "In summary, facility-level analysis and consumption volumes cannot accurately capture data center impacts. Impact assessments and tracking must move towards integrated water—energy models that can quantify impacts at a high spatial and temporal granularity, across interconnected infrastructure and natural systems."

## 4. Section and subsection conclusions

### §1 Introduction (pp. 1–2)
- **S1.** Scope 2 (indirect) consumption links energy and water impacts: siting, cooling, and energy supply decisions "result in tradeoffs across the water–energy nexus, and across spatial and temporal dimensions."
- **S2.** Cooling choices that reduce direct water can raise electricity demand and indirect water (evaporative: more direct water, less electricity; non-evaporative: the reverse); "The resulting environmental impact of a data center cannot be inferred from metrics reporting direct water consumption alone." PUE, WUE, and WCI "Together ... determine the water impact of a data center facility."
- **S3.** Impacts vary temporally and spatially; indirect consumption occurs at responding generators, possibly in different hydrologic regions.
- **S4.** Because depletion accounts for return flows and captures the share of available water actually consumed, "this study uses a depletion-based indicator to evaluate water risk"; hence "the same increase in consumption can result in different water risk values, depending on existing consumption and available water where it occurs."

### §1.1 Related Works and Research Gaps (p. 2)
- **S5.** Across prior studies, the indirect calculation "retains the same fundamental limitation: it uses the water consumption intensity of an averaged generation mix rather than identifying the generators whose output actually changes in response to that demand."
- **S6.** The limitation "persists even at higher temporal resolutions": existing assessments assume generators increase output in proportion to the observed mix, which holds only when the mix is fairly uniform, "a limiting assumption for most real-world systems."
- **S7.** Spatially, aggregating into regional intensities loses responding-generator locations, so "an assessment based on the facility location [33] or an aggregated electricity region [22] may estimate the total indirect consumption volume while misidentifying the regions in which the consumption actually occurs."

### §1.2 Contributions (p. 2)
- **S8.** "existing approaches cannot resolve which generators respond to added demand, nor the hydrologic regions in which that response's consumption and depletion occur." Contributions C1–C3 above.

### §2 An Integrated Water–Energy Model (p. 2)
- **S9.** The model comprises three coupled systems: DCF System (facility siting, capacity, hourly load, cooling, PUE, WUE; computes Scope 1 via WUE); Energy System (grid, hourly demand, generators, economic dispatch; computes Scope 2 via generator WCI; coupled to DCF via PUE); Water System (HUC boundaries, monthly baseline availability and consumption; computes depletion-based water risk at subbasin level; coupled via direct and indirect depletion).
- **S10.** Scope boundary: "indirect consumption refers only to electricity generation"; the pathways "do not constitute a complete life-cycle analysis"; Scope 3 (construction, manufacturing, supply chain) is outside the model boundary.

### §2.1 DCF System model (pp. 2–3)
- **S11.** Each facility is specified by coordinates, capacity (IT or total facility load), load profile, and cooling configuration; PUE and WUE determine facility electricity and water use; these "primarily remain fixed" but vary over time with the selected mode for multi-mode configurations.
- **S12 (§2.1.1).** IT-load representation: facility electricity = IT load × Δt × PUE (Eq. 1).
- **S13 (§2.1.2).** Facility-load representation: facility electricity = facility load × Δt (Eq. 2); IT electricity = facility electricity / PUE (Eq. 3).
- **S14 (§2.1.3).** WUE is treated as consumptive cooling water intensity (L/kWh of IT electricity); direct consumption = IT electricity × WUE (Eq. 4).
- **S15 (§2.1.4).** PUE and WUE come from the 2024 DOE *United States Data Center Energy Usage Report* [20], which gives simulated annualized ranges from thermodynamic-based models; the IT cooling system (removes heat from servers) is distinct from the heat rejection system (removes heat from the facility), and "cooling configuration" means the combination of both.

### §2.2 Energy System model (pp. 3–4)
- **S16.** The grid is a graph of buses and lines with line limits; generators have capacity limits and linear cost curves; generators map to buses via an incidence matrix; load is a bus demand vector.
- **S17 (§2.2.1).** Generators and nameplate capacities come from EIA-860 [28]; generators at a plant are grouped by technology; facilities and generators are assigned to the closest bus by Haversine distance.
- **S18 (§2.2.2).** Dispatchable generators are available to nameplate; wind uses ReEDS county-level hourly capacity factors; solar uses nearest NSRDB 4 km location (normalized GHI); no minimum generation except nuclear (95% minimum load); wind and solar can be curtailed.
- **S19 (§2.2.3).** Dispatch uses a linearized optimal power flow minimizing total system generating cost under network constraints, implemented in PyPSA and solved with HiGHS [5].
- **S20 (§2.2.4).** Monthly generator WCI (gal/MWh) comes from the EIA thermoelectric cooling water dataset (generators >100 MW), with a four-step fallback for missing data (generator value → monthly technology median → annual average of monthly technology medians → manual assignment from other sources); generator water consumption is Eq. 5. "This calculation links the Energy System to the Water System."

### §2.3 Water System model (p. 4)
- **S21.** HUC-8 subbasins are the reporting scale because they "balance spatial granularity with regional interpretability"; the model "can be resolved at other hydrologic scales, if sufficient data is available." Subbasin assignment is separate from bus assignment.
- **S22.** Monthly baseline comes from USGS National Water Availability Assessment outputs [31], aggregated from HUC-12 to HUC-8 by area-weighted means; consumption covers public supply, thermoelectric, and crop irrigation and is cumulative over upstream area; gross supply S = A + C (Eq. 6). (The reference entry [31] notes the analysis uses calendar year 2019.)

### §2.4 Water Risk (pp. 4–5)
- **S23.** Impact is computed against a baseline with no facility addition: change in generation (Eq. 7) and change in generator water consumption (Eq. 8); "only the change in generator water consumption is added to the hydrologic baseline because the USGS baseline ... already includes thermoelectric water use."
- **S24.** Direct and indirect consumption are aggregated to subbasins and converted to depth (Eqs. 9–10); baseline and facility-addition depletion are Eqs. 11–12; the change in depletion in percentage points is Eq. 13. "Throughout the calculations, the direct and indirect terms remain assigned to their respective subbasins, capturing the full spatial impacts of facility addition beyond the specific site location."

### §3 Case Study (p. 5)
- **S25.** The model is implemented with Michigan-specific data and applied to two scenarios "that illustrate its ability to evaluate different elements of data center development and its impacts."

### §3.1 Michigan Model Implementation (p. 5)
- **S26 (§3.1.1).** Michigan is four buses (Southeast, Central, West, North) joined by four corridors, each with a 6,000 MW thermal limit "selected heuristically to remain well above expected interregional power transfers and thereby prevent transmission congestion from dominating the dispatch results"; line reactance 0.10 Ω and resistance 0.01 Ω are heuristic parameters consistent with PyPSA examples.
- **S27 (§3.1.2).** Michigan has 32.4 GW of installed capacity (natural gas 44.6%, coal 19.5%, wind 11.7%, nuclear 10.8%, hydro 7.2%, solar 3.6%, biomass 1.5%, petroleum 1.3%, battery <0.1%); dispatch "generally prioritizes" wind and solar, then hydro, nuclear and natural gas, coal, biomass, petroleum. Technologies missing from EIA data get fixed WCI (Table 1). Petroleum coke gets the median steam-coal WCI. Hydroelectric (conventional and pumped) is assumed WCI = 0, against studies that use high values from reservoir evapotranspiration, because "the operation of a hydroelectric plant does not significantly change the evapotranspiration of the reservoir"; "The WCI metric is more accurate in capturing the change in resource operations due to an addition of load."
- **S28 (§3.1.3).** Load comes from 2023 hourly county profiles (Open Energy Data Initiative [15]), with each county assigned to the nearest bus by centroid Haversine distance.

### §3.2 Scenario 1 (pp. 5–6)
- **S29.** A hypothetical 200 MW IT-load facility in Oakland County, Southeast Michigan (highest concentration of operating data centers in the state [2]), using the IT-load representation so cooling affects both direct water (WUE) and electricity (PUE). Three configurations: water-cooled chiller, air-cooled chiller (both at upper endpoints of midsize ranges, "representing worst-case configurations"), and a hybrid airside economizer / water-cooled chiller (lower endpoints for air-cooled mode, upper for water-cooled mode). Daily mode: economizer when daily mean temperature ≤ 27 °C and mean RH ≤ 70% (2023 NSRDB data; thresholds from the FEMP best-practices guide [32]), otherwise chiller.

### §3.3 Scenario 2 (p. 6)
- **S30.** Three proposed hyperscale developments from FracTracker's tracker [6], with maximum demands of 2,700, 1,400, and 525 MW (combined 4,625 MW); configurations are not known, so all are assumed IT-liquid cooling with waterside economizer and water-cooled chiller at median PUE/WUE. Facility-load representation with an hourly synthetic load profile [3] (Eq. 14); PUE is used only to back out IT electricity for direct water.
- **S31.** Two siting cases: base (all three at proposed Southeast Michigan locations, concentrated) and alternate (West, Southeast, Central). Total direct water and electric load are the same across cases; locations of direct consumption differ; indirect quantities and locations "may also vary."
- **S32.** Qualifier: "this scenario is an illustrative analysis of how significant data center additions can impact water and energy systems, and does not serve as an assessment of the impacts of any specific project."

### §4.1 Cooling Configuration Results in a Water–Energy Tradeoff (pp. 6–7)
- **S33.** "Generally, configurations with lower direct water consumption (e.g., air-cooled) reduce total modeled water consumption, while increasing the relative contribution of indirect water use."
  - Water-cooled → air-cooled chiller: direct −97% (6.45 → 0.21 million m³); facility electricity +32% (3.08 → 4.06 TWh); indirect +32% (4.48 → 5.91 million m³); total −44% (10.93 → 6.12 million m³); indirect share 41% → 96.6%. "The selection of cooling configuration increased the indirect consumption, shifting the water footprint from the facility site (DCF System) to the generator sites (Energy System)."
  - Hybrid: direct 3.20 million m³ (between the two); lowest electricity (2.76 TWh) and indirect (3.98 million m³); total 7.19 million m³, higher than air-cooled but 34% lower than water-cooled. "The hybrid configuration captured the direct water savings from using the air-cooled mode, without fully absorbing the electricity and indirect water penalties."
  - "This efficiency gain comes with more complex and climate-dependent operations": economizer mode only 25% of the year; chiller >80% of days in January and August–December; largest economizer share May (68%) and June (53%). In Figure 3, May has among the lowest direct but higher indirect water; August has high direct water. The expected winter-economizer / summer-chiller pattern did not occur because both temperature and humidity conditions had to be met; the site is in IECC climate zone 5A (Cool-Humid), "where higher relative humidity restricts how often free-cooling conditions are met, despite lower temperatures."

### §4.2 Average Grid Water Intensities Cannot Capture the True Indirect Water Impacts (p. 7)
- **S34.** For water-cooled and air-cooled configurations, direct water and power are constant month to month (minor variation from month length), but "The indirect water consumption, however, varies substantially throughout the year" (e.g., water-cooled indirect "substantially higher in July than in June"). "This monthly variation does not come from variable power demand from the facility, but is driven by variation in (i) generation availability and (ii) baseline electricity demand." Per Figure 4, nuclear and hydro provide baseload near full capacity, wind and solar dispatch when available, and natural gas provides load-following.

### §4.3 Data Center Impacts Extend Beyond the Facility Site (pp. 7–8)
- **S35.** The tradeoff "has spatial implications": direct use affects the facility's subbasin while indirect use is determined by responding generators, so "cooling configuration selection also changes the spatial impacts of data center development."
  - Scenario 1: reducing direct water (e.g., to air-cooled) increases indirect consumption and depletion in other subbasins. The spatial distribution of indirect depletion "remained largely consistent" across configurations, "likely because of the highly aggregated grid model (only 4 buses and 4 transmission lines)," which "limits the ability to model variable patterns in grid congestion"; the magnitude "varied substantially," air-cooled largest and hybrid smallest (Figure 5).
  - Scenario 2, base case: the three facilities fall in two Southeast Michigan subbasins with depletion increases of 6.74% and 2.58%; indirect contributed less than 0.03% of those increases; the remaining six of the eight top subbasins see increases from indirect consumption, the top four ranging 0.81% to 1.5%, in Southwest, Southeast, North and Central Michigan. Direct consumption is 57% of the footprint and indirect 43% (Table 2), "distributed across generator subbasins elsewhere in the state." "Methodologies such as those proposed by [33] misattribute this consumption to the facility site."
  - Relocated case: direct consumption is spread over three subbasins (Western, Central, Southeastern); with the same direct total, "the largest total depletion change in any subbasin decreased to 2.78% (from 6.74%)."

### §4.4 Annualized Reporting Obscures the Underlying System Conditions (pp. 8–9)
- **S36.** In the three most-affected subbasins (Scenario 2 base), depletion "varies substantially month to month," driven by water availability interacting with baseline depletion, the load profile (direct), and generation availability and baseline demand (indirect). Depletion is highest in summer due to lower availability. The two direct-dominated subbasins show elevated depletion most of the year; the indirect-only subbasin rises in July–September "when water availability drops, baseline electric load peaks, and the marginal generators have a higher water cost." "Annualized totals for this subbasin understate depletion during these months of high water risk, and overstate depletion in other months."

### §4.5 Water Consumption Magnitude Alone Cannot Determine Water Risk (p. 9)
- **S37.** Comparing depletion increase with total depletion "shows a mischaracterization of impact when only water consumption magnitude (or depletion increase) is considered." A large increase may not be significant (HUC-8 04100002, second-ranked on increase); a small one may be (HUC-8 04050002, third on increase but second on total depletion). 04050002 has "a modest 1.48% increase" on "a higher baseline depletion of 4.4% compared to other subbasins," and the increase "occurred entirely from indirect consumption: the facility is not located near this subbasin."

### §5 Implications for Sustainable Data Center Development (p. 9)
- **S38.** "data center water impacts arise from interactions between cooling configuration, electricity demand, grid dispatch, and existing hydrologic conditions" (cooling → direct and facility electricity; dispatch → magnitude and location of indirect; subbasin conditions → depletion and risk). "An assessment that does not capture all three systems therefore obscures both the magnitude and location of a data center's water footprint."

### §5.1 Recommendations for Industry and Policy (pp. 9–10)
Presented as "Grounded in engineering modeling and real-world data"; five numbered recommendations, keyed to FN1–FN5:
- **R1. Cooling tradeoff.** Because PUE and WUE assumptions govern the tradeoff and its seasonal shifts, "any impact assessment that assumes annualized fixed values may misrepresent a facility's water and energy demands, and its seasonal variation." In Scenario 1, the air-cooled chiller's greater electricity demand "increased indirect consumption enough to offset part of that saving"; the offset depends on the responding generators, "so the same cooling configuration can produce different water outcomes in a different grid region." Without better industry-reported data, assessments "will continue to substitute broad performance ranges for real facility behavior," a gap that becomes more consequential as hybrid and liquid-cooled systems spread for AI training.
- **R2. Average grid intensities.** Indirect water intensity varies through the year; "A regional or averaged water intensity factor assigns a single water cost to all loads on the system, obscuring the true marginal water cost of adding a unit of load." Integrated models are needed to resolve which generators respond.
- **R3. Beyond the site.** Planning and siting "must consider water conditions at proposed facility sites and in the hydrologic regions where the added electricity generation may increase consumption." Relocation "can reduce the concentration of direct depletion impacts without reducing total consumption," while indirect impacts follow the grid response; "Distributing data center compute is therefore not automatically a better outcome, since the affected subbasins carry different baseline conditions."
- **R4. Annualized reporting.** Sub-annual consumption and availability data are needed; "Neither facility-level nor grid-average assessments provide sufficient visibility"; "Reporting and impact assessments should require sub-annual, subbasin-level depletion metrics rather than annualized, system-wide totals."
- **R5. Magnitude vs. risk.** "Consumption magnitude and the increase in depletion it produces cannot substitute for water risk"; risk depends on existing uses and availability in a subbasin; "Reporting frameworks for data center water impact should track total depletion, not just consumption volume or its incremental change."
- Summary statement CO5 (above).

### §5.2 Model Limitations and Future Work (p. 10)
- **S39.** The model "is the first to connect facility cooling configuration, grid dispatch, and subbasin-level water depletion for assessing data center sustainability" and is "intentionally modular." Limitations stated by the authors:
  - *DCF System:* DOE PUE/WUE are "estimated ranges rather than the true values of specific facilities"; the hybrid used fixed temperature/humidity thresholds, which "significantly simplifies" real controls (e.g., mixing cold, humid outdoor air with return air to raise winter economizer use); Scenario 2's load profile does not reflect different uses (training, inference, data I/O); workload-specific profiles are future work.
  - *Energy System:* four-region aggregation "limits the spatial resolution at which indirect water consumption can be assigned to individual generators and limits the ability to evaluate the impact of transmission congestion"; higher-resolution and sub-hourly modeling is ongoing work.
  - *Water System:* HUC-12 → HUC-8 aggregation "may average out local differences"; depletion estimates "indicate regional patterns"; assigning by location/distance "may misallocate consumption if the water is actually sourced from a different subbasin."
  - *General data:* "Outdated reporting required the analysis to combine electricity, weather, generator, and hydrologic datasets from different years," and gaps in generator water data "required substitutions that may not reflect individual generator performance."

### §6 Conclusion (p. 10)
- See CO1–CO4 above.

### Appendix A Generator and Water Consumption Intensity Data (p. 12)
- **SA.** Reports modeled installed capacity from 2024 EIA-860 (Table A.1), carrier-level marginal costs for dispatch (Table A.2), and mean annual WCI by technology, each "the arithmetic mean of the annual generator WCI values within that technology group" (Table A.3).

---

## 5. Figures

All figures are raster images. Readings marked "read off the figure" are approximate.

- **F1 — Figure 1, p. 3 (§2).** "Integrated water–energy model is composed of three systems: data center facility, energy, and water systems." Block diagram: DCF System (facility design + operation: location, IT capacity and hourly load, cooling configuration, PUE and WUE) ↔ Energy System (grid operation + dispatch: regional electricity demand, generators and transmission, economic dispatch) ↔ Water System (hydrologic impacts: monthly water availability, baseline water consumption, HUC-8 depletion-based stress), with two-way arrows between adjacent systems.
- **F2 — Figure 2, p. 3 (§2.1.4).** "Data from the 2024 DOE report on data center energy usage, showing PUE and WUE ranges by cooling configuration and data center size [20](see Figure 4.4)." Two box-plot panels (simulated PUE range ~1.0–2.5; simulated WUE range ~0–4) for many cooling configurations, colored by size (small, midsize, large-scale). Read off the figure: air-cooled/direct-expansion configurations have higher PUE and near-zero WUE; water-cooled chillers and water-cooled economizers have lower PUE but higher WUE (roughly 2–3.5); IT liquid cooling configurations show the lowest PUE. Reproduced from [20], not the authors' own results.
- **F3 — Figure 3, p. 7 (§4.1, §4.2).** "Monthly direct and indirect water consumption across cooling configurations" (Scenario 1). Stacked bars per month (direct blue, indirect grey) for evaporative (water-cooled), hybrid, and air-cooled, in million m³/month. Shows: evaporative has roughly constant direct (~0.5–0.55) plus varying indirect, total ~0.8–1.05; air-cooled is almost entirely indirect (~0.4–0.65); hybrid direct varies with operating mode (low in May/June, higher in Aug–Dec). Indirect varies month to month for all configurations (e.g., higher in July than June for water-cooled) (read off the figure).
- **F4 — Figure 4, p. 8 (§4.2).** "Monthly total generation mix across the three cooling configurations in Scenario 1." Stacked bars of total system generation (TWh, ~7.5–10.5 per month) by technology. Shows nuclear and hydro as roughly flat baseload, natural gas as the varying load-following share (largest in July/August), wind and solar varying by month; small differences between configurations at the top of each bar.
- **F5 — Figure 5, p. 8 (§4.3).** "Spatial distribution of indirect water impacts across cooling configurations." Three Michigan HUC-8 maps — (a) water-cooled chiller, (b) hybrid, (c) air-cooled chiller — colored by annual indirect contribution to depletion (0–0.14 pp). Shows the same subbasins affected in all three (similar spatial pattern), with darkest shading (largest magnitude) for air-cooled and lightest for hybrid.
- **F6 — Figure 6, p. 8 (§4.3, §4.5).** "Annual depletion components for the eight HUC-8 subbasins with the largest depletion increases under the proposed data center siting scenario." Stacked bars of baseline (grey), direct (blue), indirect (orange) depletion (%) with totals printed: 04090005 7.27; 04100002 4.26; 04050002 5.88; 04090001 2.57; 04080103 2.65; 04080201 1.69; 04050004 1.48; 04090004 1.55. The first two have increases that are almost entirely direct (baselines read off the figure ≈0.5 and ≈1.7); the other six have increases entirely from indirect; 04050002 has the largest baseline (≈4.4).
- **F7 — Figure 7, p. 9 (§4.3, §4.5).** "Scenario 2: Spatial distribution of increase in water depletion (top: a and b), and total depletion (bottom: c and d), for the base locations (left) and alternate locations (right). Facility locations are indicated by yellow dots." Panels: (a) proposed locations, increase; (b) relocated facilities, increase; (c) total depletion, proposed; (d) total depletion, relocated; color scale 0–7.5%. Shows the increase concentrated near the Southeast sites in (a) and more dispersed and lower in (b); total depletion maps (c, d) dominated by high-baseline subbasins in southwestern/southern Lower Michigan.
- **F8 — Figure 8, p. 9 (§4.4).** "Monthly HUC-8 depletion components for the three most impacted subbasins under the proposed data center siting scenario." Three panels: HUC8 04090005 (annual increase 6.74 pp), 04100002 (2.58 pp), 04050002 (1.48 pp). Shows depletion peaking in July–September in all three (read off the figure: 04090005 up to ~19%; 04100002 up to ~48% in September; 04050002 up to ~30% in August), with the first two dominated by direct and the third by indirect, whose indirect component rises in summer.

## 6. Tables

- **T1 — Table 1, p. 5 (§3.1.2).** "WCI values for generating technologies not found in EIA dataset." Values (gal/MWh): batteries 0¹; conventional hydroelectric 0¹; hydroelectric pumped storage 0¹; landfill gas 35 [12]; natural-gas combustion turbine 0 [26]; natural-gas internal-combustion engine 0 [30]; onshore wind 0 [12]; petroleum coke 687 [7, 12, 27]; solar photovoltaic 26 [12]. Footnote ¹: "Values assumed based on technology operations."
- **T2 — Table 2, p. 7 (§4.1, §4.3).** "Annual electricity and water consumption across the modeled cooling and siting cases." Columns: facility electricity (TWh), direct, indirect, total water (million m³), indirect share (%).
  - Scenario 1, water-cooled chiller: 3.08 / 6.45 / 4.48 / 10.93 / 41.0
  - Scenario 1, hybrid airside economizer / water-cooled chiller: 2.76 / 3.20 / 3.98 / 7.19 / 55.4
  - Scenario 1, air-cooled chiller: 4.06 / 0.21 / 5.91 / 6.12 / 96.6
  - Scenario 2, base locations (concentrated), 4,625 MW, IT liquid cooling (waterside economizer / water-cooled chiller): 36.22 / 70.71 / 53.41 / 124.11 / 43.0
  - Scenario 2, alternative locations, same cooling: 36.22 / 70.71 / 53.42 / 124.13 / 43.0
  - Shows the Scenario 1 tradeoff, and that relocation in Scenario 2 leaves totals essentially unchanged.
- **T3 — Table 3, p. 7 (§4.1).** "Monthly operating-mode selection for the hybrid airside economizer / water-cooled chiller configuration." Economizer / chiller % of days: Jan 10/90; Feb 25/75; Mar 19/81; Apr 33/67; May 68/32; Jun 53/47; Jul 32/68; Aug 16/84; Sep 10/90; Oct 13/87; Nov 17/83; Dec 3/97; Annual 25/75.
- **TA.1 — Table A.1, p. 12 (Appendix A).** "Modeled Michigan installed generating capacity." Capacity (MW) / plants / share (%): natural gas 14,445.7 / 58 / 44.6; coal 6,306.9 / 5 / 19.5; wind 3,777.3 / 34 / 11.7; nuclear 3,502.3 / 2 / 10.8; hydroelectric 2,327.1 / 52 / 7.2; solar 1,159.1 / 61 / 3.6; biomass 479.8 / 31 / 1.5; petroleum 410.2 / 21 / 1.3; battery storage 1.4 / 2 / 0.0; total 32,409.8 / 266 / 100.0.
- **TA.2 — Table A.2, p. 12 (Appendix A).** "Carrier-level marginal-cost assumptions used for dispatch." $/MWh: wind and solar 0; hydroelectric 15; nuclear 23; natural gas 23; coal 41; biomass 45; other generation 60; petroleum 90.
- **TA.3 — Table A.3, p. 12 (Appendix A).** "Mean annual WCI by grouped generating technology." gal/MWh: petroleum 831.65; nuclear 671.33; coal 523.95; biomass 336.00; natural gas 193.49; solar 26.00; hydroelectric 0.00; battery storage 0.00; wind 0.00.

---

## 7. Notes for the close-reading judge

These are observations about the article's own text, not judgments of the analysis. They mark places where a reading might reasonably differ.

1. **Abstract vs. body numbers.** The abstract's "nearly halve" total water corresponds to −44% in the body; "roughly one-third" more indirect water corresponds to +32%. The abstract's "approximately 50%" monthly variation in indirect intensity (AB9) has no matching number in the body text.
2. **Units of depletion change.** Eq. 13 defines the change in depletion in percentage points (pp), and Figure 8 labels the annual increases in pp; the §4.3 and §4.5 text gives the same quantities with a % sign (6.74%, 2.58%, 0.81%–1.5%, 1.48%, 2.78%).
3. **"Top four" indirect subbasins.** §4.3 says the top four indirect-only subbasins see increases from 0.81% to 1.5%; these increases are read from Figure 6 by subtraction and are not printed individually.
4. **Hedged claims.** Several conclusions carry hedges that should survive a close reading: "may overlook" (AB10), "likely because of the highly aggregated grid model" (§4.3), "generally prioritizes" (§3.1.2), "Generally, configurations with lower direct water consumption ..." (§4.1), "may misrepresent" (R1), "may estimate ... while misidentifying" (§1.1), "illustrative analysis ... does not serve as an assessment of ... any specific project" (§3.3).
5. **Scenario-specific scope.** The Scenario 1 percentages depend on worst-case (upper-endpoint) PUE/WUE for the single-mode configurations and on a four-bus Michigan grid with congestion deliberately kept from binding (§3.1.1).
