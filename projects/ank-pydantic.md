---
layout: default
section: network-automation
---

# Network Modeling Library

<span class="status-badge status-active">Phase 92/94</span>

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Quick Facts](#quick-facts)
- [What This Is](#what-this-is)
- [Core Value](#core-value)

## Concept

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 92/94 |
| **Language** | N/A |

---

## What This Is

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

---

## Core Value

A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
