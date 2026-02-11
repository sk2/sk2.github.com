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

**Design-to-Visualization Workflow:**

1. **Generate** (`TopoGen`)
   - Create realistic topologies (spine-leaf, WAN, random graphs)
   - Output YAML with nodes, links, and parameters

2. **Model** (`ank_pydantic`)
   - Load topology into type-safe Python API
   - Transform through layers (Whiteboard → Plan → Protocol)
   - Query relationships, compute paths, assign addressing

3. **Analyze** (Analysis Module)
   - **ank_pydantic**: Query topology structure, compute metrics
   - **Network Simulator**: Validate protocol behavior, test failover scenarios
   - Combined analysis identifies issues before deployment

4. **Visualize** (`NetVis`)
   - Render topology with advanced layout algorithms
   - Show analysis results (failed routes, bottlenecks, coverage)
   - Generate documentation-quality diagrams

5. **Orchestrate** (`ANK Workbench`)
   - Web UI manages entire pipeline
   - One-click workflow execution
   - Interactive result exploration

**Example End-to-End:**
```
TopoGen: Generate 4-pod spine-leaf topology
  ↓
ank_pydantic: Load YAML, apply OSPF+BGP transformations
  ↓
Analysis:
  ├─ ank_pydantic: Verify all leaf-spine links present, compute redundancy
  └─ Network Simulator: Validate OSPF convergence, test link failure scenarios
  ↓
NetVis: Render hierarchical layout with color-coded health status
  ↓
ANK Workbench: Display results, allow parameter tweaks, re-run workflow
```

All orchestrated through **ANK Workbench** — a unified web interface for the complete network automation pipeline.

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
A deterministic, tick-based network simulator that models packet-level routing protocol behavior. It's the middle ground between pure algorithmic analysis (C-BGP) and full device emulation (Containerlab) — protocol-level fidelity without the resource cost of running actual network operating systems.

**Key Features:**
- **Deterministic Simulation**: Tick-based execution ensures reproducible results
- **Protocol Implementations**: OSPF, IS-IS, BGP with packet-level accuracy
- **Fast Validation**: Simulate 100+ node topologies in seconds
- **RIB/FIB Separation**: Models routing decisions (control plane) and forwarding behavior (data plane)
- **Comprehensive Testing**: 1,350+ tests validate protocol behavior against RFCs
- **Parallel Execution**: Multi-core support for large topologies

**Detailed Protocol Support:**

**Layer 2: Data Link**
- **Ethernet**: Full IEEE 802.3 frame handling with MAC learning
- **ARP**: Address Resolution Protocol for IPv4-to-MAC mapping
- **Switching**: VLAN-aware forwarding with MAC address tables

**Layer 3: Network**
- **IPv4**: Complete packet forwarding with TTL decrement, fragmentation handling
- **ICMPv4**: Echo request/reply, destination unreachable, time exceeded
- **Routing Table**: Longest-prefix-match lookups with administrative distance

**OSPF (RFC 2328 - OSPFv2):**
- **Neighbor Discovery**: Hello protocol with dead interval detection
- **Link State Database**: Full LSA flooding with sequence number validation
- **SPF Calculation**: Dijkstra's algorithm for shortest path computation
- **Areas**: Single-area and multi-area with ABR support
- **Network Types**: Broadcast, point-to-point, NBMA
- **Metrics**: Interface cost calculation and cumulative path costs
- **Convergence**: Sub-second convergence for typical topologies

**IS-IS (ISO 10589):**
- **Level 1/Level 2**: Intra-area and inter-area routing
- **TLV Encoding**: Proper handling of IS-IS TLV structures
- **Pseudonodes**: LAN representation with designated IS election
- **Metrics**: Wide metrics (32-bit) and narrow metrics (6-bit) support

**BGP (RFC 4271 - BGP-4) - In Development:**
- **Session Management**: TCP-based peering with keepalive/hold timers
- **Path Attributes**: AS_PATH, NEXT_HOP, LOCAL_PREF, MED
- **Route Selection**: Full BGP decision process implementation
- **Policy**: Community-based filtering and attribute manipulation

**MPLS - Planned:**
- **LDP**: Label distribution for IP prefixes
- **RSVP-TE**: Traffic engineering with explicit paths
- **Fast Reroute**: Link/node protection with backup tunnels

**Example: OSPF Triangle Topology**

Input topology (`ospf-triangle.yaml`):
```yaml
name: ospf-triangle
description: Three OSPF routers in a triangle with hosts

devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: eth0
        ip: 10.0.12.1/24
        ospf: { area: 0, cost: 10 }
      - name: eth1
        ip: 10.0.13.1/24
        ospf: { area: 0, cost: 10 }
      - name: eth2
        ip: 10.0.1.1/24
        ospf: { area: 0, cost: 1 }

  - name: r2
    type: router
    router_id: 2.2.2.2
    interfaces:
      - name: eth0
        ip: 10.0.12.2/24
        ospf: { area: 0, cost: 10 }
      - name: eth1
        ip: 10.0.23.2/24
        ospf: { area: 0, cost: 10 }

  - name: r3
    type: router
    router_id: 3.3.3.3
    interfaces:
      - name: eth0
        ip: 10.0.13.3/24
        ospf: { area: 0, cost: 10 }
      - name: eth1
        ip: 10.0.23.3/24
        ospf: { area: 0, cost: 10 }

  - name: h1
    type: host
    interfaces:
      - name: eth0
        ip: 10.0.1.10/24
        gateway: 10.0.1.1

  - name: h3
    type: host
    interfaces:
      - name: eth0
        ip: 10.0.3.10/24
        gateway: 10.0.3.1

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r1:eth1, r3:eth0]
  - endpoints: [r2:eth1, r3:eth1]
  - endpoints: [r1:eth2, h1:eth0]
  - endpoints: [r3:eth2, h3:eth0]

script:
  - at: converged
    device: r1
    command: show ip route
  - at: converged + 100
    device: h1
    command: ping 10.0.3.10
```

Run simulation:
```bash
$ netsim run ospf-triangle.yaml

[t=0ms] Network initialized: 5 devices, 5 links
[t=0ms] OSPF: r1, r2, r3 sending Hello on all interfaces
[t=10ms] OSPF: Neighbors established (r1<->r2, r1<->r3, r2<->r3)
[t=15ms] OSPF: LSA flooding in progress
[t=20ms] OSPF: SPF calculation complete on all routers
[t=20ms] Network converged

[t=20ms] r1> show ip route
10.0.1.0/24   directly connected (eth2)
10.0.3.0/24   via 10.0.13.3 [OSPF/110] metric=11
10.0.12.0/24  directly connected (eth0)
10.0.13.0/24  directly connected (eth1)
10.0.23.0/24  via 10.0.12.2 [OSPF/110] metric=20

[t=120ms] h1> ping 10.0.3.10
PING 10.0.3.10: 64 bytes from 10.0.3.10: icmp_seq=1 ttl=62 time=2.1ms
Round-trip path: h1 -> r1 -> r3 -> h3 -> r3 -> r1 -> h1

Simulation complete: 120ms simulated, 0.034s real time (3529x speedup)
```

**Use Cases:**
- **Pre-deployment Validation**: Catch routing loops, black holes, and misconfigurations before production
- **Convergence Analysis**: Measure failover time and validate backup paths
- **Capacity Planning**: Test network behavior under scaled topologies
- **Protocol Verification**: Validate RFC compliance for custom implementations
- **Training**: Safe environment for learning routing protocol behavior

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

**Example: Quick Start**

Input (Rust API):
```rust
use netvis::{EdgeData, ForceDirectedLayout, Layout,
              NetVisGraph, NodeData, Renderer, SvgRenderer};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create graph with typed nodes
    let mut graph = NetVisGraph::new();

    let r1 = graph.add_node(NodeData::new("r1").node_type("router"));
    let r2 = graph.add_node(NodeData::new("r2").node_type("router"));
    let s1 = graph.add_node(NodeData::new("s1").node_type("switch"));
    let s2 = graph.add_node(NodeData::new("s2").node_type("switch"));
    let h1 = graph.add_node(NodeData::new("h1").node_type("host"));
    let h2 = graph.add_node(NodeData::new("h2").node_type("host"));

    // Add edges with weights
    graph.add_edge(r1, s1, EdgeData::new(1.0));
    graph.add_edge(r1, s2, EdgeData::new(1.0));
    graph.add_edge(r2, s1, EdgeData::new(1.0));
    graph.add_edge(r2, s2, EdgeData::new(1.0));
    graph.add_edge(s1, h1, EdgeData::new(1.0));
    graph.add_edge(s2, h2, EdgeData::new(1.0));
    graph.add_edge(s1, s2, EdgeData::new(0.5));

    // Apply force-directed layout
    let layout = ForceDirectedLayout::new().seed(42);
    let scene = layout.layout(&graph)?;

    // Render to SVG
    SvgRenderer::default()
        .render_to_file(&scene, 800.0, 600.0, "output.svg")?;

    Ok(())
}
```

**Example Output: Data Center Topology**

A real-world data center spine-leaf topology rendered with NetVis:

![NetVis Data Center Example](images/netvis-datacenter-example.svg)

This visualization shows:
- **Hierarchical Layout**: Spine layer at top, leaf layer below
- **Node Differentiation**: Different visual styles for device types
- **Clean Edge Routing**: Minimal crossings, readable even at scale
- **Information Density**: Compact representation without cluttering

**Use Cases:**
- **Network Documentation**: Auto-generate topology diagrams from inventory
- **Change Impact Visualization**: Show blast radius of configuration changes
- **Capacity Planning**: Identify bottlenecks and underutilized links
- **Architectural Reviews**: Present network designs to stakeholders
- **Incident Response**: Quickly understand failure domains and dependencies

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

**Example: Data Center Leaf-Spine**

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

**Python API:**
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

**The Transformation Model:**

AutoNetkit pioneered a multi-stage compilation approach:

**1. Whiteboard Layer** (High-level intent)
```python
# Simple topology definition
router("r1", asn=65000)
router("r2", asn=65000)
router("r3", asn=65001)

link(r1, r2, protocol="ospf")
link(r2, r3, protocol="bgp")
```

**2. Plan Layer** (Protocol-specific graphs)
```
OSPF Graph:
  r1 [area=0, router_id=1.1.1.1]
  r2 [area=0, router_id=2.2.2.2]
  r1 -- r2 [cost=10, network=10.0.12.0/24]

BGP Graph:
  r2 [asn=65000, router_id=2.2.2.2]
  r3 [asn=65001, router_id=3.3.3.1]
  r2 -- r3 [peer_type="ebgp", network=10.0.23.0/24]
```

**3. Build Layer** (Vendor-specific configuration)

*Cisco IOS (r1):*
```
interface GigabitEthernet0/0
 ip address 10.0.12.1 255.255.255.0
 no shutdown

router ospf 1
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.255 area 0
```

*Juniper JunOS (r3):*
```
interfaces {
    ge-0/0/0 {
        unit 0 {
            family inet {
                address 10.0.23.3/24;
            }
        }
    }
}

protocols {
    bgp {
        group ebgp {
            type external;
            peer-as 65000;
            neighbor 10.0.23.2;
        }
    }
}
```

**Example Workflow:**
```python
import autonetkit

# Load topology from GraphML
topo = autonetkit.load("topology.graphml")

# Apply design rules
topo.compile(
    protocols=["ospf", "bgp", "isis"],
    ip_allocation="hierarchical"
)

# Generate configurations for multiple vendors
configs = topo.build(
    targets=["cisco_ios", "juniper_junos", "arista_eos"]
)

# Deploy or simulate
topo.deploy_to_virl()
```

**Key Innovation:**
Separating *what* (Whiteboard: "these routers run OSPF") from *how* (Build: vendor-specific OSPF syntax) allows one topology definition to generate configurations for multiple vendors. The Plan layer captures protocol semantics independent of vendor implementation.

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
