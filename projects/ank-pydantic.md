---
layout: default
section: network-automation
---

# Configuration Engine

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A modern configuration engine for defining a network model and compiling it into a consistent, reviewable plan for downstream tooling. Built with type-safe Pydantic models and a fast Rust core (NTE), it provides a predictable, programmable way to manage large-scale topology data and derived configuration state.

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Uses an explicit intermediate representation and transformation passes (design -> plan -> protocol layers), with type-safe models for nodes/edges/layers and a composable query API.

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.

---

## Current Status

2026-02-24 -- Completed -01 (allocation templates)

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
