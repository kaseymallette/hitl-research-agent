## Phase 2 — Single-Source Analysis

### 1. Review Phase 2 Architecture

**Prompt:** Read `README.md`, `docs/BUILD_PLAN.md`, `docs/prompt_logs/phase_1.md`, and the implemented Phase 1 model and test files. Familiarize yourself with the current project architecture and development workflow. Treat the README, build plan, and current repository state as the sources of truth. Use the Phase 1 prompt log to understand how we iteratively review architectural decisions before writing or implementing a finalized plan.

We are beginning Phase 2 — Single-Source Analysis. The goal is to use an LLM to convert a manually supplied research source into a validated `SourceAnalysis`. Manually supplied sources are an implementation-stage bridge until source discovery and ingestion are added in Phase 5.

Treat these boundaries as settled: single-source analysis does not receive the human’s research question; `project_tag` does not belong in the Phase 1 models or Phase 2 analysis output; and Phase 2 does not include evaluation, human review, persistence, source discovery, cross-source synthesis, RAG, or orchestration.

Do not modify any files or write the finalized Phase 2 build plan yet. First, review the existing schemas and project setup, then propose an initial Phase 2 architecture. Identify the decisions we need to resolve concerning the analysis input, application-owned versus model-generated fields, structured LLM output, citation and source-location handling, prompting, validation and retry behavior, error handling, model configuration, dependency choices, module layout, and testing without routine paid API calls.

Ask questions only when the answer would materially change the architecture. Otherwise, give your recommended choice and explain the tradeoff. End with the first small set of architectural questions we should resolve together before drafting the Phase 2 build plan.

**Response:**
Claude reviewed the current documentation, Phase 1 implementation, configuration, and dependencies. It proposed a dedicated source-input model, separate extraction schemas for model-generated content, one structured OpenAI call, deterministic verbatim-evidence checking, bounded correction retries, explicit extraction errors, injectable models for network-free tests, and a new `extraction/` package. It identified four decisions concerning extraction-schema reuse, single versus multiple model calls, Phase 2 grounding checks, and retry behavior.

**Issue:**
The proposed extraction schemas must be reviewed against OpenAI’s strict structured-output requirements before deciding which Phase 1 models can be reused. The model configuration, source-size boundary, and usage/cost metadata also remain unresolved.

### 2. Clarify the Phase 2 Design

**Prompt:** I understand the main distinction you’re making: the LLM should generate the research analysis, but the application should add factual metadata such as provenance, IDs, and timestamps. I agree that we should not refactor the finalized Phase 1 models just to make them work as the LLM’s output format.

Before we decide exactly which separate extraction models to create, please check which existing Phase 1 models can actually be reused with OpenAI’s structured output and which cannot. Explain the reason in plain language. I want to understand why each new model is necessary rather than approving duplicate models I do not understand.

For the other questions, I’m leaning toward one model call for the complete source analysis. I also think Phase 2 should verify that evidence labeled `"verbatim"` actually appears in the source, because that is part of producing a valid analysis rather than the broader evaluation planned for Phase 3. For retries, I’m leaning toward one correction attempt when the model’s analysis fails validation. Technical retries for API or network failures should be handled separately.

I also want to understand the input more clearly. Explain whether `RawSource` is the right name if Phase 5 will eventually pass normalized source content into Phase 2, how large a source Phase 2 will support, and whether we need to divide long sources into pieces. Please recommend the simplest approach that can analyze the controlled MVP sources without prematurely building Phase 5.

Finally, explain what information we should retain from each model call, such as the model used and token usage, and recommend an appropriate current OpenAI model based on analysis quality and cost. Confirm that the proposed LangChain approach uses OpenAI’s native structured output correctly.

Revise the Phase 2 proposal based on these points. Do not modify any files or write the finalized build plan yet. End by identifying only the decisions that still genuinely require my input.

**Response:**
Claude confirmed that Phase 2 needs three extraction models so the LLM generates research content without generating application-owned IDs, timestamps, or provenance. It proposed a NormalizedSource input, one whole-source model call with a configurable size limit, deterministic checking of verbatim evidence, and one correction attempt for invalid output. It also proposed retaining model and token-usage metadata through an AnalysisResult wrapper. Two decisions remained: the public return type and the OpenAI model.

### 3. Use GPT-6 Sol

**Prompt:** I approve returning an `AnalysisResult` rather than a bare `SourceAnalysis`. It should contain the completed analysis, the model used, total input tokens, total output tokens, and `attempt_count`. If a correction attempt is needed, the token totals should include both calls. Do not add other metadata without explaining why it is necessary first.

Use `gpt-6-sol` as the default model, configurable through `Settings`. This replaces the earlier `gpt-5.6-terra` selection. Start with `medium` reasoning and omit `temperature` and other sampling parameters unsupported with reasoning enabled.

Check the current official documentation:
- https://developers.openai.com/api/docs/models/gpt-6-sol
- https://developers.openai.com/api/docs/guides/latest-model

Use the Responses API with OpenAI’s native structured output through LangChain. Verify how the current LangChain integration selects that API, supplies the strict output schema, and exposes token usage—including when output fails validation. Do not assume older configuration examples apply.

Use `SourceDocument` rather than `RawSource` or `NormalizedSource`. It should contain source text and provenance without defining the normalization process that Phase 5 will eventually perform.

Review the updated Phase 2 section of `docs/BUILD_PLAN.md`, then revise your architecture proposal around these decisions. Explain any remaining compatibility issues or design choices in plain language, particularly extraction-schema reuse and source-size limits.

Do not modify files, install dependencies, make paid API calls, or write the finalized build plan yet. End with only the decisions that still genuinely require my input.

**Response:**
Claude reported verifying GPT-6 Sol’s availability, pricing, structured-output support, and `medium` reasoning against the official documentation. It recommended explicitly setting `use_responses_api=True`, omitting incompatible sampling-parameter settings, and using LangChain’s `with_structured_output(ExtractedAnalysis, method="json_schema", strict=True, include_raw=True)`. It explained that retaining the raw response allows token usage to be accumulated across a locally invalid first response and its correction attempt. It left the exact generated Responses API request payload to be checked without a paid call during implementation.

Claude retained the proposed `ExtractedEvidence`, `ExtractedClaim`, and `ExtractedAnalysis` split to separate model-generated research content from application-owned fields. It revised its earlier character-count proposal to recommend adding `tiktoken` and capping source text at 150,000 tokens, citing the higher whole-request pricing above 272,000 input tokens. It asked for approval of the proposed limit and tokenizer dependency. These remain proposals, not accepted decisions. Claude acknowledged the existing user edits and reported no file changes.

**Open Issues:**
The source-size limit and `tiktoken` dependency remain undecided. The generated request payload still needs inspection, and Claude’s claims about tokenizer precision and usage availability across failure cases need review before finalizing the plan.

### 4. Keep Phase 2 Simple

**Prompt:** Your Phase 2 proposal is getting too detailed for this stage. Please give me a short recommendation on the two choices you raised: a sensible source-size limit for our initial documents, and whether we need `tiktoken` now. Explain each in plain language. A rough, conservative limit is fine; we can refine it after testing real sources.

For the rest, use the simplest approach that fits our agreed Phase 2 scope. Check schema compatibility and handle failures during implementation. Don't promise exact token counts when an API call fails before a response arrives.

Please explain your recommendation in plain language so I can understand the tradeoff. Do not change files or write the final build plan yet.

**Response:**
Claude recommended a provisional 200,000-character limit on source text, checked before calling the model. Longer documents would produce a clear error rather than being truncated. It recommended deferring `tiktoken` because a rough character guard is enough for the initial controlled sources, while tokenizer setup would add complexity to offline tests. The limit should be revisited after testing real sources. Claude will handle schema compatibility, failures, and token accounting during implementation, without reporting usage for a call that returned no response. No files were changed and no dependencies were installed.

### 5. Finalize the Phase 2 Build Plan

**Prompt:** I accept your Phase 2 recommendations: start with a 200,000-character limit on `SourceDocument.text`, reject longer sources clearly before the model call, and defer `tiktoken`. Treat the limit as provisional and adjustable after testing real sources. Please now turn the agreed Phase 2 design into the finalized Phase 2 section of `docs/BUILD_PLAN.md`, following the structure used for Phases 0 and 1: goal, architectural decisions, technologies, implementation tasks, tests, and acceptance criteria.

Keep the plan focused on one manually supplied source, GPT-6 Sol, the `AnalysisResult` we approved, native structured output, verbatim evidence checks, and one correction attempt for invalid analysis. Technical API retries should remain separate. Let the application supply provenance, IDs, and timestamps. Do not add evaluation, human review, storage, discovery, chunking, or orchestration. Resolve routine schema and failure-handling details in the plan using your judgment, and describe them plainly. Preserve the completed Phase 0 and 1 sections and my edits to the prompt log. Do not implement code, install dependencies, make API calls, commit, or push. After editing, briefly tell me what you added and flag any decision you truly cannot make without me.

**Response:**
Claude replaced the Phase 2 placeholder in `docs/BUILD_PLAN.md` with a complete plan covering the agreed input and output models, field ownership, GPT-6 Sol configuration, structured extraction, source-size guard, evidence checking, correction policy, implementation tasks, tests, and acceptance criteria. It recorded the 200,000-character limit as provisional and left the acceptance criteria unchecked because Phase 2 has not been implemented. Claude reported changing only the build plan, leaving Phase 0 and 1 intact, and making no code changes, dependency installations, API calls, commits, or pushes. It reported no remaining architectural decisions requiring user input.

### 6. Implement Phase 2

**Prompt:** Implement Phase 2 according to the finalized Phase 2 section of `docs/BUILD_PLAN.md`. Add the extraction code, configuration, required dependencies, and meaningful offline tests. Use fake model responses in the normal test suite; do not make paid API calls. Check that the LangChain structured-output schema and request configuration work as planned without sending a request. Handle parsing failures clearly as part of the agreed failure policy. Make routine implementation choices yourself; if the plan requires a material architectural change, explain it before making that change.

Preserve the existing Phase 0 and 1 code and my edits to `README.md` and `docs/prompt_logs/phase_2.md`. After implementation, run `uv run pytest`, `uv run ruff check .`, `uv run ruff format --check .`, and `uv run mypy src`. Update the Phase 2 acceptance checkboxes only for criteria you verified. Briefly report what changed, the check results, and any remaining limitation in plain language. Do not commit or push.

**Response:**
Claude implemented the Phase 2 extraction package, configuration, dependencies, and offline tests. It reported 66 passing tests, clean Ruff lint and formatting checks, and clean mypy checks. It verified that the extraction schema converts to OpenAI's strict format and that the LangChain pipeline can be constructed without sending a request. The tests used fake model responses; no OpenAI API call was made. Claude noted that refusal and incomplete-response handling still needs confirmation against a real response, and the provisional 200,000-character source limit has not been tested against representative documents. It checked the Phase 2 acceptance criteria, made no commit or push, and preserved the existing README and prompt-log edits.
