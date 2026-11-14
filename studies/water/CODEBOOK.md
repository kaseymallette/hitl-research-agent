# CODEBOOK — Water Study Experiment

Codes for judging the answers in the water experiment, where each of the three
approaches (original documents, structured analyses, combined) retrieves from
the collection and answers the same research questions.

Judging started blind and head to head: the A/B experiments chose the analysis
setup by tournament. The experiment moves to codebook judging. An answer's
quality can't be judged against a correct answer, because no one has written
one. It is judged by what the answer does, and every code points to the
passage that shows it.

Everything here is *(draft)* until reviewed.

- **Study:** the water study (see [README.md](README.md))
- **Unit coded:** one approach's answer to one research question
- **Adapted from:** the [rubric](RUBRIC.md): its close reading criteria (A) for
  attribution, its argument evaluation criteria (B) for argument

## Dimensions

Answering a research question is two tasks, the same two as the close reading
and the argument evaluation:

- **ATT:** Attribution — what the sources say. Does the answer represent each
  source faithfully and credit each claim to the source that makes it?
- **ARG:** Argument — what the answer argues. The answer is itself an
  argument: it chooses A over B and says why. Does that argument hold up?

A good answer does both. An answer can quote every source correctly and argue
badly, or argue well by leaning on a source for something it never said.

## Excerpt fields

- **Excerpt ID:** for experiment answers, [DIM]-[Q#]-[APPROACH]-[##], where
  APPROACH is DOC (original documents), SA (structured analyses), or COMB
  (combined). For the examples below, taken from the accepted analyses,
  [DIM]-[ARTICLE]-[##], where ARTICLE is HER (Herrera et al. 2025), CER
  (Ceres 2026), or KAN (Kanbur et al. 2020)
- **Question:** the research question answered
- **Code:** the code applied, with its qualifier
- **Answer excerpt:** verbatim from the answer, or for the examples, from the
  close reading or argument evaluation
- **Source passage:** for ATT codes, verbatim from the article the answer
  credits, checked against the article's text; *not found* if it isn't there
- **Judge:** the checking session's finding on the code; for the examples, the
  accepted judgment's finding (03 or 05)
- **Analytic memo:** why the code applies
- **Certain or uncertain:** how sure the coding is

## Codes

A code applies where the passage it cites shows what the definition
describes. ATT codes are checked against the original article, never against
the close reading or argument evaluation, since those are the model's
writing, not the source.

### ATT — Attribution

- **ATT-1: Attributed claim** — a claim credited to a named source that the
  source makes, as the source states it. *(draft)*
- **ATT-2: Misattribution** — a claim credited to a source that doesn't make
  it, or credited to the wrong source. *(draft)*
- **ATT-3: Model reading as source** — a close reading's interpretation or an
  argument evaluation's judgment reported as what a source says. *(draft)*
- **ATT-4: Qualification dropped** — a condition, scope, sample, unit, or hedge
  the source attached to a claim is missing from the answer. *(draft)*
- **ATT-5: Certainty shifted** — a source's claim reported as more or less
  certain than the source states it. *(draft)*
- **ATT-6: Conflict noted** — the answer reports that sources disagree, and on
  what. *(draft)*
- **ATT-7: Comparability check** — the answer explains why findings from
  different sources can't be compared directly: different definitions,
  boundaries, units, or methods. *(draft)*
- **ATT-8: Shared evidence noted** — the answer notes that several sources rest
  on the same underlying estimate or dataset, so their agreement isn't
  independent. *(draft)*
- **ATT-9: Unsourced claim** — a factual claim that needs a source and cites
  none. *(draft)*

### ARG — Argument

- **ARG-1: Reason given** — the answer says why for its conclusion (why A over
  B), not only what the sources say. *(draft)*
- **ARG-2: Evidence weighed** — the answer judges whether the evidence behind
  its conclusion is worthy of belief: method, modeled or measured, scale,
  provenance. *(draft)*
- **ARG-3: Insufficient grounds** — the conclusion goes beyond what the cited
  evidence supports: evidence that only permits a conclusion treated as if it
  settled it. *(draft)*
- **ARG-4: Unstated warrant** — the conclusion depends on an assumption the
  answer never states. *(draft)*
- **ARG-5: Qualified conclusion** — the conclusion carries the conditions and
  scope the evidence calls for. *(draft)*
- **ARG-6: Counterevidence addressed** — the answer takes up evidence or an
  alternative explanation that cuts against its conclusion. *(draft)*
- **ARG-7: Bounded conclusion** — the answer says what the collection doesn't
  establish, and what evidence is missing. *(draft)*
- **ARG-8: Own inference marked** — the answer's own inference is marked as its
  own, not credited to a source. *(draft)*
- **ARG-9: Straw man** — the answer criticizes a source for a claim the source
  didn't make. *(draft)*

### Code qualifiers

- **(partial)** — only part of the pattern is present. *(draft)*
- **(absent — notable)** — the question or the sources call for the pattern
  and the answer lacks it, as when sources conflict and the answer doesn't say
  so. Cite where it would be expected. *(draft)*

## Process

The same as the literacy codebook's trial run:

1. Code a trial set of answers with these codes.
2. A separate session checks every code against the answer and, for ATT codes,
   against the article.
3. The researcher spot-checks where the coding and the check disagree.
4. Revise: codes that didn't fit get clarified, and observations no code fits
   become proposed new codes.

The approaches are compared by how often each code appears in their answers,
reported per code, never as a single score.

## Not yet included

Codes for the water question's own distinctions (withdrawal and consumption,
onsite and grid water, freshwater, drinking-quality, and process water,
modeled and measured results) may be added after the trial run.

## Coded excerpts

Until the experiment produces answers, the examples come from the ten accepted
analyses, which already do both tasks: the close reading attributes claims to
one source, and the argument evaluation makes its own argument about it. Each
example quotes the analysis, quotes the article where an ATT code needs it
(checked against the article's extracted text), and gives the accepted
judgment's finding. Where a code names a flaw in an argument (ARG-3, ARG-4),
the example is a flaw the evaluation found in the article's argument and the
judge confirmed, to show what the pattern looks like. *(draft)*

### ATT — Attribution

#### ATT-HER-01 — Herrera et al. 2025

- **Code:** ATT-1: Attributed claim
- **Source:** close reading, step 11, claim 6; article p. 4, §3.1
- **Judge:** scored 2: the passage supports it, with its condition kept.

**Answer excerpt:**

> "Air cooling can raise total data-centre energy demand by 10%–30% relative to evaporative cooling, depending on temperature and humidity."

**Source passage:**

> "Studies suggest that air cooling can increase total data centre energy demand by 10%–30% compared to evaporative cooling, depending on ambient temperature and humidity levels (Li et al., 2025)."

**Analytic memo:** The number, its comparison, and its condition all survive, and the support item credits the figure to Li et al., as the article does. The article's own hedge ("Studies suggest") isn't carried into the claim, but the claim is attributed to the cited work through its support.

**Certain or uncertain:** Certain.

#### ATT-HER-02 — Herrera et al. 2025

- **Code:** ATT-4: Qualification dropped
- **Source:** close reading, step 2, claim 1; article p. 1, §1
- **Judge:** scored 1: the reading "retains 'roughly' and drops the upper-bound condition."

**Answer excerpt:**

> "By 2030, an estimated 70% of companies worldwide will use AI, associated with roughly $15 trillion in output and productivity gains; anticipated GDP gains are 26% in China and about 14% in North America."

**Source passage:**

> "An estimated 70% of companies worldwide will be using AI technologies, becoming up to roughly $15 trillion in economic output and productivity gains."

**Analytic memo:** "Up to roughly" is a ceiling; "roughly" alone reads as a central estimate. The other figures and the PwC attribution are kept.

**Certain or uncertain:** Certain.

#### ATT-HER-03 — Herrera et al. 2025

- **Code:** ATT-5: Certainty shifted
- **Source:** close reading, step 27, claim 2; article p. 9, §6.3
- **Judge:** scored 1: "'Could prevent' slightly strengthens their preventive sufficiency."

**Answer excerpt:**

> "International reporting and siting standards could prevent transboundary clustering of water stress; the EU Green Deal and US state water regulations offer promising implementation models."

**Source passage:**

> "International standards for sustainability reporting and site location planning could also help prevent water stress clustering across borders."

**Analytic memo:** "Could help prevent" makes standards one contributor; "could prevent" makes them sufficient on their own.

**Certain or uncertain:** Certain.

#### ATT-CER-01 — Ceres 2026

- **Code:** ATT-5: Certainty shifted
- **Source:** close reading, step 22, claim 1; article PDF p. 17, printed p. 16, Recommended Actions
- **Judge:** scored 1: "'will improve evaluation and mitigation' strengthens the report's narrower promise."

**Answer excerpt:**

> "...comprehensive assessment will improve evaluation and mitigation."

**Source passage:**

> "Comprehensive assessments will support better evaluation of water dependency, impacts, and risks, and inform more effective risk mitigation strategies."

**Analytic memo:** The report promises that assessments will support evaluation and inform strategies. The reading turns that into an outcome: assessment will improve mitigation.

**Certain or uncertain:** Certain.

#### ATT-CER-02 — Ceres 2026

- **Code:** ATT-7: Comparability check
- **Source:** argument evaluation, paragraph on the headline withdrawal figures; article PDF p. 11, printed p. 10
- **Judge:** confirmed: "The comparison does not establish equivalent depletion or harm."

**Answer excerpt:**

> "Yet approximately 78% of withdrawals across the studied power fleet are attributed to hydropower, whose turbine flows return to the source (printed page 10). [...] It does not make each gallon equivalent to municipal demand in its consequences for competing users."

**Source passage:**

> "In the states analyzed, the withdrawal volumes were dominated by hydropower (approximately 78%), which passes large volumes through turbines and returns them to the source."

**Analytic memo:** The report compares withdrawals with city water use. The evaluation explains why the two can't be compared directly: most of the withdrawn water returns to its source, while municipal use takes water away from other users. This is the withdrawal-and-consumption distinction the water question depends on.

**Certain or uncertain:** Certain.

### ARG — Argument

#### ARG-CER-01 — Ceres 2026

- **Codes:** ARG-1: Reason given; ARG-6: Counterevidence addressed
- **Source:** argument evaluation, paragraph on the headline withdrawal figures
- **Judge:** confirmed (see ATT-CER-02).

**Answer excerpt:**

> "Counting that water is defensible for describing dependence: generation cannot occur without sufficient flow. It does not make each gallon equivalent to municipal demand in its consequences for competing users. Water can support generation and remain available downstream."

**Analytic memo:** Before concluding, the evaluation grants the strongest case for the report's accounting (generation does depend on that flow), then gives its reason for limiting it: the water stays available downstream.

**Certain or uncertain:** Certain.

#### ARG-CER-02 — Ceres 2026

- **Code:** ARG-2: Evidence weighed
- **Source:** argument evaluation, paragraph on attribution
- **Judge:** confirmed: the article "applies state electricity-use shares to state plant withdrawals [...] This is an acknowledged approximation."

**Answer excerpt:**

> "The study applies data centers' state-level electricity-use shares to withdrawals by power plants within each state. This is a transparent screening approximation, but it does not trace electricity actually delivered to facilities."

**Analytic memo:** The evaluation judges the method behind the headline figure, not just the figure: it credits the approach as transparent and names what it can't measure.

**Certain or uncertain:** Certain.

#### ARG-CER-03 — Ceres 2026

- **Code:** ARG-3: Insufficient grounds (in the article's argument)
- **Source:** argument evaluation; article PDF p. 2, executive summary
- **Judge:** confirmed: "The criticism holds specifically for comparative impact, not merely water-use scale."

**Answer excerpt:**

> "The executive summary's assertion that electricity-related water use has a greater impact than facility cooling goes beyond what the report's withdrawal accounting alone establishes."

**Source passage:**

> "While data center companies typically focus on the amount of water they use to cool the technology running within their facilities, the water used for power generation to meet their massive energy needs has an even greater impact."

**Analytic memo:** The report's evidence is a withdrawal inventory for electricity; it has no matching inventory of direct use or of harm. A conclusion about which has the greater impact needs both.

**Certain or uncertain:** Certain.

#### ARG-CER-04 — Ceres 2026

- **Code:** ARG-4: Unstated warrant (in the article's argument)
- **Source:** argument evaluation, paragraph on attribution
- **Judge:** confirmed "as an inferential limit": the allocation "does not model marginal dispatch or new capacity."

**Answer excerpt:**

> "More fundamentally, allocating a share of existing withdrawals is different from estimating the additional withdrawals caused by another data center."

**Analytic memo:** The report's concern is expansion, which needs the warrant that today's share of withdrawals stands for what new demand would cause. The report never states that assumption, and the evaluation says what would be needed to support it: which plants respond to new demand, and when.

**Certain or uncertain:** Certain.

#### ARG-CER-05 — Ceres 2026

- **Code:** ARG-7: Bounded conclusion
- **Source:** argument evaluation, paragraph on the city comparisons
- **Judge:** confirmed (see ARG-CER-03).

**Answer excerpt:**

> "The present total establishes scale under an accounting convention, not the scale of depletion or social damage."

**Analytic memo:** The evaluation says exactly what the evidence does establish and what it doesn't, rather than accepting or rejecting the total outright.

**Certain or uncertain:** Certain.

#### ARG-HER-01 — Herrera et al. 2025

- **Codes:** ARG-8: Own inference marked; ARG-5: Qualified conclusion
- **Source:** argument evaluation, final paragraph
- **Judge:** B5 scored 2: the evaluation "explicitly states its preference [...] It acknowledges that this preference might undervalue precautionary scenario planning."

**Answer excerpt:**

> "My judgment is shaped by a preference for separating exploratory calculations from demonstrated intervention effects. That preference could undervalue scenarios whose purpose is to motivate preparation before precise data exist. [...] I would use its scenarios to formulate questions, but would withhold confidence in the headline forecast and 95% mitigation claim until their assumptions, calculations, and causal interpretation are reconciled."

**Analytic memo:** The evaluation marks its conclusion as its own, names the framing behind it and how that framing could bias it, and states the conditions under which it would change its view.

**Certain or uncertain:** Certain.

#### ARG-KAN-01 — Kanbur et al. 2020

- **Code:** ARG-3: Insufficient grounds (in the article's argument)
- **Source:** argument evaluation; article PDF p. 15, printed p. 10467, Conclusions
- **Judge:** confirmed: "Recommending SI as a substitute for ε rests only on parallel trends in this case."

**Answer excerpt:**

> "The recommendation to substitute it for exergy efficiency in more complex systems requires a relationship demonstrated beyond the plotted trends of this case (p. 10465)."

**Source passage:**

> "The sustainability index trends were found in parallel to the exergy efficiency trends. [...] In the case of complex hybrid designs that can result in difficulties for exergy efficiency calculations, the sustainability index can be used as an alternative assessment criterion."

**Analytic memo:** Parallel trends in one modeled case permit the substitution; they don't establish that the two measures move together in the more complex systems the recommendation is for.

**Certain or uncertain:** Certain.

#### ARG-KAN-02 — Kanbur et al. 2020

- **Code:** ARG-9: Straw man (partial)
- **Source:** argument evaluation, paragraph on chemical exergy
- **Judge:** B2 scored 1: "The article never claims SI measures environmental impact. It defines SI only as the ratio of fuel exergy to destroyed exergy."

**Answer excerpt:**

> "Its parallel movement with another exergy metric supplies no independent evidence about environmental impacts."

**Analytic memo:** A passing remark aimed at a claim the article doesn't make. The rest of the paragraph addresses the article's actual recommendation, which is why the code is partial.

**Certain or uncertain:** Certain.

### Codes without examples yet

The accepted analyses have no example of ATT-2 (misattribution), ATT-3 (model
reading as source), or ATT-9 (unsourced claim): their sampled claims were all
scored 1 or 2, with none at 0. ATT-6 (conflict noted) and ATT-8 (shared
evidence noted) are about several sources at once, which single-source
analyses don't compare. These need examples from the experiment's answers.
