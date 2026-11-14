# Judgment — close reading

**Article:** `article.pdf`: Zohar Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866 (Making Waves, 7 pp.)

**Run judged:** `run/analysis.json` (20 steps, 105 claims, 61 support items, 68 citations)

**Seed:** `20261107`. Python `random.seed(20261107); random.sample(range(1, 106), 30)`, with claims numbered 1–105 in reading order across all steps.

**Sampled claims (C#):** 4, 5, 9, 10, 20, 22, 23, 24, 28, 31, 32, 37, 40, 43, 49, 52, 55, 57, 71, 72, 73, 78, 85, 89, 93, 94, 95, 97, 100, 104. The sample includes 12 support items.

**How I read the article:** I extracted its text with pypdf. I rendered page 1 with pypdfium2 and looked at the graphical abstract by eye. Table 1 is printed as text, so its values are in the extracted text. The mechanical checks were scripted against the extracted text.

---

## A1. Attribution fidelity

| Score | Claims (n = 30) | Support items (n = 12) |
|---|---|---|
| 2 | 29 (96.7%) | 12 (100%) |
| 1 | 1 (3.3%) | 0 |
| 0 | 0 | 0 |
| Passage not found | 0 | 0 |

**The one 1:**
- **C72** (§5 opening, p. 5). The reading has "Water-sustainable AI requires accountable governance, standardized disclosure, and changed expectations about digital resource consumption." The article says it "requires robust governance frameworks that establish accountability, standardize disclosure, and *fundamentally reframe* societal expectations." The paraphrase drops the author's intensifiers ("robust", "fundamentally reframe" became "changed"). That softens the strength of the claim. The passage does support its content.

**Notes on 2s that were close calls** (none changes the claim against the author):
- **C49** (§4.1). The article says reservoir evaporation "should be considered in lifecycle assessments *of data centers powered by hydroelectricity*". The reading has "should be counted in lifecycle assessment". It drops the qualifier, but the step's context is the hydro-powered Luleå site, so the scope is still clear.
- **C43 S1** (§3.2). Two reservoirs "nearly depleted, *forcing* agricultural communities to rely on trucked and bottled water" became "nearly ran dry **and** farming communities relied on…". The causal link is joined with "and" instead of stated, but both facts are kept.
- **C78 S1** (§5.1). "Practical mechanisms *could* include" became "Proposed instruments include". This firms the hedge slightly. The instruments are listed accurately.
- **C52** is close to verbatim but is marked `paraphrased`. That marking is honest, because it adjusts the wording ("dissolved oxygen" for "dissolved oxygen levels", "neither example" for "Neither facility").
- **C104** (competing-interests declaration) is accurate. It falls outside the reference list's scope but is attributed correctly.

All 12 sampled support items are faithful. Several of them (C9 S1, C23 S1, C24 S1, C28 S1, C49 S1) only describe what is cited ("The U.S. data center energy report supports the comparison") rather than stating evidence. They are accurate, but they add little beyond the citation itself.

No claim field contains the model's own inference. Where the reading adds observations of its own, it puts them in `meaning`. For example, step 19 notes that the Luleå "25 million liters" figure was introduced in §4.1 as a withdrawal, not a consumption figure. That is the correct place for it.

## A2. Coverage (against `claims_reference.md`)

| Type | In list | Caught | Caught without what it shows | Missed |
|---|---|---|---|---|
| Contributions (C1–C6) | 6 | 6 | 0 | 0 |
| Highlights (H1–H5) | 5 | 5 | 0 | 0 |
| Abstract (AB1–AB7) | 7 | 7 | 0 | 0 |
| Conclusions (CO1–CO26) | 26 | 26 | 0 | 0 |
| Figures (F1, graphical abstract) | 1 | 1 | 0 | 0 |
| Tables (T1) | 1 | 1 | 0 | 0 |

Where each item is caught:
- **Contributions:**
  - C1 → run C6, C73, C75, C76
  - C2 → C11
  - C3 → C16
  - C4 → C21, C22
  - C5 → C25–C30
  - C6 → C89–C98
- **Highlights and abstract:** caught in step 1 (run C1–C6), with the highlights and abstract merged where they say the same thing.
  - H5 ("Mandatory facility-level transparency needed") is caught only through C6's mention of mandatory transparency and the later C76/C95. It is not recorded as a highlight claim in its own right.
  - AB4 ("Many data centers…") is folded into C3's two-thirds figure.
  - AB5's four named technologies appear only in C4 S1, the graphical-abstract reading.
- **Conclusions:** every CO item has one or more matching claims. Examples:
  - CO1 → C15
  - CO4 → C41
  - CO8 → C69–C70
  - CO11 → C75
  - CO19 → C99–C100
  - CO22–CO26 → steps 8–12, each including its trade-off and scalability paragraphs.

  CO8 is caught with less detail than the list gives. C70 names the three trade-offs (financial–environmental, energy–water, regional), but only the regional one is spelled out as a claim (C69). The other two are explained only in step 13's `meaning`.
- **F1:** both the flow and the Solutions branch are read and correctly marked `paraphrased` (C4 S1, C6 S1). I checked them against the rendered image, and the elements named match.
- **T1:** all six rows are read with their WUE values, consumption values, examples and trade-offs (C25–C30). All three footnotes are kept: ᵃ in C26 S1, ᵇ in C27 S1, ᶜ in C29 S1.

**Where the reading stops:** it goes past the list's endpoint. Step 20 covers the CRediT statement, the competing-interest declaration, the data-availability statement and the references, which the list excludes. Those three claims (C103–C105) are accurate.

**Found beyond the list** (I confirmed each in the article):
- C7: AI's footprint is invisible to end users (§1, p. 1)
- C19: evaporative cooling vs once-through cooling, consumption vs thermal pollution (§2)
- C81: freshwater as "a finite common resource requiring equitable allocation" (§5.1)
- C87: operators withhold facility data as commercially sensitive (§5.3)

## A3. Strength of language — **2**

The conditions, scope, units and certainty the article attaches survive almost everywhere:
- the conditional on the 2027 projection ("If this increase in AI use continues"), recorded explicitly in C9
- "could" on the 4.2–6.6 billion m³ figure (C2)
- the once-through/open-loop condition on the curtailment risk (C54), which the reference list flags as easy to lose
- "suggesting" for Project Natick (C57)
- "expected" for the planned Espoo region (C65 S5)
- "may" for indirect water savings from heat recovery (C66)
- the withdrawal-versus-consumption caveats on the Google and Luleå figures (C33, C26 S1, step 19 `meaning`)
- the author's strong wording: "inherently", "systematic disregard", "inadequate", "severely limited", "critical", "will persist absent regulatory correction"

The lapses are few, at the level of single words, and go in both directions, so they are not a systematic shift:
- C72 softens "fundamentally reframe" to "changed".
- C11 and C101 recast flat assertions as "the author regards…".
- C15 turns "warranting" into "requiring".
- C73 turns "encompasses… evaluating" into "requiring evaluation".

Since these touch three or four claims out of 105, I scored 2 rather than 1. A stricter reader could call it a high 1.

## A4. Mechanical checks

| Check | Pass | Fail |
|---|---|---|
| Verbatim texts found in the extracted text | 8 | 0 |
| Numbers found in the extracted text (multi-digit and decimal values) | 84 | 0 |
| Numbers written as single digits | 26 | 0 |
| `reference_entry` matches the article's reference list | 68 | 0 |

- **Verbatim:** C5, C40, C46, C82, C89, C99, C100 and C105 are all exact after normalizing quotes and line-break hyphens. No support item is marked verbatim.
- **Numbers:** a substring search can't meaningfully test single digits, so I checked those by eye:
  - "2 L/kWh", "1 MW" and "3 m³/MWh" correctly render the article's "two liters", "one MW" and "three m³/MWh". These are paraphrases, so writing them as digits is fine.
  - The rest ("Table 1", "GPT-3", "5–8 °C", "6–19%", "<1 °C", "3%") are correct in context.
- **References:**
  - All 68 entries match once extraction artifacts are folded (detached diacritics such as "H¨olzle" and "Ya˜nez", line-break hyphens in URLs, and the running page footer).
  - None is null, and none is invented or completed.
  - Every `citation_text` is as printed, including "2025b" for "(Vertiv, 2025a, 2025b…)".
  - Uncited statements are correctly left without citations (Project Natick C57, Stockholm C65 S4).
  - I found no citation printed in a covered passage that the reading omitted.
- **Image-based elements:** the graphical abstract is the only one. The reading's description of it (C4 S1, C6 S1) matches the image and contains no numbers. It is not counted as a failure.

## A5. Detail and readability

- **Steps and pacing:** 20 steps over seven pages, about 300 words of article per step, in line with the prompt's 200–500. Coverage is even:
  - one step each for the front matter, introduction, methods, Table 1 and §3 volumes
  - two steps for §3.1–3.2
  - one step for each technology subsection §4.1–4.5
  - a synthesis step that also pivots to §5
  - two steps for §5.1, one for §5.2–5.3, one each for §6.1, §6.2 and §6.3
  - one step for the back matter
- **Moves and meaning:** the `moves` fields name argumentative moves accurately (defining, qualifying, inferring by analogy, conceding, restating). The `meaning` fields are short and track how the argument builds. Examples are the shift of denominator from global to watershed in step 5, and the widening of the system boundary in steps 8, 9 and 12.
- **Following the argument:** a reader could follow the article from this reading alone.
- **Merging:** a few claims merge distinct sentences, against the prompt's "keep distinct claims separate":
  - C52 merges the ecological-questions sentence with the 5–8 °C and monitoring sentences.
  - C64 merges a trade-off with two scalability limits.
  - C79 merges the climate/biodiversity precedents, the structural advantages and the cautionary conclusion.

  These reduce granularity but don't distort anything.
- **Repetition:** there is little padding. The repetition the article itself makes (Table 1 rows → §4 subsections; §5.1 instruments → §6.2) is handled mostly as restatement moves. Steps 4 and 9 do repeat some Table 1 values as claims, though.

---

## Summary for the researcher

This is a faithful, complete and well-calibrated close reading.
- **Accuracy:** 29 of the 30 sampled claims and all 12 sampled support items score 2. The one 1 is an intensifier dropped from the §5 opening.
- **Mechanical checks:** every verbatim text, number and reference entry checks out against the article.
- **Coverage:** nothing on the reference list is missed. All six rows and three footnotes of Table 1 are read, and the graphical abstract is described correctly as a paraphrase.
- **Strength of language:** the author's conditions and hedges survive, including the easy-to-lose ones (the "if AI use continues" condition on the 2027 projection, the once-through/open-loop scope of the curtailment risk, "expected" for Espoo, and the withdrawal-versus-consumption caveats). The reading keeps its own observations in `meaning`.

The weaknesses are minor:
- a handful of claims that merge several of the author's sentences
- several support items that only restate which source is cited
- the first two of the three §4 trade-offs spelled out only in `meaning`
- three or four claims where an intensifier is softened or a flat assertion is recast as "the author regards"

None of these would mislead a cross-source comparison. On A1–A5 I see nothing that argues against accepting it.
