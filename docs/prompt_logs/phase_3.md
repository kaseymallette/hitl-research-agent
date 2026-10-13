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
Claude reported finalizing only the Phase 3 section of `docs/BUILD_PLAN.md`, with no installations or paid calls. It replaced the proposed `sources/` package with a preparation script, `data/phase_3/sources.yaml`, and per-source preparation records. New results go under `outputs/phase_3/`. For figures and poorly extracted tables, it proposed rendering images, having the user approve the visual list, and using a vision model to transcribe approved visuals into labeled blocks in reading order. Original images would be retained and evidence drawn from transcription blocks flagged for review. Claude noted that a judge reading only prepared text cannot independently detect transcription errors.

Claude reported that DeepEval supports `threshold=None` for individual metrics but requires at least one threshold-bearing, non-flaky metric when using `evaluate()`. It therefore planned to call `measure()` / `a_measure()` directly, omit pass/fail fields, prohibit `strict_mode`, pin and record the DeepEval version, and disable telemetry. The exact `GEval` source-input parameter remained to be checked during implementation. These are Claude's reported compatibility findings, not independently verified here.

Claude left judge and vision-model selection pending, recommending configurable Sol medium as judge, with Astra low or a two-judge setup as alternatives. It estimated roughly 0.5 million input and at least 50,000 output tokens per 20,000-token source, excluding reasoning tokens, but could not verify official pricing and supplied no dollar estimate. It proposed a dry run before paid work and user confirmation of the provenance manifest. Its claim that choosing a different model eliminates self-grading is too strong; a different model does not guarantee independent or correct evaluation. No model choice or paid run has been approved.

### 3. Clarify the Pilot Cost and Transcription Handling

**Prompt:** Keep the agreed Phase 3 scope and use one configurable judge for the initial implementation. Before I choose the judge and vision model, give me a concise, concrete pilot proposal using one actual source from `data/phase_3/`.

Identify the source, its extracted text size, and the figures or tables that need visual transcription. Explain the expected calls for transcription, single-source analysis, and each DeepEval metric, including internal judge calls and how per-item checks scale with the resulting analysis. Separate known input sizes from assumptions about output, reasoning tokens, and retries.

Verify the proposed models' current capabilities and pricing using official OpenAI documentation. Give an estimated cost range for this one-source pilot, including reasoning and image inputs where applicable, and propose a bounded budget and stopping rule for my approval. If pricing or usage cannot be verified, say what remains unknown rather than substituting third-party prices or presenting a precise total.

Explain how model-transcribed content will remain distinguishable from directly extracted source text throughout analysis and evaluation, with links or locators back to the retained page images for my Phase 4 review. A judge reading the same transcription cannot validate it against the original image. Likewise, describe a different judge model as another perspective, not a guarantee against self-grading bias.

Keep this focused on the decisions needed to authorize the pilot. Do not reopen the evaluation framework or source selection. Do not implement code, edit files, install dependencies, make paid calls, commit, or push yet.

**Response:**
Claude proposed Li et al., “Making AI Less ‘Thirsty’,” as the pilot: eight pages and 35,406 characters by its raw extraction. It recommended transcribing Table 1 and Figure 2, optionally Figure 1, and excluding the decorative illustration. It noted that the IEA and Shehabi sources are close enough to the size limit that formatting and visual transcription could push them over. Claude reported no repository changes or paid calls; it used scratch programs to inspect pages and measure text.

Claude recommended keeping Astra low for analysis, using Astra medium for visual transcription, and Sol medium as the single judge. It estimated roughly 50–90 judge calls, driven mainly by per-citation and per-evidence checks. Analysis estimates were extrapolated from saved Phase 2 runs; judge output, reasoning usage, retries, and four internal faithfulness calls remained assumptions. Claude reported consulting official OpenAI documentation through a summarizing fetch tool and quoted standard input/output prices of $10/$50 per million tokens for Astra and $2/$10 for Sol, with reasoning billed as output. It asked the user to verify the pricing before approval; these rates and capability claims are recorded here as Claude's report, not independently verified findings.

Its estimated one-source pilot cost was $2–7 with Sol as judge, versus $7–20 with Astra as judge, including a stated 25% retry allowance. It proposed a $10 total budget with stage caps of $1.50 for transcription, $2.50 for analysis, and $5 for judging; usage tracking, per-call output limits, bounded retries, and an early usage check after five judge calls would stop unexpectedly expensive runs. Partial results would be saved as incomplete, with no automatic rerun. The proposed cap and stopping mechanism have not been implemented or validated, and reported API usage is not a billing reconciliation.


### 4. Reconcile the Cost Estimate

**Prompt:** I am not willing to spend $2–7 per source. My Phase 2 single-source analysis runs cost about $0.06–$0.08 each. Where did your estimate come from?

Reconcile that observed cost with your proposed $0.50–$1.50 for analysis alone before adding evaluation. Check the saved Phase 2 usage, the model and pricing assumptions, and your arithmetic. Distinguish reported usage from estimated usage, and do not double-count reasoning tokens if they are already included in output totals.

Then show clearly how much of the proposed total comes from analysis, visual transcription, and DeepEval evaluation. Explain why you proposed 50–90 judge calls per source and which of those calls are required by DeepEval versus choices in your design. Recommend a substantially less expensive approach that still implements our agreed evaluation framework. Do not assume a new budget on my behalf.

Keep the explanation focused and understandable. No implementation, dependency installations, paid calls, commits, or pushes. The proposed $10 pilot budget is not approved.

**Response:**
Claude attributed the cost discrepancy to the model rates it applied: the saved Sol runs calculated to approximately $0.06–$0.08, while the saved Astra-low run calculated to approximately $0.415 at its quoted rates. Saved results contain token totals, not billed costs, so it requested a dashboard comparison and reported that reasoning tokens were already included in output totals rather than counted twice. These dollar amounts remain Claude's calculations, not confirmed charges.

Claude acknowledged that 40–70 of its proposed judge calls were its own per-item design choice and that judge output estimates were unmeasured. It proposed combining evidence and citation checks per claim, using Sol low as judge and Sol for two visual transcriptions, and running deterministic checks first. Its revised Li pilot estimate was roughly $0.80–$1.90 overall, still based on assumptions and an unresolved analysis-price discrepancy. It reported no repository edits or paid calls. The cheaper evaluation configuration was not approved.

### 5. Run the Li et al. Single-Source Analysis

**Prompt:** Run one single-source analysis of `data/phase_3/li_et_al_2025_making_ai_less_thirsty.pdf` through the existing `analyze_source()` pipeline using the current default, `gpt-6-astra` at `low` reasoning, and the API key already in my local `.env`. I authorize this paid analysis run, including the existing one-correction-attempt policy. We want observed usage for analysis alone before deciding on evaluation costs.

Prepare the source with verified provenance, correct reading order, and readable tables. Preserve important figure information using local inspection and transcription, without paid vision calls; identify any transcription and any information you cannot reliably recover. Check the final source size before the analysis call. Keep the research question out of the analyzer's input and leave the existing analysis prompt and model defaults unchanged.

Save the prepared source and the returned `AnalysisResult` under `outputs/phase_3/li_et_al_2025_making_ai_less_thirsty/`, preserving existing files. Briefly report the output paths, actual model and reasoning setting, attempt count, input/output token usage, and whether validation succeeded. Record the run time and available request identifiers locally so I can compare the run with my API usage dashboard. Report any calculated dollar cost separately from confirmed billing, state the rate used, and do not add reasoning tokens twice.

Do not run DeepEval, make paid transcription calls, analyze other sources, or automatically rerun the pilot after failure. Do not build the Phase 3 evaluation framework, expose the API key, commit, or push. If the run fails, save available diagnostics and explain the failure briefly.

**Response:**
Pending.
