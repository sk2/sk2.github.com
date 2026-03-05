---
layout: default
section: network-automation
---

# Network Simulator

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Index](#index)
- [Running Examples](#running-examples)
- [Usage](#usage)
- [Architecture](#architecture)
- [Roadmap](#roadmap)
- [The Insight](#the-insight)
- [Overview](#overview)
- [Problem It Solves](#problem-it-solves)
- [Protocols Implemented](#protocols-implemented)
- [Automation](#automation)
- [Examples](#examples)
- [Development Status](#development-status)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Current Milestone: v2.1 Enterprise & Campus Protocols](#current-milestone-v21-enterprise-campus-protocols)
- [Future Milestones (Proposed)](#future-milestones-proposed)
- [Ecosystem Context](#ecosystem-context)
- [Current Status](#current-status)
- [Roadmap](#roadmap)

## Concept

Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.

Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.

---

## Technical Reports

- [Download Technical Report: paper.pdf](/assets/docs/netsim-paper.pdf)
- [Download Technical Report: techreport.pdf](/assets/docs/netsim-techreport.pdf)

---

## Code Samples

### README.md

```markdown
# Network Simulator Examples

A collection of topology scenarios for the Network Simulator, ranging from basic connectivity to advanced protocol designs.

## Index

### Core & Basics
- **[simple.yaml](simple.yaml)**: Minimal two-host direct connection.
- **[mixed-network.yaml](mixed-network.yaml)**: Demonstrates Routers, Switches, and Hubs in a single topology.
- **[ospf-triangle.yaml](ospf-triangle.yaml)**: Basic OSPF triangle with three routers and hosts.

### Routing Protocols (Advanced)
- **[isis-hierarchical.yaml](isis-hierarchical.yaml)**: **(New)** Multi-area IS-IS with Level 1, Level 2, and L1L2 routers.
- **[bgp-rr-loop.yaml](docs-bgp-rr-loop.yaml)**: iBGP Route Reflection with ORIGINATOR_ID and CLUSTER_LIST loop prevention.
- **[bgp-community-policy.yaml](bgp-community-policy.yaml)**: **(New)** BGP standard communities (NO_EXPORT, NO_ADVERTISE) and propagation.
- **[ospf-basic.yaml](docs-ospf-basic.yaml)**: Standard OSPF two-router setup with ping/traceroute validation.

### High Availability & Tunnels
- **[bfd-fast-failover.yaml](bfd-fast-failover.yaml)**: **(New)** Demonstrates BFD-triggered sub-second failover for OSPF and BGP.
- **[gre-overlay.yaml](gre-overlay.yaml)**: **(New)** GRE tunnel over an OSPF underlay, including recursion checks and keepalives.

### MPLS & LDP
- **[mpls-ldp-oam.yaml](docs-mpls-ldp-oam.yaml)**: LDP signaling, MPLS forwarding, and OAM (LSP Ping/Traceroute).

### L3VPN & Segment Routing
- **[l3vpn-service-provider.yaml](l3vpn-service-provider.yaml)**: **(New)** L3VPN with VRF isolation, VPNv4 routing, and MPLS transport. [Sample Output](l3vpn-service-provider.md)
- **[sr-mpls-transport.yaml](sr-mpls-transport.yaml)**: **(New)** Segment Routing MPLS with SRGB, Node-SID, and label-switched paths. [Sample Output](sr-mpls-transport.md)

### Scale & Benchmarking
- **[data-center.yaml](data-center.yaml)**: Large-scale leaf-spine data center topology.
- **[service-provider.yaml](service-provider.yaml)**: Hierarchical OSPF design with 148+ devices.
- **[large-enterprise.yaml](large-enterprise.yaml)**: Complex three-tier enterprise model with 400+ devices.
- **[wan-mesh.yaml](wan-mesh.yaml)**: Full-mesh WAN connectivity.

### Traffic & Names
- **[names-traffic-small.yaml](names-traffic-small.yaml)**: Demonstrates the `names:` registry and basic traffic generation.
- **[names-traffic-medium.yaml](names-traffic-medium.yaml)**: More complex traffic generation patterns.

## Running Examples

To run an example and see the results:
```bash
netsim run examples/isis-hierarchical.yaml
```

To validate a file's syntax and build logic without running the simulation:
```bash
netsim validate examples/isis-hierarchical.yaml
```

```

### bfd-fast-failover.yaml

```yaml
name: bfd-fast-failover
description: |
  BFD fast failover example demonstrating OSPF and BGP reaction to link failures.
  
  Topology:
  - Triangle of routers (r1, r2, r3)
  - r1 and r2 have a primary link with BFD enabled.
  - OSPF and BGP run over the links.
  
  Scenario:
  - Simulation converges.
  - Event at tick 1000: r1-r2 interface goes down.
  - Observation: BFD detects failure, OSPF/BGP tear down sessions immediately without waiting for protocol dead timers.

devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: to-r2
        ip: 10.0.12.1/24
        ospf: { area: 0, bfd: true }
      - name: to-r3
        ip: 10.0.13.1/24
        ospf: { area: 0 }
    bgp:
      as: 65001
      neighbors:
        - ip: 10.0.12.2
          remote_as: 65002
          bfd: true
    bfd:
      default_min_tx: 100
      default_min_rx: 100
      default_multiplier: 3

  - name: r2
    type: router
    router_id: 2.2.2.2
    interfaces:
      - name: to-r1
        ip: 10.0.12.2/24
        ospf: { area: 0, bfd: true }
      - name: to-r3
        ip: 10.0.23.2/24
        ospf: { area: 0 }
    bgp:
      as: 65002
      neighbors:
        - ip: 10.0.12.1
          remote_as: 65001
          bfd: true
    bfd:
      default_min_tx: 100
      default_min_rx: 100
      default_multiplier: 3

  - name: r3
    type: router
    router_id: 3.3.3.3
    interfaces:
      - name: to-r1
        ip: 10.0.13.3/24
        ospf: { area: 0 }
      - name: to-r2
        ip: 10.0.23.3/24
        ospf: { area: 0 }

links:
  - endpoints: [r1:to-r2, r2:to-r1]
  - endpoints: [r1:to-r3, r3:to-r1]
  - endpoints: [r2:to-r3, r3:to-r2]

events:
  - at: 1000
    interface_down: { device: r1, interface: to-r2 }
    label: primary-link-failure

script:
  - at: 500
    device: r1
    command: show bfd
  - at: 500
    device: r1
    command: show bgp summary
  - at: 1010  # Immediately after failure
    device: r1
    command: show bfd
  - at: 1010
    device: r1
    command: show bgp summary
  - at: 1010
    device: r1
    command: show ospf neighbors
  - at: 1500  # After reconvergence
    device: r1
    command: show ip route

```

### bgp-community-policy.yaml

```yaml
name: bgp-community-policy
description: |
  BGP propagation example across multiple ASes.
  
  Topology:
  - AS 65001 (r1): Originator.
  - AS 65002 (r2): Intermediate Transit.
  - AS 65003 (r3): External Peer.
  
  Scenario:
  - r1 originates a network.
  - Observation: r2 and r3 receive the route.

  Simulator note:
  - Well-known community semantics (NO_EXPORT / NO_ADVERTISE) are implemented in the core,
    but YAML does not currently provide a route-origination attachment surface to set
    communities on originated prefixes.

devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: lo0
        ip: 1.1.1.1/32
        ospf: { area: 0 }
      - name: eth0
        ip: 10.0.12.1/24
        ospf: { area: 0 }
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
        ospf: { area: 0 }
      - name: eth0
        ip: 10.0.12.2/24
        ospf: { area: 0 }
      - name: eth1
        ip: 10.0.23.2/24
        ospf: { area: 0 }
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
        ospf: { area: 0 }
      - name: eth0
        ip: 10.0.23.3/24
        ospf: { area: 0 }
    bgp:
      as: 65003
      neighbors:
        - ip: 10.0.23.2
          remote_as: 65002

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r2:eth1, r3:eth0]

script:
  - at: 2000
    device: r2
    command: show bgp summary
  - at: converged
    device: r2
    command: show bgp
  - at: converged + 500
    device: r2
    command: show bgp
  - at: converged
    device: r3
    command: show bgp

```

### bgp-ipv6-multi-as.yaml

```yaml
name: "BGP IPv6 Multi-AS Topology"
description: "Reference topology with eBGP, iBGP, route reflection for IPv6"
routers:
  - name: R1
    asn: 65001
    interfaces:
      - name: eth0
        ipv4: "10.0.1.1/24"
        ipv6: "2001:db8:1::1/64"
      - name: eth1
        ipv4: "10.0.12.1/24"
        ipv6: "2001:db8:12::1/64"
    bgp:
      router_id: "1.1.1.1"
      address_families:
        - ipv6_unicast
      neighbors:
        - peer_ip: "2001:db8:12::2"
          peer_asn: 65002
          address_families:
            - ipv6_unicast
      redistribute:
        - connected
        - static
        - ospfv3

  - name: R2
    asn: 65002
    interfaces:
      - name: eth0
        ipv4: "10.0.2.1/24"
        ipv6: "2001:db8:2::1/64"
      - name: eth1
        ipv4: "10.0.12.2/24"
        ipv6: "2001:db8:12::2/64"
      - name: eth2
        ipv4: "10.0.23.2/24"
        ipv6: "2001:db8:23::2/64"
    bgp:
      router_id: "2.2.2.2"
      address_families:
        - ipv6_unicast
      neighbors:
        - peer_ip: "2001:db8:12::1"
          peer_asn: 65001
          address_families:
            - ipv6_unicast
        - peer_ip: "2001:db8:23::3"
          peer_asn: 65002
          address_families:
            - ipv6_unicast
      redistribute:
        - connected

  - name: R3
    asn: 65002
    interfaces:
      - name: eth0
        ipv4: "10.0.3.1/24"
        ipv6: "2001:db8:3::1/64"
      - name: eth1
        ipv4: "10.0.23.3/24"
        ipv6: "2001:db8:23::3/64"
    bgp:
      router_id: "3.3.3.3"
      address_families:
        - ipv6_unicast
      route_reflector_client: true
      neighbors:
        - peer_ip: "2001:db8:23::2"
          peer_asn: 65002
          address_families:
            - ipv6_unicast

links:
  - source: R1:eth1
    target: R2:eth1
  - source: R2:eth2
    target: R3:eth1

```

### capture-profiles.yaml

```yaml
# Minimal topology demonstrating  capture profiles.

# Topology metadata
name: capture-profiles
description: Capture profile example with OSPF-only capture on a node

devices:
  - name: R1
    type: router
    router_id: 10.0.0.1
    interfaces:
      - name: eth0
        ip: 10.0.12.1/24

  - name: R2
    type: router
    router_id: 10.0.0.2
    interfaces:
      - name: eth0
        ip: 10.0.12.2/24

links:
  - endpoints: [R1:eth0, R2:eth0]

ospf:
  routers: [R1, R2]

capture_profiles:
  ospf_only:
    filter: "proto ospf"
    output: "captures/{node}_ospf.pcap"
    scope:
      nodes: ["R1"]
    mode: capture_time

capture:
  profiles: ["ospf_only"]

```

### chaos-simple.yaml

```yaml
# Chaos Engineering Example - Simple Failure Injection
#
# Demonstrates basic failure patterns and cascade rules for chaos testing.
# This topology models a simple network where probabilistic link failures
# test resilience and demonstrate cascade behavior.

name: chaos-simple
description: Basic chaos monkey pattern with probabilistic failures and cascades

devices:
  - name: router-1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: eth0
        ip: 10.0.1.1/24
      - name: eth1
        ip: 10.0.2.1/24

  - name: router-2
    type: router
    router_id: 2.2.2.2
    interfaces:
      - name: eth0
        ip: 10.0.1.2/24
      - name: eth1
        ip: 10.0.3.1/24

  - name: host-1
    type: host
    interfaces:
      - name: eth0
        ip: 10.0.2.10/24
        gateway: 10.0.2.1

  - name: host-2
    type: host
    interfaces:
      - name: eth0
        ip: 10.0.3.10/24
        gateway: 10.0.3.1

links:
  - endpoints: [router-1:eth0, router-2:eth0]
    latency_ms: 1

  - endpoints: [router-1:eth1, host-1:eth0]
    latency_ms: 1

  - endpoints: [router-2:eth1, host-2:eth0]
    latency_ms: 1

# Failure pattern: Chaos monkey - random link failures
failure_patterns:
  - name: chaos-monkey
    trigger: !probabilistic
      check_interval: 100  # Check every 100 ticks
      probability: 0.1     #  chance of failure at each check
    selector:
      all: true  # Target all links
    action: fail_random_link
    recovery: !after_ticks
      ticks: 50  # Recover after 50 ticks (50ms)

# Cascade rule: When router fails, downstream host fails
cascade_rules:
  - name: router-failure-cascade
    trigger: !dependency_based
      primary_selector:
        link_name_pattern: "router-*"
      cascade_selector:
        link_name_pattern: "host-*"
      relationship: downstream
    action: fail_devices
    recovery: !permanent
    delay: 10  # 10 tick delay before cascade fires

```

### containerlab-bridge.yaml

```yaml
# Example topology showing an external TAP bridge.
#
# NOTE: This uses a host TAP interface name (e.g. tap0).

devices:
  - name: sw1
    type: Switch

  - name: ext0
    type: External
    tap:
      interface_name: tap0

links:
  - endpoints: ["ext0:tap0", "sw1:port0"]

```

### data-center.yaml

```yaml
name: data-center
description: |
  Data center spine-leaf topology with 2 spine routers and 4 leaf switches.
  Each leaf connects to both spines for redundancy. Servers are attached
  to leaf switches.

devices:
  # Spine layer (routers for L3 routing)
  - name: spine1
    type: router
    router_id: 10.255.1.1
    interfaces:
      - name: eth0
        ip: 10.0.11.1/30
        ospf: { area: 0, cost: 1 }
      - name: eth1
        ip: 10.0.12.1/30
        ospf: { area: 0, cost: 1 }
      - name: eth2
        ip: 10.0.13.1/30
        ospf: { area: 0, cost: 1 }
      - name: eth3
        ip: 10.0.14.1/30
        ospf: { area: 0, cost: 1 }

  - name: spine2
    type: router
    router_id: 10.255.1.2
    interfaces:
      - name: eth0
        ip: 10.0.21.1/30
        ospf: { area: 0, cost: 1 }
      - name: eth1
        ip: 10.0.22.1/30
        ospf: { area: 0, cost: 1 }
      - name: eth2
        ip: 10.0.23.1/30
        ospf: { area: 0, cost: 1 }
      - name: eth3
        ip: 10.0.24.1/30
        ospf: { area: 0, cost: 1 }

  # Leaf layer (routers with switch ports for servers)
  - name: leaf1
    type: router
    router_id: 10.255.2.1
    interfaces:
      - name: spine1
        ip: 10.0.11.2/30
        ospf: { area: 0, cost: 1 }
      - name: spine2
        ip: 10.0.21.2/30
        ospf: { area: 0, cost: 1 }
      - name: servers
        ip: 10.1.1.1/24
        ospf: { area: 0, cost: 10 }

  - name: leaf2
    type: router
    router_id: 10.255.2.2
    interfaces:
      - name: spine1
        ip: 10.0.12.2/30
        ospf: { area: 0, cost: 1 }
      - name: spine2
        ip: 10.0.22.2/30
        ospf: { area: 0, cost: 1 }
      - name: servers
        ip: 10.1.2.1/24
        ospf: { area: 0, cost: 10 }

  - name: leaf3
    type: router
    router_id: 10.255.2.3
    interfaces:
      - name: spine1
        ip: 10.0.13.2/30
        ospf: { area: 0, cost: 1 }
      - name: spine2
        ip: 10.0.23.2/30
        ospf: { area: 0, cost: 1 }
      - name: servers
        ip: 10.1.3.1/24
        ospf: { area: 0, cost: 10 }

  - name: leaf4
    type: router
    router_id: 10.255.2.4
    interfaces:
      - name: spine1
        ip: 10.0.14.2/30
        ospf: { area: 0, cost: 1 }
      - name: spine2
        ip: 10.0.24.2/30
        ospf: { area: 0, cost: 1 }
      - name: servers
        ip: 10.1.4.1/24
        ospf: { area: 0, cost: 10 }

  # Access switches for servers
  - name: tor1
    type: switch
    interfaces:
      - name: uplink
      - name: port1
      - name: port2
      - name: port3

  - name: tor2
    type: switch
    interfaces:
      - name: uplink
      - name: port1
      - name: port2
      - name: port3

  - name: tor3
    type: switch
    interfaces:
      - name: uplink
      - name: port1
      - name: port2

  - name: tor4
    type: switch
    interfaces:
      - name: uplink
      - name: port1
      - name: port2

  # Servers (rack 1 - web tier)
  - name: web1
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.1.10/24
        gateway: 10.1.1.1

  - name: web2
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.1.11/24
        gateway: 10.1.1.1

  - name: web3
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.1.12/24
        gateway: 10.1.1.1

  # Servers (rack 2 - app tier)
  - name: app1
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.2.10/24
        gateway: 10.1.2.1

  - name: app2
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.2.11/24
        gateway: 10.1.2.1

  - name: app3
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.2.12/24
        gateway: 10.1.2.1

  # Servers (rack 3 - database tier)
  - name: db1
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.3.10/24
        gateway: 10.1.3.1

  - name: db2
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.3.11/24
        gateway: 10.1.3.1

  # Servers (rack 4 - storage tier)
  - name: storage1
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.4.10/24
        gateway: 10.1.4.1

  - name: storage2
    type: host
    interfaces:
      - name: eth0
        ip: 10.1.4.11/24
        gateway: 10.1.4.1

links:
  # Spine to leaf (full mesh)
  - endpoints: [spine1:eth0, leaf1:spine1]
  - endpoints: [spine1:eth1, leaf2:spine1]
  - endpoints: [spine1:eth2, leaf3:spine1]
  - endpoints: [spine1:eth3, leaf4:spine1]

  - endpoints: [spine2:eth0, leaf1:spine2]
  - endpoints: [spine2:eth1, leaf2:spine2]
  - endpoints: [spine2:eth2, leaf3:spine2]
  - endpoints: [spine2:eth3, leaf4:spine2]

  # Leaf to ToR switches
  - endpoints: [leaf1:servers, tor1:uplink]
  - endpoints: [leaf2:servers, tor2:uplink]
  - endpoints: [leaf3:servers, tor3:uplink]
  - endpoints: [leaf4:servers, tor4:uplink]

  # Servers to ToR switches
  - endpoints: [tor1:port1, web1:eth0]
  - endpoints: [tor1:port2, web2:eth0]
  - endpoints: [tor1:port3, web3:eth0]

  - endpoints: [tor2:port1, app1:eth0]
  - endpoints: [tor2:port2, app2:eth0]
  - endpoints: [tor2:port3, app3:eth0]

  - endpoints: [tor3:port1, db1:eth0]
  - endpoints: [tor3:port2, db2:eth0]

  - endpoints: [tor4:port1, storage1:eth0]
  - endpoints: [tor4:port2, storage2:eth0]

script:
  # Verify spine routing and OSPF
  - at: converged
    device: spine1
    command: show ip route

  - at: converged
    device: spine1
    command: show ospf neighbors

  # Web to database connectivity (cross-rack)
  - at: converged + 100
    device: web1
    command: ping 10.1.3.10

  # Trace path through fabric
  - at: converged + 2s
    device: web1
    command: traceroute 10.1.4.10

  # App to database (adjacent racks)
  - at: converged + 3s
    device: app1
    command: ping 10.1.3.11

```

---

## Usage



---

## Architecture



---

## Roadmap

- IPv6 support
- RSVP-TE for traffic engineering
- Enhanced MPLS L3VPN features
- VLANs and 802.1Q tagging

See `.planning/ROADMAP.md` for full roadmap.

- [x] Tick-based execution with deterministic ordering — v1.0
- [x] Queue-based packet flow between devices — v1.0
- [x] Convergence detection via FIB stability — v1.0
- [x] Device trait with interfaces, queues, and counters — v1.0
- [x] RIB/FIB separation with admin distance selection — v1.0
- [x] Ethernet framing and IPv4 forwarding — v1.0
- [x] ARP resolution with cache and request/reply — v1.0
- [x] ICMP echo, TTL exceeded, destination unreachable — v1.0
- [x] ping, traceroute, show commands — v1.0
- [x] OSPF adjacency, LSA flooding, SPF calculation — v1.0
- [x] Multi-hop routing via LSDB synchronization — v1.0

**v1.1 Scale & Features (15 requirements):**
- [x] Tokio parallel device processing (REQ-ENGINE-006) — v1.1
- [x] 100+ device topology benchmarks — v1.1
- [x] YAML/JSON topology file loading (REQ-TOPO-002) — v1.1
- [x] Structured logging with tracing (REQ-OBS-001) — v1.1
- [x] Packet capture export (REQ-OBS-002) — v1.1
- [x] Multi-access OSPF with DR/BDR (REQ-OSPF-008) — v1.1
- [x] Latency/loss modeling hooks (REQ-WIRE-002/003) — v1.1
- [x] iBGP and eBGP routing protocol (REQ-BGP-001) — v1.1
- [x] Name resolution via centralized registry (REQ-DNS-001) — v1.1
- [x] Traffic generation (CBR, Poisson, Burst) — v1.1
- [x] Realistic benchmark scenarios with traffic — v1.1

**v1.2 Engine Hardening (14 requirements):**
- [x] Quiescence detection (control plane packet tracking) — v1.2
- [x] Custom convergence hooks (enter/sustain/exit callbacks) — v1.2
- [x] Dynamic wire removal with graceful/immediate modes — v1.2
- [x] Dynamic device removal with cascade cleanup — v1.2
- [x] Tick .2

**v1.3 Automation (11 requirements):**
- [x] Scheduled events at specific simulation ticks — v1.3
- [x] Python bindings via PyO3 (netsim-py package) — v1.3
- [x] REST API for remote simulation control — v1.3
- [x] OpenAPI documentation and SSE real-time events — v1.3

**v1.4 Observability & Export (47 requirements):**
- [x] Export Infrastructure (EXP-01 through EXP-08) — v1.4
  - SimulationClock for tick-to-wallclock conversion
  - ExportSink trait (file/UDP/memory) with non-blocking I/O
  - MemoryBudget with VecDeque ring buffers
  - StreamingWriter for tick-based flushing
- [x] Pcap Export (PCAP-01 through PCAP-10) — v1.4
  - Pcap/pcapng file export with Wireshark compatibility
  - Wall-clock timestamps (microsecond/nanosecond precision)
  - Per-interface filtering with glob patterns
- [x] NetFlow v9 Export (NF9-01 through NF9-18) — v1.4
  - 5-tuple flow aggregation with tick-based timeouts
  - Template and data record generation via netgauze-flow-pkt
  - UDP streaming to port 2055
- [x] IPFIX Export (IPFIX-01 through IPFIX-11) — v1.4
  - RFC 7011 compliance with version 10 headers
  - + code reuse via FlowKey/FlowRecord/FlowTable re-exports
  - Enterprise IE registration API

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## The Insight

Network simulation usually falls into two traps: it's either too slow (VM-based emulation) or too abstract (mathematical models). **netsim** takes a middle path-deterministic, tick-based protocol simulation. It doesn't emulate the kernel; it simulates the logic of routing protocols. This allows you to validate massive topologies in seconds, ensuring that a configuration change won't cause a routing loop before it ever hits a real router.

---

## Overview

netsim is a deterministic, tick-based network protocol simulator that validates network configurations before production deployment. It provides protocol-level fidelity with guaranteed reproducibility: same topology always produces same results.

---

## Problem It Solves

Network engineers need to validate configurations before deploying to production. Current options:

- **Full emulation** (Containerlab, GNS3, EVE-NG): Runs device images and real network stacks. Slower and more resource-intensive than protocol simulation.
- **Real hardware labs**: Expensive, requires physical space, limited scale.
- **Production testing**: Risky, causes outages when configs have errors.

netsim provides fast, deterministic simulation with protocol-level fidelity. Catch routing loops, unreachable hosts, and misconfigurations before touching production.

---

## # Tick-Based Execution

Simulation advances in discrete time units ("ticks", ~1ms simulated time). All devices process packets in lockstep for determinism.

---

## # RIB/FIB Separation

Mirrors real router behavior:

- **RIB** (Routing Information Base): Holds all learned routes from protocols
- **FIB** (Forwarding Information Base): Holds active best paths used for forwarding

---

## # Convergence Detection

Automatically detects when network stabilizes (no routing changes for N ticks). Scripts can trigger commands "at: converged" or "converged + 100" ticks.

---

## # Wires as Devices

Links are first-class simulation participants, enabling future latency/loss modeling without architectural changes.

---

## Protocols Implemented



---

## # Routing Protocols

**OSPF (Open Shortest Path First):**

- Point-to-point adjacencies with hello/dead timers
- LSA flooding (Types 1 & 2)
- SPF calculation via Dijkstra's algorithm
- Area 0 support

**IS-IS (Intermediate System to Intermediate System):**

- L1/L2 hierarchical routing
- LSP flooding with sequence numbers
- SPF calculation across levels
- Area-based routing

**BGP (Border Gateway Protocol):**

- iBGP and eBGP sessions
- Route propagation with communities
- RIB/FIB integration
- `show bgp neighbors` support

---

## # MPLS & Tunneling

**MPLS (Multiprotocol Label Switching):**

- Label imposition, swap, and pop operations
- LFIB (Label Forwarding Information Base)
- MPLS OAM for LSP verification

**LDP (Label Distribution Protocol):**

- Automatic label binding and distribution
- Targeted sessions
- Integration with IGP

**GRE (Generic Routing Encapsulation):**

- Layer 3 overlay connectivity
- IP-in-IP encapsulation
- IGP over GRE support

**VRF (Virtual Routing and Forwarding):**

- L3VPN foundations
- Per-VRF routing tables
- Route import/export

---

## # Resilience

**BFD (Bidirectional Forwarding Detection):**

- Subsecond failure detection
- Async mode with configurable timers
- Integration with OSPF for fast convergence

---

## # Layer 2/3

**ARP:** Request/reply with proper cache management
**ICMP:** Echo (ping), Time Exceeded (traceroute), Destination Unreachable
**IPv4:** Forwarding, TTL handling, fragmentation not supported

---

## # YAML Topology Definition

```yaml
name: ospf-triangle
description: Three OSPF routers with hosts

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

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r1:eth1, r3:eth0]

script:
  - at: converged
    device: r1
    command: show ip route
  - at: converged + 100
    device: h1
    command: ping 10.0.3.10
```

---

## # CLI Usage

```bash
# Run simulation
netsim run examples/ospf-triangle.yaml

# JSON output for CI/CD
netsim run topology.yaml -f json -o results.json

# Set tick limit for long simulations
netsim run large-topology.yaml --max-ticks 50000
```

---

## # Daemon Mode (Interactive)

```bash
# Start the daemon
netsim daemon --topology topology.yaml

# Connect with the CLI
netsim cli --target localhost:50051

# Example session
show ip route
show bgp neighbors
interface eth0 shutdown
interface eth0 no shutdown
```

---

## # Scenario Runs

```bash
# Validate convergence and dump JSON for CI
netsim run topology.yaml --run-until converged -f json -o results.json

# Inject a link failure at a specific time window
netsim run topology.yaml --event "tick=200,link_down=r1:eth0-r2:eth0" --event "tick=800,link_up=r1:eth0-r2:eth0"

# Run a longer scenario and cap ticks
netsim run large-topology.yaml --max-ticks 50000
```

---

## # Available Commands

**Diagnostics:**

- `ping <ip>` - ICMP echo with round-trip confirmation
- `traceroute <ip>` - Hop-by-hop path discovery
- `show ip route` - Display RIB
- `show arp` - Display ARP cache

**Protocol-Specific:**

- `show isis database` - IS-IS link-state database
- `show isis neighbors` - IS-IS adjacencies
- `show mpls forwarding` - MPLS LFIB
- `show ldp bindings` - LDP label bindings
- `show bfd sessions` - BFD session state
- `show vrf` - VRF configuration
- `show bgp neighbors` - BGP peer status

**Traffic:**

- `show traffic` - Traffic statistics (sent/received, latency percentiles)

---

## # Output Formats

**ASCII:** Human-readable tables (default)
**JSON:** Machine-parseable for scripting and CI/CD

---

## Automation

```python
import netsim_py

engine = netsim_py.Engine()
engine.load_topology("topology.yaml")
engine.run_until_converged()
engine.execute_command("router1", "show ip route")
```

Python API available via PyO3 bindings in `crates/netsim-py` for programmatic access and integration with existing Python workflows.

---

## Examples

Repository includes examples for:

- Simple two-host connectivity
- OSPF triangle with three routers
- IS-IS hierarchical routing (L1/L2)
- MPLS/LDP label distribution
- BFD fast failure detection
- GRE overlay tunnels
- Traffic generation with statistics

---

## Development Status

Active development with regular protocol additions and improvements.

**Recently Added:**

- L2 bridge domains, VXLAN data plane, BGP EVPN Type-2/3/5, IRB anycast gateway (v1.8)
- LACP/LAG with hash-based load distribution, LLDP neighbor discovery (v1.8)
- EVPN multi-homing with ESI and DF election (v1.8)
- IPv6 forwarding, NDP, ICMPv6, OSPFv3, MP-BGP IPv6 Unicast (v2.0)
- Dual-stack integration and benchmarking (v2.0)
- Wire jitter, pattern-based impairments, traffic matrix patterns, failure injection (v1.9)

---

## # Validated

**v1.6 MPLS L3VPN & TE + Telemetry:**
- [x] MPLS L3VPN (VRFs) — BGP/MPLS VPN (RFC 4364)
- [x] RSVP-TE — Explicit-path TE tunnels (RFC 3209)
- [x] BMP export — BGP Monitoring Protocol telemetry stream (RFC 7854)
- [x] Advanced PCAP filtering — on-the-wire frame filtering (MPLS-aware)

**v1.7 SR-MPLS, Daemon Mode & Routing Matrix:**
- [x] SR-MPLS forwarding foundations (SRGB, Node-SID, SR LFIB/FTN with deterministic precedence)
- [x] Daemon mode with gRPC command channel, IOS-like CLI, tab completion
- [x] Interface shutdown/no-shutdown with protocol teardown and reconvergence
- [x] Routing matrix export (REST API, CLI, periodic file, convergence-triggered)
- [x] Convergence detection hardening (BGP Loc-RIB stability, IS-IS convergence signal)
- [x] E2E test suite expansion (cross-protocol failure, ECMP, L3VPN, determinism validation)

**v1.8 Data Center Fabric & EVPN (shipped 2026-02-28):**
- [x] L2 bridge domains with per-BD FDB, MAC learning, aging, BUM flooding 
- [x] VXLAN data plane — RFC 7348 encap/decap, VTEP endpoints, head-end replication 
- [x] BGP EVPN control plane — Type-2 (MAC/IP), Type-3 (IMET), ARP suppression 
- [x] EVPN Type-5 (IP prefix) + IRB with anycast gateway for inter-subnet routing 
- [x] LACP/LAG with hash-based load distribution, LACP PDU negotiation 
- [x] LLDP neighbor discovery with TTL aging, `show lldp neighbors` 
- [x] EVPN multi-homing — ESI, DF election (service-carving), Type-1/4 routes 

**v1.9 Advanced Impairments & Topology Patterns (shipped 2026-02-28):**
- [x] Uniform and Gaussian jitter models for wire-level latency variation 
- [x] Pattern-based link impairments — declarative profiles, selectors, distance-based latency 
- [x] Gravity-model traffic matrix generation with node importance weighting 
- [x] Declarative failure injection — time-based, correlated, cascading failures with dry-run 

**v2.0 IPv6 Foundation (shipped 2026-03-01):**
- [x] IPv6 forwarding with NDP , ICMPv6 
- [x] OSPFv3 for IPv6 routing 
- [x] MP-BGP IPv6 Unicast (AFI 2, SAFI 1) 
- [x] Dual-stack integration and performance benchmarking

---

## # Out of Scope

- Vendor bug replication — idealized behavior only
- TCP congestion algorithms — not the goal
- GUI/visual topology editor — text-based only
- SCTP transport for IPFIX — UDP sufficient for simulator

---

## Context

**Shipped:** v1.8 DC Fabric & EVPN (2026-02-28) + v1.9 Impairments & Patterns (2026-02-28) + v2.0 IPv6 Foundation (2026-03-01)
- ~200,000+ lines of Rust
- 72+ phases, 302+ plans across 11 milestones shipped
- 2,200+ tests passing
- 11 milestones shipped (v1.0 through v1.9, v2.0)

**Tech stack:** Rust, Tokio (parallel), PetGraph (SPF), ipnet (CIDR), comfy-table (CLI), tracing (logging), pcap-file (capture), netgauze-flow-pkt (NetFlow/IPFIX), axum (REST), pyo3 (Python)

**Architecture:** Parallel tick-based execution with adaptive thresholds, device-per-tick processing, deterministic packet ordering via timestamps. Quiescence-based convergence detection with programmable hooks. Safe dynamic topology modification via deferred removal queue. Export infrastructure with non-blocking sinks and tick-based timeouts.

---

## Constraints

- **Language**: Rust — performance critical for large-scale simulation
- **Graph library**: PetGraph — for SPF/Dijkstra calculations
- **Execution model**: Tokio parallel with serial fallback

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| FIB stability for convergence | Clean signal without tracking protocol internals | ✓ Good |
| RIB + FIB separation | Scales to multi-protocol (BGP later), proper networking model | ✓ Good |
| Wires as first-class devices | Uniform abstraction, latency/loss hooks ready for future | ✓ Good |
| Packet timestamps for ordering | Solves parallel processing ordering without sub-tick complexity | ✓ Good |
| Serial before Tokio | Simpler debugging, validate architecture first | ✓ Good |
| PetGraph for SPF | Proven Rust graph library for Dijkstra | ✓ Good |
| Batch execution model | Simpler than interactive CLI, validates core loop first | ✓ Good |
| BTreeMap for LSDB | Deterministic iteration order for reproducible SPF | ✓ Good |
| Fast-path to Full for P2P | Skip DBD exchange complexity for MVP | ✓ Good |
| LSU flooding on adjacency | Simple reliable LSDB sync without LSR/LSAck | ✓ Good |
| Parallel with spawn_blocking | CPU-bound tick mitigation for parallel execution | ✓ Good |
| Adaptive parallelism thresholds | Avoid overhead on small topologies | ✓ Good |
| Rate as packets_per_tick | Efficient tick-based traffic generation | ✓ Good |
| Latency samples capped at 10k | Prevent unbounded memory in long simulations | ✓ Good |
| SmallRng seeded from device_id | Deterministic Poisson generation | ✓ Good |
| IpProtocol::BgpControl = 254 | Internal BGP transport over simulator fabric | ✓ Good |
| Control plane = OSPF/BGP/ARP | Quiescence ignores data plane traffic (ICMP, TrafficData) | ✓ Good |
| Quiescence window = 5 ticks | Conservative default ensures real stability | ✓ Good |
| Hooks receive &Engine | No separate EngineState type, full access to public API | ✓ Good |
| std::mem::take for hook invocation | Avoids borrow conflicts during mutable callback + shared engine | ✓ Good |
| Wire removal queued | Safe removal during parallel tick execution | ✓ Good |
| Device dropped on removal | User preference over returning device to caller | ✓ Good |
| apply_pending_removals at Phase 0 | Before any device access, ensures clean state | ✓ Good |
| SimulationClock for timestamps | Maps ticks to wall-clock with configurable epoch | ✓ Good |
| ExportSink non-blocking I/O | Never stall simulation on export backpressure | ✓ Good |
| Tick-based flow timeouts | Deterministic behavior, not wall-clock dependent | ✓ Good |
| FlowTable re-export for IPFIX | + code reuse between NetFlow v9 and IPFIX | ✓ Good |
| Template ID 256 | Standard starting ID for user templates | ✓ Good |

---

## Current Milestone: v2.1 Enterprise & Campus Protocols

**Goal:** Enable validation of campus network designs with gateway redundancy (VRRP) and DHCP relay services across subnets.

**Target features:**
- VRRP (Virtual Router Redundancy Protocol) with master election, priority-based preemption, and sub-second failover
- DHCP relay agent for cross-subnet DHCP service with Option 82 insertion
- Integration with routing protocols (VIP route installation, subnet alignment)
- Observability commands for VRRP state and DHCP relay statistics

**Success criteria:**
- VRRP master election observable with priority tracking
- Failover scenarios validated with sub-second convergence timing
- DHCP relay works across subnets with proper Option 82 handling
- VRRP VIP routes integrate correctly with FIB

---

## Future Milestones (Proposed)

- **v1.10 Engine Hardening & Protocol Fidelity** — Phases 111-115
- **v1.11 Advanced Analysis & Assertions** — Phases 116-119
- **v2.2 Advanced Transport** — Phases 75-77
- **v2.3 Multicast** — Phases 78-79
- **v2.4 Chaos Engineering & Performance** — Phases 80-82
- **v2.5 Intelligent Simulation & Scale** — Phases 83-85
- **v2.6 Ecosystem & Digital Twin** — Phases 86-96
- **v2.7 Production-Grade E2E Test Suite** — Phases 101-104
- **v2.8 Security & Policy Framework** — Phases 105-110
- **v2.11 Optical & Transport Layer**
- **v2.12 Modern Management Plane** — Phases 120-123

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. netsim provides protocol simulation and routing validation — the "simulate" stage of the pipeline.

**Role:** Validate routing convergence and protocol behavior for topologies generated by topogen or modeled by ank-pydantic. Export FIBs and routing state for traffic analysis by netflowsim.

**Key integration points:**
- Consumes topology from topogen (direct netsim YAML export) or ank-pydantic (`export_netsim()`)
- FIB/routing matrix export feeds netflowsim for traffic engineering analysis
- Workbench orchestrates simulation via subprocess and gRPC daemon
- BMP telemetry and PCAP capture provide observability

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities
- [Cross-Project Data Contracts](../../topogen/.planning/ARCHITECTURE.md) — ownership boundaries and format specifications

*Last updated: 2026-03-01 after starting v2.1 Enterprise & Campus Protocols milestone*

---

## Current Status

2026-03-04 — Completed  (Visual Path Tracing Analysis)

---

## Roadmap

- **v1.10 Engine Hardening & Protocol Fidelity** (Proposed) — Phases 111-115
- **v1.11 Advanced Analysis & Assertions** (Proposed) — Phases 116-119
- **v2.2 Advanced Transport** (Proposed) — Phases 75-77
- **v2.3 Multicast** (Proposed) — Phases 78-79
- **v2.4 Chaos Engineering & Performance** (Proposed) — Phases 80-82

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
