# Claims reference list

**Article:** `article.pdf` — Alissa, H. et al. "Using life cycle assessment to drive
innovation for sustainable cool clouds." *Nature* 641, 331–338 (8 May 2025).
https://doi.org/10.1038/s41586-025-08832-3. Article type: Analysis.

Written from the article alone. Locations give the PDF page (p.1–13) and, for
pages 1–8, the printed journal page (331–338). Pages 9–13 are the Methods and
Extended Data and carry no printed page number.

## Where the article ends for this list

The list covers the **main text (PDF p.1–8), the Methods (PDF p.9–11), and
Extended Data Table 1 (PDF p.13)**. The Methods and Extended Data are included
because the main text points into them for its claims (fluid risks, data
quality, the PFAS discussion) and they carry claims of their own.

Left out: the reference list, Acknowledgements, Author contributions,
Competing interests, Peer review information, and the Online content /
Data availability boilerplate. The one exception is Data availability, listed
as a claim (M-9) because it states what the authors release. The
Supplementary Information (including the "LCA Tool Excel" pedigree matrix) is
not in the PDF and is not covered.

## How to use this list

- IDs are stable so the close-reading judgment can count against them:
  `AB-` abstract, `C-` contributions, `S-` section and subsection conclusions,
  `M-` Methods conclusions, `F-` figures, `T-` tables.
- Quoted text is the article's exact wording. Other text is a paraphrase that
  keeps the article's numbers, hedges and scope conditions.
- "Note" lines record where the article's own statements differ from one
  another or depend on a condition stated elsewhere. They describe the text and
  aren't a judgment of the argument. Where this list and the article disagree,
  the article decides.

---

## 1. Abstract claims (standfirst, PDF p.1 / p.331)

The abstract is the bold opening paragraph, split here into its separate
claims.

| ID | Claim |
| --- | --- |
| AB-1 | Addressing climate change requires accelerating the development of sustainable alternatives to energy- and water-intensive technologies, particularly for rapidly growing infrastructure such as data centres and cloud (ref. 1). |
| AB-2 | The article presents an LCA study of the impacts of advanced cooling technologies on cloud infrastructure, "from virtual machines to server architecture, data centre buildings and the grid". |
| AB-3 | LCA is important for early-stage design decisions, enhancing sustainability outcomes alongside feasibility and cost analysis (ref. 2). |
| AB-4 | The article discusses constructing an LCA for a complex cloud ecosystem (software, chips, servers and data centre buildings), analyses how the cooling technologies interact with that ecosystem, and evaluates each technology from a sustainability perspective "to provide adoption guidelines". |
| AB-5 | LCA "quantifies the benefits" of advanced cooling methods (cold plates and immersion cooling) in reducing GHG emissions (15–21%), energy demand (15–20%) and blue water consumption (31–52%) in data centres. |
| AB-6 | "This comprehensive approach demonstrates the transformative potential of life cycle assessment in driving sustainable innovation across resource-intensive technologies." |

Note on AB-5: the ranges match the 100%-grid-electricity case of Table 4 for
GHG (15–21%) and energy (15–20%). Water (31–52%) doesn't match Table 4's grid
water column (31%, 45%, 48%). The 52 appears in Fig. 4 as the two-phase grid
water bar (that is, 48% savings). The abstract doesn't say which electricity
case it reports.

---

## 2. Contributions

The article has **no enumerated contribution list**. These are the statements
in which it marks what it contributes or claims as new or as a key result.

| ID | Location | Claim |
| --- | --- | --- |
| C-1 | p.2 / 332, intro, last paragraph | "to our knowledge, this is the first public LCA comparing the GHG emissions, energy demand and blue water consumption of air cooling, cold plate and immersion cooling completed by a hyperscale cloud provider." |
| C-2 | p.2 / 332, same paragraph | The LCA approach described, and the lessons learnt, "can be leveraged for other energy- and water-hungry applications." |
| C-3 | p.3 / 333, "Why LCA?" | This LCA "is the first public end-to-end (software–server–data centre impacts) LCA" comparing GHG emissions, primary energy demand and blue water consumption of ACDs, cold-plate data centres and ICDs. |
| C-4 | p.3 / 333, end of "The cooling technology contenders"; repeated in abstract | The LCA provides a quantitative comparison of the technologies to enable design decisions that enhance sustainability. LCA quantifies reductions in GHG (15–21%), energy (15–20%) and blue water (31–52%). |
| C-5 | p.3 / 333, "Data sources and functional unit"; p.7 / 337, Conclusions | The functional unit, annualized virtual core units (Vcores), "was found to be an ideal comparison unit for LCAs relating to general-purpose cloud infrastructure". The Conclusions call "the effectiveness of the virtual core concept" "A key result from our study", describing it as "a new approach towards a functional unit that can simplify and improve LCA analysis and comparison for complex cloud ecosystems". |
| C-6 | p.4 / 334, "Cooling technology sustainability comparison" | The study includes a parametric comparison of electricity sources (100% average grid vs 100% renewable) and presents "this LCA approach, challenges, successes and the lessons learnt to help other industries and sectors achieve their own sustainability goals". |
| C-7 | p.7 / 337, Conclusions | The analysis "has provided quantitative evidence of the sustainability aspects of relevant cooling technologies so they can be properly evaluated in decision-making". |
| C-8 | p.8 / 338, Perspective on future work | The authors have summarized the process and lessons learnt for building LCA for cloud systems (ref. 45) so others can build on the approach. This "foundational work will serve as a living tool" that is improved iteratively. |
| C-9 | p.11, Data availability | Datasets and tools are available at Zenodo (https://doi.org/10.5281/zenodo.14268168), and source data are provided with the paper. |

---

## 3. Section and subsection conclusions — main text

Order follows the article. Each entry gives the conclusion(s) the section
reaches, then any secondary claims it marks.

### S-1. Introduction (unheaded), PDF p.1–2 / 331–332

- S-1a. Global internet traffic has increased more than 15-fold since 2010.
  Demand for cloud, ML, AR, autonomous vehicles and AI is moving computing to
  data centres, a phenomenon "called the fourth industrial revolution", which
  "has just begun" (refs 3–6).
- S-1b. Data centres consume 10–50 times more energy per square foot than
  typical commercial offices (ref. 1). They accounted for about 1.5% (about
  300 TWh) of global electricity demand in 2020, expected to increase (ref. 7).
  Energy per compute instance has decreased by 20% annually since 2010
  (ref. 7).
- S-1c. "The information, communication and technology (ICT) sector needs to do
  more." SBTi indicates a 42% GHG reduction by 2030 (vs a 2015 baseline) across
  ICT is needed to reach net-zero and limit warming to 1.5 °C (ref. 8). The ICT
  sector "should prioritize data centre designs that reduce consumption of
  water, energy and GHG emissions."
- S-1d. Without understanding the overall environmental implications of new
  technologies, organizations find it difficult to chart a path to their
  reduction goals. Microsoft has committed to being carbon-negative and
  water-positive by 2030 (ref. 9) and has used LCA to enable sustainability by
  design.
- S-1e. LCAs show traditional cooling can be up to 40% of a data centre's
  total energy demand (ref. 10). Microsoft has reached PUE as low as 1.12
  (ref. 11). "Doing more requires a better understanding of the impacts of
  different cooling technologies, which can be provided by LCA."
- S-1f. Any product or system benefits from LCA, "but early application
  provides the greatest benefits" (refs 2, 12). The study analyses three
  technologies (cold plate / direct-to-chip, one-phase immersion, two-phase
  immersion), including their effect on the efficiency and performance of the
  compute infrastructure. The LCA covers raw material acquisition, production,
  transport, use and EOL.
- S-1g. Cooling systems have been extensively reviewed (refs 13, 14). For the
  novelty claim, see C-1 and C-2.

### S-2. "The challenges of data centre cooling", PDF p.2 / 332

- S-2 conclusion: with the slowing of Moore's law and Dennard scaling,
  "improving chip performance now requires more power and generates more
  heat". Rising GPU/CPU power and heat flux "will probably push the thermal
  loads of data centres beyond the capacity of current air-cooling
  technologies" (refs 16, 17) and cause power leakage and reduced efficiency.
  Exceeding thermal limits can increase emissions, reduce clock frequency and
  degrade performance (ref. 18). Excessive heat reduces server packing density.

### S-3. "The cooling technology contenders", PDF p.2–3 / 332–333

- S-3a. Cold plate and immersion "can decrease energy consumption while
  increasing computational efficiency and capacity" (ref. 19), "which reduces
  GHG emissions and water consumption". They also enable overclocking and
  denser packing of VMs and servers (ref. 20).
- S-3b. Cold plates: microchannel heat-exchange modules on high-power chips.
  Their liquid-to-air heat transfer ratio "ranges from 50% to 80% or more".
- S-3c. Immersion: servers submerged in dielectric fluid that absorbs 100% of
  generated heat. Dielectric fluid increases heat transfer, improves chip power
  and performance (ref. 21), and reduces power overhead and equipment
  degradation (no fans, ref. 22). One-phase works by convection with
  hydrocarbon (sometimes fluorinated) fluids. Two-phase uses latent heat: the
  fluid boils at 30–50 °C and recondenses, and "In most cases" the fluids are
  fluorinated.
- S-3d. Pros and cons (Table 1, Fig. 1; refs 23–25). Cold plates deploy with
  less disruption to ACDs but can be complex to install, and air cooling may
  still be needed. One-phase uses cheaper coolants and simpler tanks than
  two-phase but performs less effectively at the chip. Two-phase supports very
  high tank power densities (+500 kW) but uses PFAS under legislative scrutiny
  and requires complex tanks. In Feb 2023 ECHA proposed restricting PFAS
  (ref. 26), covering more than 10,000 substances and affecting immersion
  cooling and other industries.
- S-3e. Immersion (both types) isolates servers from airborne corrosive agents,
  lowers failure rates and increases reliability, which "combine to decrease the
  total cost of ownership and reduce embodied carbon". "Scale and space do not
  limit immersion cooling." Intel has shown ACDs can be retrofitted (ref. 22).
  Microsoft, Alibaba, Bitfury (LiquidStack), Riot and others have pioneered
  ICDs (refs 16, 17).
- S-3f. Section conclusion: the prevailing sentiment has been that the
  benefits "could ultimately outweigh their drawbacks". The authors conducted
  the LCA to give a quantitative comparison. "Our findings highlight that using
  LCA enables informed decision-making, optimizing the sustainability of
  advanced cooling technologies in data centres by quantifying their
  environmental benefits." LCA measures reductions of GHG 15–21%, energy
  15–20% and blue water 31–52% (same as AB-5 / C-4).

### S-4. "LCA for data centre cooling", PDF p.3–4 / 333–334

#### S-4.1. "Why LCA?", p.3 / 333

- S-4.1a. "LCAs drive effective design and maximize the environmental
  performance of a product or system" (refs 2, 12). Cold-plate and immersion
  servers reduce energy use, but understanding their full potential "requires
  assessment of the complete picture" of GHG and environmental impacts.
- S-4.1b. Novelty claim: see C-3.
- S-4.1c. Metrics: GHG by IPCC AR5 100-year, excluding biogenic carbon
  (kgCO2e). Primary energy by lower heating value, non-renewable (MJ). Blue
  water consumption = withdrawals minus water returned in usable form.
- S-4.1d. Cradle-to-grave scope (Fig. 3): building core and shell, use-phase
  workload, servers, racks (air), tanks (liquid), support equipment, grid
  electricity, cooling water, cooling-fluid production, cold plates, CDUs and
  material EOL.

#### S-4.2. "Data sources and functional unit", p.3 / 333

- S-4.2a. Data: equipment lists and BOM for server rack elements (ref. 27),
  with material impacts from LCA FE, ecoinvent 3.6 (refs 28, 29) and EPDs.
  Support equipment was mainly modelled with EPDs (refs 30–34).
- S-4.2b. Functional unit: annualized Vcores, "the smallest operational set for
  memory and processing capacity, and the basic unit for the cloud ecosystem".
  The choice "enabled data centre comparison across the entire ecosystem and
  was found to be an ideal comparison unit" for general-purpose cloud LCAs
  (see C-5).
- S-4.2c. Limitations: missing or outdated life cycle inventory data for
  specific equipment or semiconductors, so proxies and best-available data were
  used. The Supplementary Information has the details.
- S-4.2d. The use phase was modelled on the 2021 US grid average (coal 22%,
  natural gas 38%, ref. 35). Coal and gas contribute most to GHG and primary
  energy. In 2015 thermoelectric power was the largest water consumer at 41%
  (ref. 36). EOL was estimated from recycled and remarketed components. Primary
  data came from Microsoft, secondary data from EPDs, background data from LCA
  FE / ecoinvent 3.6. A 100% renewable scenario was included because of
  Microsoft's commitment (ref. 9).
- S-4.2e. Fluids: cold-plate coolant assumed PG25, modelled as 75:25
  water–propylene glycol, with EOL as spent-glycol treatment. Two-phase fluid
  production and EOL were modelled and supplied by the manufacturer
  (confidential). One-phase hydrocarbon fluid was proxied by natural gas
  production, liquefaction and fractionation, assumed re-refined, reused or
  repurposed without additional impacts, with final disposal as incineration.

#### S-4.3. "LCA model", p.4 / 334

- S-4.3. Impacts were aggregated over a 15-year data centre lifetime.
  Components were modelled on their own lifetimes. Servers were assumed to last
  6 years. Support equipment was annualized from EPD/LCA lifetimes or assumed to
  last 15 years. Results were annualized and normalized by total Vcores.
  Table 3 gives component differences relative to the ACD.

### S-5. "Cooling technology sustainability comparison", PDF p.4–5 / 334–335

- S-5a. Baseline (grid) result: cold plate, one-phase and two-phase immersion
  "for GHG emissions, energy demand and blue water consumption can save ≥15%,
  15% and 31%, respectively (Table 4)". Breakdown in Fig. 4.
- S-5b. Section conclusion (main driver): across building, cooling overhead,
  server architecture, overclocking and increased server lifetime, "the primary
  environmental impact reduction driver is energy savings during the use phase
  and the expanded server lifetime."
- S-5c. The use phase is the largest contributor to impacts for all
  technologies, "consistent with other data centre LCA literature" (ref. 37).
  Grid electricity drives GHG, energy and water: it is fossil-dependent, and
  thermal generation consumes water.
- S-5d. The second largest contributor is embodied carbon in server
  manufacturing. Per-server impacts are similar, but liquid cooling allows more
  servers (higher IT capacity) and more Vcores (better heat transfer). Cold
  plate hosts more Vcores than one-phase immersion "because of its higher
  cooling ability at the chip", so cold plate has lower server embodied carbon
  per Vcore than one-phase.
- S-5e. "Building size reductions did not markedly contribute to the
  environmental impact reductions of cold plate or immersion cooling."
- S-5f. Fluids: coolant impacts (cold plate) are lower than two-phase fluid
  impacts because less coolant is used. Immersion needs more fluid than cold
  plates. "Overall, the embodied carbon impacts of the cooling fluid for the
  three technologies are low compared with other components."
- S-5g. Data limits stated here: LCA data for fluids were not readily
  available. One-phase was approximated from Microsoft expert opinion, and LCA
  FE "cannot accurately model one-phase fluid production" ("better data are
  needed"). PG25 additives (corrosion inhibitors, biofilm resistors) were
  excluded for lack of data.
- S-5h. Section conclusion (choice): "Further optimizations for cold-plate and
  one-phase immersion cooling that would put them on par with two-phase
  immersion are possible. Technology choice, thus, depends on regulatory
  requirements, implementation cost, environmental savings goals and deployment
  complexity." Immersion's lower dependence on water "is particularly important
  in water-stressed regions."

### S-6. "Impact of using 100% renewable energy", PDF p.5–6 / 335–336

- S-6a. Context: renewables rose from 20% (2010) to 29% (2020) of global
  generation (ref. 38), but further grid decarbonization is needed for 1.5 °C
  (ref. 39). Microsoft's commitments (100% matched renewable by 2025; 100/100
  carbon-free by 2030, ref. 40) made 100% renewable "a key scenario".
- S-6b. Under 100% renewable, savings vs air cooling for GHG, energy and blue
  water "were ≥13%, 15% and 50%, respectively (Fig. 4)".
- S-6c. Ranking reversal: on the US grid, one-phase immersion had slightly
  higher GHG savings than cold plate (lower server power and lower PUE allowed
  more servers), although cold plate overclocks more. Under renewables,
  overclocking "became more dominant", so cold plate had lower GHG. Water
  savings were higher because renewable electricity consumes less water.
- S-6d. Switching from 100% grid to 100% renewable reduced GHG by 85–90%,
  energy demand by 6–7% and blue water by 55–85%, depending on the technology
  (each normalized to air cooling, Fig. 4).
- S-6e. Under renewables, embodied carbon in servers "became more
  significant", which "highlights the need for improved and relevant data on
  server components for additional decarbonization" (ref. 41).
- S-6f. Building-water impacts don't change substantially between
  technologies, because construction metals drive embodied water. Metal
  recyclability gives a positive water impact at EOL. Embodied water impacts
  across air, immersion and cold plate "are within 1–15% of each other."
- S-6g. Data quality: a pedigree matrix was used because standard deviations
  were not available ("a quantitative uncertainty assessment would provide
  incomplete information"). It indicates where uncertainty could be reduced.
  Details are in the Supplementary Information (LCA Tool Excel).

Note on S-6c vs Table 4: on the grid, Table 4 gives one-phase 16% and cold
plate 15% GHG savings. Under renewables it gives cold plate 16% and one-phase
13%. The "≥13%" in S-6b is the lowest renewable GHG figure, which is below the
"at least 15%" in the Conclusions (S-8a).

### S-7. "LCAs to inform engineering design", PDF p.6–7 / 336–337

- S-7a. Section conclusion: "Our LCA has shown that reducing data centre energy
  use through advanced liquid-cooling technologies will lead to marked
  reductions in data centre environmental impacts. This is valuable and
  actionable information."
- S-7b. Comparative LCAs let the cloud industry focus on its most notable
  impacts. The ICT industry "must prioritize environmental assessment at the
  same level as cost and performance". LCAs are "a powerful tool" for engaging
  stakeholders and "ensure a harmonized approach to advancing potentially
  sustainable technologies and facilitating decision-making."
- S-7c. Trade-offs: cold plate has better chip-level heat transfer than
  one-phase "but may not have as low PUE values". Two-phase "could have" high
  chip heat transfer and lower PUE "but might involve" more complex,
  higher-embodied-carbon components (tank, fluid). "LCA ensures that all these
  engineering design decisions and trade-offs can be considered within holistic
  sustainability perspectives."
- S-7d. Pros: air needs no retrofits and no new embodied carbon. Cold plate
  needs less fluid per rack. One-phase can use varied dielectric fluids (most
  commonly hydrocarbon mineral oils), with low GWP fluids (ref. 42), and is
  relatively inexpensive. Two-phase fluids are mostly fluorine-based, with heat
  rejection "multiple times higher than traditional air cooling" (ref. 43).
- S-7e. Cons: "Air cooling uses by far the most electricity." Cold-plate copper
  components must be replaced for each server every IT cycle. One-phase
  hydrocarbon oils are flammable and viscous, leave oil blooms that inhibit
  maintenance (ref. 43), and carry spill risks (aspiration, bioaccumulation,
  groundwater). Engineering controls such as triple containment can help, and
  established clean-up procedures exist. Two-phase fluids are PFAS facing
  legislative restrictions.
- S-7f. "Each cooling technology assessed in this study has drawbacks." When
  selecting a cooling fluid, designers should consider (bulleted list): EHS
  analysis as "the first step"; end-to-end LCA impacts; high chip-level cooling
  capability; socioeconomic and business impacts including regulation; ODP and
  GWP ("only fluids with low to zero values should be considered");
  bioaccumulation, toxicity, persistence and breakdown (minimal); and viscosity,
  flammability and volatility.
- S-7g. "LCAs can help inform regulation and policy by enabling the evaluation
  of trade-offs." "As shown in this LCA, all immersion cooling and cold-plate
  cooling technologies offer efficient cooling and heat rejection. But all
  available immersion fluid options have their challenges, including regulatory
  ones." "An important application of LCA should be in the design of regulatory
  approaches", because emerging EU and US PFAS rules "will restrict its use for
  two-phase immersion cooling". The Methods have more.

### S-8. "Conclusions", PDF p.7 / 337

- S-8a. The study uses LCA to compare ACDs with cold-plate data centres and
  ICDs. The results "demonstrate the importance of using LCA in early-stage
  design decisions to improve sustainability outcomes" (ref. 44) "and show how
  cold-plate and immersion cooling have excellent potential for reducing
  environmental impacts such as GHG emissions (at least 15% reduction), energy
  consumption (at least 15% reduction) and water consumption (at least 31%
  reduction) per Vcore per year."
- S-8b. "highly optimized cold-plate or one-phase immersion cooling
  technologies can perform on par with two-phase immersion (which has
  challenges because of emerging regulatory constraints on PFAS), making all
  three liquid-cooling technologies desirable options." Additional
  considerations: time-to-market, regulatory and supply chain landscapes,
  technology complexity and implementation cost.
- S-8c. The effectiveness of the Vcore concept was "A key result" (C-5).
  Worked illustration: a 10 GW data centre handling 1 thousand million Vcores
  at 1 kgCO2e, 1 MJ and 1 l each in the ACD would, with any of the
  liquid-cooling technologies, fall to 0.85 thousand million kgCO2e,
  0.85 thousand million MJ and 0.69 thousand million l of water "at the very
  least".

Note on S-8a: "at least 15%" GHG matches the grid case in Table 4 (15–21%).
Under 100% renewable, Table 4 gives one-phase 13% (S-6b's "≥13%"). The
Conclusions don't state which electricity case they report.

### S-9. "Perspective on future work", PDF p.7–8 / 337–338

- S-9a. Microsoft is using the results to drive cooling and cloud
  infrastructure innovation. "the early use of LCA identified the embodied
  impacts of electronic equipment and how addressing use phase energy and
  shifting to renewables can reduce them", which enables Microsoft and others
  to engage suppliers.
- S-9b. "Limited data availability, particularly for cooling fluids
  production, data-centre-specific equipment and electronics life cycles, is a
  constraint in the effectiveness of any LCA." The authors encourage more
  comprehensive databases.
- S-9c. Microsoft is integrating LCAs into decision-making and design. The
  authors hope the study gives guidance to other companies and industries. The
  process and lessons are summarized in ref. 45, and the work "will serve as a
  living tool" updated for new cooling, usage patterns (for example, AI
  training) and waste-heat reuse (ref. 46). See C-8.

---

## 4. Section and subsection conclusions — Methods (PDF p.9–11)

### M-1. "Methodology and background", p.9

- M-1a. Restates scope: CPD, 1P-ICD and 2P-ICD compared with ACD,
  cradle-to-grave, with the Table 2 components and the same three metrics as
  S-4.1c. Excluding biogenic carbon quantifies fossil-source GHG.
- M-1b. Use phase on the 2021 US grid (coal 22%, gas 38%; thermoelectric water
  41% in 2015). EOL based on the extent of recycling. Same data hierarchy as
  S-4.2d.
- M-1c. Functional unit: 1 Vcore is "the fundamental unit that represents the
  operations carried out to provide the different cloud services". A server
  Vcore results from physical cores, logical cores and packing density, given as
  the equation 1 Physical core = 2 Logical cores = 2V × a cores, where a is
  packing density, 0 < a < 1.5.
- M-1d. 15-year data centre lifetime. Servers 6 years "based on expert opinion
  from Microsoft". Support equipment annualized from EPD/LCA lifetimes. LCA FE /
  ecoinvent-modelled equipment assumed 15 years. Results annualized and
  normalized by total Vcores.
- M-1e. Building production and EOL (run-in subhead): building shell from
  Microsoft BOM and Tally. GHG and energy modelled in Tally, blue water in LCA
  FE. Concrete assumed 5,000 psi and 8 in average depth. Interior non-structural
  partitions, ceilings and equipment excluded. EOL: EPA data for metal recycling
  and landfill, with other materials landfilled.
- M-1f. Server production and EOL (run-in subhead): compute, networking and
  storage servers make up 70%, 10% and 20% of IT capacity. The compute server is
  modelled from Microsoft BOM. The network server is assumed to be 1.3 times
  compute-server embodied impacts "based on internal expertise" because of data
  gaps. Server types are identical across designs, except that cold-plate
  servers add copper plates, tubing, manifold and CDUs, and immersion servers
  are air-cooled servers without fans, heat sinks or baffles. Electronics come
  from the LCA FE electronics database, based on research (ref. 48) that "is two
  decades old, and it is crucial to have newer data for electronics". SSDs
  "conservatively modelled" (16-layer PCB, wafer one-third, DRAM two-thirds).
  Server EOL is 100% recycling after 6 years.
- M-1g. Rack and tank production and EOL (run-in subhead): racks and tanks
  have a 15-year lifetime. Material data from Microsoft suppliers. PDU and power
  and management distribution units excluded because no ICD data were
  available. Assembly and test energy included. EOL is 100% recycling of input
  metals.
- M-1h. Support equipment production and EOL (run-in subhead): mainly EPDs and
  LCAs from Microsoft equipment lists, otherwise LCA FE, scaled by capacity.
  Lists the equipment for ACD/CPD vs ICD. Where an EPD gave water use rather
  than consumption, water use was used. Proxies: adiabatic cooler (chiller +
  radiator), e-house (steel weight), bus ducts (copper). Transformer oil treated
  as hazardous waste.

### M-2. "Use phase", p.10

- M-2a. Annual energy (MWh/yr) = IT capacity (MW) × load factor × PUE × 8,760
  h/yr. The model uses design capacity with "a conservative assumption for the
  utilization rate".
- M-2b. Blue water covers cooling water. Non-cooling use (restrooms, cafés,
  irrigation) was excluded, assumed equal across designs because staffing would
  be similar. Temperature-based scenarios were run for two locations (dry and
  humid climate).
- M-2c. All designs use evaporative AHUs. Immersion uses fluid coolers, dry in
  most climates and adiabatic (wet) above 35 °C dry-bulb. Adiabatic systems use
  more water but cool more efficiently, especially in warm, dry climates
  (refs 20, 49, 50). "Fewer air-handling units and adiabatic coolers result in
  less water use for cooling in ICDs." Higher cycles of concentration mean more
  make-up water and greater water use.

### M-3. "Design assumptions for cooling technologies", p.10–11

- M-3a. Cold plate "is a functional hybrid of air-cooling and two-phase
  immersion cooling". It has chip-level cooling similar to two-phase but "could
  have a higher PUE" because it still needs air cooling. Its racks have the
  same power as two-phase tanks. Its compute-server power and PUE are each
  modelled as the average of the air-cooled and two-phase values. Rack embodied
  impacts are scaled to include copper, tubing, manifolds and CDUs. Coolant is
  PG25 (75:25), with EOL as spent water–glycol treatment.
- M-3b. One-phase immersion has the same tank power, compute-server power and
  count, architecture, footprint and PUE as two-phase. The fluid is a
  natural-gas-derived hydrocarbon, re-refined and reused, then incinerated. The
  fluid quantity equals two-phase, but heat removal is lower, so overclocking
  "under the best-case scenario for one-phase immersion is capped at 10%". Tank
  embodied impacts equal two-phase's (more CDUs, simpler tank).
- M-3c. The two-phase fluid and its EOL impacts were modelled by the
  manufacturer "and remain confidential".

### M-4. "Data quality assessment", p.11

- M-4a. A quantitative uncertainty assessment "is not possible" because most
  LCA FE datasets lack standard deviations. A pedigree matrix instead gives a
  qualitative indication of variability and uncertainty.
- M-4b. Five indicators (reliability, completeness, temporal, geographical and
  technological correlation; Extended Data Table 1), scored 1 (high
  representativeness) to 5 (low) per input and averaged by indicator (ref. 51).
  Geographical resolution has seven levels. Technological correlation has four
  categories.
- M-4c. Section conclusion: data quality across phases "is between good and
  average", scoring 2–3 in all categories, with an overall score of 3, "which
  indicates that the variability in data is not large and is manageable". The
  reason is that the use phase dominates all three impact categories and its
  data quality has been consistently high, so "the uncertainty of the overall
  results is also low."

### M-5. "PFAS: LCAs to inform sustainability regulations", p.11

- M-5a. "As shown in this LCA, immersion cooling offers the most efficient
  cooling and heat rejection; however, all available fluid options have their
  challenges, including regulatory ones." LCA should be applied to the design of
  regulation, given emerging EU and US PFAS rules.
- M-5b. Two-phase fluids are PFAS. "more than 4,000 synthetic chemicals are
  used in industries and products such as firefighting, medicine and food
  packaging." ECHA published its restriction proposal on 7 Feb 2023 (ref. 26),
  and several US states are working on restrictions. "A broad ban on more than
  10,000 chemicals might be impractical, but science-based regulations based on
  overall LCA, persistence, bioaccumulation and toxicity may be effective."
- M-5c. PFAS limits "may directly influence" immersion-cooling efforts. LCAs
  can calculate PFAS leakage impacts, help mitigate risks and establish best
  practices (sealed tanks, multiple containment).
- M-5d. "For end users, LCAs are powerful tools in reducing GHG emissions,
  water consumption and energy demand." Risk mitigation list for liquid-cooling
  fluids at scale: fluids that won't partition into groundwater; EHS-compliant
  production and a "good neighbour" plant; tracked transport on the shortest
  routes; containers and secondary containers; siting away from large water
  bodies in low-disaster, drier zones; asphalt and concrete barriers to speed
  evaporation; and minimal fluid use, low-loss tanks, primary and secondary
  containment, vapour monitoring, vapour traps and adequate air circulation.

Note on M-5a vs S-7g: the main text says "all immersion cooling and cold-plate
cooling technologies offer efficient cooling and heat rejection". The Methods
version of the same paragraph says "immersion cooling offers the most efficient
cooling and heat rejection". Note on M-5b vs S-3d: "more than 4,000" PFAS
chemicals in use (Methods) vs restrictions on "more than 10,000 substances" /
"more than 10,000 chemicals".

### M-9. "Data availability", p.11

- See C-9.

---

## 5. Figures

| ID | Location | What it shows |
| --- | --- | --- |
| F-1 | Fig. 1, PDF p.2 / 332 | Schematics of the three liquid-cooling technologies as alternatives to air cooling. (a) Cold plate: a metal plate with embedded coolant channels (for example, 25% polyethylene glycol / 75% water) absorbs chip heat by convection, with server rack, coolant distribution unit and facility water loop. (b) One-phase immersion: whole server in a tank of dielectric fluid (for example, mineral oil), heat removed by convection, with CDU and facility water. (c) Two-phase immersion: servers in a low-boiling dielectric fluid (for example, a refrigerant), with vapour rising to a condenser cooled by facility water, heat removed by phase change. Note: the caption says "polyethylene glycol" for the example coolant, while the text models PG25 as propylene glycol. |
| F-2 | Fig. 2, PDF p.4 / 334 | Photographs of Microsoft's proof-of-concept builds. (a) Cold-plate configurations: general-purpose server cooled by air (top left) vs cold plates (bottom left), and GPU server by air (top right) vs cold plates (bottom right). (b) One-phase immersion tanks (left) and a partially submerged server (right). (c) Two-phase immersion tank, with refrigerant boiling visible as surface turbulence (inset). Supports the claim that Microsoft has built and tested pilots of each technology. |
| F-3 | Fig. 3, PDF p.4 / 334 | Cradle-to-grave system boundary diagram with three stages. Material production: raw material inputs, plus manufacturing inputs such as heat, power, water, production of low-GWP fluid, servers, racks, tanks and supporting equipment. Use phase: data centre infrastructure differences, use-phase energy and component replacement. End of life: waste treatment (recycling, landfill, incineration). |
| F-4 | Fig. 4, PDF p.7 / 337 | Stacked horizontal bars of GHG (kgCO2e), energy (MJ) and blue water (l) per Vcore per year for air-cooled, cold-plate, one-phase and two-phase data centres, each under 0% renewable (grid) and 100% renewable. All bars are normalized to the ACD on 100% grid = 100. Bars are broken down by use phase, building, server, rack/tank, cable, supporting equipment and fluid impacts. Totals as printed: **GHG**, grid: air 100, cold plate 85, one-phase 84, two-phase 79; renewable: air 11, cold plate 9, one-phase 9, two-phase 9. **Energy**, grid: air 100, cold plate 85, one-phase 85, two-phase 80; renewable: air 93, cold plate 79, one-phase 79, two-phase 74. **Water**, grid: air 100, cold plate 69, one-phase 55, two-phase 52; renewable: air 45, cold plate 22, one-phase 9, two-phase 8. Visually, the use phase is the largest segment in grid bars and server embodied impacts are the next largest. Under renewables, GHG bars are mostly server embodied impacts. Supports S-5a–d and S-6b–e. The totals are printed on the image; per-segment values aren't printed. |

---

## 6. Tables

| ID | Location | What it shows |
| --- | --- | --- |
| T-1 | Table 1, PDF p.3 / 333 | Pros and cons of cold plate, one-phase and two-phase immersion across four rows. **Deployment:** cold plate pro "Quick time-to-market"; one-phase and two-phase con "Longer development cycle". **Architecture:** cold plate con "Can lead to complex layouts"; one-phase and two-phase pro "Can simplify server form factor". **Effectiveness:** cold plate and two-phase pro "High heat transfer capability"; one-phase con "Intermediate heat transfer capability (can be further optimized)". **Policy:** cold plate and one-phase pro "No regulation challenges for used coolants"; two-phase con "PFAS fluids used in two-phase immersion face strict regulation proposals (even if low GWP and ODP)". Footnotes define GWP and ODP. |
| T-2 | Table 2, PDF p.5 / 335 | Data centre components in the model. Building: site works (pads), core, shell. Supporting equipment, mechanical: AHUs, adiabatic cooler, e-house. Supporting equipment, electrical: generator, UPS and battery, PDU, cables, bus plug and duct, transformer. IT: compute server (excluding PSU), storage server (JBOD + head nodes), networking server, racks (air) / tanks (immersion). All data collected per MW of IT capacity. Footnotes define e-house and JBOD. |
| T-3 | Table 3, PDF p.5 / 335 | Design and operation differences vs the ACD for cold plate / one-phase / two-phase. MW IT capacity: +3% / +6% / +6%. Overclocking factor: +20% / +10% / +20%. PUE: −3% / −6% / −6%. Compute IT %: identical. Compute servers: +6% / +13% / +13%. Storage IT %: identical. JBODs: +10% / +13% / +13%. Head nodes: +10% / +13% / +13%. Networking IT %: identical. Networking servers: +10% / +13% / +13%. Vcores (with overclocking, part of the functional unit): +28% / +25% / +36%. Compute server power: −3% / −6% / −6%. Footnote: lower is better for PUE and server power, higher is better for the rest. |
| T-4 | Table 4, PDF p.6 / 336 | Savings vs an ACD (cold plate / one-phase / two-phase). **100% grid:** GHG 15% / 16% / 21%; energy 15% / 15% / 20%; blue water 31% / 45% / 48%. **100% renewable:** GHG 16% / 13% / 20%; energy 15% / 15% / 20%; blue water 50% / 80% / 82%. Footnote hedges: results "are sensitive to design criteria such as overclocking, heat sink design and thermal resistances"; savings "can change based on the assumptions used"; "We are not suggesting any of them are superior to the other but rather showing that they all have sustainability benefits compared with air cooling and can be optimized further." (a) Traditional PG25 cold plate "tends to have the same cooling capability at the chip as two-phase immersion"; jet-impingement or phase-change cold plates could increase it and support further overclocking. (b) Traditional one-phase "can have lower cooling capability at the chip" but can use optimized heat sinks. (c) Two-phase chip cooling "will mostly depend on the boiling enhancement coating". |
| T-ED1 | Extended Data Table 1, PDF p.13 | Data quality indicators (pedigree matrix scale, adapted from ref. 51, Edelen & Ingwersen 2016), with scores from 1 (highest confidence) to 5 (lowest). **Reliability:** 1 primary MSFT measured; 2 primary MSFT estimated; 3 literature with exact proxy match; 4 literature with proxy match; 5 online sources, not an exact match, limited documentation. **Completeness:** 1 >80% of market over an adequate period; 2 60–79% (adequate period) or >80% (shorter period); 3 40–59% (adequate) or 60–79% (shorter); 4 <40% (adequate) or 60–79% (shorter); 5 unknown or few sites and short periods. **Temporal:** <3, <6, <10, <15 years, or unknown / >15 years. **Geographical:** same resolution and area; within one level and related area; within two levels and related area; outside two levels but related area; different or unknown area. **Technological:** all, three, two, one or none of the technology categories equivalent. It shows the scale only; the scores assigned to this study are reported in text (M-4c) and the Supplementary Information. |

---

## 7. Counts

| Type | Count | IDs |
| --- | --- | --- |
| Abstract claims | 6 | AB-1 – AB-6 |
| Contributions (no enumerated list; marked statements) | 9 | C-1 – C-9 |
| Section / subsection conclusions, main text | 11 units (9 sections, with S-4 split into 3 subsections) | S-1, S-2, S-3, S-4.1, S-4.2, S-4.3, S-5, S-6, S-7, S-8, S-9 |
| Section / subsection conclusions, Methods | 9 units (M-1 with 4 run-in subsections, plus M-2 – M-5) | M-1a–d, M-1e, M-1f, M-1g, M-1h, M-2, M-3, M-4, M-5 |
| Figures | 4 | F-1 – F-4 |
| Tables | 5 (4 main + 1 Extended Data) | T-1 – T-4, T-ED1 |
