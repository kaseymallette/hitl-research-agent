# Close readings, head to head: run A vs run B

**Article:** Barnett-Itzhaki, "The water footprint of artificial intelligence: Emerging solutions and governance imperatives," *Water Research* 299 (2026) 125866.

**ids:** A `56377890-9bfb-469c-8786-ece6a6ea5348` · B `182e2233-37de-4fde-b637-d787f5cc0fef`

**Read for this session:** `RUBRIC.md`, `prompts/close-reading.md`, `article.pdf` (text extracted with PyMuPDF and checked against the page layout), `judgments/claims_reference.md`, `runs/A/analysis.json`, `runs/B/analysis.json`. I did not open the other judgments or any argument evaluation.

**How I compared them:** Both readings are short enough that I checked every claim and support item against the article, so the A1 notes below cover every item, not a seeded sample of 30. A4 checks were scripted: whitespace, soft hyphens and quotation marks were normalized, then each verbatim text, number and `reference_entry` was matched against the extracted text. I confirmed every reported failure by hand.

## At a glance

| | Run A | Run B |
|---|---|---|
| Steps | 23 | 26 |
| Claims / support items | 133 / 75 | 109 / 46 |
| Claims marked verbatim | 11, all exact | 17, 16 exact, **1 not the author's wording** |
| Numbers found in article text | 97 / 97 | 101 / 101 |
| `reference_entry` matching the reference list | 65 / 66 (**1 drops an author**) | 64 / 64 |
| Claims scoring 0 under A1 | 0 | 1 |
| Claims scoring 1 under A1 | 1 | 3 |
| Support items below 2 | 2 (strengthening or the run's own gloss) | 0 |
| Graphical abstract (F1) read | no | no |

## What each caught that the other missed (against `claims_reference.md`)

Both readings cover all five contribution and abstract statements, Table 1 row by row with all three footnotes, and every section conclusion CO1–CO26. Both list the §4.1–4.5 trade-offs and scalability limits. Neither reads the **graphical abstract (F1)**. Both record the five research priorities (CO17), but neither records the fourth, ecological impact monitoring, as a claim. Each mentions it only in its `meaning` field.

**Run A caught and run B missed:**
- **H3, the highlight that deployment is "limited by policy gaps."** A's C4 keeps "policy gaps." B's C5 follows the abstract's wording ("deployment remains limited"), so the highlight's reason is missing.
- **CO12's EIA analogy.** A records that the proposed water impact assessments are "analogous to Environmental Impact Assessment (EIA)" (support to C101). B's C78 lists the mechanisms without the analogy.
- **The detail behind digital water sobriety's first dimension (§5.1).** A's C95 keeps "training runs consume hundreds of thousands of liters in water-stressed regions for limited social benefit." B's C73 reduces it to "urgent because public awareness is limited."
- Smaller details A keeps that B doesn't: Luleå is "south of the Arctic Circle," and each §4.5 heat-recovery example is its own claim, where B puts all four into one support item.

**Run B caught and run A missed:**
- **The condition on the 2027 projection (§1).** B's C9 support says the 4.2–6.6 billion m³ figure is "conditional on continued growth in AI use," following the article's "If this increase in AI use continues." B also keeps the abstract's hedge verbatim ("Projections suggest… could reach…"). A keeps "could" but drops both the condition and "Projections suggest."
- **More of the author's key sentences as verbatim:** the scope statement (C11), "does not perform an independent water footprint calculation" (C19), the resource-justice question (C102), and the governance-failure sentence (C104). A paraphrases each one faithfully, so A gives up exact wording, not content.
- B's `meaning` points out that §4.4's heading puts "Waterless" in quotation marks.

On balance A catches a little more of what the reference list asks for (H3 and the EIA part of CO12). B catches one qualifier A drops, the condition on the headline projection.

## Where each is wrong and the other isn't

**Run A:**
1. **A misplaced step and a duplicate claim.** A's step 5 ("Section 3 opening, before Table 1") records C25: the peer-reviewed stream was "identified through Web of Science and Google Scholar." That is a second copy of C18 from §2. The step's location doesn't contain the claim, and the step's moves describe it as completing a "displaced description of the review." Step 4's `meaning` also says "the supplied text begins mid-sentence." Neither is true of the article: §2 is continuous in the PDF. (B makes a milder version of this mistake; see "Both wrong" below.) I score C25 as **1**: the content is supported, but it is attached to the wrong location.
2. **A reference entry with an author missing.** The Pfister et al. 2017 entry (step 4) goes from "Scherer, L." straight to "Manzardo, A." and leaves out "Döll, P." B's entry includes him.
3. **A support item that strengthens the author.** C99's support says competition with local water uses is "decisive." The article says such uses are "difficult to justify when it competes with agricultural or domestic water needs." Score **1**.
4. **The run's own commentary in support fields.** About a dozen support items describe the run's reading of how the argument links up rather than evidence the author gives. Examples: C17 ("The author draws this conclusion from…"), C46, C54, C65 ("This is an inference from the power-plant analogy and the interaction between warm source water, discharge thresholds, and cooling demand"), C69, C90, C114. Most of them accurately describe the author's own linkage, so I counted only C65 (score **1**, for the added mechanism) and C99 as faults. Still, the pattern puts the run's voice in a field that belongs to the author.

**Run B:**
1. **A "verbatim" quote that isn't verbatim.** C72 reads "Digital water sobriety challenges the assumption that AI expansion should proceed without considering water constraints." The article reads "Digital water sobriety, *analogous to frameworks in climate and energy policy*, challenges…". The phrase is cut with no ellipsis, and it carries the framework's stated analogy. Under A1 that is a **0**. A records the same sentence as paraphrased (C94) and doesn't misattribute it.
2. **A scope widened at the claim level.** C51 says "Natural-water-body cooling can expose data centers to forced curtailment." The article confines the curtailment risk to data centers "employing once-through or open-loop cooling," and §4.2 opens by describing closed-loop systems. B's support item states the restriction correctly, but the claim itself is broader than what the author said. Score **1**. A's C64 keeps the restriction in the claim.
3. **Two mild shifts, each scored 1.** C53 extends "eliminating freshwater consumption" from the Hainan installation to subsea facilities in general. C106 rewrites the closing question ("whether the society possesses the political will") as an assertion that implementation "requires political will." A keeps that closing sentence verbatim (C130).

**Both wrong:**
- Both describe Table 1 as read from a "retained image." It is printed as text. Both mark their table readings `paraphrased`, so this costs no points.
- Both report an interrupted methods passage that the PDF doesn't have, which suggests a quirk in the text they were given. B absorbs it into one correctly placed §2 step. A builds a separate step around it (see A, item 1).
- Both cite "(Yanez-Barnuevo, 2025˜ )" and carry stray "¨" characters into reference entries. These are text-extraction artifacts that appear identically in both.

## Grounds by criterion

- **A1, attribution fidelity:** A has no 0s, one claim at 1 (C25) and two support items at 1. B has one 0 (the C72 verbatim) and three claims at 1. Both are highly faithful; every other item in each run scores 2. **Edge: A**, because the rubric keeps a 0 apart from a 1, and only B has a 0.
- **A2, coverage:** Close to even. Both miss F1 and leave the ecological-monitoring priority out of their claims. A also catches H3 and CO12's EIA analogy, and keeps more §5.1 and §4 detail. **Edge: A, slight.**
- **A3, strength of language:** Both mostly 2. A drops the condition on the 2027 projection and strengthens one support item ("decisive"). B widens the curtailment scope and hardens the closing question. Each slips in about two places, in opposite directions, so neither run is systematically shifted. **Even.**
- **A4, mechanical:** All numbers check out in both. A has 11/11 verbatim and 65/66 references. B has 16/17 verbatim and 64/64 references. **Even**: one failure each.
- **A5, detail and readability:** B's 26 steps follow the article's natural breaks more closely. §3's global-context paragraph, §3.1, and the two halves of §3.2 each get their own step, and nothing is duplicated. A runs to 133 claims with finer granularity, which helps a reader find individual figures, but it has the spurious step 5 and a dozen support items padded with the run's own commentary. A reader could follow the argument from either. **Edge: B.**

## Verdict

**Run A is better, narrowly.** The deciding criterion is A1: A has no claim the author didn't make or didn't word that way, while B has one misquoted "verbatim" sentence that drops the author's stated analogy, plus one claim with a widened scope. A also has a small coverage edge (H3, the EIA analogy, more decisive detail). B's advantages are real but carry less weight: a cleaner step structure, preserving the condition on the headline projection, and more exact quotation of key sentences. Both readings are strong, and the gap between them is small compared with their quality.

## Order check

- **A first, then B:** After A, B's C72 misquote and its broadened C51 stand out as faults A doesn't have. B's cleaner structure and its kept projection condition register as advantages, but they don't outweigh a 0 under A1. **A.**
- **B first, then A:** After B, A's spurious step 5, the missing reference author, and the commentary in its support fields stand out, and B looks tidier. But A's flaws score at most 1 under A1 or count as A4 items, and they're offset by B's own A4 failure (the verbatim). A's H3 and EIA coverage still isn't in B. **A, by a smaller margin.**

**The verdict held in both orders:** A, narrowly. Because the margin is thin, a researcher choosing a configuration should treat these two as close to equivalent on this article, with A slightly more faithful and B slightly better structured.
