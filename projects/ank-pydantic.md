---
layout: default
---

# ank_pydantic

<span class="status-badge status-active">Phase 59/62 (99%)</span>

[← Back to Projects](../projects)

---


## The Insight

Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. **ank-pydantic** eliminates this trade-off by using Pydantic for schema validation and a high-performance Rust core (`petgraph`) for graph traversals.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 59/62 (99%) |
| **Language** | N/A |
| **Started** | 2025 |

---

## What This Is

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
