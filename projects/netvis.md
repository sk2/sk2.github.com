---
layout: default
section: network-automation
---

# Network Visualization Engine

<span class="status-badge status-active">v1.3 — Embed Readiness & API Stability</span>

[← Back to Network Automation](../network-automation)

---


## The Concept

Network visualization often fails at scale because layout algorithms treat all nodes and edges equally, producing cluttered "hairball" diagrams. **NetVis** treats topologies as hierarchical structures and uses domain-aware layout constraints—including isometric views and edge bundling—to reflect engineering intent.

## Quick Facts

| | |
|---|---|
| **Status** | v1.3 — Embed Readiness & API Stability |
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

## Integration with ank_pydantic

ank_pydantic topologies export directly to NetVis format:
```python
# NetVis
topo.export_for_netvis(
    "output.json",
    layout="hierarchical",
    node_metadata=True  # Include device types, roles for styling
)
```

NetVis reads the exported topology and applies advanced layout algorithms, producing publication-quality diagrams that reflect the logical structure captured in ank_pydantic.

## Example Gallery

### Enterprise Campus Network

![Enterprise Campus](/images/netvis-enterprise-campus.png)
*Multi-building campus with core/distribution/access layers, firewalls, ISP uplinks, data center spine-leaf, and management infrastructure. Edge bundling groups related connections; path analysis overlays highlight application, backup, and management traffic flows.*

### Data Center Spine-Leaf Fabric

![Data Center Fabric](/images/netvis-datacenter-large.png)
*Spine-leaf topology with 4 leaf switches, 2 spines, and 12 racks of hosts. Bandwidth annotations (10G, 25G, 100G) on each link. Force-directed layout separates rack groups while keeping the spine-leaf hierarchy visible.*

### ISP Backbone with Path Analysis

![ISP Backbone](/images/netvis-isp-backbone.png)
*US-wide ISP backbone spanning 8 cities (LAX, SEA, DEN, DAL, CHI, NYC, BOS, WAS) with core routers, customer edge devices, and IX peering. Path analysis overlay shows primary east-west, backup, and regional paths with distinct colors and weights.*

### Radial Layout — Distributed Service Mesh

![Radial Layout](/images/netvis-showcase-radial-layout.png)
*Zone-based service mesh with central controller, regional coordinators, edge nodes, and service endpoints arranged in a radial layout. Demonstrates NetVis's ability to handle hierarchical topologies with many leaf nodes.*

### Isometric Multi-Layer View

![Isometric Multi-Layer](/images/netvis-isometric-multi-layer.png)
*Three network layers (WAN, distribution, access) rendered as stacked isometric planes. The same topology is shown at each layer with inter-layer connections visible, revealing how logical structure maps across the network hierarchy.*

### Theme Showcase — Device-Aware Icons

![Theme Showcase](/images/netvis-theme-showcase.png)
*Device-type-aware rendering with distinct icons for routers, switches, firewalls, servers, and cloud nodes. Bandwidth labels (1G, 10G) on links. Shows the visual fidelity available for smaller, detail-rich diagrams.*

## Current Status

**v1.2 Visual Polish & Production Hardening** shipped (Feb 9, 2026) with SVG filter infrastructure, WCAG 3:1 contrast enforcement, high-contrast theme, and label collision avoidance.

Currently working on **v1.3 Embed Readiness & API Stability**: stable public API, deterministic output contracts, versioned config/topology schemas, and WASM compatibility testing.

## Tech Stack

Rust, petgraph, fjadra (d3-force port), SVG/PDF/PNG rendering, WASM-ready

---

[← Back to Network Automation](../network-automation)
