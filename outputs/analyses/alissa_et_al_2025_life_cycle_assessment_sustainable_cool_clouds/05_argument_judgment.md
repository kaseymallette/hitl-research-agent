# Judgment — argument evaluation

**Article:** `article.pdf` — Alissa et al., "Using life cycle assessment to drive innovation for sustainable cool clouds", *Nature* 641, 331–338 (2025), Analysis.

**Judged:** `run/argument_evaluation.md`, against the article alone. No reference list was used. I didn't open `run/analysis.json`, `references/claims_reference.md`, or anything in `judgments/`.

**How I read the article:** I extracted the text with macOS PDFKit (through a Swift script), because poppler and the Python PDF libraries weren't installed. I rendered pages 5–7 to images and read Figure 4 by eye. I checked the values in Table 3 against the extracted text: each of the three liquid-cooling columns came out as 12 values, in the order of the 12 parameter rows.

---

## B1. Premise acceptability — **2**

The evaluation weighs the evidence behind the central conclusions and points to the passages it uses:

- **Functional unit.** It treats the Vcore denominator as part of the claimed benefit. Table 3 gives the liquid designs 25–36% more Vcores, and the evaluation notes that the article never shows this extra capacity becomes useful work. That is the main evidential question behind every headline percentage.
- **Modelling inputs.** Methods p. 10 sets cold-plate server power and PUE to the average of the air-cooled and two-phase values. Methods p. 11 gives one-phase immersion the same server power and PUE as two-phase. The evaluation calls these "reasonable starting assumptions" that were never tested for sensitivity.
- **Provenance.** It notes that the two-phase fluid figures were "supplied by the manufacturer" (pp. 334, 339).
- **What the pedigree matrix can tell you.** It says the matrix measures how representative the inputs are, not how far the results move when the inputs change.
- **Scope of the water metric.** The blue-water figure includes water used to generate electricity, and wet cooling depends on outdoor temperature (Methods p. 338).
- **Prototypes.** It reads Figure 2 as showing that the designs are credible candidates, not as evidence of environmental benefit.

Gaps: it doesn't weigh the article's admitted data weaknesses. The electronics data are two decades old (p. 337). The network server is a proxy, estimated at 1.3 × a compute server from internal expertise (p. 337). The one-phase fluid is a natural-gas proxy. These matter less than the points it does weigh, because Figure 4 shows the results are driven by the use phase.

## B2. Relevance of critique — **2**

Each criticism attaches to something the article says:

- **Per-Vcore versus whole facility.** The evaluation presents this as "the claim … a reader could take from the opening percentages," and it notes that the evidence supports reductions per Vcore. The article does carry this ambiguity. The abstract says the reductions are "in data centres." On p. 336 the article says liquid cooling "will lead to marked reductions in data centre environmental impacts," with no per-Vcore qualifier. Only the Conclusions add "per Vcore per year." The evaluation doesn't quote the p. 336 sentence, which would have tied the critique to the author's own wording, but the critique is not a straw man.
- **The 10 GW example (p. 337).** The criticism matches the text: the example keeps 1 thousand million Vcores for both designs.
- **PFAS.** The criticism targets the article's actual sentence: "A broad ban … might be impractical, but science-based regulations … may be effective" (Methods p. 339).
- **Ranking.** It credits the authors' own qualification in the Table 4 footnote ("We are not suggesting any of them are superior") instead of attacking a ranking they disclaimed.

On the SBTi sector target, it is careful to say the article doesn't claim the study meets that target. It doesn't attribute the claim to the authors.

## B3. Sufficiency — **2**

For the central quantitative conclusions, the evaluation separates evidence that permits a conclusion from evidence that requires it, and says what would be needed:

- The per-Vcore savings permit comparing capacity "for the kind of cloud the authors modeled." Applying them elsewhere needs "measured work at comparable service quality."
- The size of the savings needs sensitivity tests on overclocking, utilization and equipment life.
- A facility-level claim needs absolute impacts reported alongside per-service impacts.
- Water claims for a particular site need watershed-level data.
- Regulatory conclusions need evidence that containment works at scale.

It is thinner on the article's other central conclusion, which is in the title: that LCA is important for early-stage design and has "transformative potential." It calls this "the strongest case" and explains how the renewable-energy scenario earns it. It doesn't ask whether one company's single comparative study is enough to support the general claim.

## B4. Unstated warrants and missing qualifiers — **2**

Warrants it finds that the conclusions rely on but the article never states:

- extra Vcores mean an equivalent amount of useful work;
- the 10 GW illustration holds the Vcore count fixed, although Table 3 has liquid designs hosting more;
- lower impact per unit means lower impact for the facility;
- aggregate blue water stands in for local water stress;
- counting the fluid's GHG emissions captures its environmental cost, when hazard is a separate question.

Missing or wrong qualifiers it catches:

- the opening percentages lack "per Vcore";
- the abstract's water range ends at 52%, which doesn't match Table 4 (explained below under problem 4).

In each case it says why the gap matters.

## B5. Self-attribution — **2**

The judgments are written in the first person ("I would therefore use…", "I would extend that caution…"). The evaluation names the authors' position and stake: Microsoft and WSP employees, and a framing that treats cloud growth as a given. It names its own bias: "My own preference is to ask first about absolute emissions and local water use, which can make me underrate a measure that matters to designers choosing how to serve a fixed amount of demand." The 1.07 figure is labelled "an implication of the modeled ratios, not an observed increase or a prediction." Nothing the evaluation concludes is presented as the author's position.

## B6. Correctness

### Problems raised

1. **The headline percentages are per Vcore, and the Vcore count is itself part of the benefit.** **Confirmed.** Table 3 (p. 335) gives 28% more Vcores for cold plate, 25% for one-phase and 36% for two-phase, "with overclocking, part of the functional unit." Overclocking factors are 20%, 10% and 20% higher, and compute server counts are 6–13% higher. The article never shows that this capacity is used: the load factor is a "conservative assumption" (Methods p. 338).

2. **The 10 GW example applies per-Vcore reductions to an unchanged Vcore count, and the modeled designs imply about 7% more total GHG for two-phase.** **Confirmed as arithmetic.**
   - The example (p. 337) holds Vcores at 1 thousand million for both designs.
   - 1.36 × 0.79 ≈ 1.07, using Table 3's Vcore ratio and Table 4's 21% grid-case GHG saving.
   - One nuance the evaluation leaves out: Table 3 also has the two-phase design at 6% higher MW of IT capacity. Part of the higher total therefore comes from a larger IT load, not only from the per-unit framing. The article doesn't clearly say what Table 3 holds constant (Table 2's footnote says data were "collected per MW of IT capacity"). The evaluation's hedge, "for the two modeled designs at their respective Vcore counts," stays within what the tables support.

3. **The ranking between one-phase immersion and cold plate reverses between the grid and renewable cases.** **Confirmed.**
   - Table 4 (p. 336): GHG saving on grid is 16% for one-phase versus 15% for cold plate; on renewable it is 13% versus 16%.
   - The text on p. 335 explains the switch.
   - The authors' qualification is in the Table 4 footnote.

   On the same point, the evaluation reads Figure 4 correctly:
   - air cooling on renewable energy: GHG 11;
   - liquid designs on grid: 79–85;
   - server manufacturing becomes more prominent once operating emissions fall (p. 336).

4. **The abstract's blue-water range (31–52%) doesn't match Table 4. The 52 appears to be the share of impact remaining, not the reduction.** **Confirmed.**
   - The abstract (p. 331) and p. 333 give 31–52%.
   - Table 4's grid-case water savings are 31%, 45% and 48%.
   - Figure 4 shows the two-phase grid water bar at **52** against the baseline of 100. A remaining 52 corresponds to a 48% saving.

   The Conclusions' "0.69 thousand million l" fits Table 4, not the abstract.

5. **No sensitivity analysis; the pedigree matrix doesn't measure how far results move.** **Confirmed.**
   - The only parametric study is grid versus renewable electricity (p. 334).
   - The Table 4 footnote admits the results "are sensitive to design criteria such as overclocking, heat sink design and thermal resistances."
   - The Methods (p. 339) nonetheless conclude that "the uncertainty of the overall results is also low," based on a qualitative pedigree matrix.
   - The averaged and copied design parameters are described accurately (Methods pp. 338–339).

6. **Aggregate blue water can't tell you the pressure on a local watershed.** **Confirmed.** The metric includes thermoelectric water use (pp. 333, 337). Adiabatic cooling switches on above a 35 °C dry-bulb temperature (Methods p. 338). The article makes a water-stress argument for immersion cooling ("particularly important in water-stressed regions," p. 335) without results for specific sites.

7. **The two-phase fluid's small GHG contribution, from manufacturer-supplied data, says nothing about leakage or persistence. The model doesn't show that containment works at scale or justify a position on regulation.** **Confirmed.**
   - The fluid figures are manufacturer-modelled and confidential (pp. 334, 339).
   - Fluid impacts are "low compared with other components" (p. 335).
   - The study's impact categories are GHG, energy and water only.
   - The Methods say LCAs "can calculate PFAS leakage impacts" (p. 339), but this study doesn't.
   - The EHS-first recommendation is on p. 336.

8. **The framing treats cloud growth as given, and the paper doesn't evaluate when retrofitting a working air-cooled installation is worthwhile.** **Confirmed as a reading of the framing.** The introduction (p. 331) treats demand growth as given. The article states the advantage of air cooling, "no required retrofits and new embodied carbon" (p. 336), but no scenario models a retrofit decision.

### Errors

**None found.** I checked every factual statement about the article: page references, table and figure values, Methods assumptions, author affiliations, the placement of the headline percentages before the model is laid out, the EHS-first recommendation, and the PFAS sentence. Each is borne out by the article.

### Problems in the article the evaluation doesn't raise (my own reading, not scored)

- **"At least 15%" GHG doesn't hold in the renewable case.** The Conclusions claim "at least 15% reduction" in GHG, but Table 4's renewable case gives 13% for one-phase. The text on p. 335 itself says "≥13%."
- **The two cooling sections disagree.** The Methods (p. 339) say "immersion cooling offers the most efficient cooling and heat rejection." The corresponding main-text passage (p. 337) says this of "all immersion cooling and cold-plate cooling technologies."
- **The Vcore claim is asserted, not tested.** "A key result from our study was the effectiveness of the virtual core concept" (p. 337), but the study never compares it with any other functional unit.
- **The "low uncertainty" conclusion leans entirely on the use phase.** The data-quality score is 3 out of 5, and the electronics data are acknowledged to be two decades old. That matters more in the renewable scenario, where server embodied impacts dominate (Figure 4).

---

## Summary for the researcher

This is a careful, selective evaluation that is factually accurate.

**Strengths**
- Its main judgment holds up. The headline savings are per Vcore, and the Vcore count is itself increased by liquid cooling. The point is grounded in Table 3, the 10 GW example and a transparent piece of arithmetic, and the evaluation hedges that arithmetic properly.
- It catches a real inconsistency in the abstract: the 52% water figure matches the remaining impact in Figure 4, not any reduction in Table 4.
- It reads Figure 4 correctly.
- It keeps its own view separate from the authors' and states its own bias.
- I found no misstatements about the article.

**Weaknesses**
- It examines the quantitative claims much harder than the methodological one in the title, that LCA is important for early design and has transformative potential. It accepts that claim as "the strongest case" without asking whether one company's single comparative study supports a general conclusion.
- It doesn't use the article's own unqualified sentence on p. 336 ("will lead to marked reductions in data centre environmental impacts"), which would have anchored its main critique more firmly.
- It misses the "at least 15%" GHG claim, which the renewable case contradicts.
- It leaves aside the documented data weaknesses: the two-decade-old electronics data and the network-server proxy.

None of these undermine what it does say.
