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

## This branch

A workspace branch of `hitl-research-agent` for running single-source
analyses on a set of articles. It is an orphan branch: it shares no history
with `main` and is not merged back. Changes worth keeping on `main`, such as
edits to the rubric or prompts, are carried over by hand.

```
├── data/
│   ├── scholarly/        scholarly publications, with their source details
│   ├── popular-press/    popular press
│   └── legislation/      legislation
├── evaluations/          the workspace for one article's run; see evaluations/README.md
├── outputs/              results copied out of evaluations/, per article
├── scripts/              this branch's own code, such as loading an article into evaluations/
├── src/                  the hitl_research_agent package from main, unchanged
├── prompts/              the prompt originals; evaluations/prompts/ must match them
├── docs/RUBRIC.md        the rubric original; evaluations/RUBRIC.md must match it
└── tests/                tests for src/ and the prompt and rubric copies
```

Checks: `uv run pytest` · `uv run ruff check . && uv run ruff format --check .` · `uv run mypy src`
