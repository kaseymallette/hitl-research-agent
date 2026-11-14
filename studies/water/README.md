# Water study

> Why does AI infrastructure use freshwater, and under what conditions could
> alternative cooling methods or water supplies, including desalination, reduce
> pressure on local freshwater resources?

The study distinguishes freshwater, drinking-quality water, and water suitable
for a particular process, and treats desalination as one possible supply
rather than the preferred one. A source about process-grade cooling water is
not evidence about drinking water.

This was the first case study, and the analysis harness was built on it. All
ten articles have been analyzed and accepted into the collection.

## The collection

Ten articles, listed with their provenance in
[`data/sources.yaml`](data/sources.yaml). Seven PDFs are in
[`data/`](data/) because their licenses allow sharing (open access or US
government work). Barnett-Itzhaki, Katakam, and Kanbur are
publisher-copyrighted, so their PDFs stay local and only their DOIs are
tracked.

[`outputs/collection.yaml`](outputs/collection.yaml) lists the accepted
articles with their judgment scores.

## Single-source analysis: five calls per article

Each call is its own Codex session, reading the PDF, and sees only the files
it needs, so the judges work independently. Each writes one file to
`outputs/analyses/<slug>/`:

| Call | What it does | File |
| --- | --- | --- |
| **01** Close reading | records what the author says, step by step, without judging it | `01_close_reading.json` |
| **02** Claims reference | lists the article's own claims, from the article alone | `02_claims_reference.md` |
| **03** Close reading judgment | judges 01 against the article and 02 | `03_close_reading_judgment.md` |
| **04** Argument evaluation | the model's own judgment of the argument | `04_argument_evaluation.md` |
| **05** Argument judgment | judges 04 against the article | `05_argument_judgment.md` |

In the close reading, a step's claims and support are the author's, each
marked `verbatim` or `paraphrased`; a step's moves and meaning are the
model's reading. The argument evaluation is the model's judgment. The judges
follow [`RUBRIC.md`](RUBRIC.md), and the prompts are in
[`prompts/`](prompts/).

## Run it

From the repository root:

```bash
uv run python scripts/run_single_source.py <slug>
```

With no option, the calls whose file is missing run in order. `--only 03`
reruns one call; `--revise 01` revises the close reading from its judgment
(and `--revise 04` the argument evaluation from its judgment).
