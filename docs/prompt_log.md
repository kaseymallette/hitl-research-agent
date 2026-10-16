# Prompt Log

This log records the prompts given to the AI tools building this project and
what came back. It exists so the reasoning and decisions behind the project's
structure — not just the resulting code and documentation — stay visible to
future contributors and sessions.

Claude Code writes the code; Codex helps with design and prompt writing and
maintains this log.

## Conventions

Entries are organized by [build plan](BUILD_PLAN.md) phase, one file per phase,
numbered locally within that phase in the order the prompts were given.

Nothing is rewritten after the fact. A prompt that turned out to be wrong, a
response that overstated what it had done, and a decision later reversed all
stay as recorded — that record is the point of the log.

Each entry carries:

- **Prompt** — the instruction as given.
- **Response** — what came back: what was built or changed, what was checked,
  and, kept distinct from both, what was claimed but not independently
  verified. Reported test counts and clean checks are claims until someone
  looks.
- **Pending decision:** — written out where a turn ends needing the
  researcher's call, so it is not lost between entries.

## Phases

- [Phase 1 — A/B Testing](prompt_logs/phase_1.md)
- [Phase 2 — DeepEval](prompt_logs/phase_2.md)
- [Phase 3 — Research Collection](prompt_logs/phase_3.md)
- [Phase 4 — Synthesis Agent](prompt_logs/phase_4.md)
- [Phase 5 — Research Agent](prompt_logs/phase_5.md)
- [Phase 6 — RAG](prompt_logs/phase_6.md)

The v1 logs for the old nine-phase plan were removed when the project was
redesigned; they remain in git history (`git show main:docs/prompt_logs/`).
