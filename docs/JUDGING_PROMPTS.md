# Judging Prompts

The prompts that start each judging session, one new chat per prompt, in the
order below. Each experiment compares two runs, A and B. Each session works in
a folder set up as [RUBRIC.md](RUBRIC.md) describes, with the rubric copied
in. The reference lists are kept in `references/`, and each judgment is
written to `judgments/`.

## Setting up the folder

```
RUBRIC.md
article.pdf
prompts/
  close-reading.md
  evaluate-argument.md
runs/
  A/
    analysis.json
    argument_evaluation.json
  B/
    analysis.json
    argument_evaluation.json
references/                      the two reference lists
judgments/                       empty to start
```

- Copy the runs in under letters, with nothing in a file or folder name that
  says how a run was made. Rename an evaluation file if it needs it, such as
  `argument_evaluation_2.json`.
- Record which letter is which in [EVALUATION_KEY.md](EVALUATION_KEY.md),
  here, and never put it in the folder.
- Copy `prompts/` from the repository so the judge can see the instructions
  the runs followed.

## The order

1. Claims reference list
2. Close reading, run A
3. Close reading, run B
4. Close readings, A and B head to head
5. Problems reference list
6. Evaluation, run A
7. Evaluation, run B
8. Evaluations, A and B head to head

Run each in a new chat, so no session carries another's context. Sessions 1
and 5 write the reference lists before any run is judged against them.
Check each list against your own reading before going on: every later
session uses it as written.

When they're done, copy `judgments/` into
`outputs/judgments/<article>/<experiment>/` in the repository, under the
experiment's name in the key, and `references/` into
`outputs/judgments/<article>/references/`.

### Later experiments on the same article

The reference lists are written once per article, in its first experiment,
and every later experiment on that article uses the same two, so all of its
runs are judged against the same lists.

- Before starting, copy `outputs/judgments/<article>/references/` into the
  new folder as `references/`, and skip prompts 1 and 5.
- Copy only `judgments/` back; the article's folder already has the lists.

### A final with two sessions

From Kanbur's final on, a final runs only prompts 4 and 8, each in two
sessions with the letters swapped: session 1 with one champion under A,
session 2 with the other. Before each session, empty `judgments/` or move the
earlier file out, and afterwards rename the judgment by its session, such as
`close_reading_head_to_head_1.md` and `_2.md`. A configuration wins a
head-to-head only if it wins both sessions; a split is a tie.

---

## 1. Claims reference list

```
Hi! You're writing a reference list for judging close readings of an academic
article. Please start by reading RUBRIC.md, which explains the setup, and
especially its section "The reference lists".

This session reads article.pdf on its own and writes the article's own claims
to references/claims_reference.md, as the rubric describes. Every later
session judges the close readings against your list as written, so take care
that it's complete: cover the conclusion of every section and subsection, not
only the article's summary claims, along with every contribution, abstract
claim, figure, and table.

Please open only RUBRIC.md and article.pdf. Don't open anything in runs/,
prompts/, or judgments/.
```

## 2. Close reading, run A

```
Hi! You're judging close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session judges run A's close reading. Read article.pdf and
references/claims_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open runs/A/analysis.json and judge it against the article and the list
on A1–A5. Write the judgment to judgments/close_reading_A.md.

Please open only these files. Don't read any other judgment, argument
evaluation, or run B.
```

## 3. Close reading, run B

```
Hi! You're judging close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session judges run B's close reading. Read article.pdf and
references/claims_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open runs/B/analysis.json and judge it against the article and the list
on A1–A5. Write the judgment to judgments/close_reading_B.md.

Please open only these files. Don't read any other judgment, argument
evaluation, or run A.
```

## 4. Close readings, head to head

```
Hi! You're comparing close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session compares runs A and B's close readings head to head. Read
article.pdf and references/claims_reference.md, then runs/A/analysis.json and
runs/B/analysis.json.

Compare them as the rubric's "Comparing head to head" describes, using A1–A5
as the grounds, and write the comparison to
judgments/close_reading_head_to_head.md.

Please don't read the other judgments in judgments/ or any argument
evaluation. Your verdict should be your own.
```

## 5. Problems reference list

```
Hi! You're writing a reference list for judging evaluations of an academic
article's argument. Please start by reading RUBRIC.md, which explains the
setup, and especially its section "The reference lists".

This session reads article.pdf on its own and writes the problems in its
argument to references/problems_reference.md, as the rubric describes. Every
later session judges the evaluations against your list as written, so take
care that it's complete: work through the whole article, checking its
reasoning, its numbers, and whether its conclusions follow from its evidence.

Please open only RUBRIC.md and article.pdf. Don't open anything in runs/,
prompts/, or judgments/, or references/claims_reference.md.
```

## 6. Evaluation, run A

```
Hi! You're judging evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session judges run A's argument evaluation. Read article.pdf and
references/problems_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open runs/A/argument_evaluation.json and judge it against the article
and the list on B1–B6. Write the judgment to judgments/evaluation_A.md.

Please open only these files. Don't read any other judgment, close reading,
or run B.
```

## 7. Evaluation, run B

```
Hi! You're judging evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session judges run B's argument evaluation. Read article.pdf and
references/problems_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open runs/B/argument_evaluation.json and judge it against the article
and the list on B1–B6. Write the judgment to judgments/evaluation_B.md.

Please open only these files. Don't read any other judgment, close reading,
or run A.
```

## 8. Evaluations, head to head

```
Hi! You're comparing evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session compares runs A and B's argument evaluations head to head. Read
article.pdf and references/problems_reference.md, then
runs/A/argument_evaluation.json and runs/B/argument_evaluation.json.

Compare them as the rubric's "Comparing head to head" describes, using B1–B6
as the grounds, and write the comparison to
judgments/evaluation_head_to_head.md.

Please don't read the other judgments in judgments/ or any close reading.
Your verdict should be your own.
```
