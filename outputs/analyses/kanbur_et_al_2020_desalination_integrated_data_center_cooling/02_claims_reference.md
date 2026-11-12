# Claims reference list

**Article:** Kanbur BB, Wu C, Duan F. "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system." *Int J Energy Res.* 2020;44:10453–10470. DOI 10.1002/er.5677.

**Written from the article alone**, in a session of its own, per RUBRIC.md "The reference lists". No run, prompt, or judgment was opened.

## Scope: where the article ends

- **Claims are drawn from the main text:** Summary (abstract), Sections 1–5 (pp. 10453–10467), with Figures 1–10 and Tables 1–3.
- **Not a source of claims:** Nomenclature, Acknowledgments, ORCID, References (1–47), and Appendices A–C (pp. 10470). The appendices hold only the coefficient correlations for seawater enthalpy (A1–A3), density (B1–B9), and entropy (C1–C3), credited to Sharqawy et al (ref. 32). They contain no findings. A reading that stops at the end of Section 5 has covered the article for coverage purposes; a reading that also records the appendices as "coefficient correlations from ref. 32" is accurate.
- Section 4 (Results and discussion) has no numbered subsections. It is split below by the paragraph/figure it discusses, so that each result counts as a conclusion.

## How to use this list

- IDs (AB-, C-, S-, F-, T-) are for counting coverage under A2.
- Quotation marks mean the article's exact wording (as extracted from the PDF text, ligatures and line-break hyphens aside). Everything else is a paraphrase.
- Hedges and strength words the article attaches are recorded, because A3 judges whether they survive. Where the article is confident ("clearly infer", "crucial", "drastic"), that is noted too.
- **Internal inconsistencies:** in several places the article gives different numbers for the same quantity in different places. These are flagged with ⚠ so that a judge does not mark a run wrong for faithfully reporting either version. A run that reports the number from the passage its `location` points to is correct for that passage. These flags are not a problems list (that is `problems_reference.md`).

---

## 1. Abstract (Summary, p. 10453)

| ID | Claim (as stated) | Strength / notes |
| --- | --- | --- |
| AB1 | Waste heat management of data center cooling systems "has a significant share in the energy-efficient operations of the data centers." | Framing premise. |
| AB2 | A new hybrid desalination–data center cooling system is proposed "to reduce the cost drawback of the waste heat in the data center cooling operations." | Aim. |
| AB3 | A two-phase liquid-immersion cooling unit is the DC cooling method, cooling load range 0.7 to 1.5 kW. | Design range. |
| AB4 | Two-phase immersion cooling "is a promising solution thanks to the high heat flux removal performance but there is still a lack of research about waste heat management." | Research gap. |
| AB5 | The immersion system's waste heat heats the feed side of the desalination module; a direct contact membrane distillation (DCMD) system is the desalination module, membrane area range 5 to 75 cm². | Design. |
| AB6 | The system is investigated on thermodynamic, economic, and thermoeconomic aspects; the thermoeconomic assessment uses "the unique exergy-cost matrix of the original design." | Method. |
| AB7 | Maximum thermal and exergy efficiencies are 64.5% and 53.7%, respectively. | Result. |
| AB8 | Daily distilled water "can reach 6.13 kg at the highest cooling load and membrane area." | Result. |
| AB9 | Compared to stand-alone DC cooling, the hybrid system has higher capital and operation costs. | Result. |
| AB10 | Payback period is 3.72 years, "that means the proposed system is economically feasible for real applications." | Strong inference; note the Conclusion words it as feasible "for further real-scale demonstrations" (C-5.5). |
| AB11 | Levelized product cost of the hybrid design is 2.69 to 5.33 SGD/h. | Result. |
| AB12 | In multiobjective optimization, the best trade-off point is at cooling load 1.1 kW "whilst the membrane area varies between 5.12 and 5.19 cm²." | ⚠ Section 4 gives 5.13 and 5.19 cm²; the Conclusion gives only 5.13 cm². "5.12" appears only in the abstract. |

## 2. Enumerated contributions (Section 1, last paragraph, p. 10455)

The article lists four "main original contributions", labelled (a)–(d).

| ID | Contribution |
| --- | --- |
| C-a | "the proposed system has not been investigated before." It uses DC cooling waste heat in the DCMD module, so "clean water production can be achieved." |
| C-b | "it is the first time of the two-phase liquid-immersion cooling system for the waste heat utilization via desalination purposes." This "brings a new alternative to the data center cooling systems, especially for low DC cooling loads." |
| C-c | "A unique exergy-cost matrix is built since the proposed hybrid system is new and has not been investigated before." The design is also assessed economically and thermodynamically. The matrix "can be useful in the waste heat utilization studies of future two-phase liquid-immersion cooling systems." (hedged: "can be useful") |
| C-d | The multiobjective optimization: minimize distilled water cost and system product cost, maximize exergy efficiency; design constraints DC cooling load 0.7–1.5 kW and membrane area 5–75 cm². |

## 3. Section conclusions

### Section 1 — Introduction (pp. 10453–10455)

Background claims (each with its citation):

- S1.1 Global DC energy demand reached 200 TWh in 2018 [ref 1]; US DC consumption projected to reach 70 TWh in 2020 [ref 2]; ICT energy demand "up to 100 times higher" than standard offices [ref 3]; DC cooling is "roundly 40%" of total DC energy consumption, per Rong et al [ref 4]. Hence DC cooling has "a pivotal role" in DC thermal management.
- S1.2 Two DC cooling types, air- and liquid-cooled [ref 5]; both generally reject heat via dry towers or economizers [refs 6, 7]. Waste heat can go to combined heating and cooling [8], district heating/hot water [9], vapor compression [10]. Seawater desalination with DC waste heat was "proposed as an idea by Ebrahimi et al" [11], but "the modeling and performance assessment details were not given in that study."
- S1.3 Desalination integration is "widely-proposed" for other energy systems (nuclear [12], marine [13,14], solar [15,16], fuel cell/gas turbine [17], thermoelectric coolers [18]); those studies "inferred that low-temperature energy systems can be efficiently combined with the desalination process. Thus, the combined solution of DC cooling and seawater desalination has also a strong potential for the real-scale systems." DC waste heat "is able to provide a sufficient amount of energy for desalination units." (Inference from analogy, stated without hedge.)
- S1.4 Combined DC cooling and desalination addresses UN SDGs 6 and 7; it fits the energy–water nexus concept [19, 20].
- S1.5 **Gap 1:** "Up to now, there is no detailed understanding study for this concept."
- S1.6 **Gap 2:** DC waste-heat studies have "usually" been on air-cooled systems; system-scale waste heat studies on liquid-cooled DCs "have not been widely-performed as far as we know." (hedged)
- S1.7 Liquid cooling removes higher heat flux than air; indirect liquid cooling has two drawbacks (leakage potential; layout sizing to the load), which direct cooling overcomes (dielectric liquid contact, no server/rack-level piping; flexible for different loads). Direct methods: jet impingement, spray cooling, two-phase immersion. Two-phase immersion gives "a more uniform temperature distribution" via latent heat transfer [refs 21–24].
- S1.8 **Gap 3:** Despite advantages, two-phase immersion systems "still do not have wide-spread system-scale studies"; companies (Submer, GIGABYTE, 3M, FUJITSU) run system-scale studies, "but there is still a lack of thermal management and economic assessment research."
- S1.9 The authors' prior work: an experimental setup run "up to 21 kW" with "satisfying steady performance" [25]; a model coupled with a PEM fuel cell found low-carbon electricity obtainable at DC load "of nearly 6 kW" [26].
- S1.10 **Gap 4 / section conclusion:** "For the DC cooling loads below 6 kW, the waste heat utilization may not be efficient for low-carbon electricity generation or other well-known thermal processes. Therefore, for lower DC cooling loads, there is a research gap." (hedged "may not")
- S1.11 The study "proposes a novel hybrid system solution" — leading into contributions C-a to C-d.

### Section 2 — System description (pp. 10455–10456)

- S2.1 Configuration (Figure 1): seawater (stream 1; 35 g/L, 302.75 K Singapore seawater, 1 atm [refs 27, 28]) is pumped (EB120 pump by Euroflo) through condenser pipes in a customized server tank (up to 2 kW) filled with NOVEC 7100 (boiling 61 °C); heated seawater (stream 3) feeds the DCMD; permeate enters at 293.15 K (stream 5→6) via a second pump; streams 4 and 7 exit; mass flow of 4 is lower than 3, of 7 higher than 6.
- S2.2 Servers' power rate assumed constant, allowing steady-state assessment [29]. The two-phase immersion setup "was experimentally operated and verified in our previous work" [25].
- S2.3 **Design criterion:** stream 3 cannot exceed 61 °C; "we determine the temperature difference limit as 3 K" between dielectric boiling temperature and stream 3.
- S2.4 DCMD is "the oldest technique of membrane distillation" [30]; hydrophobic membrane passes vapor, blocks liquid.
- S2.5 **Assumptions:** steady state; membrane fouling neglected; DCMD and tank well-insulated (no heat loss); piping well-insulated, justified by the earlier experiment [25] showing pipe heat loss "very small"; server heat 0.7–1.5 kW; DCMD heat/mass transfer characteristics and PVDF membrane (126 μm, 0.41 W/mK, porosity 0.75, pore 0.22 μm) from ref 31; feed velocity 1.85 m/s, permeate 2.92 m/s, hydraulic diameter 0.003 m; corrosion and salt deposition neglected; membrane area 5–75 cm²; reference state 293.15 K, 1 atm; DCMD model validated with ref 31.

### Section 3 — Modeling (pp. 10456–10463)

- S3.0 Modeling has five parts (thermodynamic model, validation, economic, thermoeconomic, multiobjective optimization); the flow is Figure 2.

**3.1 Thermodynamic model**
- S3.1a Energy model: water and seawater enthalpy/density correlations from Sharqawy et al [32] (Eqs 1–4); pump work adds to H1, H5 (Eqs 5–6); tank energy balance H3 = Q_DC + H2 (Eq 7) gives T3.
- S3.1b DCMD heat transfer: feed-side, membrane, and permeate-side fluxes (Eqs 8, 9, 12); Dittus–Boelter Nusselt correlation (Eq 11) [31]; membrane flux = latent (JΔh_fg) + conduction. Δh_fg from ref 31's experimental correlation.
- S3.1c Mass flux is computed from mass flow differences (Eq 13). Alternatives (permeability × vapor pressure difference; non-equilibrium thermodynamics) rely on experimentally measured membrane characteristics "that may result in additional uncertainties" [34]; the mass-flow approach "is an easier way… especially for the experimental setups."
- S3.1d Equations 8–14 are solved iteratively (estimate T_f,m, iterate until q″ balances). Pr is evaluated at average temperatures; this "is a reasonable solution step for the small-scale DCMD setups. However, it must be replaced by the dynamic observation of temperature gradients… for the large-scale commercial DCMD systems." (stated scope limit)
- S3.1e Exergy: specific exergy (Eq 18); chemical exergy "not considered… since there is no change in the chemical components of the streams"; exergy balance with fuel, product, destruction, loss, gain (Eq 19); loss neglected (zero heat loss), gain (from Q_DC) included.
- S3.1f Performance criteria: COP = Q_DC / W_fp (Eq 20); thermal efficiency η = JΔh_fg / q″ (Eq 21); GOR (Eq 22; "the maximum GOR value is desired"); PR = product water / inlet feed (Eq 23); exergy efficiency ε (Eq 24); sustainability index SI = E_F / E_D after Rosen et al [38] (Eq 25).
  - ⚠ Eq 24 (ε) is printed with the same right-hand side as Eq 22 (GOR): JΔh_fg·A_m / Q_DC. A run reproducing either as printed is faithful.
- S3.1g Section conclusion: increasing fuel exergy "via better utilization grows the SI," and lowering exergy destruction "via better design considerations achieves higher SI trends."

**3.2 Thermodynamic model validation**
- S3.2a DCMD model compared with ref 31 at feed 40–70 °C (10 °C steps), permeate 20 °C, without the DC unit; relative differences "less than 1%" at 40, 60, 70 °C and "less than 1.5%" at 50 °C (Table 1).
- S3.2b **Conclusion:** "The obtained results clearly infer that the current mathematical model of the DCMD module is in a very good agreement with the reference study." (strong)
- S3.2c DC cooling side was validated in prior work: experimental steady operation up to Q_DC of 21 kW [25]; model in [26].
- S3.2d **Stated limit:** "the validation of the proposed hybrid model is currently not possible since the proposed system is firstly presented in this paper; but, further studies will focus on their small-scale demonstration."

**3.3 Economic model**
- S3.3a Economic assessment is by payback period relative to a stand-alone DC cooling unit (streams 1–3 only, no permeate pump or DCMD), which has lower capital and future costs; the distilled water's value decides whether the hybrid is "economically more feasible" (Eq 26).
- S3.3b TCI = 6.32·PEC from Bejan et al [36] (Eq 27), chosen as "a well-known and widely-preferred coefficient"; TCI is otherwise "very difficult to calculate… especially for the new-proposed energy systems." PEC from Table 2.
- S3.3c "the given payback period definition is a simple definition"; since both systems have the same lifetime and interest rate, "the basic payback period definition seems sufficient for a comparison purpose." Life-cycle-costing methods "can be preferred" for more detail. (hedged "seems")
- S3.3d Water value C_w = c_w·ṁ_dw with c_w = 2.74 (printed "m³/h") [40] (Eq 28). ⚠ Text calls this "Equation (31)"; the electricity equations printed as (29), (30) are called "(32)" and "(33)" in the text. Units of c_w are printed as "m³/h".
- S3.3e O&M = 1.092% of PEC ("widely-used" [41], used in authors' prior work [42]); membrane replacement cost = 15% of DCMD PEC, after Al-Obaidani et al [27]; stand-alone replacement cost zero; electricity 0.2552 SGD/kWh [43] (Eqs 29–30).
- S3.3f Lifetime 20 years, so a PP over 20 years means "economically infeasible"; lifetime refers to the cooling/DCMD equipment, not the servers; 20 years is "an acceptable value" per prior DC cooling [44, 45] and DCMD [27] analyses.

**3.4 Thermoeconomic model**
- S3.4a The exergy-cost matrix is "a unique cost matrix for each original energy system" [46]. Unit costs: c1 = 0 (seawater "does not have a cost at atmospheric conditions"); c5 = c_w = 2.74; c8 = c9 = 0.2552 SGD/kWh.
- S3.4b Cost balance Ċ_p = Ċ_f + Ż_k (Eq 31); Ż_k from CRF, O&M (1.092%), τ = 8000 h/yr (Eq 32); CRF with i = 1.7%, n = 20 years (Eq 33).
- S3.4c Component balances (Table 3) give the 4×4 exergy-cost matrix (Eq 34) solved for unknown unit costs u1–u4.
- S3.4d **Conclusion/aim:** the thermoeconomic goal is the minimum Ċ_p for the overall system [36]; minimum levelized distilled-water cost Ċ_dw "can be specifically aimed in this study."

**3.5 Multiobjective optimization procedure**
- S3.5a Because the thermodynamic, economic, and thermoeconomic criteria trend differently, "the multi-criteria decision-making step is required"; the best trade-off point is found with the genetic algorithm tool in MATLAB.
- S3.5b Two coupled objectives: (a) ε–Ċ_p (described as "two of the most preferred objective functions" [47]) and (b) ε–Ċ_dw, added because the system is "novel with respect to the energy-water nexus perspective." Constraints 0.7 ≤ Q_DC ≤ 1.5 kW, 5 ≤ A_m ≤ 75 cm² (Eq 35).
- S3.5c The best trade-off point is picked from the Pareto frontier by weighted sum, normalized with utopia and pseudo-nadir points (Eqs 36–37), with equal weights of 50%.

### Section 4 — Results and discussion (pp. 10463–10467)

**4a. Stand-alone DC cooling and DCMD (Figure 3)**
- S4a.1 T3 rises from 316.68 to 330.92 K as Q_DC rises 0.7→1.5 kW (~4.5%). Since DCMD performance depends directly on T3, "the impact of Q_DC on the DCMD performance is crucial."
- S4a.2 COP at maximum Q_DC is "2.15 times as high as" at minimum Q_DC. ⚠ Conclusion says "1.5 times higher" (C-5.1).
- S4a.3 Maximum q″ = 30.68 kW/m² and J = 34.05 kg/m²h at 1.5 kW; from 1.5 to 0.7 kW, q″ and J drop by 55.1% and 64.9%.

**4b. Produced water (Figure 4)**
- S4b.1 Q_DC 1.5→0.7 kW: produced water drops "by nearly 65%, which is a significant decrement and shows the impact of the data center cooling rate on the combined system performance." ⚠ Conclusion says a 0.8 kW increase grows water "1.85 times" (C-5.2); a 65% drop would correspond to ~2.9×.
- S4b.2 Water at 5 cm² is 93.3% smaller than at 75 cm²; "the applied membrane area has a pivotal role in the produced water rate trends." Larger area brings higher future costs, so the trade-off study considers DCMD cost (Table 2).
- S4b.3 With 24-h operation, daily water is 0.14 to 6.13 kg "according to the applied membrane area."

**4c. Energy and exergy efficiency (Figure 5)**
- S4c.1 Membrane thermal efficiency is independent of membrane area (depends only on vapor share of heat flux, Eq 21); minimum 50.1%, maximum 64.5%, an increase of 28.8% from lowest to highest Q_DC.
- S4c.2 ε depends on both A_m and Q_DC via exergy destruction; 0.7→1.5 kW raises ε by 70.2% at 5 cm² and 62.7% at 75 cm². ε is higher at low membrane areas "since less exergy destruction rates occurred." Range 27.3% (min) to 53.7% (max).

**4d. GOR and PR (Figure 6)**
- S4d.1 "both GOR and PR have the highest values at the minimum membrane area, 5 cm²," and the difference between areas "is huge, namely, the maximum GOR and PR values are nearly 14 times higher than the GOR and PR values of the minimum membrane area." ⚠ The two halves of this passage point in opposite directions (highest at minimum area vs. max ~14× the minimum-area value); Eq 22 has A_m in the numerator. Record faithfully either way; see F6.
- S4d.2 Pump power: per the selected pumps' curves, raising area 5→75 cm² "does not remarkably affect the pump power rate"; it can matter at larger scale, but for the low Q_DC proposed, area "is not a critical consideration for the pump operations." (scoped)
- S4d.3 GOR and PR grow with Q_DC: 0.7→1.5 kW, GOR up "nearly 33.8%"; PR reaches "1.9 times higher value."

**4e. Sustainability index (Figure 7)**
- S4e.1 Smaller area and higher Q_DC give higher SI: max 2.16 at 5 cm², 1.5 kW; min 1.38 at 75 cm², 0.7 kW.
- S4e.2 The SI gap between 5 and 75 cm² widens with Q_DC: smallest area 20.1% higher at 1.5 kW, 6.2% at 0.7 kW.
- S4e.3 **Conclusion:** "SI has parallel trends with the ε; thus, it can be assessed instead of ε in further studies when the calculation of ε becomes more complex for different hybrid DCMD-DC cooling systems." (hedged "can")

**4f. Payback period (Figure 8)**
- S4f.1 PP "does not show crucial variation and stays stable at roundly 3.72 years," "very smaller than the system lifetime, 20 years." Q_DC does not change PP remarkably; A_m has "a very small impact."
- S4f.2 Explanation is hedged: the stable trend "may be" due to low cooling loads; Q_DC "may significantly affect the PP at higher DC cooling load operations," and higher areas "can also affect" PP. For the studied range "the PP is assumed constant." Further studies can examine higher Q_DC and A_m.

**4g. Thermoeconomics (Figure 9)**
- S4g.1 Ċ_dw: A_m has "negligible impacts"; Ċ_dw increases "roundly 1.9 times" from 0.7 to 1.5 kW. Ċ_p and Ċ_dc show the same increasing trends (not plotted in 9A).
- S4g.2 Ċ_p is highest (covers both DC cooling and DCMD), "as expected from the nature of the exergy cost matrix." Ċ_dc follows; it is 2.1% below Ċ_p at 0.7 kW and 1.3% below at 1.5 kW.
- S4g.3 Ċ_dw is lowest; the stated reason is "the lower capital costs of the DCMD module" relative to the hybrid total and the DC cooling equipment (Table 2). Ċ_dw is 0.68% below Ċ_dc at 0.7 kW and 6.6% below at 1.5 kW, because the DC cooling capital cost rises "sharper" with Q_DC than the DCMD's. (Conclusion C-5.6 attributes this instead to "lower exergetic costs.")
- S4g.4 **Conclusion:** "the levelized costs dramatically increase with the Q_DC increment," with trends also affected by the exergetic costs of the hybrid (Ċ_p), stand-alone DC cooling (Ċ_dc), and DCMD (Ċ_dw).

**4h. Multiobjective optimization (Figure 10)**
- S4h.1 Optimization run for ε–Ċ_p and ε–Ċ_dw; Ċ_dc excluded "because its performance trends are between the Ċ_p and Ċ_dw trends." Equal 50% weights.
- S4h.2 Best trade-off point (BToP) differs between the two because of the Ċ_p/Ċ_dw cost difference: ε–Ċ_p at Q_DC = 1.1 kW, A_m = 5.13 cm²; ε–Ċ_dw at 1.1 kW, 5.19 cm².
- S4h.3 Same Q_DC for both because Q_DC strongly affects both ε and cost (Figs 5B, 9B), "thus, the middle Q_DC value is selected." Optimal A_m is near the minimum because A_m's impact is smaller than Q_DC's on both.
- S4h.4 Optimal A_m for ε–Ċ_dw is "slightly greater" because A_m has a more dominant impact on Ċ_dw than on Ċ_p.
- S4h.5 **Scope limit:** outcomes are "for the low Q_DC values, and the BToP trends can give different outcomes for larger Q_DC and A_m values"; larger scales "are not considered in this work."

### Section 5 — Conclusion (p. 10467)

Summary statements:
- S5.0a A new hybrid membrane distillation–DC cooling system was presented; "It was the first time combining the desalination unit with the two-phase liquid-immersion cooling operation." Thermoeconomics done "with a new and unique exergy-cost matrix." Optimization on exergy efficiency, levelized product cost, and distilled water cost.
- S5.0b "Even though the proposed system was designed for a specific data center cooling load, the results can be useful for real-scale operations in future studies." (hedged) The system is "one of the energy-water nexus examples."

Bulleted main conclusions (the article's overall conclusions):

| ID | Conclusion | Notes |
| --- | --- | --- |
| C-5.1 | Released heat "crucially increased" DCMD parameters (heat and mass fluxes); COP "1.5 times higher" at 1.5 kW than at 0.7 kW. | ⚠ Section 4 says 2.15× (S4a.2). |
| C-5.2 | System "was able to produce 6.13 kg water in a day" at 75 cm²; a 0.8 kW increase "grew up the produced water rate 1.85 times." | ⚠ Section 4: nearly 65% drop (S4b.1). |
| C-5.3 | Membrane thermal efficiency 50.1–64.5%; overall exergy efficiency 27.3–53.7%. Thermal efficiency independent of area; exergy efficiency "drastically affected." | |
| C-5.4 | SI trends parallel exergy efficiency; highest SI 2.16 at largest released heat and minimum area; SI "can be used as an alternative assessment criterion" for complex hybrid designs. | hedged "can" |
| C-5.5 | PP "calculated as 3.72 years in the operating ranges. The proposed hybrid system was found economically feasible for further real-scale demonstrations." | Abstract: "for real applications" (AB10). |
| C-5.6 | Released heat had "a dominant impact" on levelized costs. "Due to the lower exergetic costs of the DCMD module, it had the minimum levelized cost" among hybrid, stand-alone DC, and DCMD. | Section 4 gives capital cost as the reason (S4g.3). |
| C-5.7 | Levelized product cost 2.69–5.33 SGD/h, "corresponded to 64.6 and 127.9 SGD in a day." | |
| C-5.8 | Optimization found optimal DC cooling rate and membrane area "at 1.1 kW and 5.13 cm² for the hybrid design." | Only the ε–Ċ_p point; abstract gives 5.12–5.19. |

Future work:
- S5.1 First direction: real-scale demonstration, "since the thermodynamic, economic, and thermoeconomic results showed satisfying performances. The hybrid system can be efficiently operated for the low data center cooling loads." Investigate membrane characteristics, distillation techniques, dielectric liquids, and corrosion/salt deposition on the condenser pipe experimentally.
- S5.2 Second direction: large-scale operation, to see its effect on thermodynamic and thermoeconomic results, including corrosion and salt deposition.

---

## 4. Figures

Values marked "by eye" are read from the image and are approximate; the text gives no exact figure for them.

| ID | Location | What it is | What it shows |
| --- | --- | --- | --- |
| F1 | p. 10456 | Schematic of the combined liquid-cooling DC and DCMD system. | Streams 1–9: feed pump (1→2, power stream 8), dielectric liquid bath with two servers and condenser coil (2→3), DCMD module with feed flow (3→4) and permeate flow (6→7) on either side of the membrane, permeate pump (5→6, power stream 9). |
| F2 | p. 10456 | Solution algorithm flowchart. | Inputs (flow characteristics; released heat; membrane area; equipment/energy/water costs) → enthalpy/entropy of streams 1, 5 → pump work → streams 2, 6 → stream 3 → DCMD energy balance → iterative membrane surface temperatures → mass flux → transferred mass → streams 4, 7 → energetic and exergetic assessments → economic analysis and exergy-cost matrix → thermoeconomic assessment → multiobjective optimization with genetic algorithm. |
| F3 | p. 10463 | (A) Stand-alone DC cooling: T3 (K, axis 310–360) and COP (axis 0–20) vs released heat 0.6–1.6 kW, polar-style plot. (B) Stand-alone DCMD: q″ (kW/m², 0–50) and J (kg/m²h, 0–50) vs released heat. | All four rise with released heat. Text values: T3 316.68→330.92 K; COP ratio 2.15×; q″ max 30.68 kW/m², J max 34.05 kg/m²h at 1.5 kW. |
| F4 | p. 10464 | 3-D surface: produced water rate (kg/h) vs membrane area (cm²) and released heat from DC (kW); color bar 0.0050–0.2560. | Water rate rises with both area and heat; highest (~0.25 kg/h by eye) at largest area and highest load. Text: ~65% drop 1.5→0.7 kW; 5 cm² is 93.3% below 75 cm²; 0.14–6.13 kg/day. |
| F5 | p. 10464 | (A) Bar chart, membrane thermal efficiency (%) at 0.7, 0.9, 1.1, 1.3, 1.5 kW. (B) Contour of overall exergy efficiency ε (%) vs membrane area (≈5–75 cm²) and released heat (0.7–1.5 kW); color scale 27.20–53.70. | (A) Bars rise from ~50% to ~64.5% (text: 50.1 to 64.5%), no area dependence. (B) ε highest at low area and high heat (upper left), lowest at high area and low heat; range 27.3–53.7%. |
| F6 | p. 10465 | 3-D surfaces vs membrane area (0–80 cm²) and released heat (0.6–1.6 kW): (A) GOR (%), axis 0–10, color bar 1–9; (B) Performance ratio (%), axis 0–60, color bar 5–50. | Both rise with released heat. By eye, the surfaces rise toward larger membrane area (highest values at the large-area, high-load corner), which matches Eq 22 but conflicts with the text's "highest values at the minimum membrane area" (S4d.1). Text: GOR +33.8%, PR ×1.9 from 0.7 to 1.5 kW; max ~14× the minimum-area value. |
| F7 | p. 10465 | Radar chart of SI on spokes for membrane areas 5, 15, 25, 50, 75 cm², one series per released heat (0.7, 0.9, 1.1, 1.3, 1.5 kW); SI scale ≈1.3–2.2. | SI higher for higher heat and smaller area; text: max 2.16 (5 cm², 1.5 kW), min 1.38 (75 cm², 0.7 kW); gap between areas widens with heat (20.1% vs 6.2%). |
| F8 | p. 10465 | Horizontal bar chart: payback period (years, axis 3.719–3.727) at membrane areas 5, 15, 25, 50, 75 cm². | PP ≈ 3.72 years throughout; by eye, it lengthens slightly with area (≈3.7212 at 5 cm² to ≈3.7262 at 75 cm²), a variation of under 0.01 year. The axis starts at 3.719, which magnifies the bars' visual difference. |
| F9 | p. 10466 | (A) 3-D surface: levelized cost of distilled water ($/h, 2.5–5.5) vs membrane area and released heat. (B) Grouped bars of system product cost, DC released heat cost, distilled water cost ($/h) at 0.7–1.5 kW. | (A) Cost rises with released heat; nearly flat across area. (B) All three rise with load from ≈2.6–2.7 to ≈5.0–5.3 $/h; product cost highest, DC heat cost next, distilled water lowest; gap widens at higher load. Note: axes are labelled "$/h" while the text reports SGD/h. |
| F10 | p. 10466 | Pareto frontier plots: levelized cost ($/h, 2.0–5.5) vs exergy efficiency (%, 30–55) for system product cost and distilled water cost; BToP@Hybrid and BToP@DCMD marked. | Cost rises with exergy efficiency along both fronts (the trade-off); distilled water cost lies below product cost. The two BToPs sit near the middle, by eye at ε ≈ 41–42% and cost ≈ 3.5 $/h (text: both at 1.1 kW; 5.13 and 5.19 cm²). |

## 5. Tables

| ID | Location | What it is | What it shows |
| --- | --- | --- | --- |
| T1 | p. 10461 | Validation of the solution algorithm against Reference 31: at T_feed (T3) 40, 50, 60, 70 °C, current vs reference values for U (W/m²K) and two q^T columns (both printed with units W/m²K), with relative difference (%). | Relative differences: 40 °C 0.025 / 0.029 / 0.821%; 50 °C 1.169 / 1.170 / 1.257%; 60 °C 0.415 / 0.180 / 0.537%; 70 °C 0.466 / 0.467 / 0.211%. All under 1% except 50 °C (under 1.5%). Example values: U 524.75 vs 524.88 at 40 °C; first q^T 49 037 vs 49 267 at 70 °C. Both flux columns carry the same header "q^T (W/m²K)" as printed. |
| T2 | p. 10461 | Purchased equipment cost of the hybrid system. | DC cooling tank 1775.00 SGD/kW-DC cooling load (tank, condenser pipe, dielectric liquid; from the authors' experimental setup [25]); feed and permeate pumps 950.00 SGD (from setup [25]); DCMD module 140.00 SGD/m² [39], converted from USD. |
| T3 | p. 10462 | Thermoeconomic balance equations of the hybrid system, with auxiliary equations. | Feed pump: Ċ1 + c_el·Ẇ_fp + Ż_fp = Ċ2 (c1 = 0, c2 = u1). DC tank: Ċ2 + c_dc·Ė_G + Ż_DC-Tank = Ċ3 (c2 = c3 = u1, c_dc = u2). Membrane: Ċ3 + Ċ6 + Ż_DCMD = Ċ4 + Ċ7 + Ċ_dw (c6 = c7 = u3, c_dw = u4). Permeate pump: Ċ5 + c_el·Ẇ_pp + Ż_pp = Ċ6 (auxiliary printed as "c3 = u3"). Basis of the matrix in Eq 34. |

## 6. Counting summary for A2

| Type | Count | IDs |
| --- | --- | --- |
| Contributions | 4 | C-a to C-d |
| Abstract claims | 12 | AB1–AB12 |
| Conclusions — section/subsection | Sections 1, 2, 3 (3.0, 3.1–3.5), 4 (4a–4h), 5 (summary + future work) | S1.x, S2.x, S3.x, S4x.x, S5.x |
| Conclusions — overall (Section 5 bullets) | 8 | C-5.1 to C-5.8 |
| Figures | 10 (with panels 3A/B, 5A/B, 6A/B, 9A/B) | F1–F10 |
| Tables | 3 | T1–T3 |

For section conclusions, the claims a reading most needs to catch are: S1.10 (gap for loads below 6 kW), S2.3 (3 K limit) and S2.5 (assumptions), S3.1d (Pr averaging valid only small scale), S3.2b and S3.2d (DCMD validated; hybrid not validated), S3.3c and S3.3f (simple PP sufficient for comparison; 20-year threshold), S3.4d, S3.5c (equal weights), S4a.1, S4b.1–2, S4c.1–2, S4d.1, S4e.3, S4f.1–2, S4g.3–4, S4h.2–5.
