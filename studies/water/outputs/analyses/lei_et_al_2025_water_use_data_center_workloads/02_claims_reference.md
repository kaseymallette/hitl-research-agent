# Claims reference: Lei et al. (2025)

Article file: `lei_et_al_2025_water_use_data_center_workloads.pdf`  
Title: *The Water Use of Data Center Workloads: A Review and Assessment of Key Determinants*  
Authors: Nuoa Lei, Jun Lu, Arman Shehabi, and Eric Masanet.

## Scope and use

This inventory is based only on the supplied article PDF, independently of any close reading or argument evaluation. It records the authors' claims, definitions and methodological conclusions, including qualifications; it does not evaluate their validity. All entries are paraphrases, including descriptions of images. IDs identify reference items, not importance or scores. Repeated claims remain separately identifiable where needed for abstract, contribution, section-conclusion, and visual coverage.

**Endpoint:** both the main article and the Supplementary Information (SI) embedded in this PDF are included. The main substantive text ends with §5 on manuscript p. 28 (PDF p. 29); main references end on manuscript p. 31 (PDF p. 32). SI substantive material ends with §S10 and Table S10 on SI p. 27 (PDF p. 59); its references end on SI p. 28 (PDF p. 60), the end of the supplied PDF. Acknowledgements, the supporting-information availability statement, and bibliographies add no separate scientific conclusion. The repository cover page and SI title page add no substantive claims. No externally linked code, data, or cited work was opened.

**Locations:** PDF page numbers count the repository cover as page 1. Main manuscript page = PDF page minus 1; SI page = PDF page minus 32. Locations below give both where useful. Section headings identify passages even when pagination differs in another version.

**Units and direction:** the workload measure is SPECpower_ssj 2008 `ssj_ops`, not an arbitrary service, AI query, or token. Overall and facility water use are expressed as L/ssj_ops. Server electricity per workload is modeled in kWh/ssj_ops; several figures display milliwatt/ssj_ops as printed. Higher server workload efficiency means *less* server electricity per workload. PUE is facility electricity divided by IT electricity; WUE-site is onsite water divided by IT electricity; WUE-source includes onsite and electricity-related water divided by IT electricity; WCF is grid water consumption per kWh generated. Water use here means consumption, not withdrawal, with the operational categories explicitly specified by the authors.

## Abstract claims

Location for A01–A08: Abstract, manuscript p. 1, lines 15–25 (PDF p. 2).

- **A01.** Data center water use is becoming globally more important with the rapid growth of digitalization and artificial intelligence.
- **A02.** The study analyzes determinants of water consumed per workload, measured in liters per workload, to guide water-saving strategies.
- **A03.** The findings reveal workload-level water-use variation exceeding 10,000-fold.
- **A04.** This variation is driven in part by differences exceeding 1,000-fold in water consumption per kWh of server electricity consumed.
- **A05.** Approximately tenfold differences in server workload efficiency also drive the workload-level variation.
- **A06.** Determinants are ranked, in order: server efficiency; electrical grid WCF; server utilization; cooling system type; infrastructure efficiency; climate zone; inactive server percentage; server refresh cycle.
- **A07.** There is no single recipe for minimizing water use; optimal outcomes require tailored combinations of determinants.
- **A08.** The analysis fills critical knowledge gaps by identifying water-use determinants and exploring achievable minima under diverse site-specific constraints.

## Explicitly enumerated contributions

The four contribution bullets appear in §4, manuscript p. 25, lines 5–24 (PDF p. 26). They are distinct reference items even where the section inventory repeats them.

- **C01 — Workload metric.** A comprehensive workload-level water-use metric integrates PUE, WUE-site, WCF, and server workload efficiency. It enables consistent comparisons across facilities with differing site characteristics and offers a route toward standardized reporting, currently inconsistent in scope, quality, and granularity.
- **C02 — Direct and indirect scope.** A holistic analysis covers onsite humidification, adiabatic cooling, and cooling towers, alongside upstream water for electricity fuel production, processing, and transportation and water at electricity generation. This lays a foundation for integrated water-saving strategies, beyond prior studies concentrating primarily on one side of the boundary.
- **C03 — Parametric analysis.** Extensive analysis covers server efficiency, grid WCF, utilization, cooling technology, infrastructure efficiency, climate, inactive servers, and refresh cycles, providing actionable insights and tailored water-reduction strategies under diverse conditions.
- **C04 — Server workload efficiency.** Incorporating server workload efficiency and its determinants into water use per workload provides a foundational framework for understanding and improving water use for different digital services and supporting policymakers and operators concerned with direct and indirect consumption.

## Main-text section and subsection conclusions

### M01 — §1 Introduction

Location: manuscript pp. 2–5 (PDF pp. 3–6), especially the gap bullets on pp. 3–4 and closing paragraphs on pp. 4–5.

- **M01a.** Direct cooling/conditioning consumption and indirect electricity-generation consumption both make data center water use consequential, particularly for local scarcity and conservation. Illustrations include 355 million gallons at Google's The Dalles facilities in 2021 (29% of city consumption), and cited generation intensities of 0.18–2.0 L/kWh for thermoelectricity and 0.67–1194 L/kWh for hydropower. These are background examples, not new estimates from this analysis.
- **M01b.** WUE-site and WUE-source are simple and increasingly reported, but neither incorporates hardware efficiency or computing performance. They therefore cannot compare water use across data centers with differing workload quantities and efficiencies.
- **M01c.** Four gaps motivate the study: company reporting is uneven and insufficiently detailed about determinants; prior cooling/PUE/WUE studies either omit indirect consumption or aggregate infrastructure efficiency too coarsely; regional totals lack fine-grained determinant analysis; and server workload efficiency is often overlooked. The regional example is approximately 21.2 billion liters of direct U.S. data center consumption in 2014 versus 66 billion liters in 2023, from cited studies.
- **M01d.** Integrating SPECpower throughput establishes liters per workload as a fairer comparison basis. The decomposition proceeds through three enumerated tasks: server workload-efficiency determinants; cooling/climate/infrastructure effects on PUE and WUE-site and their interaction with server efficiency in facility use; and WUE-source determinants and their interaction with server efficiency in overall use.
- **M01e.** The analysis confirms that workload efficiency is crucial for comparing water use and identifies measures that can optimize consumption from multiple perspectives. The framework can be extended to other workload measures, such as MLPerf AI benchmarks, **when sufficient data exist**; the paper does not itself supply an MLPerf analysis.

### M02 — §2 Methods, including §2.1 Data center water use

Location: manuscript pp. 6–7 (PDF pp. 7–8), Eqs. (1)–(4). §2 has no separate concluding paragraph beyond its four subsections.

- **M02a.** The analysis includes direct and indirect consumption per workload. Direct consumption includes humidification, direct adiabatic cooling, and cooling-tower evaporation, windage, and draw-off. Indirect consumption includes upstream fuel extraction/processing and renewable-equipment manufacturing, and generation-site cooling, reservoir evaporation, and PV cleaning.
- **M02b.** Overall water per workload equals facility water per workload plus facility electricity per workload multiplied by WCF: `W_overall = W_site + E_site × WCF` (Eq. 1).
- **M02c.** Facility water per workload is `WUE-site × e_server`; facility electricity per workload is `PUE × e_server` (Eqs. 2–3). Thus `W_overall = (WUE-site + PUE × WCF) × e_server = WUE-source × e_server` (Eq. 4). This decomposition makes server workload efficiency indispensable to workload-based comparison.

### M03 — §2.2 Direct server electricity use per workload

Location: manuscript pp. 7–8 (PDF pp. 8–9), Eqs. (5)–(8).

- **M03a.** Servers are the focus because they host workloads, the principal digital service of most data centers. AI training/inference measures and storage capacity for storage-focused centers are possible future extensions.
- **M03b.** Average server electricity per workload depends on utilization, installed-stock vintage distribution/refresh cycle, server power efficiency, and inactive-server fraction, including comatose and redundant idle servers. Eq. (5) expresses electricity per workload through weighted-average power and throughput; inactive servers use power without contributing useful throughput.
- **M03c.** Vintage-weighted idle power, active power, and power-performance are formed by Eqs. (6)–(8). Local linear kernel regression of SPECpower data models power and power-performance by utilization and installation year; different efficiency quantiles represent the spread within a given year. SI S1–S2 supply details.

### M04 — §2.3 Climate and technology-specific PUE and WUE-site

Location: manuscript pp. 8–9 (PDF pp. 9–10).

- **M04a.** PUE and WUE-site jointly depend on cooling technology, climate, and operating practices, sometimes with competing effects on overall water use. Simulations account for IT, lighting, fans, pumps, and power-distribution/transmission losses in PUE; WUE-site includes humidification, adiabatic cooling, and cooling-tower evaporation, windage, and draw-off where applicable.
- **M04b.** Ten cooling-system archetypes and nineteen ASHRAE climate zones (0A through 8, as listed) are modeled, which the authors describe as comprehensive global coverage. The ten systems are inventoried in T02 below. Supplemental chillers operate only when the primary method cannot meet setpoints, typically in extreme weather.
- **M04c.** Within a cooling technology and climate, operating-practice differences are represented by quantiles of simulated PUE/WUE-site. The purpose is to clarify their interrelationships and trace their effects through the workload-level metric, rather than equating low PUE or low WUE-site alone with low total water per workload.

### M05 — §2.4 Electric power water consumption factors

Location: manuscript p. 10, lines 1–13 (PDF p. 11).

- **M05a.** Eight generation sources—geothermal, hydro, biomass, oil, coal, natural gas, solar PV, and wind—are examined with both upstream and generation-site consumption included.
- **M05b.** WCF inputs are generation-weighted **U.S. averages**. They can vary substantially by region, cooling technology, prime mover, and allocation method. Further research is needed to assess these variations for more accurate application outside the United States. Global climate coverage does not make the WCF inputs globally representative.

### M06 — §3 Results, including §3.1 Determinants of direct server electricity use per workload

Location: manuscript pp. 10–12 (PDF pp. 11–13), Fig. 2 and SI Figs. S5.1–S5.4. §3's findings are distributed across §§3.1–3.7; there is no separate parent-section conclusion.

- **M06a.** With newest installed servers assumed purchased in 2023, the lowest electricity per workload is generally associated with efficient servers, high utilization, faster refresh, and few inactive servers. Usually none alone suffices; combinations can produce the same electricity per workload.
- **M06b.** The text illustrates compensation between high efficiency/low utilization/many inactive servers and low efficiency/high utilization/few inactive servers. Fig. 2's letter placement differs from the prose's A/B assignment; retain the substantive compensation claim without relying on those letter labels (see source notes).
- **M06c.** Server efficiency is the main influence. Efficient servers have lower idle power and typically greater dynamic range and better proportionality. Increasing utilization reduces electricity per workload, but benefits diminish above about 40% utilization.
- **M06d.** Shorter refresh cycles reduce electricity per workload at all utilization levels because newer servers are more efficient. Removing inactive servers also reduces it, but newer servers' lower idle power diminishes the impact of inactive machines over time.

### M07 — §3.2 Determinants of facility-level water use per server workload

Location: manuscript pp. 12–13 (PDF pp. 13–14), Fig. 3.

- **M07a.** At fixed server electricity per workload, facility water per workload rises with WUE-site; the electricity-per-workload value determines the slope.
- **M07b.** Low onsite water per workload does not necessarily imply low WUE-site. Very different WUE-site and server-efficiency combinations can give identical facility water per workload. Both quantities must be considered, rather than WUE-site alone.

### M08 — §3.3 Relationships between PUE and WUE-site values

Location: manuscript pp. 13–15 (PDF pp. 14–16), Fig. 4 and SI S6.

- **M08a.** PUE/WUE-site vary substantially across cooling technologies. Water-cooled chillers generally raise WUE-site through cooling-tower consumption, especially evaporation; direct expansion and air-cooled chillers generally have lower WUE-site but higher PUE because of lower chiller COP.
- **M08b.** Liquid cooling combined with dry coolers, economizers, or adiabatic systems can reduce both metrics. The section identifies airside economizers with direct adiabatic cooling as achieving the greatest electricity and water savings; it also says IT liquid cooling can further reduce the metrics through better heat transfer, higher coolant/facility-water setpoints, and reduced or eliminated fan/chiller power. These are the authors' system-specific statements, not an unconditional ranking for every site.
- **M08c.** Within each technology cluster the relationship is positive and nonlinear: favorable climate and efficient operation give lower values; hot/humid climate and inefficient operation give higher values.
- **M08d.** Overlapping clusters show that different combinations can reach similar PUE/WUE-site. Illustrative points have equal WUE-site but PUE differing by 2.0, or equal PUE but WUE-site differing by 2.6 L/kWh. System-wide optimization must consider technology, climate, and efficiency simultaneously.

### M09 — §3.4 Relationships between facility-level electricity use and water use per workload

Location: manuscript pp. 15–17 (PDF pp. 16–18), Fig. 5.

- **M09a.** Combining server workload efficiency with PUE/WUE-site produces broad feasible regions of facility electricity and water use per workload. The lowest use of both resources is generally associated with the highest server efficiency, but attainable minima differ substantially by cooling archetype.
- **M09b.** Cooling selection entails a tradeoff: air-cooled chillers/direct expansion typically use less water but more electricity per workload; water-cooled chillers use less electricity but more water. Economizers, dry coolers, liquid cooling, or adiabatic cooling can reduce both; adiabatic cooling particularly reduces electricity use per workload.
- **M09c.** Distinct determinant combinations yield equal electricity and/or water use per workload. Neither resource metric can be assessed using one determinant alone; there are multiple paths to reducing one or both.

### M10 — §3.5 Determinants of WUE-source

Location: manuscript pp. 17–20 (PDF pp. 18–21), Fig. 6(a–c).

- **M10a.** WUE-source depends on WUE-site plus `PUE × WCF`. Under the other fixed conditions of Eq. (4), it varies linearly with WUE-site and WCF. Feasible-region widths reflect cooling-specific WUE-site ranges; vertical bounds use wind and geothermal as the lowest and highest modeled U.S. WCFs.
- **M10b.** WCF has a large influence: high-WUE-site centers can attain low WUE-source with wind/solar; low-WUE-site centers can have high WUE-source with fossil, hydro, or geothermal electricity. Fig. 6(c)'s examples have the same WUE-site but 34-fold different WUE-source, or the same WUE-source but 4.5-fold different WUE-site, as stated in the text.
- **M10c.** Two principal reduction routes follow: improve operation to lower PUE/WUE-site, limited by cooling technology and climate; or obtain lower-WCF electricity, a more general route constrained by available grid options rather than the installed cooling technology. WUE-site alone cannot establish overall water-use efficiency.

### M11 — §3.6 Determinants of overall water use per workload

Location: manuscript pp. 20–23 (PDF pp. 21–24), Fig. 7(a–b).

- **M11a.** Wind and geothermal bracket the modeled U.S. WCF range. In the airside-economizer/air-cooled-chiller example, upper/lower overall-use bounds represent low/high server workload efficiency. The larger separation for geothermal emphasizes server-efficiency improvement when a center is constrained to high-WCF electricity.
- **M11b.** With low-WCF electricity, facility water per workload becomes relatively more important. Low-WCF-powered centers typically have much lower overall use, except where onsite consumption is substantial, for example with water-cooled chillers or waterside economizers.
- **M11c.** Facility and overall use become more positively correlated as power shifts from high to low WCF. Once low-WCF power is available, cooling-system choice, lower PUE/WUE-site, and improved server workload efficiency become routes for further reducing facility and overall consumption.
- **M11d.** Different combinations of WCF, cooling, and efficiency can still give similar overall water per workload. Centers should not be compared on WUE-source, WCF, or WUE-site alone; overlap between the geothermal and wind cases illustrates this.

### M12 — §3.7 Sensitivity analysis

Location: manuscript pp. 23–24 (PDF pp. 24–25), Fig. 8.

- **M12a.** Sobol total-effect indices rank contributions to variance in modeled overall water per workload: server efficiency first, WCF second, utilization third, then cooling system, infrastructure efficiency, climate, inactive-server fraction, and refresh cycle. This is a variance decomposition under the modeled inputs.
- **M12b.** Installing efficient servers (e.g., Energy Star), consolidation/virtualization, and wind/solar PV electricity can reduce overall water use. Cooling, infrastructure practices, and climate remain nontrivial because they determine PUE/WUE-site. Removing unnecessary equipment or refurbishment also helps through server workload efficiency.

### M13 — §4 Conclusion

Location: manuscript pp. 24–25 (PDF pp. 25–26).

- **M13a.** Increasing digitalization and freshwater restrictions make conservation salient. WUE-site/WUE-source reporting is increasing, but these metrics fall short of workload-level comparison, which the authors call the ideal basis for understanding and comparing data center water use.
- **M13b.** The study links server efficiency, utilization, refresh and inactivity to direct electricity per workload; climate/technology-specific PUE and WUE-site to facility electricity and water; and electrical WCF and WUE-source to overall water per workload. It enables more direct comparisons across diverse sites.
- **M13c.** The section closes with four explicit contributions, C01–C04 above: integrated workload metric and reporting comparability; joint direct/indirect accounting; extensive determinant analysis and tailored strategies; and inclusion of server workload efficiency for digital-service assessment.

### M14 — §5 Implications and limitations

Location: manuscript pp. 26–28 (PDF pp. 27–29).

- **M14a.** Promoting wind/solar PV, efficient servers, and virtualization/high utilization can reduce national water use while maximizing service outputs. Strategies should nevertheless be developed case by case; there is often no universal solution.
- **M14b.** Where grid or climate is geographically constrained, improving average server workload efficiency is described as the most effective reduction strategy. Choosing cooling carefully at design time can greatly reduce water use and onsite competition for local water resources.
- **M14c.** Workload-level indicators reveal computing efficiency often missed by PUE/WUE-focused analysis. A cloud center with economizers/adiabatic cooling and supplemental water-cooled chillers may use more onsite water per kWh than a traditional direct-expansion center yet deliver more services per unit of total water. Treating the traditional center as more water-efficient on WUE-site alone can therefore be biased; different settings can produce equal overall water per workload.
- **M14d.** Suggested strategies have potential co-benefits: virtualization can reduce required IT capacity and initial investment with proper planning; IT/infrastructure efficiency can reduce electricity/water bills; energy efficiency and wind/solar can lower carbon emissions. The authors regard these resource, cost, and climate benefits as grounds for policy incentives and operational measures.
- **M14e.** SPECpower may not represent the full distribution of real-world server computational efficiency over time. Even its least efficient servers may be more efficient than typical market servers, potentially **underestimating the upper bounds** of water use.
- **M14f.** The server focus omits a broader assessment of GPU, storage, and network loads, which future research should include. U.S.-average source WCFs omit regional, cooling, prime-mover, and other variation.
- **M14g.** Only consumption is analyzed; withdrawals also matter for local resources. The authors recommend combining electrical water-withdrawal factors with WCFs in future assessments of total site water use.
- **M14h.** Workload-level consumption is sometimes called a water footprint, but precise terminology matters. A clear, standardized, data-center-specific water-footprint definition is essential for future research and policy. This is the final substantive main-text conclusion.

## Supporting-information section conclusions

### S01 — S1 Server Vintage Distributions

Location: SI p. 2 (PDF p. 34), Table S.1.

- Refresh cycles of 1–8 years are used to represent practices ranging from traditional small facilities to hyperscale centers. Refresh duration maps to a server-vintage distribution referenced to 2023: equal shares of vintages in the most recent N years for an N-year cycle, as specified in T01.

### S02 — S2 Server Power Use And Power-performance

Location: SI pp. 3–5 (PDF pp. 35–37), Eqs. (S1)–(S3), Fig. S2.1.

- SPECpower provides standardized volume-server power/performance records since 2007. LLKR is selected to handle unexpected nonlinear relationships between utilization/installation year and power/power-performance. Models use Gaussian kernels, AIC-selected smoothing, and R's `sm.regression`, with response surfaces for yearly 5th/95th efficiency quantiles.
- Four observations close the analysis: power generally rises with utilization; efficient servers tend to have lower idle power; power-performance is zero at idle and increases with utilization and installation year, with the low/high-efficiency gap widening over time; and response/predictor relations are nonlinear, supporting the selected nonparametric model.

### S03 — S3 PUE And WUE-site

Location: SI pp. 5–12 (PDF pp. 37–44), Tables S3.1–S3.2 and Fig. S3.1.

- Review of existing simulations plus additional simulations covers ten air- and liquid-cooled IT system configurations. Supplemental chillers may not actually operate in favorable climate zones; systems not labeled liquid cooling represent air-cooled IT.
- Fifty scenarios per cooling-system/climate-zone pairing combine uncertain facility variables sampled with Latin Hypercube Sampling and representative-city typical meteorological year data. They reveal infrastructure operating-practice effects on both PUE and WUE-site.
- Within a given technology and climate, the 5th quantiles of PUE/WUE-site identify efficient facilities; the 95th identify inefficient ones. This quantile direction differs from server power-efficiency quantiles, for which the 95th is efficient.

### S04 — S4 Water Consumption Factor

Location: SI pp. 12–13 (PDF pp. 44–45), Table S4.1.

- WCF varies substantially by fuel/source and includes upstream and generation-site stages. The compiled U.S. inputs distinguish high-WCF geothermal/hydro from low-WCF wind/solar PV. Upstream includes fuel production, processing, transportation; generation-site categories include cooling, scrubbers, human use, and fire suppression. T04 records the actual supplied values and boundaries.

### S05 — S5 Server Electricity Use Per Workload

Location: SI pp. 13–17 (PDF pp. 45–49), Figs. S5.1–S5.4.

- The full factorial design spans utilization 0.1–0.8, refresh cycles 1–8 years, 5% versus 30% inactive servers, and the 5th/95th SPECpower efficiency quantiles.
- High-efficiency servers reduce electricity per workload; the paired-test 95% CI for the mean difference between low- and high-efficiency groups is 0.121–0.156 milliwatt/ssj_ops.
- Expected electricity per workload decreases with utilization; the figure includes a 95% CI and points representing factorial combinations.
- Shorter refresh generally reduces electricity per workload across utilization levels because newer generations are more efficient. Its savings are less significant than improving utilization or deploying efficient servers, especially at low utilization.
- Removing comatose servers further reduces electricity per workload because they consume power without useful work. The reported 95% CI for the mean difference between high/low inactive-fraction groups is 0.019–0.031 milliwatt/ssj_ops.

### S06 — S6 Relationship Between PUE And WUE-site values

Location: SI pp. 17–23 (PDF pp. 49–55), Figs. S6.1–S6.3 and Table S6.1. The following three paragraph groups are unnumbered topics within S6, all included here.

- **Climate and operation:** For airside economizers/direct adiabatic cooling with supplemental water-cooled chillers, climate and infrastructure practices define the feasible PUE/WUE-site region. Hot/humid zones typically yield higher values than cool zones, and efficient/inefficient operation can differ considerably even within one climate.
- **Two technology clusters:** Cluster 1 (direct expansion, air-cooled chillers, and airside economizers with air-cooled supplemental chillers, with or without adiabatic cooling) generally has low WUE-site, largely from occasional humidification. For the adiabatic/economizer system, advanced practices typical of Internet Giants permit free cooling much of the year, leaving little adiabatic consumption. Cluster 2 includes the other six systems: all water-cooled-chiller variants and liquid cooling with adiabatic-assisted dry coolers. It generally uses more water through cooling towers or wet dry-cooler operation. The liquid/dry-cooler system is lowest in cluster 2 because elevated facility-water temperatures permit dry operation most of the year and wet operation only for a small share.
- **Liquid-cooled IT scenarios:** Two liquid-cooling infrastructure systems are each examined for rear-door heat exchangers, cold plates, and immersion. Annual PUE/WUE-site differences among these IT scenarios are relatively small compared with differences across infrastructure technologies. The prose states that values are highest for rear-door exchangers, lowest for immersion, and intermediate for cold plates, but says this is hard to discern in Fig. S6.3. Broad overlapping permissible water temperatures allow free/adiabatic operation most of the year, even in warm/humid climates. Already-low PUE and heat-rejection-driven WUE-site limit gains from changing IT cooling alone; even small further gains need substantial system-wide optimization. The authors call for new infrastructure-efficiency metrics.

### S07 — S7 Facility-level electricity and water use per workload

Location: SI pp. 23–24 (PDF pp. 55–56), Fig. S7.1.

- Multiplication of PUE/WUE-site by server electricity per workload creates a feasible region for the example airside-economizer/adiabatic system with supplemental water-cooled chillers. Highest server workload efficiency is associated with the lowest facility electricity and water per workload.

### S08 — S8 WUE-source

Location: SI pp. 24–25 (PDF pp. 56–57), Fig. S8.1.

- The examples compare airside economizers/adiabatic cooling with supplemental water-cooled chillers and direct expansion. WUE-source is linearly related to WCF and PUE under the corresponding fixed other inputs. The text assigns the highest/lowest WUE-source bounds to highest/lowest WCFs, geothermal/wind, respectively. The plotted power-source labels need separate treatment; see the source notes below.

### S09 — S9 Overall Water Use Per Workload

Location: SI pp. 25–26 (PDF pp. 57–58), Fig. S9.1.

- Additional examples use hydro, biomass, oil, coal, natural gas, and solar PV. Low-WCF sources generally yield much lower overall water per workload, but do not guarantee it: high PUE, high WUE-site, and low server workload efficiency can still yield high consumption, illustrated by the upper-right solar-PV region.

### S10 — S10 Data Source Summary

Location: SI pp. 26–27 (PDF pp. 58–59), Table S10.

- This section contributes a provenance inventory rather than a new empirical conclusion. It identifies the inputs and cited sources for server electricity per workload, PUE/WUE-site, and upstream/generation-site electrical WCF, and points to the methodological sections. See T06.

## Figures: what each shows and where

There are **8 numbered main figures** and **12 numbered SI figures**. Panels are described separately within the parent item. Descriptions below are paraphrased visual readings checked against the PDF images and adjacent explanation; approximate plot readings are identified as such.

| ID / element | Location | What it shows |
| --- | --- | --- |
| F01 — Fig. 1 | Main p. 5; PDF p. 6 | Calculation schematic: server electricity per workload multiplies PUE and WUE-site to give facility electricity and water per workload; facility electricity multiplies grid WCF to give indirect water, which is added to facility water. Dashed determinant boxes connect server efficiency/utilization/vintage/inactivity; cooling/climate/component efficiencies/setpoints/tower/humidification conditions; and power-plant/cooling/reservoir/mix/upstream assumptions to the quantities they affect. |
| F02 — Fig. 2 | Main p. 12; PDF p. 13; interpretation pp. 10–11 | Four heat maps plot electricity per workload against utilization and refresh cycle for 5th/95th server-efficiency quantiles and 5%/30% inactive pools. Efficient servers, higher utilization, shorter cycles, and fewer inactive machines generally lower use, with diminishing utilization gains. Different combinations yield similar colors/use. The displayed color scale is in milliwatt/ssj_ops. A/B illustrate compensation, but their panel assignments differ from the prose. |
| F03 — Fig. 3 | Main p. 13; PDF p. 14 | Fan-shaped relationship between WUE-site (x), facility water per workload (y), and server electricity per workload (colored lines). At fixed electricity per workload, onsite water is linear in WUE-site; worse server efficiency steepens the slope. A/B have equal facility water at very different WUE-site/efficiency. The server range is uniformly sampled from Fig. 2's extrema; the figure labels endpoints about 0.06–0.57 milliwatt/ssj_ops. |
| F04 — Fig. 4 | Main p. 15; PDF p. 16 | PUE versus WUE-site for ten cooling technologies; x is logarithmic. Within-technology points/regions span climates and operating efficiencies; overlaps show that distinct system conditions can attain similar metrics. Air-cooled/direct-expansion systems occupy low-water/higher-PUE regions, water-cooled systems higher-water regions, and economizer/adiabatic/liquid options extend toward low PUE. Values are yearly averages; liquid scenarios include rear-door, cold-plate, immersion. A/B and C/D illustrate equal-one-metric/different-other-metric examples. |
| F05 — Fig. 5 | Main p. 17; PDF p. 18 | Ten panels show facility electricity per workload (y) versus facility water per workload (log x), with regions combining climate, infrastructure practices, and server workload efficiency. Cooling-specific minima and electricity/water tradeoffs coexist with overlaps. Points A share facility water; points B share facility electricity. |
| F06 — Fig. 6(a–c) | Main pp. 19–20; PDF pp. 20–21 | (a) WUE-source versus WUE-site regions for two cooling systems under wind/geothermal power, bounded horizontally by technology-specific WUE-site and vertically by WCF/PUE. (b) U.S. source WCF bars in L/kWh: wind 0.011, solar PV 0.034, natural gas 1.170, coal 2.200, oil 2.900, biomass 4.280, hydro 6.800, geothermal 11.090, as printed. (c) Ten technology regions show wide WUE-source differences at equal WUE-site and vice versa, with wind/geothermal bounds. The text's 34-fold and 4.5-fold examples are recorded in M10b. Fig. 6(b)'s wind number differs from Table S4.1's total; do not silently replace either. |
| F07 — Fig. 7(a–b) | Main p. 22, with (b) caption on p. 23; PDF pp. 23–24 | (a) Geothermal/wind panels for airside economizers with air-cooled supplemental chillers plot overall against facility water per workload, with low/high server-efficiency boundaries; the server-efficiency separation is much larger under high-WCF geothermal. Regions combine extrema from Figs. 2/4 and WCFs from Fig. 6(b). (b) Ten cooling-technology regions for each power source show generally lower totals under wind and overlap in overall consumption across combinations. Both axes are logarithmic. Dashed horizontal lines mark extrema used to illustrate overlap; the caption's color description is reversed relative to the displayed lines (source notes). |
| F08 — Fig. 8 | Main p. 24; PDF p. 25 | Sobol total-effect sensitivity bars rank all eight determinants in the A06/M12a order, with 95% confidence-interval error bars. Approximate indices from the plot: server efficiency 0.41, WCF 0.40, utilization 0.38, cooling 0.085; the other four are much smaller. The top three confidence intervals overlap. Server-efficiency quantile describes power efficiency within a year; infrastructure-efficiency quantile describes PUE/WUE-site within a technology/climate. |
| F09 — Fig. S2.1(A–B) | SI p. 5; PDF p. 37 | (A) Response surfaces for server power and (B) for ssj_ops/W, each versus utilization and installation year, comparing 5th/95th efficiency quantiles. Power generally increases with utilization and efficient servers have lower idle power; performance per watt rises with utilization and newer vintage, with a widening efficient/inefficient gap and nonlinear responses. |
| F10 — Fig. S3.1 | SI p. 10; PDF p. 42 | Scenario-generation flowchart: cooling type selects facility variables/50 operating-efficiency scenarios; climate selects representative-city TMY data; both enter the PUE/WUE-site model to produce values by cooling system and climate. |
| F11 — Fig. S5.1 | SI p. 14; PDF p. 46 | Boxplots and factorial-design points compare server electricity per workload for 5th/95th efficiency quantiles. The efficient group has lower consumption; accompanying paired-test CI is 0.121–0.156 milliwatt/ssj_ops. |
| F12 — Fig. S5.2 | SI p. 15; PDF p. 47 | Server electricity per workload versus utilization, with expected-value curve, gray 95% CI, and factorial points. A steep reduction at low utilization flattens at higher utilization, consistent with diminishing benefits around/above 40%. |
| F13 — Fig. S5.3 | SI p. 16; PDF p. 48 | Refresh-cycle plots for 5%/30% inactive pools, utilization levels 0.2/0.4/0.6/0.8, and bands spanning 5th/95th server-efficiency endpoints. Shorter refresh generally lowers electricity per workload, but its impact is smaller than efficiency/utilization differences; a higher inactive fraction raises use. Bands indicate the efficiency endpoints, not a stated statistical CI. |
| F14 — Fig. S5.4 | SI p. 17; PDF p. 49; test discussion p. 16 | Boxplots/factorial points compare electricity per workload at 5%/30% inactive servers. Fewer inactive servers reduce consumption. The adjoining text reports a 0.019–0.031 milliwatt/ssj_ops 95% CI for the mean difference. |
| F15 — Fig. S6.1 | SI p. 18; PDF p. 50 | Climate-labeled PUE/WUE-site points at efficient 5th and inefficient 95th infrastructure quantiles for airside economizers/adiabatic cooling with supplemental water-cooled chillers. Illustrates how climate/operation define a region in Fig. 4, generally lower in cool/favorable and efficient conditions. |
| F16 — Fig. S6.2 | SI p. 20; PDF p. 52 | PUE/WUE-site regions split into low-water cluster 1 and higher-water cluster 2, using linear x axes (with different panel ranges). Re-expresses Fig. 4's technologies so the very low onsite water of air-cooled/economizer combinations is visible; liquid/dry-cooler/adiabatic assist has the lowest WUE-site within cluster 2. |
| F17 — Fig. S6.3(a–b) | SI pp. 22–23; PDF pp. 54–55 | Boxplots compare (a) PUE and (b) WUE-site for rear-door heat exchangers, cold plates, immersion under two infrastructure systems: adiabatic-assisted dry cooler/air-cooled chiller and waterside economizer/water-cooled chiller. IT-scenario distributions largely overlap, while heat-rejection-system differences, especially WUE-site, are larger. Left/right y scales differ. The prose's claimed small rear-door-to-immersion ordering is recorded in S06, rather than asserted as visually clear. |
| F18 — Fig. S7.1 | SI p. 24; PDF p. 56 | Facility electricity versus facility water per workload for the economizer/adiabatic/water-cooled-supplement system, with high/low server-efficiency series bounding a region. High efficiency lies toward lower resource use. The caption reverses the correspondence between efficiency and electricity-per-workload extrema; see source notes. |
| F19 — Fig. S8.1 | SI p. 25; PDF p. 57 | Linear-x WUE-source versus WUE-site for economizer/adiabatic/water-cooled supplement and direct expansion, with source-specific series. Demonstrates wide source-dependent separation; PV/wind are nearly coincident at this scale. The text identifies geothermal/wind as extrema, but the visible legend has conflicting labels and also includes nuclear; see source notes. |
| F20 — Fig. S9.1 | SI p. 26; PDF p. 58 | Six power-source panels (hydro, biomass, oil, coal, natural gas, solar PV), each showing overall versus facility water per workload by cooling technology on log axes. Lower WCF generally reduces overall consumption; the high-use solar-PV corner shows that high onsite use and poor efficiencies can defeat a simple low-WCF comparison. |

## Tables: what each shows and where

There are **no numbered tables in the main text** and **6 numbered SI tables**. The raster table S.1 was read from its image. Other tables were checked in the PDF's extracted text; table locations include caption/header pages when split.

### T01 — Table S.1 (also called Table S1 in the prose)

Location: SI p. 2 (PDF p. 34). Maps 1–8-year refresh cycles to installed-server vintage shares, reference year 2023. A one-year cycle is 100% 2023; two years is 50% each 2022/2023; three years is 33.3% each 2021–2023; four years is 25% each 2020–2023; five is 20% each 2019–2023; six is 16.7% each 2018–2023; seven is 14.3% each 2017–2023; eight is 12.5% each 2016–2023. Earlier vintages have zero share. Values retain the table's rounding. This defines the modeled refresh/vintage relationship, not an empirical stock census.

### T02 — Table S3.1

Location: SI pp. 6–10 (PDF pp. 38–42; last note continues on p. 42). Describes the ten modeled cooling systems and their mechanisms/tradeoffs:

| System | What the table says |
| --- | --- |
| Direct expansion | Refrigerant cools indoor air directly; CRACs are simple and cost-effective. |
| Air-cooled chiller | Air-cooled condensers, typically with CRAH units; attractive where water conservation matters or cooling towers cannot fit. |
| Water-cooled chiller | Efficient for large loads, typically with CRAHs; cooling towers reject heat but evaporation raises consumption concerns. |
| Waterside economizer (water-cooled chiller) | Uses naturally cool water or cooling-tower-produced cool water to avoid refrigeration, with supplemental water-cooled chilling; towers can consume substantial water. |
| Airside economizer (air-cooled chiller) | Outdoor air provides cooling during favorable weather, lowering energy/cost; air-cooled chilling supplements unmet demand. |
| Airside economizer (water-cooled chiller) | Similar, with water-cooled supplemental chilling during unfavorable conditions/high demand. |
| Airside economizer & adiabatic cooling (air-cooled chiller) | Direct evaporation reduces mechanical refrigeration; in some climates it can eliminate supplemental chilling for the year. |
| Airside economizer & adiabatic cooling (water-cooled chiller) | Same primary methods, with water-cooled chilling when both cannot meet demand. |
| Liquid cooling: waterside economizer (water-cooled chiller) | Higher permissible water temperatures enable economizer operation much of the year; water-cooled chilling supplements; cooling towers can still consume substantial water. |
| Liquid cooling: dry cooler with adiabatic assist (air-cooled chiller) | High-temperature liquid systems favor dry heat rejection much of the year; wet mode uses adiabatic pre-cooling upstream of coils; air-cooled chilling supplements. Designed to conserve water relative to evaporative towers while reducing energy. |

Parentheses mean supplementary cooling, potentially unused in favorable climates. Systems not prefixed with liquid cooling use air-cooled IT. The liquid systems encompass rear-door exchangers, direct-to-chip, and immersion configurations.

### T03 — Table S3.2

Location: caption SI p. 10 and body p. 11 (PDF pp. 42–43). Summarizes model/input provenance: the physical PUE model includes IT, power supply/distribution losses, lighting and cooling; the physical WUE-site model includes humidification, cooling towers, and adiabatic processes. Facility-system scenarios use Latin Hypercube Sampling over uncertain variables. TMY inputs use representative cities for each climate zone, with EnergyPlus weather data. Physical models and facility variables cite Lei et al. (2023) and Lei and Masanet (2022, 2020); representative-city selection cites Woldekidan et al. (2020).

### T04 — Table S4.1

Location: caption SI p. 12, body p. 13 (PDF pp. 44–45). Source-specific U.S. WCF components and totals, in L/kWh as defined in §2.1. Upstream source: Peer et al. (2019); generation-site source: Siddik et al. (2021). Entries below reproduce the printed values without reallocating boundaries or replacing N/A.

| Boundary | Geothermal | Hydro | Biomass | Oil | Coal | Natural gas | Solar PV | Wind |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Upstream | 9.5 | 6.8 | 1.2 | 1.4 | 0.4 | 0.21 | 0.011 | 0.011 |
| Point of generation | 1.59 | N/A | 3.0763 | 1.5 | 1.8 | 0.96 | 0.0227 | 0.0038 |
| Total | 11.09 | 6.8 | 4.2763 | 2.9 | 2.2 | 1.17 | 0.034 | 0.0148 |

The table brackets sources from high geothermal/hydro to low wind/PV. Fig. 6(b) prints wind as 0.011 rather than this table's total 0.0148, and rounds biomass to 4.280. Preserve the location-specific numbers.

### T05 — Table S6.1

Location: caption/header SI p. 21, rows p. 22 (PDF pp. 53–54). Facility-water supply temperature assumptions: rear-door heat exchanger 2–32 °C; cold plate/direct-to-chip 2–40 °C; immersion 2–45 °C. Broad overlapping ranges help explain the small infrastructure-metric differences among IT cooling scenarios. Sources printed with the table are ASHRAE (2014) and ASHRAE Technical Committee 9.9 (2011).

### T06 — Table S10

Location: SI pp. 26–27 (PDF pp. 58–59). Crosswalk of components, variables, relevant sections, and data sources:

- Direct server electricity per workload: utilization (§2.2/S2/S5), Shehabi et al. (2016); vintage distribution (S1/S5), Horizon Editorial (2023) and Supermicro (2019); server efficiency (S2/S5), SPEC (2022); inactive fraction (§2.2/S5), Koomey and Taylor (2017).
- PUE and WUE-site (§2.3/S3/S6): ASHRAE (2014, 2013), ASHRAE TC9.9 (2011), EnergyPlus (2016), Lei (2022), Lei et al. (2023), Lei and Masanet (2022, 2020).
- Electrical WCF (§2.4/S4): upstream, Peer et al. (2019); point of generation, Siddik et al. (2021).

## Source-specific reading notes

These notes distinguish text from visuals where the supplied PDF differs internally. They are location aids for fidelity checking, not judgments of the argument, and they do not override the article.

- **Fig. 2 labels:** §3.1's prose assigns A to high-efficiency/low-utilization/many-inactive and B to low-efficiency/high-utilization/few-inactive settings. The image puts A in the 5th-efficient/5%-inactive panel near utilization 0.8 and B in the 95th-efficient/30%-inactive panel near utilization 0.2. A faithful account can identify the substantive equivalence while specifying whether it follows the text or the plotted letters.
- **Fig. 6(c) numerical example:** the prose says equal-WUE-source points C/D differ in WUE-site by a factor of 4.5. The displayed logarithmic x-axis places C near 10^-4 and D near units of L/kWh, a much larger visible separation. M10b inventories the textual claim; F06 does not infer a repaired ratio.
- **Fig. 7(b) dashed lines:** its caption describes blue as geothermal minimum and red as wind maximum. The displayed blue line is lower and the red line higher, with red at the geothermal minimum and blue at the wind maximum. The shared substantive point is overlap in attainable overall water per workload.
- **Fig. S7.1 caption:** it says low/high workload efficiency represent minimum/maximum server electricity per workload, respectively. Eq. (4), the accompanying text, and the plotted high-efficiency series associate high efficiency with lower electricity/resource use. F18 records the image and section conclusion without adopting the reversed caption wording.
- **Fig. S8.1 sources:** S8 prose names geothermal and wind as upper/lower bounds and mistakenly refers to WCFs in Fig. 5(b), whereas the main WCF panel is Fig. 6(b). The visible legend in S8.1 includes Coal, Geothermal, Hydro, Natural gas, Nuclear, Solar PV, Wind; its highest series is labeled Hydro, with Geothermal below it. Nuclear is not one of §2.4/Table S4.1's eight sources. Record these plotted labels as printed rather than silently substituting the main analysis's source list or ordering.

## Coverage ledger

- Abstract: A01–A08 cover its context, purpose, three magnitude claims, determinant ordering, tailored-strategy conclusion, and knowledge-gap/minima claim.
- Enumerated contributions: C01–C04 cover all four §4 bullets. The three enumerated analytical tasks in §1 are separately retained in M01d; the four gap bullets in M01c.
- Main sections: §1; §2 and §§2.1–2.4; §3 and §§3.1–3.7; §4; §5 are covered by M01–M14. Methods subsections are represented by their definitions, scope and methodological conclusions where they have no independent result conclusion.
- SI sections: all ten, S1–S10, are covered by S01–S10; S6's three unnumbered substantive topics are included explicitly.
- Figures: all 20 numbered figures, F01–F20, including Fig. 6(a–c), Fig. 7(a–b), Fig. S2.1(A–B), and Fig. S6.3(a–b).
- Tables: all six SI tables, T01–T06; none in main text.
- Scientific text endpoint: through SI §S10/Table S10, PDF p. 59, with bibliography continuing to final PDF p. 60. No claims are inferred from unprovided external supporting code/data.
