# Claims reference list

**Article:** `article.pdf` — Katakam, V.S.S., Arzumanyan, M., Lin, N., Bahadur, V. "System-scale design and analysis of desalination systems for meeting water needs of data centers." *Water Research* 308 (2027) 126748. doi:10.1016/j.watres.2026.126748. 20 pages.

**Written from:** the article alone (RUBRIC.md read for the setup only).

## Where the article ends for this purpose

- **Included:** front matter (Highlights, Graphical abstract, Abstract), Sections 1–4 (Introduction through Conclusions, pp. 2–18), all figures (Figs. 1–7), Table 1 and its footnotes.
- **Not included:** the back matter after Section 4 (CRediT statement, competing-interest declaration, acknowledgements, data availability, references). These hold no argumentative claims. The only statements there are that the authors declare no competing interests, that funding came from the Energy Institute at UT Austin, and that "Data will be made available on request".
- **Not in the PDF:** the article has no appendices. It often cites **Supplementary Information** (Sections S.1–S.4, Figs. S1–S4, Tables S2–S4). None of it is in `article.pdf`, so it is out of scope. A reading that reports values "from" those supplementary items can only be repeating what the main text says about them.

## How to use this list

- IDs: **H** = highlight, **GA** = graphical abstract, **AB** = abstract claim, **C** = contribution, **S** = section/subsection conclusion, **F** = figure, **T** = table, **CO** = overall conclusion (Section 4).
- Quotation marks show the article's wording. Text without them is a close paraphrase. Numbers are given as printed.
- Where the article disagrees with itself (for example, text against figure), the conflict is listed in the last section ("Internal inconsistencies as printed"). A reading that reports either printed value correctly is still attributing faithfully.
- The article numbers no contributions. The contributions below are the passages the article marks as its own advances ("The present study addresses…", "this is the first study…", "Importantly… a novel performance parameter", "Collectively, this establishes…").

---

## 1. Highlights (p. 1)

- **H1** — "Techno-economic assessment of desalination systems for data centre use."
- **H2** — "Novel SWUI metric introduced for data center water-stress impact assessment."
- **H3** — "RO and MVC analyzed for brackish to hypersaline PW feeds till MLD-ZLD limits."
- **H4** — "MLD and ZLD based treatment increase energy and cost by >12%."
- **H5** — "Evaporative cooling causes severe water stress with SWUI > 7."

## 2. Graphical abstract (p. 1)

- **GA1** — A schematic, with no data. It shows power input (heat, electricity) and saline water (ground water, seawater, wastewater) entering a water treatment unit (membrane-based or thermal-based). Freshwater goes through post-treatment to a data center, labelled with Water Utilization Effectiveness. Concentrate goes to waterbody disposal or minimum-to-zero liquid discharge. The output metrics are labelled Freshwater Recovery, Energy Demand, and Water Cost.

## 3. Abstract claims (p. 1)

- **AB1** — The buildout of data centers for high-performance computing and AI has increased energy demand, which raises freshwater requirements for thermal management by a similar amount.
- **AB2** — The study presents technical and techno-economic analyses of desalination systems that produce freshwater for data centers (TDS < 500 ppm).
- **AB3** — Two-stage RO, MVC, and hybrid configurations are evaluated for brackish (5000 ppm), seawater (35,000 ppm), and produced water (≥50,000 ppm) feeds.
- **AB4** — Brine is managed by conventional disposal or by minimum/zero liquid discharge (MLD, ZLD).
- **AB5** — Freshwater recovery (FR), energy consumption (Winp), and water cost (WC) are quantified for the technologies.
- **AB6** — "transitioning from conventional disposal to MLD and ZLD increased FR by 4–220% across feed salinities, while Winp and WC rise >12% and >15%, respectively."
- **AB7** — Seawater hybrid RO-MVC with MLD: FR = 736 L/1000 kg-feed, Winp = 9.4 kWh/m³-permeate, WC = 3.2 $/m³-permeate.
- **AB8** — MVC (with MLD) treating 50,000 ppm PW: FR = 753 L/1000 kg-feed, Winp = 36 kWh/m³-permeate, WC = 10.4 $/m³-permeate.
- **AB9** — A "novel performance metric, Saline Water Utilization Intensity (SWUI)" is introduced. It quantifies how data center desalination affects local water stress.
- **AB10** — "Across representative conditions, SWUI increased from 2023–2030, spanning mild to substantial stress impacts."
- **AB11** — "Higher recovery through MLD reduces SWUI by 40% in water-stressed settings, enabling effective water-resource utilization despite energy and cost tradeoffs."
- **AB12** — "Overall, this study establishes a detailed modeling framework for sustainability-driven assessment of desalination-integrated data center infrastructure."

## 4. Contributions (Section 1, pp. 4)

- **C1** — A detailed system-level design and techno-economic evaluation of desalination for data center freshwater production. It "holistically" integrates pretreatment, post-treatment, and concentrate-management costs, "each updated for present-day costs" (inflation-adjusted).
- **C2** — Conventional RO, MVC, and their hybrids are modeled and techno-economically optimized for brackish, seawater, and hypersaline PW. The analysis covers conventional, MLD, and ZLD disposal, and quantifies freshwater recovery, specific energy consumption, second-law efficiency, and water cost (including pre- and post-treatment) for each scenario.
- **C3** — Novelty claim: "From a data-center perspective, this is the first study to provide such a detailed process, thermodynamic and economic analysis of these desalination technologies across the entire brackish-to-hypersaline feed range and conventional to MLD/ZLD brine management conditions."
- **C4** — A "novel performance parameter", SWUI (L/kWh), which links desalination recovery and data center water demand to regional water scarcity.
- **C5** — SWUI is evaluated for three representative data center case studies through 2030. The evaluation captures the combined effect of cooling technique, local saline water, geographic water stress, and brine disposal strategy.
- **C6** — "Collectively", a "desalination-centered framework" (mature RO, MVC, and hybrids; recovery-dependent thermodynamic and economic performance; inflation-adjusted costs). It "goes beyond" prior studies limited to water-use projections or to waste-heat-driven, technologically nascent desalination.
- **C7** — The SWUI-based framework is said to enable identification of application-specific trade-offs to guide saline-source selection and brine-management strategy. It is also said to provide "a standard benchmark" for comparing future desalination technologies and lower-water-demand data center designs.
- **C8 (stated scope limit attached to the contributions)** — "System-level integration" here means coupling the full desalination treatment train, designed and cost-optimized to <500 ppm TDS, with an SWUI evaluation of regional water stress. "Further system-level thermal or operational integration between the desalination system and the data center is beyond scope". The article expects facility-specific operational data to extend this in future work.

## 5. Section and subsection conclusions

### Section 1 — Introduction (pp. 2–4)

- **S1.1** — Data centers are highly energy-intensive: projected rack-level loads approach ~1 MW by 2028, equivalent to 1000 US households. All of this energy becomes waste heat, so substantial onsite (direct) water can be needed for cooling, in addition to indirect water use from electricity generation. When a data center generates its own power (often with natural gas), the water for that generation counts as direct use.
- **S1.2** — The energy–water tradeoff is characterized by PUE and WUE. Direct evaporative cooling has low PUE (~1.3) but high WUE (1.7–2.5 L/kWh), which means 2–19 million L/day for mid- to hyperscale centers. Air cooling has WUE ~0.2 L/kWh but PUE 1.2–1.8. US data center water use is projected to rise 2–4-fold by 2028, to 150–270 billion L/yr. Off-grid gas-turbine sites "will exacerbate scarcity" (WUE 0.8–4.2 L/kWh).
- **S1.3** — Water must be <500 ppm TDS. Water-related obstacles to buildout "would be greatly alleviated" if saline water could be desalinated to data center standards. Feed classes: BW 1000–10,000 ppm, SW ~35,000 ppm, PW 50,000 to >200,000 ppm (PW also has valorization and mineral-recovery potential).
- **S1.4** — RO is energy-efficient and cost-effective but cannot treat hypersaline brines (>50,000 ppm) with substantial recovery, because of membrane burst pressure, fouling, and degradation. Thermal processes (MVC, MSF) are largely insensitive to feed salinity but very energy-intensive. Recent SIE advances "substantially improve" its operational stability up to ZLD.
- **S1.5** — Brine management is a critical determinant of environmental impact. Conventional discharge is ~70,000 ppm; MLD concentrates brine to ~130,000–200,000 ppm; ZLD concentrates it toward saturation (~260,000 ppm NaCl), which is attractive for inland, water-stressed regions.
- **S1.6 (gap)** — "there is very limited analysis/discussion on the potential impact of saline water sources (via desalination) in meeting demands of data centers." Existing work is limited to waste-heat thermal or thermoelectric RO systems, which carry cost, complexity, and reliability risks. That work also relies on simplified models (property and salt-rejection assumptions, constant flux, limited salinity ranges, negligible or single recovery). Its techno-economics often leave out pretreatment, brine disposal, and post-treatment costs.
- **S1.7 (gap)** — The bidirectional impacts between desalination performance and data center expansion on regional water scarcity are "largely unexplored". Significant gaps remain in techno-economic and environmental assessment of mature desalination for data centers.
- **S1.8 (gap)** — Prior MVC studies were mostly limited to a single feed and recovery. Tucker et al. overestimated evaporator mean temperature difference and missed capital-cost variation. Hybrid RO-thermal studies used simplified assumptions. "Nearly all" used cost parameters without inflation adjustment and so underpredict present-day costs.
- Contributions C1–C8 close the section.

### Section 2 — Modeling and methodology (opening text, p. 5)

- **S2.0** — The study examines commercially available RO and MVC for their technical maturity, scalability, and the data available for techno-economic analysis. Both "provide a wide range of desalination capabilities with energy-efficient operation" compared with other techniques in their category. Stream and solute mass conservation (Eqs. 1–2) hold at module, stage, and system level. Freshwater recovery RR is defined in Eq. 3 (L-permeate/1000 kg-feed).

### 2.1 — Design and thermodynamic analysis of RO and MVC (heading only; content is in 2.1.1–2.1.2)

### 2.1.1 — RO modeling framework (pp. 5–6)

- **S2.1.1a** — Two-stage RO is chosen over single-stage "for its lower energy consumption and treatment costs", which come from optimized inter-stage recovery distribution and control of stage-level pressure.
- **S2.1.1b** — Permeate concentration is modeled from the membrane rejection ratio (Eqs. 4–5). Membrane area comes from the authors' heat–mass-transfer-analogy method (Eq. 6), and a prior study is cited as giving "substantial corroboration" of the MRR-based approach. Two-stage Winp is given by Eqs. 7–8.
- **S2.1.1c** — 5% extra work input and membrane area are added "to conservatively incorporate" fouling, viscous, and circulating-pump effects.
- **S2.1.1d (validation)** — Against circulating-pump power with viscous losses (feed-side pressure drop 0.5–3 bar; BW, SW, and 50,000 ppm; RP from 30% up to a concentrate of ~75,000 ppm), the Winp method shows a mean deviation of 2.5% and a maximum of 4.8%. For the cost-optimal BW and SW two-stage systems, the net deviation is <0.06 kWh/m³-permeate.

### 2.1.2 — MVC modeling framework (pp. 6–7)

- **S2.1.2a** — MVC is modeled with two-stage compression and intercooling (Eq. 9) and heat-exchanger area by LMTD (Eq. 10), with permeate salt assumed to be zero. 5% extra Winp and heat-exchanger area are added for viscous and fouling effects.
- **S2.1.2b (conclusion)** — Higher TTD raises Winp and lowers heat-exchanger area; the opposite happens as TTD approaches 0 K. TTD is therefore "a critical design parameter that simultaneously influences Winp and AHX, suggesting an optimal operating point exists for minimizing overall water treatment cost."

### 2.2 — Technoeconomic modeling (p. 7)

- **S2.2a** — WC = [CF·ACE + AOE]/AWP (Eq. 11). RO costs follow Mo et al. (2022), post-treatment follows dos Santos et al. (2024), and 10% is added to membrane replacement for fouling.
- **S2.2b** — Two-stage RO is optimized by minimizing WC iteratively across all feasible stage-level recovery and pressure combinations, including non-ideal solution behavior, membrane selectivity, and concentration polarization. This is contrasted with prior studies that "minimize only Winp or Am" under simplified or constrained assumptions.
- **S2.2c** — MVC costs follow Swaminathan et al. and Bartholomew et al. (pretreatment is excluded for the MVC stage in the hybrid), and the optimum is found over a range of TTD. 10% of ACE is added for system integration (both RO and MVC), plus 10% of evaporator and preheater capex for fouling.

### 2.3 — Modeling impact of data center water requirements (pp. 7–8)

- **S2.3a (gap)** — "no metric directly quantifies the practical implications of data center water footprint on regional water scarcity." WUI is defined only on freshwater WUE, leaves out site-dependent supply and desalination factors, was calculated only for evaporative cooling ("no longer being considered in any significant manner"), and is not evaluated under future water-stress projections.
- **S2.3b (definition)** — SWUI = [WUE × 10⁶ / (RR × ρfi)] × (WS + 1) (Eq. 12), in L-feed/kWh. It is the saline water withdrawn per unit of IT energy, times a factor proportional to local water stress. The first factor is SWUE, which depends on cooling (WUE) and on desalination (RR, which depends on feed and disposal strategy). Mainly direct WUE is used.
- **S2.3c** — WS comes from the Aqueduct Water Risk Atlas: the ratio of projected demand to renewable supply, on a 0–5 scale. 1 is added, consistent with WUI, so SWUI is never zero. WS represents the regional water-stress context, not stress on the saline source. The freshwater produced could otherwise serve competing demands. SWUI is "a first-order water utilization intensity metric" of relative implications, "rather than the depletion or intrinsic sustainability of the saline feed source itself."
- **S2.3d** — SWUI rises monotonically with SWUE and WS. The linear form is justified because (1) SWUI is not directly measurable, so a nonlinear form "would add arbitrariness rather than remove it", and (2) it keeps SWUI consistent with WUI for direct comparison.
- **S2.3e (conclusion)** — "SWUI is a practical, easily applicable and unified metric" that captures the integrated effects of desalination, available saline resources, and thermal management on local water stress. Sensitivity of the linear, quadratic, and exponential forms is in Table S.2 (SI). The derivation of Eq. 12 is in SI Section S3.

### 2.4 — Methodology and input parameters (pp. 8–10)

- **S2.4a** — Because ">93–97%" of the dissolved salt in pretreated BW, SW, and PW is NaCl, all streams are modeled as NaCl solutions. This is called "a reasonable approach" supported by recent studies in which pretreatment makes the impact of fouling and scaling "almost negligible". Pretreatment: UF, NF, coagulation–flocculation. Post-treatment: UV and electro-deionization.
- **S2.4b (stated limitation and future work)** — Future work should use realistic industrial feeds (multivalent ions, sulfates, silica, scaling precursors) and study fouling, scaling, and flux decline. It may need more pretreatment (softening, pH adjustment, antiscalant), especially for high-recovery RO and MVC. Pretreatment selection is site- and feed-specific.
- **S2.4c** — BW and SW use two-stage RO to conventional disposal, and hybrid RO-MVC for MLD and ZLD. PW (≥50,000 ppm) uses MVC only, because RO is of limited suitability. Design space: stage recovery and pressure (0–ΔPmax) for RO; TTD (0–5 K) for MVC. Excess pressure is 0–30 bar. ΔP > 65 bar is infeasible and excluded. Only systems with ≥100 L-permeate/1000 kg-feed are considered. Second-law analysis is in SI (Fig. S1, Section S.2).
- **S2.4d (case studies)** — Case 1: inland, mild WS (<3), brackish water, Project Rose, Longview TX. Case 2: coastal, substantial to severe WS (3–5), seawater, Project Gladys near Corpus Christi. Case 3: semi-arid/arid, severe WS (>4), produced water near ZLD for mineral extraction, Project Crusoe, Abilene (near the Permian). PW feed: 91,000 ppm, the Permian average from a USGS report (wells range from 7000 to >200,000 ppm; the Table 1 footnote says 85 wells).
- **S2.4e** — The analysis "can be used to evaluate the impacts of data center deployment at any location" if WS, saline-water characteristics, and disposal strategy are known. The cases were chosen for their diversity, which spans mild to severe water stress impact. The focus is planned or under-development hyperscale facilities.
- **S2.4f** — WS is averaged over pessimistic, optimistic, and business-as-usual climate scenarios. High and low WUE projections (Eqs. 13–14) are fitted to LBNL data through 2028 (R² > 0.99) and extrapolated "minimal[ly]" to 2030. WUE is "observed to increase in the near future due to increased shift towards hyperscale data centers." The LBNL limits are adopted because they average across many scenarios from "a holistic and rigorous simulation database".
- **S2.4g** — Costs are normalized to 2026 dollars with CEPCI. Membrane properties are similar to those in recent modeling and pilot studies.

### Section 3 — Results and discussions (heading only; no text of its own before 3.1)

### 3.1 — Freshwater yield, energy and cost metrics (pp. 10–11)

- **S3.1a (recovery)** — Brackish feeds give the highest yield, ">900 L/kg-feed" (printed so; Fig. 4a gives 931–986 per 1000 kg). Brackish recovery rises "about 6%" from conventional disposal to ZLD (260,000 ppm). Recovery falls with feed concentration, "75% reduction for MLD upper limit disposal" from seawater toward hypersaline.
- **S3.1b** — The lowest yields are MLD for 125,000–150,000 ppm PW (little dewatering is needed to reach 130,000–200,000 ppm) and conventional disposal for 50,000 ppm PW (only up to 70,000 ppm). These are ">74% lower" than the maximum RR (brackish water at the ZLD upper limit).
- **S3.1c (implication)** — Such large drops in recovery "would result in increased saline water withdrawal by data centers", and so increased regional water stress depending on local conditions (developed further in 3.3).
- **S3.1d (energy)** — BW and SW Winp is far lower than PW Winp, but it "increases drastically" from conventional disposal to ZLD: more than double for BW and eight-fold for SW, because of the energy-intensive MVC stage. "Consequently, MLD and ZLD systems, while more sustainable, inherently demand higher energy than conventional brine disposal."
- **S3.1e** — For PW at 50,000–150,000 ppm with MVC, the Winp increase is only 1.2–1.6× (lowest to ZLD), because thermal desalination is insensitive to feed. Winp therefore changes little between PW feeds for a given disposal strategy. MVC second-law efficiency rises with feed concentration (Fig. S2).
- **S3.1f** — In general, Winp "remains highly sensitive" to feed and recovery because of non-ideal behavior (osmotic pressure, boiling-point elevation). Winp rises "about 50–400%" from brackish to seawater across scenarios. Winp and WC are "almost an order of magnitude higher" for PW than for BW and SW at the same disposal condition, which "clearly highlights the substantial energy and cost requirements for treating hypersaline feeds under MLD and ZLD".
- **S3.1g (cost)** — WC rises 30–290% from brackish to seawater, because higher osmotic pressure and concentration polarization raise membrane area and push the optimal ΔP toward 65 bar. For PW, WC rises "slow[ly]… but marked[ly]" from 50,000 to 150,000 ppm (compressor pressure ratio from boiling-point elevation, brine disposal costs). WC "was found to asymptotically increase beyond 200,000–230,000 ppm" (citing Katakam et al., n.d.): MVC's energy advantage does not keep WC constant.
- **S3.1h** — Going to MLD and ZLD raises WC by 90% (BW) and 470% (SW) from conventional disposal to ZLD, consistent with the energy trends, because of the costly MVC stage. PW shows a similar nonlinear increase.
- **S3.1i (trade-off)** — At 91,000 ppm, WC falls from MLD lower to MLD upper before rising again at ZLD, because an "almost 2x increase in freshwater recovery" outweighs the higher annual costs. The same happens for 50,000 ppm between conventional disposal and MLD lower. The benefit disappears at MLD upper and ZLD, where the rise in AOE and ACE dominates.

### 3.2 — Comprehensive process-level results for selected case studies (pp. 11–14)

- **S3.2a** — Two cases are detailed as typical applications: (1) hybrid RO-MVC seawater to 130,000 ppm (MLD, Fig. 5), and (2) MVC for mildly hypersaline PW to 200,000 ppm (MLD, Fig. 6).
- **S3.2b (hybrid, RO stage)** — RO dewaters seawater to 75,000 ppm. Stage 1 runs well below 65 bar and stage 2 approaches the limit. The pressure redistribution between stages enables energy-efficient operation. The second stage's higher solute passage (within limits) increases flux, lowers area, and lowers cost. RO: RP = 0.53, ~325 ppm permeate, 1.6 kWh/m³ and 0.6 $/m³ (normalized to total hybrid permeate). Membrane and electricity are the main RO cost items. Pretreatment and post-treatment "contribute up to 30% of the overall water cost", "clearly highlighting the non-negligible contribution" and the importance of including them. RO second-law efficiency is 51.2%, and its main irreversibility is permeate depressurization through the membrane.
- **S3.2c (hybrid, MVC stage)** — MVC dewaters to 130,000 ppm at TTD = 9.2 K: RP = 0.42, 7.8 kWh/m³-permeate, second-law efficiency 8.7%, 2.6 $/m³. Electricity and evaporator are the main MVC costs.
- **S3.2d (hybrid, overall)** — "the hybrid two-stage RO-MVC MLD desalination system will provide 736 liters of freshwater suitable for data center end use, for every 1000 kg of seawater", at 9.4 kWh/m³ (overall second-law efficiency 15.9%) and 3.2 $/m³. Hybrid Winp and WC are "dominated by" MVC.
- **S3.2e (hybrid, sensitivity)** — In the Monte Carlo analysis (±20%), MVC parameters influence WC more than RO parameters. Electricity cost, then MVC evaporator cost, then compressor cost "significantly influence" WC. This "corroborates" the TTD-based cost-optimization approach. WC also depends strongly on discount rate, plant life, and MLD brine-management cost, then RO membrane and RO pump costs. Among technical parameters, MVC compressor efficiency, then RO pump efficiency, drive the economics, with an efficiency–cost trade-off for the compressor (lower efficiency raises energy cost; higher efficiency raises compressor capex).
- **S3.2f (PW MVC case)** — Cost-optimal TTD = 10 K, close to the hybrid's; a similar TTD was obtained for the 50,000 ppm case. 50,000 ppm PW to 200,000 ppm gives "754 liters of freshwater… per 1000 kg of PW treated", Winp 36 kWh/m³, and a "low" second-law efficiency of 6.8% from phase-change separation. Most exergy destruction is in the evaporator–condenser (finite-temperature-difference heat transfer), followed by the compressor.
- **S3.2g** — WC is 10.4 $/m³. Compressor electricity "significantly drives" cost, followed by evaporator–condenser cost, "further validating the hypothesis and cost-optimization approach in Section 2.1.2 on the critical role of TTD". In the Monte Carlo analysis, electricity cost, then evaporator cost and compressor cost, have the strongest influence. WC is "highly sensitive" to discount rate and plant life, followed by compressor efficiency.

### 3.3 — SWUI results for representative emerging data centers (pp. 14–16)

- **S3.3a** — SWUI is classed following WUI: 0–9 bands, with values above 9 meaning severe water-stress impact. Medium WUE is the mean of high and low.
- **S3.3b** — "SWUI values increase across all case studies through 2030 mainly due to rising WUE."
- **S3.3c** — Case 1 (brackish, conventional) "only reaches moderate SWUI based water stress impact by 2030" and has the lowest SWUI of all cases, because of high RR (931.2 L/kg-feed as printed) and low WS (1–3).
- **S3.3d** — Case 3 (ZLD PW) "falls in the lower moderate water stress impact SWUI range" because of high WS (4–5) and lower RR (~653).
- **S3.3e** — Case 2 conventional seawater is near the upper moderate limit, "crossing into substantial water stress impact range by 2029", because of low RR (482) and high WS (3–5).
- **S3.3f (key comparison)** — Although Case 3 has higher WS and a hypersaline feed, its SWUI is lower than that of Case 2 (conventional SW), because Case 2's lower recovery requires more saline withdrawal. "These results clearly demonstrate the SWUI parameter's ability to assess water-related impacts… using a scenario-specific and multifactorial approach." The previous WUI metric "would have suggested Case 3. to be more intensive and environmentally detrimental" than Case 2.
- **S3.3g (mitigation)** — Hybridizing Case 2 with MVC up to 200,000 ppm MLD "will reduce SWUI by about 40%". This brings it below Case 3, to minimal to low-moderate impact through the decade. MLD also supports circular-economy incentives instead of "hazardous disposal".
- **S3.3h (trade-off)** — "These results highlight the previously un-analyzed tradeoffs" for MLD and ZLD in data center applications: higher recovery increases energy and cost but decreases water-stress impact. This could be especially useful for inland and arid sites with plentiful wastewater and limited disposal options.
- **S3.3i** — Desalination energy is "generally two orders of magnitude lower" than typical data center power consumption. This "suggests" the added energy and carbon from MLD/ZLD "would be negligible" compared with the end use, and that the small increase would enable effective water-resource use, viable mineral extraction, and relief of local hydrological impacts.
- **S3.3j** — Earlier formulations (WUI/WUE) "cannot" capture these desalination effects. They would give "an indifferent result for Case 2" between conventional and MLD/ZLD, and would underpredict water-stress impact "by a factor of (10⁶/(RR×ρfi))", "substantially overestimating" sustainability, especially at high recovery (Cases 1 and 3). The SWUI framework "could be utilized as key inputs" to a data center resource-effectiveness model (DCRE).
- **S3.3k (interpretive caveats)** — Higher SWUI for Case 2 "do[es] not imply that seawater withdrawal depletes freshwater resources". It reflects the alternative uses of the freshwater in that region. Including recovery means the framework "inherently incentivizes higher-recovery MLD/ZLD strategies". For Case 3, PW is a byproduct of water-intensive hydraulic fracturing in water-stressed basins, so freshwater availability "remains an important sustainability consideration". Still, Case 3 "sees substantial benefit" from its higher recovery.
- **S3.3l (sensitivity)** — In Table S2 (SI), comparing linear, quadratic, and exponential WS forms for 2023–2030 mean SWUI, the nonlinear forms show more overlap between cases, but "the overall case-study ranking… is preserved across all three formulations, corroborating the mathematical considerations" of SWUI.
- **S3.3m (evaporative cooling)** — With evaporative cooling (WUE 1.7–2.5 L/kWh), "only brackish water desalination in Case 1 maintained SWUI below the severe water stress threshold (SWUI = 7.2)". All other scenarios had substantially higher SWUI (12.9–22.3). This "underscores the intensified water stress impact" of water-intensive cooling in scarce or arid regions (Cases 2 and 3). Using WUE alone would give "an indifferent water stress impact result between the three cases", which is only qualitative.

## 6. Overall conclusions (Section 4, pp. 17–18)

- **CO1** — The study models and techno-economically optimizes two-stage RO and MVC for data center water: BW 5000, SW 35,000, PW "50,000 and 90,000 ppm", with CD (70,000), MLD (130,000–200,000), and ZLD (200,000–260,000 ppm).
- **CO2** — For BW and SW, hybrid RO-MVC to MLD/ZLD increased energy and cost by 53–715% and 44–470%, respectively, compared with conventional RO to the CD limit.
- **CO3** — For PW, MLD/ZLD MVC-only treatment "limited energy consumption and cost increase by <63% and <18%", compared with MVC at the CD limit.
- **CO4** — Case studies: MLD hybrid RO-MVC seawater (736 L/1000 kg-feed, 9.4 kWh/m³, 3.2 $/m³, dominated by MVC costs). MVC for 50,000 ppm PW to MLD (753.7 L/1000 kg-feed, 36 kWh/m³, 10.4 $/m³, dominated by electricity and evaporator–condenser costs).
- **CO5** — SWUI was formulated to combine WUE and desalination recovery with operating conditions to assess the regional water-stress impact of data centers. It was calculated for three representative data centers.
- **CO6** — Projected SWUI rose from 2023 to 2030 because of rising WUE (the average across all heat-rejection methods).
- **CO7** — The water-stress impact of desalination-integrated data centers "depends on regional water stress and desalination recovery."
- **CO8** — SWUI "provides a unified assessment capability that previous WUE/WUI-based frameworks could not capture, particularly for distinguishing conventional disposal from MLD/ZLD desalination pathways."
- **CO9** — "Overall, this study establishes a desalination benchmark linking technical feasibility, cost competitiveness, and regional water-stress implications of brackish-to-hypersaline water treatment for data-centers." The framework "supports sustainable data-center deployment and siting decisions" and gives a basis for comparing future developments.

## 7. Figures

- **F1 (p. 3, Fig. 1)** — A schematic of desalination for data centers, with no data. Power input (heat, electricity) and saline water (ground water, seawater, wastewater) enter a water treatment unit (membrane-based or thermal-based). Freshwater goes to the data center and to "Energy" and "Agricultural Sectors". Concentrate goes to waterbody disposal or minimum-to-zero liquid discharge. It supports Section 1's framing of feeds, technologies, and brine strategies.
- **F2 (p. 5, Fig. 2)** — Process schematics, with no data. (a) Two-stage series RO: a stage-1 pump, PXs, a stage-2 pump; the stage-1 concentrate feeds stage 2; permeate from both stages is combined; concentrate is depressurized through the PX. (b) MVC with two-stage compression: pretreated feed passes two feed preheaters into the evaporator–condenser; distillate vapor goes through low- and high-pressure compressors with an intercooler and returns as condensate; permeate and concentrate exit through the preheaters.
- **F3 (p. 9, Fig. 3)** — WUE (L/kWh) against year, 2023–2030: LBNL "higher" and "lower" WUE data (to 2028), interpolated fits (2023–2028), and extrapolated trends (2028–2030), with the band shaded. Both rise from ~0.38 L/kWh in 2023, to ~0.51 (high) and ~0.47–0.48 (low) by 2030. The text gives R² > 0.99 and Eqs. 13–14. It shows that WUE is projected to rise, which is the driver of rising SWUI.
- **F4 (p. 10, Fig. 4)** — Heat maps of cost-optimal performance by feed (rows) and disposal (columns: CD 70,000; MLD lower 130,000; MLD upper 200,000; ZLD 260,000 ppm). Blank cells are infeasible or not applicable.
  - (a) Freshwater per 1000 kg feed (L): BW 931 / 967 / 980 / 986. SW 482 / 736 / 830 / 870. PW 50,000: 254 / 618 / 754 / 812. PW 91,000: – / 300 / 547 / 653. PW 125,000: – / – / 377 / 522. PW 150,000: – / – / 251 / 425.
  - (b) Specific energy (kWh/m³): BW 1.5 / 2.3 / 2.9 / 3.4. SW 2.1 / 9.4 / 14.0 / 17.1. PW 50,000: 25.5 / 28.5 / 36.0 / 41.6. PW 91,000: – / 30.6 / 36.1 / 41.6. PW 125,000: – / – / 36.2 / 41.7. PW 150,000: – / – / 36.2 / 41.7.
  - (c) Water cost ($/m³): BW 0.7 / 1.0 / 1.2 / 1.3. SW 0.9 / 3.2 / 4.3 / 5.1. PW 50,000: 10.1 / 8.9 / 10.4 / 11.9. PW 91,000: – / 11.1 / 10.8 / 12.2. PW 125,000: – / – / 11.7 / 12.6. PW 150,000: – / – / 13.3 / 13.4.
  - It supports S3.1a–i, AB6–AB8, and CO2–CO3.
- **F5 (pp. 12–14, Fig. 5, three parts)** — Cost-optimal two-stage RO-MVC hybrid, MLD seawater (35,000 ppm).
  - (a) Schematic with values: pretreated feed 1000 kg at 35,000 ppm; pump ΔP = 28.7 bar. Stage 1: ΔP = 53 bar, Am = 5.2×10³ m², permeate 335 kg at 275 ppm, interstage 665 kg at 52,500 ppm. Booster ΔP = 6.5 bar. Stage 2: ΔP = 65 bar, Am = 6.1×10³ m², permeate 205 kg at 400 ppm. RO permeate 540 kg at 325 ppm. RO concentrate (MVC feed) 460 kg at 75,000 ppm. MVC feed is saturated liquid at 50 °C. Preheater 1 is 180 m² and preheater 2 is 440 m². Evaporator–condenser TTD = 9.2 °C, 1.4×10³ m². MVC permeate 193 kg at 0 ppm. Concentrate 267 kg at 130,000 ppm.
  - (b) Cost breakdown: RO 16%, MVC 84%. RO portion: Electricity 35%, Pretreatment 16%, Membranes 16%, Pump 12%, Miscellaneous 12%, Posttreatment 8%, Pressure Exchanger 2%. MVC portion: Electricity 45%, Evaporator 26%, Compressor-Preheater 15%, Miscellaneous 8%, Brine Disposal (labelled "ZLD") 6%.
  - (c) Monte Carlo (±20% inputs), box plots of water-cost deviation (%, axis ±~6–7%). The order on the axis, from widest to narrowest spread as plotted: Electricity Cost, Discount Rate, MVC Evaporator Cost, Plant Life, MVC Compressor Efficiency, RO Pump Efficiency, MVC Compressor Cost, MLD Brine Management Cost, Pretreatment Cost, RO Membrane Cost, RO Pump Cost, Post-treatment Cost, RO Membrane Replacement Cost, RO Pressure Exchanger Cost. The electricity-cost spread is the widest.
  - It supports S3.2b–e, AB7, and CO4.
- **F6 (pp. 15–16, Fig. 6, three parts)** — Cost-optimal MVC, 50,000 ppm PW to MLD.
  - (a) Schematic: pretreated feed 1000 kg at 50,000 ppm. Preheater 1 is 400 m² and preheater 2 is 130 m². Feed is saturated liquid at 50 °C. Evaporator–condenser TTD = 10 °C, 4.9×10³ m². Permeate 750 kg at 0 ppm. Concentrate 250 kg at 200,000 ppm.
  - (b) Cost breakdown: Electricity 50%, Evaporator 29%, Miscellaneous 11%, Compressor-Preheater 8%, Brine Disposal (labelled "ZLD") 1%, Pretreatment <1%.
  - (c) Monte Carlo water-cost deviation (%, axis ±10%), in order: Electricity Cost, Evaporator Cost, Compressor Efficiency, Discount Rate, Plant Life, Compressor Cost, Pretreatment Cost, MLD Brine Management Cost. Electricity has the widest spread.
  - It supports S3.2f–g, AB8, and CO4.
- **F7 (p. 17, Fig. 7, two parts)** — SWUI for the three case studies.
  - (a) Projected SWUI bands (L-feed/kWh-elec) for 2023–2030. Background impact classes: Zero–Low 0–3, Moderate 3–6, Substantial 6–9, High 9+. Bands, from lowest to highest: Case 1 conventional brackish (~0.8 → ~2.2); Case 2 MLD seawater; Case 3 ZLD Permian PW; Case 2 conventional seawater (top edge from ~4.6 in 2023 to ~6.2 in 2030). All bands rise over time. A dashed line, "Average Direct Evaporative Cooling SWUI (Case 1)", sits at ~7.2.
  - (b) 2030 SWUI by WUE projection (rows High / Mid / Low) and climate scenario (columns Opt. / BAU / Pess.). Bracketed values are direct evaporative cooling.
    - Case 1 conv. brackish: High 1.1 (5.4), 1.7 (8.1), 2.2 (10.7). Mid 1.1 (4.6), 1.6 (6.8), 2.1 (9.1). Low 1 (3.7), 1.5 (5.6), 2.1 (7.5).
    - Case 2 conv. seawater: High 4.2 (20.3), 5.2 (25.3), 6.2 (30.4). Mid 4.1 (17.2), 5 (21.5), 6 (25.8). Low 3.9 (14.1), 4.8 (17.7), 5.8 (21.2).
    - Case 2 MLD seawater: High 2.4 (11.8), 3. (14.7), 3.6 (17.7). Mid 2.3 (10), 2.9 (12.5), 3.5 (15). Low 2.3 (8.2), 2.8 (10.3), 3.4 (12.3).
    - Case 3 ZLD Permian PW: High 3.7 (17.8), 4 (19.8), 4.4 (21.6). Mid 3.6 (15.2), 3.9 (16.8), 4.3 (18.3). Low 3.4 (12.5), 3.8 (13.8), 4.1 (15).
  - It supports S3.3b–m, AB10–AB11, H5, and CO6–CO8.

## 8. Tables

- **T1 (p. 8, Table 1: "Key design, operation and cost parameters in this study")**
  - Process: feed 200 m³/hr. Feed concentrations: 5000 (BW), 35,000 (SW), 50,000 (mild hypersaline PW), 91,000*–150,000 ppm (hypersaline PW). Feed temperature 25 °C. Permeate <500 ppm. Concentrate: 70,000 (conventional#), 130,000–200,000 (MLD), 200,000–260,000 ppm (ZLD).
  - RO: A = 4.2×10⁻¹² m³/Pa-m²-s; B = 3.5×10⁻⁸ m³/m²-s; MRR 0.99; max ΔP 65 bar; ηP 80%; ηPX 96%.
  - MVC: preheater U = 1.18 kW/m²-K; evaporator–condenser inlet temperature "50 K" (as printed); TTD 0–10 K; ηcomp 0.8.
  - Techno-economic: load factor 0.9; membrane 48 $/m²; pump 74 $/(m³-bar/hr); PX cost 4369.1(ṁfe/ρfe)^0.58; interest 8%; lifetime 20 yr; system integration 10% (ACC); PIF 1.4; membrane replacement 11% of membrane capex; electricity 0.14 $/kWh; preheated feed mixer 503.2 $/(L/s); intake and pretreatment 4418 $/(m³-feed/hr); concentrate handling 0.073 $/m³ (conventional) and 0.44 $/m³ (MLD/ZLD); pressure vessels 20% of membrane capex; post-treatment 0.41 $/m³ capital + 0.03 $/m³ operating.
  - Footnotes: * mean PW concentration from 85 USGS Permian wells. # based on typical SWRO brine and maximum conventional-RO concentrate TDS. & other RO inputs in Katakam & Bahadur 2025. $ NaCl and vapor properties and heat-transfer correlations from Thiel et al. and El-Dessouky & Ettouney. @ other cost parameters from Mo et al. and Swaminathan et al., normalized to 2026 dollars with CEPCI (equations in SI S.4).
  - It shows the inputs behind all results. It carries no result claims.
- No other tables are in the main text. Tables S2–S4 are in the SI (out of scope).

---

## Internal inconsistencies as printed

These are recorded so the close-reading judge doesn't score a faithful report of one printed value as an error. They are not a judgment of the article's argument.

1. **50,000 ppm PW MLD recovery:** 753 L (abstract, AB8), 754 L (Section 3.2 and Fig. 4a), 753.7 L (Conclusions, CO4), and permeate 750 kg (Fig. 6a).
2. **Abstract "WC rise >15%" (AB6) and Highlight "energy and cost by >12%" (H4)** against the article's own data. Fig. 4c shows WC falling for 50,000 ppm PW from CD (10.1) to MLD lower (8.9), and for 91,000 ppm from MLD lower to upper (S3.1i). The Conclusions give PW cost increases as "<18%" (CO3).
3. **PW feeds in the Conclusions:** "50,000 and 90,000 ppm" (CO1), while Table 1 and Fig. 4 also include 125,000 and 150,000 ppm, and the case-study PW is 91,000 ppm.
4. **TTD range:** 0–5 K in the Section 2.4 text, 0–10 K in Table 1. The cost-optimal TTDs reported are 9.2 K and 10 K.
5. **Units:** brackish yield ">900 L/kg-feed" and RR "931.2 L/kg-feed" / "653 L/kg-feed" in the text, against L/1000 kg in figures and definitions. Table 1 gives the evaporator inlet temperature as "50 K", while Figs. 5a and 6a show 50 °C.
6. **Hybrid freshwater total:** Fig. 5a permeates add up to 540 + 193 = 733 kg, against 736 L stated (and RO RP printed as 0.53 against 540/1000).
7. **Severity thresholds for SWUI:** the text says values "above 9" are severe (S3.3a; Fig. 7a "High water stress impact (9+)"), but S3.3m calls SWUI = 7.2 "the severe water stress threshold". H5 says SWUI > 7 is "severe".
8. **Case 1 class:** the text says Case 1 "reaches moderate" impact by 2030 (S3.3c), but Fig. 7b's 2030 values for Case 1 (1.0–2.2) fall in the 0–3 Zero–Low band of Fig. 7a.
9. **Sensitivity rankings:** the text for Fig. 5c names electricity, then MVC evaporator cost, then compressor cost. The plot orders Electricity, Discount Rate, MVC Evaporator Cost, Plant Life, MVC Compressor Efficiency, RO Pump Efficiency, MVC Compressor Cost. For Fig. 6c the text names electricity, then evaporator and compressor cost, then discount rate and plant life, then compressor efficiency. The plot orders Electricity, Evaporator Cost, Compressor Efficiency, Discount Rate, Plant Life, Compressor Cost.
10. **Cost pie label:** both MLD cases (Figs. 5b and 6b) label brine disposal as "(ZLD)".
11. **Pretreatment and post-treatment share:** the text says they are "up to 30% of the overall water cost" (S3.2b). Fig. 5b shows Pretreatment 16% + Posttreatment 8% within the RO slice, and RO is 16% of the total.
12. **Citations:** two citations are printed as numbers in an author–year article ("USGS report[14]" in 2.4, "WUI metric for data centers[1]" in 3.3). There are also duplicated reference entries (Yuan et al. 2023a/b; Onishi et al. 2017 cited twice).
