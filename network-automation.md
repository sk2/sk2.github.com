---
layout: default
---

# Network Automation Ecosystem

Tools for network topology modeling, simulation, and visualization.

## Contents
- [Overview](#overview)
- [How They Work Together](#how-they-work-together)
- [The Tools](#the-tools)
  - [ANK Workbench — Unified Platform](#ank-workbench--unified-platform)
  - [ank_pydantic — Topology Modeling Library](#ank_pydantic--topology-modeling-library)
  - [Network Simulator (netsim) — Protocol Validation](#network-simulator-netsim--protocol-validation)
  - [NetFlow Sim — Flow-Based Performance Analysis](#netflow-sim--flow-based-performance-analysis)
  - [NetVis — Visualization Engine](#netvis--visualization-engine)
  - [TopoGen — Topology Generator](#topogen--topology-generator)
  - [AutoNetkit — The Foundation](#autonetkit--the-foundation)
- [Getting Started](#getting-started)
- [Source Code](#source-code)

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
A Python library for modeling and querying network topologies with type-safe Pydantic models and a high-performance Rust core. Expressive Python API backed by blazing-fast graph algorithms, with automatic configuration generation for multi-vendor network deployments.

**Key Features:**
- **Two-Stage Transformation Model**: Whiteboard (sketch) → Plan (logical) → Protocol Layers (physical)
- **Type-Safe Models**: Pydantic validation ensures correct topology structure at design time
- **Lazy Query API**: Composable queries with Rust-backed execution (powered by `petgraph`)
- **Configuration Generation**: Automatic multi-vendor config generation (Cisco IOS/IOS-XR/NX-OS, Juniper JunOS, Arista EOS)
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

**Rapid Prototyping for Agentic AI & Network Automation:**
The simulator's core value is accelerating the development iteration loop for agentic AI systems and network automation tools. Instead of spinning up containers for every test cycle (minutes), validate configurations in simulation (seconds):

1. **Design topology** with ank_pydantic
2. **Generate configs** automatically for target platforms
3. **Simulate in seconds** to validate routing behavior
4. **Iterate rapidly** on agent logic, automation scripts, or config templates
5. **Deploy to containers** only after simulation validates the approach

This workflow dramatically shortens the iteration cycle for developing network automation agents, DevOps pipelines, and AI-driven network operations — validate ideas in simulation before committing to heavyweight container deployments. Originally built to enable this exact use case: fast prototyping for automated network systems.

**Daemon Mode — Real-Time Interaction:**
Run simulations as background daemons and interact with them in real-time, like `docker exec` for network simulations:
- **Start a daemon**: `netsim daemon start my-network topology.yaml`
- **Execute commands**: `netsim exec my-network r1 "show ip route"`
- **Attach interactively**: `netsim attach my-network r1` for full REPL console with command history
- **Agent development**: Test automation agents against live network state without container overhead
- **CI/CD integration**: Start daemon, run tests via `exec`, collect results, stop daemon

This enables real-time exploration of network state as the simulation evolves — perfect for developing agentic systems and automated testing.

**Current Status:** v1.6 shipped with OSPF support, daemon mode with interactive console

**Tech Stack:** Rust, Tokio, petgraph

---

### Traffic Simulator — Flow-Based Performance Analysis

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

**Key Capabilities:**
- **Automated Layout**: Reduce visual noise in 100+ node topologies
- **Multi-Layer Support**: Visualize logical overlays on physical infrastructure
- **High-Fidelity Output**: Publication-ready SVG and PDF exports

**Current Status:** Core layout algorithms implemented, building interactive web renderer.

**Tech Stack:** Rust, petgraph, svg-renderer

---

### TopoGen — Topology Generator

<span class="status-badge status-active">Phase 17/24 (11%)</span> · [Full Details →](projects/topogen)

**What It Is:**
A Rust library with Python bindings for generating realistic network topologies. Supports data center (spine-leaf, fat-tree), WAN (hub-spoke, mesh), and random graph patterns.

**Current Status:** Early development

**Tech Stack:** Rust core, PyO3 bindings

---

### AutoNetkit — The Foundation

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

**Step 4: Deploy to ContainerLab and verify**

Generated IOS-XR configuration for P1:
```cisco
hostname P1
!
interface Loopback0
 ipv4 address 10.0.0.1 255.255.255.255
!
router isis CORE
 is-type level-2-only
 net 49.0001.0100.0000.0001.00
 address-family ipv4 unicast
  metric-style wide
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
 !
 interface GigabitEthernet0/0/0/0
  point-to-point
  address-family ipv4 unicast
 !
!
mpls ldp
 router-id 10.0.0.1
 interface GigabitEthernet0/0/0/0
 !
!
```

Verify IS-IS neighbors on P1:
```bash
$ docker exec -it clab-transitnet-P1 xr show isis neighbors

IS-IS CORE neighbors:
System Id       Interface       SNPA           State  Holdtime Type IETF-NSF
P3              Gi0/0/0/0       *PtoP*         Up     28       L2   Capable
P5              Gi0/0/0/1       *PtoP*         Up     26       L2   Capable
PE1             Gi0/0/0/2       *PtoP*         Up     29       L2   Capable
```

Verify MPLS/LDP sessions on P1:
```bash
$ docker exec -it clab-transitnet-P1 xr show mpls ldp neighbor

Peer LDP Identifier: 10.0.0.3:0
  TCP connection: 10.0.0.3:646 - 10.0.0.1:37854
  Graceful Restart: No
  Session Holdtime: 180 sec
  State: Oper; Msgs sent/rcvd: 15/14; Downstream-Unsolicited
  Up time: 00:05:23
  LDP Discovery Sources:
    IPv4: (1)
      Gi0/0/0/0
    IPv6: (0)

Peer LDP Identifier: 10.0.0.5:0
  TCP connection: 10.0.0.5:646 - 10.0.0.1:41203
  Graceful Restart: No
  Session Holdtime: 180 sec
  State: Oper; Msgs sent/rcvd: 16/15; Downstream-Unsolicited
  Up time: 00:05:21
```

Verify BGP sessions on PE1 (to route reflectors):
```bash
$ docker exec -it clab-transitnet-PE1 xr show bgp summary

BGP router identifier 10.0.0.11, local AS number 65000
BGP generic scan interval 60 secs
BGP table state: Active
Table ID: 0xe0000000   RD version: 5
BGP main routing table version 5
BGP scan interval 60 secs

BGP is operating in STANDALONE mode.

Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker               5          5          5          5           5           0

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10.0.0.21         0 65000      12      11        5    0    0 00:05:18          0
10.0.0.22         0 65000      12      11        5    0    0 00:05:17          0
```

Check routing table on PE1:
```bash
$ docker exec -it clab-transitnet-PE1 xr show route

Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP

Gateway of last resort is not set

L    10.0.0.11/32 is directly connected, 00:05:45, Loopback0
i L2 10.0.0.1/32 [115/10] via 10.1.11.1, 00:05:28, GigabitEthernet0/0/0/0
i L2 10.0.0.3/32 [115/20] via 10.1.11.1, 00:05:28, GigabitEthernet0/0/0/0
i L2 10.0.0.5/32 [115/20] via 10.1.11.1, 00:05:28, GigabitEthernet0/0/0/0
i L2 10.0.0.16/32 [115/30] via 10.1.11.1, 00:05:28, GigabitEthernet0/0/0/0
i L2 10.0.0.21/32 [115/20] via 10.1.11.1, 00:05:28, GigabitEthernet0/0/0/0
i L2 10.0.0.22/32 [115/20] via 10.1.11.1, 00:05:28, GigabitEthernet0/0/0/0
```

Verify MPLS forwarding table:
```bash
$ docker exec -it clab-transitnet-PE1 xr show mpls forwarding

Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes
Label  Label       or ID              Interface                    Switched
------ ----------- ------------------ ------------ --------------- ------------
24000  Pop         10.0.0.1/32        Gi0/0/0/0    10.1.11.1       0
24001  24001       10.0.0.3/32        Gi0/0/0/0    10.1.11.1       0
24002  24002       10.0.0.5/32        Gi0/0/0/0    10.1.11.1       0
24003  24003       10.0.0.16/32       Gi0/0/0/0    10.1.11.1       0
24004  24004       10.0.0.21/32       Gi0/0/0/0    10.1.11.1       0
24005  24005       10.0.0.22/32       Gi0/0/0/0    10.1.11.1       0
```

End-to-end connectivity test (PE1 to PE6):
```bash
$ docker exec -it clab-transitnet-PE1 ping 10.0.0.16 -c 3
PING 10.0.0.16 (10.0.0.16) 56(84) bytes of data.
64 bytes from 10.0.0.16: icmp_seq=1 ttl=62 time=2.1 ms
64 bytes from 10.0.0.16: icmp_seq=2 ttl=62 time=1.8 ms
64 bytes from 10.0.0.16: icmp_seq=3 ttl=62 time=1.9 ms

$ docker exec -it clab-transitnet-PE1 traceroute 10.0.0.16
1  P1 (10.0.0.1) [MPLS: Label 24001]
2  P5 (10.0.0.5) [MPLS: Label 24002]
3  P6 (10.0.0.6) [MPLS: Label 24003]
4  PE6 (10.0.0.16)
```

**Key Insight:** ank_pydantic's design functions automatically derive protocol layers from the whiteboard topology, then netsim validates the resulting configuration converges correctly. The generated configs can be deployed directly to ContainerLab for real device testing.

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
- Test multi-vendor interoperability

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
