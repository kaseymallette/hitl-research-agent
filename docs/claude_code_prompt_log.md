# Claude Code Prompt Log

## Phase 0 — Build Plan

### Prompt 1
Read README.md and familiarize yourself with the project. Do not write or modify code yet. I want to create a separate BUILD_PLAN.md that turns the project roadmap into an engineering implementation plan. We will develop the plan collaboratively, one phase at a time. For each phase, help me identify the goal, architectural decisions, technologies, implementation tasks, tests, and acceptance criteria. Do not move to later phases or make architectural decisions without discussing them with me first.

**Response:**            
Claude proposed Phase 0 infrastructure using uv, Ruff, mypy, pre-commit, pytest, GitHub Actions, Pydantic settings, and a src/ package layout.

### Prompt 2
I made a few changes since your last pass:

- Updated docs/BUILD_PLAN.md
- Added docs/claude_code_prompt_log.md
- Updated README.md with a Project Documentation section

Please re-read those files and use the current repo state as the source of truth. Do not modify code yet. Confirm that the documentation is internally consistent, flag any conflicts or missing decisions, and then help me prepare Phase 0 for implementation.

**Response:**            
Claude found and corrected several documentation inconsistencies, including the moved README link, Hatchling configuration, `.python-version`, Python version constraints, and deferred dependencies. It also confirmed `hitl-research-agent` as the project name, `hitl_research_agent` as the Python module, and Python 3.12-only CI.

### Prompt 3
Before we begin Phase 0 implementation, I want to establish a clear approval boundary for this project.

When I ask you to review, analyze, or plan:
- Do not modify existing files.
- Do not create new files.
- Do not delete, rename, or move files.
- Do not implement proposed changes.
- Do not make architectural decisions on my behalf.

You may identify issues, recommend changes, and explain what you would do.

Present proposed changes for my review first. Only modify the repository when I explicitly approve the change or tell you to implement it.

Please confirm that you understand and will follow this boundary before we continue.

**Response:**               
Claude confirmed the approval boundary: no modifying, creating, deleting, renaming, moving, or implementing changes during review/planning without explicit approval. It also saved the rule for future project sessions.

### Prompt 4
Let’s begin Phase 0. Review Implementation Task 1 in `docs/BUILD_PLAN.md` and tell me what you propose to do.

**Response:**               
Claude proposed the Phase 0 `pyproject.toml`, including project metadata, Pydantic dependencies, uv dev dependencies, Hatchling, Ruff, and mypy configuration. It also flagged open decisions around versioning, metadata, dependency bounds, Ruff rules, and mypy strictness for approval before making changes.

### Prompt 5
I approve the proposed pyproject.toml as written. Keep version = "0.1.0", leave license and author metadata out for now, use [dependency-groups], keep the proposed Ruff rules and mypy strict = true, and use the explicit Hatchling package configuration. Implement Task 1 only.

**Response:**               
Claude created `pyproject.toml` as approved and limited the change to Task 1. It also flagged that mypy will not pass until the `src/hitl_research_agent/` package is created in a later task.