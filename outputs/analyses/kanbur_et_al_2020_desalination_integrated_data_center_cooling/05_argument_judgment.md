# Judgment — argument evaluation

**Article:** `article.pdf` — Kanbur, Wu & Duan, "Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system," *Int J Energy Res* 2020;44:10453–10470, doi:10.1002/er.5677.

**Run judged:** `run/argument_evaluation.md` (about 1,350 words).

**How the article was read:** the text was extracted with macOS PDFKit. Pages 10459, 10461, 10464 and 10465 were also rendered as images so I could check the equations, Tables 1–2 and Figures 4–8 by eye. Page numbers below are the journal's.

No seed applies to this session. No reference list was used. Every check below is against the article itself.

---

## B1. Premise acceptability — **2**

The evaluation weighs the evidence behind each of the article's central conclusions, says where that evidence comes from, and cites the passage each time.

- **Validation:** it notes that Table 1 shows differences under 1.5%. It then points out that the DCMD model is checked against Reference 31, the same source that supplies its heat- and mass-transfer characteristics and membrane properties (p. 10456). That is a fair point about where the evidence comes from: the check shows the model agrees with its source, not that it was tested independently. It also notes that the authors concede the hybrid system itself is unvalidated (p. 10460).
- **Boundary inputs:** it questions the 293.15 K permeate inlet (p. 10455) and the neglect of fouling, corrosion and salt deposition (p. 10456) as inputs to a 20-year economic case.
- **Economic inputs:** it checks the units of the water price, printed as "2.74 m³/h" (p. 10460, Eq. 28). It also finds that the annual-cost equations (Eqs. 28–29) contain no time conversion. It then shows what this implies with a calculation it labels as conditional.

None of the evidence is taken at face value.

## B2. Relevance of critique — **1**

Almost all of the criticisms address what the author actually claims, with the author's qualifiers kept:

- It aims the feasibility criticism at the abstract's wording, "economically feasible for real applications" (p. 10453).
- It credits the authors for disclosing the 50% weights.
- It credits their concession that the hybrid is unvalidated.
- It criticizes the SI substitution recommendation in the terms the article states it (p. 10465).

Two places are aimed at a broader claim than the article makes:

- **Environmental impact:** it says the sustainability index's parallel trend "supplies no independent evidence about environmental impacts." The article never claims SI measures environmental impact. It defines SI only as the ratio of fuel exergy to destroyed exergy (Eq. 25, after Rosen et al.).
- **"Unconditional optimum":** it sets the optimization against "an unconditional engineering optimum" and a "deployment prescription." The article does call 1.1 kW / 5.13 cm² "optimal" in its conclusion (p. 10467) without a qualifier. But it also says the best trade-off point "is selected according to the design criteria by the decision-maker" (p. 10463), and that its results hold only for low Q̇DC and might differ at larger scales (p. 10467). The evaluation's own conclusion, "a conditional model compromise," is close to the article's own qualified position. So the contrast it draws is partly with a stronger claim than the article makes.

Neither point is the evaluation's main criticism, and neither changes its conclusions. They are the reason this scores 1 rather than 2.

## B3. Sufficiency — **2**

For each of the central conclusions, the evaluation says whether the evidence requires the conclusion or only permits it, and what would be needed to close the gap:

| Conclusion | Evaluation's verdict | What it says is needed |
| --- | --- | --- |
| Thermal coupling | Permitted. Worth investigating as a research hypothesis. | A measured prototype with explicit accounting for the cold side. |
| Economic feasibility (3.72-year payback) | Not reached. | Reconciled units and cash flows, and an explanation of why payback barely moves when water output changes 15-fold. It adds that a 3.72-year payback well under a 20-year lifetime "cannot cure uncertainty in the cash flows." |
| Optimum (1.1 kW, ≈5.1 cm²) | Not required. | A corrected definition of ε, a defended weighting, a water-yield constraint, and a recognition that the cooling load is set by the computing workload, not chosen. |
| Sustainability index as a substitute for ε | Not reached. | A relationship shown beyond the trends plotted for this one case. |

It also says novelty "cannot establish its advantage over competing heat uses or water supplies." That is a sufficiency point about the framing of the whole paper.

## B4. Unstated warrants and missing qualifiers — **2**

It identifies warrants the conclusions depend on but the authors never state, and says why each one matters:

- **Cold permeate supply:** the analysis assumes a continuous supply of cold permeate water at 20 °C but never accounts for the energy and supply cost of keeping it cold.
- **Cooling load as a design variable:** the optimization treats Q̇DC as something a designer can choose (Eq. 35 constraint), when in a real deployment the computing workload fixes it.
- **Equal weights:** giving cost and efficiency 50% each stands in for a stakeholder preference the paper never argues for.
- **Water output:** water output is not among the objectives, so the chosen membrane area of about 5 cm² gives up roughly 93% of the water the 75 cm² option would produce.
- **Chemical exergy:** chemical exergy is left out because "there is no change in the chemical components" (p. 10459). That justification does not cover a separation process, where the components keep their identity but their concentrations change.
- **Sustainability index:** the claim that SI can stand in for ε rests only on the two trending together in this one case.

On missing qualifiers, it finds the abstract's "feasible for real applications" stated without the qualifier the evidence calls for, given an unvalidated hybrid (p. 10460) and an economic model whose inputs cannot be checked. It also points out that the conclusion is weaker than the abstract: "feasible for further real-scale demonstrations."

## B5. Self-attribution — **2**

The evaluation's judgments are written in the first person and are clearly its own: "I therefore cannot treat…", "This is my conditional calculation, not a verified correction…", "I would retain… I would withhold…".

It describes the authors' likely framing:

- their investment in an ongoing immersion-cooling research programme,
- the SDG framing,
- the NTU and Defence Science & Technology Agency funding, with a note that this is context, not evidence of improper influence.

It also names its own bias: "My own emphasis on reproducible definitions and deployment boundaries may undervalue the exploratory contribution of a first model."

No conclusion of its own is presented as the author's position.

## B6. Correctness

### Problems raised (13)

| # | Problem the evaluation raises | Verdict | Passage |
| --- | --- | --- | --- |
| 1 | The abstract's claim of feasibility "for real applications" outruns the evidence. | **Confirmed** | Abstract p. 10453. Hybrid "currently not possible" to validate, p. 10460. The conclusion's weaker "for further real-scale demonstrations," p. 10467. |
| 2 | Alternative heat uses and water supplies appear only as introductory context, not as developed comparators. | **Confirmed** | pp. 10454–10455. The only economic comparator is stand-alone cooling, p. 10460. |
| 3 | The DCMD validation uses the same reference (Ref. 31) that supplies the module's parameters, so it shows consistency, not independent validation. | **Confirmed** | p. 10456 (characteristics, membrane data, "also validated with Reference 31"). p. 10459. Table 1, p. 10461 (maximum difference 1.257%). |
| 4 | The permeate inlet at 293.15 K is assumed, with no accounting for how it would be supplied or kept cold. | **Confirmed** | p. 10455. The models contain no chiller or heat-rejection term. Stream 5 is costed only at the water price (p. 10461). |
| 5 | Fouling, corrosion and salt deposition are neglected even though the economics assume a 20-year life. | **Confirmed** | Assumptions, p. 10456. Listed as future experimental work, p. 10467. |
| 6 | Eq. 24 (ε) is identical to Eq. 22 (GOR), contains no exergy terms, and would increase with membrane area. Yet Fig. 5B shows ε decreasing with area. | **Confirmed** | The two equations are identical as printed (p. 10459, checked on the page image). Flux J does not depend on area: Eqs. 7–14 fix T3 from Q̇DC alone, and water output at 5 cm² is exactly 93.3% (= 1 − 5/75) below 75 cm² (p. 10463). Fig. 5B and its text, p. 10464. Further support the evaluation did not cite: Fig. 6A plots GOR *rising* with area to about 9%, while ε, from the same printed formula, is reported at 27–54% and falling with area (p. 10465). |
| 7 | Omitting chemical exergy is not justified for a separation process. | **Confirmed** (premise). The article's stated justification is as quoted. The critique of it is a sound judgment. | p. 10459 |
| 8 | Recommending SI as a substitute for ε rests only on parallel trends in this case. | **Confirmed** | p. 10465. Conclusion, p. 10467. (The "environmental impacts" aside attacks a claim the article does not make; see B2.) |
| 9 | The water price is printed as "2.74 m³/h", and the annual-cost equations contain no time conversion. | **Confirmed** | Eq. 28, p. 10460. Repeated as c₅ on p. 10461. Eq. 29 multiplies SGD/kWh by kW with no hours term. |
| 10 | Order-of-magnitude check: at 2.74 SGD/m³, 6.13 kg/day is worth about 6 SGD/yr, which cannot recover the added pump and its 6.32× investment multiplier. | **Confirmed as a conditional calculation.** The arithmetic is correct: 6.13 × 365 = 2,237 kg ≈ 2.24 m³, × 2.74 ≈ 6.13 SGD. | Table 2 (p. 10461) lists "Feed and permeate pumps 950.00 SGD." Whether that is per pump or for the pair is ambiguous, but the check holds either way. Eq. 27, p. 10460. |
| 11 | Payback stays nearly constant even though water output changes 15-fold across the area range. | **Confirmed** | Fig. 8 runs from about 3.722 to 3.726 years and in fact *rises* slightly with area, which makes the puzzle sharper (p. 10465). Water output changes by 93.3% across the area range at fixed load (p. 10463). Pump power "does not remarkably" change (p. 10464). |
| 12 | The optimization encodes preferences: equal weights, no water-yield objective, a near-minimum area that gives up most of the water, and the cooling load treated as a choice. | **Confirmed** | Weights, p. 10463. Eq. 35 objectives and constraints. Results, p. 10466. Conclusion, p. 10467. |
| 13 | The SDG framing gives water production importance without showing a comparative benefit. | **Confirmed** | p. 10454 |

**Summary:** 13 problems raised. 13 confirmed: 12 directly, and #10 as the conditional calculation it says it is. None not confirmed. None wrong.

### Errors

**None found.** Every factual statement about the article that I checked holds:

- the numbers: 302.75 K, 293.15 K, the 3 K approach, under 1.5%, 6.13 kg/day, 950 SGD, 6.32, 20 years, 50% weights, 1.1 kW, 5.13–5.19 cm², about 3.72 years;
- the equation numbers: 22, 24, 26, 28;
- the figure and table references: Table 1, Table 2, Figs 5B, 8, 9;
- the page citations;
- the funding description.

The "5.13–5.19 cm²" range matches the body text. The abstract says 5.12–5.19.

### Problems I see that the evaluation does not raise

These are my own reading and are **not** scored against the evaluation.

- **GOR text vs. figure:** the text says GOR and PR "have the highest values at the minimum membrane area, 5 cm²" (p. 10464). Fig. 6A and Eq. 22 both show GOR highest at the *maximum* area.
- **COP ratio:** the results say COP at the highest load is "2.15 times as high" as at the lowest (p. 10463). The conclusion says "1.5 times higher" (p. 10467).
- **Currency units:** levelized costs are given in SGD/h in the abstract but plotted in $/h in Fig. 9, and the nomenclature mixes $ and SGD. This compounds the unit-auditability problem the evaluation raises.
- **Purchased water as an input:** stream 5 (the permeate inlet) is charged at the municipal water price in the thermoeconomic model (p. 10461). Yet the payback model credits only distilled-water output and has no cost for that input water. This goes beyond the evaluation's cold-supply point.

---

## Summary for the researcher

This is a strong, well-targeted evaluation. It picks the weak points in the argument that matter most and checks each one against the text:

- **The ε definition:** the printed definition of exergy efficiency is identical to GOR and cannot produce the trends reported in Fig. 5B. Every conclusion in the article checks out on this, and it bears directly on the recommended optimum.
- **The payback figure:** the 3.72-year payback that carries the feasibility claim cannot be checked as printed. Water value calculated from the paper's own numbers appears far too small to recover the added equipment. And the payback barely moves even though water output varies 15-fold.

All 13 problems it raises hold up against the article, and I found no factual misstatements. It keeps the author's qualifiers and concessions in view, separates what the evidence permits from what it requires, and is open about its own framing.

The one weakness is two passing remarks aimed at claims slightly broader than the article makes:

- that SI says nothing about "environmental impacts";
- the contrast with an "unconditional" optimum.

That is why it scores 1 on B2. Neither remark changes its conclusions.

It is selective rather than exhaustive. It misses some internal inconsistencies, such as the GOR text vs. the figure and the COP ratio, but those are outside what it was asked to cover. On B1–B6 it is suitable to accept.
