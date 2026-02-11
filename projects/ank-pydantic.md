---
layout: default
---

# ank-pydantic

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | Python, Rust (PyO3) |
| **Started** | 2025 |

---

## The Insight

In network automation, you usually have to choose between the **speed** of untyped graph libraries (like NetworkX) and the **rigidity** of database-backed sources of truth. **ank-pydantic** breaks this trade-off by using Pydantic for strict schema validation at the edge, while offloading heavy graph traversals to a high-performance Rust core (`petgraph`). It brings the safety of modern software engineering to the "wild west" of network topology data.

## What This Is

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

## Problem It Solves

- Graph libraries (NetworkX, rustworkx): fast but untyped, easily create invalid structures.
- Source-of-truth tools (NetBox, Nautobot): great for inventory but not designed for topology analysis.
- Custom solutions: full control but require building validation, storage, and query layers.

## Features

- Type-safe device, interface, relationship models with Pydantic validation.
- Rust-backed graph operations for performance with Python ergonomics.
- Rich query API: chainable filters and traversals without manual graph walking.
- Multi-layer modeling: separate physical, logical, protocol views.
- Multi-vendor config generation for 11+ platforms.
- Optional API server, CLI, visualization.

## Use Cases

- Design validation before deployment.
- Multi-vendor config generation.
- Architecture compliance checking.
- SDN controller prototyping.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)