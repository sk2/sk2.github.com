---
layout: default
section: network-automation
---

# Topology Generator

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

## Concept

Rust-based network topology generator with Python bindings. Takes a declarative YAML config describing the desired topology type, scale, and parameters, and produces a validated network graph with realistic structure — proper tier hierarchies, vendor-specific interface naming, geographic placement, and bandwidth profiles.

Consolidates topology generation logic that was previously scattered across AutoNetKit, the [Network Simulator](/projects/netsim), and the [Network Visualization Engine](/projects/netvis) into a single library. Network engineers can generate data center fabrics, WAN backbones, enterprise hierarchies, and random graph models without implementing the algorithms from scratch.

Three interfaces with parity guarantees: CLI for quick generation, Python API for workflow integration, config files for repeatable setups.

---

## Code Samples

### Data center fat-tree

```yaml
name: fat-tree-lab
type: fat_tree
k: 4
vendor: cisco
seed: 42
```

### Multi-layer POP backbone

```yaml
name: multi-layer-pop-backbone
type: multi_layer

layers:
  - name: physical
    type: pop
    count: 5
    redundancy: n+1

  - name: backbone
    type: mesh
    node_count: 4
    underlay: physical
    strategy: shortest-path
```

### Random graph models

```yaml
# Scale-free network (Barabasi-Albert)
name: scale-free
type: barabasi_albert
n: 100
m: 3
seed: 42
```

---

## Usage

```bash
# Generate a topology from config
topogen generate configs/datacenter-lab/fat-tree--lab-k4-cisco--seed42.yaml \
  --output topology.yaml

# Validate structure
topogen validate topology.yaml

# Python API
from topogen import generate
topo = generate("leaf_spine", spines=4, leaves=16, bandwidth="400g")
```

<div class="mermaid">
flowchart TD
    TT[Topology Types]
    TT --> CLOS[Clos Family]
    TT --> TRAD[Traditional]
    TT --> RAND[Random Graphs]
    CLOS --> FT[Fat-Tree]
    CLOS --> LS[Leaf-Spine]
    TRAD --> RING[Ring]
    TRAD --> MESH[Mesh]
    TRAD --> HAS[Hub-and-Spoke]
    TRAD --> C3T[Campus 3-Tier]
    TRAD --> HWAN[Hierarchical WAN]
    RAND --> BA[Barabasi-Albert]
    RAND --> WS[Watts-Strogatz]
    RAND --> ER[Erdos-Renyi]
</div>

---

## Current Status

v1.5 Intent-Based Overlays & Schematic Enrichment in progress. Previous: v1.4 Interactive Editing & Incremental Validation shipped 2026-03-02.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/topogen-techreport.pdf)

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
