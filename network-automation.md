---
layout: default
---

# Network Automation Ecosystem

Tools for network topology modeling, simulation, and visualization.

---

## Overview

A set of tools that work together: generate or model topologies, run basic protocol simulations, and render network diagrams.

## How They Work Together

```
┌──────────────────────────────────────────────────────────────────┐
│                        ANK Workbench                             │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │ ank_pydantic │   Simulator  │    NetVis    │ │
└───┴──────────────┴──────────────┴──────────────┴──────────────┴─┘
    │              │              │              │
    │              │              │              │
    │   ┌──────────▼──────────┐   │              │
    │   │     TopoGen         │   │              │
    │   │  (Generate Topo)    │   │              │
    │   └──────────┬──────────┘   │              │
    │              │               │              │
    │              │               │              │
    │   ┌──────────▼──────────────────────┐      │
    │   │       ank_pydantic              │      │
    │   │   (Topology Modeling API)       │      │
    │   └──────────┬──────────────────────┘      │
    │              │                              │
    │              │                              │
    │   ┌──────────▼─────────────────────────────────────┐
    │   │            Analysis Module                      │
    │   │  ┌─────────────────────┬─────────────────────┐ │
    │   │  │  ank_pydantic       │ Network Simulator   │ │
    │   │  │  (Query & Transform)│ (Protocol Behavior) │ │
    │   │  └─────────────────────┴─────────────────────┘ │
    │   └──────────┬──────────────────────────────────────┘
    │              │
    │              │
    │   ┌──────────▼──────────┐
    │   │       NetVis        │
    │   │   (Visualization)   │
    │   └─────────────────────┘
    │
    └─► ANK Workbench coordinates entire pipeline
```

**Workflow:**

1. Generate or create topology (TopoGen or ank_pydantic)
2. Optionally run simulation to check routing behavior
3. Visualize the topology (NetVis)

ANK Workbench provides a web interface to coordinate these tools.

---

## The Tools

### ANK Workbench — Unified Platform

<span class="status-badge status-active">Phase 18/19 (98%)</span> · [Full Details →](projects/ank-workbench)

**What It Is:**
A web-based platform that integrates the entire network automation ecosystem into a single workflow. Upload topology YAML, visualize the network, run simulations, and analyze results without switching between tools.

**Key Features:**
- **Unified Web Interface**: React/Vue frontend with modern UX
- **Topology Management**: Import, edit, and version control network designs
- **Integrated Simulation**: One-click validation with netsim
- **Live Visualization**: Interactive topology rendering with NetVis
- **Results Analysis**: Compare configuration states, routing tables, and protocol behavior

**Current Status:** Near production-ready. Core integration complete, polishing UI/UX and adding advanced workflow features.

**Tech Stack:** Python backend (FastAPI/Flask), React or Vue frontend, integrates all ANK ecosystem components

---

### ank_pydantic — Topology Modeling Library

<span class="status-badge status-active">Phase 59/62 (99%)</span> · [Full Details →](projects/ank-pydantic)

**What It Is:**
A Python library for modeling and querying network topologies with type-safe Pydantic models and a high-performance Rust core. Think of it as SQLAlchemy for network topologies — expressive Python API backed by blazing-fast graph algorithms.

**Key Features:**
- **Two-Stage Transformation Model**: Whiteboard (sketch) → Plan (logical) → Protocol Layers (physical)
- **Type-Safe Models**: Pydantic validation ensures correct topology structure at design time
- **Lazy Query API**: Composable queries with Rust-backed execution (powered by `petgraph`)
- **Batteries-Included Blueprints**: Pre-built domain models for ISIS, MPLS, EVPN, L3VPN, IXP
- **Rust Core (`ank_nte`)**: Graph operations run at native speed with Python FFI bindings

**Example Usage:**
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

**Integration with NetVis:**
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

**Current Status:** Feature-complete, final polish and documentation before 1.0 release.

**Tech Stack:** Python (Pydantic), Rust core (`petgraph`-backed), PyO3 bindings

---

### Network Simulator (netsim) — Protocol Validation

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/network-simulator)

**What It Is:**
A deterministic, tick-based network simulator for rapid prototyping and testing of network configurations. Simulates OSPF, IS-IS, and BGP with packet-level accuracy for quick validation before deployment.

**Current Status:** v1.6 shipped with OSPF support

**Tech Stack:** Rust, Tokio, petgraph

---

### NetFlow Sim — Flow-Based Performance Analysis

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/netflowsim)

**What It Is:**
High-performance flow-based network simulator using analytic queuing models and Monte Carlo simulations. Validates topologies and routing strategies against billions of flow iterations in seconds, providing massive-scale network performance analysis.

**Current Status:** Early development

**Tech Stack:** Rust, Petgraph, Rayon

---

### NetVis — Visualization Engine

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/netvis)

**What It Is:**
A Rust-based network topology layout and visualization engine. Renders complex multi-layer networks using advanced layout algorithms (force-directed, hierarchical, geographic) with high-quality static output (SVG, PDF, PNG).

**Current Status:** Core layout algorithms implemented

**Tech Stack:** Rust, petgraph

---

<span class="status-badge status-active">Phase 17/24 (11%)</span> · [Full Details →](projects/topogen)

**What It Is:**
A Rust library with Python bindings for generating realistic network topologies. Supports data center (spine-leaf, fat-tree), WAN (hub-spoke, mesh), and random graph patterns.

**Current Status:** Early development

**Tech Stack:** Rust core, PyO3 bindings

```

**Current Status:** Early development, focusing on core algorithms and Python bindings.
<span class="status-badge status-active">PhD 2017</span> · [Full Details →](projects/autonetkit)

**What It Is:**
The original compiler-based network automation tool from my PhD research. Introduced declarative network design with the Whiteboard → Plan → Build transformation model, integrated into Cisco VIRL.

**Current Status:** Maintained for reference. Active development moved to ank_pydantic and ANK Workbench.

**Tech Stack:** Python, NetworkX

**Current Status:** Maintained for historical reference and research use. Active development has moved to ank_pydantic and ANK Workbench, which implement the same concepts with modern tooling.

**Tech Stack:** Python, NetworkX for graph operations

---

## Getting Started

**For Network Engineers:**
1. Start with **ANK Workbench** (coming soon) — the unified web interface for the entire workflow
2. Explore **ank_pydantic** for programmatic topology modeling
3. Use **Network Simulator** for validation and testing

**For Developers:**
1. Check out **ank_pydantic** for the Python API and documentation
2. Explore **netsim** source code for protocol implementation details
3. Contribute to **NetVis** for visualization algorithms

---

## Source Code

- **ank_pydantic**: [github.com/sk2/ank_pydantic](https://github.com/sk2/ank_pydantic)
- **netsim**: [github.com/sk2/netsim](https://github.com/sk2/netsim)
- **NetVis**: [github.com/sk2/netvis](https://github.com/sk2/netvis)
- **TopoGen**: [github.com/sk2/topogen](https://github.com/sk2/topogen)
- **AutoNetkit**: [github.com/sk2/autonetkit](https://github.com/sk2/autonetkit)

---

[← Back to Projects](projects) | [View CV](cv) | [Development Philosophy](development)

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
.status-planning {
  background-color: #ffc107;
  color: #343a40;
}
</style>
