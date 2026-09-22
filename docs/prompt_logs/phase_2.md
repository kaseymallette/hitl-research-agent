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

### 3. Choose the Return Type, Model, and Source Input

**Prompt:** I approve returning an AnalysisResult rather than a bare SourceAnalysis. The result should contain the completed analysis, the model used, total input tokens, total output tokens, and attempt_count. If the model needs its one correction attempt, the token totals should include both calls. Do not add other metadata unless it is necessary, and explain why before adding it.

Use gpt-5.6-terra as the default model, while allowing it to be changed through Settings. Confirm which configuration parameters that model currently supports. In particular, do not assume that temperature=0.0 is appropriate just because it was used with older models. Recommend whether we should set a reasoning-effort value for this extraction task and explain the choice in plain language.

Use SourceDocument rather than RawSource or NormalizedSource. Phase 2 needs a document containing source text and provenance, but it does not need to define the normalization process that Phase 5 will eventually perform.