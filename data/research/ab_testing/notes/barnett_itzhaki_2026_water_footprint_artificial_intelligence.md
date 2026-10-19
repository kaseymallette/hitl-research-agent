# Barnett — Water Footprint of AI

## Abstract

> Artificial intelligence (AI) is increasingly run on high-density computing infrastructure, yet its environmental
footprint is still assessed mainly through electricity use and associated greenhouse-gas emissions. A critical, less
visible dimension is water: AI infrastructure consumes freshwater through evaporative cooling, indirect water
use in electricity generation, and water-intensive semiconductor manufacturing. Projections suggest AI's global
water footprint could reach 4.2–6.6 billion cubic meters annually by 2027. Many data centers are located in
water-stressed regions. While technologies, including cold-climate siting, natural water body cooling, waterless
designs, and waste heat recovery, can reduce on-site demand, their deployment remains limited. This work
introduces "digital water sobriety" as a governance framework linking evaluation of which AI applications justify
freshwater consumption, water conscious siting, and mandatory facility-level water use transparency. Achieving
water-sustainable AI demands not merely technological optimization but fundamental policy reform integrating
water constraints into computational infrastructure planning.

## Methods

> Evidence on AI infrastructure water consumption was synthesized through a targeted review of three streams: (1) peer-reviewed studies on data center water footprint and cooling technologies identified via Web of Science and Google Scholar (2015–2025), prioritizing quantitative assessments and lifecycle analyses; (2) corporate sustainability reports and technical documentation from major cloud providers (Google, Microsoft, AWS) that report operational practices and metrics; and (3) investigative journalism and policy analyses documenting siting conflicts, regulatory responses, and community impacts. Peer-reviewed sources were prioritized over the other two sources.

> No data was used for the research described in the article.

## Overview

- AI produces waste heat that must be removed by water\-cooling systems
- Global water footprint for AI: **4\.2–6\.6 billion cubic meters annually by 2027**
- Water consumption for data centers is low compared to annual global consumption but high in water-stressed regions
- AI consumes freshwater through:
  - Evaporative cooling
  - Indirect electricity generation
  - Semiconductor manufacturing
- Technologies to reduce water consumption have benefits and tradeoffs, but remain limited:
  - Cold-climate siting
  - Natural water body cooling
  - Subsea data centers
  - Waterless designs
  - Waste heat recovery
- Digital water sobriety: Governance framework for sustainable AI water usage → policy reform and infrastructure planning

## Key Takeaways (User-Implied)
1. The majority of the paper covers the technical aspects of water consumption in AI infrastructure and proposes solutions with tradeoffs. Yet, the paper argues for a moral justification for AI applications. The technical solutions are presented as possible ways to create sustainable AI systems, but only if those systems offer a clear societal benefit. It's unclear why the author is turning a sustainability question into a moral justification question.
2. The abstract lists three ways that freshwater is consumed in AI infrastructure: evaporative cooling, indirect electricity generation, and semiconductor manufacturing, but the paper spends very little time discussing semiconductor manufacturing. Why is that in the abstract if it's not discussed in the paper?
3. The paper spends a lot of time discussing the tradeoffs of different technical solutions, without any clear resolution, only to propose policy changes, regulations, and mandatory disclosures. This seems like a disconnect between the technical solutions and the policy recommendations.
4. There are several examples of companies successfully using water-efficient data centers: Meta had an energy efficient data center in Sweden, demonstrating efficiency of using cold climates, Google had its most efficient data center in Finland, using natural water body cooling, Microsoft launched a successful datacenter at a subsea level, and Stockholm’s Open District Heating used wasteheat to heat homes. These examples show that AI data centers do not necessarily require freshwater for cooling, if electronics are protected from saltwater, and that the wasteheat can be transferred to other uses. 
5. The paper focuses more on the challenges of water-cooling methods and on the increasing water consumption by AI rather than on solving the technical challenges, ultimately arguing for a policy and moral framework to guide sustainable AI development. 


## Water Footprint Concepts

|Category   |Definition in the notes                |
|-----------|---------------------------------------|
|Blue water |Surface water and groundwater.         |
|Green water|Rainwater stored in soil.              |
|Grey water |Clean water needed to dilute pollution.|

### Water withdrawal vs\. water consumption

- Data centers consume water by converting it to vapor, resulting in consumptive loss
- Once\-through cooling withdraws water, uses it for cooling, and returns it to the source\. Raises water temperature and contributes to thermal pollution

## Water Usage Effectiveness

- This study focuses on **blue water consumption**
- Quantified by **Water Usage Effectiveness &#40;WUE&#41;**

**WUE = Annual site water used for cooling and humidification / Annual IT energy consumption**

|Cooling approach        |WUE|
|------------------------|----------------------|
|Air-conditioned building|Approximately 0.      |
|Evaporative cooling     |>3 m³/MWh.            |

- One **1 MW data center** consumes **25,500 m³ annually**

## Data Center Water Use

### Withdrawal

- Data centers withdraw billions of liters of water per year
- Example: Google withdraws **20 billion liters** (2024)

**Withdrawal ≠ consumption\.**

### Consumption

|Year |Data center water consumption|
|-----|------------------------------------------------|
|2014 |21.2 billion liters.                            |
|2023 |66 billion liters.                              |
|2028*|60–124 billion liters.                          |


## Global Context and Local Impacts

- Globally, **4,000 km³ of freshwater** is withdrawn annually

|Sector       |Share of global freshwater withdrawal|
|-------------|-------------------------------------|
|Agriculture  |72%.                                 |
|Industry     |15%.                                 |
|Municipal use|13%.                                 |

- U\.S\. data centers make up a fraction of global withdrawals
- Data centers are concentrated in **water\-stressed regions**
- Impacts are significant when measured **locally vs\. globally**
- Understanding water scarcity in these regions is necessary to understand the effects of data center water usage

## Cooling Technologies

The water footprint depends on **cooling architecture** and **local climate**.

### 1. Evaporative cooling systems

- Use evaporation for heat rejection
- High energy efficiency, but **high WUE**

### 2. Air-cooled systems

- Minimize on-site water use
- Increase electricity demand → indirect water usage

### 3. Liquid and immersion cooling

- Enable efficient heat removal, but need water rejection pathways
- Low on-site WUE; high for evaporation

## Local Conflicts

- **Two-thirds of data centers built or planned since 2022** are in water-stressed regions
- Example: Texas has **400 data centers**, with consumption projected to reach **3% of statewide water by 2030**, while drought conditions remain
- Water consumption in water-stressed regions:
  - **42% of Microsoft’s water consumption**
  - **15% of Google’s water consumption**

### Colón

- Municipality north of Mexico City
- **67,000 residents**
- Severe drought conditions
- Microsoft data center
- Two primary reservoirs have been depleted

### Water concessions and allocation

- Water concessions were granted by national agencies
- Once granted, allocations carry legal standing even if there is drought or scarcity
- Designed around historical use patterns
- **Allocation failures → environmental justice concerns**

## Technical Solutions

### 1. Cold-climate siting

- Data centers in colder climates can use free air cooling
- Example: Meta’s data center in Sweden:
  - Withdraws only **25.4 million liters annually**
  - Uses hydropower → still requires water
- **Tradeoff:** Limited geography and seasonality

### 2. Natural water bodies

- Site data centers near lakes, rivers, or seawater
- Example: Google’s data center in Finland uses seawater from the bay
  - Described as the company’s most efficient data center
- Low WUE and low water consumption, but ecological questions remain:
  - Warming plumes
  - Stratification
  - Cumulative impacts
- **Ecological concerns:** 
  - Discharge temperatures elevated by **5–8°C**
  - Can disrupt thermal stratification in lakes and affect dissolved oxygen levels
  - The EU has restrictions on temperatures of returned cooling water
- **Sustainability tradeoffs:**
  - Operational and financial risk
  - Restricted scalability

### 3. Subsea data centers

- Place sealed server capsules directly on the seabed
- Use surrounding seawater as a passive heat sink
- Example: China sealed **400–800 AI servers**, achieving WUE close to **0** by eliminating freshwater consumption
- Microsoft noted economic and operational constraints → discontinued despite success
- Potential impacts:
  - Effects on local temperature
  - Marine life
  - Electromagnetic emissions
- Initial assessments indicate low thermal effects: **<1°C temperature rise**
- Costly and complex maintenance

### 4. Waterless systems

- Modular data centers using:
  - Immersion cooling
  - Direct-to-chip liquid cooling
- Can achieve **near-zero WUE**
- Example: Deep Green deploys immersion-cooled units, capturing **96% of waste heat for reuse**
- Example: AWS operates reclaimed wastewater systems at **20 facilities**
- **Tradeoffs:**
  - Increase electricity use by **10–25% compared with evaporative cooling**
  - Electricity makes up **40–60% of operating costs**
  - Operators face incentives to lower costs by using evaporative cooling
  - Dry cooling performance degrades in hot climates

### 5. Waste heat recovery
- Some companies use waste heat as a resource
- Example: Deep Green uses waste heat to heat a UK swimming pool, offsetting 62% of conventional natural gas heating
- Example: For the 2024 Paris Olympics, Equinix reused server heat for the Olympic Aquatic Center
- Example: Stockholm’s Open District Heating provides heat for 30,000 apartments
- System benefits: Enhances overall energy efficiency by enabling dual services
- Tradeoff: Requires proximity to heat demand and seasonal alignment with data center operation
- Scalability: Currently pilot-scale; systematic integration requires coordinated planning and policy frameworks

## Water sustainability
- Water is priced lower than electricity, creating market incentives that favor evaporative cooling
- This pricing structure may not reflect the true environmental cost of water use in water-stressed regions
- Waterless systems could be a good alternative but require higher electricity consumption, which may not be economically viable in all regions
- Freshwater is not necessarily needed for cooling - recycled or seawater can be used, but this may not be feasible in all locations
- Waste heat recovery can help offset water use by providing useful heat output but infrastructure constraints may limit adoption

## Digital Water Sobriety
- AI applications should be evaluated on their use cases and environmental impact
  - Social justification: medical diagnosis, climate modeling, pharmaceutical discovery
  - Diffuse impact: image generation, automated marketing content, conversational queries 
- Does not propose binary approval
- Advocated a graduated governance approach linking resource cost to demonstrated societal benefit 

### Solutions
- Scarcity-adjusted water pricing to reflect local opportunity costs
- Mandatory impact assessments for training runs 
- Facility-level water budgets 
- Permits for adopting water-efficient cooling technologies

**Awareness is insufficient**       
Awareness of pollution ≠ willingness to adopt sustainable practices     
→ Need for policy intervention and incentives

**Freshwater is a finite resource**       
AI water footprint results from design choices and operational decisions      
Requires systemic changes in how we build and operate AI systems

### Accountability Gaps 
- Google and Microsoft have pledged to be "water positive" by 2030
- However, these pledges rely on water replenishment credits, watershed restoration, or infrastructure investments
- Fail to address difference between continuous, localized consumption vs. seasonal, distributed replenishment
- WUE reporting remains voluntary 

### Regulation 
- Virginia proposed a water disclosure bill to mandate annual reporting
- Operators withhold facility-level data
- Need disclosure of facility locations, cooling configurations, and electricity sources 

**Need standardized reporting and mandatory disclosure requirements**

## Discussion
- Previous sections demonstrate water efficient AI is achievable through innovation and policy intervention
- **Limitations**
  - Knowledge gaps
  - Implementation barriers
  - Research priorities are bottlenecked

### Research Priorities
- Benchmark datasets linking workload to water consumption
- Indirect water usage tracking (electricity generation, semiconductor manufacturing)
- Ecological impact monitoring for lakeside and subsea approaches
- Integrating district heating into legacy systems and city infrastructure
- Standardized disclosure protocols

### Policy Imperatives
- Mandatory facility-level transparency
- Water-conscious sitting regulations
- Digital water sobriety frameworks
- Heat recovery integration incentives

## Conclusion
*How much "intelligence" per liter of water is justified as both energy and freshwater become constrained?*

> The choices made regarding where AI is deployed, how it is cooled, and whose water it consumes will determine whether this technology exacerbates water insecurity for vulnerable populations or catalyzes innovation in integrated water-energy-heat systems.