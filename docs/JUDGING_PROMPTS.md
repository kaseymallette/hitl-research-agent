# Judging Prompts

The prompts that start each judging session for one article's analysis, one
new chat per prompt, in the order below. Each session works in a folder set up
as [RUBRIC.md](RUBRIC.md) describes, with the rubric copied in.

## Setting up the folder

```
RUBRIC.md
article.pdf
prompts/
  close-reading.md
  evaluate-argument.md
run/
  analysis.json
  argument_evaluation.md
references/                      empty, or the article's existing claims list
judgments/                       empty to start
```

- Copy in `docs/RUBRIC.md` as `RUBRIC.md`, `prompts/` from the repository,
  and the article from `data/research/synthesis/` as `article.pdf`.
- Copy `analysis.json` and `argument_evaluation.md` from
  `outputs/analyses/<slug>/` into `run/`. Leave `run_note.md` out.
- **Barnett and kanbur already have a claims list,** written from the article
  alone for the A/B judging: copy
  `outputs/judgments/<barnett or kanbur>/references/claims_reference.md` into
  `references/`, and skip prompt 1. Leave their `problems_reference.md` out.

## The order

1. Claims reference list
2. Close reading
3. Argument evaluation

Run each in a new chat, so no session carries another's context. Session 1
writes the list before the close reading is judged against it. Skim it against
the article before going on: session 2 uses it as written. Session 3 doesn't
use the list, so it can run at any point.

When they're done, copy them into the article's folder in the repository,
`outputs/judgments/<article>/` (`alissa`, `alston`, `barnett`, `kanbur`,
`katakam`, `lei`, or `li`): the claims list into `references/`, and the
contents of `judgments/` into `judgments/`. Barnett and kanbur already have
their lists in `references/`, so copy only the judgments.

---

## 1. Claims reference list

```
Hi! You're writing a reference list for judging a close reading of an
academic article. Please start by reading RUBRIC.md, which explains the
setup, and especially its section "The claims reference list".

This session reads article.pdf on its own and writes the article's own claims
to references/claims_reference.md, as the rubric describes. A later session
judges the close reading against your list as written, so take care that it's
complete: cover the conclusion of every section and subsection, not only the
article's summary claims, along with every contribution, abstract claim,
figure, and table.

Please open only RUBRIC.md and article.pdf. Don't open anything in run/,
prompts/, or judgments/.
```

## 2. Close reading

```
Hi! You're judging a close reading of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the reading followed.

Read article.pdf and references/claims_reference.md, the reference list an
earlier session wrote from the article. Use it as written; don't change it.

Then open run/analysis.json and judge it against the article and the list on
A1–A5. Write the judgment to judgments/close_reading.md.

Please open only these files. Don't read run/argument_evaluation.md or
anything in judgments/.
```

## 3. Argument evaluation

```
Hi! You're judging an evaluation of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluation
followed.

Read article.pdf, then open run/argument_evaluation.md and judge it against
the article on B1–B6. There is no reference list for this session: check each
problem the evaluation raises against the article itself. Write the judgment
to judgments/evaluation.md.

Please open only these files. Don't read run/analysis.json,
references/claims_reference.md, or anything in judgments/.
```
