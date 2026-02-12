---
layout: default
---

# TopoGen - Network Topology Generator

<span class="status-badge status-active">Phase 17/24 (11%)</span>

[← Back to Projects](../projects)

---


## The Insight

Generating realistic, validated network topologies for testing often requires custom, brittle scripts. **Topogen** consolidates topology generation logic into a high-performance Rust core, producing structured data center and WAN graphs with consistent YAML output for the simulation and visualization ecosystem.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 17/24 (11%) |
| **Language** | Rust, Python |
| **Started** | 2026 |

---

## What This Is

A Rust library with Python bindings for generating realistic network topologies. Consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools into one well-tested implementation.

## Key Features

- **Realistic Topology Types**:
  - Data center: Spine-leaf, fat-tree, Clos
  - WAN: Hub-and-spoke, ring, full mesh, partial mesh
  - Random graphs: Erdős-Rényi, Barabási-Albert, Watts-Strogatz
- **Design Pattern Awareness**: Generates topologies that reflect real-world network design
- **Configurable Parameters**: Node count, link capacity, failure domains, geographic distribution
- **Custom YAML Output**: Compatible with ank_pydantic and other ecosystem tools
- **Python Bindings**: Ergonomic API for scripting and integration

## Example: Data Center Leaf-Spine

Configuration file (`leaf-spine-lab.yaml`):
```yaml
# Title: Leaf-spine lab (2 spines, 4 leaves, 100G)
# Goal: A compact 2-tier Clos for lab validation

name: dc-lab-leaf-spine-2s-4l-100g
seed: 42

type: leaf-spine
spines: 2
leaves: 4
full_mesh: true
spine_bandwidth_gbps: 100.0
```

Generate topology:
```bash
$ topogen generate leaf-spine-lab.yaml --output topology.yaml

Generated topology: dc-lab-leaf-spine-2s-4l-100g
  Nodes: 6 (2 spines, 4 leaves)
  Links: 8 (full mesh spine-leaf connectivity)
  Total bandwidth: 800 Gbps
  Oversubscription: 2:1 (standard)

Output written to: topology.yaml
```

Generated output (excerpt):
```yaml
name: dc-lab-leaf-spine-2s-4l-100g
topology_type: leaf-spine

nodes:
  - name: spine-1
    type: spine
    tier: 1
  - name: spine-2
    type: spine
    tier: 1
  - name: leaf-1
    type: leaf
    tier: 2
  - name: leaf-2
    type: leaf
    tier: 2
  - name: leaf-3
    type: leaf
    tier: 2
  - name: leaf-4
    type: leaf
    tier: 2

links:
  - src: leaf-1
    dst: spine-1
    bandwidth_gbps: 100.0
    latency_ms: 0.1
  - src: leaf-1
    dst: spine-2
    bandwidth_gbps: 100.0
    latency_ms: 0.1
  # ... (full mesh: 4 leaves × 2 spines = 8 links)
```

## Python API

```python
from topogen import DataCenter

# Programmatic generation
topo = DataCenter.spine_leaf(
    spines=2,
    leaves=4,
    full_mesh=True,
    spine_bandwidth_gbps=100.0
)

# Export to multiple formats
topo.export_yaml("topology.yaml")
topo.export_json("topology.json")

# Integration with ank_pydantic
from ank_pydantic import Topology
ank_topo = topo.to_ank_pydantic()
```

## Current Status

Early development, focusing on core algorithms and Python bindings.

## Tech Stack

Rust core, PyO3 for Python bindings

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
