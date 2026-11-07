# Runbook

Copy-paste commands for running one document through the workspace, and a log
of what was run. Run the commands from the repository folder unless a step
says otherwise.

## Get set up

```bash
cd ~/github/hitl-research-agent
```

```bash
git switch mom-research
```

```bash
git pull
```

```bash
uv sync
```

## Run one document

### 1. Load it

Pick the document's slug from `data/<corpus>/sources.yaml`.

```bash
uv run python scripts/workspace.py load california_2025_ab1454
```

```bash
uv run python scripts/workspace.py load arkansas_2023_sb294_learns_act
```

### 2. Open the workspace

```bash
open ~/sor-workspace
```

```bash
cat ~/sor-workspace/README.md
```

The workspace README holds the Codex prompts, numbered in order. Start each
one in a new Codex session in `~/sor-workspace`.

For the pilot: code the document yourself before opening
`run/discourse_analysis.md`.

### 3. Check what was written

```bash
ls ~/sor-workspace/run ~/sor-workspace/references ~/sor-workspace/judgments
```

```bash
cat ~/sor-workspace/scores.md
```

### 4. Save it

Add the **Accepted:** lines to `~/sor-workspace/scores.md` first.

```bash
uv run python scripts/workspace.py save
```

This copies the results to `outputs/<corpus>/<slug>/` and removes the
workspace, ready for the next document.

### 5. Commit and push the results

```bash
git add outputs
```

```bash
git commit -m "Add results for california_2025_ab1454"
```

```bash
git push
```

## If something goes wrong

A workspace is already loaded and you want to start over (this deletes its
contents):

```bash
rm -rf ~/sor-workspace
```

Run the checks:

```bash
uv run pytest
```

## Log

One row per step you run. Add the date, the document, the prompt number or
command, and anything worth remembering.

| Date | Document | Step | Notes |
| --- | --- | --- | --- |
| | | | |
