---
layout: default
---

# ank_pydantic

<span class="status-badge status-active">Phase 59/62 (100%)</span>

[← Back to Projects](../projects)

---


## The Insight

Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. **ank-pydantic** eliminates this trade-off by using Pydantic for schema validation and a high-performance Rust core (`petgraph`) for graph traversals.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 59/62 (99%) |
| **Language** | Python, Rust |
| **Started** | 2025 |

---

## What This Is

A Python library for modeling and querying network topologies with type-safe Pydantic models and a high-performance Rust core. Think of it as SQLAlchemy for network topologies — expressive Python API backed by blazing-fast graph algorithms.

## Key Features

- **Two-Stage Transformation Model**: Whiteboard (sketch) → Plan (logical) → Protocol Layers (physical)
- **Type-Safe Models**: Pydantic validation ensures correct topology structure at design time
- **Lazy Query API**: Composable queries with Rust-backed execution (powered by `petgraph`)
- **Batteries-Included Blueprints**: Pre-built domain models for ISIS, MPLS, EVPN, L3VPN, IXP
- **Rust Core (`ank_nte`)**: Graph operations run at native speed with Python FFI bindings

## Example Usage

```python
from ank_pydantic import Topology, Node, Edge

# Create topology
topo = Topology()
r1 = topo.add_node(Node(name="router1", device_type="cisco_ios"))
r2 = topo.add_node(Node(name="router2", device_type="juniper_junos"))
topo.add_edge(Edge(src=r1, dst=r2, interface="ge-0/0/0"))

# Query with lazy evaluation
border_routers = topo.query().filter(role="border").collect()

# Transform to protocol layers
topo.transform_to_protocol("ospf")

# Export for visualization
topo.export_for_netvis("topology.json")
```

## Integration with NetVis

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

Feature-complete, final polish and documentation before 1.0 release.

## Tech Stack

Python (Pydantic), Rust core (`petgraph`-backed), PyO3 bindings

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
