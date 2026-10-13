## Phase 3 — Evaluation

### 1. Plan the DeepEval Implementation

**Prompt:** We are starting Phase 3 — Evaluation. Implementing DeepEval is an established design decision. Read `README.md`, `docs/BUILD_PLAN.md`, and the current analysis models to understand the integration points, then propose a concrete Phase 3 implementation plan.

I have selected 12 preliminary sources in `data/` for the freshwater research question in the README. Their single-source analyses have not been run yet. Include preparation of source text and provenance, followed by use of the existing analysis pipeline, as prerequisites to evaluating the results with DeepEval. Preserve reading order and important tables and figures, check the source-size limit, and identify the IEA source as an excerpt. Each analysis remains question-independent. These sources are research inputs, not a labeled benchmark; do not reconsider my source selection.

Keep the plan focused on DeepEval faithfulness, citation evaluation, and custom research-specific metrics described in the README. Verify DeepEval's current documentation and distinguish built-in metrics from custom metrics we need to define.

Specify:
- What analysis data and source text each metric receives.
- What each metric checks and what scores and explanations it returns.
- The modules, dependencies, and tests needed to run evaluation and retain its results for Phase 4.

Phase 3 provides automated evaluation. Phase 4 is where I review the analysis and evaluation results and decide whether they are good enough. Do not add human labeling, a gold dataset, or automatic acceptance/rejection gates to Phase 3.

Do not reopen Phase 2, redesign the project, or expand the agreed scope. Keep your plan concise, make routine implementation recommendations yourself, and flag only genuine blockers. Do not edit files, install dependencies, or make paid API calls yet.

**Response:**
Claude proposed using DeepEval's built-in `FaithfulnessMetric`, custom per-item metrics for citation faithfulness and evidence mapping, and five `GEval` rubrics for argument reconstruction, assumption discipline, limitation discipline, inference control, and research usefulness. It reported checking DeepEval's documentation and recommended a configurable `gpt-6-sol` judge at `medium` reasoning through a `DeepEvalBaseLLM` adapter. Scores and explanations would be retained for Phase 4 without acceptance gates; judge errors would be recorded separately from scores. Judge selection and the proposed `threshold=None` configuration remain unconfirmed.

For the 12 preliminary sources, Claude proposed a new `sources/` package, a provenance manifest, PDF extraction with `pymupdf4llm`, preparation records, size checks, and an explicit IEA excerpt label. It would then run the existing question-independent analyzer and save analysis and evaluation JSON separately. Its figure-handling proposal retained captions but omitted figure contents. It proposed offline tests with a fake judge, followed by an approved paid pilot and then the remaining sources. Claude reported no file edits, installations, or paid calls, and noted the existing source/output deletions and documentation edits without changing them.

### 2. Refine and Document the Phase 3 Plan

**Prompt:** This direction fits the agreed Phase 3 scope. Before implementation, finalize the Phase 3 section of `docs/BUILD_PLAN.md`.

The sources are now organized by phase: `data/phase_2/` contains the restored care-ethics PDF, and `data/phase_3/` contains the 12 preliminary freshwater sources. Use only `data/phase_3/` for this preparation and analysis batch.

Keep preparation of these 12 sources lightweight: use a script and provenance records rather than building a replacement ingestion package. Preserve important information in tables and figures; captions alone are insufficient where the figure carries evidence.

Verify the proposed DeepEval configuration, particularly `threshold=None`, with its supported API. Evaluation results must remain advisory regardless of internal metric thresholds.

Explain briefly the expected cost and practical tradeoff of your proposed judge configuration before I choose it. Don't make paid calls yet. Record the judge choice as pending in the plan.

The care-ethics source and its eight saved JSON results have been restored for the development record in `data/phase_2/` and `outputs/phase_2/`. Use `outputs/phase_3/` for the new analyses and evaluation results. Preserve my current files and source selection. Do not implement code, install dependencies, commit, or push.

**Response:**
Pending.
