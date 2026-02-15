---
layout: default
---

# Network Automation Ecosystem

Tools for network topology modeling, simulation, and visualization.

## Contents
- [Overview](#overview)
- [How They Work Together](#how-they-work-together)
- [The Tools](#the-tools)
  - [Network Simulator](#network-simulator--protocol-validation)
  - [Network Visualization Engine](#network-visualization-engine)
  - [Network Modeling & Configuration Library](#network-modeling--configuration-library)
  - [Network Topology Engine](#network-topology-engine)
  - [Network Automation Workbench](#network-automation-workbench)
  - [Network Traffic Simulator](#network-traffic-simulator--flow-based-performance-analysis)
  - [Topology Generator](#topology-generator)
  - [AutoNetKit](#autonetkit--the-foundation)
- [Getting Started](#getting-started)
- [Source Code](#source-code)

---

## Overview

An integrated ecosystem of tools for network topology modeling, deterministic protocol simulation, and visualization. Design topologies declaratively, validate routing behavior in simulation, and render publication-quality network diagrams — driven from YAML, Python, CLI, or a unified web and text interface.

## How They Work Together

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              Network Automation Workbench                               │
│                    (Orchestration · Web UI · Workflow Management)                       │
│   ┌───────────────────┬──────────────────────────┬─────────────────┬──────────────────┐  │
│   │ Topology Generator│ Modeling & Configuration │ Network Simulator│ Visualization    │  │
│   │                   │ Library                  │                  │ Engine           │  │
└───┴───────────────────┴──────────────────────────┴─────────────────┴──────────────────┴──┘
    │                   │                        │                  │
    │                   │                        │                  │
    │   ┌───────────────▼───────────────┐        │                  │
    │   │     Topology Generator        │        │                  │
    │   │     (Generate Topo)           │        │                  │
    │   └───────────────┬───────────────┘        │                  │
    │                   │                        │                  │
    │                   │                        │                  │
    │   ┌───────────────▼────────────────────────┐                  │
    │   │     Network Modeling &                   │                  │
    │   │     Configuration Library               │                  │
    │   └───────────────┬────────────────────────┘                  │
    │                   │                                           │
    │                   │                                           │
    │   ┌───────────────▼──────────────────────────────────────┐    │
    │   │            Analysis Module                            │    │
    │   │  ┌──────────────────────┬──────────────────────────┐ │    │
    │   │  │ Modeling & Config    │ Network Simulator         │ │    │
    │   │  │ Library              │ (Protocol Behavior)       │ │    │
    │   │  │ (Query & Transform)  │                          │ │    │
    │   │  └──────────────────────┴──────────────────────────┘ │    │
    │   └───────────────┬──────────────────────────────────────┘    │
    │                   │                                           │
    │                   │                                           │
    │   ┌───────────────▼───────────────────┐                       │
    │   │   Network Visualization Engine    │                       │
    │   │   (Visualization)                 │                       │
    │   └───────────────────────────────────┘                       │
    │                                                               │
    └─► Network Automation Workbench coordinates entire pipeline
```

**Workflow:**

1. Generate or create topology (Topology Generator or Network Modeling & Configuration Library)
2. Optionally run simulation to check routing behavior
3. Visualize the topology (Network Visualization Engine)

The Network Automation Workbench provides a web interface to coordinate these tools.

---

## The Tools

### Network Simulator — Protocol Validation

<span class="status-badge status-active">v1.7 — Segment Routing</span> · [Full Details →](projects/network-simulator)

**What It Is:**
A deterministic, tick-based network simulator for rapid prototyping and testing of network configurations. Simulates OSPF, IS-IS, and BGP with packet-level accuracy for quick validation before deployment.

**Rapid Prototyping for Agentic AI & Network Automation:**
The simulator's core value is accelerating the development iteration loop for agentic AI systems and network automation tools. Instead of spinning up containers for every test cycle (minutes), validate configurations in simulation (seconds):

1. **Design topology** with the Network Modeling & Configuration Library
2. **Generate configs** automatically for target platforms
3. **Simulate in seconds** to validate routing behavior
4. **Iterate rapidly** on agent logic, automation scripts, or config templates
5. **Deploy to containers** only after simulation validates the approach

**Daemon Mode — Real-Time Interaction:**
Run simulations as background daemons and interact with them in real-time, like `docker exec` for network simulations:
- **Start a daemon**: `netsim daemon start my-network topology.yaml`
- **Execute commands**: `netsim exec my-network r1 "show ip route"`
- **Attach interactively**: `netsim attach my-network r1` for full REPL console with command history
- **Agent development**: Test automation agents against live network state without container overhead

**Current Status:** v1.7 shipped with SR-MPLS dataplane, interactive console enhancements (TUI device selector, daemon management), L3VPN (VRFs, RD/RT, MP-BGP VPNv4), and BMP telemetry. 130,000+ lines of Rust, 1,350+ tests.

**Tech Stack:** Rust, Tokio, petgraph, gRPC (daemon IPC), ratatui (TUI)

---

### Network Visualization Engine

<span class="status-badge status-active">v1.3 — Embed Readiness & API Stability</span> · [Full Details →](projects/netvis)

**What It Is:**
A Rust-based network topology layout and visualization engine. Renders complex multi-layer networks using advanced layout algorithms (force-directed, hierarchical, geographic, radial) with high-quality static output (SVG, PDF, PNG).

**Key Capabilities:**
- **Automated Layout**: Reduce visual noise in 100+ node topologies
- **Multi-Layer Support**: Visualize logical overlays on physical infrastructure
- **Device-Aware Rendering**: Distinct icons for routers, switches, firewalls, servers, cloud
- **Path Analysis Overlays**: Highlight traffic flows, backup paths, and protocol adjacencies
- **WCAG Contrast**: Accessibility-compliant color schemes and high-contrast themes

![Enterprise Campus](/images/netvis-enterprise-campus.png)
*Enterprise campus network with edge bundling and path analysis overlays.*

![Data Center Fabric](/images/netvis-datacenter-large.png)
*Spine-leaf data center with bandwidth annotations and rack grouping.*

**Current Status:** v1.2 shipped with visual polish and production hardening. v1.3 in progress — stable API, deterministic rendering, geographic layout with real-world coordinates, and spatial indexing for WASM embedding.

**Tech Stack:** Rust, petgraph, fjadra (d3-force port), WASM-ready

---

### Network Modeling & Configuration Library

<span class="status-badge status-active">v1.8 — Performance & Optimization</span> · [Full Details →](projects/ank-pydantic)

**What It Is:**
A Python library for modeling and querying network topologies with type-safe Pydantic models and a Rust core. Expressive Python API backed by compiled graph algorithms (petgraph), with automatic configuration generation for multi-vendor network deployments.

**Key Features:**
- **Two-Stage Transformation Model**: Whiteboard (sketch) → Plan (logical) → Protocol Layers (physical)
- **Type-Safe Models**: Pydantic validation ensures correct topology structure at design time
- **Lazy Query API**: Composable queries with Rust-backed execution (powered by `petgraph`)
- **Configuration Generation**: Automatic multi-vendor config generation (Cisco IOS/IOS-XR/NX-OS, Juniper JunOS, Arista EOS)
- **Batteries-Included Blueprints**: Pre-built domain models for ISIS, MPLS, EVPN, L3VPN, IXP
- **Rust Core (Network Topology Engine)**: Graph operations run at native speed with Python FFI bindings

**Declarative Design:**
```python
from ank_pydantic import Topology
from ank_pydantic.core.designs import build_isis_layer, build_mpls_layer

# Load a declarative topology specification
topo = Topology.from_yaml("campus-network.yaml")

# Query: find all PE routers in the West PoP
west_pes = (topo.query()
    .filter(role="pe", pop="west")
    .select("name", "loopback", "asn")
    .collect())

# Query: trace the path between two nodes
path = topo.query().shortest_path("PE1", "PE4").collect()

# Build protocol layers from the whiteboard topology
build_isis_layer(topo, level=2, area="49.0001")
build_mpls_layer(topo, igp_layer="isis")

# Generate multi-vendor configs
topo.generate_configs(vendors=["cisco_ios", "juniper_junos"])
```

**Current Status:** v1.7 API Usability shipped. Working on v1.8 Performance & Optimization — query performance, profiling infrastructure, and 10k+ node validation.

**Tech Stack:** Python (Pydantic), Network Topology Engine (Rust), PyO3 bindings

---

### Network Topology Engine

<span class="status-badge status-active">Stable</span> · [Full Details →](projects/nte)

**What It Is:**
The Rust graph engine that powers the Network Modeling & Configuration Library. Provides native-speed topology operations exposed to Python through PyO3 bindings.

**Core Capabilities:**
- **Graph Engine**: petgraph `StableDiGraph` for topology representation with stable node/edge indices across mutations
- **Query Engine**: Composable, lazy-evaluated queries over topology attributes — filter by node role, device type, protocol participation, or arbitrary properties. Queries compile to Rust iterators for zero-overhead execution
- **Pluggable Storage**: Three backend options — Polars (columnar analytics), DuckDB (SQL queries over topology data), and Lite (minimal in-memory for embedded use)
- **Monte Carlo Simulation**: Stochastic failure analysis via `nte-monte-carlo` — inject random link/node failures across thousands of iterations to compute availability metrics and identify single points of failure
- **Distributed Computation**: `nte-server` crate for splitting large topology analyses across multiple processes

**Architecture:** Cargo workspace with specialized crates:

| Crate | Purpose |
|-------|---------|
| `nte-core` | Graph representation, node/edge types, topology mutations |
| `nte-query` | Lazy query builder, filter/map/collect pipeline |
| `nte-domain` | Network-specific types (interfaces, protocols, addressing) |
| `nte-backend` | Storage abstraction trait |
| `nte-datastore-polars` | Polars columnar backend for analytics workloads |
| `nte-datastore-duckdb` | DuckDB backend for SQL-based topology queries |
| `nte-datastore-lite` | Minimal HashMap backend for embedding |
| `nte-monte-carlo` | Stochastic simulation (failure injection, availability) |
| `nte-server` | Distributed computation over topology partitions |

**Tech Stack:** Rust, petgraph, Polars, DuckDB, PyO3/Maturin bindings

---

### Network Automation Workbench

<span class="status-badge status-active">v1.3 — Tool Integration & Interactive Workflows</span> · [Full Details →](projects/ank-workbench)

**What It Is:**
A platform that integrates the entire network automation ecosystem into a single workflow. Driven from YAML, a text-based TUI, or the web interface — upload topology YAML, visualize the network, run simulations, and analyze results without switching between tools.

**Milestones:** v1.0 Foundation, v1.1 UX Polish, v1.2 Scale Visualization, v1.3 Tool Integration (current) — simulator integration, interactive device terminals, and live event streaming.

**Tech Stack:** Python (FastAPI), React frontend, integrates all ecosystem components

---

### Network Traffic Simulator — Flow-Based Performance Analysis

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/netflowsim)

**What It Is:**
Flow-based network traffic simulator using analytic queuing models and Monte Carlo simulations. Validates topologies and routing strategies against billions of flow iterations in seconds, providing massive-scale network performance analysis.

**Current Status:** Early development

**Tech Stack:** Rust, Petgraph, Rayon

---

### Topology Generator

<span class="status-badge status-active">Phase 21/24 (89%)</span> · [Full Details →](projects/topogen)

**What It Is:**
A Rust library with Python bindings for generating realistic network topologies. Supports data center (fat-tree, leaf-spine), WAN/backbone (ring, mesh, hierarchical, POP), and random graph patterns. Includes traffic matrix generation, ContainerLab output converter, and vendor-specific interface naming.

**Current Status:** Phase 21/24. Geographic placement, POP design patterns, and multi-layer generation in progress.

**Tech Stack:** Rust core, PyO3 bindings

---

### AutoNetKit — The Foundation

<span class="status-badge status-active">PhD 2017</span> · [Full Details →](projects/autonetkit)

**What It Is:**
The original compiler-based network automation tool from my PhD research. Introduced declarative network design with the Whiteboard → Plan → Build transformation model: specify high-level intent (AS numbers, protocol choices, link roles) in a declarative format, and the compiler derives device-level configurations for multiple vendors automatically.

Integrated into Cisco's VIRL platform for automated multi-vendor lab provisioning. The abstractions pioneered here — layered transformations, declarative topology specification, compiled configuration generation — form the foundation of the current Network Modeling & Configuration Library.

**Current Status:** Maintained for reference. Active development continues in the Network Modeling & Configuration Library and Network Automation Workbench.

---

## Integration Examples

These examples demonstrate how the Network Modeling & Configuration Library, Network Simulator, and Network Visualization Engine work together for end-to-end network design workflows.

### Example 1: Service Provider Core (IS-IS/MPLS/iBGP)

Multi-layer service provider topology showing Network Modeling & Configuration Library → Network Simulator integration.

**Topology Overview:**
- 16 devices: 8 core (P), 6 edge (PE), 2 route reflectors (RR)
- AS 65000, 4 Points of Presence (PoPs): West, East, North, South
- Protocol stack: IS-IS underlay, MPLS/LDP transport, iBGP with RR

**Step 1: Model topology with the Network Modeling & Configuration Library**

```python
from ank_pydantic import Topology
from ank_pydantic.core.designs import build_isis_layer, build_mpls_layer

# Load whiteboard topology (YAML defining 16 routers, PoP locations, roles)
topology = Topology.from_yaml("transitnet-sp-core.yaml")
print(f"Loaded {len(list(topology.layer('input').nodes()))} nodes")
# Output: Loaded 16 nodes

# Build IS-IS Layer (Level 2 flat domain)
isis_layer = build_isis_layer(
    topology,
    level=2,
    area="49.0001",
    parent_layer="physical"
)
print(f"Created {len(list(isis_layer.edges()))} IS-IS adjacencies")
# Output: Created 14 IS-IS adjacencies

# Build MPLS/LDP Layer (follows IS-IS)
mpls_layer = build_mpls_layer(
    topology,
    igp_layer="isis",
    layer_name="mpls"
)
print(f"Created {len(list(mpls_layer.edges()))} LDP sessions")
# Output: Created 14 LDP sessions

# Build iBGP Layer (PE to RR sessions)
rr_nodes = ["RR1", "RR2"]
pe_nodes = ["PE1", "PE2", "PE3", "PE4", "PE5", "PE6"]

print("iBGP Sessions:")
for pe in pe_nodes:
    for rr in rr_nodes:
        print(f"  {pe} <-> {rr} (client-to-RR)")
print(f"  RR1 <-> RR2 (RR-to-RR)")
# Total: 13 iBGP sessions (6 PEs × 2 RRs + 1 RR-RR)
```

**Step 2: Export for Network Simulator validation**

```python
# Export topology for protocol simulation
topology.export_netsim("transitnet-netsim.yaml")
```

**Step 3: Validate with the Network Simulator**

```bash
$ netsim run transitnet-netsim.yaml

[t=0ms] Network initialized: 16 devices, 14 links
[t=5ms] IS-IS: Adjacencies Up (14 adjacencies)
[t=12ms] IS-IS: SPF calculation complete (all routers)
[t=20ms] MPLS: Label bindings distributed
[t=30ms] BGP: iBGP sessions Up (13 sessions, 2 RRs)
[t=35ms] Network converged

Simulation complete: 35ms simulated
- 16 IS-IS routers, 14 adjacencies
- 14 LDP sessions, labels distributed
- 13 iBGP sessions, 2 route reflectors
```

**Step 4: Visualize with the Network Visualization Engine**

```python
# Export for visualization
topology.export_for_netvis("transitnet-vis.json", layout="hierarchical", node_metadata=True)
```

```bash
$ netvis render transitnet-vis.json --layout hierarchical --output transitnet.svg
Loaded topology: 16 nodes, 14 edges
Rendering to SVG...
Written: transitnet.svg
```

The Network Visualization Engine renders the topology with device-aware icons, PoP grouping, and protocol overlay annotations.

**Key Insight:** The Network Modeling & Configuration Library's design functions automatically derive protocol layers from the whiteboard topology, the Network Simulator validates convergence in seconds, and the Network Visualization Engine renders the result.

---

### Example 2: Data Center Fabric (EVPN/VXLAN) — Proposed

**Topology:**
- Spine-leaf architecture: 4 spines, 8 leafs
- eBGP underlay (unique ASN per switch)
- iBGP EVPN overlay (spines as route reflectors)
- VXLAN tunnels for L2 extension across fabric

**Network Modeling & Configuration Library workflow:**
```python
from ank_pydantic.blueprints.designs.datacenter import build_spine_leaf_fabric
from ank_pydantic.blueprints.designs.evpn import build_evpn_overlay

# Generate spine-leaf physical topology
fabric = build_spine_leaf_fabric(
    num_spines=4,
    num_leafs=8,
    link_speed="100G"
)

# Add eBGP underlay (RFC 7938 - unique ASN per leaf)
underlay = build_ebgp_underlay(
    fabric,
    asn_base=65100,  # Spine ASNs: 65100-65103
    leaf_asn_base=65200  # Leaf ASNs: 65200-65207
)

# Add EVPN overlay
overlay = build_evpn_overlay(
    fabric,
    route_reflectors=["spine-1", "spine-2", "spine-3", "spine-4"],
    vnis=[10001, 10002, 10003]  # Tenant VNIs
)

# Export for validation
fabric.export_netsim("dc-fabric-netsim.yaml")
```

**Network Simulator validation:**
- Verify eBGP underlay convergence
- Check EVPN Type-2 MAC routes advertised
- Validate VXLAN tunnel establishment
- Test L2 connectivity across fabric

---

### Example 3: L3VPN Service Provisioning — Proposed

**Topology:**
- SP core from Example 1 (IS-IS/MPLS)
- 3 customer sites requiring VPN connectivity
- VRFs on PE routers with RT import/export

**Network Modeling & Configuration Library workflow:**
```python
from ank_pydantic.blueprints.designs.l3vpn import provision_l3vpn

# Start with existing SP core
sp_core = Topology.from_yaml("transitnet-sp-core.yaml")

# Add L3VPN service for customer "ACME Corp"
l3vpn = provision_l3vpn(
    sp_core,
    vpn_name="ACME-CORP-VPN",
    vrf_rd="65000:100",
    rt_import=["65000:100"],
    rt_export=["65000:100"],
    customer_sites=[
        {"pe": "PE1", "ce": "ACME-HQ", "interface": "ge-0/0/1", "vlan": 100},
        {"pe": "PE3", "ce": "ACME-DC", "interface": "ge-0/0/1", "vlan": 100},
        {"pe": "PE5", "ce": "ACME-REMOTE", "interface": "ge-0/0/1", "vlan": 100}
    ]
)

# Generate VRF configs on PE routers
l3vpn.export_netsim("l3vpn-netsim.yaml")
```

**Network Simulator validation:**
- Verify VRF configuration on PEs
- Check MP-BGP VPNv4 routes exchanged
- Validate end-to-end customer connectivity
- Test route leaking between VRFs

---

### Example 4: Multi-Vendor IXP Peering — Proposed

**Topology:**
- Internet Exchange Point with route servers
- Members: 3 ISPs (Cisco, Juniper, Arista platforms)
- BGP communities for routing policy

**Network Modeling & Configuration Library workflow:**
```python
from ank_pydantic.blueprints.designs.ixp import build_ixp_fabric

# Create IXP peering fabric
ixp = build_ixp_fabric(
    name="MetroIX",
    peering_lan="192.0.2.0/24",
    route_servers=[
        {"name": "rs1", "ip": "192.0.2.1"},
        {"name": "rs2", "ip": "192.0.2.2"}
    ],
    members=[
        {"name": "ISP-A", "asn": 64510, "ip": "192.0.2.10", "platform": "iosxr"},
        {"name": "ISP-B", "asn": 64520, "ip": "192.0.2.20", "platform": "junos"},
        {"name": "ISP-C", "asn": 64530, "ip": "192.0.2.30", "platform": "eos"}
    ]
)

# Add route server BGP sessions
ixp.add_route_server_sessions(transparent_asn=True)

# Export multi-vendor configs
ixp.export_netsim("ixp-netsim.yaml")
```

**Network Simulator validation:**
- Verify BGP sessions to route servers
- Check transparent AS path handling
- Validate community-based filtering

---

[← Back to Projects](projects)

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
