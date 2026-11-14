# hitl-research-agent

AI-assisted close reading of research documents, with a human deciding what
counts, applied to two case studies.

| Study | Question | Status |
| --- | --- | --- |
| [**Literacy**](studies/literacy/) | How is the science of reading defined, simplified, and contested as it moves from scholarship, through the popular press, into state legislation? | Legislation trial run done (six laws); scholarly and popular press next |
| [**Water**](studies/water/) | Why does AI infrastructure use freshwater, and when could other cooling methods or water supplies, including desalination, reduce pressure on local freshwater? | Ten articles analyzed and accepted |

The literacy study is a collaboration with a professor of literacy education.
The water study came first and is where the harness was built.

Both studies do the same core work: take the claims out of individual
documents, then compare them across documents. Water compares what sources
claim about one question. Literacy traces how claims change as they travel
between corpora. A question shared by both: does a structured close reading
help find and compare those claims, compared with working from the documents'
text directly?

What we're doing, why, and what's been decided is in
[`docs/PROJECT.md`](docs/PROJECT.md).

## Layout

```
├── docs/
│   ├── PROJECT.md                 the questions, current decisions, and status
│   └── ENGINEERING_DIRECTIVES.md  the coding baseline
├── studies/
│   ├── literacy/                  three corpora, codebooks, rubrics, prompts, results
│   └── water/                     sources, prompts, rubric, accepted analyses
├── scripts/
│   ├── run_single_source.py       water: five Codex calls per article
│   ├── workspace.py               literacy: load a source into the Codex workspace, save its results
│   └── prepare_sources.py         extracts a PDF's text, tables, and figure crops
├── src/hitl_research_agent/       the data models and input handling prepare_sources.py uses
└── tests/
```

Earlier work (the A/B experiments, the decision records, the prompt log, and
the API pipeline) is on the `v2` branch. The literacy study was developed on
the `mom-research` branch, kept as a record.

## Setup and checks

```bash
uv sync
```

```bash
uv run pytest
```

```bash
uv run ruff check . && uv run ruff format --check .
```

```bash
uv run mypy src
```
