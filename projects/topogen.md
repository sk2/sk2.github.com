---
layout: default
---

# topogen

<span class="status-badge status-active">v0.10</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Active, v0.10 released |
| **Language** | Rust, Python (PyO3) |
| **Started** | 2025 |

---

## The Insight

Network engineers can quickly generate realistic, validated network topologies without implementing complex algorithms from scratch.

## What This Is

A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetkit, simulation tools, and visualization tools. It generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters. The tool outputs a custom YAML format for use across the network engineering tool ecosystem.

## Topology Types

- **Data center**: Fat-tree, leaf-spine with realistic parameters.
- **WAN/backbone**: Ring, mesh, hierarchical.
- **Random graphs**: Erdős-Rényi, Barabási-Albert, Watts-Strogatz.

## Interfaces

- **CLI**: Quick generation from the command line.
- **Python API**: For workflow integration.
- **Config-driven**: Uses YAML for complex/repeatable setups.
- **Parity tests**: Ensure interface consistency.

## Validation

- **Structural correctness**: Ensures valid graph structures.
- **Design pattern compliance**: Adheres to common network designs.
- **Realistic parameters**: Includes bandwidth, latency, and interface naming conventions.

## Current Status

v0.10 released. Latest update: v0.9 User Interfaces (Feb 5, 2026) with mdBook documentation and doc-tests.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)