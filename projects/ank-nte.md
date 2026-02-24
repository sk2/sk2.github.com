---
layout: default
section: network-automation
---

# Topology Core (NTE)

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

### What This Is

NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite). This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement.

### Core Value

The engine must be correct and observable — mutations never silently corrupt state, errors always surface meaningful information, and operations are traceable through logging.

---

## Current Status

2026-02-24 — Verified  (Graph Metadata Foundation)

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
