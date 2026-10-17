# ADR-0008 — Compare sending the full PDF against prepared text plus crops

- **Status:** Provisional — Phase 1 decides, and the record that states the outcome supersedes this one
- **Date:** 2026-10-15
- **Landed in:** `f36a056`

## Context

Claude Code proposed extracting text from the PDFs and preparing image crops
for figures, equations, and multi-level table headers. That approach was
built: `scripts/prepare_sources.py` is 793 lines, the largest file in the
repository.

After it was underway, I asked:

> Why not just send the PDF?

The two approaches had never been compared. Preparation was the input because
it was the first thing proposed and the first thing built, not because there
was any evidence it produced better analyses. The question has a real answer
in either direction and nobody had looked for it.

Sending the PDF lets the model read figures and tables as they are laid out,
with nothing lost in extraction, but gives up any control over what was read
and leaves no inspectable artifact behind. Prepared text is inspectable and
citable, costs manual effort for every article, and loses whatever extraction
gets wrong.

The quotation gate in [ADR-0005](0005-no-hard-quality-gates.md) arrived the
same way — built first, questioned later. This one was questioned before the
comparison got expensive.

## Decision

**Do not choose yet. Measure, and state in advance what will settle it.**

Phase 1 runs a 2 × 2 over the four articles in `data/research/ab_testing/`,
producing 16 analyses:

| | GPT-6.1 Sol, medium effort | GPT-6 Astra, low effort |
| --- | --- | --- |
| **Full PDF** | 4 analyses | 4 analyses |
| **Extracted text + crops** | 4 analyses | 4 analyses |

Held fixed across every cell: the analysis prompt, the output schema, the
one-correction policy, and the question-independence of the task
([ADR-0006](0006-analysis-and-synthesis-never-receive-the-question.md)). The
intended variables are the input method and the model configuration.

What settles it, decided before the results exist so the criteria cannot be
fitted to them:

- faithfulness and assessment quality against the Phase 2 evaluation axes,
  with a human-scored sample
- token usage, calculated cost, and runtime
- the manual time and work preparation actually takes per article

A third input mode exists in the code — `prepared_text`, text with no crops —
and is not a third arm. An article with no figures, equations, or multi-level
table headers produces no crops, so the prepared arm sends text alone for that
article and records `crops_sent`. The arm is the input *workflow*; the crop
count is a property of the article.

## Alternatives considered

- **Keep the prepared-text pipeline because it exists.** 793 lines and the
  hours that produced them are the whole argument, and that is a sunk cost.
  This is the option the project was already on without having chosen it,
  which is why it is worth naming and rejecting in writing rather than just
  moving past.
- **Switch to PDF-only now, on the grounds that it is obviously simpler.**
  Simpler, probably cheaper, and equally unmeasured — the same mistake in the
  other direction. Preparation might genuinely produce better analyses; the
  point is that nobody knows.
- **Test the input method and the model separately** rather than as a 2 × 2.
  Half the runs and half the cost. It cannot see an interaction, and an
  interaction is plausible here: a lower-effort model may depend more on clean,
  well-ordered text than a stronger one does.
- **Use more than four articles.** Better evidence, proportionally more money
  and review time. Four is what the budget and the human scoring effort
  support.

## Consequences

**`prepare_sources.py` is frozen until this resolves.** It is not expanded,
tidied, or improved, because changing it changes what one arm of the
experiment produces. Its known rough edges stay as they are for now. This is
already recorded as the reason that file was untouched by the Phase 0
consolidation.

**If prepared text loses, most of those 793 lines go**, and
[ADR-0004](0004-pin-pymupdf4llm-exactly.md) — the exact `pymupdf4llm` pin —
goes with them, along with the 27 preparation tests.

**If it wins, the manual preparation cost is accepted knowingly** for all 16
articles, having been measured rather than assumed.

**Phase 3 cannot start until this is settled**, since the collection should be
analyzed in one configuration.

**Four articles is an initial comparison, not a conclusion** about which
approach works best across research topics. The record of the outcome should
say so too.

The experiment costs real API spend and real review time. That cost is
accepted as the cheaper error: finding out after analyzing all 16 articles
that the input format was wrong would cost more.

## Notes

Back-filled 2026-10-17, and the only record here that is not `Accepted`. It
holds a question open on purpose so it cannot drift closed — the outcome needs
a new record, and this one is then marked superseded rather than edited.

The experiment design is in [README.md](../../README.md#the-ab-experiment) and
the procedure in [BUILD_PLAN.md](../BUILD_PLAN.md); this record is the decision
to run it instead of choosing.
