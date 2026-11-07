# Runbook

How to run one document, explained once with California as the example, and
then each run's commands and prompts together, ready to copy.

## How it works

Run these from the repository folder:

```bash
cd ~/github/hitl-research-agent
```

**Before you start:** make sure you're on the branch and up to date.

```bash
git switch mom-research
```

```bash
git pull
```

```bash
uv sync
```

**1. Load the document.** This builds the workspace at `~/sor-workspace` with
the document as `article.pdf`, its details, the prompts, the rubric, and the
codebook. The slug comes from `data/<corpus>/sources.yaml`.

```bash
uv run python scripts/workspace.py load california_2025_ab1454
```

**2. Run the five Codex prompts.** Each one goes in a new Codex session in
`~/sor-workspace`, in order: close reading, provisions reference, judge the
close reading, discourse analysis, judge the discourse analysis. For the
pilot, code the document yourself before opening
`run/discourse_analysis.md`.

To open the workspace in the Codex app: choose the folder for the project,
press **Cmd+Shift+G** in the file window, paste `~/sor-workspace`, press
Enter, then Open.

**3. Check what was written.**

```bash
ls ~/sor-workspace/run ~/sor-workspace/references ~/sor-workspace/judgments
```

```bash
cat ~/sor-workspace/scores.md
```

**4. Save.** Add the **Accepted:** lines to `~/sor-workspace/scores.md`
first. Saving copies the results to `outputs/<corpus>/<slug>/` and removes the
workspace, ready for the next document.

```bash
uv run python scripts/workspace.py save
```

**5. Commit and push the results.**

```bash
git add outputs
```

```bash
git commit -m "Add results for california_2025_ab1454"
```

```bash
git push
```

**If a workspace is stuck** and you want to start over, this deletes it:

```bash
rm -rf ~/sor-workspace
```

---

## Runs

### 1. California AB 1454

Notes:

```bash
uv run python scripts/workspace.py load california_2025_ab1454
```

Prompt 1, close reading:

```
Follow prompts/close-reading.md. The document is article.pdf, and its source
details are in source.yaml. Write analysis.json and run_note.md to run/.
```

Prompt 2, provisions reference:

```
Hi! You're writing a reference list for judging a close reading of a
legislative text. Please start by reading RUBRIC.md, which explains the
setup, and especially its section "The provisions reference list".

This session reads the document (article.pdf, with its text in article.txt and an image of each page in pages/) on its own and writes the document's
provisions to references/claims_reference.md, as the rubric describes. A
later session judges the close reading against your list as written, so take
care that it's complete.

Please open only RUBRIC.md, article.pdf, article.txt, and pages/. Don't open anything in run/,
prompts/, or judgments/.
```

Prompt 3, judge the close reading:

```
Hi! You're judging a close reading of a legislative text. Please start by
reading RUBRIC.md, which explains the setup and the criteria, and
prompts/close-reading.md, which holds the instructions the reading followed.

Read the document (article.pdf, with its text in article.txt and an image of each page in pages/) and references/claims_reference.md, the reference list an
earlier session wrote from the document. Use it as written; don't change it.

Then open run/analysis.json and judge it against the document and the list
on A1–A5. Write the judgment to judgments/close_reading.md.

Then add your scores to scores.md in the close reading table. Leave the
Accepted line for me.

Please open only these files and scores.md. Don't read
run/discourse_analysis.md or anything in judgments/.
```

Prompt 4, discourse analysis:

```
Follow prompts/discourse-analysis.md. The document is article.pdf, its source
details are in source.yaml, the close reading is run/analysis.json, and the
codebook is CODEBOOK.md. Write discourse_analysis.md to run/ and add your
section to run/run_note.md.
```

Prompt 5, judge the discourse analysis:

```
Hi! You're judging a discourse analysis of a legislative text. Please start
by reading RUBRIC.md, which explains the setup and the criteria,
prompts/discourse-analysis.md, which holds the instructions the analysis
followed, and CODEBOOK.md.

Read the document (article.pdf, with its text in article.txt and an image of each page in pages/), then open run/discourse_analysis.md and judge it against
the document on B1–B5. Write the judgment to judgments/discourse_analysis.md.

Then add your scores to scores.md in the discourse analysis table. Leave the
Accepted line for me.

Please open only these files and scores.md. Don't read run/analysis.json,
references/claims_reference.md, or anything in judgments/.
```

```bash
uv run python scripts/workspace.py save
```

```bash
git add outputs && git commit -m "Add results for california_2025_ab1454" && git push
```

### 2. Arkansas Act 1063 (Right to Read Act, 2017)

Notes:

```bash
git pull
```

```bash
uv run python scripts/workspace.py load arkansas_2017_act1063_right_to_read
```

Prompts 1–5: the same as run 1. Before starting, check the model picker in
Codex so this run uses the same model as California.

```bash
uv run python scripts/workspace.py save
```

```bash
git add outputs && git commit -m "Add results for arkansas_2017_act1063_right_to_read" && git push
```

### 3. Arkansas Code § 6-17-429 (Right to Read Act, 2025)

Notes:

```bash
git pull
```

```bash
uv run python scripts/workspace.py load arkansas_2025_code6_17_429_right_to_read
```

Prompts 1–5: the same as run 1. Before starting, check the model picker in
Codex so this run uses the same model as California.

```bash
uv run python scripts/workspace.py save
```

```bash
git add outputs && git commit -m "Add results for arkansas_2025_code6_17_429_right_to_read" && git push
```

### 4. Ohio Revised Code 3313.6028 (Literacy curriculum)

Notes:

```bash
git pull
```

```bash
uv run python scripts/workspace.py load ohio_2026_orc3313_6028_literacy_curriculum
```

Prompts 1–5: the same as run 1. Before starting, check the model picker in
Codex so this run uses the same model as California.

```bash
uv run python scripts/workspace.py save
```

```bash
git add outputs && git commit -m "Add results for ohio_2026_orc3313_6028_literacy_curriculum" && git push
```

### 5. Georgia HB 1193 (Georgia Early Literacy Act of 2026)

Notes:

```bash
git pull
```

```bash
uv run python scripts/workspace.py load georgia_2026_hb1193_early_literacy_act
```

Prompts 1–5: the same as run 1. Before starting, check the model picker in
Codex so this run uses the same model as California.

```bash
uv run python scripts/workspace.py save
```

```bash
git add outputs && git commit -m "Add results for georgia_2026_hb1193_early_literacy_act" && git push
```

### 6. Minnesota Statutes 120B.12 (Read Act)

Notes:

```bash
git pull
```

```bash
uv run python scripts/workspace.py load minnesota_2026_120b12_read_act
```

Prompts 1–5: the same as run 1. Before starting, check the model picker in
Codex so this run uses the same model as California.

```bash
uv run python scripts/workspace.py save
```

```bash
git add outputs && git commit -m "Add results for minnesota_2026_120b12_read_act" && git push
```
