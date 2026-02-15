---
layout: default
section: network-automation
---

# Topology Generator

<span class="status-badge status-active">Phase 21/24 (89%)</span>

[← Back to Network Automation](../network-automation)

---


## The Concept

Generating realistic, validated network topologies for testing often requires custom, brittle scripts. The **Topology Generator** consolidates topology generation logic into a high-performance Rust core, producing structured data center and WAN graphs with consistent YAML output for the simulation and visualization ecosystem.

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

# Integration with the Topology Modeling Library
from ank_pydantic import Topology
ank_topo = topo.to_ank_pydantic()
```

## Milestones

**v1.0-alpha Foundation** (Shipped Jan 28, 2026)
Core topology generators, validation framework, and output format.
- Data center generators (fat-tree, leaf-spine) and WAN generators (ring, mesh, hierarchical)
- Random graph generators (Barabási-Albert, Watts-Strogatz, Erdős-Rényi)
- Structural and design-pattern validation
- YAML output format

**v0.9 User Interfaces** (Shipped Feb 5, 2026)
CLI, Python API, config-driven generation, and documentation.
- Production CLI with shell completions and JSON diagnostics
- Python bindings via PyO3 with full API parity
- Config-driven generation from YAML/TOML files
- Documentation site with algorithm references and example gallery

**v0.10 Gap Closure** (Shipped Feb 11, 2026)
Output converters, traffic patterns, and POP design patterns.
- ContainerLab topology file export
- AutoNetKit GraphML converter
- Gravity-model traffic matrices with diurnal/weekly temporal dynamics
- POP design patterns — access, metro, regional, and backbone tiers with geographic placement and redundancy models

**v1.0 Production Features** (In Progress — Phases 22-24)

- **Geographic placement infrastructure** — City database lookup, H3 grid placement, distance-based latency calculation, region/country filtering
- **Fiber map integration** — GeoJSON import/export, estimated vs actual fiber route distinction, terrain plausibility checks
- **Multi-layer topology generation** — Explicit underlay/overlay layer dependencies, overlay-to-underlay path mapping, cross-layer capacity validation
- **Eyeball network generator** — Access-aggregation-core hierarchy for ISP topologies, inbound-heavy traffic ratios, peering and transit policy configuration

## Tech Stack

Rust core, PyO3 for Python bindings, Maturin build system

---

[← Back to Network Automation](../network-automation)
