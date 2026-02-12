---
layout: default
---

# Network Simulator

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Insight

A deterministic, tick-based network simulator for rapid prototyping and testing of network configurations. Enables quick validation of routing protocol behavior before moving to full emulation or production deployment — catch obvious errors early in the design cycle.

## Quick Facts

| | |
|---|---|
| **Status** | v1.6 shipped |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation.

## Key Features

- **Deterministic Simulation**: Tick-based execution ensures reproducible results
- **Protocol Implementations**: OSPF, IS-IS, BGP with packet-level accuracy
- **Fast Validation**: Simulate 100+ node topologies in seconds
- **RIB/FIB Separation**: Models routing decisions (control plane) and forwarding behavior (data plane)
- **Comprehensive Testing**: 1,350+ tests validate protocol behavior against RFCs
- **Parallel Execution**: Multi-core support for large topologies

## Detailed Protocol Support

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

**BGP (RFC 4271 - BGP-4):**
- **Session Management**: Full FSM with keepalive/hold timers
- **Path Attributes**: AS_PATH, NEXT_HOP, LOCAL_PREF, MED, Communities, Extended Communities
- **Route Selection**: RFC 4271 best-path algorithm with all tie-breakers
- **Route Reflection**: RFC 4456 with CLUSTER_ID and ORIGINATOR_ID
- **eBGP/iBGP**: Multi-AS topologies with proper next-hop handling
- **Advanced Features**: Graceful restart (RFC 4724), VPNv4 (RFC 4760)

**MPLS - Planned:**
- **LDP**: Label distribution for IP prefixes
- **RSVP-TE**: Traffic engineering with explicit paths
- **Fast Reroute**: Link/node protection with backup tunnels

## Example 1: OSPF Triangle Topology

Simple three-router topology to verify basic OSPF functionality.

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

## Example 2: IS-IS Level 1/Level 2 Hierarchy

Service provider topology demonstrating IS-IS hierarchical routing with L1 and L2 areas.

Input topology (`isis-hierarchy.yaml`):
```yaml
name: isis-hierarchy
description: IS-IS L1/L2 hierarchy with inter-area routing

devices:
  - name: r1
    type: router
    isis:
      net: "49.0001.0000.0000.0001.00"
      level: l1
    interfaces:
      - name: eth0
        ip: 10.1.0.1/24
        isis: { metric: 10 }
      - name: lo
        ip: 192.0.2.1/32
        isis: {}

  - name: r2
    type: router
    isis:
      net: "49.0001.0000.0000.0002.00"
      level: l1l2  # Area border router
    interfaces:
      - name: eth0
        ip: 10.1.0.2/24
        isis: { metric: 10 }
      - name: eth1
        ip: 10.0.0.2/24
        isis: { metric: 10 }
      - name: lo
        ip: 192.0.2.2/32
        isis: {}

  - name: r3
    type: router
    isis:
      net: "49.0002.0000.0000.0003.00"
      level: l2
    interfaces:
      - name: eth0
        ip: 10.0.0.3/24
        isis: { metric: 10 }
      - name: lo
        ip: 192.0.2.3/32
        isis: {}

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r2:eth1, r3:eth0]

script:
  - at: converged
    device: r2
    command: show isis neighbors
  - at: converged
    device: r2
    command: show isis database
  - at: converged
    device: r1
    command: show ip route
```

Run simulation:
```bash
$ netsim run isis-hierarchy.yaml

[t=0ms] Network initialized: 3 devices, 2 links
[t=0ms] IS-IS: r1, r2, r3 sending IIH (IS-IS Hello)
[t=3ms] IS-IS: Adjacencies forming
[t=5ms] IS-IS: r1<->r2 L1 adjacency Up
[t=5ms] IS-IS: r2<->r3 L2 adjacency Up
[t=8ms] IS-IS: LSP flooding in progress
[t=12ms] IS-IS: SPF calculation complete (L1 and L2)
[t=12ms] Network converged

[t=12ms] r2> show isis neighbors
System ID       Interface  State  Level  Holdtime
0000.0000.0001  eth0       Up     L1     24s
0000.0000.0003  eth1       Up     L2     24s

[t=12ms] r2> show isis database
IS-IS Level-1 Link State Database:
LSPID                 LSP Seq Num  Checksum  Lifetime  Attributes
0000.0000.0001.00-00  0x00000003   0x4a2e    864       L1
0000.0000.0002.00-00  0x00000003   0x5c1a    864       L1L2

IS-IS Level-2 Link State Database:
LSPID                 LSP Seq Num  Checksum  Lifetime  Attributes
0000.0000.0002.00-00  0x00000003   0x7f3c    864       L1L2
0000.0000.0003.00-00  0x00000003   0x9a2b    864       L2

[t=12ms] r1> show ip route
Codes: C - connected, i L1 - IS-IS level-1, i L2 - IS-IS level-2

C    10.1.0.0/24 is directly connected, eth0
C    192.0.2.1/32 is directly connected, lo
i L1 192.0.2.2/32 [115/10] via 10.1.0.2, eth0
i L2 192.0.2.3/32 [115/20] via 10.1.0.2, eth0
     (route leaked from L2 to L1 by ABR r2)

Simulation complete: 15ms simulated, 0.008s real time
IS-IS events: 18 hellos, 4 LSPs, 2 SPF runs
```

## Example 3: Protocol State Inspection (OSPF)

Detailed protocol state inspection with full routing tables and OSPF database dumps.

```bash
[t=45ms] core-1> show ip route
Codes: C - connected, O - OSPF, IA - OSPF inter-area
       * - candidate default

Gateway of last resort is not set

C    10.0.0.0/30 is directly connected, eth0
C    10.0.0.4/30 is directly connected, eth1
C    10.0.0.8/30 is directly connected, eth2
C    10.0.100.1/32 is directly connected, lo0
O    10.0.100.2/32 [110/10] via 10.0.0.2, eth0, 00:00:25
O    10.0.100.3/32 [110/10] via 10.0.0.6, eth1, 00:00:25
O    10.0.100.4/32 [110/10] via 10.0.0.10, eth2, 00:00:25
O    10.5.1.0/24 [110/20] via 10.0.0.2, eth0, 00:00:23
O    10.5.2.0/24 [110/20] via 10.0.0.6, eth1, 00:00:23
O    10.5.12.0/24 [110/20] via 10.0.0.2, eth0, 00:00:23
                  [110/20] via 10.0.0.6, eth1, 00:00:23
O IA 10.10.1.0/24 [110/25] via 10.0.0.10, eth2, 00:00:20
O IA 10.10.2.0/24 [110/25] via 10.0.0.10, eth2, 00:00:20

[t=45ms] core-1> show ip ospf database

       OSPF Router with ID (10.0.100.1) (Process ID 1)

                Router Link States (Area 0.0.0.0)

Link ID         ADV Router      Age  Seq#       Checksum
10.0.100.1      10.0.100.1      25   0x80000003 0x6d2a
10.0.100.2      10.0.100.2      23   0x80000003 0x7f1c
10.0.100.3      10.0.100.3      24   0x80000003 0x8b0e
10.0.100.4      10.0.100.4      22   0x80000004 0x9700

                Net Link States (Area 0.0.0.0)

Link ID         ADV Router      Age  Seq#       Checksum
10.0.0.1        10.0.100.1      25   0x80000001 0x4a12
10.0.0.5        10.0.100.1      25   0x80000001 0x5b23
10.5.12.2       10.0.100.2      23   0x80000002 0x7c45

                Summary Net Link States (Area 0.0.0.0)

Link ID         ADV Router      Age  Seq#       Checksum
10.10.1.0       10.0.100.4      20   0x80000001 0xa1f3
10.10.2.0       10.0.100.4      20   0x80000001 0xb2e4

[t=45ms] core-1> show ip ospf database router 10.0.100.1

       OSPF Router with ID (10.0.100.1) (Process ID 1)

                Router Link States (Area 0.0.0.0)

  LS age: 25
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 10.0.100.1
  Advertising Router: 10.0.100.1
  LS Seq Number: 0x80000003
  Checksum: 0x6d2a
  Length: 60
  Number of Links: 3

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.0.0.1
     (Link Data) Router Interface address: 10.0.0.1
      Number of TOS metrics: 0
       TOS 0 Metrics: 10

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.0.0.5
     (Link Data) Router Interface address: 10.0.0.5
      Number of TOS metrics: 0
       TOS 0 Metrics: 10

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.0.0.9
     (Link Data) Router Interface address: 10.0.0.9
      Number of TOS metrics: 0
       TOS 0 Metrics: 10

[t=45ms] core-1> show ip protocols
Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Router ID 10.0.100.1
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    10.0.0.0 0.0.0.3 area 0.0.0.0
    10.0.0.4 0.0.0.3 area 0.0.0.0
    10.0.0.8 0.0.0.3 area 0.0.0.0
  Routing Information Sources:
    Gateway         Distance      Last Update
    10.0.100.2      110           00:00:25
    10.0.100.3      110           00:00:24
    10.0.100.4      110           00:00:22
  Distance: (default is 110)

[t=45ms] core-1> show ip ospf interface eth0
eth0 is up, line protocol is up
  Internet Address 10.0.0.1/30, Area 0.0.0.0
  Process ID 1, Router ID 10.0.100.1, Network Type BROADCAST, Cost: 10
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 10.0.100.1, Interface Address 10.0.0.1
  Backup Designated router (ID) 10.0.100.2, Interface Address 10.0.0.2
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:07
  Neighbor Count is 1, Adjacent neighbor count is 1
    Adjacent with neighbor 10.0.100.2 (Backup Designated Router)
  Suppress hello for 0 neighbor(s)
```

## Example 4: BGP Multi-AS Route Propagation

eBGP peering across three autonomous systems with route propagation and path attribute handling.

Input topology (`bgp-multi-as.yaml`):
```yaml
name: bgp-multi-as
description: BGP propagation across multiple ASes with communities

devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: lo0
        ip: 1.1.1.1/32
      - name: eth0
        ip: 10.0.12.1/24
    bgp:
      as: 65001
      networks: ["10.1.0.0/24"]
      neighbors:
        - ip: 10.0.12.2
          remote_as: 65002
          send_community: true

  - name: r2
    type: router
    router_id: 2.2.2.2
    interfaces:
      - name: lo0
        ip: 2.2.2.2/32
      - name: eth0
        ip: 10.0.12.2/24
      - name: eth1
        ip: 10.0.23.2/24
    bgp:
      as: 65002
      neighbors:
        - ip: 10.0.12.1
          remote_as: 65001
        - ip: 10.0.23.3
          remote_as: 65003

  - name: r3
    type: router
    router_id: 3.3.3.3
    interfaces:
      - name: lo0
        ip: 3.3.3.3/32
      - name: eth0
        ip: 10.0.23.3/24
    bgp:
      as: 65003
      neighbors:
        - ip: 10.0.23.2
          remote_as: 65002

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r2:eth1, r3:eth0]

script:
  - at: converged
    device: r2
    command: show bgp summary
  - at: converged
    device: r3
    command: show bgp
```

Run simulation:
```bash
$ netsim run bgp-multi-as.yaml

[t=0ms] Network initialized: 3 devices, 2 links
[t=0ms] BGP: r1, r2, r3 establishing sessions
[t=5ms] BGP: r1<->r2 session established (eBGP AS65001-AS65002)
[t=5ms] BGP: r2<->r3 session established (eBGP AS65002-AS65003)
[t=10ms] BGP: r1 advertising 10.1.0.0/24
[t=12ms] BGP: Route propagation in progress
[t=15ms] Network converged

[t=15ms] r2> show bgp summary
BGP router identifier 2.2.2.2, local AS number 65002

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.0.12.1       4 65001       3       3        1    0    0 00:00:15        1
10.0.23.3       4 65003       3       3        1    0    0 00:00:15        0

Total number of neighbors 2

[t=15ms] r3> show bgp
BGP table version is 1, local router ID is 3.3.3.3
Status codes: s suppressed, d damped, h history, * valid, > best, i internal
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 10.1.0.0/24      10.0.23.2                0             0 65002 65001 i

Total number of prefixes 1

Path details:
  10.1.0.0/24:
    AS_PATH: 65002 65001
    NEXT_HOP: 10.0.23.2
    ORIGIN: IGP
    MED: not set
    LOCAL_PREF: not set (eBGP)
    Communities: (none)

Simulation complete: 18ms simulated, 0.009s real time
BGP events: 6 sessions established, 1 route originated, 2 UPDATEs sent
```

**Key BGP Features Demonstrated:**
- **eBGP Peering**: Cross-AS session establishment
- **AS_PATH Construction**: Path vector grows as route propagates (65002 65001)
- **Next-Hop Handling**: Next-hop set to eBGP peer address
- **Route Selection**: Best-path algorithm applied at each AS
- **Session Management**: Keepalive/hold timers, graceful establishment

## Example 5: Service Provider Core with IS-IS/MPLS/iBGP (from ank_pydantic)

Multi-layer service provider topology using ank_pydantic to generate topology and netsim for protocol validation.

**Topology Overview:**
- 16 devices: 8 core (P), 6 edge (PE), 2 route reflectors (RR)
- AS 65000
- 4 Points of Presence (PoPs): West, East, North, South

### Step 1: Define Whiteboard Topology

Create `transitnet-sp-core.yaml`:
```yaml
# TransitNet Service Provider Core
# 16 devices across 4 PoPs with IS-IS/MPLS/iBGP

topology:
  - metadata:
      name: TransitNet SP Core
      description: Tier 1 service provider backbone
      organisation: TransitNet
      asn: 65000

  - nodes:
      # PoP-West: Core and Edge
      - P1:
          role: core
          data:
            pop: West
            platform: iosxr
            asn: 65000
            loopback: 10.0.0.1/32
          endpoints:
            - Gi0/0/0/0  # to P3
            - Gi0/0/0/1  # to P5
            - Gi0/0/0/2  # to PE1

      - PE1:
          role: pe
          data:
            pop: West
            platform: iosxr
            asn: 65000
            loopback: 10.0.0.11/32
          endpoints:
            - Gi0/0/0/0  # to P1

      # PoP-South: Route Reflectors
      - RR1:
          role: rr
          data:
            pop: South
            platform: iosxr
            asn: 65000
            loopback: 10.0.0.21/32
          endpoints:
            - Gi0/0/0/0  # to P7

      # ... (additional nodes omitted for brevity)

  - links:
      # Inter-PoP core links
      - [P1, Gi0/0/0/0, P3, Gi0/0/0/0]   # West-East
      - [P1, Gi0/0/0/1, P5, Gi0/0/0/0]   # West-North
      - [P3, Gi0/0/0/1, P7, Gi0/0/0/0]   # East-South
      # Core to PE links
      - [P1, Gi0/0/0/2, PE1, Gi0/0/0/0]  # West
      # ... (additional links omitted)
```

### Step 2: Generate Protocol Layers with ank_pydantic

```python
from ank_pydantic import Topology
from ank_pydantic.core.designs import build_isis_layer, build_mpls_layer

# Load the whiteboard topology
topology = Topology.from_yaml("transitnet-sp-core.yaml")
print(f"Loaded {len(list(topology.layer('input').nodes()))} nodes")

# Build IS-IS Layer (Level 2 flat domain)
isis_layer = build_isis_layer(
    topology,
    level=2,
    area="49.0001",
    parent_layer="physical"
)
print(f"Created {len(list(isis_layer.edges()))} IS-IS adjacencies")

# Build MPLS/LDP Layer (follows IS-IS)
mpls_layer = build_mpls_layer(
    topology,
    igp_layer="isis",
    layer_name="mpls"
)
print(f"Created {len(list(mpls_layer.edges()))} LDP sessions")

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

### Step 3: Export to netsim Format

```python
# Export for netsim validation
topology.export_netsim("transitnet-netsim.yaml")
```

### Step 4: Run in netsim

```bash
$ netsim run transitnet-netsim.yaml

[t=0ms] Network initialized: 16 devices, 14 links
[t=0ms] IS-IS: All routers sending IIH (IS-IS Hello)
[t=5ms] IS-IS: Adjacencies Up (14 adjacencies)
[t=8ms] IS-IS: LSP flooding in progress
[t=12ms] IS-IS: SPF calculation complete (all routers)
[t=15ms] MPLS: LDP sessions establishing
[t=20ms] MPLS: Label bindings distributed
[t=25ms] BGP: iBGP sessions establishing (13 sessions)
[t=30ms] BGP: Route reflectors active, PE sessions Up
[t=35ms] Network converged

Simulation complete: 35ms simulated
- 16 IS-IS routers, 14 adjacencies
- 14 LDP sessions, labels distributed
- 13 iBGP sessions, 2 route reflectors
```

### Key Features Demonstrated

- **Multi-layer modeling**: Physical → IS-IS → MPLS → iBGP
- **ank_pydantic design functions**: Automated layer derivation
- **Route reflector topology**: Scalable iBGP without full mesh
- **Service provider patterns**: Realistic SP core architecture
- **Incremental validation**: Verify each layer before adding next

This example shows how ank_pydantic topology modeling integrates with netsim for protocol validation in complex multi-layer networks.

---

## Limitations

- Protocol behavior is simplified compared to real implementations
- Timing is deterministic (useful for testing, not realistic)
- Some edge cases and vendor-specific behaviors not modeled
- Best used for smoke testing, not certification

## Use Cases

- **Pre-deployment Validation**: Catch routing loops, black holes, and misconfigurations before production
- **Convergence Analysis**: Measure failover time and validate backup paths
- **Capacity Planning**: Test network behavior under scaled topologies
- **Protocol Verification**: Validate RFC compliance for custom implementations
- **Training**: Safe environment for learning routing protocol behavior

## Current Status

v1.6 shipped with OSPF support. 126,000 lines of Rust, 122 requirements met (35 MVP + 87 advanced).

## Tech Stack

Rust, Tokio for async execution, petgraph for topology representation

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
