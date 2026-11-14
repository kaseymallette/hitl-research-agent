# Project

What we're doing, why, and what's been decided. This is the working
reference. When a decision changes, edit it here; don't add a new record.

## The questions

**Literacy (the main study).** How is the science of reading defined,
simplified, and contested as it travels from peer-reviewed research, through
the popular press, into state legislation? What gets lost in translation at
each step? The study analyzes discourse (critical discourse analysis,
translation theory, critical policy analysis), not whether any approach to
reading instruction works. Details are in
[`studies/literacy/README.md`](../studies/literacy/README.md).

**Water (the first case study).** Why does AI infrastructure use freshwater,
and when could other cooling or water supplies, including desalination,
reduce pressure on local freshwater? Details are in
[`studies/water/README.md`](../studies/water/README.md).

**The method question, shared by both.** Does a structured close reading
(claims, their support, and the model's reading of each step) help find and
compare claims across documents, compared with working from the documents'
text directly? For literacy this is concrete: tracing a claim from a law back
through the press to scholarship is a matter of finding the related passages.

## How they connect

Both studies take claims out of individual documents and compare them across
documents. Water compares sources on one question. Literacy traces claims
between corpora. The method question is answered on the studies' own data,
with literacy judged by the domain expert, rather than on a benchmark.

## Decisions

- **Only a technical failure stops a run.** A thin analysis, an unsupported
  claim, or a `verbatim` quotation that doesn't match the source is reported
  to the researcher, never withheld.
- **The human decides what counts.** Each analysis is accepted, revised,
  rerun, or rejected before it is used.
- **Analyses run in Codex, reading the PDF.** Water uses
  `scripts/run_single_source.py` (five automated calls); literacy uses
  `scripts/workspace.py` (load, run the session, save). The two workflows stay
  separate until it's clear what tracing claims between corpora needs.
- **Source PDFs that can't be redistributed stay local.** Only their
  `sources.yaml` entries are tracked. That covers all literacy PDFs for now
  and three publisher-copyrighted water articles.

## Open

- What "travel" means concretely for the literacy study: the unit that
  travels (a claim, a term, a cited study), and whether to trace specific
  lineages or compare how each corpus treats the same concept. To settle with
  the domain expert, starting with a few concepts traced by hand.
- How to test the method question: what to compare (document text, close
  readings, or both) and how to judge what each one finds.
- Whether the legislation PDFs, which are public domain, should be tracked.

## Status

- **Literacy:** six laws analyzed (close reading and discourse analysis), and
  the legislation codebook revised from them. Proposed new codes await
  review. Scholarly and popular press not started.
- **Water:** ten articles analyzed and accepted. Synthesis across them not
  built.
