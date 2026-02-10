---
layout: default
---

# TopoGen

<span class="status-badge status-active">v0.10 Gap Closure</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | v0.9 shipped, v0.10 in progress |
| **Language** | Rust + Python bindings |
| **Latest Release** | v0.9 User Interfaces (Feb 5, 2026) |
| **Topology Types** | Data center, WAN, random graphs |
| **Started** | 2025 |
| **License** | TBD |

---

## Overview

TopoGen is a network topology generator with Python bindings that consolidates scattered generation logic from AutoNetKit, simulation tools, and visualization tools into a single high-performance Rust library. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters.

## Problem It Solves

Topology generation code currently exists in three separate places:
- AutoNetKit (graph-based topology generation)
- Simulation engines (topology setup for network simulation)
- Visualization tools (topology generation for diagrams)

This duplication causes:
- Inconsistent implementations across tools
- Repeated effort maintaining similar code
- Different parameter handling in each tool
- No shared improvements or optimizations

**TopoGen consolidates** generation logic into single, high-performance library with consistent interface across CLI, Python API, and config files.

## Topology Types

### Data Center

**Fat-Tree:**
- K-ary fat-tree topologies for modern data centers
- Proper oversubscription ratios
- Realistic bandwidth allocation (10G/40G/100G)

**Leaf-Spine:**
- Two-tier Clos architecture
- Configurable spine/leaf counts
- ECMP-ready structure

### WAN/Backbone

**Ring:**
- Simple ring topology for redundant WAN
- Configurable link costs and latencies

**Mesh:**
- Full or partial mesh
- Realistic WAN latencies (based on geographic distance)

**Hierarchical:**
- Core/distribution/access tiers
- Enterprise campus structure

### Random Graphs

**Erdős-Rényi:**
- Random graph with configurable edge probability
- Good for testing worst-case routing scenarios

**Barabási-Albert:**
- Scale-free network with preferential attachment
- Models realistic network growth patterns

**Watts-Strogatz:**
- Small-world network with configurable clustering
- Balance between local clustering and global connectivity

## Architecture

### Three Interfaces

**CLI:** Quick generation from command line
```bash
topogen datacenter fat-tree --k 4 --output topology.yaml
topogen wan ring --nodes 5 --latency 20ms
topogen random erdos-renyi --nodes 50 --probability 0.1
```

**Python API:** Workflow integration
```python
from topogen import FatTree, export_yaml

topology = FatTree(k=4, bandwidth="10G")
export_yaml(topology, "datacenter.yaml")
```

**Config-Driven:** Complex/repeatable setups via YAML
```yaml
type: fat-tree
k: 4
bandwidth: "10G"
oversubscription: "3:1"
naming:
  spine: "spine-{:02d}"
  leaf: "leaf-{:02d}"
```

### Parity Tests

Ensure interface consistency. Same parameters via CLI, Python API, or config file produce identical topologies.

### Validation

**Structural Correctness:**
- Check graph connectivity
- Verify degree distribution
- Validate expected properties (diameter, clustering coefficient)

**Design Pattern Compliance:**
- Fat-tree has correct structure (pods, aggregation, core)
- Leaf-spine has proper two-tier design
- Hierarchical has expected tier structure

**Realistic Parameters:**
- Bandwidth appropriate for topology type (DC vs WAN)
- Latency realistic for link type
- Interface naming follows vendor conventions

## Custom YAML Format

Interfaces stored under nodes (not edge-centric):

```yaml
nodes:
  - name: spine-01
    type: router
    interfaces:
      - name: eth0
        speed: "10G"
        connected_to: leaf-01:eth0
      - name: eth1
        speed: "10G"
        connected_to: leaf-02:eth0

  - name: leaf-01
    type: router
    interfaces:
      - name: eth0
        speed: "10G"
        connected_to: spine-01:eth0
```

Following AutoNetKit "whiteboard" model. More extensible than classical graph formats for network topologies.

## Vendor-Specific Interface Naming

Configurable interface naming conventions:
- Cisco: GigabitEthernet0/0/1, TenGigabitEthernet0/1/1
- Juniper: ge-0/0/0, xe-0/0/0
- Arista: Ethernet1, Ethernet2/1
- Generic: eth0, eth1

## Features

### Example Gallery

17 example topologies included:
- Simple (star, ring, mesh)
- Data center (fat-tree K=2, K=4, leaf-spine)
- WAN (ring, partial mesh, hierarchical)
- Random (various parameters)

### Algorithm Documentation

Full documentation with:
- Mathematical formulations
- Complexity analysis (time/space)
- Parameter guidance
- References to research papers

### Enhanced CLI

- Parameter ranges and validation
- Examples in help text
- Shell completions (bash, zsh, fish)
- JSON diagnostics for errors

### Error Handling

Typed Python exception hierarchy:
- `InvalidParameterError`
- `TopologyGenerationError`
- `ValidationError`

Better error messages with context and suggestions.

## Development Status

**v0.9 Complete** (Feb 5, 2026) - User interfaces with documentation

**v0.10 In Progress:**
- Expose Erdős-Rényi generator via all interfaces
- Integrate topology-specific structural validators
- Complete Phase 06 verification

**v1.0-alpha Goals:**
- All core topology types ✅
- All three interfaces (CLI, API, config) ✅
- Comprehensive validation ✅
- Vendor-specific naming ✅
- Example gallery ✅
- Full documentation ✅

## Future Work

**Out of Scope for v1:**
- Multi-layer topologies (use AutoNetKit parameters)
- Geographic placement (stochastic placement based on real-world data)
- POP design patterns
- Traffic pattern generation
- GNN-based topology generation

These may be added in future versions based on user needs.

## Integration

Will likely become dependency or part of AutoNetKit workflow engine. Designed to be "whiteboard view" that other tools build from.

Used by:
- ANK Workbench (sample gallery)
- netsim (example topologies)
- netvis (visualization testing)

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** mdBook with algorithm details
- **Related:** [ank-pydantic](ank-pydantic) consumes generated topologies

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- CLI usage with various topology types
- Generated YAML topology example
- Visualization of fat-tree topology
- Leaf-spine topology output
- Example topology gallery
- Shell completion demonstration
-->
