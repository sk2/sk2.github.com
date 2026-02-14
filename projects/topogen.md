---
layout: default
---

# Topology Generator

<span class="status-badge status-active">Phase 21/24 (89%)</span>

[← Back to Network Automation](../network-automation)

---


## The Concept

Generating realistic, validated network topologies for testing often requires custom, brittle scripts. **Topogen** consolidates topology generation logic into a high-performance Rust core, producing structured data center and WAN graphs with consistent YAML output for the simulation and visualization ecosystem.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 21/24 (89%) |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

A Rust library with Python bindings for generating realistic network topologies. Consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools into one well-tested implementation.

## Key Features

- **Topology Types**:
  - Data center: Fat-tree, leaf-spine
  - WAN/Backbone: Ring, mesh, hierarchical WAN, POP (Points of Presence)
  - Random graphs: Barabási-Albert, Watts-Strogatz, Erdős-Rényi
- **Realistic Interface Specifications**: Vendor-specific naming conventions (Cisco, Arista, Juniper)
- **Traffic Matrix Generation**: Gravity-model traffic matrices with temporal dynamics (diurnal/weekly patterns)
- **Distance-Aware Latency**: Geographic placement drives realistic link latencies
- **Seed-Deterministic**: Reproducible topology generation from a seed value
- **Output Converters**: YAML, ContainerLab topology files, AutoNetKit GraphML
- **Three Interfaces**: CLI, Python API, and config-driven YAML/TOML input
- **Validation**: Structural and design-pattern compliance checks

## Example: Data Center Leaf-Spine

Configuration file (`leaf-spine-lab.yaml`):
```yaml
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

topo = DataCenter.spine_leaf(
    spines=2,
    leaves=4,
    full_mesh=True,
    spine_bandwidth_gbps=100.0
)

topo.export_yaml("topology.yaml")
topo.export_json("topology.json")

# Integration with topology modeling library
from ank_pydantic import Topology
ank_topo = topo.to_ank_pydantic()
```

## Current Status

**v0.10 Gap Closure** shipped (Feb 11, 2026) with ContainerLab output converter, AutoNetKit GraphML converter, traffic pattern generation, and POP design patterns.

Currently working on **Phase 22-24**: geographic placement infrastructure (city database, H3 grids), fiber map integration (GeoJSON import/export), multi-layer topology generation, and eyeball network generators.

## Tech Stack

Rust core, PyO3 for Python bindings, Maturin build system

---

[← Back to Network Automation](../network-automation)
