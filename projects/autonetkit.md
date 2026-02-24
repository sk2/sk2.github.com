---
layout: default
section: network-automation
---

# AutoNetkit

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. **AutoNetkit** eliminates this trade-off by using Pydantic for schema validation and a Rust core (`petgraph`) for graph traversals.

It is a modern reimagining of the original AutoNetkit research, reclaiming the name for a production-ready automation library.

Expressive Python API backed by compiled graph algorithms (petgraph), with automatic configuration generation for multi-vendor network deployments.

---

## Features

- **Type-safe modeling**: Every device, link, and protocol attribute is validated using Pydantic.
- **High-performance core**: Graph traversals and topological queries are executed in Rust.
- **Multi-vendor support**: Generates configurations for Cisco, Juniper, Arista, and more.
- **Intent-based workflow**: Define the target state and let the engine handle the addressing and protocol logic.

---

## Architecture

Specification abstraction → intermediate network-wide state representation → low-level device configuration → template assembly.

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
