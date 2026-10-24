# Judging Prompts

The prompts that start each judging session, one new chat per prompt, in the
order below. Each session works in a folder set up as
[RUBRIC.md](RUBRIC.md) describes, with the rubric copied in, and writes its
judgment to `judgments/`.

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

1. Close reading, first run (run A)
2. Close reading, each further run (once per run: B, C, …)
3. Close readings, head to head
4. Evaluation, first run (run A)
5. Evaluation, each further run (once per run: B, C, …)
6. Evaluations, head to head

For two runs that's six sessions: 1, 2 for B, 3, 4, 5 for B, and 6. Run each
in a new chat, so no session carries another's context. Sessions 1 and 4 must
come before the others in their half, since they write the reference lists.

When they're done, copy `judgments/` into
`outputs/judgments/<experiment>/` in the repository, under the experiment's
name in the key.

In prompts 2 and 5, replace `<RUN>` with the run's letter.

---

## 1. Close reading, first run

```
Hi! You're judging close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session judges run A's close reading. Before you open any run, read
article.pdf on its own and write the article's own claims to
judgments/claims_reference.md, as the rubric describes. Later sessions will
use your list as written, so take care that it's complete.

Then open runs/A/analysis.json and judge it against the article and your
list on A1–A5. Write the judgment to judgments/close_reading_A.md.

Please open only these files. Don't read any argument evaluation or other
run.
```

## 2. Close reading, each further run

```
Hi! You're judging close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session judges run <RUN>'s close reading. Read article.pdf and
judgments/claims_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open runs/<RUN>/analysis.json and judge it against the article and the
list on A1–A5. Write the judgment to judgments/close_reading_<RUN>.md.

Please open only these files. Don't read any other judgment, argument
evaluation, or run.
```

## 3. Close readings, head to head

```
Hi! You're comparing close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session compares every run's close reading head to head. Read
article.pdf and judgments/claims_reference.md, then the analysis.json in each
folder under runs/.

Compare them as the rubric's "Comparing head to head" describes, using A1–A5
as the grounds, and write the comparison to
judgments/close_reading_head_to_head.md.

Please don't read the other judgments in judgments/ or any argument
evaluation. Your ranking should be your own.
```

## 4. Evaluation, first run

```
Hi! You're judging evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session judges run A's argument evaluation. Before you open any run,
read article.pdf on its own and write the problems in its argument to
judgments/problems_reference.md, as the rubric describes. Later sessions will
use your list as written, so take care that it's complete.

Then open run A's argument evaluation in runs/A/ and judge it against the
article and your list on B1–B6. Write the judgment to
judgments/evaluation_A.md.

Please open only these files. Don't read any close reading, other judgment,
or other run.
```

## 5. Evaluation, each further run

```
Hi! You're judging evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session judges run <RUN>'s argument evaluation. Read article.pdf and
judgments/problems_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open run <RUN>'s argument evaluation in runs/<RUN>/ and judge it against
the article and the list on B1–B6. Write the judgment to
judgments/evaluation_<RUN>.md.

Please open only these files. Don't read any other judgment, close reading,
or run.
```

## 6. Evaluations, head to head

```
Hi! You're comparing evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session compares every run's argument evaluation head to head. Read
article.pdf and judgments/problems_reference.md, then the argument evaluation
in each folder under runs/.

Compare them as the rubric's "Comparing head to head" describes, using B1–B6
as the grounds, and write the comparison to
judgments/evaluation_head_to_head.md.

Please don't read the other judgments in judgments/ or any close reading.
Your ranking should be your own.
```
