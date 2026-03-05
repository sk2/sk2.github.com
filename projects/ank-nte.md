---
layout: default
section: network-automation
---

# Topology Engine Core

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Technical Depth](#technical-depth)
- [Tech Stack](#tech-stack)
- [Roadmap Direction](#roadmap-direction)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Current Milestone: v1.0 Engine Hardening](#current-milestone-v10-engine-hardening)
- [Ecosystem Context](#ecosystem-context)
- [Current Status](#current-status)

## Concept

The high-performance graph core that powers the ANK ecosystem. NTE (Network Topology Engine) provides a native Rust implementation of multi-layer network graphs, optimized for low-latency queries and complex topological transformations.

NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite). This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement.

The engine must be correct and observable — mutations never silently corrupt state, errors always surface meaningful information, and operations are traceable through logging.

---

## Architecture

Built as a 14-crate Cargo workspace, the engine utilizes `petgraph`'s StableDiGraph for structural persistence. It features a pluggable datastore architecture supporting Polars, DuckDB, and Lite backends, allowing for efficient attribute storage and bulk data analysis.

---

## Technical Depth

The engine implements a 'Write-Through' model with Python bindings via PyO3. Mutations in the Python layer are automatically persisted to the Rust core, ensuring that topological queries always execute against high-performance compiled graph algorithms rather than slower interpreted structures.

---

## Tech Stack

- Rust 2021 workspace with feature-flagged backends
- Graph structure: `petgraph` `StableDiGraph`
- Datastores: Polars DataFrame store (default), DuckDB backend, Lite in-memory store
- Python bindings: PyO3 + maturin; `pyo3-log`/logging bridge planned
- Service mode: Axum HTTP + WebSocket server (`nte-server`) for remote execution

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Roadmap Direction

**Milestone 1: Engine Hardening** focuses on user-facing correctness and debuggability:

- Logging and traceability throughout Rust and Python boundaries
- Domain-specific Python exceptions (replace generic error returns)
- Dual-write safety: explicit error propagation and rollback/compensation for failed updates
- GIL release for O(N) operations (`py.allow_threads`) to unblock Python workloads
- CI/CD so the engine can be updated without breaking downstream consumers

**Milestone 2: LadybugDB Evaluation** is the architectural fork:

- Evaluate whether a graph database backend improves diff/snapshots/temporal queries
- Build a `TopologyBackend` implementation and benchmark at meaningful scales
- Decide the backend path before committing to topology diff, snapshots, or a wire protocol

---

## # Validated

- ✓ Graph topology with petgraph StableDiGraph (nodes, edges, layers) — existing
- ✓ PyO3 Python bindings for topology operations — existing
- ✓ Pluggable datastore backends (Polars, DuckDB, Lite) — existing
- ✓ Query engine with QuerySpec flat filters (type, layer, id, field) — existing
- ✓ Event sourcing for mutation tracking — existing
- ✓ JSON export with layer filtering — existing
- ✓ Force-directed layout via fjadra — existing
- ✓ Topology archive save/load (ZIP + NDJSON) — existing
- ✓ Standalone Axum HTTP/WebSocket server (nte-server) — existing
- ✓ Edge type correctness (Inter, Intra, Intranode) — existing

---

## # Active

**Milestone 1: Engine Hardening**
- [ ] Logging throughout the engine (`log` + `pyo3-log` bridge)
- [ ] Domain-specific Python exceptions replacing all generic errors
- [x] Dual-write safety (error propagation, rollback on failure)
- [ ] GIL release for O(N) PyO3 methods (`py.allow_threads`)
- [ ] CI/CD pipeline (GitHub Actions, Clippy, fmt, tests)
- [ ] One-way dependency: ank_pydantic depends on NTE, never reverse
- [ ] Internal/external boolean flag on nodes and edges

**Milestone 2: LadybugDB Evaluation**
- [ ] Schema design spike (generic schema with existing benchmarks)
- [ ] Port/interface modelling assessment
- [ ] `TopologyBackend` trait implementation for LadybugBackend
- [ ] Benchmark at target scales (1k, 5k, 10k nodes)
- [ ] Query translation: `compile_to_cypher()` for QuerySpec flat filters
- [ ] Pattern compilation: PatternNode chain to Cypher MATCH clauses
- [ ] Concurrent read/write testing under server workloads
- [ ] Evaluation summary with recommendation

---

## # Out of Scope

- Topology diff (`nte-diff`) — blocked on backend decision (Milestone 2)
- Snapshots & temporal queries — blocked on backend decision
- Binary wire protocol (`nte-wire`) — blocked on backend decision
- Full query engine pattern matching — depends on backend choice; current stub returns empty results by design until backend is decided
- Monte Carlo integration — standalone, not part of these milestones
- Export formats (YAML, GraphML, NetworkX) — nice-to-have, not priority
- Visualisation library (D3/React frontend) — deferred until after hardening

---

## Context

- NTE is consumed by ank_pydantic as its backend engine (sibling repo `../ank_pydantic/`)
- The dual-write architecture (petgraph + DataFrameStore) is fully protected by a RAII `DualWriteGuard`  which automatically rolls back graph mutations if DataFrame operations fail.
- No CI/CD pipeline exists — all testing is manual
- LadybugDB (formerly using KuzuDB) has a standalone benchmark crate (`ladybug_backend/`) but does NOT implement `TopologyBackend` trait
- The backend evaluation is the biggest architectural decision: it shapes diff, snapshots, and wire protocol implementation
- British English throughout; "vis" not "viz"

---

## Constraints

- **Tech stack**: Rust 2021 + PyO3 0.26 + Python 3.13+ (fixed)
- **Backwards compatibility**: Python API must remain stable — changes are additive, not breaking
- **Build system**: maturin + uv (fixed)
- **Naming**: Use "LadybugDB" for the graph database backend, not "KuzuDB" (deprecated upstream name)

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Harden before evaluate | Fix correctness/observability issues that affect users today, independent of backend choice | — Pending |
| Two-milestone structure | Hardening is prerequisite — reliable engine needed to properly benchmark LadybugDB | — Pending |
| LadybugDB not KuzuDB naming | Upstream rebrand; use current name throughout | ✓ Good |

---

## Current Milestone: v1.0 Engine Hardening

**Goal:** Make NTE production-ready with correct error handling, observable logging, automated CI/CD, and Python-level parallelism.

**Target features:**
- CI/CD pipeline (GitHub Actions, multi-platform wheels, automated testing)
- Dual-write rollback mechanism (graph ↔ DataFrameStore consistency)
- Structured logging with tracing (Python-Rust bridge)
- GIL release for O(N) PyO3 methods
- Domain-specific Python exceptions
- Type stubs (.pyi) for Python consumers
- Property-based testing for graph invariants
- LICENSE file

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. NTE provides the high-performance graph engine — the foundation that ank-pydantic builds on.

**Role:** Rust graph engine with petgraph, Polars DataFrames, query engine, and pluggable datastores. Consumed by ank-pydantic as a dependency; potentially usable by other tools (netvis, netflowsim) for zero-conversion topology loading.

**Key integration points:**
- Primary consumer: ank-pydantic (Python ↔ Rust FFI via PyO3)
- Bidirectional ID mapping: external IDs (user-facing) ↔ internal petgraph NodeIndex
- Event sourcing: ring-buffer EventStore for audit/replay (future: live topology bus)
- Pluggable datastore: Polars (default), DuckDB, Lite backends via feature flags

**Critical note:** The dual-write architecture (petgraph + DataFrameStore) was completely hardened with transaction isolation and automatic rollback handling in , and . State divergence is impossible.

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities

*Last updated: 2026-02-15 after milestone v1.0 started*

---

## Current Status

2026-03-04 — Completed  (Zero-copy Mmap CSR Serialization and Traversal).

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
