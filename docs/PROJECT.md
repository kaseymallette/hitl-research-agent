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
- **Analyses run in separate Codex sessions, reading the PDF.** The scholarly
  runner uses GPT-6.1 Sol at medium effort with API billing, replacing
  ChatGPT-plan authentication. It requires `OPENAI_API_KEY` or `CODEX_API_KEY`;
  `OPENAI_API_KEY` takes precedence and is passed as `CODEX_API_KEY` to Codex.
  Each session sees only the files its step needs.
- **Legislation uses the workspace workflow.** `scripts/workspace.py` loads
  a law's PDF, extracted text, and page images into an external workspace.
  The close reading, claims reference, discourse analysis, and two judgments
  run there in Codex. Saving copies the results to
  `studies/science_of_reading/outputs/legislation/<slug>/`.
- **Scholarly articles test whether close reading gives better answers; laws
  get a discourse analysis.** `scripts/run_scholarly.py` runs five Codex
  sessions per article using the study's `harness/scholarly/prompts/`, writing
  to `studies/science_of_reading/outputs/scholarly/<slug>/`: a claims reference,
  Method A's baseline answers, Method B's close reading and answers, and scoring.
  The reference sees neither the questions nor the answers. Method A reads the
  article alone; Method B answers from the article and close reading. Every
  step reads the article, and both methods quote its exact words. The
  legislation codebook is not used for articles.
- **Precision and recall measure the two methods.** Precision is exact, real,
  relevant quotations divided by total quotations. Recall is relevant claims
  used divided by total relevant claims. Both are scored for each question
  against the claims reference, supplemented with relevant claims it missed.
  Null hypothesis: Method B is no better than Method A.
- **Source PDFs stay local.** Only their `sources.yaml` entries are tracked.
- **The saved cross-document answers currently cover legislation.** The
  expert's three questions are answered from the six laws' close readings and
  discourse analyses in `studies/science_of_reading/questions/`. The scholarly
  harness answers the questions separately for each article.

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
- **Scholarly:** running the harness on the scholarly articles.
- **Popular press:** not started.

Earlier work (the water study and the retrieval experiments) is kept in git
history and on the `wip-2026-11-25` branch.
