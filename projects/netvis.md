---
layout: default
section: network-automation
---

# Network Visualization Engine

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Metrics](#metrics)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)

## Concept

Network visualization often fails at scale because layout algorithms treat all nodes and edges equally, producing cluttered "hairball" diagrams. The **Network Visualization Engine** treats topologies as hierarchical structures and uses domain-aware layout constraints—including isometric views and edge bundling—to reflect engineering intent.

---

## Architecture

- `petgraph`-backed graph wrapper with typed nodes/edges
- Layout algorithms: force-directed, Sugiyama hierarchical, radial tree
- Multi-layer support with isometric/starburst layouts
- Edge refinement: force-directed edge bundling (FDEB), obstacle-aware routing
- Customizable styling system with type-safe builder pattern

---

## Metrics

582 tests (554 unit + 28 integration), 17 example topologies, CLI tool

---

## Tech Stack

Rust, petgraph, fjadra (d3-force port), SVG/PDF/PNG rendering, WASM-ready

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Key Features

- **Advanced Layout Algorithms**:
  - Force-directed layout with configurable parameters
  - Hierarchical layout for tree-like topologies
  - Geographic layout for physical infrastructure
  - Edge bundling to reduce visual clutter
- **Multi-Layer Support**: Visualize L2, L3, and logical layers simultaneously
- **Static Output Formats**: SVG, PDF, PNG (v1 focus)
- **High-Quality Rendering**: Anti-aliased, publication-ready graphics
- **Topology Awareness**: Uses `petgraph` for graph analysis

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
