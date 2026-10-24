# Primer — Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system

*Background from gpt-6.1-sol at high effort, 2026-10-24. This is the model's general knowledge of the field, written to read before the article; it is not a reading of the article and is unchecked.*

## Where this subject sits

This topic connects three fields: **electronics cooling**, **desalination**, and **thermal-system design**. The broader idea is heat integration: heat that one process must discard can supply another process that needs warming. This belongs to the **energy–water nexus**, the study of how energy production and water supply depend on each other.

The engineering challenge is not simply finding enough heat. Its temperature, availability, distance from the water-treatment equipment, and cost of collection all matter. Research in this area commonly combines heat-and-mass-transfer models, thermodynamic accounting, cost estimates, and optimization. A modeled integrated system and an experimentally demonstrated installation are different stages of development.

## 1. What data-center cooling actually does

Almost all electricity consumed by computing equipment eventually becomes heat. A server drawing roughly 1 kilowatt therefore creates roughly 1 kilowatt of cooling demand. Cooling does not eliminate that heat; it transfers it to water, air, or another destination.

The main approaches are:

- **Air cooling:** fans move air across electronic components, and room-level equipment removes the heat.
- **Cold-plate cooling:** liquid flows through metal plates attached to hot components, without normally touching the electronics.
- **Immersion cooling:** electronics sit directly in an electrically insulating, or **dielectric**, liquid.

In **single-phase immersion**, the liquid warms without boiling. In **two-phase immersion**, it boils at hot surfaces, and its vapor condenses on a cooler heat exchanger. Evaporation absorbs substantial energy without requiring a large temperature rise. The condensed liquid returns to the bath. The vapor is coolant vapor—not necessarily water vapor or steam.

A second fluid can carry heat away through the condenser wall while remaining separate from the dielectric liquid. This separation matters whenever the heat-carrying stream is salty or otherwise unsuitable for contact with electronics.

For scale, a kilowatt-sized apparatus is small relative to a complete data center. Conventional racks often dissipate several to tens of kilowatts, while high-density computing racks can exceed 100 kilowatts. Whole facilities commonly operate at megawatt scales. These are broad reference points, not fixed categories.

## 2. Why warm waste heat can drive desalination

Data-center heat is usually **low-grade heat**: available at modest temperatures rather than the hundreds of degrees associated with furnaces or power-plant steam. Warmth around 40–70°C can be useful for heating or evaporation, but is difficult to convert efficiently into electricity.

**Membrane distillation** exploits evaporation without requiring the entire water stream to boil. A warm saline stream passes one side of a porous, water-repelling membrane. Water evaporates at the pore entrances, crosses as vapor, and condenses on the cooler side. Dissolved salts are essentially nonvolatile and remain behind.

In **direct-contact membrane distillation**, or **DCMD**, warm saline water and cooler fresh water each contact one membrane face. “Direct contact” refers to contact with the membrane—not mixing the two streams. Other configurations use an air gap, vacuum, or sweeping gas on the receiving side.

Useful vocabulary includes:

- **Feed:** incoming saline water.
- **Permeate/distillate:** water transported through the membrane and collected as product. In DCMD, a circulating freshwater stream may collect this product, so its entire outlet flow is not newly produced water.
- **Brine/retentate:** the saline water left behind.
- **Hydrophobic membrane:** a membrane whose pores resist entry by liquid water while allowing vapor transport. PVDF, polyvinylidene fluoride, is one commonly studied material.

The main commercial competitor is **reverse osmosis**, which uses pressure rather than heat to move water through a selective membrane. Large seawater reverse-osmosis installations commonly consume roughly **3–5 kWh of electricity per cubic meter of product water**, depending on plant boundaries and conditions. Membrane distillation instead requires substantial thermal energy plus electricity for circulation and any cooling equipment. Thermal and electrical kilowatt-hours should therefore be reported separately.

## 3. Units and physical reference points

**Power versus energy.** A kilowatt, kW, measures an energy-transfer rate. A kilowatt-hour, kWh, measures an amount of energy. A continuous 1 kW heat source supplies 24 kWh per day.

**Temperature.** Kelvin equals degrees Celsius plus 273.15. Temperature differences have the same numerical size in either unit: a 3 K difference is a 3°C difference. Heat exchange requires a temperature difference, so the receiving water cannot simply reach the hot fluid’s temperature in a finite heat exchanger.

**Salinity.** Ordinary seawater contains about 35 grams of dissolved salts per kilogram, approximately 35 g/L for rough engineering comparisons. **TDS**, total dissolved solids, measures dissolved material, not whether water is safe to drink.

**Water production and membrane flux.** Fresh water weighs approximately 1 kg/L; 1 m³ is 1,000 L. Membrane **mass flux**, usually kg/(m²·h), is production per membrane area. Laboratory DCMD fluxes are often of order **5–40 kg/(m²·h)**, though values outside that range occur. Temperature, salinity, membrane construction, and flow conditions strongly affect the result.

Flux is not total output. For example, 20 kg/(m²·h) through 10 cm²—only 0.001 m²—produces 0.02 kg/h. Square-centimeter membrane areas indicate small test sections rather than industrial-scale treatment.

**Evaporation energy.** At relevant temperatures, evaporating water requires roughly 2.3–2.4 MJ/kg, about 0.65 kWh per liter. Without heat reuse or other losses, 1 kW could evaporate approximately 1.5 L/h. Recovering condensation heat allows larger output per unit of externally supplied heat.

## 4. Heat transfer and the meaning of efficiency

A DCMD membrane transfers energy in two ways: vapor carries **latent heat**, while ordinary **conduction** carries heat through the membrane without producing water. Membrane thermal efficiency commonly means the fraction of membrane heat transfer associated with evaporation. Thus, 60% would mean roughly six-tenths serves evaporation—not that 60% of the feed becomes fresh water or electricity.

The membrane surfaces also differ in temperature from the main flowing streams. This is **temperature polarization**, which reduces the effective driving force. Flowing water more vigorously can reduce it, but usually requires more pumping.

Heat-transfer equations often use three dimensionless quantities: **Reynolds number**, describing flow behavior; **Prandtl number**, comparing momentum and thermal diffusion; and **Nusselt number**, describing convective heat transfer relative to conduction. Empirical correlations connect them, with accuracy depending on channel geometry and flow regime.

Several performance measures must be kept distinct:

- **COP, coefficient of performance:** heat removed divided by electrical power consumed. It can exceed one because cooling moves heat rather than converting electricity into heat removal. Refrigeration-system COPs are often around 3–7; pump-only heat-transport ratios can be much larger. Their equipment boundaries differ.
- **GOR, gained output ratio:** product-water evaporation energy divided by external heat supplied. A simple single-pass system commonly has GOR below one; heat-reusing systems can exceed one without violating energy conservation.
- **Recovery ratio:** product-water flow divided by feed flow. Terminology such as “performance ratio” varies across desalination literature, so the equation is more reliable than the label.

## 5. Energy versus exergy

**Energy analysis** checks conservation. **Exergy analysis** asks how much useful work an energy stream could theoretically provide relative to a specified environment.

Electricity is high-quality energy. Heat near ambient temperature has much less work potential. For perspective, heat supplied at 60°C with a 20°C environment has an ideal heat-to-work limit of about **12%**, before practical losses. Using it directly for warming or evaporation can therefore be more natural than generating electricity.

**Enthalpy** tracks energy carried by flowing material. **Entropy** helps quantify the degradation of energy’s usefulness. **Exergy destruction** measures useful-work potential lost through irreversibilities such as friction, mixing, and heat transfer across temperature differences. Desalination also involves composition-related, or chemical, exergy because separating fresh water from salt requires work even without chemical reactions.

There is no universal “good” exergy-efficiency percentage: the useful product, inputs, reference environment, and system boundary must match before comparing values. An exergy-based **sustainability index** is likewise a thermodynamic indicator, not a complete environmental life-cycle assessment.

## 6. Costs and optimization

**Capital cost** pays for equipment and installation; **operating cost** covers electricity, maintenance, cleaning, and replacements. Purchased-equipment cost is narrower than total installed investment.

**Simple payback** divides extra investment by annual net savings or revenue. It does not fully account for discounting, financing, changing prices, or later replacement costs. **Levelization** spreads costs over an assumed lifetime using a discount rate and operating schedule. Continuous operation means at most 8,760 hours per year; 8,000 hours is about 91% utilization.

**Thermoeconomics**, or **exergoeconomics** when exergy is used, assigns costs to useful physical streams. An **exergy-cost matrix** is bookkeeping that links component cost balances and allocation rules. Here, “fuel” means a resource consumed and “product” means a useful output—not necessarily combustible fuel or something sold.

Watch the denominator: **SGD/h is an hourly cost rate**, not SGD/m³ of water. A unit water cost requires dividing the allocated cost rate by water production. No robust universal cost benchmark exists for small waste-heat-driven DCMD installations; scale, heat availability, cold-source provision, membrane life, and cost allocation vary greatly.

Finally, **multiobjective optimization** handles competing aims such as lower cost and higher efficiency. A **Pareto frontier** contains designs where improving one aim requires worsening another. A genetic algorithm searches candidate designs heuristically. Selecting one “best trade-off” requires preferences, often expressed through normalized objectives and weights. Equal weights are a decision rule, not a uniquely determined physical optimum.
