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
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A Rust-based network topology layout and visualization engine that transforms complex multi-layer networks into clear, information-dense renderings. Advanced layout algorithms minimize visual complexity while preserving structural clarity.

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

## Example: Quick Start

Input topology (`simple-network.yaml`):
```yaml
nodes:
  - name: r1
    type: router
  - name: r2
    type: router
  - name: s1
    type: switch
  - name: s2
    type: switch
  - name: h1
    type: host
  - name: h2
    type: host

edges:
  - src: r1
    dst: s1
  - src: r1
    dst: s2
  - src: r2
    dst: s1
  - src: r2
    dst: s2
  - src: s1
    dst: h1
  - src: s2
    dst: h2
  - src: s1
    dst: s2
```

Render with CLI:
```bash
$ netvis render simple-network.yaml \
    --layout force-directed \
    --output output.svg \
    --width 800 \
    --height 600

Loaded topology: 6 nodes, 7 edges
Applying force-directed layout...
Layout converged in 245 iterations
Rendering to SVG...
Written: output.svg (6.5 KB)
```

## Example Outputs

Data center spine-leaf:
![NetVis Data Center](/images/netvis-datacenter-example.svg)

Mesh network:
![NetVis Mesh](/images/netvis-mesh-example.svg)

Ring topology:
![NetVis Ring](/images/netvis-ring-example.svg)

## Integration with ank_pydantic

ank_pydantic topologies export directly to NetVis format:
```python
# Export topology with layout hints
topo.export_for_netvis(
    "output.json",
    layout="hierarchical",
    node_metadata=True  # Include device types, roles for styling
)
```

NetVis reads the exported topology and applies advanced layout algorithms, producing publication-quality diagrams that reflect the logical structure captured in ank_pydantic.

## Current Status

Core layout algorithms implemented, refining edge bundling and multi-layer rendering. Interactive browser embedding planned for v2.

## Tech Stack

Rust, petgraph for graph algorithms, SVG/PDF rendering libraries

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
