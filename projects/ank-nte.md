---
layout: default
section: network-automation
---

# Network Topology Engine

<span class="status-badge status-active">Phase 06/15 (96%)</span>

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Quick Facts](#quick-facts)
- [What This Is](#what-this-is)
- [Core Value](#core-value)

## Concept

NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite). This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement.

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 06/15 (96%) |
| **Language** | N/A |

---

## What This Is

NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite). This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement.

---

## Core Value

The engine must be correct and observable — mutations never silently corrupt state, errors always surface meaningful information, and operations are traceable through logging.

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
