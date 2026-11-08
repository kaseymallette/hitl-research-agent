# mom-research

My mom is a professor of literacy education at Binghamton University. We are
doing a collaborative study combining her scholarship and content knowledge in
literacy education with my technical expertise in AI/ML engineering. The
purpose of this study is to examine how the science of reading is defined and
enacted across three corpora (i.e., scholarly publications, popular press, and legislation).

## Research goals

Scholarship is where the science of reading is defined, because science is
research. From there, it makes its way through the popular press into
legislation. In research, the science of reading is broad and expansive: the
idea that there is a scientific basis for how we teach reading. By the time it
reaches legislation, it is often reduced to simplified directives such as
"phonics first" or "don't use the three-cueing system," and it is defined and
enacted in other unexpected ways. Our goal is to trace that pathway and
understand where things are lost in translation.

## The study

Working title: *Science by Other Means: Reading Research, Legislative
Mandates, and the Spaces Between*

The study examines how the science of reading is constructed, simplified, and
contested as it travels from peer-reviewed research, through the popular
press, into state legislation. It does not evaluate whether any approach to
reading instruction is effective. It analyzes the discourse through which
claims about the science of reading are authorized, legitimated, and
institutionalized, and what is reduced at each step.

It draws on:

- **Critical policy analysis** (Bacchi, 2009; Ball, 1993): policy as a text
  that produces the problem it claims to solve.
- **Translation theory** (Latour, 1987; Callon, 1986; Coburn, 2006; Honig,
  2006): research changes meaning as it moves into new institutional contexts.
- **Critical discourse analysis** (Fairclough, 2003; Rogers, 2011): the
  analytic method, applied across all three corpora.

## Legislation: trial run

Five states, with Arkansas at two points in time. Details for each are in
`data/legislation/sources.yaml`, and the commands for each run are in
`RUNBOOK.md`.

| Run | Source | Form | Pages | Date |
| --- | --- | --- | --- | --- |
| 1 | California AB 1454 | bill as signed into law (chaptered) | 4 | Oct 9, 2025 |
| 2 | Arkansas Act 1063 (Right to Read Act) | original act | 3 | Apr 6, 2017 |
| 3 | Arkansas Code § 6-17-429 (Right to Read Act) | code section, from Justia | 18 | 2025 edition |
| 4 | Ohio Revised Code 3313.6028, 3313.608, 3319.2310 | three code sections, printed from the state site | 19 | Oct 9, 2026 |
| 5 | Georgia HB 1193 (Georgia Early Literacy Act of 2026) | bill as passed | 42 | signed May 5, 2026 |
| 6 | Minnesota Statutes 120B.118–120B.124 (Read Act) | code sections, official state statutes | 17 | 2026 edition |

### Results

| Run | Source | Close reading | Discourse analysis |
| --- | --- | --- | --- |
| 1 | California AB 1454 | [analysis.json](outputs/legislation/california_2025_ab1454/run/analysis.json) | [discourse_analysis.md](outputs/legislation/california_2025_ab1454/run/discourse_analysis.md) |
| 2 | Arkansas Act 1063 (2017) | [analysis.json](outputs/legislation/arkansas_2017_act1063_right_to_read/run/analysis.json) | [discourse_analysis.md](outputs/legislation/arkansas_2017_act1063_right_to_read/run/discourse_analysis.md) |
| 3 | Arkansas Code § 6-17-429 (2025) | [analysis.json](outputs/legislation/arkansas_2025_code6_17_429_right_to_read/run/analysis.json) | [discourse_analysis.md](outputs/legislation/arkansas_2025_code6_17_429_right_to_read/run/discourse_analysis.md) |
| 4 | Ohio Revised Code 3313.6028, 3313.608, 3319.2310 | [analysis.json](outputs/legislation/ohio_2026_literacy_code/run/analysis.json) | [discourse_analysis.md](outputs/legislation/ohio_2026_literacy_code/run/discourse_analysis.md) |
| 5 | Georgia HB 1193 (2026) | [analysis.json](outputs/legislation/georgia_2026_hb1193_early_literacy_act/run/analysis.json) | [discourse_analysis.md](outputs/legislation/georgia_2026_hb1193_early_literacy_act/run/discourse_analysis.md) |
| 6 | Minnesota Read Act, 120B.118–120B.124 | [analysis.json](outputs/legislation/minnesota_2026_120b118_124_read_act/run/analysis.json) | [discourse_analysis.md](outputs/legislation/minnesota_2026_120b118_124_read_act/run/discourse_analysis.md) |

### Codebook

The [codebook](docs/CODEBOOK.md) sets out the codes for the five CDA
dimensions: LEX (lexical choices and definitional framing), PRE
(presuppositions), FOS (foregrounding and silencing), SUB (subject
positioning), and INT (intertextuality).

It began as a preliminary framework, compiled in February 2026 from initial
research on state science of reading legislation: 33 codes across the five
dimensions, each illustrated with excerpts from state laws. The trial runs
were then used to revise it:

- **Coded with the codebook.** Each of the six texts was coded on the five
  dimensions, and a separate session checked every observation against the
  law and judged whether its code fit.
- **Examples from the trial.** The codebook's examples are now the trial's
  113 coded passages, each quoted from the law and checked against its text.
  The preliminary examples, and other material whose sources couldn't be
  traced, were removed.
- **Codes kept as written.** The 33 codes and their definitions are
  unchanged.
- **Proposed changes, in draft.** Seven new codes are proposed for the 21
  observations no existing code fit, and five clarifications for the code
  assignments the judges found didn't fit. Both await review.

The [trial run matrix](docs/CODEBOOK.md#trial-run-matrix) shows which codes
each text received.

## This branch

A workspace branch of `hitl-research-agent` for running single-source
analyses on a set of articles. It is an orphan branch: it shares no history
with `main` and is not merged back. Changes worth keeping on `main`, such as
edits to the rubric or prompts, are carried over by hand.

```
├── RUNBOOK.md            copy-paste commands for running a document, and a run log
├── data/
│   ├── scholarly/        scholarly publications, with their source details
│   ├── popular-press/    popular press
│   └── legislation/      legislation
├── evaluations/          the workspace template and Codex prompts; see evaluations/README.md
├── outputs/              saved results, per corpus and article: outputs/<corpus>/<slug>/
├── scripts/
│   └── workspace.py      loads an article into the workspace and saves its results to outputs/
├── src/                  the hitl_research_agent package from main, unchanged
├── prompts/              the prompt originals; evaluations/prompts/ must match them
│   └── legislation/      draft legislation workspace: close reading, five-dimension discourse analysis, guide, scores
├── docs/
│   ├── CODEBOOK.md       the CDA codebook for the legislation corpus: codes and coded excerpts
│   ├── RUBRIC.md         the rubric original; evaluations/RUBRIC.md must match it
│   └── RUBRIC_LEGISLATION.md   draft rubric for legislative texts
└── tests/                tests for src/ and the prompt and rubric copies
```

Checks: `uv run pytest` · `uv run ruff check . && uv run ruff format --check .` · `uv run mypy src`
