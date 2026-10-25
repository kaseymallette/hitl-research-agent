# Close readings, head to head — runs A and B

**Article:** Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866.

**Files compared**

| Run | `id` | Steps | Claims | Support items | Claims marked `verbatim` |
|---|---|---|---|---|---|
| A | `b52aa04e-d9f7-4e11-8e78-fbab1dd1da59` | 25 | 117 | 55 | 13 |
| B | `58057f58-eb36-44ca-bdc6-f8a84ac4f6a6` | 21 | 93 | 43 | 5 |

**Read for this session:** `RUBRIC.md`, `prompts/close-reading.md`, `article.pdf` (text extracted with PyMuPDF), `references/claims_reference.md`, `runs/A/analysis.json`, `runs/B/analysis.json`. No other judgment and no argument evaluation was opened.

**Method.** I read both runs claim by claim against the article and checked them against every entry in the claims reference (C, H, AB, CO, F, T). I ran the A4 checks with a script over the extracted text. I did not rescore A1 on a random sample, because the rubric leaves that to the single-run sessions. The A1–A5 findings below are the grounds for the comparison, not full scores.

---

## 1. Shared baseline

The two readings are very similar. They follow the same order, split the article in nearly the same places, and often paraphrase it in almost the same words. Neither one:

- invents a figure. Neither cites a "Figure 1" or similar; both treat the graphical abstract as the only image and describe it only in `meaning`.
- invents a reference.
- presents an evaluation of the argument as the author's claim.
- stops early. Both read through §6.3 and the end matter.

**A4 mechanical checks (both runs)**

| Check | A | B |
|---|---|---|
| `verbatim` texts found in the article's text | 13 / 13 | 5 / 5 |
| Numbers found in the article's text | 97 / 97 | 91 / 91 |
| `reference_entry` values matching the article's reference list | 64 / 64 | 53 / 53 |

- **Verbatim texts.** Three of A's quotes and one of B's failed a raw string match. In each case the cause was a soft hyphen in the PDF ("opera­tional", "quali­tatively", "di­mensions"). All pass once those are ignored.
- **Reference entries.** Diacritics in the PDF extraction ("Ya˜nez", "Lathuilli`ere") had to be normalized first. After that, every entry matches.
- **Null entries.** Neither run has a `reference_entry` of null. Both leave the citation list empty where the article cites nothing, such as the Lule River hydropower figure in A, and the §6.3 recalls of Luleå and Colón in both runs.
- **Images.** No values were read off an image, so there is nothing to report separately. Table 1 is printed as text, and the graphical abstract has no numbers.

The mechanical checks don't separate the two runs.

---

## 2. What each caught that the other missed (against `claims_reference.md`)

| Ref | A | B |
|---|---|---|
| **T1** Table 1 | **Caught in full.** Six claims, one per row. Each gives WUE, consumption, the example facility, and the Key Trade-off column; footnotes ᵃ and ᶜ are folded into the relevant rows. | **Caught without part of what it shows.** The WUE and consumption values for all rows are in one claim, and footnotes ᵃ, ᵇ and ᶜ are recorded. Missing: the Example Facility column and almost all of the Key Trade-off column (high water use vs. energy efficiency; geographically constrained and seasonal; high capital cost and limited sites; higher electricity use and degrades in hot climates; dual infrastructure). |
| **CO22** §4.1 conclusion | Caught: "Facilities in Nordic regions… can achieve exceptional energy and water efficiency with very low WUE" (C11.2), and Luleå's "minimal on-site water consumption" (C11.3). | **Partial.** B records free-air cooling reducing or eliminating chillers, but drops the Nordic, very-low-WUE conclusion. "Minimal on-site consumption" appears only as "relies predominantly on air cooling" in a support item. |
| **AB5** technologies listed in the abstract | Caught, with all four technologies listed (C1.5). | **Partial.** "Technologies can reduce on-site water demand" (C1.5) leaves out the list of cold-climate siting, natural water body cooling, waterless designs and waste heat recovery. |
| **H3** "…deployment remains limited by policy gaps" | **Partial.** C1.5 follows the abstract ("deployment remains limited") and drops the highlight's attribution to "policy gaps". | Caught (C1.5 includes "limited by policy gaps"). |
| **CO9** SMRs "merit further assessment" | Caught (C16.4: "need assessment"), plus the framing that companies are "exploring" nuclear for "reliable low-carbon electricity independent of grid constraints" (C16.3). | Mostly caught. C14.3 has the shift-not-eliminate point and the dependence on design and siting, but drops "merit further assessment" and the reason companies are exploring nuclear. |
| **CO17** §6.1, ecological monitoring priority | Caught with content: "low consumption can coexist with altered thermal regimes and aquatic effects" (C22.4). | Caught by name only: "Ecological monitoring… remains a research priority" (C18.3), with nothing on what is to be monitored or why. |
| **CO23** curtailment risk limited to once-through or open-loop systems | **Scope lost** (see §3). | Caught with the qualifier: "Open-loop or once-through data centers face analogous risks" (C10.3). |
| §3 sentence "data centers collectively withdraw billions of liters… accelerating sharply in the AI era" (body text, not counted under A2) | Recorded (C6.4). | Not recorded. |

**Covered equally by both runs**

- **C1–C6:** all six.
- **H1, H2, H4, H5:** all four.
- **AB1–AB4, AB6, AB7:** all six. Both runs fold AB4 ("Many data centers…") into the stronger two-thirds figure from H2, and neither records AB4 separately.
- **The other conclusions:** CO1–CO8, CO10–CO16, CO18–CO21, CO24–CO26.
- **F1, the graphical abstract:** both describe it only in `meaning`, at the same coarse level ("three water pathways, then branches toward technical solutions and policy"). Neither names the items listed inside its boxes. Count it as caught without all of what it shows, for both.

**Coverage count**

| Type | A: caught / partial / missed | B: caught / partial / missed |
|---|---|---|
| Contributions (6) | 6 / 0 / 0 | 6 / 0 / 0 |
| Highlights (5) | 4 / 1 (H3) / 0 | 5 / 0 / 0 |
| Abstract (7) | 6 / 1 (AB4, merged) / 0 | 5 / 2 (AB4 merged; AB5) / 0 |
| Conclusions (26) | 25 / 1 (CO23, scope) / 0 | 24 / 2 (CO22; CO17, thin) / 0 |
| Figures (1) | 0 / 1 / 0 | 0 / 1 / 0 |
| Tables (1) | 1 / 0 / 0 | 0 / 1 / 0 |

---

## 3. Where each is wrong that the other isn't

### Run A

1. **C12.4 (§4.2) widens the scope of the curtailment risk.** A writes: "Natural-water cooling can create operational and financial risk from thermal-discharge limits, especially during extreme heat." The article limits that risk to "Data centers employing once-through or open-loop cooling from natural water bodies". The installations §4.2 actually describes use closed-loop heat exchangers, so A's version applies the risk to exactly the systems the author had left out of it. Scored A1 = 1, because the scope condition is lost. This is A's only substantive alteration I found, and B does not make it.

### Run B

1. **C8.3 (§3.2) states more than the author does about Colón.** B writes: "Colón illustrates acute local impacts and environmental injustice arising from rigid water allocation." The article says Colón "illustrates acute local impacts". Two sentences later, after generalizing beyond Mexico, it says only that "Such allocation failures raise fundamental environmental justice dimensions". B turns "raise… dimensions" into an asserted injustice and attaches it directly to the case. A1 = 1. A quotes the sentence verbatim (C10.4).
2. **C11.1 support (§4.3) drops a qualifier on Hainan's size.** B gives the Hainan installation "with 400–800 AI servers". The article says "with capacity for 400–800 AI servers". Losing "capacity" turns a capacity figure into what reads as a deployed count. A1 = 1. A keeps "capacity for" (C13.2).
3. **C9.2 support (§4.1) puts an uncited figure under a citation.** B merges the Luleå withdrawal (cited to Zhang, 2024) and the Lule River figure of 13.6 million MWh (uncited in the article) into one support item under Zhang. That makes Zhang the apparent source of the hydropower figure. A keeps them as two support items and leaves the Lule River figure uncited, as the article does.
4. **C4.2 (§2) slightly weakens the ISO wording.** B says the framework is "described here in relation to ISO 14046". The article says "formally standardized in ISO 14046". This is a minor softening; A keeps "formally standardized".

### Shared by both runs (not a difference)

- Both write that natural-water-body coupling "can eliminate" consumptive withdrawals, where the article states it as fact: the installations are coupled "via closed-loop heat exchangers, eliminating consumptive withdrawals".
- Both reduce AB2's "indirect water use in electricity generation" to "electricity generation".

### A3, strength of language

Both runs largely keep the author's hedges and certainty. Examples include:

- "Projections suggest… could"
- "Bloomberg… suggests"
- Natick's "suggesting economic or operational constraints"
- Espoo's "expected"
- "may yield indirect water savings"
- "would face analogous regulatory constraints"
- the strong closing claims ("severely limited", "inadequate", "irreversibly deepens")

Neither shifts systematically in one direction. A has one scope slip, which broadens a claim. B has one strengthening and two qualifiers dropped. Both are near the top of A3, and B a little less clean than A.

---

## 4. A5, detail and readability

- **Size and spread.** A has 25 steps and B has 21, at about 220 and 260 words of article per step. Both stay within the scale the prompt asks for and cover the article evenly.
- **Where A splits more.** The extra steps fall in §3 and §5, the article's densest parts:
  - §3's global-context paragraph and §3.1 are separate steps in A, one step in B.
  - The Colón case is its own step in A, merged into §3.2 in B.
  - §5.1 is three steps in A, two in B.
  - §5.2 and §5.3 are separate steps in A, one in B.
  - The §4 synthesis and the §5 opening are separate steps in A, one in B.
- **Merged claims in B.** B more often fuses separate claims into one: C7.4 (all of §3.1), C16.1 (the climate and biodiversity concession plus water governance's advantages), C11.3 (subsea impacts plus the <1 °C initial assessments), and C17.4. The prompt asks the runs to "keep distinct claims separate". B's merges stay accurate, but they make individual claims harder to cite.
- **Padding.** Neither run pads. A's extra claims are mostly distinct sentences that B folds together, not repetition. Where the article repeats itself (25,500 m³; the two-thirds figure; the 42% and >25% figures in §5.2; the §6.2 mechanisms), both runs note the repetition as a move instead of recording it again, as the prompt asks.
- **The `meaning` fields.** Both stay on the right side of the reading/judgment line. A's tend to say more about how strong the evidence is. Examples:
  - S12: the power-plant comparison is "an analogy… not a reported observation of such curtailment."
  - S21: the Virginia measure "remains a proposal."
  - S15: "planned capacity" is distinguished from operating examples.
  - S9: "built or planned", not operating.

  B's are accurate but more general.
- **Readability.** A reader could follow the article's argument from either run. With A they could also rebuild Table 1 and the §4.1 conclusion, which B doesn't allow.

---

## 5. Verdict

**Run A is the better close reading, by a modest margin.**

The reasons, by criterion:

- **A1, attribution fidelity.** A has one substantive alteration: the once-through scope in C12.4. B has three small ones: the Colón injustice claim strengthened, Hainan's "capacity" dropped, and the Lule River figure put under Zhang's citation. A also uses `verbatim` more often (13 quotes against 5), and every quote is exact. Where B paraphrases a sentence A quotes, B's paraphrase is the one that drifts (C8.3).
- **A2, coverage.** A fully catches Table 1, CO22 and AB5, where B is partial. B is ahead only on H3 ("policy gaps") and the once-through qualifier in CO23. Table 1 is one of the article's six claimed contributions (C5), and B leaves out two of its five columns.
- **A3, strength of language.** Close to even, with A slightly cleaner.
- **A4, mechanical checks.** Even: both pass every check.
- **A5, detail and readability.** A splits the dense sections more finely, keeps distinct claims separate more consistently, and its `meaning` fields track evidence status more closely. It does this without padding.

B is not a weak reading. It is accurate, compact, and faithful on most claims, and it gets the one qualifier A loses (once-through or open-loop). If length and cost had to be traded against quality, B gives up some table detail and some precision on individual claims. It does not give up anything structural.

## 6. Order check

- **Reading A first, then B.** A sets a high bar on Table 1 and §4. Reading B next, the gaps that stand out are the compressed table, the missing Nordic conclusion and the merged claims. B's correct once-through qualifier is a real point in its favor, but it doesn't outweigh those gaps. **Verdict: A.**
- **Reading B first, then A.** B reads as a clean, complete reading on its own terms. Coming to A next, A adds the table's example and trade-off columns, CO22, the four-technology list in the abstract, and more exact quotes. It also corrects B's three small alterations (capacity; "raise environmental justice dimensions"; the Lule River figure uncited). A's once-through slip stands out as A's one error, and it is roughly equal in size to any one of B's. **Verdict: A.**

**The verdict holds in both orders.** One limit on this check: both passes were made in this one session, so the second reading was not blind to the first.
