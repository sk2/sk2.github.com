---
layout: default
---

# NetVis

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Insight

Network visualization often fails at scale because layout algorithms treat all nodes and edges equally, producing cluttered "hairball" diagrams. **NetVis** treats topologies as hierarchical structures and uses domain-aware layout constraints—including isometric views and edge bundling—to reflect engineering intent.

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | N/A |
| **Started** | 2025 |

---

## What This Is

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
