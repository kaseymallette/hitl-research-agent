## Phase 1 — Research Data Model

### 1. Draft Phase 1 Build Plan 

**Prompt:**
Can you write the build plan for Phase 1?

**Clarifying Questions and Decisions:**
Before drafting the plan, Claude asked four architectural questions:

1. **How should the schema be composed — one flat `SourceAnalysis` model, or separate sub-models (`Claim`, `Evidence`, `Assumption`, `Limitation`, `Methodology`, `Provenance`) nested inside a top-level model?**
   **Decision:** Composed sub-models.

2. **How should the author-stated vs. model-inferred distinction be represented for assumptions and limitations?**
   **Decision:** Discriminator field.

3. **Should claims, evidence, and analyses receive stable identifiers, such as UUID fields, during Phase 1, even though nothing consumes them until synthesis or knowledge-base development?**
   **Decision:** Add IDs during Phase 1.

4. **How strict should field validation be during Phase 1, including non-empty claim and evidence text and minimum list lengths for central claims?**
   **Decision:** Use strict validation during Phase 1.

**Response:**
Claude drafted the proposed Phase 1 Research Data Model without modifying `docs/BUILD_PLAN.md`. The proposal used composed Pydantic sub-models, discriminator fields for author-stated versus model-inferred assumptions and limitations, UUIDs for analyses, claims, and evidence, and strict validation of required fields and lists. It also proposed the module layout, implementation tasks, tests, acceptance criteria, and four remaining decisions concerning required claim evidence, source-type values, IDs for assumptions and limitations, and file organization.      

**Concern:** The Phase 0 approval boundary may be too broad for planning. It successfully prevents unapproved repository changes, but it may also cause Claude to avoid making provisional architectural recommendations, ask for approval on minor design details, or repeatedly restate the boundary.

### 2. Clarify Planning and Implementation Boundaries

**Prompt:**
Before we revise the Phase 1 draft, I want to clarify the approval boundary. Continue to make no repository changes without my explicit approval. However, during planning and review, you may make provisional architectural recommendations, develop a complete proposed design, and resolve minor design details when you explain your reasoning. A recommendation in a draft is not an approved implementation decision. You do not need to repeatedly restate the no-write boundary. Ask me questions when the answer would materially change the architecture. Otherwise, give me your recommended choice, explain the tradeoff, and flag it for review. For now, do not modify any files. Review the proposed Phase 1 schema for semantic ambiguities or missing distinctions, especially how claims are grounded versus supported, where source-stated content must be separated from model inference, whether every permitted source type has a methodology, and how IDs would be generated.

**Clarifying Questions and Decisions:**

1. **How should `Evidence` distinguish grounding that is verbatim and directly checkable from softer support involving paraphrase or indirect inference?**
   **Decision:** Add both `quote_type` and `support_strength` fields.

2. **Should the source-stated versus model-inferred discriminator extend to `central_claims`, `proposed_solutions`, and `open_questions`, rather than applying only to assumptions and limitations?**
   **Decision:** Extend the discriminator to all listed categories.

**Response:**
Claude confirmed that proposed architectural recommendations would remain provisional and that repository changes would still require explicit approval. It identified two gaps in the original schema: `Evidence` did not distinguish source grounding from different degrees of claim support, and the source-stated versus model-inferred distinction was not enforced across all relevant categories. After receiving the decisions, Claude updated `Evidence` with `quote_type` and `support_strength` fields. It introduced a shared `InterpretedStatement` base containing the statement text and its source classification, then created distinct `Claim`, `Assumption`, `Limitation`, `ProposedSolution`, and `OpenQuestion` models.Claude also recommended making `methodology` optional because some permitted source types may not describe a methodology. It recommended generating UUID4 identifiers automatically through Pydantic for `SourceAnalysis`, `Claim`, and `Evidence`, while noting that rerunning an analysis would generate new identifiers and that revision tracking may need to be addressed in Phase 4.

### 3. Extend the Discriminator to Research Problem

**Prompt:** Include `research_problem` in the discriminator coverage as an `InterpretedStatement`. In `Evidence`, rename `quote_type` to `evidence_form`, with the values `"verbatim"` and `"paraphrased"`. Rename `support_strength` to `support_relationship`, because `"direct"`, `"partial"`, and `"contextual"` describe how the evidence relates to the claim rather than its methodological strength. Use the values `"claim_grounding"`, `"direct_support"`, `"partial_support"`, and `"contextual_support"`. Keep the optional methodology and automatically generated UUID4 identifiers as proposed.

**Response:**
Claude applied the requested schema changes by extending `InterpretedStatement` to `research_problem`, renaming the evidence fields, retaining optional methodology and generated UUIDs, and consolidating the four statement subclasses into one module.

**Issue:**
Claude interpreted `claim_grounding` as the strongest value on an ordered support scale. Grounding only establishes that the source made the claim; it does not measure evidentiary support. The field therefore needs to be renamed `relationship_to_claim`, with the values documented as distinct relationships rather than a strongest-to-weakest progression.

### 4. Clarify Evidence Relationship Semantics

**Prompt:** Do not treat `claim_grounding` as the strongest value on an ordered support scale. It is categorically different from evidentiary support: it establishes that the source makes the claim, while the other values describe how source material supports that claim.

Rename `support_relationship` to `relationship_to_claim`, with these meanings:

* `"claim_grounding"`: establishes that the claim is stated or made by the source
* `"direct_support"`: directly supports the claim
* `"partial_support"`: supports only part of the claim
* `"contextual_support"`: provides relevant context without directly supporting the claim

These four values should not be documented as a single progression from strongest to weakest. Update the proposed schema and field documentation only. Do not write the finalized Phase 1 build plan yet.

**Response:**
Claude corrected the evidence model by renaming `support_relationship` to `relationship_to_claim` and documenting the four permitted relationships. It clarified that `claim_grounding` establishes attribution, while `direct_support`, `partial_support`, and `contextual_support` describe different ways source material may support a claim. The values are no longer treated as a single ordered strength scale. No files were modified.

**Outcome:**
The semantic distinction was corrected as requested.

### 5. Clarify Statement Origin and Field Documentation

**Prompt:** Rename `InterpretedStatement.source` to `statement_origin`, retaining the values `"author_stated"` and `"model_inferred"`.

Treat this as a categorical attribution field. Although we previously called it a discriminator, do not implement it as a Pydantic discriminated union unless the model structure actually requires one.

Encode semantic field documentation using `Field(description=...)` so the explanations appear in Pydantic’s generated JSON Schema. Apply this to `statement_origin`, `evidence_form`, and `relationship_to_claim`; do not rely on standalone string literals as field documentation.

Update the proposed schema only. Do not write the finalized Phase 1 build plan yet.

**Response:**
Claude renamed `InterpretedStatement.source` to `statement_origin` and confirmed that it will remain a categorical `Literal` field rather than a Pydantic discriminated union. It moved the semantic documentation for `statement_origin`, `evidence_form`, and `relationship_to_claim` into `Field(description=...)` so the descriptions will appear in the generated JSON Schema. No files were modified.

**Outcome:**
The naming and field-documentation concerns were resolved as requested.

### 6. Define Strict Schema Validation

**Prompt:** Before finalizing Phase 1, revise the proposed validation rules and tests.

Use a reusable constrained string type that strips surrounding whitespace and rejects empty or whitespace-only values. Apply it to required text fields and to optional text fields whenever they are provided.

Configure the models to reject unexpected fields, and use `Field(default_factory=list)` for list defaults. Require at least one `central_claim` and at least one `Evidence` item per `Claim`. Require `retrieved_at` to contain timezone information.

Add cross-field validation for claims and evidence:

* An `"author_stated"` claim must include at least one Evidence item whose `relationship_to_claim` is `"claim_grounding"`.
* A `"model_inferred"` claim must not contain `"claim_grounding"` evidence.
* Evidence marked `"claim_grounding"` must use the `"verbatim"` evidence form.

Add tests covering these rules, including whitespace-only strings, unexpected fields, independent list defaults, timezone-naive datetimes, and invalid combinations of statement origin, evidence form, and relationship.

Update the proposed schema, validation rules, and tests only. Do not modify any files or write the finalized Phase 1 build plan yet.

**Response:**
Claude defined a reusable `NonEmptyStr` type that strips whitespace and rejects empty values, plus a shared `ResearchBaseModel` that forbids unexpected fields. It added timezone-aware retrieval timestamps, safe list factories, required non-empty claim and evidence lists, and cross-field validators enforcing consistency among statement origin, evidence form, and relationship to the claim. Claude also proposed tests for whitespace handling, unexpected fields, independent list defaults, timezone validation, invalid evidence combinations, and a valid author-stated claim as a positive control. No files were modified.

**Outcome:**
The strict-validation requirements were implemented correctly in the proposed schema and tests.

### 7. Complete Source Provenance

**Prompt:** Revise `Provenance` before finalizing the Phase 1 plan.

Add `source_id: UUID = Field(default_factory=uuid4)`. Document that `source_id` identifies the underlying source and should be reused when the same source is reanalyzed, while `SourceAnalysis.id` identifies a particular analysis result.

Add `"research_institute_report"` and `"technical_document"` to `source_type` so the enum matches the project’s planned source pool.

Add optional `doi: NonEmptyStr | None = None` and `publisher: NonEmptyStr | None = None` fields. Keep `publication_date` and `url` optional.

Keep `retrieved_at` as a required `AwareDatetime`, but document it as application-supplied metadata recording the actual retrieval event rather than model-generated content.

Use `Field(description=...)` for fields whose ownership or meaning requires explanation. Update the proposed `Provenance` schema and related tests only. Do not modify any files or write the finalized Phase 1 build plan yet.

**Response:**
Claude added a stable `source_id` distinct from each `SourceAnalysis.id`, expanded the source categories to include research-institute reports and technical documents, added optional DOI and publisher metadata, and documented `retrieved_at` as application-supplied rather than model-generated. It also added tests covering ID creation and reuse, the new source types, and validation of the optional provenance fields.

**Outcome:**
The source identity and provenance requirements were resolved. One source-type gap remains for official government policy documents that are not reports.

### 8. Add Government Policy Source Type

**Prompt:** Add `"government_policy"` to `Provenance.source_type` for official government policy, standards, frameworks, and guidance documents that are not accurately classified as government reports.

Add a test confirming that `"government_policy"` is accepted. Update the proposed `Provenance` schema and tests only. Do not modify any files or write the finalized Phase 1 build plan yet.

**Response:**
Claude added `"government_policy"` to `Provenance.source_type` and distinguished it from `"government_report"` as covering official policies, standards, frameworks, and guidance documents. It incorporated the new value into the existing source-type acceptance test. No files were modified.

**Outcome:**
The remaining source-category gap was resolved.

### 9. Structure Methodology for Comparison

**Prompt:** Revise the proposed `Methodology` model while keeping `SourceAnalysis.methodology` optional.

Retain the required `summary: NonEmptyStr`, but replace the vague `approach` field with:

* `study_design: NonEmptyStr | None = None`
* `data_sources: list[NonEmptyStr] = Field(default_factory=list)`
* `sample_or_scope: NonEmptyStr | None = None`
* `analysis_methods: list[NonEmptyStr] = Field(default_factory=list)`

Add `statement_origin` with the same `"author_stated"` and `"model_inferred"` values and field description used for other interpretive content. This should indicate whether the methodology is described by the source or reconstructed by the model.

Do not introduce a closed methodology-type enum in Phase 1. Add tests confirming that methodology may be absent, that a provided methodology requires a non-empty summary and valid statement origin, and that its list defaults are independent.

Update the proposed `Methodology` schema and related tests only. Do not modify any files or write the finalized Phase 1 build plan yet.

**Response:**
Claude expanded `Methodology` with structured fields for study design, data sources, sample or scope, and analysis methods while keeping the model optional within `SourceAnalysis`. It added `statement_origin` and extracted its shared field description into a reusable constant. It also proposed tests covering absent methodology, required summary and origin values, independent list defaults, and complete model construction.

**Outcome:**
The methodology structure and validation requirements were resolved.

### 10. Finalize the SourceAnalysis Structure

**Prompt:** Make two final revisions to the proposed `SourceAnalysis` schema.

Add `ResearchProblem` as a named subclass of `InterpretedStatement`, alongside `Assumption`, `Limitation`, `ProposedSolution`, and `OpenQuestion`. Change `SourceAnalysis.research_problem` from `InterpretedStatement` to `ResearchProblem` so the category remains distinct during type checking.

Add `analyzed_at: AwareDatetime` to `SourceAnalysis`. It should be generated by the application when the analysis result is constructed, not produced by the LLM. Document that it records the creation time of this specific analysis result, while `Provenance.retrieved_at` records when the underlying source was retrieved.

Add tests confirming that `analyzed_at` is timezone-aware and that a complete `SourceAnalysis` constructs and round-trips successfully with `ResearchProblem`.

Do not add revision links, review status, evaluation results, or schema-version fields in Phase 1; those belong to later phases. Update the proposed schema and tests only. Do not modify any files or write the finalized Phase 1 build plan yet.

**Response:**
Claude added a distinct `ResearchProblem` subclass and updated `SourceAnalysis.research_problem` to use it. It added an application-generated, timezone-aware `analyzed_at` timestamp that distinguishes the creation of an analysis result from the source’s retrieval time. It also updated the test helper and added validation and JSON round-trip tests.

**Outcome:**
The top-level `SourceAnalysis` structure was completed as requested.

### 11. Consolidate and Verify the Phase 1 Schema

**Prompt:** Before writing the finalized Phase 1 section, consolidate the complete proposed model set end to end for one final consistency review.

Include the final module layout, every model and field, shared types and configuration, field descriptions, cross-field validators, planned tests, and acceptance criteria. Incorporate every decision approved during this review without introducing new architectural changes.

Ensure the consolidated proposal includes the finalized provenance categories and identifiers, structured methodology, named interpreted-statement subclasses, evidence form and relationship semantics, strict validation, `ResearchProblem`, and the distinction between `retrieved_at` and `analyzed_at`.

In the timezone-awareness test, assert that `analyzed_at.utcoffset()` is not `None`, rather than checking only that `tzinfo` exists.

Identify any contradiction, omitted decision, invalid import relationship, or mismatch between the schema, tests, module layout, and acceptance criteria. If none remain, say so explicitly.

Do not modify any files or write `docs/BUILD_PLAN.md` yet.

**Response:**
Claude consolidated the complete Phase 1 schema, module layout, import graph, validation rules, test organization, and acceptance criteria. It confirmed that the module dependencies form an acyclic graph and that nested evidence validators run before claim-level validators. It also corrected the timezone-awareness assertion and added direct tests for the interpreted-statement subclasses and valid retrieval timestamps.

**Issue:**
The consolidated test plan does not explicitly test two stated acceptance criteria: rejection of an empty `Claim.evidence` list and rejection of an empty `SourceAnalysis.central_claims` list.

### 12. Close Final Test-Coverage Gaps

**Prompt:** The consolidated schema is approved.

Before writing the Phase 1 build plan, add explicit planned tests confirming that:

* `Claim.evidence=[]` raises a `ValidationError`.
* `SourceAnalysis.central_claims=[]` raises a `ValidationError`.
* Separately constructed `SourceAnalysis` objects receive different automatically generated IDs.

Update the consolidated test plan and acceptance-criteria mapping only. Do not modify any files or write `docs/BUILD_PLAN.md` yet.

**Response:**
Claude added explicit tests confirming that claims reject empty evidence lists, source analyses reject empty central-claim lists, and separately constructed source analyses receive unique generated IDs. It mapped each test to the existing acceptance criteria without changing the schema or acceptance-criteria wording.

**Outcome:**
The remaining test-coverage gaps were resolved.

### 13. Write the Finalized Phase 1 Build Plan

**Prompt:** I approve the consolidated Phase 1 architecture, validation rules, tests, module layout, and acceptance criteria.

Replace the `*To be planned.*` placeholder under `## Phase 1 — Research Data Model` in `docs/BUILD_PLAN.md` with the finalized Phase 1 build plan.

Match the organizational style of Phase 0 and include the Phase 1 goal, architectural decisions, technologies, module layout, implementation tasks, validation rules, planned tests, and acceptance criteria. Incorporate every decision from the approved consolidated proposal, including the three final test additions.

Do not implement any models or tests yet. Do not modify the README, prompt log, Phase 0 section, later-phase placeholders, project configuration, or any other file. Do not commit or push anything.

After writing the Phase 1 section, report exactly what changed and confirm that only `docs/BUILD_PLAN.md` was modified. 

**Response:**
Claude replaced the Phase 1 placeholder in `docs/BUILD_PLAN.md` with the approved Research Data Model build plan, including the goal, architectural decisions, technologies, module layout, implementation tasks, validation rules, tests, and acceptance criteria. It did not implement any models or tests, modify later phases, commit, or push changes.

Claude also reported that `docs/claude_code_prompt_log.md` appeared as modified in `git status`, correctly identified it as a pre-existing user-authored change, and confirmed that its only modification was to `docs/BUILD_PLAN.md`.

**Outcome:**
The finalized Phase 1 build plan was written within the approved scope.

### 14. Clarify Concurrent User Edits

**Prompt:** You’re not in trouble. I am actively editing `docs/claude_code_prompt_log.md` while we work, so that modification is expected and belongs to me.

You handled the situation correctly by checking `git status`, distinguishing your change from my pre-existing change, and preserving my work. The `docs/BUILD_PLAN.md` update is accepted.

Going forward, if you encounter an unrelated modified file, briefly identify it as a pre-existing user change and continue preserving it. You do not need to provide an extended defense unless your changes overlap with it or the source of the modification is genuinely unclear.

Do not make any additional changes yet.

**Response:**
Claude acknowledged that the prompt-log modification was an expected user-authored change and saved the workflow calibration for future turns. It confirmed that it would preserve concurrent user edits and made no additional file changes.