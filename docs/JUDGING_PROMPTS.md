# Judging Prompts

The prompts that start each judging session, one new chat per prompt, in the
order below. Each experiment compares two runs, A and B. Each session works in
a folder set up as [RUBRIC.md](RUBRIC.md) describes, with the rubric copied
in, and writes its judgment to `judgments/`.

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

1. Close reading, run A
2. Close reading, run B
3. Close readings, A and B head to head
4. Evaluation, run A
5. Evaluation, run B
6. Evaluations, A and B head to head

Run each in a new chat, so no session carries another's context. Sessions 1
and 4 come first in their half, since they write the reference lists.

When they're done, copy `judgments/` into
`outputs/judgments/<experiment>/` in the repository, under the experiment's
name in the key.

### Later experiments on the same article

The reference lists are written once per article, in its first experiment,
and every later experiment on that article uses the same two, so all of its
runs are judged against the same lists.

- Before starting, copy `claims_reference.md` and `problems_reference.md`
  from the first experiment's folder in `outputs/judgments/` into the new
  folder's `judgments/`. Prompts 1 and 4 find them there and use them instead
  of writing new ones.
- When copying `judgments/` back, leave out the two lists; they stay in the
  first experiment's folder.

---

## 1. Close reading, run A

```
Hi! You're judging close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session judges run A's close reading. First, check for
judgments/claims_reference.md. If it's there, an earlier session wrote it from
the article: read article.pdf and the list, and use the list as written,
without changing it. If it isn't, read article.pdf on its own, before you open
any run, and write the article's own claims to judgments/claims_reference.md,
as the rubric describes. Later sessions will use your list as written, so take
care that it's complete.

Then open runs/A/analysis.json and judge it against the article and the list
on A1–A5. Write the judgment to judgments/close_reading_A.md.

Please open only these files. Don't read any argument evaluation or run B.
```

## 2. Close reading, run B

```
Hi! You're judging close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session judges run B's close reading. Read article.pdf and
judgments/claims_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open runs/B/analysis.json and judge it against the article and the list
on A1–A5. Write the judgment to judgments/close_reading_B.md.

Please open only these files. Don't read any other judgment, argument
evaluation, or run A.
```

## 3. Close readings, head to head

```
Hi! You're comparing close readings of an academic article. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the readings followed.

This session compares runs A and B's close readings head to head. Read
article.pdf and judgments/claims_reference.md, then runs/A/analysis.json and
runs/B/analysis.json.

Compare them as the rubric's "Comparing head to head" describes, using A1–A5
as the grounds, and write the comparison to
judgments/close_reading_head_to_head.md.

Please don't read the other judgments in judgments/ or any argument
evaluation. Your verdict should be your own.
```

## 4. Evaluation, run A

```
Hi! You're judging evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session judges run A's argument evaluation. First, check for
judgments/problems_reference.md. If it's there, an earlier session wrote it
from the article: read article.pdf and the list, and use the list as written,
without changing it. If it isn't, read article.pdf on its own, before you open
any run, and write the problems in its argument to
judgments/problems_reference.md, as the rubric describes. Later sessions will
use your list as written, so take care that it's complete.

Then open runs/A/argument_evaluation.json and judge it against the article
and the list on B1–B6. Write the judgment to judgments/evaluation_A.md.

Please open only these files. Don't read any close reading, other judgment,
or run B.
```

## 5. Evaluation, run B

```
Hi! You're judging evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session judges run B's argument evaluation. Read article.pdf and
judgments/problems_reference.md, the reference list an earlier session wrote
from the article. Use it as written; don't change it.

Then open runs/B/argument_evaluation.json and judge it against the article
and the list on B1–B6. Write the judgment to judgments/evaluation_B.md.

Please open only these files. Don't read any other judgment, close reading,
or run A.
```

## 6. Evaluations, head to head

```
Hi! You're comparing evaluations of an academic article's argument. Please
start by reading RUBRIC.md, which explains the setup and the criteria, and
prompts/evaluate-argument.md, which holds the instructions the evaluations
followed.

This session compares runs A and B's argument evaluations head to head. Read
article.pdf and judgments/problems_reference.md, then
runs/A/argument_evaluation.json and runs/B/argument_evaluation.json.

Compare them as the rubric's "Comparing head to head" describes, using B1–B6
as the grounds, and write the comparison to
judgments/evaluation_head_to_head.md.

Please don't read the other judgments in judgments/ or any close reading.
Your verdict should be your own.
```
