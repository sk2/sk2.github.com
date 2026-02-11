---
layout: default
---

# Network Automation Ecosystem

A comprehensive suite of tools for network design, validation, simulation, and visualization — from topology modeling to protocol-level simulation to production-quality rendering.

---

## The Vision

Network engineering traditionally fragments across disconnected tools: design in one tool, validate in another, visualize in a third. This ecosystem provides an integrated workflow where topology models flow seamlessly from design through simulation to visualization, with consistent data structures and APIs throughout.

**Core Philosophy:**
- **Declarative over imperative**: Define *what* the network should do, not *how* to configure it
- **Type-safe modeling**: Catch errors at design time, not deployment time
- **Protocol-level fidelity**: Simulate routing protocol behavior, not just connectivity
- **Performance without compromise**: Rust cores with Python bindings where ergonomics matter
- **Composable components**: Each tool solves one problem well and integrates cleanly with others

## How They Work Together

```
┌─────────────────────────────────────────────────────────────┐
│                      ANK Workbench                          │
│        (Unified Platform - Web UI + Orchestration)          │
└────────────────┬───────────────────────────┬────────────────┘
                 │                           │
        ┌────────▼─────────┐        ┌────────▼─────────┐
        │  ank_pydantic    │        │    TopoGen       │
        │  (Topology API)  │        │  (Generate)      │
        └────────┬─────────┘        └────────┬─────────┘
                 │                           │
                 └──────────┬────────────────┘
                            │
              ┌─────────────▼──────────────┐
              │     Network Simulator      │
              │   (Protocol Validation)    │
              └─────────────┬──────────────┘
                            │
              ┌─────────────▼──────────────┐
              │         NetVis             │
              │   (Visualization Engine)   │
              └────────────────────────────┘
```

**Typical Workflow:**
1. **Design**: Use `TopoGen` to generate realistic topologies or `ank_pydantic` to model networks declaratively
2. **Validate**: Run the `Network Simulator` to verify routing protocol behavior and catch misconfigurations
3. **Visualize**: Use `NetVis` to render topology layouts with advanced algorithms
4. **Deploy**: Generate vendor-specific configurations (future ANK Workbench capability)

All orchestrated through **ANK Workbench** — a unified web interface for the complete workflow.

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
```

**Current Status:** Feature-complete, final polish and documentation before 1.0 release.

**Tech Stack:** Python (Pydantic), Rust core (`petgraph`-backed), PyO3 bindings

---

### Network Simulator (netsim) — Protocol Validation

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/network-simulator)

**What It Is:**
A deterministic, tick-based network simulator that models packet-level routing protocol behavior. It's the middle ground between pure algorithmic analysis (C-BGP) and full device emulation (Containerlab) — protocol-level fidelity without the resource cost of running actual network operating systems.

**Key Features:**
- **Deterministic Simulation**: Tick-based execution ensures reproducible results
- **Protocol Implementations**: OSPF, IS-IS, BGP with packet-level accuracy
- **Fast Validation**: Simulate 100+ node topologies in seconds
- **RIB/FIB Separation**: Models routing decisions (control plane) and forwarding behavior (data plane)
- **Comprehensive Testing**: 1,350+ tests validate protocol behavior against RFCs
- **Parallel Execution**: Multi-core support for large topologies

**Protocol Coverage:**
- **Layer 2**: Ethernet, ARP
- **Layer 3**: IPv4, ICMPv4
- **Routing**: OSPF (full), IS-IS (in progress), BGP (planned)
- **MPLS**: LDP, RSVP-TE (planned)

**Example Scenarios:**
- Detect routing loops before deployment
- Validate convergence behavior during link failures
- Test traffic engineering policies
- Smoke test configuration changes

**Current Status:** v1.6 shipped with OSPF support. 126,000 lines of Rust, 122 requirements met (35 MVP + 87 advanced).

**Tech Stack:** Rust, Tokio for async execution, petgraph for topology representation

---

### NetVis — Visualization Engine

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/netvis)

**What It Is:**
A Rust-based network topology layout and visualization engine that transforms complex multi-layer networks into clear, information-dense renderings. Advanced layout algorithms minimize visual complexity while preserving structural clarity.

**Key Features:**
- **Advanced Layout Algorithms**:
  - Force-directed layout with configurable parameters
  - Hierarchical layout for tree-like topologies
  - Geographic layout for physical infrastructure
  - Edge bundling to reduce visual clutter
- **Multi-Layer Support**: Visualize L2, L3, and logical layers simultaneously
- **Static Output Formats**: SVG, PDF, PNG (v1 focus)
- **High-Quality Rendering**: Anti-aliased, publication-ready graphics
- **Topology Awareness**: Uses `petgraph` for graph analysis

**Use Cases:**
- Network documentation
- Change impact visualization
- Capacity planning
- Architectural reviews
- Incident response (understand blast radius)

**Current Status:** Core layout algorithms implemented, refining edge bundling and multi-layer rendering. Interactive browser embedding planned for v2.

**Tech Stack:** Rust, petgraph for graph algorithms, SVG/PDF rendering libraries

---

### TopoGen — Topology Generator

<span class="status-badge status-active">Phase 17/24 (11%)</span> · [Full Details →](projects/topogen)

**What It Is:**
A Rust library with Python bindings for generating realistic network topologies. Consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools into one well-tested implementation.

**Key Features:**
- **Realistic Topology Types**:
  - Data center: Spine-leaf, fat-tree, Clos
  - WAN: Hub-and-spoke, ring, full mesh, partial mesh
  - Random graphs: Erdős-Rényi, Barabási-Albert, Watts-Strogatz
- **Design Pattern Awareness**: Generates topologies that reflect real-world network design
- **Configurable Parameters**: Node count, link capacity, failure domains, geographic distribution
- **Custom YAML Output**: Compatible with ank_pydantic and other ecosystem tools
- **Python Bindings**: Ergonomic API for scripting and integration

**Example Usage:**
```python
from topogen import DataCenter

# Generate 4-pod spine-leaf topology
topo = DataCenter.spine_leaf(
    num_pods=4,
    spines_per_pod=2,
    leaves_per_pod=4,
    servers_per_leaf=8
)
topo.export_yaml("dc-topology.yaml")
```

**Current Status:** Early development, focusing on core algorithms and Python bindings.

**Tech Stack:** Rust core, PyO3 for Python bindings

---

### AutoNetkit — The Foundation

<span class="status-badge status-active">PhD 2017</span> · [Full Details →](projects/autonetkit)

**What It Is:**
The original compiler-based network automation tool from my PhD research. AutoNetkit introduced the concept of treating network configuration as a compilation problem — transform high-level intent into vendor-specific configuration through a series of graph transformations.

**Historical Significance:**
- **First Implementation**: Declarative network design with multi-vendor support
- **Industry Adoption**: Integrated into Cisco VIRL (Virtual Internet Routing Lab)
- **Open Source Pioneer**: Presented at PyCon AU 2013, widely used in academic research
- **Design Patterns**: Established the Whiteboard → Plan → Build transformation model now used in ank_pydantic

**Why It Matters:**
AutoNetkit proved that declarative, intent-based network automation could work at scale. The lessons learned — graph-based modeling, type safety, vendor abstraction — directly inform the design of the modern ANK ecosystem.

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

**For Researchers:**
1. Review **AutoNetkit** papers and thesis for theoretical foundations
2. Use **TopoGen** for reproducible topology generation in experiments
3. Cite the relevant papers (see individual project pages)

---

## Philosophy: Why This Approach?

### Type Safety Over Runtime Errors
Pydantic models catch topology errors at design time. Invalid node types, missing interfaces, and broken references fail fast rather than causing cryptic runtime errors during simulation or deployment.

### Rust for Performance-Critical Paths
Graph algorithms (path finding, centrality, layout) run in Rust with Python bindings. Engineers get Python ergonomics for modeling, Rust speed for computation.

### Protocols, Not Emulation
Simulating OSPF/BGP logic is 100x faster than running actual network OS instances. For validation and testing, protocol-level fidelity is sufficient — you don't need a full kernel.

### Declarative Over Imperative
Define *what* the network should do (all routers run OSPF, advertise loopbacks) rather than *how* to configure it (87 lines of Cisco IOS commands per router). The compiler handles vendor-specific syntax.

### Composable Tools Over Monoliths
Each tool solves one problem well and integrates via standard formats (YAML topologies, JSON APIs). Use the whole stack or just the pieces you need.

---

## Open Source & Contributions

All projects are open source and actively developed. Contributions welcome:

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
