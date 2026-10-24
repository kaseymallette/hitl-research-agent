# Primer — Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system

*Background from gpt-6.1-sol at medium effort, 2026-10-24. This is the model's general knowledge of the field, written to read before the article; it is not a reading of the article and is unchecked.*

## Where this topic sits

This topic joins three engineering fields: cooling electronic equipment, desalinating water, and designing energy systems that deliver more than one useful service. The broader idea is **waste-heat recovery**: heat that must be removed from one process becomes an input to another. It is part of the **energy–water nexus**, the study of how energy production and water supply depend on each other.

Work in this area often combines component models, heat-and-mass balances, equipment-cost estimates, and numerical optimization. Such system-design studies sit between laboratory research on individual technologies and demonstrations of an integrated installation. Component performance, whole-system performance, and commercial-scale performance are distinct levels of evidence.

The central engineering challenge is matching temperatures, not merely finding enough heat. A large quantity of lukewarm water can contain substantial energy while being unsuitable for a process that needs a much hotter source.

## Data-center cooling and two-phase immersion

Almost all electricity consumed by computing equipment eventually becomes heat. **Cooling load**, measured in kilowatts (kW), is the rate at which that heat must be removed; it is not the electricity consumed by the cooling equipment. A 1 kW heat load maintained for 24 hours releases 24 kilowatt-hours (kWh) of thermal energy. A kilowatt is a rate; a kilowatt-hour is an amount.

For scale, individual servers can consume hundreds of watts to several kilowatts. Racks commonly dissipate several to tens of kilowatts, with high-density computing racks exceeding that range. Entire data centers operate at megawatt scales. A kilowatt-scale cooling study therefore concerns a small unit rather than a complete commercial facility.

The principal cooling approaches are:

- **Air cooling:** fans move air over heat sinks, and room or building equipment removes the heat.
- **Direct-to-chip liquid cooling:** liquid flows through cold plates attached to processors.
- **Immersion cooling:** electronics sit in an electrically insulating, or **dielectric**, liquid.

In **single-phase immersion**, the liquid warms but remains liquid. In **two-phase immersion**, it boils at heated surfaces. Vapor rises, condenses on a cooler heat exchanger, and returns to the bath. “Two-phase” means liquid and vapor coexist; it does not mean two different liquids.

Boiling removes heat through **latent heat**, the energy absorbed during a phase change, rather than only through a temperature rise, called **sensible heat**. A suitable dielectric fluid can boil at temperatures far below water’s normal boiling point. The electronics-contact fluid and the coolant inside the condenser remain separate.

Recovered data-center heat is generally **low-grade heat**, often at temperatures of a few tens of degrees Celsius. Heat flows spontaneously only toward something colder, so every heat exchanger needs a temperature difference. The recovered coolant must therefore leave cooler than the condensing vapor. Temperature differences have the same numerical value in kelvin and degrees Celsius; absolute temperature is K = °C + 273.15.

## How membrane distillation makes fresh water

**Desalination** separates water from dissolved salts. Ordinary seawater contains roughly 35 grams of salt per kilogram of solution, approximately 35 g/L for rough comparisons. **Total dissolved solids**, or TDS, describes the overall dissolved-material concentration.

The dominant commercial seawater technology is **reverse osmosis (RO)**, which uses pressure to force water through a selective membrane. Large seawater RO installations commonly use roughly 3–5 kWh of electricity per cubic meter of product water, depending on the plant and accounting boundary. Thermal alternatives include multi-effect distillation and multistage flash desalination.

**Membrane distillation (MD)** is thermally driven. Warm saline water contacts a porous, water-repelling—or **hydrophobic**—membrane. Water evaporates at the warm surface, travels through gas-filled pores, and condenses on the colder side. Nonvolatile salts stay behind. The membrane does not require the feed to boil: evaporation occurs below the normal boiling temperature, and warmer water has a higher vapor pressure.

In **direct contact membrane distillation (DCMD)**, warm feed water and colder fresh water both touch opposite membrane surfaces. The cold stream is often called the **permeate** stream; its net mass increase is the fresh-water production. Other MD designs introduce an air gap, a vacuum, or a sweep gas. These arrangements trade simplicity, water output, heat leakage, and heat recovery against one another.

MD commonly operates with warm feeds around 40–80°C, although operating ranges vary. It is attractive for low-temperature heat and concentrated brines, but still requires circulation power and a cold side. Maintaining that cold side is a system service: its energy and cost depend on whether cooling comes from the environment, a cooling tower, or refrigeration.

## Reading membrane and heat-transfer numbers

**Mass flux**, usually written J, is water production per membrane area per time, commonly kg/(m²·h). For fresh water, 1 kg is approximately 1 L. Laboratory DCMD fluxes of a few to several tens of kg/(m²·h) are common, but temperature, salinity, membrane properties, and flow conditions strongly affect them; there is no universal benchmark.

Production equals flux multiplied by active membrane area. For example, 20 kg/(m²·h) over 0.01 m² produces 0.2 kg/h, or about 4.8 L/day. Remember that 10,000 cm² equals 1 m²: membrane areas measured in tens of square centimeters are small laboratory-scale areas.

**Heat flux**, in W/m², is heat-transfer rate per unit area. **Thermal conductivity**, in W/(m·K), describes how readily heat crosses a material. **Heat-transfer coefficients**, in W/(m²·K), describe how effectively heat moves between a flowing fluid and a surface.

Membrane thickness, pore size, and **porosity**—the fraction occupied by pores—affect both vapor transport and heat leakage. PVDF, polyvinylidene fluoride, is a commonly used membrane polymer. **Temperature polarization** means membrane surfaces are less hot or cold than their adjacent bulk streams, reducing the actual driving force. **Fouling**, mineral **scaling**, and pore **wetting** can reduce output or impair salt rejection.

Reynolds, Prandtl, and Nusselt numbers are dimensionless tools for estimating flow and heat transfer. Empirical correlations using them are valid only for appropriate flow regimes and geometries.

## Energy, exergy, and different meanings of efficiency

**Energy analysis** applies conservation of energy. **Enthalpy** accounts for energy carried by flowing material. **Entropy** helps quantify irreversibility: real heat transfer, friction, and mixing reduce the ability to obtain useful work.

**Exergy** measures that work potential relative to a specified environment. Electricity is essentially all exergy; lukewarm heat is not. For heat supplied at a fixed temperature T, its ideal work potential is Q(1 − T₀/T), with temperatures in kelvin. Heat at 60°C relative to a 20°C environment has a work potential of only about 12% of its heat content. Desalination also changes composition, so a complete separation-exergy treatment includes concentration effects, not just temperature effects.

Several performance measures must be kept separate:

- **Cooling coefficient of performance (COP):** heat removed divided by cooling electricity consumed. Values above one are normal. Chiller COPs are often around 3–7; pump-only cooling ratios can be much higher because they include different equipment.
- **Membrane thermal efficiency:** the share of heat crossing the membrane that accompanies evaporation rather than direct conduction. It is not a whole-plant efficiency.
- **Gained output ratio (GOR):** product water’s latent-heat equivalent divided by supplied heat. A simple, unrecovered single-stage process generally has GOR below one; heat-reusing systems can exceed one.
- **Water recovery:** product water divided by feed water. “Performance ratio” has varying meanings across desalination literature, so its equation matters.
- **Exergy efficiency:** useful product exergy divided by input exergy. Comparisons require matching product definitions and boundaries.

Evaporating 1 kg of water near these temperatures takes roughly 2.3–2.4 MJ, about 0.65 kWh of heat. That is a useful reference for understanding thermal demand before heat recovery. Thermal kWh and electrical kWh should not be treated as equally valuable inputs.

An exergy-based **sustainability index** is a thermodynamic indicator, not a comprehensive assessment of environmental impact, materials, or water quality.

## Costs and optimization

**Capital cost** pays for equipment and installation; operating costs include electricity, maintenance, and replacements. A **capital recovery factor** converts an initial investment into an equivalent annual payment using an assumed lifetime and interest rate. Operating hours matter: a full year has 8,760 hours, so 8,000 hours represents high utilization.

**Simple payback** is additional investment divided by annual net savings or revenue. It does not capture all lifetime cash flows or investment risk. Water value also depends on whether the comparison uses wholesale production cost, retail tariff, or avoided delivery cost.

**Thermoeconomics**, often called exergoeconomics when based on exergy, assigns costs to energy and material streams. An **exergy-cost matrix** is a set of accounting equations linking those stream costs with equipment costs. “Fuel” means a component’s resource input and “product” its intended service—not necessarily combustible fuel or a saleable commodity.

Units are crucial: SGD/h is a cost rate in Singapore dollars, not a water price. Water costs are usually compared in currency/m³; converting requires dividing the attributable cost rate by water output. Combined cooling-and-water systems also need an explicit rule for sharing costs between services.

Finally, **multiobjective optimization** searches for compromises between competing goals. A **Pareto frontier** contains designs where improving one goal requires worsening another. A **genetic algorithm** searches candidate designs through repeated selection and variation. Choosing a “best trade-off” additionally requires preferences: normalization, objective weights, and design constraints. Those choices identify a preferred compromise, not a universally best design.
