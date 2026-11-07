# Legislation codebook pilot report

The model pass is complete for ten selected passages from two official historical sources. The pilot supports trying the five CDA dimensions, with tighter rules for teacher positioning, presupposition, and silencing. Independent researcher coding and adjudication remain pending; no accuracy or agreement result is claimed.

## What was analyzed

The sources are Arizona's 2022 Chapter 120 (HB2026), selected passages from sections 1 and 2, and Minnesota Statutes 2023 section 120B.12, selected passages from subdivisions 1 and 2. One is an enacted amending law and the other a historical consolidated section. They are not equivalent whole-state policy records. No interstate prevalence comparison follows from them.

Both official pages were inspected through web tools on November 7, 2026. Full-source download was declined; the saved records contain short excerpts and URLs, not immutable source snapshots. The statutory versions are identified by the official page headings, not inferred from the codebook. Exact enactment dates were not established and remain null in sources.json. Arizona's amending HTML has typography that is not reproduced in the text excerpts; the pilot makes no added-versus-deleted wording claim. Check source formatting before a final legal-text extraction.

Selection was purposive, informed by the preceding codebook review: include regulation, support, an exemption, multilingual provisions, and ambiguous wording. The assistant had already seen the codebook's original examples. This is a code-boundary exercise, not held-out validation, a full close-reading evaluation, or an independent model judgment. The original examples supplied no quotations for these records; the official pages supplied the excerpts.

## What the model pass found

| Issue | Pilot evidence | Consequence for coding |
| --- | --- | --- |
| Regulation and support coexist | AZ-02 conditions a specified funding stream on approval; AZ-03 provides specialist support; AZ-04 offers a conditional route recognizing existing teacher competence. | Record the mechanisms separately. Do not infer that an entire state positions teachers in only one way. |
| Training does not settle a deficit interpretation | MN-03 requires districts to provide approved training and permits deadline extensions. | SUB-5 and SUB-7 have direct textual support; teacher-deficit and professional-development interpretations remain uncertain for that passage. |
| Five components do not prove an NRP citation | MN-02 includes the five components and oral language without naming NRP in that passage. | LEX-1 can apply under the draft definition while INT-1 does not. |
| Multilingual and oral-language provisions challenge an absence expectation | MN-01, MN-02, and MN-04 explicitly address these topics. | Preserve counterexamples as separate outcomes. Their presence does not by itself establish implementation adequacy or national uniqueness. |
| Goals and presuppositions require different evidence | MN-01 seeks universal grade-level reading while also recognizing individualized goals. | PRE-1 remains uncertain; do not recast an aspiration as a guaranteed outcome. |
| Existing lexical categories leave a gap | AZ-01 names science of reading and includes phonics without defining it through the draft's named frameworks. | Consider a new lexical code for naming SoR without defining it. Do not force it into LEX-1, LEX-2, or LEX-3. |
| A local missing definition may be elsewhere | AZ-05 uses evidence-based wording in a cross-referencing legal scheme. | LEX-4 remains uncertain within this boundary; do not claim a statewide definitional vacuum. |

No positive silencing finding is established by this small set. No passage establishes interstate borrowing, named research authority, or unanimous scientific consensus. Those are limits of the selected evidence, not findings that the full laws lack those patterns.

## Provisional codebook changes

The pilot_rules.md file preserves all 33 draft code definitions without the original coded examples, and adds operational overrides. The original codebook receives an evidence-status notice; its substantive content remains preserved for review.

Before expanding coding, researcher review should resolve these changes:

1. Split SUB-1's teacher regulation from teacher deficiency, and SUB-7's state assistance from state arbitration. Each can coexist with the other.
2. Split FOS-4 into background knowledge and comprehension, and FOS-7 into oral language and writing. A counterexample to one half does not resolve the other.
3. Require an explicit textual warrant before treating a goal, a mandate, or evidence-based language as a PRE code.
4. Add a lexical category for SoR named without a framework definition; test it against LEX-4 rather than treating the two as interchangeable.
5. Require an absence boundary and contextual search before a silencing claim. Keep statutory cross-references separate from citations of research or advocacy authority.

These changes arose during the model pass. They are not presented as preregistered or human-approved decisions. The original model records remain available for comparison after human coding.

## Researcher handoff

Give the researcher only pilot_rules.md and human_worksheet.md, with access to the linked primary texts. Save their code-level decisions and any prior exposure before opening the model results. Then use comparison.md to document disagreements, adopted decisions, and revisions. Do not send this report first if an independent initial pass is desired.

No human coding, expert consultation, saturation assessment, reliability estimate, or model accuracy measurement has occurred in this pilot. The next required contribution is the researcher's independent reading of the ten passages, not another model's approval.
