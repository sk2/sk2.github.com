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
  - [Topology Modeling Library](#topology-modeling-library)
  - [Network Topology Engine](#network-topology-engine)
  - [Network Automation Workbench](#network-automation-workbench)
  - [Network Traffic Simulator](#network-traffic-simulator--flow-based-performance-analysis)
  - [Topology Generator](#topology-generator)
  - [AutoNetKit](#autonetkit--the-foundation)
- [Getting Started](#getting-started)
- [Source Code](#source-code)

---

## Overview

An integrated ecosystem of high-performance tools for network topology modeling, deterministic protocol simulation, and visualization. Design topologies declaratively, validate routing behavior in simulation, and render publication-quality network diagrams — driven from YAML, Python, CLI, or a unified web and text interface.

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

### Network Simulator — Protocol Validation

<span class="status-badge status-active">v1.7 — Segment Routing</span> · [Full Details →](projects/network-simulator)

**What It Is:**
A deterministic, tick-based network simulator for rapid prototyping and testing of network configurations. Simulates OSPF, IS-IS, and BGP with packet-level accuracy for quick validation before deployment.

**Rapid Prototyping for Agentic AI & Network Automation:**
The simulator's core value is accelerating the development iteration loop for agentic AI systems and network automation tools. Instead of spinning up containers for every test cycle (minutes), validate configurations in simulation (seconds):

1. **Design topology** with ank_pydantic
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
- **CI/CD integration**: Start daemon, run tests via `exec`, collect results, stop daemon

**Current Status:** v1.6 shipped with L3VPN (VRFs, RD/RT, MP-BGP VPNv4), daemon mode with interactive console (command abbreviation, tab completion), and BMP telemetry. v1.7 adds SR-MPLS dataplane support. 126,000+ lines of Rust, 1,350+ tests.

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

**Current Status:** v1.2 shipped with visual polish and production hardening. Working on v1.3 API stability and WASM embedding for ANK Workbench integration.

**Tech Stack:** Rust, petgraph, fjadra (d3-force port), WASM-ready

---

### Topology Modeling Library

<span class="status-badge status-active">v1.8 — Performance & Optimization</span> · [Full Details →](projects/ank-pydantic)

**What It Is:**
A Python library for modeling and querying network topologies with type-safe Pydantic models and a high-performance Rust core. Expressive Python API backed by blazing-fast graph algorithms, with automatic configuration generation for multi-vendor network deployments.

**Key Features:**
- **Two-Stage Transformation Model**: Whiteboard (sketch) → Plan (logical) → Protocol Layers (physical)
- **Type-Safe Models**: Pydantic validation ensures correct topology structure at design time
- **Lazy Query API**: Composable queries with Rust-backed execution (powered by `petgraph`)
- **Configuration Generation**: Automatic multi-vendor config generation (Cisco IOS/IOS-XR/NX-OS, Juniper JunOS, Arista EOS)
- **Batteries-Included Blueprints**: Pre-built domain models for ISIS, MPLS, EVPN, L3VPN, IXP
- **Rust Core (NTE)**: Graph operations run at native speed with Python FFI bindings

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

**Current Status:** v1.7 API Usability shipped. Working on v1.8 Performance & Optimization — query performance, profiling infrastructure, and 10k+ node validation.

**Tech Stack:** Python (Pydantic), NTE Rust engine, PyO3 bindings

---

### Network Topology Engine

<span class="status-badge status-active">Stable</span> · [Full Details →](projects/nte)

**What It Is:**
The high-performance Rust engine that powers ank_pydantic's graph operations. Extracted into its own repository as the engine's scope grew beyond a simple backing store.

**Key Features:**
- **petgraph StableDiGraph**: Native-speed topology representation
- **Polars Storage**: Columnar data backend for efficient queries
- **Pluggable Backends**: Polars, DuckDB, and Lite storage options
- **Monte Carlo**: Simulation capabilities via nte-monte-carlo crate
- **Distributed Support**: nte-server crate for distributed computation

**Architecture:** Cargo workspace with specialized crates: nte-core, nte-query, nte-domain, nte-backend, nte-datastore-*, nte-server, nte-monte-carlo.

**Tech Stack:** Rust, petgraph, Polars, DuckDB, PyO3/Maturin bindings

---

### Network Automation Workbench

<span class="status-badge status-active">v1.3 — Tool Integration & Interactive Workflows</span> · [Full Details →](projects/ank-workbench)

**What It Is:**
A platform that integrates the entire network automation ecosystem into a single workflow. Driven from YAML, a text-based TUI, or the web interface — upload topology YAML, visualize the network, run simulations, and analyze results without switching between tools.

**Milestones:** v1.0 Foundation shipped (Feb 4). v1.1 UX Polish shipped (Feb 9). v1.2 Scale Visualization at 98%. v1.3 adds simulator integration, interactive device terminals, and live observability.

**Tech Stack:** Python (FastAPI), React frontend, integrates all ANK ecosystem components

---

### Network Traffic Simulator — Flow-Based Performance Analysis

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/netflowsim)

**What It Is:**
High-performance flow-based network traffic simulator using analytic queuing models and Monte Carlo simulations. Validates topologies and routing strategies against billions of flow iterations in seconds, providing massive-scale network performance analysis.

**Current Status:** Early development

**Tech Stack:** Rust, Petgraph, Rayon

---

### Topology Generator

<span class="status-badge status-active">Phase 21/24 (89%)</span> · [Full Details →](projects/topogen)

**What It Is:**
A Rust library with Python bindings for generating realistic network topologies. Supports data center (fat-tree, leaf-spine), WAN/backbone (ring, mesh, hierarchical, POP), and random graph patterns. Includes traffic matrix generation, ContainerLab output converter, and vendor-specific interface naming.

**Current Status:** v0.10 shipped. Geographic placement and multi-layer generation in progress.

**Tech Stack:** Rust core, PyO3 bindings

---

### AutoNetKit — The Foundation

<span class="status-badge status-active">PhD 2017</span> · [Full Details →](projects/autonetkit)

**What It Is:**
The original compiler-based network automation tool from my PhD research. Introduced declarative network design with the Whiteboard → Plan → Build transformation model, integrated into Cisco VIRL.

**Current Status:** Maintained for reference. Active development moved to ank_pydantic and ANK Workbench.

**Tech Stack:** Python, NetworkX

---

## Integration Examples

These examples demonstrate how ank_pydantic, netsim, and NetVis work together for end-to-end network design workflows.

### Example 1: Service Provider Core (IS-IS/MPLS/iBGP)

Multi-layer service provider topology showing ank_pydantic → netsim integration.

**Topology Overview:**
- 16 devices: 8 core (P), 6 edge (PE), 2 route reflectors (RR)
- AS 65000, 4 Points of Presence (PoPs): West, East, North, South
- Protocol stack: IS-IS underlay, MPLS/LDP transport, iBGP with RR

**Step 1: Model topology with ank_pydantic**

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

**Step 2: Export for netsim validation**

```python
# Export topology for protocol simulation
topology.export_netsim("transitnet-netsim.yaml")
```

**Step 3: Validate with netsim**

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

**Step 4: Visualize with NetVis**

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

NetVis renders the topology with device-aware icons, PoP grouping, and protocol overlay annotations.

**Step 5: Deploy to ContainerLab**

The generated configs deploy directly to ContainerLab for real device testing:

```python
env = get_environment('containerlab')
artifacts = env.generate(topology)
```

```bash
$ sudo containerlab deploy -t transitnet.clab.yml
```

**Key Insight:** ank_pydantic's design functions automatically derive protocol layers from the whiteboard topology, netsim validates convergence in seconds, and NetVis renders the result — all before committing to container deployment.

---

### Example 2: Data Center Fabric (EVPN/VXLAN) — Proposed

**Topology:**
- Spine-leaf architecture: 4 spines, 8 leafs
- eBGP underlay (unique ASN per switch)
- iBGP EVPN overlay (spines as route reflectors)
- VXLAN tunnels for L2 extension across fabric

**ank_pydantic workflow:**
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

**netsim validation:**
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

**ank_pydantic workflow:**
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

**netsim validation:**
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

**ank_pydantic workflow:**
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

**netsim validation:**
- Verify BGP sessions to route servers
- Check transparent AS path handling
- Validate community-based filtering

---

## Getting Started

**For Network Engineers:**
1. Start with **ANK Workbench** — the unified platform for the entire workflow
2. Explore **ank_pydantic** for programmatic topology modeling
3. Use **Network Simulator** for validation and testing

**For Developers:**
1. Check out **ank_pydantic** for the Python API and documentation
2. Explore **netsim** source code for protocol implementation details
3. Contribute to **NetVis** for visualization algorithms

---

## Source Code

- **ank_pydantic**: [github.com/sk2/ank_pydantic](https://github.com/sk2/ank_pydantic)
- **NTE**: [github.com/sk2/ank_nte](https://github.com/sk2/ank_nte)
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
