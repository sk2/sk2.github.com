---
layout: default
---

# ank_pydantic

<span class="status-badge status-active">Phase 58/62 (99%)</span>

[← Back to Projects](../projects)

---


## The Insight

In network automation, you usually have to choose between the **speed** of untyped graph libraries (like NetworkX) and the **rigidity** of database-backed sources of truth. **ank-pydantic** breaks this trade-off by using Pydantic for strict schema validation at the edge, while offloading heavy graph traversals to a high-performance Rust core (`petgraph`). It brings the safety of modern software engineering to the "wild west" of network topology data.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 58/62 (99%) |
| **Language** | N/A |
| **Started** | 2025 |

---

## What This Is

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
