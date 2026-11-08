# Close-reading judgment

Document: **article.pdf** — Minnesota Statutes 2026 excerpt, 17 PDF pages (printed pages 18–34), from the incomplete 120B.117 continuation through visible 120B.125(a)(1).

Seed: **20261108**. Flatten `reading_path` in array order, then each step's `claims` in array order; number claims 1–280. Sample without replacement with Python `random.Random(20261108).sample(range(1, 281), 30)` and sort the selected IDs for presentation. Step and claim indices below are one-based. The reference list was used unchanged. No other judgment or discourse analysis was read; no outside source was consulted.

## A1. Attribution fidelity

**Provisions: 30/30 at 2 (100%); 0/30 at 1 (0%); 0/30 at 0 (0%).** All locations were found. This is a sample result, not a claim that every provision was independently scored under A1.

| Global claim | Step.claim | Location | Score | Evidence |
| --- | --- | --- | --- | --- |
| 1 | 1.1 | Opening fragment of 120B.117, PDF page 1 (printed page 18) | 2 | Consultation actor and inclusive council/community list retained. |
| 7 | 5.1 | 120B.119, subdivision 2 | 2 | CAREI definition reproduced exactly. |
| 8 | 6.1 | 120B.119, subdivision 2a | 2 | All cumulative facilitator qualifications retained. |
| 40 | 20.2 | 120B.119, subdivision 15 | 2 | Instructional characteristics and components reproduced exactly. |
| 42 | 21.1 | 120B.119, subdivision 16 | 2 | Three-cueing definition and MSV alias reproduced exactly. |
| 43 | 22.1 | 120B.119, subdivision 17 | 2 | Vocabulary definition reproduced exactly. |
| 44 | 22.2 | 120B.119, subdivision 17 | 2 | Communication assertion and inclusive examples reproduced exactly. |
| 50 | 23.5 | 120B.12, subdivision 1 | 2 | Strong encouragement remains encouragement. |
| 56 | 24.5 | 120B.12, subdivision 2, paragraph (a) | 2 | District, K–3 data fields and June 15 submission retained. |
| 95 | 33.2 | 120B.12, subdivision 3, paragraphs (c)-(d) | 2 | Approved materials remain strongly encouraged. |
| 104 | 35.5 | 120B.12, subdivision 4, paragraph (b) | 2 | Governing district shall and fifth staff-development outcome retained. |
| 115 | 37.10 | 120B.12, subdivision 4a, paragraph (a), opening and clauses (1)-(8) | 2 | Required data and all three student categories retained. |
| 135 | 43.1 | 120B.12, subdivision 5 | 2 | Commissioner, multiple tools and both purposes retained. |
| 153 | 46.4 | 120B.121, paragraph (a) | 2 | Provider duty, daily environment and open materials list retained. |
| 168 | 49.1 | 120B.122, subdivision 2 | 2 | Four credential alternatives and minimum three-year experience retained. |
| 172 | 51.3 | 120B.123, subdivision 1 | 2 | 2024–2025 restriction applies to district staff and external partners. |
| 192 | 59.1 | 120B.123, subdivision 5, paragraph (f) | 2 | School years, agreement, 5-1/2 hours and same-day condition retained; secondary limitation follows in claim 194. |
| 198 | 61.3 | 120B.123, subdivision 5a, paragraph (a) | 2 | Tier 1 second-renewal threshold reproduced exactly. |
| 201 | 62.1 | 120B.123, subdivision 5a, paragraph (b) | 2 | Tier 2 cohort, July 1, 2027 date and first-renewal condition reproduced exactly. |
| 205 | 63.2 | 120B.123, subdivision 5a, paragraph (c) | 2 | Progress-based protection against Tier 3 denial reproduced exactly. |
| 207 | 65.1 | 120B.123, subdivision 5a, paragraph (e) | 2 | Leave/disability conditions and extension-cost protection retained. |
| 218 | 67.7 | 120B.123, subdivision 7, paragraphs (a)-(e) | 2 | Department template duty and full cross-reference reproduced exactly. |
| 222 | 68.4 | 120B.123, subdivision 7, paragraphs (f)-(g) | 2 | Two review dimensions and department notice duty retained. |
| 231 | 70.5 | 120B.124, subdivision 1, paragraph (a), opening and clauses (1)-(6) | 2 | No requirement to use an approved curriculum. |
| 235 | 70.9 | 120B.124, subdivision 1, paragraph (a), opening and clauses (1)-(6) | 2 | Provider-selection exemption and section number reproduced exactly. |
| 240 | 70.14 | 120B.124, subdivision 1, paragraph (a), opening and clauses (1)-(6) | 2 | Joint actors and guidance on both evidence-based and other practices retained. |
| 251 | 73.4 | 120B.124, subdivision 2 | 2 | Required rubric and culturally responsive addition retained. |
| 255 | 74.2 | 120B.124, subdivision 3 | 2 | Joint duty and accessible professional-development content retained. |
| 256 | 74.3 | 120B.124, subdivision 3 | 2 | Joint duty to provide MTSS adoption guidance retained. |
| 264 | 75.7 | 120B.124, subdivision 4 | 2 | Joint actors, no-cost rule and eligible unlicensed staff retained. |

**Support items attached to the sample: 5/5 at 2 (100%); 0 at 1; 0 at 0.** Claim 40's support is the exact final sentence of 120B.119 subd. 15, supplying the stated science-of-reading consistency and literacy purpose. The other four support items identify printed legal cross-references: claim 192, section 120A.41 and section 120A.05, subdivisions 9 and 13; claim 201, section 122A.182; claim 218, section 120B.12, subdivision 4a; and claim 235, section 16C.08. These are accurate paraphrased descriptions of references, expressly distinguished from empirical justification. Their explanatory boilerplate belongs more naturally in moves, but does not invent a source or substantive basis. All sampled `reference_entry` values are null, appropriately.

## A2. Coverage — counts, not a score

The reference has **195 P entries**. Across those entries, **193 are caught with their content; 2 are partially caught; none is wholly missed**. Repetition identified in moves counts as caught, as the reading instructions require: for example P128 (progress monitoring) appears in step 52 rather than as a duplicate claim, and the repeated cost protections in P151–P153 are noted in steps 62–64.

The following type counts use reference P entries, once per applicable type, rather than counting every sentence or every modal separately. Types overlap and do not sum to 195. “Without content” means recognition only; “partial” means some actual content is preserved. Category-specific coverage is credited where the missing portion concerns a different type. For named sources, units are the reference's nine section-level source groups and eight separately listed history entries.

| Reference type | Caught with relevant content | Caught without content | Partial content | Wholly missed |
| --- | ---: | ---: | ---: | ---: |
| Definitions, including definition-scope entry | 20 | 0 | 0 | 0 |
| Findings, intent and purpose | 16 | 0 | 0 | 0 |
| Requirements, including governed list components | 162 | 0 | 1 | 0 |
| Prohibitions and constraints | 11 | 0 | 0 | 0 |
| Permissions, should and encouragements | 28 | 0 | 0 | 0 |
| Assigned duties and discretionary authority | 169 | 0 | 1 | 0 |
| Criteria, standards and list components | 169 | 0 | 1 | 0 |
| Consequences and accountability | 67 | 0 | 0 | 0 |
| Exceptions and alternatives | 26 | 0 | 0 | 0 |
| Funding and timing | 52 | 0 | 0 | 0 |
| Named sources and printed histories (group units) | 9 | 8 | 0 | 0 |
| Marked amendments | 0 (none supplied) | 0 | 0 | 0 |
| Express repeal/status notice | 1 | 0 | 0 | 0 |

The omissions are limited but should remain visible:

- **P001, opening 120B.117 fragment, PDF p. 1:** step 1 preserves all three complete consultation, reporting and publication duties and acknowledges the advisory-council fragment. It omits the visible subject “of racially and ethnically diverse teachers” and the question of the council's composition and charge if established. This is partial context, not an omitted complete council-establishment mandate; the PDF does not supply one.
- **P059, 120B.12 subd. 4a(a), PDF p. 7:** steps 37–38 retain the plan's goals, annual June 15 update/submission and all fourteen components, but omit the express requirement that the plan be consistent with the Read Act. This produces the partial requirement/authority/criterion entries above; it is one missing matter, not three different omissions.
- **Eight printed history entries**, for 120B.117, .118, .119, .12, .121, .122, .123 and .124: the reading recognizes history lines as provenance in its plan and step 1, but does not transcribe their enactment citations. These are counted as recognized without content, separately from operative requirements. The express repeal citation in 120B.124 subd. 6 is preserved.

Counts are deliberately tied to the reference's paragraph/list units. Requirements include inherited duties in numbered components; authority includes those duties and discretionary powers. Criteria include definitions, eligibility/quality conditions and list components. Funding/timing counts explicit dates, recurring or conditional durations, deadlines and cost provisions; grade and age eligibility is also checked under criteria. In particular, the fourteen local-plan components, seven legislative-summary components, seven 2026 training cohorts, three 2027 cohorts, ten joint partnership tasks, four support tasks and both unlicensed training categories are all present with content.

The reading ends where the document ends, after 120B.125(a)(1), and explicitly identifies the missing continuation. No confirmed provision was found beyond the reference list. The images show a consolidated statute without strikeout/underline amendments; neither reading nor reference reconstructs deleted text.

## A3. Strength of language — 2/2

The recorded provisions preserve mandatory duties, permissions and encouragements without a directional shift. MTSS adoption remains encouraged and its suggested processes retain “should” (step 23); personal plans remain strongly encouraged while their stated conditions and IEP exception survive (step 32). Retention is conditional and cannot rest solely on literacy delay. Evidence-based interventions are mandatory from 2026–2027, while approved intervention materials remain encouraged (step 33). Approved curricula and intervention models are expressly optional (steps 70–71).

Open lists retain their openness: intervention options (step 31), advisory membership (step 44), and illustrative transition-plan skills (step 78). Minimum curriculum/program counts remain minima. Dual-language contingencies, parent/teacher opt-out conditions, training cohorts and deadlines, distinct Tier 1/Tier 2 renewal thresholds, protected delays, and the narrower secondary-school hours reduction all survive. The isolated unrecorded plan-consistency requirement is reported under A2; it does not establish a pattern of modal or conditional rewriting in recorded provisions.

## A4. Mechanical checks — pass/fail counts

Python checks used `article.txt`, with whitespace normalized. For uninterrupted quotation checks, publication headers/footers and page markers were removed while retaining body text and punctuation. All 17 supplied page images were also inspected, including the six quotations crossing page boundaries.

| Check and counting unit | Pass | Fail |
| --- | ---: | ---: |
| Verbatim claim fields | 189 | 0 |
| Verbatim support fields | 3 | 0 |
| Total verbatim fields | 192 | 0 |
| Numeric occurrences in claim/support text (55 distinct numeric tokens) | 333 | 0 |
| `citation_text` fields (28 distinct strings) | 38 | 0 |

The numeric count includes section/subdivision references, list numerals, grades, dates, years, tiers and the 5-1/2-hour quantity. Numbers spelled out in quoted text are covered by the verbatim checks and were also assessed in context, including the three-year experience threshold, minimum five curricula/three programs and eight-hour training ceiling. This occurrence check establishes presence; A1/A3 address whether numbers are attached to the right actors and conditions. Named bodies in the recorded provisions, including CAREI's full institutional name, the Indian Affairs Council and the Professional Educator Licensing and Standards Board, match the document. No completed or fabricated bibliographic entry appears.

A whitespace-only whole-file search initially missed global claims **38, 54, 89, 105, 193 and 221** because page furniture interrupts their sentences. All six match after its removal and agree with the page images; these are extraction artifacts, not failures. No table, chart or image-only substantive value requires a separate paraphrase check. The images contain ordinary statutory text, not amendment markup.

## A5. Detail and readability — description only

There are **78 steps and 280 claims**, with 40 support items. Distribution is: opening 120B.117 fragment 1 step; 120B.118 2; 120B.119 19; 120B.12 23; 120B.121 2; 120B.122 3; 120B.123 19; 120B.124 8; and 120B.125 1. This follows statutory order and allocates more steps to definitions, district duties and implementation. Long enumerations are sometimes bundled—particularly step 70's fourteen claims—so list items take more work to locate than the individual definitions, but their content remains available. Subdivision/paragraph locations allow a reader to follow the statutory sequence without reconstructing it from scattered themes.

Moves and meanings generally explain how definitions lead to district duties, reporting, staffing and review. Repeated legal-cross-reference boilerplate in support adds bulk, and a few substantial steps could be split further; neither issue substitutes interpretation for provisions. The incomplete boundaries are clearly marked. A reader can follow the document's operative structure, exceptions and distribution of responsibility from this reading alone, subject to the small coverage omissions above.

## Assessment for the researcher

This is a faithful and unusually comprehensive reading of the supplied excerpt. Its sampled attribution, exact quotations, dates, cross-references, exceptions and modal distinctions are strong; it also preserves awkward printed timing and the Tier 3 completion/non-denial tension without silently resolving them. The principal limitations are the lost opening-fragment context, the omitted explicit local-plan consistency requirement, absent detailed history citations, and some bulky cross-reference commentary. These are bounded coverage and presentation issues rather than evidence of invented provisions or systematically altered force. Acceptance remains the researcher's decision.
