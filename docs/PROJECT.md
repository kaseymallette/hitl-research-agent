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

**The main question.** Can AI meaningfully support rigorous,
evidence-grounded research?

**The experiment.** Does structured source analysis improve downstream
research quality compared with retrieving original source passages directly?
It runs on the water study first; see below.

## How they connect

Both studies take claims out of individual documents and compare them across
documents. Water compares sources on one question. Literacy traces claims
between corpora. What the experiment means for literacy is decided once the
water experiment is done.

## The experiment: water

**Why water.** All ten articles are analyzed and accepted, so the experiment
can start now on a complete collection.

**The framing.** Suppose a researcher had to write a paper on the water
question. The test questions are the questions they would need answered to
write it: research questions about the collection, not lookups of single
facts. Each approach is judged on how well what it retrieves would let the
researcher answer them, grounded in the sources.

### The two approaches

1. **Original documents.** Extract, chunk, embed, and retrieve passages from
   each article's text. `scripts/prepare_sources.py` already extracts the text.
2. **Structured analyses.** Retrieve from each article's close reading (01),
   claims reference (02), and argument evaluation (04).

A third approach, retrieving from both, was dropped after the trial run: how
much of each kind it retrieved varied by question (for question 8, none of
the article text), which added a variable without isolating one. Comparing
two approaches tests one difference: the articles' text or their analyses.

Every retrieved item names its article and what kind of item it is (source
text, close reading, claims reference, or argument evaluation), so the model's
reading and judgment are never reported as what a source says.

**Measures:** retrieval quality, source attribution, synthesis accuracy, and
cost.

### How it's judged

Judging started blind and head to head: the A/B experiments chose the analysis
setup by tournament. The experiment moves to codebook judging, in the style of
the literacy study's codebook. No one writes correct answers to the
questions. Each answer is coded for three things: the same two tasks as the
close reading and the argument evaluation, and the water question's own
distinctions:

- **Attribution:** does it represent the sources faithfully and credit each
  claim to the source that makes it? Checked against the original articles.
- **Argument:** does its own argument hold up: reasons for the why, evidence
  weighed, conclusions qualified and bounded, counterevidence addressed?
- **Water distinctions:** does it keep apart withdrawal and consumption,
  onsite and grid water, water of different quality, different accounting
  boundaries and units, local and total pressure, modeled and measured results,
  and treat desalination as one option among others?

The codes are in [`studies/water/CODEBOOK.md`](../studies/water/CODEBOOK.md),
in draft. A second session checks the coding, and the researcher spot-checks
where they disagree. The approaches are compared by how often each code
appears in their answers.

### Research questions

Ten candidates, moving from explaining freshwater use to comparing
interventions and judging what the evidence can support.

1. What explains the use of freshwater, and specifically drinking-quality
   water, in the cooling systems described in this collection, and under what
   conditions could other water supplies meet the same requirements?
2. Which differences among reported water footprints reflect differences in
   the systems studied, and which reflect definitions, accounting boundaries,
   or units of comparison?
3. Under what conditions do changes in cooling technology reduce overall water
   consumption, and when do they shift water use between the facility,
   electricity generation, and other life-cycle stages?
4. How does accounting for where and when water is used change assessments of
   pressure on local freshwater resources and the relative merits of
   interventions?
5. What does the collection establish about desalination as a way to reduce
   reliance on existing freshwater supplies, and what remains unresolved when
   it is compared with reclaimed water or lower-water cooling?
6. How far can findings from the systems and workloads studied here be
   generalized to AI infrastructure operating at commercial scale?
7. Under what combinations of computing-demand growth, efficiency
   improvements, and infrastructure changes could total water use rise,
   stabilize, or fall?
8. Where does agreement across the collection reflect independent evidence,
   and where does it reflect reliance on shared estimates, datasets, or
   illustrative cases?
9. Which proposed reporting, planning, and governance measures are supported
   by the collection's findings, and which depend on additional evidence or
   value judgments?
10. What does the collection show about who bears the effects of data center
    water use (nearby communities, agriculture, ecosystems), and how much of
    that rests on evidence of actual harm rather than on volumes of water used
    or exposure to water stress?

### Steps

- [x] Draft the codebook.
- [x] Draft the test questions.
- [x] Build the original-documents index.
- [x] Build the structured-analyses index.
- [x] Build the answering step: same retrieved-text budget, model, and prompt
      for every approach, citing sources and recording cost.
- [ ] Trial run: answer a few questions with each approach, code the answers,
      and revise the codes.
- [ ] Full run: all ten questions through both approaches (20 answers),
      recording what comes back and what it cost.
- [ ] Code the answers and compare the two approaches.

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
- **The original-documents index.** `scripts/build_index.py` cuts each
  article's prepared text into passages of at most 200 tokens, overlapping by
  up to 25, at paragraph, then line, sentence, or word breaks. Each passage is
  labeled with its article and PDF pages and embedded with
  `BAAI/bge-small-en-v1.5` (local, through fastembed: no API key or per-call
  cost). The index and the prepared text stay local, like the PDFs.
- **Passages match the size of analysis items.** Both approaches get the same
  retrieved-text budget, so the pieces must be about the same size, or the
  approach with smaller pieces gets more of them and reaches more articles for
  that reason alone. The first trial cut passages at up to 450 tokens (mean
  386) against analysis items of mean 177: structured RAG got about twice as
  many pieces. Passages are now cut at up to 200 tokens, and the traditional
  RAG trial answers were rerun.
- **The structured-analyses index.** The same script splits each article's
  close reading into its reading-path steps (with their claims, support, and
  cited references), the claims reference into its entries (with the headings
  they sit under), and the argument evaluation into paragraphs. Each item is
  labeled with its article and kind, and embedded with the same model. An item
  over 450 tokens is split at line breaks, its location or section repeated on
  every part. Ten articles give 1,751 items: 542 close reading, 1,107 claims
  reference, 102 argument evaluation.
- **The answering step.** `scripts/answer.py` gives each answer the items
  nearest the question, in rank order, until the next would take the total
  over the budget: 4,000 tokens of item text to start, to revisit after the
  trial run (`--budget`). One Codex session per answer, on GPT-6.1 Sol at
  medium effort with the ChatGPT sign-in, as in single-source analysis, writes
  the answer from `prompts/06_answer.md`, citing items as [E1], [E2]. The
  budget, model, and prompt are the same for both approaches. Each
  answer's record keeps the retrieved items, the citations, Codex's token
  usage, and the time taken; there is no per-token cost to record.
- **Approach names.** In the scripts and the answer folders the approaches
  are `rag` (original documents) and `structured` (structured analyses). The
  indexes keep their own names: `rag` searches `source_text`, `structured`
  searches `analyses`.

## Open

- What "travel" means concretely for the literacy study: the unit that
  travels (a claim, a term, a cited study), and whether to trace specific
  lineages or compare how each corpus treats the same concept. To settle with
  the domain expert, starting with a few concepts traced by hand.
- The water experiment's test questions, and how each measure is judged.
- Whether the literacy study gets an argument analysis of each document (for
  legislation, an argument analysis of the law) alongside its discourse
  analysis, and what the experiment looks like for literacy.
- Whether the legislation PDFs, which are public domain, should be tracked.

## Status

- **Literacy:** six laws analyzed (close reading and discourse analysis), and
  the legislation codebook revised from them. Proposed new codes await
  review. Scholarly and popular press not started.
- **Water:** ten articles analyzed and accepted. Synthesis across them not
  built.
