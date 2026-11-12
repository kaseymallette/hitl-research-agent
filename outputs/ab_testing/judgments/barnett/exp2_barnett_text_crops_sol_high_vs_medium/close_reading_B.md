# Close reading — run B

**Run:** B (`runs/B/analysis.json`)
**id:** `182e2233-37de-4fde-b637-d787f5cc0fef`
**Article:** Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866.
**Reference list:** `judgments/claims_reference.md`, used as written.
**Seed (A1 sample):** `20261025`. Python `random.seed(20261025); random.sample(range(109), 30)`, claims numbered 1–109 in reading order.

**How I checked.** I extracted the article's text with pypdf. The PDF can't be rendered here because poppler isn't installed, so I didn't view the graphical abstract by eye. Run B records no reading of it, so nothing depended on that. I checked verbatim strings, numbers, and reference entries with a script after normalizing whitespace, line-break hyphenation, and quote marks. I scored A1 by hand against the passages.

**Size of the run:** 26 steps, 109 claims, 46 support items, 64 citations.

---

## A1. Attribution fidelity (30 of 109 claims sampled)

Sampled claims (1-based): 6, 7, 8, 10, 11, 18, 19, 26, 29, 44, 46, 47, 49, 50, 53, 55, 57, 62, 74, 75, 77, 80, 81, 87, 89, 93, 100, 101, 104, 107.

| Score | Claims | Share |
|---|---|---|
| 2 | 25 | 83% |
| 1 | 5 (C29, C49, C50, C53, C93) | 17% |
| 0 | 0 | 0% |

**Support items attached to sampled claims:** 8 (on C10, C26, C29, C46, C49, C50, C53, C104). All 8 score 2 (100%).

**The 1s:**
- **C29** (§3, p. 3). "…is accelerating as computationally intensive LLM and AI workloads expand…" The article says "demand accelerating **sharply** in the AI era". The intensifier is dropped, and the claim is moved from global data-center withdrawals to "cooling water use" in general. This is a mild softening.
- **C49** (§4.2, p. 4). "Thermally coupling … through closed-loop heat exchangers **can** eliminate consumptive withdrawals." The article reports that "Several installations couple … eliminating consumptive withdrawals." The run turns a report about specific installations into a general capability and adds a modal the article doesn't have.
- **C50** (§4.2, p. 4). "Low consumptive use and favorable WUE leave unresolved ecological questions about … cumulative effects." The article says "These systems **may** have low consumptive water use … cumulative impacts **if widely scaled**." Both the hedge and the scope condition are dropped.
- **C53** (§4.3, p. 4). "Subsea facilities use seawater … eliminating freshwater consumption." The article attaches "eliminating freshwater consumption entirely" to the Hainan installation. The run generalizes it to subsea facilities as a class. The support item correctly ties WUE zero to Hainan.
- **C93** (§6.1, p. 6). "…application-level decisions about justified water costs." The article says "…which AI deployments justify their water costs **in stressed watersheds**." The run drops the scope condition.

**Notes on 2s.** C10's support says the citation covers "its three-part account". That is a fair reading, because the marker closes the sentence that holds all three components. C89 adds "because" between two adjacent sentences, linking transparency limits to operators withholding data. The causal link is a reasonable reading of the juxtaposition, so I scored it 2. C19 is recorded verbatim and correctly. The step's `location`, however, places it in a "continuation printed after the Section 3 heading", which isn't where the article prints it (see A5). The passage was still easy to find.

**Outside the sample, for context.** I didn't score these.
- **C72** is marked verbatim but silently drops an appositive (see A4). Under A1 it would score 0.
- **C51** says natural-water-body cooling in general "can expose data centers to forced curtailment". The article restricts this risk to "once-through or open-loop cooling". The run's support item restores the restriction, but the claim text strips it. This matters because both of the section's examples are closed-loop.

## A2. Coverage (against `claims_reference.md`)

| Type | On list | Caught | Partial | Missed |
|---|---|---|---|---|
| Contributions (C1–C6) | 6 | 6 | 0 | 0 |
| Highlights (H1–H5) | 5 | 4 | 1 (H3) | 0 |
| Abstract (AB1–AB7) | 7 | 6 | 0 | 1 (AB4) |
| Conclusions (CO1–CO26) | 26 | 25 | 1 (CO17) | 0 |
| Figures (F1) | 1 | 0 | 0 | 1 (F1) |
| Tables (T1) | 1 | 0 | 1 (T1) | 0 |

- **H3** ("Technical solutions exist but deployment remains limited by policy gaps"). The run merges the highlights into the abstract step. It records only the abstract's version (C5, "deployment remains limited"), so the highlight's attribution of the limit to **policy gaps** is lost.
- **H1** is the same claim as AB3 and is recorded once, as C3. I counted it as caught.
- **AB4** ("Many data centers are located in water-stressed regions") is missed. The run records Highlight 2's stronger "Two-thirds of post-2022 data centers…" (C4) in its place.
- **CO17** (five research priorities). Four priorities are recorded as claims (C92–C97). The fifth, ecological impact monitoring, appears only in the step's `meaning` as a restatement, not as a claim. The "remain major bottlenecks" framing isn't recorded.
- **F1, the graphical abstract,** is never mentioned. It's the article's only figure.
- **T1, Table 1.** All six rows' WUE and per-MW consumption values are read correctly, along with all three footnotes (a, b, c). The **Example Facility** column isn't read, apart from Meta Luleå via footnote a. The **Key Trade-off** entries for the evaporative and free-air rows are also left out. The other four rows' trade-offs are recorded.
- **CO1–CO16 and CO18–CO26** are all caught, including each §4 subsection's conclusion, trade-offs, scalability, and examples (CO22–CO26). The run keeps several qualifiers the reference list flags: the Natick inference ("suggesting", C54), Espoo as "planned … expected", footnote a's approximation, and the conditional "If this increase in AI use continues".
- **Where the reading stops.** The run doesn't stop early. It runs past the reference list's endpoint and also records the CRediT, competing-interest, and data-availability statements (step 26). This is harmless, but those statements are out of scope for the list.

## A3. Strength of language: **1**

The run keeps most of the article's certainty markers and scope conditions:
- "Projections suggest … could" (C3)
- the conditional on continued growth (C9's support item)
- the Bloomberg "suggests about two-thirds" (C38's support item)
- "systematic disregard" (C38), flagged in `meaning` as the author's interpretation
- the Natick inference marked as an inference (C54 and `meaning`)
- "may offer structural advantages" (C80)
- "severely limited" (C89)
- "inadequate" (C85)
- the withdrawal versus consumption qualification on Google's figure (C30)

Strong claims are kept strong, for example C84, C104, and C106 ("irreversibly").

Some slips run the other way. C50 and C51 broaden the claim by dropping a hedge or a technology restriction. C53 generalizes from one installation to a class. C93 drops "in stressed watersheds". In the other direction, C49 adds "can", and C29 drops "sharply". The slips aren't all in one direction, so the reading isn't systematically shifted, which rules out a 0. But they occur often enough in §4.2–4.3 that 2 isn't warranted.

## A4. Mechanical checks

| Check | Pass | Fail |
|---|---|---|
| Verbatim texts found in the article | 16 | 1 |
| Numbers found in the article | 62 distinct number tokens; all present and, on manual review, attached to the right quantity and unit | 0 |
| Reference entries matching the article's reference list | 64 | 0 (0 null, 0 invented) |

- **Verbatim fail: C72.** The run records "Digital water sobriety challenges the assumption that AI expansion should proceed without considering water constraints." The article reads "Digital water sobriety**, analogous to frameworks in climate and energy policy,** challenges…". The appositive is cut with no ellipsis.
- **Numbers spot-checked.** These included 700,000 L; 10–50 responses per 500 ml; 4.2–6.6 billion m³; 280 billion L; 50–100+ versus 5–10 kW; 25,500 m³; 21.2 → 66 billion L; 84%; 60–124 billion L; 4,000 km³ split 72/15/13%; 0.066 km³; two-thirds; over 400 centers and nearly 3%; 42% and 15%; 67,000; 6.7 million gal (25.4 million L); 13.6 million MWh; 17 °C at 35 m; WUE below 0.2; over 90%; 5–8 °C; 6–19%; 400–800 servers; below 1 °C; 96%; 20 facilities and 16 in Virginia; over 25%; 10–25%; 40–60%; 62%; about 20 suppliers and about 30,000 apartments; about 40% and about 250,000; 73%. Every one matches the article and keeps its unit and context.
- **Reference entries.** Each matches the article's own list. Diacritics are displaced as PDF-extraction artifacts, for example "Yanez-Barnuevo, M., 2025. … ˜" and "Holzle, ¨". Two `citation_text` values carry the same artifacts and so aren't exactly as printed: "(Yanez-Barnuevo, 2025˜ )" and "(Holzle, ¨ 2022)". No citation was invented or completed. The odd Jain (2025) citation in §5.3, an article on chip verification, is recorded faithfully as the article prints it.
- **Readings of images:** none. The run marks its Table 1 readings `paraphrased` and says it read them "from the retained image". In this PDF, Table 1 is printed as text, so its values appear in the extracted text and were checked with the other numbers above. The run makes no reading of the graphical abstract.

## A5. Detail and readability

- **Steps and coverage.** There are 26 steps, spread evenly in the article's order: highlights and abstract 1; §1 2; §2 2; §3 3, including Table 1; §3.1 1; §3.2 2; §4 6 (one per subsection plus the synthesis); §5 5; §6 3; administrative back matter 1. Step size matches the plan's stated pace of roughly one subsection or a few paragraphs.
- **Can a reader follow the argument?** Yes. The `moves` fields name the argumentative work accurately: concession in §3, analogy in §4.2, inference from Natick, prescriptive consolidation in §6.2. The `meaning` fields track how each step connects to the last. They point out where examples or mechanisms are reused rather than newly established (§5.2, §6.2, §6.3). They also separate the author's interpretation from the evidence offered for it. Someone who hasn't read the article could reconstruct its arc from this reading.
- **Input artifacts leak into the reading.** The plan and step 4 describe an "interrupted methodological passage" in "the prepared text". They place §2's closing sentences "after the Section 3 heading". In the article, all of §2 comes before the §3 heading, so this misdescribes the article's layout and reflects the run's input rather than the source. Table support items are labelled "gap T1", a pipeline label rather than anything in the article.
- **Some distinct claims are merged,** against the instruction to keep them separate. C62 combines the non-potable trade-off, reclaimed-water scalability, and dry-cooling scalability. C67 packs three trade-offs into one claim. C106 combines two closing sentences.
- **Some support items are thin.** Several only say that a citation exists, for example "The author cites the AWARE characterization model." and "A review of data-center waste-heat recovery is cited…". They carry the reference but no evidential content.
- **No padding or repetition.** Restatements are noted as moves rather than recorded again, as the instructions ask.

---

## Summary

Run B is a faithful, well-paced close reading. Its attribution is strong: 83% of sampled claims score 2, none score 0, and every sampled support item scores 2. Mechanically it is clean: all numbers are correct, all 64 reference entries match, and 16 of 17 verbatim quotes are exact. It covers every contribution and all but a fraction of one conclusion, including every §4 subsection's trade-offs and scalability limits. Its `meaning` fields are a real strength, since they keep the author's interpretation apart from the evidence and mark reuse and inference.

Its weaknesses are:
- a cluster of scope and hedge slips in §4.2–4.3 (C49–C51, C53)
- one verbatim quote with a silent omission (C72)
- the missed graphical abstract
- an incomplete reading of Table 1's example-facility and trade-off columns
- AB4 replaced by the stronger highlight figure
- a few merged claims and thin, citation-only support items
- leaked references to its own prepared input, which misdescribe where §2's text sits in the article
