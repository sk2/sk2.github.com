---
layout: default
section: network-automation
---

# Network Modeling & Configuration Library

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A Python-native configuration engine for defining a network model and compiling it into a consistent, reviewable plan. It solves the 'type safety vs performance' problem by combining the ergonomics of Pydantic models with a fast Rust graph core (NTE).

As one of the two primary modeling tools in the ecosystem, it offers a high-level, developer-friendly interface for building complex network designs. It uses an explicit intermediate representation and transformation passes (design -> plan -> protocol layers) to ensure architectural consistency across the entire topology.

---

## Features

- **Type-Safe Modeling**: Device, interface, and relationship models with strict Pydantic validation.
- **Rust-Backed Operations**: High-performance graph traversals and queries via PyO3 and petgraph.
- **Rich Query API**: Chainable filters and traversals that replace manual graph walking with declarative intent.
- **Multi-Layer Support**: Native modeling of physical, logical, and protocol views within a single graph structure.
- **Multi-Vendor Generation**: Compiles intent into validated configurations for 11+ major networking platforms.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
