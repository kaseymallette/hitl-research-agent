# Evaluations

The workspace for running and judging one article's close reading and
argument evaluation. This folder is the template: `scripts/workspace.py load`
copies it to a folder outside the repository (`~/sor-workspace` by default), so
no session can see other runs or judgments. The prompts below are the same for
every article: only `article.pdf` and `source.yaml` change.

```
evaluations/
├── README.md                this file: the Codex prompts
├── RUBRIC.md                copy of docs/RUBRIC.md: the criteria
├── source.yaml              the article's details, written by load from data/<corpus>/sources.yaml
├── scores.md                the scores, filled in by prompts 3 and 5
├── prompts/                 copies of prompts/: the instructions for the run
│   ├── close-reading.md
│   └── evaluate-argument.md
├── article.pdf              the article, copied in by load
├── run/                     analysis.json and run_note.md (prompt 1), argument_evaluation.md (prompt 4)
├── references/              claims_reference.md, from prompt 2
└── judgments/               close_reading.md (prompt 3), evaluation.md (prompt 5)
```

`RUBRIC.md` and `prompts/` are copies; `tests/test_prompt_files.py` keeps them
identical to `docs/RUBRIC.md` and `prompts/`.

## For each article

1. Load the article by its slug in `data/<corpus>/sources.yaml`:
   `uv run python scripts/workspace.py load <slug>`. This builds the
   workspace with the article as `article.pdf` and its details in
   `source.yaml`.
2. Run prompts 1–5 in order in the workspace, each in a new Codex session, on
   GPT-6.1 Sol at medium effort. Skim the claims list against the article
   before prompt 3: the judge uses it as written.
3. Add the **Accepted:** lines to `scores.md` once you decide.
4. Save: `uv run python scripts/workspace.py save`. This copies `run/`,
   `references/`, `judgments/` and `scores.md` to
   `outputs/<corpus>/<slug>/` and removes the workspace, ready for the next
   article.

If the analysis is revised, put the revision in `run/` as `analysis.json`, run
prompt 3 again with the judgment's file name changed to
`close_reading_revised.md`, then `_2.md` and so on. Keep `scores.md` as it is:
the judge adds a column for the revision. A revised argument evaluation works
the same way with prompt 5 and `evaluation_revised.md`.

---

## 1. Close reading

```
Follow prompts/close-reading.md. The article is article.pdf, and its source
details are in source.yaml. Write analysis.json and run_note.md to run/.
```

## 2. Claims reference

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

## 3. Evaluate close reading

```
Hi! You're judging a close reading of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the reading followed.

Read article.pdf and references/claims_reference.md, the reference list an
earlier session wrote from the article. Use it as written; don't change it.

Then open run/analysis.json and judge it against the article and the list on
A1–A5. Write the judgment to judgments/close_reading.md.

Then add your scores to scores.md. If its Original column is empty, fill it
in; otherwise this is a revision, so add the next column (Revised 1, Revised
2, and so on). Give A1 as percentages, A3 as x/2, and A2 and A4 as counts. In
the second table, name your judgment file and the version judged, with its
number of claims and of verbatim claims. Leave the Accepted line for me.

Please open only these files and scores.md. Don't read
run/argument_evaluation.md or anything in judgments/.
```

## 4. Argument evaluation

```
Follow prompts/evaluate-argument.md. The article is article.pdf, its source
details are in source.yaml, and the close reading is run/analysis.json. Write
argument_evaluation.md to run/ and add your section to run/run_note.md.
```

## 5. Evaluate argument evaluation

```
Hi! You're judging an evaluation of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluation
followed.

Read article.pdf, then open run/argument_evaluation.md and judge it against
the article on B1–B6. There is no reference list for this session: check each
problem the evaluation raises against the article itself. Write the judgment
to judgments/evaluation.md.

Then add your scores to scores.md, in the argument evaluation tables. If its
Original column is empty, fill it in; otherwise this is a revision, so add the
next column (Revised 1, Revised 2, and so on). Give B1–B5 as x/2, B6 as the
problems confirmed out of those raised, and the errors as a count. In the
second table, name your judgment file and the version judged. Leave the
Accepted line for me.

Please open only these files and scores.md. Don't read run/analysis.json,
references/claims_reference.md, or anything in judgments/.
```
