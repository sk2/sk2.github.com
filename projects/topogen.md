---
layout: default
section: network-automation
---

# Topology Generator

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Generator Types](#generator-types)
- [Configuration](#configuration)
- [Usage](#usage)
- [Multi-Layer Topologies](#multi-layer-topologies)
- [Ecosystem Integration](#ecosystem-integration)
- [Status](#status)
- [Technical Reports](#technical-reports)

## Concept

Rust-based network topology generator with Python bindings. Takes a declarative YAML config describing the desired topology type, scale, and parameters, and produces a validated network graph with realistic structure — proper tier hierarchies, vendor-specific interface naming, geographic placement, and bandwidth profiles.

Consolidates topology generation logic that was previously scattered across AutoNetKit, the Network Simulator, and the Visualization Engine into a single library. Network engineers can generate data center fabrics, WAN backbones, enterprise hierarchies, and random graph models without implementing the algorithms from scratch.

Three interfaces with parity guarantees: CLI for quick generation, Python API for workflow integration, config files for repeatable setups.

---

## Generator Types

### Data Center

- **Fat-tree** — k-ary Clos topology with core, aggregation, and edge tiers. k=4 produces 20 switches; k=8 produces 80. Supports vendor-specific interface naming (Cisco, Arista, Juniper).
- **Leaf-spine** — two-tier fabric with configurable spine count, leaf count, and full/partial mesh. Bandwidth profiles from 100G to 400G.

### WAN & Backbone

- **Ring** — regional WAN ring with geographic constraints (NA, EU, APAC). Configurable bandwidth profiles and redundancy levels.
- **Mesh** — full-mesh backbone for Tier-1/CDN interconnect. City-tier selection controls which global hubs are included.
- **Hierarchical** — multi-region enterprise WAN with access/distribution/core tiers. Variable bandwidth and redundancy (minimal, standard, high).

### Access & ISP

- **Eyeball** — access ISP hierarchy (access, aggregation, core) with subscriber host nodes, peering/transit endpoints, and configurable tiers.

### Random Graph Models

- **Barabasi-Albert** — scale-free graph with power-law degree distribution. Parameter `m` controls new edges per node.
- **Watts-Strogatz** — small-world graph with configurable rewiring probability (`beta`).
- **Erdos-Renyi** — G(n, p) random graph baseline.

---

## Configuration

Topology configs are YAML files with annotated headers. Each config specifies the generator type, scale parameters, and optional constraints:

```yaml
# Fat-tree data center (k=4, Cisco interface naming)
name: dc-lab-fat-tree-k4-cisco
seed: 42
vendor: cisco

type: fat-tree
k: 4
core_bandwidth_gbps: 400.0
agg_bandwidth_gbps: 100.0
```

```yaml
# Enterprise WAN (hierarchical, NA+EU, 20 nodes)
name: enterprise-wan-na-eu-20
seed: 4242

type: hierarchical
node_count: 20
regions: ["NA", "EU"]
bandwidth_profile: variable
redundancy: standard
```

```yaml
# Access ISP (regional, 1k subscribers)
name: eyeball-regional-1k
seed: 42

type: eyeball
template: regional-isp
subscriber_count: 1000
tiers: 3
redundancy: standard
peering_to_transit_split: 0.7
```

Seeded generation is deterministic — same config, same seed, same output every time.

---

## Usage

### CLI

```bash
# Generate a topology
topogen generate config.yaml --output topology.yaml

# Validate structural correctness
topogen validate topology.yaml
```

### Python API

```python
import topogen

# Generate a fat-tree
topo = topogen.generate("fat-tree", k=4, seed=42, vendor="cisco")
print(f"nodes={topo.node_count()} edges={topo.edge_count()}")

# Export to YAML
topo.export("topology.yaml")
```

### Config-Driven

```bash
# Run from a config file (repeatable)
topogen generate examples/configs/datacenter-lab/fat-tree--lab-k4-cisco--seed42.yaml \
  --output topology.yaml
```

---

## Multi-Layer Topologies

The generator supports multi-layer topologies where an overlay network is built on top of a physical underlay:

```yaml
name: multi-layer-pop-backbone
type: multi-layer

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

Each layer is generated independently, then interconnected according to the specified strategy.

---

## Ecosystem Integration

The Topology Generator exports to multiple downstream formats:

- **AutoNetKit YAML** — for the [Network Modeling & Configuration Library](ank-pydantic), with topology_type, tier, role, and region metadata
- **Network Simulator YAML** — directly consumable by the [Network Simulator](netsim) with device/wire/traffic structure
- **ContainerLab YAML** — for lab deployment on containerized network devices
- **Traffic matrix (CSV/JSON)** — gravity-model traffic matrices for the [Network Flow Simulator](netflowsim)
- **GeoJSON** — geographic node placement for the [Visualization Engine](netvis)

---

## Status

**Current**: v1.5 Intent-Based Overlays — formalizing BGP/OSPF/Physical overlay tags, intent-based role assignment, and schematic grouping (Site, Pod, Zone hierarchies).

**Recently shipped:**
- v1.4 — Interactive editing and incremental validation (March 2026)
- v1.0 — All generator types (fat-tree, leaf-spine, ring, mesh, hierarchical, eyeball, random graphs), Python bindings, config-driven generation, structural validation
- v0.9 — CLI, vendor interface naming, example gallery, documentation

---

## Technical Reports

- [Download Technical Report: topogen-techreport.pdf](/assets/docs/topogen-topogen-techreport.pdf)

---

[← Back to Projects](../projects)
