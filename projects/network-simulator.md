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
| **Started** | 2025 |

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

**BGP (RFC 4271 - BGP-4) - In Development:**
- **Session Management**: TCP-based peering with keepalive/hold timers
- **Path Attributes**: AS_PATH, NEXT_HOP, LOCAL_PREF, MED
- **Route Selection**: Full BGP decision process implementation
- **Policy**: Community-based filtering and attribute manipulation

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

## Example 2: Enterprise Campus (25 routers)

Larger topology to test convergence behavior and routing table consistency.

```bash
$ netsim run enterprise-campus.yaml

[t=0ms] Loading topology: 25 devices, 48 links
[t=0ms] Initializing OSPF on 25 routers
[t=10ms] OSPF: Hello packets sent
[t=15ms] OSPF: 24 adjacencies formed
[t=20ms] OSPF: LSA flooding in progress (157 LSAs)
[t=35ms] OSPF: SPF calculation triggered on all routers
[t=45ms] OSPF: Network converged

[t=45ms] core-1> show ip route summary
Routes: 178 total
  directly connected: 6
  OSPF intra-area: 164
  OSPF inter-area: 8

[t=45ms] core-1> show ip ospf neighbor
Neighbor ID     State    Priority  Dead Time  Interface
10.0.0.2        Full     1         38s        eth0
10.0.0.3        Full     1         37s        eth1
10.0.0.4        Full     1         39s        eth2

[t=50ms] Link failure simulation: core-1:eth0 down
[t=52ms] OSPF: LSA update triggered on core-1
[t=55ms] OSPF: Recalculating SPF on 12 affected routers
[t=60ms] OSPF: Reconverged (10ms convergence time)

[t=60ms] core-1> show ip route 10.5.12.0
10.5.12.0/24  via 10.0.0.3 [OSPF/110] metric=30
  (rerouted via backup path)

Simulation complete: 180ms simulated, 0.156s real time
OSPF events: 243 hellos, 157 LSAs, 25 SPF runs
Convergence: initial=45ms, failover=10ms
```

## Example 3: Advanced OSPF Inspection

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
