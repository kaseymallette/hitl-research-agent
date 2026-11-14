# Claims reference: article.pdf

## Source, scope, and use

Pengfei Li, Jianyi Yang, Mohammad A. Islam, and Shaolei Ren, **“Making AI Less ‘Thirsty’,”** *Communications of the ACM* 68(7), July 2025, pp. 54–61, DOI 10.1145/3724499. Deck: “Uncovering and addressing the secret water footprint of AI models.”

This inventory was prepared from `article.pdf` alone, after reading `RUBRIC.md`. Locations below use printed page numbers; PDF pages 1–8 correspond to printed pp. 54–61. The article's substantive text ends with **Conclusion**, p. 61. There are **no appendices**. The acknowledgment, references, author biographies, and license follow on p. 61; they add no substantive research conclusions. Both footnotes, all displayed equations, both numbered figures (including every panel), the sole table, and the unnumbered opening illustration are accounted for below. All claim descriptions are paraphrases, except short quoted labels.

The article has **no labeled abstract and no formally enumerated contributions**. Do not count an abstract or numbered contribution list as missed. Its deck and introductory roadmap make summary claims; these are inventoried explicitly below. Contribution IDs inventory six distinct items in that prose roadmap, not an enumeration supplied by the authors. Section/conclusion IDs include definitions, methodological results, and recommendations where those are the endpoint of an expository subsection. Repeated claims are cross-referenced rather than treated as independent findings. Figures F1–F2 and table T1 are separate coverage units; F2 has three panels. This is an inventory of the authors' positions and supporting particulars, not an assessment of their validity.

## Introductory summary and stated contributions

- **S1 — Deck and opening framing (p. 54).** AI models have a largely hidden water footprint that needs to be uncovered and addressed. AI enables important breakthroughs, including help with climate challenges, but large generative models' energy-intensive training and deployment increase datacenter energy use. Carbon scrutiny has driven efficiency progress, whereas water use for cooling and electricity generation remains relatively overlooked and is escalating. If inadequately addressed, it could become a major sustainability obstacle and cause social conflicts because usable freshwater is limited and unevenly distributed.
- **K1 — Holistic sustainability framing (p. 56, introductory roadmap).** The authors advocate extending sustainable AI beyond carbon accounting to include water.
- **K2 — Estimation methodology (p. 56).** They present a principled methodology for estimating total AI water footprint, including operational and embodied water (developed on pp. 58–59).
- **K3 — GPT-3 case study (p. 56).** For 175-billion-parameter GPT-3, training in Microsoft's U.S. datacenters can consume about **5.4 million L**, including about **700,000 L onsite**. Roughly **10–50 medium-length responses** can consume **500 mL**, depending on deployment time and location. These are estimates, not measurements of a disclosed training run. Table 1 supplies location-specific operational estimates, and its full range is wider than the introductory response shorthand.
- **K4 — Spatial and temporal water efficiency (p. 56).** WUE varies across place and time; judiciously choosing when and where to train a large model can significantly reduce its water footprint.
- **K5 — Transparency (p. 56).** More operational data should be disclosed, and users should be informed of runtime water efficiency.
- **K6 — Water–carbon coordination (p. 56).** Truly sustainable AI requires addressing water together with carbon; water footprint can no longer remain overlooked.

## Section and subsection claims, in article order

### Unheaded introduction (pp. 54, 56)

- **C01 — Growth and urgency (p. 54).** Expanding AI products and services are a key driver of rapidly growing datacenter water consumption. As supporting context, one technology company's self-owned datacenters, excluding leased colocation facilities, withdrew **29 billion L** and consumed **more than 23 billion L** for onsite cooling in **2023**, nearly **80%** potable water. This consumption rivals a major beverage company's. That company's consumption grew approximately **20%** in 2021–2022 and **17%** in 2022–2023; another company's grew approximately **34%** and **22%**, respectively. These are datacenter-wide figures used to motivate the AI issue, not an allocation solely to AI.
- **C02 — Datacenter projection (p. 54).** The cited U.S. datacenter energy report projects that annual U.S. datacenter onsite consumption in **2028 could double or quadruple 2023 levels**, reaching roughly **150–280 billion L**, further stressing water infrastructure.
- **C03 — AI projections (pp. 54, 56).** AI is the fastest-expanding datacenter workload. One cited study suggests global AI electricity use of **85–134 TWh in 2027**; a more aggressive cited projection puts U.S. AI-server electricity consumption alone above **150–300 TWh in 2028**. Using the lower global estimate, the authors project combined scope-1 and scope-2 global AI withdrawal of **4.2–6.6 billion m³ in 2027**, more than four to six Denmarks' or half the U.K.'s annual withdrawal, and consumption of **0.38–0.60 billion m³**. The U.S. alone in 2028 would exceed these global water estimates **if** the cited U.S. energy projection materializes.
- **C04 — Accounting boundary (p. 56, footnote b).** Water scopes follow the carbon-emissions scope framework. Throughout the article, scope-2 water is for **location-based electricity generation**. Renewable purchasing or other offset programs may yield lower **market-based** carbon and water footprints; those are distinct from the estimates here. Footnote a (p. 54) points forward to the withdrawal/consumption distinction.
- **C05 — Attention and complementary metrics (p. 56).** AI water use receives disproportionately little attention from the AI community and public. Model cards routinely include scope-2 carbon emissions but omit even scope-1 direct water usage, whether withdrawal or consumption, as well as scope 2. This may impede sustainability innovation. Carbon and water footprints are complementary, not substitutable: optimizing carbon need not improve water efficiency and may worsen it, because water efficiency responds to electricity fuel mixes and weather differently.
- **C06 — Introduction's concluding position (p. 56).** Uncovering and addressing AI's water footprint is urgent if AI growth is not to exacerbate water stress or outweigh its environmental benefits, given scarcity, drought, and aging infrastructure. Industry commitments to being water positive by 2030 and inclusion of water in a forthcoming ISO/IEC sustainable-AI standard reflect the urgency. The introductory roadmap ends with K1–K6, especially the demand for transparency and combined water/carbon sustainability.

### Background (pp. 56–58)

#### Water withdrawal versus water consumption (pp. 56–57)

- **C07 — Withdrawal.** Withdrawal is freshwater taken temporarily or permanently from surface or ground sources for agricultural, industrial, or municipal uses, normally excluding hydroelectric generation. It indicates sectors' competition for and dependence on finite shared water resources.
- **C08 — Consumption and subsection conclusion.** Consumption is withdrawal minus discharge: water evaporated, transpired, incorporated into products/crops, or otherwise removed from the immediate water environment. It reflects downstream availability and is important for watershed scarcity. These yield different footprints, WWF and WCF. **“Water footprint” defaults to consumption footprint (WCF)** in the article unless otherwise specified.

#### How does AI use water? (pp. 57–58)

- **C09 — Three-scope framework (p. 57).** AI uses onsite water for datacenter cooling (**scope 1**), offsite water for electricity generation (**scope 2**), and supply-chain water for server manufacturing (**scope 3**).
- **C10 — Scope-1 water usage: two cooling stages (p. 57).** Nearly all server energy becomes heat that must be removed. Server-level cooling transfers heat to the facility or heat exchanger using air or liquid, including direct-to-chip and immersion cooling; this stage does **not** evaporate or consume water. High power densities often lead new AI-training datacenters to use liquid cooling. Facility-level cooling rejects heat outdoors; cooling towers and evaporation-assisted air cooling are common, water-intensive methods. Liquid cooling at the server does not by itself establish facility water consumption.
- **C11 — Cooling tower (p. 57; F1).** Some water evaporates to reject heat; remaining water circulates to absorb server heat. Non-evaporated water is typically recycled only **3–10 cycles**, depending on quality, before discharge. Freshwater must replace both evaporated and discharged water, preventing mineral/salt accumulation; clean, often potable water also avoids clogs and bacterial growth. Withdrawal includes both replacement components; consumption is only evaporation. With good water quality, about **80%** of withdrawal is consumed. Reported evaporation is approximately **1–9 L/kWh of server energy**, dependent on weather and operating settings: **1 L/kWh** is Google's annual global onsite average, whereas **9 L/kWh** is a commercial Arizona datacenter in summer, not a universal datacenter rate.
- **C12 — Air cooling with water evaporation assistance (p. 57).** Favorable climates permit outside-air cooling, but evaporation is still needed when air is too hot (for example, above **85°F**) and water may be needed for humidity control when too dry. Meta reports about **70%** of added water consumed. Outside-air cooling is generally more water-efficient on average than cooling towers, but hot weather raises evaporative demand and peak consumption, potentially stressing local supplies when demand is high. Hot regions and business-district colocation facilities may face application challenges.
- **C13 — Dry-cooler qualification and scope-1 conclusion (pp. 57–58).** Dry coolers can eliminate onsite water consumption year-round, but typically increase cooling electricity use relative to water-based cooling, potentially increasing scope-2 water consumption and overall water-resource stress. Eliminating onsite consumption alone does not establish a lower overall water cost.
- **C14 — Scope-2 water usage (p. 58).** Thermoelectric generation is among leading water-withdrawal and consumption sectors in many countries. Datacenters are accountable for electricity-related offsite water as part of their true water cost. Rates differ with power plants and cooling technologies. Hydropower withdrawal is typically excluded, while increased evaporation due to hydropower is included as consumption. The article cites U.S. averages of about **43.8 L/kWh withdrawn** and **3.1 L/kWh consumed**, and Meta's reported **3.7 L/kWh** global datacenter scope-2 consumption in 2023 (**55,475 ML / 14,975,435 MWh**).
- **C15 — Scope-3 water usage (p. 58).** Chip/server manufacturing uses large quantities of water, including ultrapure wafer-fabrication water and plant cooling water; discharge may contain toxic chemicals or hazardous waste. Recycling can reduce withdrawal but is often low: cited Singapore averages are **45% for wafer plants** and **27% for semiconductor plants**. Though obscure, scope-3 water is **likely significant**; Apple's supply chain accounting for **99%** of its total water footprint is supporting context, not a measured AI supply-chain share.
- **C16 — Background's closing distinction (p. 58).** Unlike agriculture, whose footprint is mostly green water held in soil and used by plants, most of AI's water footprint is **blue water** from rivers, lakes, or groundwater, directly available for human use but often more limited.

### Estimating AI's Water Footprint (pp. 58–60)

- **C17 — Section's method and boundary (p. 58).** The general methodology estimates consumption footprint. Replacing WUE with water-withdrawal efficiency yields withdrawal footprint.

#### Operational water footprint (pp. 58–59)

- **C18 — Onsite WUE (p. 58).** Operational water combines scopes 1 and 2. Onsite WUE, `rho_s1,t`, is onsite water consumption divided by **server energy** at time `t`. It varies with weather: cooling-tower WUE rises significantly with wet-bulb temperature; outside-air cooling WUE rises with excessive dry-bulb temperature or low humidity. A larger L/kWh value means more water used per unit energy.
- **C19 — Offsite WUE (p. 58).** Offsite WUE, `rho_s2,t`, is water consumption per kWh of electricity (EWIF). One common estimate is the generation-weighted average `rho_s2,t = sum_k(b_k,t * EWIF_k) / sum_k(b_k,t)`, where `b_k,t` is generation from fuel `k` on the serving grid at time `t`. Changing grid fuel mixes produce temporal and regional differences in offsite WUE.
- **C20 — Operational formula and subsection conclusion (pp. 58–59).** For time slots `t = 1,...,T`, server energy `e_t`, and datacenter PUE `theta_t` covering non-IT overhead, the model's operational footprint is `WaterOperational = sum_t e_t * [rho_s1,t + theta_t * rho_s2,t]`. Server energy can be obtained from power meters or built-in server tools; slot length depends on desired assessment frequency. The onsite term uses server energy directly, while the offsite term uses PUE-adjusted energy.

#### Embodied water footprint (p. 59)

- **C21 — Amortization.** As with embodied carbon, scope-3 manufacturing water is amortized over server lifespan. If manufacturing uses `W` water and expected service duration is `T0`, allocated embodied water over duration `T` is `WaterEmbodied = T * W / T0`.
- **C22 — Total-footprint conclusion.** Total water is operational plus embodied: `WaterTotal = sum_t e_t * [rho_s1,t + theta_t * rho_s2,t] + T * W / T0`. Annualized average WUE and estimated AI-server energy can provide a **rough** practical estimate. These equations are methodological expressions, not independently measured outcomes.

#### Case Study: Estimating GPT-3's operational water-consumption footprint (pp. 59–60)

- **C23 — Case boundary (p. 59).** The case estimates operational consumption for full **175-billion-parameter GPT-3**. It **excludes embodied water because public scope-3 data are lacking**. GPT-3 is selected because Microsoft publishes location-specific WUE and PUE. The article describes ChatGPT as based on subsequent versions of GPT-3; the numerical case is specifically GPT-3, not a measurement of all ChatGPT versions. Results are in T1.
- **C24 — Training assumptions (p. 59).** GPT-3 training energy is estimated at **1,287 MWh**. The authors use Microsoft's most recent annualized location-specific PUE/WUE and Reig et al.'s EWIF for consistent estimation across regions. Their U.S. EWIF is about **3.14 L/kWh**, below the **4.35 L/kWh** in the more recent U.S. report. The actual GPT-3 training location is undisclosed; the table therefore considers multiple Microsoft locations, excluding Singapore and Taiwan for lack of EWIF data. Starred locations have projected PUE/WUE, as specified in T1.
- **C25 — Training result (pp. 56, 59; T1).** The U.S.-average case is **5.439 million L** operational training consumption, comprising **0.708 million L onsite** and **4.731 million L offsite**; this is the source of the introductory rounded 5.4 million/700,000 figures. Location substantially changes the estimates. They are alternative location scenarios, not evidence that GPT-3 was trained in all these locations.
- **C26 — Inference task and energy assumptions (pp. 59–60).** The representative conversation request has approximately **≤800 input words and 150–300 output words**, with a CPU-intensive prompt phase and memory-intensive token phase. An official estimate gives about **0.4 kWh per 100 pages**, or **0.004 kWh/page**; details are unavailable and the authors think it likely covers only token-generation GPU energy. To include the prompt and non-GPU server energy, they **assume 0.004 kWh of server energy per request** for their task. They use the same PUE, WUE, and EWIF as in training. The page-based source estimate and the assumed per-request energy are distinct steps.
- **C27 — Inference results and conservatism (p. 60; T1).** The authors characterize their GPT-3 inference estimate as conservative; actual consumption **could be several times higher**. Supporting comparisons for medium-sized conversation requests under response-time SLOs, enterprise Nvidia DGX H100 systems, a state-of-the-art inference solution, and non-GPU overhead are about **0.010 kWh for Llama-3-70B** and **0.016 kWh for Falcon-180B** (similar in size to GPT-3-175B). These are comparisons, not reported GPT-3 energy measurements.
- **C28 — Deployment and EWIF qualifications (p. 60).** Microsoft's onsite WUE is already among the industry's lowest; third-party colocation could make direct scope-1 consumption several times higher for the same model. The chosen U.S. EWIF is also conservative relative to the newer 4.35 L/kWh estimate.
- **C29 — Case-study and estimation-section closing outlook (p. 60).** Although no official resource-consumption information is available, subsequent models such as GPT-4 **could** use substantially more energy and water for the same request, particularly in reasoning mode. Efficiency and computation reductions **may** lower per-request water use, but total consumption is **likely** to keep rising with AI-service demand and application scale.

### Our Recommendations (pp. 60–61)

- **C30 — Section's purpose (p. 60).** Scheduling and policy recommendations address AI water footprint to make future AI more environmentally sustainable; its substantive conclusions are C31–C35.

#### More transparency and comprehensive reporting (pp. 60–61)

- **C31 — Model/user reporting (p. 60).** Model cards omit water consumption despite routinely reporting carbon. Limited transparency may obstruct innovation. The authors recommend tracking and reporting AI water consumption through **model cards and/or cloud dashboards** as an initial step to inform users about the water effects of their usage.
- **C32 — Scope-2 reporting (p. 60).** Comprehensive scope-2 understanding/reporting remains limited; climate-conscious cooling designs mainly reduce scope 1 while largely overlooking scope 2. Addressing electricity-related water is as crucial to true water-cost reduction as addressing scope-2 carbon is to climate mitigation. Meta has begun including scope 2 in sustainability reporting. The authors recommend **standard scope-2 water-consumption reporting**, making offsite consumption visible to developers and users and potentially enabling demand-side flexibility that alleviates total water-resource strain.
- **C33 — Scope-3 research and subsection conclusion (p. 61).** Despite a large supply-chain footprint, chip-manufacturing embodied-water data are limited. The authors recommend more research on scope-3 consumption to understand AI's overall footprint comprehensively and foster corporate water stewardship.

#### 'When' and 'where' matter (p. 61)

- **C34 — Scheduling conclusion.** Weather-driven onsite efficiency and grid-fuel-mix-driven offsite efficiency vary across time and place (F2). Dynamic scheduling of both training and inference can cut the footprint. Examples are training at midnight and/or at a more water-efficient datacenter. **If informed** of real-time efficiency, some water-conscious users **may** choose more efficient times/locations for inference, enabling demand-side flexibility. Midnight is an example, not an unconditional universal optimum.

#### 'Follow the Sun' or 'Unfollow the Sun' (p. 61)

- **C35 — Trade-off and recommendation-section conclusion.** Abundant solar energy favors following the sun for carbon reduction; avoiding high-temperature, high-WUE hours may favor unfollowing it for water reduction. F2a–b illustrate misalignment of scope-2 water intensity and carbon emission rates: minimizing one **might increase** the other. Carbon and water impacts are not substitutable. Holistic, carbon-efficient and water-wise approaches are needed to reconcile potential conflicts, rather than optimizing either metric alone.

### Conclusion (p. 61)

- **C36 — Concern and method.** AI water usage is critical to socially responsible and environmentally sustainable AI; the article presents a principled estimation method (K1–K2).
- **C37 — Scale of training.** GPT-3 illustrates that large-model training can consume millions of liters (K3, C25).
- **C38 — Scheduling leverage.** Scope-1 and scope-2 efficiencies vary spatially and temporally; choosing where and when to run a large model can significantly reduce water footprint (K4, C34).
- **C39 — Reporting and coordinated sustainability.** Greater transparency and comprehensive reporting are recommended, and sustainable AI requires addressing water together with carbon (K5–K6, C31–C35).
- **C40 — Final normative conclusion.** AI water footprint must become a **priority** in collective efforts to combat global water challenges; it can no longer remain overlooked.

## Figures and other visual material

- **F1 — Figure 1 (p. 57; PDF p. 4), operational water schematic.** Shows both onsite scope-1 cooling-water use and offsite scope-2 power-generation water use. A datacenter cooling tower and heat exchanger move heat from a server-rack/CRAH chilled-water loop to the outside; a separate power plant with cooling tower draws from a water source and supplies electricity to the datacenter. The schematic distinguishes water used directly for cooling from water used indirectly in generating electricity. It illustrates a cooling-tower arrangement, not all cooling systems; the AI-model icons are illustrative only. Read alongside C10–C14.
- **F2 — Figure 2 (p. 60; PDF p. 7), three panels on carbon/water efficiency and electricity fuel mixes.**
  - **F2a:** U.S. eGRID-region **scope-2 water consumption intensity (L/kWh)** plotted against **carbon emission rate (kg/kWh)**, with a dashed linear regression. The plotted regional variation and fitted line show the efficiencies are **not aligned**; lower carbon intensity does not consistently imply lower water intensity. The figure is not an onsite cooling comparison.
  - **F2b:** A **five-day Virginia snapshot beginning April 4, 2022**, with hourly scope-2 water intensity and carbon emission rates calculated from fuel mixes and fuel-specific factors. Water intensity varies markedly and its peaks/troughs do not track carbon reliably; the caption reports **Pearson correlation 0.06** for Virginia. This is a specific location/time illustration, not a global correlation estimate.
  - **F2c:** Hourly percentage electricity fuel mixes serving Virginia for the **same five days**: coal, natural gas, nuclear, oil, wind, solar, hydro, and other. It displays changing generation composition behind time-varying offsite efficiencies. Together the panels support temporal/spatial scheduling opportunities and potential water–carbon conflicts (C19, C34–C35).
- **V1 — Unnumbered full-page opening illustration (p. 55; PDF p. 2).** Server racks surrounded by flowing water beneath large waterfalls; it visually introduces the water-footprint theme. It has no quantitative evidentiary claim and is separate from the two numbered scientific figures.

## Table

### T1 — Table 1 (p. 59; PDF p. 6): estimate of GPT-3's operational water consumption footprint

The table compares **18 rows** (U.S. average plus 17 location scenarios), giving PUE, onsite WUE (L/kWh), offsite EWIF (L/kWh), onsite/offsite/total training consumption (**million L**), onsite/offsite/total consumption for each request (**mL**), and requests consuming **500 mL**. It shows substantial location dependence and that offsite consumption exceeds onsite consumption in every listed row, including an India scenario with zero onsite consumption but positive total consumption. It estimates **operational consumption**, not withdrawal or embodied water. Assumptions and limitations are C23–C28.

An asterisk means **under construction as of July 2023**, with **Microsoft-projected PUE and WUE**, not observed operating figures. All values below are as printed; they are not recalculated.

| Location | PUE | Onsite WUE L/kWh | Offsite EWIF L/kWh | Training onsite million L | Training offsite million L | Training total million L | Request onsite mL | Request offsite mL | Request total mL | Requests / 500 mL |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| U.S. Average | 1.170 | 0.550 | 3.142 | 0.708 | 4.731 | 5.439 | 2.200 | 14.704 | 16.904 | 29.6 |
| Arizona | 1.180 | 1.630 | 4.959 | 2.098 | 7.531 | 9.629 | 6.520 | 23.406 | 29.926 | 16.7 |
| Georgia* | 1.120 | 0.060 | 2.309 | 0.077 | 3.328 | 3.406 | 0.240 | 10.345 | 10.585 | 47.2 |
| Illinois | 1.350 | 0.740 | 2.233 | 0.952 | 3.880 | 4.833 | 2.960 | 12.060 | 15.020 | 33.3 |
| Iowa | 1.160 | 0.140 | 3.104 | 0.180 | 4.634 | 4.814 | 0.560 | 14.403 | 14.963 | 33.4 |
| Texas | 1.280 | 0.250 | 1.287 | 0.322 | 2.120 | 2.442 | 1.000 | 6.590 | 7.590 | 65.9 |
| Virginia | 1.140 | 0.140 | 2.385 | 0.180 | 3.499 | 3.679 | 0.560 | 10.875 | 11.435 | 43.7 |
| Washington | 1.150 | 0.950 | 9.501 | 1.223 | 14.063 | 15.285 | 3.800 | 43.706 | 47.506 | 10.5 |
| Wyoming | 1.110 | 0.130 | 2.574 | 0.167 | 3.677 | 3.845 | 0.520 | 11.429 | 11.949 | 41.8 |
| Australia* | 1.120 | 0.012 | 4.259 | 0.015 | 6.138 | 6.154 | 0.048 | 19.078 | 19.126 | 26.1 |
| Denmark* | 1.160 | 0.010 | 3.180 | 0.013 | 4.747 | 4.760 | 0.040 | 14.754 | 14.794 | 33.8 |
| Finland* | 1.120 | 0.010 | 4.542 | 0.013 | 6.548 | 6.561 | 0.040 | 20.350 | 20.390 | 24.5 |
| India* | 1.430 | 0.000 | 3.445 | 0.000 | 6.340 | 6.340 | 0.000 | 19.704 | 19.704 | 25.4 |
| Indonesia* | 1.320 | 1.900 | 2.271 | 2.445 | 3.858 | 6.304 | 7.600 | 11.992 | 19.592 | 25.5 |
| Ireland | 1.190 | 0.020 | 1.476 | 0.026 | 2.261 | 2.287 | 0.080 | 7.027 | 7.107 | 70.4 |
| Mexico* | 1.120 | 0.056 | 5.300 | 0.072 | 7.639 | 7.711 | 0.224 | 23.742 | 23.966 | 20.9 |
| Netherlands | 1.140 | 0.060 | 3.445 | 0.077 | 5.054 | 5.131 | 0.240 | 15.708 | 15.948 | 31.4 |
| Sweden | 1.160 | 0.090 | 6.019 | 0.116 | 8.986 | 9.101 | 0.360 | 27.927 | 28.287 | 17.7 |

For orientation, the printed total-training estimates range from **2.287 million L (Ireland)** to **15.285 million L (Washington)**; total per-request consumption ranges from **7.107 mL** to **47.506 mL**, with **70.4** to **10.5** requests per 500 mL, respectively. The U.S.-average inference case is **16.904 mL/request**, or **29.6 requests/500 mL**. These tabular scenarios should be retained alongside the introduction's rough **10–50 responses/500 mL** summary, without silently replacing either.

## Coverage checklist for the later judging session

- Abstract: **none labeled**; opening/deck claim S1 and introductory summaries K1–K6 are recorded.
- Contributions: **six prose roadmap items K1–K6**; no formal numbered contribution list.
- Section/subsection content and conclusions: **C01–C40**, through the final Conclusion on p. 61, including nested scope/cooling subsections and the three operational-method bullets.
- Numbered figures: **F1 and F2**, with **F2a–F2c** individually described. Additional unnumbered opening art: **V1**.
- Tables: **T1**, including every row, column, unit, and projection-marker qualification.
- Appendices: **none**. Acknowledgment and bibliographic matter are outside the substantive claim inventory.
