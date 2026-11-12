# ADR-0023 — Synthesis retrieves from a store of each accepted article's close reading, claims reference, and argument evaluation

- **Status:** Accepted
- **Date:** 2026-11-12
- **Landed in:** not yet committed

## Context

All ten articles were analyzed and accepted into `outputs/collection.yaml`
([ADR-0022](0022-five-calls-five-files-one-folder.md)), which left Phase 3's
open decisions: the claims store, synthesis, and retrieval. The build plan had
treated retrieval as later work, for when the collection outgrew one call.

The ten close readings share one structure: reading steps, each with a
location, the model's moves and meaning, and claims, each claim with its text,
its `verbatim` or `paraphrased` form, and its support with citations. Together
they hold 1,344 claims and 804 support items. Each article also has a claims
reference, an inventory of the article's own claims written from the article
alone, and an argument evaluation, the model's judgment of the argument. Both
are Markdown, and their headings differ from article to article.

[ADR-0018](0018-three-agents-analysis-synthesis-research-assistant.md) had
synthesis read only close readings, so that the model's judgment of an
argument never became part of what the sources say.

## Decision

**Synthesis works by retrieval, from a store built from every accepted
article's close reading, claims reference, and argument evaluation.**

- `outputs/collection.yaml` decides what enters. The builder reads only the
  articles listed there, and from each, its `01_close_reading.json`,
  `02_claims_reference.md`, and `04_argument_evaluation.md`, plus its
  provenance from `data/research/sources.yaml`. Judgments and scores stay out
  of what synthesis retrieves; the scores are kept per article for my review.
- The store is a SQLite database with full-text search, built by a script
  from those committed files, with no model call. It is rebuilt, never edited
  by hand, and is not committed.
- Every item records its kind and its source. In the store, the documents are
  named by what they are, not by their call number:

  | Kind | From | Whose words |
  | --- | --- | --- |
  | `claim`, with its support and citations | `close_reading` | the authors', `verbatim` or `paraphrased` |
  | `reading`: a step's moves and meaning | `close_reading` | the model's reading |
  | `reference_section` | `claims_reference` | the authors', as listed by a separate session |
  | `evaluation_section` | `argument_evaluation` | the model's judgment |

- Close-reading items keep their step, their order in it, and the step's
  location, and are identified by position: `<slug>` plus step, claim, and
  support numbers. The claims reference and the argument evaluation are split
  into sections at their headings, each identified by its heading and order,
  not parsed into claims.
- The builder stops only on a technical failure: a file that does not parse,
  a missing field, or a slug in `collection.yaml` with no folder
  ([ADR-0005](0005-no-hard-quality-gates.md)). Nothing is dropped or flagged
  for its quality.
- A query script retrieves: text search, an article's items in document
  order, and one item with its support, citations, and location. Every result
  carries its kind and source.
- The synthesis session runs in Codex like the single-source calls. It is
  given the database and the query script and queries the store itself. Each
  position it reports cites the IDs it rests on and keeps the kinds apart: a
  model `reading` or `evaluation_section` is never reported as what a source
  says. It receives no research question
  ([ADR-0006](0006-analysis-and-synthesis-never-receive-the-question.md)).
- Each synthesis records the build of the store it read: a hash of the input
  files.

## Alternatives considered

- **One synthesis call over all ten close readings.** Their author-reported
  text is about 80k tokens, so it would fit today. But it gives synthesis no
  way to look anything up, and retrieval would be built later anyway.
- **Close readings only, as ADR-0018 had it.** It keeps the model's judgment
  out by leaving it out. Labeling every item by kind keeps it apart while
  letting synthesis see where the evaluation found an argument weak.
- **A vector database.** Not shown to retrieve better here than full-text
  search over text that is already split into claims.
- **Parsing the claims reference and evaluation into claims.** Their formats
  differ by article; a parser would be fitted to ten files and break on the
  eleventh.
- **Committing the database.** It is generated from committed files, so it
  would only be a second copy to keep in sync.

## Consequences

**Every synthesis position can be traced** to the items it cites, and through
them to an article, a step, and a location, or to a section of the claims
reference or evaluation. The judge of a synthesis can look up the same IDs
with the same script.

**The kinds are only as separate as the synthesis keeps them.** The store
labels everything, but a synthesis can still blur an evaluation into a
source's claim. That is for the synthesis judgment to catch, which needs its
own criteria in `docs/RUBRIC.md`.

**Positional IDs move when a reading is revised.** `--revise 01` can renumber
steps and claims, so a synthesis is tied to the store build it read, and a
revision means rebuilding the store and rerunning any synthesis that cited
the article.

**Sections are coarser than claims.** A search finds text inside a claims
reference or evaluation section, but cites the whole section.

## Notes

Amends [ADR-0018](0018-three-agents-analysis-synthesis-research-assistant.md):
synthesis may retrieve argument evaluations and claims references as well as
close readings, each labeled by kind. The rest of ADR-0018 stands.
