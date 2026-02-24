---
layout: default
section: network-automation
---

# Network Modeling Engine

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A modern framework for defining and querying network intent, acting as the primary **topology engine** for the ANK ecosystem. Built with type-safe Pydantic models and a fast Rust core (NTE), it provides a consistent, programmable way to manage large-scale topology data. Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers) and a composable lazy query API.

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.

---

## Current Status

2026-02-24 -- Completed 93-05-PLAN.md

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
