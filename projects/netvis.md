---
layout: default
section: network-automation
---

# Network Visualization Engine

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [Usage](#usage)
- [Features](#features)
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

![Hero Image](/images/hero-diagram.svg)

---

## Concept

Rust-based network topology layout and visualization engine. Takes multi-layer network topologies (via petgraph) and renders them using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical or geographic structure. Outputs SVG, PDF, and PNG with interactive browser embedding via WASM.

Design follows Tufte's principles: maximize information density, minimize chartjunk. An automated WCAG 3:1 contrast system ensures accessibility without manual tuning.

<div class="mermaid">
flowchart LR
    T[Topology<br/>Sources] --> L[Layout<br/>Algorithms]
    L --> R[Renderer]
    R --> SVG[SVG]
    R --> PDF[PDF]
    R --> PNG[PNG]
    R --> WASM[WASM<br/>Browser]
</div>

<div class="mermaid">
block-beta
    columns 1
    eBGP["eBGP"]
    iBGP["iBGP"]
    OSPF["OSPF"]
    IP["IP Layer"]
    L2["Layer 2"]
    Physical["Physical"]
</div>

---

## Code Samples

### Filter views

```yaml
# Production view — hide decommissioned
show:
  tags: [production]
hide:
  types: [hub]
  tags: [decommissioned]
```

### Data adapters

Importers for LLDP/CDP discovery JSON and NetBox — run `netvis import` to convert external data into topology YAML, then render with `netvis --input`.

<details class="code-collapse">
<summary>View Python bindings example (basic_topology.py)</summary>

```python
#!/usr/bin/env python3
"""Basic topology example using NetVis Python bindings."""
import netvis

def main():
    topo = netvis.Topology()

    # Add spine and leaf switches
    topo.add_node("spine-1", node_type="switch", label="Spine 1",
        attrs={"vendor": "arista", "model": "7050X3"})
    topo.add_node("spine-2", node_type="switch", label="Spine 2",
        attrs={"vendor": "arista", "model": "7050X3"})
    for i in range(1, 5):
        topo.add_node(f"leaf-{i}", node_type="switch", label=f"Leaf {i}",
            attrs={"vendor": "arista", "model": "7280R3"})

    # Add servers and connect to leaves
    for i in range(1, 9):
        leaf_num = ((i - 1) // 2) + 1
        topo.add_node(f"server-{i}", node_type="server", label=f"Server {i}")
        topo.add_edge(f"server-{i}", f"leaf-{leaf_num}",
            from_interface="eno1", to_interface=f"Eth1/{i % 48}",
            attrs={"speed": "25G", "cable_type": "DAC"})

    # Full mesh leaf-to-spine
    for leaf in range(1, 5):
        for spine in ["spine-1", "spine-2"]:
            topo.add_edge(f"leaf-{leaf}", spine,
                attrs={"speed": "100G", "cable_type": "single-mode-fiber"})

    topo.render_to_file("spine-leaf.svg", layout="hierarchical")

if __name__ == "__main__":
    main()
```

</details>

---

## Visuals

### Network Visualisation Examples

![Geographic WAN](/images/geographic_wan.png)

![Bundled Mesh](/images/bundled_mesh.png)

![Hierarchical Datacenter](/images/hierarchical_datacenter.png)

![Labels Dense](/images/labels_dense.png)

![Force Directed Basic](/images/force_directed_basic.png)

---

## Usage

```bash
# Render a topology to SVG
netvis --input topology.yaml --output network.svg

# Geographic layout
netvis --input backbone.yaml --layout geographic --output map.svg

# Multi-layer isometric view
netvis --input datacenter.yaml --layout isometric --layers physical,l2,ospf --output layers.svg

# Import from LLDP discovery
netvis import --format lldp --input discovery.json --output topology.yaml

# Timeline across snapshots
netvis timeline --input snapshots/ --output timeline.svg
```

---

## Features

**Rendering:**
- SVG, PDF, PNG output
- WASM target for browser embedding
- SVG filter effects (drop shadows, glow) with Tufte-inspired guardrails
- Effect budget system prevents performance cliffs on large topologies
- Signature-based filter deduplication reduces SVG file size

**Analysis:**
- Path highlighting via BFS
- Traffic utilization overlays with NOC color mapping
- Timeline mode for multi-snapshot SVG export with incremental diffs
- Temporal entity queries (when did a node appear/change/disappear)
- Filter by type, tag, group, or layer without re-running layout

**Integration:**
- Python bindings via PyO3
- YAML/JSON topology input
- Adapters for LLDP/CDP discovery JSON and NetBox import
- Contract-versioned API for stable embedding

---

## Current Status

v1.9 Scale & Export in progress — targeting 10K-node layouts in under 10 seconds (Barnes-Hut + Rayon parallelization) and single-file interactive HTML export with embedded WASM.

Previous: v1.8 Temporal & Interaction shipped 2026-03-01 (timeline mode, topology filters, traffic animation, annotations). Eight milestones shipped across v1.0–v1.8.

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/netvis-techreport.pdf)


---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
