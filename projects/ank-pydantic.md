---
layout: default
---

# ank_pydantic

<span class="status-badge status-active">Phase 58/62 (99%)</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 58/62 (99%) |
| **Language** | N/A |
| **Started** | 2025 |

---

## Core Value

A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.

## What This Is

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
