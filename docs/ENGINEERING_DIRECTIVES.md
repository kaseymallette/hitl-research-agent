# DSA & SWE Engineering Directives

**Purpose:** Favor correct, comprehensible, resource-conscious Python implementations. Keep design proportional to demonstrated requirements. These directives guide implementation and review; they are not a checklist of patterns to introduce.

## 1. Trust Function Contracts

Internal functions operate on documented types, preconditions, and invariants. Validate untrusted input at system boundaries, then avoid repeating `isinstance` checks, broad `try/except` blocks, and silent fallback defaults through the internal call chain. Handle expected failure explicitly; allow violated programmer assumptions to fail visibly.

## 2. Representation Before Control Flow

Choose the data structure before writing branching logic. Consider `set` for membership, `dict` for keyed access, `deque` for queues, `heapq` for prioritized work, and explicit trees or adjacency maps for relationships. Prefer a representation that simplifies the algorithm over additional flags, helper layers, or conditionals. Account for ordering, duplication, and mutation semantics.

## 3. No Speculative Abstraction

Implement the current requirements, not hypothetical variants. Avoid wrapper classes, registries, factories, and configurable frameworks without a concrete need. Introduce an interface or abstraction when it protects a meaningful boundary, enforces an invariant, or eliminates actual duplication, even if there is only one implementation. Prefer direct Python functions and standard-library facilities by default.

## 4. Complexity and Allocation Discipline

Understand asymptotic time and auxiliary space for nontrivial algorithms. Consider input scale, copying, repeated scans, recursion depth, and materialized intermediate collections. Prefer clear code over speculative micro-optimization. Document complexity where it influences design or review; benchmark or profile before claiming a practical performance improvement. State complexity accurately for the selected Python implementation.

## 5. Make Invariants Explicit

Identify the property that must remain true across each loop, recursive call, or state transition. Ensure base cases, termination conditions, and boundary behavior are deliberate. When a function relies on sorted input, monotonic progress, uniqueness, or a stable identifier, encode or document that assumption at the appropriate boundary. Do not mask invariant violations with recovery logic.

## 6. Use the Right Traversal Model

Match traversal to structure: iteration for linear sequences, explicit stacks or recursion for nested structures, BFS for level-ordered exploration, DFS for reachability and dependency analysis, and topological order for acyclic dependencies. Choose recursion only when its structure improves clarity and realistic depth is safe in Python. Detect cycles where the model permits them.

## 7. Keep State and Side Effects Contained

Prefer functions with explicit inputs and outputs for transformations and algorithmic decisions. Confine I/O, mutation, caching, retries, and external API calls to identifiable boundaries. Avoid hidden global state and incidental mutation of caller-owned data. Where mutation is intentional, make ownership and lifecycle clear.

## 8. Separate Policy From Mechanism

Keep domain decisions separate from parsing, persistence, transport, and orchestration. A function should have a coherent responsibility and an interface that exposes only what callers need. Avoid both monolithic pipelines and fragmentation into one-line wrappers. Design module boundaries around real changes and dependencies, not arbitrary file-size rules.

## 9. Test Properties and Failure Modes

Test observable behavior, contracts, and invariants rather than implementation trivia. Cover empty and singleton inputs, nested or cyclic structures when applicable, duplicate values, ordering, boundary conditions, and expected failures. Use integration tests at external boundaries. Prefer deterministic tests and focused fixtures; add property-based tests when general invariants matter more than individual examples.

## 10. Make Failure and Resource Behavior Deliberate

Differentiate programmer errors, invalid external data, transient infrastructure failures, and permanent failures. Catch exceptions only where a meaningful action can be taken; preserve causes and context. Bound retries, queues, concurrency, and memory where realistic workloads demand it. Instrument consequential operations without logging sensitive payloads or flooding normal execution paths.

## Applying These Directives

For a substantive change, evaluate the relevant directives, implement the simplest design that satisfies the contract, and test the behaviors that could break. Explain a non-obvious tradeoff in a concise code-review note or an architectural decision record only when its future significance warrants it. Do not add explanatory comments, patterns, benchmark claims, or design documents merely to demonstrate adherence.
