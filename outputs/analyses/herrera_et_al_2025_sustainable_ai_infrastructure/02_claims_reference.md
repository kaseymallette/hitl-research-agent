# Claims reference list

**Article:** `article.pdf` — Manuel Herrera, Xiang Xie, Andrea Menapace, Ariele Zanfei, and Bruno M. Brentan, “Sustainable AI infrastructure: A scenario-based forecast of water footprint under uncertainty,” *Journal of Cleaner Production* 526 (2025), 146528.

**Scope and endpoint:** This inventory covers the main text, §§1–7 (pp. 1–10), **and the entire Appendix, “Sensitivity analysis” (p. 10)**, including every figure and table. The PDF has 12 pages; pp. 11–12 are references, not additional substantive conclusions. Page numbers below are the PDF's printed page numbers. The end matter's availability and declaration statements are also identified below. No cited work, linked repository, or outside source was consulted.

**Use:** Entries are paraphrases of the article's claims unless explicitly quoted. They inventory what the authors assert, propose, assume, recommend, or report; they do not independently endorse or evaluate it. Claims repeated in different locations remain identifiable by location, but need not be counted as distinct substantive findings. The contribution, abstract, section-conclusion, figure, and table inventories are separated to support coverage checking. Equations and Algorithm 1 are additionally inventoried. Numerical and labelling differences between the article's elements are preserved, not silently reconciled.

## 1. Contributions and front-page highlights

The paper does not provide a numbered scientific-contribution list. Its three explicitly enumerated **Highlights** are H1–H3; C1–C5 identify additional contribution statements made in the abstract, introduction, methods, and conclusion. The CRediT statement concerns author roles, not scientific contributions.

- **H1 — Highlight 1, p. 1:** Provides probabilistic forecasts of global water demand from AI data centres through 2050.
- **H2 — Highlight 2, p. 1:** Introduces a scenario-based framework grounded in Bayesian-informed assumptions.
- **H3 — Highlight 3, p. 1:** Identifies cooling efficiency, electricity sourcing, and siting as critical mitigation levers.
- **C1 — Abstract, p. 1; §1, p. 2; §2.2, p. 3; §7, p. 9:** Offers a global, three-component assessment of AI data-centre consumptive blue water: on-site operational cooling, off-site electricity generation, and embodied hardware/supply-chain water. The framework follows and extends Li et al. (2025).
- **C2 — Abstract, p. 1; §1, p. 2; §§5–5.1, pp. 6–7:** Introduces what the authors call a novel scenario-based probabilistic forecasting approach that combines sparse empirical information, expert-informed assumptions, and uncertainty to distinguish alternative growth and efficiency pathways for 2030 and 2050. It is Bayesian-inspired, rather than full Bayesian inference.
- **C3 — §5.1, pp. 6–7; Algorithm 1, p. 8:** Supplies an explicit Monte Carlo workflow producing simulated means and central 90% intervals for three scenarios, with annual projections from 2025 through 2050.
- **C4 — Abstract, p. 1; §§6–7, pp. 8–10; Appendix, p. 10:** Uses scenario comparisons and sensitivity analysis to identify technical mitigation levers and translate forecasts into cooling, energy, hardware, reporting, and siting recommendations.
- **C5 — §1, p. 2; §5.1, p. 7; §7, pp. 9–10:** Presents the approach as transparent, flexible, adaptable, useful in data-sparse settings, and supportive of infrastructure design, strategic planning, sustainability reporting, investment, and policy. Regional disaggregation and updated observations are proposed extensions.

## 2. Every abstract claim (p. 1)

- **A1:** Rapid AI and cloud-computing expansion creates a significant, often overlooked impact on global water resources.
- **A2:** The paper presents a global water-consumption assessment that distinguishes facility operational use, off-site electricity-related consumption, and embodied hardware/supply-chain consumption.
- **A3:** A Bayesian-inspired, scenario-based probabilistic framework is developed to anticipate 2030 and 2050 demand using sparse empirical data, expert-informed assumptions, and policy-relevant growth trajectories.
- **A4:** Without mitigation, global water consumption associated with data centres **could increase more than seven times by mid-century**.
- **A5:** Cooling-related operational consumption accounts for the majority of demand.
- **A6:** Identified mitigation pathways include better cooling efficiency, alternative technologies, and infrastructure planning attentive to regional water availability.
- **A7:** Sensitivity analysis highlights the strong influence of compute growth and efficiency trends on future outcomes.
- **A8:** The findings offer a transparent, adaptable basis for aligning AI infrastructure development with long-term water sustainability goals.

## 3. Section and subsection claims and conclusions, in article order

### §1. Introduction (pp. 1–2)

- **S1.1 — Motivation:** AI adoption and associated infrastructure are expanding rapidly. The introduction reports projected 2030 AI use by approximately 70% of companies, roughly $15 trillion in output/productivity gains, and GDP gains of 26% in China and around 14% in North America. Data centres currently account for 1%–2% of global electricity consumption, potentially exceeding 3000 TWh annually by 2030. These are cited contextual projections, not outputs of this paper's model.
- **S1.2 — Water gap and scope:** Environmental discussion has concentrated on electricity and carbon; a holistic assessment requires equal attention to significant and growing water consumption. This study addresses **consumptive blue water**, meaning freshwater evaporated, incorporated into products, or transferred out of its originating catchment and thereby unavailable there.
- **S1.3 — Direct and dispersed indirect impacts:** Water demand grows through cooling, electricity supply, and hardware manufacture. Fossil electricity typically consumes 2–3 litres/kWh, while nuclear electricity may also be water intensive depending on cooling. Physical separation of facilities, generation, and globally sourced hardware disperses the footprint and complicates planning, especially where production occurs in water-stressed regions.
- **S1.4 — Definitions:** WUE measures on-site cooling water per unit energy; PUE is total facility energy divided by IT energy; operational use comprises on-site and electricity-related off-site water; EWU concerns hardware-manufacturing consumptive water.
- **S1.5 — Literature gap:** Quantitative future-water projections are rare, particularly ones distinguishing components and accounting for uncertainty. Existing studies establish regional vulnerability and identify server efficiency/utilisation, grid water consumption, cooling technology, and climate as determinants, but limited work constrains policy and infrastructure planning.
- **S1.6 — Proposed response/conclusion:** The paper's probabilistic framework separates on-site, off-site, and embodied water and explicitly incorporates uncertainty. BAU, moderate intervention, and sustainable transformation represent differing compute growth and efficiency/policy paths. Bayesian-inspired modelling can combine sparse observations with expert judgement and scenarios. Global forecasts through 2050 align with international sustainability horizons and offer a structured, transparent basis for decisions, especially in water-stressed regions.

### §2. Drivers of AI data centre water consumption (pp. 2–3)

- **S2.1 — Section-level claim:** AI workloads require substantially more computation than traditional applications, increasing intensive cooling and water demand. Water has received less research attention than energy. The cited estimate of roughly **1.7 billion litres/day by 2030** may underestimate demand given accelerating large-model deployment and specialised hardware. §§2.1–2.2 establish the scale of the problem and a component-based accounting framework.

### §2.1. AI water footprint: Impact at scale (pp. 2–3)

- **S2.1a:** Hyperscale cloud and specialised AI facilities use dense GPU/TPU infrastructure requiring continuous cooling. AI-focused power densities frequently exceed 40 kW and can reach 80 kW, compared with 5–10 kW for standard enterprise centres, increasing thermal loads and dependence on cooling.
- **S2.1b — Training examples:** GPT-3 training is reported to require approximately **1287 MWh** per cycle; major retraining typically occurs every one to two years, with less demanding monthly/quarterly fine-tuning. Gemini training is estimated to use over one million litres depending on regional cooling. The passage also gives **700,000–1,000,000 litres**, equivalent to daily use by **5000–7000 people**, for a training run under typical evaporative cooling, and **1.9–4.9 million litres** for a major GPT-scale event at **1.5–3.8 litres/kWh**. These examples are contextual claims as printed, not this paper's forecasts.
- **S2.1c:** Newer models demand increasing computational resources. The article describes training compute as doubling every 3–4 months since 2012 and invokes an “AI compute scaling law”; Fig. 1 supports its account of continued, accelerating growth.
- **S2.1d:** Individual inference requests use much less water than training, but aggregate inference has substantial ongoing water demand when interactions number in the billions per day.
- **S2.1e — Subsection conclusion:** Frontier-model compute requirements could increase **10- to 100-fold by 2030**. Without proactive measures, this would magnify environmental impacts, disproportionately affecting already water-scarce regions. Computational efficiency, cooling improvements, and water management are increasingly necessary.

### §2.2. AI water footprint: Quantification (p. 3)

- **S2.2a — Boundary:** The framework exclusively addresses blue water. Green water (plant-used soil rainwater) and grey water (pollution-assimilation volume) are excluded.
- **S2.2b:** Total consumptive water is the sum of on-site cooling, off-site electricity generation, and embodied manufacturing water, allowing transparent direct/indirect accounting (E1–E4 below).
- **S2.2c:** On-site water depends on IT electricity and WUE. WUE varies with cooling, design, and climate, and tends to be higher in dense AI centres.
- **S2.2d:** Off-site water depends on IT electricity, PUE, and the electricity water intensity factor (EWIF). Regional electricity mix strongly determines EWIF; fossil generation typically requires 2–3 litres/kWh, nuclear can be similarly or more demanding depending on cooling, and solar/wind are described as almost water-free.
- **S2.2e — Subsection conclusion:** Embodied manufacturing water is amortised over equipment life and is smaller in daily volume but increasingly important with hardware demand, short refresh cycles, and model complexity. A single AI accelerator GPU is estimated to require **20,000–30,000 litres** to produce, with thousands deployed annually in AI centres.

### §3. Cooling systems and their role in operational water consumption (pp. 4–5)

- **S3.1 — Section-level claims:** AI's thermal loads and weeks- or months-long training cycles pressure cooling systems. Cooling improvements helped stabilise electricity use despite rising service demand. Traditional air cooling increasingly struggles with these loads, prompting movement to liquid and immersion systems. Liquid cooling is thermally efficient but can use water-based coolants; immersion substantially reduces on-site water but faces technical/infrastructure barriers.
- **S3.2 — Section synthesis:** Cooling choices involve water, energy, and adoption trade-offs. Scaling AI makes selection of low-water strategies essential to long-term sustainability; the concluding adoption subsection reports a transition towards more water- and energy-efficient management (S3.4).

### §3.1. Air-based cooling systems (p. 4)

- **S3.1a:** Air circulates through racks, absorbs heat, and rejects it outdoors or through heat exchangers (Fig. 2).
- **S3.1b — Subsection conclusion:** Minimal direct water use makes air cooling preferable in water-scarce regions, but it generally increases energy demand, especially where warm conditions require mechanical cooling. Relative to evaporative cooling, total data-centre energy demand can increase **10%–30%**, depending on temperature and humidity.

### §3.2. Evaporative cooling towers (p. 4)

- **S3.2a:** Evaporative towers are common in large centres, especially where water is abundant, because of high thermal efficiency. Air passing sprayed water removes heat through evaporation (Fig. 3).
- **S3.2b — Subsection conclusion:** Effective heat rejection comes with high water use through evaporation and blowdown. The authors treat both as consumptive volumes permanently removed from the local water cycle. Their framework counts these volumetric losses but excludes the grey water footprint of pollution assimilation. Annual consumption can reach millions of litres, particularly problematic in hot, arid, water-stressed settings.

### §3.3. Liquid and immersion cooling (pp. 4–5)

- **S3.3a:** Direct liquid cooling circulates coolant through cold plates on CPUs/GPUs; immersion submerges servers in dielectric fluid and rejects heat through a cooling loop.
- **S3.3b:** In the direct-liquid arrangement described with Fig. 4, coolant absorbs heat at its source, passes through a heat exchanger, and recirculates. Low thermal resistance improves performance at high computing densities and reduces reliance on water-intensive evaporation.
- **S3.3c — Subsection conclusion:** Liquid cooling significantly reduces water demand, especially with closed loops replacing evaporation, accommodates higher power density, and can reduce **cooling energy by up to 50% relative to air cooling**. Adoption is limited by capital costs, integration complexity, and hardware compatibility; immersion particularly requires substantial retrofits and specialised equipment.

### §3.4. Adoption rate of cooling technologies (p. 5)

- **S3.4a:** Table 1 qualitatively compares water consumption, energy efficiency, and adoption; appropriate low-water cooling choices are essential as workloads grow.
- **S3.4b:** Air cooling remains dominant; US computer-room air conditioners/handlers reportedly grew **64% between 2020 and 2023**. High-density AI nevertheless drives advanced-cooling adoption. The liquid cooling market is projected to grow from **$5.65 billion in 2024 to over $48 billion in 2034**, and North America held **over 35%** of the immersion market in 2023.
- **S3.4c — Subsection/section conclusion:** These trends indicate a growing transition towards thermal management with better water and energy efficiency.

### §4. Regional variations in data centre water consumption (pp. 5–6)

- **S4.1:** Water consumption is geographically uneven. Infrastructure, tax incentives, renewable access, and demand create clusters that often coincide with water stress, increasing competition with agriculture and households. Inadequate regulation/consultation and uneven disclosure complicate assessment and planning.
- **S4.2:** The 2025 distribution in Fig. 5 is concentrated in North America, Europe, India, and parts of Oceania and does not consistently align with water sustainability. The US has by far the largest number; the authors emphasise medium-high stress there, high stress in India and Spain, and relatively lower stress in Germany/the UK.
- **S4.3 — Regional examples:** Thames Water warns of possible heatwave restrictions in the UK; US operators in the article's Arizona/Virginia example consume millions of litres daily and face scrutiny, while some explore recycled water and liquid cooling. China's data-centre use is expected to exceed **three billion cubic metres annually by 2030**, with facilities concentrated in water-scarce northern provinces and policy encouraging lower-water cooling/renewables. Chilean/Brazilian expansion prompts debate over infrastructure capacity and drought resilience.
- **S4.4:** Regional disparities require context-specific strategies accounting for hydrology, infrastructure, regulation, and vulnerability in forecasts.
- **S4.5 — Climate/siting conclusion:** Köppen classifications provide useful siting criteria. Hot desert/semi-arid BWh/BSh regions, including the southwestern US, northern Mexico, Australia, and northern Africa, are poorly suited to evaporative towers because heat, low humidity, and scarce freshwater intensify losses and pressure. Temperate Cfb/Cfa climates favour air/hybrid systems through lower temperatures and higher humidity. Climate-aware siting can better align infrastructure with water sustainability.
- **S4.6 — Closing qualification:** Cooling technology is only one determinant; policy, operating practices, and infrastructure design also influence consumption.

### §5. Forecast scenarios for 2030 and 2050: A probabilistic scenario-based approach (pp. 6–8)

- **S5.1 — Section-level rationale:** Limited high-resolution global observations and rapid technological change make historical-trend forecasting poorly suited to AI infrastructure. Future demand depends on changing models, hardware, and operations.
- **S5.2 — Section-level conclusion:** A semi-quantitative, scenario-based probabilistic framework transparently combines sparse observations and expert assumptions, models the three water components, and produces distributions rather than point predictions. BAU/moderate/sustainable paths offer a more robust, flexible assessment of plausible long-term outcomes for planning and environmental governance. The scenario-specific findings and closing intervention requirement are recorded under §5.2 below.

### §5.1. Probabilistic scenario-based forecasting (pp. 6–7)

- **S5.1a — Method boundary:** Monte Carlo propagates parameter uncertainty. The model incorporates prior assumptions but **does not implement full Bayesian inference**. Its plausible trajectories are conditional on present knowledge, scenario assumptions, and anticipated efficiency gains.
- **S5.1b — Baseline:** Server electricity in 2025 is Normal with mean **1.0 × 10^9 kWh/day** and standard deviation **0.1 × 10^9 kWh/day** (Eq. 5). The 2030/2050 horizons align with international environmental targets.
- **S5.1c — Efficiency assumptions:** WUE, PUE, and EWIF are deterministic values improving incrementally each year, with assumed annual efficiency gains of **0.5%–1%**. EWU also improves at a fixed annual rate. These assumptions represent gradual cooling, infrastructure, manufacturing, supply-chain, and energy-source improvements.
- **S5.1d — Energy distinction:** Immersion/direct-to-chip cooling may reduce cooling energy directly; waste-heat reuse does not itself lower cooling demand but may lower broader-system net primary energy use. Either route can indirectly lower water consumption.
- **S5.1e — Three scenario assumptions:** BAU has **10% annual compute growth**; moderate intervention **5%**; sustainable transformation **0%**, stabilising compute at current levels. The authors frame these as plausible upper/middle/lower bounds and conceptually parallel baseline, intermediate-mitigation, and net-zero climate pathways, including SSP-style scenarios.
- **S5.1f — Simulation/output:** **10,000 iterations** sample priors and apply component equations to yield empirical daily-water distributions by scenario/year. The authors describe the process as constructing likelihood functions from plausible compute, cooling, and turnover developments. Means and central 90% intervals summarise uncertainty; the interval uses the empirical 5th and 95th percentiles without assuming an output distribution shape.
- **S5.1g — Interval interpretation as stated:** The article calls the result a **90% credible interval**, describing it as the range containing the true water-consumption value with 90% probability conditional on data and prior-informed assumptions. This is the authors' interpretation alongside their explicit statement that full Bayesian inference is not implemented.
- **S5.1h — Subsection conclusion:** Algorithm 1 provides the full sampling/projection workflow. Regional disaggregation with location-specific efficiencies is possible but outside this study's scope. Annual or biannual updates of WUE/PUE/EWIF and rerunning simulations are proposed to maintain relevance and refine policy/investment decisions; actual dynamic updating is not reported as implemented.

### §5.2. Probabilistic scenario projections from scenario-based simulations (pp. 7–8)

- **S5.2a:** Table 2 gives scenario means and 90% intervals for 2030/2050 (all values reproduced under T2). Compute growth and efficiency gains strongly influence the results.
- **S5.2b:** Under BAU, water demand is projected to rise **nearly sevenfold between 2030 and 2050**; moderate intervention gives a more manageable trajectory; sustainable transformation yields a net reduction by mid-century.
- **S5.2c:** The authors say the BAU trajectory is consistent with the cited expectation of more than **20 billion litres/day by 2050**, while their framework adds explicit probabilistic treatment of uncertainty and expert-informed variability. Fig. 6 visualises trajectories and intervals.
- **S5.2d — Subsection/section conclusion:** Exponential BAU growth could worsen stress in vulnerable regions. Moderate growth plus efficiency substantially reduces demand. Systemic changes, including non-water-based cooling and extended hardware lifetimes, can decouple AI adoption from growing water use. Achieving the sustainable scenario requires regulation, technological innovation, and forward-looking infrastructure planning.

### §6. Discussion and recommendations (pp. 8–9)

- **S6.1 — Section synthesis:** Cooling is the primary water-use driver; without targeted intervention global consumption could rise sharply by mid-century. The framework identifies mitigation levers under uncertainty. Its closing recommendations integrate efficient cooling, electricity sourcing, embodied water, disclosure, and regional siting rather than relying on energy decarbonisation alone.

### §6.1. Interpreting the scenarios: Trade-offs and leverage points (p. 8)

- **S6.1a:** Model complexity and compute growth drive potentially dramatic BAU demand, but efficient cooling and moderated infrastructure expansion could substantially reduce consumption even with moderate compute growth.
- **S6.1b:** The authors say the appendix confirms operational water dominates and is most responsive to WUE/PUE improvements. Embodied water is smaller but remains relevant as refresh cycles shorten. The appendix itself additionally emphasises EWIF (AP1–AP3).
- **S6.1c — Subsection conclusion:** Energy decarbonisation alone cannot achieve water sustainability; design and operations must integrate water, energy, and emissions.

### §6.2. Probabilistic scenario-based framework: Strengths and limitations (pp. 8–9)

- **S6.2a:** Combining expert judgement and scenarios handles uncertainty transparently in fast-changing, data-scarce settings and permits credible forecasts without comprehensive histories. Private firms' commercial/security concerns limit disclosure, reinforcing the value of such forecasting tools for policy.
- **S6.2b — Stated limitation:** Although variables interact through deterministic equations, probabilistic inputs are treated independently, with **no statistical dependence/correlation modelled**. This may omit important relationships under simultaneous technological/policy changes.
- **S6.2c — Subsection conclusion:** Technological disruption and regional feedback may create nonlinear effects future models should capture. Real-time monitoring and a dynamic Bayesian framework are promising ways to improve accuracy.

### §6.3. Interpretation of results and policy implications (p. 9)

- **S6.3a:** Without targeted intervention, water consumption could rise nearly sevenfold by 2050. Water is an underappreciated AI-scaling impact; climate-style policy tools, scenario planning, and regulatory foresight may help govern it.
- **S6.3b:** Conflicts are emerging where expansion overlaps water stress and are likely to intensify with extreme weather and climate variability. Utilities/regulators have signalled possible drought/peak-demand restrictions. Water must be a core infrastructure-planning concern.
- **S6.3c — Qualification concerning AI benefits:** AI for smart grids, building optimisation, climate forecasting, and ecosystem monitoring can improve energy/water efficiency and aid mitigation/adaptation. Encouraging environmentally focused AI while managing large generative models' resource intensity could align digital innovation with sustainability.
- **S6.3d:** Reductions require efficient liquid/immersion cooling, renewable and low-water electricity, and embodied-water regulation in procurement/life-cycle assessment. International reporting and location-planning standards could prevent cross-border water-stress clustering. The authors cite the EU Green Deal and California conservation regulation as promising models.
- **S6.3e:** AI energy optimisation and modular data-centre design could reduce operational and embodied water consumption.
- **S6.3f — Enumerated recommendation 1:** Accelerate low-water, closed-loop direct-liquid and immersion cooling.
- **S6.3g — Enumerated recommendation 2:** Use grey-water and non-potable cooling supplies, especially under municipal water stress. This recommendation concerns water sources; it does not expand the model to grey water footprint accounting.
- **S6.3h — Enumerated recommendation 3:** Promote real-time cooling optimisation using AI management systems.
- **S6.3i — Enumerated recommendation 4:** Require disclosure of WUE, EWIF, and EWU in sustainability reporting.
- **S6.3j — Enumerated recommendation 5:** Include water availability in siting decisions to avoid already stressed clusters.
- **S6.3k:** Waste-heat reuse for residential/district heating may indirectly reduce energy and water consumption. It is explicitly **not modelled**, and should be evaluated alongside cooling and siting improvements.
- **S6.3l — Subsection/section conclusion:** Economic factors, electricity prices/renewables, tax incentives, and land availability often drive clusters more than hydrological suitability. Integrating climate and water stress into siting and adapting the global framework to regional climate, WUE, and local energy-water interactions could align digital expansion with sustainability and avoid freshwater conflicts.

### §7. Conclusions (pp. 9–10)

- **S7.1:** The novel probabilistic scenario framework is presented as a significant advance in projecting AI infrastructure's environmental effects: it quantifies on-site/off-site/embodied water and forecasts through 2050 under alternative technological growth and efficiency assumptions.
- **S7.2:** It is a flexible strategic-planning tool for data-scarce settings, identifies cooling efficiency and compute growth as major levers, and can support design, reporting, and policy.
- **S7.3:** If current trends remain unchecked, global data-centre water consumption **could grow more than sevenfold by mid-century**. This is avoidable through improved cooling, alternative water supplies, and climate-aligned siting.
- **S7.4 — Regional extension:** A regional summation with local WUE, EWIF, and embodied-water intensity would better represent uneven infrastructure and environmental pressure. Future models should incorporate country-level climate, infrastructure, electricity mix, regulation, centre density, cooling adoption, and water stress to improve siting/governance guidance.
- **S7.5 — Further research:** Explore dynamic Bayesian integration of real-time observations and a unified water-energy-emissions sustainability metric.
- **S7.6 — Quantified mitigation conclusion:** Improvements in WUE, EWIF, and hardware lifecycle management/EWU **could reduce 2050 water use by up to 95% relative to BAU**. With suitable technology, policy, and foresight, digital growth and environmental responsibility can advance together.
- **S7.7 — Enumerated action 1:** Accelerate immersion and closed-loop cooling deployment.
- **S7.8 — Enumerated action 2:** Standardise operational and embodied water accounting.
- **S7.9 — Enumerated action 3:** Enforce climate-aware siting reflecting regional water constraints.
- **S7.10 — Enumerated action 4:** Fund research, development, and demonstration of water-efficient AI hardware/systems.
- **S7.11 — Closing conclusion:** Coordinated industry, regulatory, and research action is necessary to realise reductions. Greater provider transparency, particularly real-time water reporting, would improve forecasting and long-term infrastructure planning.

### Appendix. Sensitivity analysis (p. 10)

- **AP1 — Scope:** Tests **±20% changes** in WUE, PUE, EWIF, and EWU against the **2050 BAU baseline of 28.11 billion litres/day**; Fig. A.7 is a relative tornado plot and Table A.3 reports absolute and relative differences.
- **AP2 — Ranking:** WUE has the strongest influence, closely followed by EWIF and PUE, governing operational water; amortised embodied water/EWU has a smaller but still relevant effect.
- **AP3 — Quantified claims:** A 20% WUE improvement reduces demand by **4.69 billion litres/day**, with a similar increase for deterioration. The corresponding stated absolute effects are **4.24** for EWIF, **4.02** for PUE, and **1.29** for EWU, all billion litres/day. Table A.3 reports relative differences of **16.7%, 15.1%, 14.3%, and 4.6%**, respectively.
- **AP4 — Appendix conclusion:** Cooling and power-infrastructure improvements offer the greatest long-term reduction potential, but hardware design and procurement improvements also belong in water-sustainability strategies.

## 4. Every figure: location, contents, and asserted significance

- **F1 — Fig. 1, p. 4; discussed in §2.1, p. 3:** Scatter plot of **training computation (petaFLOP)** against **publication date**, with logarithmic vertical scale and points coloured by model domain (biology, games, image generation, language, multiple domains, other, speech, vision). It shows a large historical rise in training compute, including dense recent high-compute models; the text uses it to support continued/accelerating infrastructure demands. The caption attributes the source to OurWorldinData and says estimates are accurate within a factor of **2**, or **5** for recent undisclosed models such as GPT-4. The caption itself prints petaFLOP as **10^5 floating-point operations**; preserve this printed statement if checking quotation rather than silently substituting another exponent.
- **F2 — Fig. 2, p. 4; §3.1:** Traditional air-cooling schematic. Outside air enters a mixing room/fan; blue arrows show cool airflow through the raised-floor space and server racks; red arrows show warmed air through the upper/false-ceiling space and hot-air outlet. It illustrates air circulation and heat rejection, accompanying the low-direct-water/high-energy trade-off. It provides no numerical water estimate.
- **F3 — Fig. 3, p. 5; §3.2, p. 4:** Evaporative-cooling schematic showing a **cooling tower**, **heat exchanger/chiller**, pumps, and **data-centre air circulation**. Red/blue arrows distinguish hot/cool paths; heat passes from the centre through the exchanger to the tower, where heat is rejected with evaporation. It illustrates the heat-removal mechanism underlying the discussion of efficient but water-intensive evaporative cooling.
- **F4 — Fig. 4, p. 5; §3.3:** Direct-liquid schematic linking a server **rack**, circulating liquid/pumps, **heat exchanger/chiller**, and an external **cooling tower**, with red/blue arrows for hot/cool flow. The adjoining text explains heat uptake through component cold plates, exchange, and recirculation, supporting high-density cooling and reduced reliance on evaporative systems. The drawing **does include a cooling tower**; it should not be described as visually proving elimination of evaporative heat rejection or zero water use.
- **F5 — Fig. 5, p. 6; §4, pp. 5–6:** World bubble map of **2025 data-centre numbers and national water stress**. Bubble area represents facility counts; colour represents low (green), medium, medium-high, high, extremely high (purple), or unknown (grey) stress. The US has by far the largest bubble, coloured medium-high; India and Spain are high-stress examples, while much of northern/western Europe is lower stress. It displays uneven deployment and possible mismatch with water availability. Facility counts come from Data Center Map (2025), stress classifications from World Resources Institute (2024). The figure's stress coding is **national**, not a facility-level basin measurement. The caption mentions interactive/data versions, which were not accessed.
- **F6 — Fig. 6, p. 8; §5.2:** Three **2025–2050** mean trajectories with shaded **90% credible intervals**. BAU rises steeply with a widening band, moderate intervention rises more slowly, and sustainable transformation declines. This supports the text's relative scenario ordering and mitigation argument. **As printed**, the vertical axis reads “Global Water Use (billion litres/day)” with ticks around **0.005–0.035**; the 2050 means appear near **0.031, 0.010, and 0.003**, respectively. These plotted coordinates do **not** reproduce Table 2's numerical scale/means. Record the plot's trend and the table's values separately rather than replacing one with the other.
- **F7 — Fig. A.7, p. 10; Appendix:** Horizontal tornado plot of **relative change in 2050 water use (%)** under **−20%** (red, left) and **+20%** (blue, right) parameter changes, relative to BAU. WUE has the widest bars, then EWIF, PUE, and the smallest embodied-water bar. Approximate plotted magnitudes are WUE **−8%/+9%**, EWIF **−7%/+7.5%**, PUE **−6.5%/+7%**, and the embodied parameter **−2%/+2.5%**. The top axis label is printed **“EWE”**, whereas the text/table call the parameter **EWU**. These individual bar magnitudes differ from Table A.3's listed relative differences; both elements should be represented as printed. The figure supports the sensitivity ranking, not an unqualified substitution of its bar endpoints for the table's values.

## 5. Every table: location and complete contents

### T1 — Table 1, p. 5: Comparison of cooling technologies in AI data centres

| Cooling method | Water volume | Energy efficiency | Adoption level |
| --- | --- | --- | --- |
| Air-based | Low | Moderate–Low | High |
| Evaporative | High | High | High |
| Direct liquid cooling | Low | Very high | Emerging |
| Immersion cooling | Very low | Very high | Limited |

**What it shows:** Qualitative trade-offs: widespread air cooling uses little direct water but is less energy efficient; widespread evaporative cooling is energy efficient but water intensive; direct liquid and immersion combine low/very low water with very high energy efficiency, with less mature adoption. There are **four rows**, although §3.4 refers to “three main cooling technologies.”

### T2 — Table 2, p. 7: Probabilistic scenario projections

All values are **billion litres/day**; entries are **mean [90% credible interval]**, as specified in §5.2.

| Scenario | 2030 | 2050 |
| --- | --- | --- |
| Business-as-usual (BAU) | 4.18 [3.67–4.68] | 28.11 [24.71–31.47] |
| Moderate intervention | 3.06 [2.68–3.44] | 8.36 [7.31–9.72] |
| Sustainable transformation | 1.86 [1.63–2.09] | 1.38 [1.15–1.61] |

**What it shows:** Strong scenario divergence by 2050: BAU rises nearly sevenfold from its 2030 mean, moderate demand rises less, and sustainable demand declines. These are conditional scenario projections, not observations or unconditional predictions. Fig. 6's printed axis scale and coordinates differ; see F6.

### T3 — Table A.3, p. 10: Sensitivity differences under ±20% shifts

The table gives **2050 BAU baseline = 28.11 billion litres/day**. “Relative diff.” and “Abs. diff” below reproduce its headings and values; the table does not separately list each signed perturbation.

| Parameter | Relative diff. (%) | Absolute difference (billion litres/day) |
| --- | --- | --- |
| WUE | 16.7% | 4.69 |
| PUE | 14.3% | 4.02 |
| EWIF | 15.1% | 4.24 |
| EWU | 4.6% | 1.29 |

**What it shows:** WUE has the largest reported sensitivity, followed by EWIF, PUE, and EWU. The appendix prose interprets 4.69 as the reduction for a 20% WUE improvement and says deterioration increases use similarly. Do not silently reinterpret that prose, or conflate the table's relative differences with Fig. A.7's individual signed bar endpoints.

## 6. Equations and algorithm supporting the claims

- **E1 — Eq. (1), §2.2, p. 3:** `W_tot(t) = W_o(t) + W_x(t) + W_e(t)`: total water is on-site operational, off-site electricity, plus embodied water.
- **E2 — Eq. (2), §2.2, p. 3:** `W_o(t) = e(t) × rho_o(t)`: server electricity `e(t)` in kWh/day times WUE in litres/kWh gives on-site volume.
- **E3 — Eq. (3), §2.2, p. 3:** `W_x(t) = e(t) × theta(t) × rho_x(t)`: server electricity times PUE times EWIF gives electricity-related off-site water.
- **E4 — Eq. (4), §2.2, p. 3:** `W_e(t) = T × W / T_0`: manufacturing water `W` is allocated over expected equipment life `T_0` (years), for analysis duration `T`. This records the equation as written rather than imposing an additional turnover model.
- **E5 — Eq. (5), §5.1, p. 7:** `e(2025) ~ Normal(mu = 1.0 × 10^9, sigma = 0.1 × 10^9)`, in kWh/day.
- **E6 — Eq. (6), §5.1, p. 7:** `CI_90%(W_t) = [q_0.05, q_0.95]`, the empirical central interval from **N = 10,000** simulated outputs.
- **ALG1 — Algorithm 1, p. 8:** Inputs comprise baseline electricity prior, initial WUE/PUE/EWIF, each efficiency's annual improvement rate, baseline embodied water, equipment life, and scenario growth `g`. For each scenario and each year 2025–2050, set `y = t − 2025`, sample baseline electricity, project it as `e(t) = e(2025)(1+g)^y`, and decrease WUE/PUE/EWIF using their respective `(1 − improvement rate)^y` factors. Embodied water is `W_emb(2025)(1 − EWU*)^y / T_0`. Compute on-site and off-site components, divide their sum and embodied water by `10^9` for the displayed total, and store means/intervals. Asterisks designate annual efficiency improvement rates. The title says “annual water consumption,” while the surrounding forecasts and Table 2 are expressed as daily volumes; preserve the distinction between projection year and units.

## 7. End matter and coverage notes

- **CRediT statement, p. 10:** Assigns conceptualisation, data curation, analysis, investigation, methodology, software, supervision, validation, visualisation, and writing roles to the named authors. It is not an enumerated list of scientific contributions.
- **Declaration of competing interest, p. 10:** Authors declare no known competing financial interests or personal relationships that could have appeared to influence the work.
- **Data availability, p. 10; front-page note, p. 1:** The article states supporting data/code are openly available at `https://github.com/manuelhf/waterforAI`; the front-page note describes part of the data, visualisation, and code as available through linked GitHub resources and states the accepted-manuscript CC BY arrangement. Availability was recorded, not checked externally.
- **Language and comparison boundaries:** “More than sevenfold” in the abstract/conclusion and “nearly sevenfold between 2030 and 2050” in §5.2 are both preserved. The explicitly specified sevenfold comparison is 2030–2050 BAU in Table 2; do not invent a different baseline for less specific passages. “Up to 95%” is a conditional 2050 reduction **relative to BAU**. The sustainable scenario assumes **no further compute growth**, so its water decline should retain that condition. The abstract's sensitivity claim mentions compute growth and efficiency broadly; the actual appendix perturbation exercise covers only WUE/PUE/EWIF/EWU, with compute growth compared through the three scenarios.

**Coverage check:** 3 enumerated Highlights; additional contribution statements C1–C5; 8 abstract claims; all numbered main sections (§§1–7) and every numbered subsection (§§2.1–2.2, 3.1–3.4, 5.1–5.2, 6.1–6.3); Appendix conclusion; all **7 figures** (Figs. 1–6 and A.7); all **3 tables** (Tables 1, 2, A.3); all **6 numbered equations** and Algorithm 1. The inventory ends after the appendix and p. 10 end matter; the remaining pages contain references.
