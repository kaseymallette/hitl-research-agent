# ADR-0004 — `pymupdf4llm` is pinned to an exact version

- **Status:** Accepted
- **Date:** 2026-10-13
- **Landed in:** `6e6f55a`

## Context

PDF preparation extracts text and tables with `pymupdf4llm` in layout mode.
The extraction behaviour was verified against version 1.28.2 — reading order,
table structure, and the block geometry the column-reordering pass depends on
— and the 27 preparation tests encode what that version produces.

The failure mode that matters is silent. Outside layout mode the library drops
tables without raising anything: the extraction succeeds, the text looks
plausible, and a table the authors' argument rests on is simply gone. A change
in extraction behaviour does not announce itself; it shows up as an analysis
that is missing something, which is indistinguishable from an analysis of a
source that never had it.

## Decision

`pymupdf4llm==1.28.2`, an exact pin, not a floor. The version moves only as a
deliberate change, with the preparation tests re-run and the output compared
against a prepared article by eye.

## Alternatives considered

- **A compatible-release floor (`>=1.28,<2`).** The normal choice, and wrong
  here: the behaviour being relied on is the detailed layout output, not the
  public API, and a patch release is free to change it without a version
  signal.
- **Stay on legacy mode** and avoid the layout dependency entirely. This is
  the silent-table-dropping path. Cheaper to install, and it quietly produces
  incomplete sources.
- **Vendor the extraction code.** Too much surface to own for a pipeline that
  may not survive the A/B experiment at all.

## Consequences

Upgrading is a task with a procedure, not a dependency bump. The preparation
tests are what makes that procedure possible; they are the most valuable tests
in the repository for exactly this reason.

Layout mode pulls in `onnxruntime` through `pymupdf-layout`, and `onnxruntime`
ships no recent Intel-macOS wheels. The lockfile would be uninstallable
without saying which platforms to resolve for, so `[tool.uv]
required-environments` names three: Intel macOS, Apple Silicon, and x86-64
Linux. A fourth platform needs adding there before it can be used. This is a
consequence of depending on layout mode, not a separate choice.

If the prepared-text arm loses the A/B experiment, most of
`prepare_sources.py` goes, and this pin goes with it.

## Notes

Back-filled 2026-10-17. The pin and the platform list are both in
`pyproject.toml`, each with a comment pointing at the reason.
