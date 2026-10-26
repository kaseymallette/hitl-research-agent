# Problems reference list

**Article:** Kanbur BB, Wu C, Duan F. "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system." *Int J Energy Res.* 2020;44:10453–10470. DOI 10.1002/er.5677.

**Scope.** This list covers the whole article: abstract, Sections 1–5, Figures 1–10, Tables 1–3, Equations 1–37, and Appendices A–C. The appendices only list property-correlation coefficients, and no problem below comes from them. Locations use the journal page numbers (10453–10470).

**How this list was built.** It was written from the article alone. Where a problem rests on arithmetic, the calculation is shown so a judge can check it. Every input to those calculations is a value printed in the article. Each entry is tagged:

- **[Major]**: undermines a headline result or conclusion (abstract, contributions, or Section 5).
- **[Moderate]**: undermines a supporting result or a stated contribution.
- **[Minor]**: an internal inconsistency or reporting error that doesn't change the main conclusions by itself.

Entries tagged *(lower confidence)* depend on an assumption stated in the entry.

A run gets credit for an entry if it identifies the substance of the problem, even in different words or without the arithmetic.

---

## A. Economic feasibility and payback period

### P1 [Major] The 3.72-year payback can't be reproduced from the article's own inputs
**Passages:** Eq. 26–30 and Table 2 (pp. 10460–10461); Figure 8 and the surrounding text (p. 10465); abstract ("The payback period is found 3.72 years that means the proposed system is economically feasible for real applications"); Section 5.

Eq. 26 gives PP = (TCI_hyb − TCI_s-alone) / [C_w − (C_hyb − C_s-alone)]. The only revenue is the value of the distilled water, C_w = c_w · ṁ_dw, with c_w = 2.74 per m³ (Eq. 28).
- The most water the system makes is 6.13 kg/day (p. 10464). That is about 2.2 m³/yr, worth about **6 SGD/yr**.
- The extra investment is TCI = 6.32 × PEC (Eq. 27), applied to the permeate pump (part of the 950 SGD pump cost in Table 2) and the DCMD module. That comes to roughly **10³ SGD or more**.
- The denominator also subtracts the extra running costs: permeate-pump electricity at 0.2552 SGD/kWh over 8000 h, O&M at 1.092% of PEC, and membrane replacement at 15% of PEC_m. These are the same size as the water revenue or larger, so the denominator is about zero or negative.

On the stated inputs the payback runs to centuries or never arrives, not 3.72 years. The paper never gives the intermediate values (ΔTCI, C_w, ΔC), so a reader can't check the headline number. The cost-side problems in P2, P10 and P15 make this worse.

### P2 [Major] A near-constant payback contradicts Eq. 26, and the authors then say it was "assumed constant"
**Passage:** p. 10465: PP "stays stable at roundly 3.72 years", "the Q̇_DC does not change the PP values remarkably", "the PP is assumed constant"; Figure 8.

Water output ranges from 0.14 to 6.13 kg/day across the design space, a 44-fold spread. Water revenue C_w is the only term in Eq. 26 that tracks it, so PP should move a lot if C_w mattered.
- Figure 8 shows PP between 3.7215 and 3.7255 years, varying by about 0.1%.
- PP also *rises* slightly with membrane area, even though larger areas make about 15 times more water. If water revenue drove the payback, PP would fall with area.

So the plotted PP does not behave the way Eq. 26 predicts. The authors then write that "the PP is assumed constant." That makes the headline economic number partly an assumption, not a computed result. The abstract and conclusion still present it as a finding.

### P3 [Major] The claim of economic feasibility outruns the evidence
**Passages:** abstract ("economically feasible for real applications"); Section 5 ("found economically feasible for further real-scale demonstrations"; "the thermodynamic, economic, and thermoeconomic results showed satisfying performances"); p. 10460 (the payback definition is "a simple definition").

- Feasibility rests on one test: simple, undiscounted payback shorter than a 20-year lifetime. Yet the paper uses a 1.7% interest rate in the CRF (Eq. 33), and the authors themselves say life-cycle methods would be needed for a more detailed assessment.
- The paper's own thermoeconomic result points the other way (P10). The levelized distilled-water cost is about 2.6–5.0 SGD/h for at most 0.256 kg/h of water. That is at least about 10 SGD per kg, or about 10⁴ SGD/m³, against a water value of 2.74 SGD/m³.
- The authors say the hybrid model has not been validated (p. 10460) and that corrosion, salt deposition and membrane fouling were neglected (pp. 10455–10456). Seawater runs through the condenser pipes inside the server tank, so these neglected effects bear directly on real costs.
- The wording shifts between the abstract ("for real applications") and the conclusion ("for further real-scale demonstrations").

---

## B. Thermodynamic metrics

### P4 [Major] The "exergy efficiency" equation is the same as the GOR equation, and neither matches the reported ε values
**Passages:** Eq. 22 (GOR = J·Δh_fg·A_m / Q̇_DC) and Eq. 24 (ε = J·Δh_fg·A_m / Q̇_DC), p. 10459; Figure 5B and its text (p. 10464); Figure 6A.

- Eq. 24 is written exactly like Eq. 22. It is an energy ratio with no exergy terms in it. Eqs. 18–19 define stream exergies and an exergy balance, but ε is never defined from them.
- The reported values don't match each other. ε runs from 27.3% to 53.7%, while GOR stays under about 9% (Figure 6A). Two quantities defined by the same formula can't differ like that.
- The direction is wrong too. Since J doesn't depend on area (P12), Eq. 24 would make ε *rise* with A_m. Figure 5B and the text say ε is highest at the *smallest* area, "since less exergy destruction rates occurred". Eq. 24 contains no destruction term that could cause that.
- The values reported for ε and SI satisfy SI = 1/(1 − ε) exactly. For ε = 53.7%, 1/0.463 = 2.16, the reported maximum SI. For ε = 27.3%, 1/0.727 = 1.38, the reported minimum SI. The same holds for the 20.1% and 6.2% SI gaps. So the ε actually computed seems to be the standard 1 − Ė_D/Ė_F, which is not what Eq. 24 says.

This matters because ε is one of the two objectives in both optimizations (Eq. 35, Figure 10), and its true definition is not stated.

### P5 [Major] The text says GOR and PR peak at the smallest membrane area; Figure 6 and the equations say the largest
**Passage:** p. 10464: "both GOR and PR have the highest values at the minimum membrane area, 5 cm², … the maximum GOR and PR values are nearly 14 times higher than the GOR and PR values of the minimum membrane area."

The sentence contradicts itself. It says the maximum is at the minimum area, then compares the maximum *to* the minimum-area value. The evidence points one way:
- Eq. 22 and Eq. 23 both scale with the water produced.
- Water output rises with area (Figure 4: at 5 cm² it is 93.3% smaller than at 75 cm²).
- Figure 6A and 6B both rise toward the 75–80 cm² edge.

The "14 times higher" figure fits the 75/5 = 15× area ratio, so GOR and PR actually peak at the *largest* area.

### P6 [Moderate] Figure 6B's performance ratio is about 100 times larger than the stated inputs allow
**Passages:** p. 10456 (feed velocity 1.85 m/s, hydraulic diameter 0.003 m); Eq. 23; Figure 6B (axis to 60%, colour bar to about 50%).

- Feed flow: 1.85 m/s × π(0.0015 m)² ≈ 1.3×10⁻⁵ m³/s, or about 0.013 kg/s (about 47 kg/h).
- This flow is consistent with the paper's own T₃ values. Adding 1.5 kW gives ΔT ≈ 1500 / (0.013 × 4000) ≈ 29 K, so T₃ ≈ 331 K against the reported 330.92 K. Adding 0.7 kW gives about 316 K against the reported 316.68 K.
- Peak product is 0.256 kg/h (Figure 4; 6.13 kg / 24 h).
- So PR = ṁ_product / ṁ₁ ≤ 0.256 / 47 ≈ **0.5%**, not the roughly 40–50% plotted.

The GOR magnitudes in Figure 6A, by contrast, do fit the inputs: about 0.256 kg/h × 2.37 MJ/kg / 1.5 kW ≈ 11%.

### P7 [Moderate] "SI tracks ε" is true by definition, and the advice to use SI instead of ε doesn't hold up
**Passages:** p. 10465 ("SI has parallel trends with the ε; thus, it can be assessed instead of ε in further studies when the calculation of ε becomes more complex"); Section 5 (SI "can be used as an alternative assessment criterion").

- SI = Ė_F/Ė_D (Eq. 25). With the standard ε, SI = 1/(1 − ε), and the reported numbers fit this exactly (P4). The "parallel trends" are an identity, not a finding.
- Computing SI needs Ė_F and Ė_D, the same exergy accounting ε needs. SI can't be easier to get when ε is hard.
- Despite its name, SI is only a ratio of exergy supplied to exergy destroyed. It says nothing about brine discharge, materials, or environmental impact, so it isn't evidence that the system is sustainable.

### P8 [Moderate] Chemical exergy is dropped on the grounds that the chemistry doesn't change, yet the system's job is to change the salinity
**Passage:** p. 10459: chemical exergy terms "are not considered in this study since there is no change in the chemical components of the streams."

Desalination separates salt from water. Stream 4 leaves as concentrated brine and stream 7 gains pure water. Concentration (chemical) exergy is exactly what separation changes, and the minimum work of separation is the thermodynamic value of the product. With only thermal exergy counted:
- the exergy efficiency, exergy destruction and SI leave out the useful separation product;
- the distilled-water exergy Ė_dw, which carries the water's cost in the cost matrix, isn't properly defined.

### P9 [Moderate] The exergy balance puts the server heat input on the output side
**Passage:** Eq. 19, p. 10459: Ė_F = Ė_P + Ė_D + Ė_L + Ė_G, where Ė_G is the exergy "gain" from the server heat Q̇_DC.

The text describes Ė_G as an input: the system "gains thermal energy from the servers". Eq. 19 lists it beside product and destruction, as if it were an outflow. Ė_D is then worked out by subtracting Ė_G, so the destruction values, SI = Ė_F/Ė_D, and any destruction-based efficiency depend on this sign choice. The paper doesn't explain the choice.

---

## C. Thermoeconomic model and exergy-cost matrix

### P10 [Major] The levelized costs are far larger than all the cost flowing into the system
**Passages:** Eq. 31–33 (p. 10462); Table 2; Figures 9 and 10; Section 5 ("levelized product cost … between 2.69 and 5.33 SGD/h that corresponded to 64.6 and 127.9 SGD in a day").

A cost balance can't produce more cost than goes in. The inputs here are:
- seawater, priced at zero (c₁ = 0);
- permeate inlet water at T₀, which carries essentially zero exergy cost (see P11);
- pump electricity;
- the levelized capital and O&M charges Ż.

Their sizes:
- **PEC:** about 1775 SGD/kW × 1.5 kW + 950 SGD + 140 SGD/m² × 0.0075 m² ≈ 3,600 SGD.
- **CRF:** at 1.7% over 20 years, ≈ 0.059. Adding O&M at 0.011 gives Ż ≈ 0.07 × 3,600 / 8,000 h ≈ **0.03 SGD/h**. Even using TCI = 6.32 × PEC, Ż is only about 0.2 SGD/h.
- **Pump electricity:** COP rises 2.15× as Q̇_DC goes from 0.7 to 1.5 kW, so the feed pump power is constant. COP in Figure 3A is of order 10, so pump power is about 0.1 kW, which costs about 0.03 SGD/h.

That totals about **0.06–0.25 SGD/h** of inputs, against reported product costs of **2.69–5.33 SGD/h**, 10–50 times larger. The reported costs also roughly double between 0.7 and 1.5 kW. The only input that grows with load is the tank's capital cost (1775 SGD/kW), worth hundredths of an SGD per hour, which can't explain an increase of several SGD/h. The thermoeconomic results can't be reconciled with the article's own cost inputs.

### P11 [Moderate] The exergy-cost matrix (Eq. 34) doesn't match the balances in Table 3
**Passages:** Eq. 34 and Table 3, p. 10462. The matrix is presented as a main contribution: "(c) A unique exergy-cost matrix is built" (p. 10455); "a new and unique exergy-cost matrix" (Section 5).

- **Row 4 (membrane):** it reads (Ė₃ − Ė₂)u₁ + (Ė₇ − Ė₆)u₃ + Ė_dw u₄ = Ż_DCMD. The Table 3 balance is Ċ₃ + Ċ₆ + Ż_DCMD = Ċ₄ + Ċ₇ + Ċ_dw. Stream 2 doesn't enter the membrane, the brine stream 4 is missing, and the signs don't follow from the balance.
- **Undefined cost:** no auxiliary equation defines c₄, the brine stream.
- **Conflicting auxiliary equations:** the permeate-pump row gives "c₃ = u₃", but the DC-tank row gives c₃ = u₁, and the membrane row sets c₆ = c₇ = u₃.
- **Row 3 (permeate pump):** Ė₆u₃ = Ż_pp + c_el·Ẇ_pp leaves out Ċ₅. The text says stream 5 carries Singapore's water price (p. 10461). Stream 5 is also at the reference temperature, 293.15 K = T₀, so its thermal exergy, and hence Ċ₅ = c₅Ė₅, is about zero anyway. Pricing the water through exergy can't carry the purchase cost of the inlet water.
- **Units:** c is defined in $/kJ in the nomenclature, but c₅ = c_w is given as "2.74 m³/h", a flow unit with no currency (see P18).

### P12 [Moderate] Two "findings" about membrane area are built into the model
**Passages:** p. 10457 (T_f "is equal to T₃"); p. 10458 (average-temperature Pr, which the authors say is reasonable only for small setups); p. 10463 ("the produced water rate with 5 cm² is 93.3% smaller … the applied membrane area has a pivotal role"); p. 10464 ("The membrane thermal efficiency is independent of the membrane area"); Section 5.

The DCMD model is lumped. The whole membrane sees the inlet feed temperature T₃, with no cooling of the feed along the channel, so the flux J doesn't depend on area. Two results follow automatically:
- Water output is exactly proportional to area. Since 5/75 = 6.7%, the "93.3% smaller" figure is just the area ratio.
- Thermal efficiency η = JΔh_fg/q″ can't depend on area.

Both are presented as results. In a real module the flux falls along the channel, so scaling with area is less than linear. The authors note that the average-temperature method doesn't suit large systems, but they don't flag that the area trends depend on it.

---

## D. Multi-objective optimization

### P13 [Major] The "optimal" design keeps water output near its minimum, and the objectives can't show it
**Passages:** Eq. 35 (p. 10463); Section 3.5; Figure 10 and its text (pp. 10466–10467); abstract; Section 5 ("optimal … 1.1 kW and 5.13 cm²").

- **Area sits on the boundary.** The best trade-off membrane area (5.13 or 5.19 cm²) is just above the 5 cm² lower bound, so the chosen range decides the result. At 1.1 kW and about 5 cm², water output is roughly 0.3 kg/day. That is near the bottom of the 0.14–6.13 kg/day range, for a system proposed as a desalination unit.
- **The objectives reward a small system.** Both use cost *rates* (Ċ_p, Ċ_dw in $/h), not the cost per unit of water. Water output is not an objective. The ε that is actually reported falls with area (Figure 5B). Every objective therefore favours less membrane and so less water.
- **The load isn't a design choice.** Q̇_DC is the heat the servers give off, set by the IT workload. Choosing an "optimal" load of 1.1 kW is not a design option open to the operator.
- **The middle load is chosen by an unrelated argument.** The text says "the middle Q̇_DC value is selected" because Q̇_DC "has a significant impact on both exergy efficiency and levelized cost". A strong effect doesn't imply a middle optimum.
- **The weighting method can't pick a point here.** The Pareto fronts in Figure 10 are nearly straight lines. After utopia–nadir normalization (Eq. 36), a 50/50 weighted sum (Eq. 37) is almost the same at every point on a straight front. The midpoint is therefore an artifact of the method and the equal weights, not a real optimum.

### P14 [Minor] Inconsistent optimum areas, and differences too small to mean anything
**Passages:** abstract ("membrane area varies between 5.12 and 5.19 cm²"); p. 10466 and Section 5 (5.13 cm² and 5.19 cm²).

- The abstract says 5.12 cm²; the results and conclusion say 5.13 cm².
- The paper explains the 5.13 vs 5.19 cm² gap physically: area "has more dominant impact on the Ċ_dw trends". A gap of 0.06 cm² sits on a boundary-constrained genetic-algorithm result, and the paper doesn't show it is larger than the algorithm's tolerance.

---

## E. Cost inputs

### P15 [Moderate] The membrane cost is almost nil, which contradicts the paper's own claims of "high" membrane costs
**Passages:** Table 2 (DCMD module 140 SGD/m²); p. 10461 (the membrane "requires periodic replacement and this results in high replacement cost values"); p. 10464 ("the increment in the membrane area brings high future cost terms"); p. 10466 (Ċ_dw is lowest because of "the lower capital costs of the DCMD module").

At 140 SGD/m², 5–75 cm² of membrane costs **0.07–1.05 SGD**, and 15% replacement comes to **0.01–0.16 SGD/yr**. These are not "high" costs. The figure also looks like the membrane price alone, without module housing, channels or seals, so DCMD capital is understated. That understatement affects PP, Ċ_dw, and the claim that membrane area barely affects PP or cost.

---

## F. Validation

### P16 [Moderate] The validation is partly circular and covers less than it seems to
**Passages:** p. 10456 ("The heat and mass transfer characteristics of the DCMD module is withdrawn from Reference 31 … the developed DCMD mathematical model is also validated with Reference 31"); Section 3.2 and Table 1 (pp. 10459–10461); conclusion of Section 3.2 ("a very good agreement").

- **Circular.** The membrane properties, channel data and Δh_fg correlation all come from Reference 31, and the model is then checked against Reference 31's results. Agreement shows the model was coded consistently with its source, not that it predicts anything independently.
- **Not three independent checks.** The first q^T column equals U × (T_feed − 20 K). For example, 524.75 × 20 = 10,495 and 980.75 × 50 = 49,037. Only two independent quantities were compared. The mass flux J, which drives water output and therefore all the cost results, is not compared directly.
- **Mislabelled table.** Both heat-flux column groups in Table 1 are headed "q^T", and both are given in W/m²K, a heat-transfer coefficient unit; flux is W/m². From the values, the third group appears to be the vapour heat flux.
- **Nothing validates the combined system.** The authors concede this (p. 10460). The DC-cooling "validation" is cited from earlier work: an experiment up to 21 kW and a separate model. It isn't shown to apply to a seawater-cooled tank at 0.7–1.5 kW.
- **The condenser is never checked.** The tank model is only the energy balance of Eq. 7. Nothing checks that the condenser can actually reject the load when the seawater outlet is only about 3 K below the 61 °C boiling point.

---

## G. Numbers and reporting

### P17 [Moderate] The COP figure in the conclusion contradicts the results, and the COP trend is built into the model
**Passages:** p. 10463 ("the COP trends of the maximum Q̇_DC are 2.15 times as high as the minimum Q̇_DC"); Section 5 ("the COP performance was found 1.5 times higher at the released heat rate of 1.5 kW").

- **2.15 vs 1.5.** The two figures conflict. 1.5/0.7 = 2.14, which fits the 2.15 in the results.
- **Built in.** COP = Q̇_DC/Ẇ_fp (Eq. 20) with constant pump power rises in proportion to Q̇_DC by definition. The text presents it as a result "in parallel to the T₃ increment".

### P18 [Minor] Unit, currency and cross-reference errors
- c_w = "2.74 m³/h" (p. 10460) and c₅ = c_w = "2.74 m³/h" (p. 10461): a volume-flow unit is given for a price. The nomenclature lists c in $/kJ.
- The text uses SGD throughout, but Figures 9 and 10 and the nomenclature use "$".
- Equation cross-references are off. The text says C_w is in "Equation (31)" (actually Eq. 28), C_el,hyb in "Equation (32)" (actually Eq. 29), and C_el,s-alone in "Equation (33)" (actually Eq. 30), p. 10460–10461.
- GOR and PR are given in "%" (nomenclature, Figure 6), though PR is defined as a mass-flow ratio.
- The colour bar in Figure 5B starts at 27.20%, while the text says the minimum ε is 27.3%. This is trivial.

### P19 [Minor] A percentage change in absolute temperature hides the size of the effect
**Passage:** p. 10463: "the increment of 0.8 kW in servers increases T₃ value roundly by 4.5%."

(330.92 − 316.68)/316.68 = 4.5% is correct arithmetic, but a percentage change in kelvin doesn't measure the effect. The rise above the 302.75 K inlet goes from about 13.9 K to about 28.2 K, a doubling. That doubling is what drives the 65% swing in DCMD flux.

### P20 [Minor] The reported J and q″ don't give the reported peak thermal efficiency *(lower confidence)*
**Passages:** p. 10463 (J_max = 34.05 kg/m²h, q″_max = 30.68 kW/m² at 1.5 kW); p. 10464 (η_max = 64.5%); Eq. 21.

η = JΔh_fg/q″ = (34.05/3600) × 2.37×10⁶ / 30,680 ≈ 73%, not 64.5%. Reaching 64.5% would need Δh_fg ≈ 2.09 MJ/kg, well below the latent heat of water at 45–58 °C. The ratio between the two loads, about 1.28, does match the reported 28.8% rise. So the absolute values don't fit together even though the trend does. This assumes the standard latent heat of water; the paper takes its Δh_fg correlation from Reference 31 and doesn't print it.

---

## H. Framing and the research gap

### P21 [Moderate] The sufficiency and "efficient operation" claims are asserted, never tested
**Passages:** p. 10454 ("The generated thermal energy from the DC waste heat systems is able to provide a sufficient amount of energy for desalination units", with no citation); p. 10455 (below 6 kW, waste heat use "may not be efficient for … other well-known thermal processes. Therefore, … there is a research gap"); Section 5 ("The hybrid system can be efficiently operated for the low data center cooling loads"; results "showed satisfying performances").

- **Nothing is compared.** The research gap is that other heat-recovery routes may be inefficient below 6 kW, but DCMD is never compared with any alternative, or with simply rejecting the heat, at these loads.
- **The paper's own numbers don't support "efficient".** At most 6.13 kg of water a day from 1.5 kW of heat, a GOR under about 0.1 (Figure 6A), and a PR under about 1% from the stated flows (P6).
- **"Satisfying" is never defined.** The paper gives no benchmark or threshold for it.
- **The generalization goes unexamined.** The paper moves from a 0.7–1.5 kW server tank to "real-scale" and "data center" use, and states that "the results can be useful for real-scale operations" (Section 5) without checking it.

---

## I. System boundary and model closure

### P22 [Moderate] The 20 °C permeate supply is assumed, never accounted for
**Passages:** p. 10455 (the permeate pump "has inlet stream (stream 5) with the temperature of 293.15 K"); p. 10455 (seawater enters at 302.75 K); Figure 1; Eq. 29 and Table 2.

The DCMD module works because the permeate side is colder than the feed. The permeate enters at 293.15 K (20 °C), almost 10 K below the 302.75 K Singapore seawater, the coldest water the system otherwise has.
- The paper never says where this cold water comes from. Figure 1 shows stream 5 simply entering the system.
- Running once-through needs a steady supply of 20 °C water. Recirculating means rejecting the latent and conducted heat the permeate picks up in the module (up to about 30 kW/m², p. 10463) and cooling it back below the seawater temperature, which needs a chiller or other equipment.
- Neither the energy nor the cost of keeping the permeate at 20 °C appears in the economic model (Eqs. 26–30, Table 2) or in the exergy balance. Only the permeate pump is counted.

The payback, the thermoeconomic costs, and the efficiency results all depend on a cold resource that is left outside the system boundary. This adds to P1, P3 and P10.

### P23 [Minor] The flux is defined from outlet flows, so the model's water output can't be reproduced
**Passage:** Eq. 13 and the text after it, p. 10458.

Eq. 13 defines the mass flux as J = (ṁ₃ − ṁ₄)/A_m = (ṁ₇ − ṁ₆)/A_m. That is a mass balance: it gives J from measured inlet and outlet flows. For a system that hasn't been built, ṁ₄ and ṁ₇ are unknowns, so Eq. 13 can't predict J.
- The paper sets aside the permeability and vapour-pressure methods because membrane characteristics "are determined via experimental measurements that may result in additional uncertainties". It calls the mass-flow route easier "especially for the experimental setups".
- It never says what relation actually closes J in the model. Eq. 12 splits the heat flux into JΔh_fg and conduction, but that needs J or q″ from somewhere else.

J drives the water output, and so every efficiency, cost and optimization result. A reader can't reproduce it from the equations given. This is a gap in the reporting; it doesn't show the computed J is wrong.

---

## Summary table

| # | Severity | Problem | Location |
|---|---|---|---|
| P1 | Major | 3.72-yr payback not reproducible; water revenue ≈ 6 SGD/yr vs ~10³ SGD extra investment | Eq. 26–30, Table 2, Fig. 8, abstract |
| P2 | Major | PP flat (and rising with area) despite 44× water range; "PP is assumed constant" | p. 10465, Fig. 8 |
| P3 | Major | "Economically feasible" rests on undiscounted PP; contradicted by own thermoeconomics; no hybrid validation | abstract, Sec. 5, p. 10460 |
| P4 | Major | ε (Eq. 24) identical to GOR (Eq. 22); reported ε fits neither its equation nor GOR; actual ε = 1 − Ė_D/Ė_F | Eq. 22/24, Figs. 5B, 6A |
| P5 | Major | Text says GOR/PR peak at min area; Fig. 6 and the equations show max area | p. 10464, Fig. 6 |
| P6 | Moderate | PR plotted ~40–50%; stated flows give ≤0.5% | Fig. 6B, p. 10456 |
| P7 | Moderate | SI = 1/(1−ε) is an identity; "use SI instead of ε" incoherent; SI isn't evidence of sustainability | p. 10465, Sec. 5 |
| P8 | Moderate | Chemical (separation) exergy ignored in a desalination system | p. 10459 |
| P9 | Moderate | Server heat input Ė_G on the output side of the exergy balance | Eq. 19 |
| P10 | Major | Levelized costs 2.69–5.33 SGD/h vs ~0.06–0.25 SGD/h of total cost inputs | Eq. 31–33, Figs. 9–10, Sec. 5 |
| P11 | Moderate | Cost matrix row 4 wrong (E₂, signs, missing c₄); c₃ = u₁ vs c₃ = u₃; C₅ omitted; units | Eq. 34, Table 3 |
| P12 | Moderate | Area-proportional water and area-independent η are built into the lumped model | pp. 10457–10458, 10463–10464 |
| P13 | Major | Optimum on area boundary with ~minimum water; cost-rate objectives; Q̇_DC not a design variable; weighted sum near-indifferent on a straight front | Eq. 35–37, Fig. 10, Sec. 5 |
| P14 | Minor | Abstract 5.12 vs text 5.13 cm²; 5.13 vs 5.19 explained physically | abstract, p. 10466 |
| P15 | Moderate | Membrane cost ≈ 0.07–1.05 SGD yet called "high"; module cost understated | Table 2, pp. 10461, 10464, 10466 |
| P16 | Moderate | Validation circular (Ref. 31 both source and check); q^T = U·ΔT, not independent; J not validated; table mislabelled; no combined validation; condenser unchecked | p. 10456, Sec. 3.2, Table 1 |
| P17 | Moderate | COP "1.5 times" (Sec. 5) vs "2.15 times" (results); COP ∝ Q̇_DC by construction | p. 10463, Sec. 5 |
| P18 | Minor | "m³/h" as a price; SGD vs $; wrong equation numbers; ratios in % | pp. 10460–10461, Figs. 9–10 |
| P19 | Minor | T₃ change as 4.5% of kelvin hides a doubling of temperature rise | p. 10463 |
| P20 | Minor (lower confidence) | J_max and q″_max give η ≈ 73%, not 64.5% | pp. 10463–10464 |
| P21 | Moderate | "Sufficient energy", "efficiently operated", "satisfying" asserted without benchmark or comparison | pp. 10454–10455, Sec. 5 |
| P22 | Moderate | 20 °C permeate supply below seawater temperature is assumed; its source, energy and cost are never accounted for | p. 10455, Fig. 1, Eqs. 26–30 |
| P23 | Minor | J defined by Eq. 13 mass balance; the relation that actually predicts flux is never given | p. 10458 |
