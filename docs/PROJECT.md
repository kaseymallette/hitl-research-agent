# Project

What we're doing, why, and what's been decided. This is the working
reference. When a decision changes, edit it here; don't add a new record.

## The questions

**The main question.** Can AI meaningfully support rigorous,
evidence-grounded research?

**The study.** How is the science of reading defined, simplified, and
contested as it travels from peer-reviewed research, through the popular
press, into state legislation? What gets lost in translation at each step?
The study analyzes discourse (critical discourse analysis, translation theory,
critical policy analysis), not whether any approach to reading instruction
works. Details are in
[`studies/science_of_reading/README.md`](../studies/science_of_reading/README.md).

## Decisions

- **Only a technical failure stops a run.** A thin analysis, an unsupported
  claim, or a `verbatim` quotation that doesn't match the source is reported
  to the researcher, never withheld.
- **The human decides what counts.** Each analysis is accepted, revised,
  rerun, or rejected before it is used.
- **Analyses run in Codex, reading the PDF.** `scripts/workspace.py` loads one
  document into a workspace outside the repository; each prompt runs in its own
  Codex session on GPT-6.1 Sol at medium effort; saving copies the results to
  `outputs/<corpus>/<slug>/`.
- **Scholarly articles answer the three questions; laws get a discourse
  analysis.** `scripts/run_scholarly.py` runs three Codex sessions per article
  from `harness/scholarly/prompts/`, writing to `outputs/scholarly/<slug>/`:
  the three questions answered from the article alone, the close reading, then
  the three questions answered from the article and the close reading.
  The legislation codebook is not used for articles.
- **Source PDFs stay local.** Only their `sources.yaml` entries are tracked.
- **Questions are answered from the saved analyses.** The expert's questions
  are answered from each document's close reading and discourse analysis, and
  kept in `studies/science_of_reading/questions/`.

## Open

- What "travel" means concretely: the unit that travels (a claim, a term, a
  cited study), and whether to trace specific lineages or compare how each
  corpus treats the same concept. To settle with the domain expert, starting
  with a few concepts traced by hand.
- Whether each document also gets an argument analysis (for legislation, an
  argument analysis of the law) alongside its discourse analysis.
- Whether the legislation PDFs, which are public domain, should be tracked.

## Status

- **Legislation:** six laws analyzed (close reading and discourse analysis),
  and the codebook revised from them. Proposed new codes await review.
- **Questions:** three of the expert's questions answered from the six laws.
- **Scholarly:** the expert's articles are being added; not yet analyzed.
- **Popular press:** not started.

Earlier work (the water study and the retrieval experiments) is kept in git
history and on the `wip-2026-11-25` branch.
