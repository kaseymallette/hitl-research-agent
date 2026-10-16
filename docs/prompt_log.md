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

- [Phase 1 — A/B Testing](phases/phase_1.md)
- [Phase 2 — DeepEval](phases/phase_2.md)
- [Phase 3 — Research Collection](phases/phase_3.md)
- [Phase 4 — Synthesis Agent](phases/phase_4.md)
- [Phase 5 — Literature Review Agent](phases/phase_5.md)
- [Phase 6 — RAG](phases/phase_6.md)

The logs for the old nine-phase plan are not here: they live on the `v1` branch
and at the `v1-final` tag, along with that version's experiment outputs — for
example `git show v1-final:docs/prompt_logs/phase_3.md`. The tag cannot move;
the branch can.
