# Argument evaluations, head to head: run A vs run B

**Article:** Kanbur, Wu & Duan, "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system," *Int J Energy Res* 2020;44:10453–10470.

**Files compared**

| Run | File | `id` |
| --- | --- | --- |
| A | `runs/A/argument_evaluation.json` | `354aac17-6f8d-4355-8ab3-74e9ca6841da` |
| B | `runs/B/argument_evaluation.json` | `dd922c0a-e4a0-40f2-a411-13b0a541f3fe` |

**How I read the article.** The PDF's page images couldn't be rendered in this session (no poppler). I extracted the text with macOS PDFKit and checked every claim below against that text. I read the figures from their descriptions in the text and the reference list, not by eye. So statements about figure shapes (Fig. 5B, 6A, 8) rest on the text plus `problems_reference.md`.

**Overview.** The two evaluations are very alike in structure, length (A 1,312 words, B 1,350), verdict and most of their content. Both credit the paper as an investigable proposal. Both reject the 3.72-year payback and the optimum as unestablished, and both rest that on the same core findings: the payback can't be reconciled with water revenue of about 6 SGD/yr, Eq. 24 duplicates Eq. 22, chemical exergy is omitted, the 20 °C permeate supply is never explained, the validation covers components only, and the optimization uses a workload-set Q̇_DC and a near-minimum area. The differences are at the margins, and they mostly favour B.

---

## Problems found, against `problems_reference.md`

| # | Problem (short) | A | B |
| --- | --- | --- | --- |
| P1 | 3.72-yr payback not reproducible | **Found.** Water ≈ 6.13 SGD/yr; 950 × 6.32 ≈ 6,004 SGD; pump O&M alone exceeds water value | **Found.** Water ≈ 6.13 SGD/yr; 3.72 yr of that repays only ≈ 22.8 SGD; 950 SGD × 6.32 is "an entirely different cost scale" |
| P2 | Flat PP contradicts Eq. 26 / "assumed constant" | Partial. Calls the flatness no evidence of *robustness*, but doesn't tie it to the varying water output | **Found (substance).** "Near-constant payback while water output changes substantially with load and area (Figures 4 and 8) … needs an explicit explanation through the numerator and denominator" |
| P3 | Feasibility claim outruns evidence | Found. No integrated validation, neglected fouling/corrosion, comparator limits the claim | Found. No integrated validation, degradation excluded over a 20-yr investment, simple-payback/discounting caveat |
| P4 | ε (Eq. 24) = GOR (Eq. 22); reported values fit neither | Found. Identical expressions, energy not exergy ratio, "different membrane-area behavior" | Found. Same, and names Fig. 5B (ε falls with area) vs Fig. 6A (GOR rises) explicitly |
| P5 | Text says GOR/PR peak at min area; figure shows max | Missed | Missed. B reads Fig. 6A correctly but doesn't flag the text's contradiction |
| P6 | PR ~100× too large | Missed | Missed |
| P7 | SI identity; SI isn't sustainability evidence | Partial. Sustainability half only | Partial. Sustainability half only |
| P8 | Chemical exergy ignored in desalination | Found | Found |
| P9 | Ė_G on output side of Eq. 19 | Missed | Missed |
| P10 | Levelized costs ≫ cost inputs | Missed | Missed |
| P11 | Cost-matrix errors | Missed (only the unit, see P18) | Missed (only the unit, see P18) |
| P12 | Area trends built into lumped model | Missed | Missed |
| P13 | Optimum on area boundary, minimal water, cost-rate objectives, Q̇_DC not a design variable, equal weights | Mostly found. Near-5 cm² area means little water; equal weights unjustified; Q̇_DC tied to computing workload. Doesn't name the cost-*rate* objective as the mechanism | **Found more fully.** All of A's points, plus "Hourly water cost is not cost per unit of net water produced: minimizing a cost rate can favor a small module" |
| P14 | 5.12 vs 5.13; 0.06 cm² gap meaningless | Missed | Partial. "Reporting hundredths of a square centimetre … gives numerical resolution without demonstrating practical certainty"; doesn't note 5.12 vs 5.13 |
| P15 | Membrane cost near nil vs "high" | Missed | Missed |
| P16 | Validation circular / partial | Partial. Component-only, not integrated | Partial. Same; also notes the four-temperature comparison |
| P17 | COP 1.5× vs 2.15× | Missed | Missed |
| P18 | Unit/currency errors | Partial. "2.74 m³/h … dimensionally unsuitable for a price" | Partial. Same point |
| P19–P20 | T₃ % of kelvin; η arithmetic | Missed | Missed |
| P21 | "Sufficient"/"efficient" asserted; no comparison | Partial. Neighbouring heat-recovery precedents can't establish *this* integration | **Found (substance).** The <6 kW research gap and novelty don't establish desalination is preferable; "No comparative assessment resolves that question"; SDG framing measures nothing |
| P22 | 20 °C permeate supply unaccounted | **Found, more fully.** Only pump electricity is costed; if cooling equipment is needed, "its energy and cost would belong in the assessment" | Found. Asks how the cooler supply "is maintained or replenished" but doesn't connect it to the cost or exergy accounts |
| P23 | Flux closure not given | Missed | Missed |

**Tally.** Counting found = 1 and partial = ½: A ≈ 8, B ≈ 9½. Both catch all four Major problems that turn on the payback and ε (P1, P3, P4, and much of P13). Both miss the same numerical-consistency Majors: P5 and P10.

### What each caught that the other missed

**B, not A:**
- **P2's actual problem.** B ties the flat payback to the large swing in water output and says Eq. 26's numerator and denominator have to explain it. A treats the flatness only as weak evidence of robustness, which is a different and milder point.
- **The cost-rate objective (P13).** B says why the optimizer drifts to a small module: Ċ_dw is an hourly rate, not a cost per unit of water. A notices that the optimum makes little water, but doesn't name the mechanism.
- **False precision of the optimum area (part of P14).**
- **The missing comparison (P21), stated explicitly.** B ties it to the paper's own research-gap argument (the 6 kW limit from the earlier fuel-cell study).
- **Figure-level evidence for P4.** B points to Fig. 5B against Fig. 6A, so a reader can check the contradiction.

**A, not B:**
- **P22 linked to the economics.** A notes that the economic model counts only pump electricity, and that any chiller's energy and cost would belong in it. B raises the boundary gap but doesn't take it into the accounts.
- **A second arithmetic route on P1.** A adds that O&M at 1.092% of a 950 SGD pump (≈ 10.4 SGD/yr) already exceeds the water value. This is a sharper "denominator ≤ 0" argument than B's capital-only one, though it depends on an assumption (see below).
- **The comparator limit.** A says that even a sound payback against stand-alone cooling would say nothing about other heat-recovery or water-supply options. This overlaps B's P21 point, from a different angle.

**Not on the list, confirmed against the article.** Neither run raises a problem outside the reference list that holds up as a distinct problem. Both raise the point that varying the cooling load means varying the computing service. That is already within P13 ("the load isn't a design choice").

---

## Where each is wrong and the other isn't

I checked each run's factual statements about the article: numbers, page locations, equations, the funding and the Table 1 values.

**Run A**
1. **Table 2's pump price, hedged but imprecise.** A writes "Table 2 lists a pump price of SGD950. If that applies to the additional permeate pump…" Table 2's row is "Feed and permeate pumps", 950 SGD, so it covers both pumps. A hedges, so this isn't flatly wrong. But the follow-on claim, that "pump maintenance at the stated 1.092% rate would itself exceed the maximum annual water value", holds only under that hypothetical. If only part of the 950 SGD is the added permeate pump, 1.092% of it can fall below 6.13 SGD (at half, about 5.2 SGD). The conclusion that payback is untenable survives once electricity and membrane replacement are added, but the sentence as written leans on the more favourable reading.
2. **"The results describe different membrane-area behavior for these supposedly identical expressions."** The results *text* says the same thing for both: ε is "higher at the low membrane areas" and GOR has "the highest values at the minimum membrane area" (p. 10464). The difference appears only in the figures, which A doesn't cite. The claim is true of Fig. 5B vs Fig. 6A, but as attributed to "the results" it misdescribes the passage. B, which cites the figures, doesn't make this error.

**Run B**
- I found no statement that the article fails to bear out. Checks that passed: four validation temperatures, differences below 1.5% (Table 1 maximum 1.257%), seawater at 302.75 K and permeate at 293.15 K, Eq. 22 and Eq. 24 identical, "higher capital and operation costs" (abstract), the NTU and Defence Science & Technology Agency funding (Acknowledgments, p. 10468), 5.13–5.19 cm², and the ~6 kW fuel-cell limit (p. 10455). B's arithmetic (6.13 × 3.72 ≈ 22.8 SGD) is correct.
- B's page references switch between PDF and printed page numbers ("PDF p. 1", "printed p. 10459 (PDF p. 7)", "pp. 12–13"). That's inconsistent but traceable, so I don't count it as an error.

---

## The criteria as grounds

- **B1 Premise acceptability.** Both weigh the component validation, the omitted degradation and the unexplained permeate supply, and both test the payback inputs against the article's own numbers. B anchors more of its judgments to specific locations (Table 1, Figs. 4, 5B, 6A, 8, Eq. 22/24/26) than A does. A cites four page locations. **Slight edge B.**
- **B2 Relevance.** Both aim at the claims as made, qualifiers included. Both treat the tariff unit charitably and say so ("conditional on the intended tariff unit" / "a charitable interpretation rather than a verified correction"). Neither attacks a straw man. **Even.**
- **B3 Sufficiency.** Both separate what the evidence permits (an integrated experiment) from what it would require (feasibility). B's close states this most directly: the evidence "does not require accepting the claimed payback, overall efficiency, or recommended optimum". It also names what would be needed: consistent efficiency definitions, a dimensionally coherent cash flow, and integrated validation. B also argues that even a short simple payback could count as preliminary evidence *if* its cash flows were coherent. That sets out the sufficiency question precisely. **Slight edge B.**
- **B4 Unstated warrants and qualifiers.** Both find the same core warrants: permeate supply, chemical exergy, an adjustable Q̇_DC, and equal weights as a preference. B adds the cost-rate warrant and the false precision. A adds the cost consequence of the permeate warrant. **Slight edge B.**
- **B5 Self-attribution.** Both say plainly which judgments are theirs ("This is my arithmetic check"; "My own judgment favors auditable quantities"). Both name their own bias toward reproducible, service-based accounting and how it might undervalue an exploratory paper. Both decline to infer improper influence from funding. B also names the author's *methodological* bias (novelty and favourable indicators get the attention). **Even**, both at the top of the scale.
- **B6 Correctness.** B finds about 1½ more reference problems and makes no errors I could find. A makes two minor ones (one a hedged overreach, one a misattributed passage). **Edge B.**

---

## Verdict

**Run B is better, narrowly.** The two share a verdict, a structure and most findings, so the margin is small. B goes further on the economic and optimization problems: it locates P2 correctly, names the cost-rate mechanism behind the near-minimum-area optimum, and anchors the ε/GOR contradiction to the figures. It also states the sufficiency gap more precisely, and I found no factual errors in it. A's distinct strengths are tying the unexplained 20 °C permeate supply to the cost and energy accounts and adding an O&M-based payback check. Neither outweighs B's additional coverage, and A's O&M check is the one that rests on a misreading of Table 2's pump row. Neither run touches the deeper numerical inconsistencies (P5, P6, P10, P11, P17), so neither should be read as a full audit.

## Order check

- **A first, then B.** Reading A sets the baseline. B then adds the P2 linkage, the cost-rate objective, false precision, the explicit comparison point and the figure citations, and drops only A's permeate-cost link and O&M check. **B better.**
- **B first, then A.** Reading B sets the baseline. A adds the permeate-cost link and the comparator-scope point. It lacks B's P2, cost-rate and precision points, and it introduces the two minor errors. **B better.**

The verdict held in both orders: **B, by a narrow margin.**
