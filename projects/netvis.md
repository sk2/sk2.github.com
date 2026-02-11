---
layout: default
---

# netvis

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Insight

Network visualization often fails at scale because layout algorithms treat all nodes and edges equally, resulting in a "hairball" effect. **NetVis** treats network topologies as hierarchical, layered structures. By using domain-aware layout constraints—like isometric multi-layer views and force-directed edge bundling—it transforms raw graph data into a map that actually reflects the engineering intent of the network.

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
