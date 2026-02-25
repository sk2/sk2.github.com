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

## Current Status

2026-02-25 — Completed 08-03-PLAN.md

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
