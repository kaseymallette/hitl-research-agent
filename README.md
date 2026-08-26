# hitl-research-agent
A human-in-the-loop agentic AI research system built with Claude Code, LangChain, and DeepEval for grounded source analysis, evaluation, evidence synthesis, and researcher-directed inquiry.

> A research system designed to increase the amount and quality of evidence a human researcher can reason over without replacing human judgment.

## Overview

 The Human-in-the-Loop Research Agent is a reusable AI research system for conducting structured technical research.

The system is designed to handle the expensive preparatory work:

**retrieve → analyze → evaluate → store → synthesize**

The human remains responsible for:

**interpretation → inference → deciding what matters → choosing the next research direction**

Rather than building a fully autonomous research agent, this project treats human oversight as part of the architecture. Every research run is explicitly initiated by a human, operates within defined limits, and returns control at meaningful decision points.

## Project Documentation

- [Build Plan](docs/BUILD_PLAN.md)
- [Claude Code Prompt Log](docs/claude_code_prompt_log.md)

## Core Principle

The system follows a simple design philosophy:

> **Human-directed, agent-executed research.**

The agent can search, process sources, reconstruct arguments, map evidence, evaluate its own outputs, and organize findings across sources.

It does not decide what should be researched next or what the evidence ultimately means.

Those decisions remain with the researcher.

## Research Workflow

The long-term workflow is:

```text
Research Question
      ↓
Source Retrieval
      ↓
Structured Analysis
      ↓
Evaluation
      ↓
Human Review
      ↓
Accepted Research Store
      ↓
Cross-Source Synthesis
      ↓
Human Interpretation
      ↓
Next Research Question
```

Human checkpoints are intentional parts of the system rather than emergency overrides.

## Structured Source Analysis

The system does more than summarize documents.

Each source is converted into a structured research representation containing information such as:

- research problem
- central claims
- supporting evidence
- methodology
- author-stated assumptions
- model-inferred assumptions
- acknowledged limitations
- model-inferred limitations
- proposed solutions
- open questions
- source-level provenance

Model interpretation is kept separate from claims made directly by the source.

The goal is **argument reconstruction and evidence extraction**, not generic summarization.

## Evaluation

AI-generated research analysis is evaluated before it is accepted into the research knowledge base.

The project uses **DeepEval** to evaluate behaviors including:

- faithfulness to source material
- citation faithfulness
- argument reconstruction
- evidence mapping
- assumption discipline
- limitation discipline
- inference control
- research usefulness

The first version uses automated evaluation together with human spot checks rather than requiring a manually annotated gold dataset.

## Human Review

After analysis and evaluation, the researcher reviews:

- structured source analysis
- supporting citations
- evaluation scores
- evaluation explanations
- flagged problems

The researcher can then:

**accept → reject → revise → rerun**

Only accepted analyses become part of the research knowledge base.

## MVP Research Question

Development begins with one deliberately narrow question:

> **Why do AI data centers use freshwater, and where is that water actually used?**

The small scope provides a real research problem while keeping the initial engineering work manageable.

Once the research system is working, the broader investigation can expand toward:

> **How could we build AI better?**

Future research may branch into cooling systems, water consumption, compute architecture, energy, materials, infrastructure, regulation, and other questions identified through the evidence.

## Planned Technical Stack

The initial implementation will use:

- **Python** — core application language
- **LangChain** — model integration and structured AI operations
- **OpenAI API** — initial model provider
- **Pydantic** — structured research schemas and validation
- **DeepEval** — evaluation framework
- **Git + GitHub** — version control and project history
- **Claude Code** — AI-assisted development
- **uv** — dependency management and virtual environments
- **Ruff** — linting and formatting
- **mypy** — static type checking
- **pre-commit** — git hooks enforcing lint/type checks before commit
- **GitHub Actions** — continuous integration

Later phases will introduce:

- **RAG and embeddings** for retrieving accepted prior research
- **retrieval evaluation** for measuring RAG quality
- **LangGraph** for stateful orchestration, bounded execution, and human approval checkpoints

The project intentionally adds these capabilities incrementally rather than beginning with a fully agentic architecture.

## Development Roadmap

### Phase 0 — Getting Started

Set up the repository, development environment, Claude Code workflow, project documentation, and implementation plan.

### Phase 1 — Research Data Model

Define and validate the structured representations used for sources, claims, evidence, assumptions, limitations, methodology, provenance, and analysis results.

### Phase 2 — Single-Source Analysis

Use an LLM to convert individual research sources into validated structured research representations.

### Phase 3 — Evaluation

Add DeepEval faithfulness, citation evaluation, and custom research-specific evaluation metrics.

### Phase 4 — Human Review

Build the accept, reject, revise, and rerun checkpoint that determines which analyses enter the research store.

### Phase 5 — Cross-Source Synthesis

Compare accepted sources to identify agreement, disagreement, methodological differences, proposed solutions, evidence strength, and research gaps.

### Phase 6 — Research Knowledge Base and RAG

Store accepted research, add embeddings, and retrieve relevant prior evidence for new research questions.

### Phase 7 — Retrieval Evaluation

Evaluate whether the RAG system retrieves the correct evidence separately from whether the model generates a faithful synthesis.

### Phase 8 — LangGraph Orchestration

Convert the working pipeline into a stateful human-in-the-loop research agent with approval checkpoints, retries, persistence, and explicit resource limits.

## Project Status

**Current stage: Phase 0 — Getting Started**

The project is currently being designed and initialized. The research architecture has been defined, and implementation will proceed incrementally so that each component can be tested before additional agentic behavior is introduced.

## Development Setup

**Prerequisites:** [uv](https://docs.astral.sh/uv/) (manages the Python 3.12 interpreter automatically — no separate Python install needed) and git 2.31 or later (required for `pre-commit` compatibility).

1. Install `uv`:
   ```bash
   brew install uv
   ```
   (See the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) for non-Homebrew options.)

2. Install dependencies and create the virtual environment:
   ```bash
   uv sync
   ```

3. Install git hooks (runs ruff and mypy automatically on commit):
   ```bash
   uv run pre-commit install
   ```

### Running checks locally

```bash
uv run pytest                       # run tests
uv run ruff check .                 # lint
uv run ruff format --check .        # check formatting
uv run mypy src                     # type-check
uv run pre-commit run --all-files   # run all hooks against the whole repo
```

## Why This Project

Most descriptions of AI research assistants focus on how much autonomy can be given to the model.

This project asks a different question:

**How much useful research work can AI perform while preserving human control over interpretation, inference, and intellectual direction?**

The goal is not to replace the researcher.

The goal is to build a better research instrument.