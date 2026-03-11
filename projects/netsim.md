---
layout: default
section: network-automation
description: "Deterministic tick-based network protocol simulator validating configurations before production deployment."
---

# Network Simulator

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [Usage](#usage)
- [Architecture](#architecture)
- [Roadmap](#roadmap)
- [Current Status](#current-status)

## Concept

Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.

Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.

---

## Technical Reports

- [Download Research Paper: paper.pdf](/assets/docs/netsim-paper.pdf)
- [Download Research Paper: techreport.pdf](/assets/docs/netsim-techreport.pdf)

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
- **[bgp-ipv6-multi-as.yaml](bgp-ipv6-multi-as.yaml)**: IPv6 eBGP + iBGP (RR) reference topology.
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

### Integration & Interop
- **[containerlab-bridge.yaml](containerlab-bridge.yaml)**: Bridge a simulated switch to a host TAP interface.

### Services
- **[dhcp-relay-simple.yaml](dhcp-relay-simple.yaml)**: Minimal DHCP relay (helper-address) topology.

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

### assertion-failure.yaml

```yaml
name: assertion-failure-demo
description: |
  A demo showing how netsim catches configuration errors using assertions.
  In this version, r2 has NO OSPF configured on its interface,
  so r1 will never form an OSPF adjacency - causing the assertion to fail.

devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: eth0
        ip: 10.0.0.1/24
        ospf: { area: 0 }

  - name: r2
    type: router
    router_id: 2.2.2.2
    interfaces:
      - name: eth0
        ip: 10.0.0.2/24
        # ERROR: No OSPF configured (should have ospf: { area: 0 })

links:
  - endpoints: ["r1:eth0", "r2:eth0"]

assertions:
  - type: ospf_neighbor_state
    router: r1
    interface: eth0
    expected_state: Full

```

### assertion-success.yaml

```yaml
name: assertion-success-demo
description: |
  A demo showing how netsim validates correct configuration using assertions.
  In this fixed version, OSPF areas MATCH (Area 0),
  allowing the adjacency assertion to pass.

devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: eth0
        ip: 10.0.0.1/24
        ospf: { area: 0 } # Fixed area

  - name: r2
    type: router
    router_id: 2.2.2.2
    interfaces:
      - name: eth0
        ip: 10.0.0.2/24
        ospf: { area: 0 } # Fixed area

links:
  - endpoints: ["r1:eth0", "r2:eth0"]

assertions:
  - type: ospf_neighbor_state
    router: r1
    interface: eth0
    expected_state: Full

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
name: bgp-ipv6-multi-as
description: |
  Reference topology for IPv6 BGP across multiple ASNs.

  Intent:
  - r1 (AS 65001) peers eBGP to r2 (AS 65002) over IPv6
  - r2 peers iBGP to r3 (AS 65002) and acts as an RR

devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: eth0
        ipv6: [2001:db8:12::1/64]
    bgp:
      as: 65001
      address_families: [ipv6_unicast]
      neighbors:
        - ip: 2001:db8:12::2
          remote_as: 65002

  - name: r2
    type: router
    router_id: 2.2.2.2
    interfaces:
      - name: eth0
        ipv6: [2001:db8:12::2/64]
      - name: eth1
        ipv6: [2001:db8:23::2/64]
    bgp:
      as: 65002
      address_families: [ipv6_unicast]
      neighbors:
        - ip: 2001:db8:12::1
          remote_as: 65001
        - ip: 2001:db8:23::3
          remote_as: 65002
          route_reflector_client: true

  - name: r3
    type: router
    router_id: 3.3.3.3
    interfaces:
      - name: eth0
        ipv6: [2001:db8:23::3/64]
    bgp:
      as: 65002
      address_families: [ipv6_unicast]
      neighbors:
        - ip: 2001:db8:23::2
          remote_as: 65002

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r2:eth1, r3:eth0]

checks:
  - description: r1 sees r3 over IPv6 via r2
    nodes:
      - name: r1
        cmd: show bgp ipv6 summary

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

### case-study-enterprise.yaml

```yaml
name: enterprise-dc-case-study
description: |
  A comprehensive enterprise data center case study demonstrating:
  - Spine-Leaf topology with redundant spines
  - OSPF for internal fabric routing
  - iBGP for cross-fabric prefix propagation
  - Interface failure recovery and path re-convergence
  - Post-convergence reachability validation

devices:
  # Spines (L3 Fabric Core)
  - name: spine1
    type: router
    router_id: 10.255.0.1
    interfaces:
      - { name: eth0, ip: 10.0.11.1/30, ospf: { area: 0, cost: 10 } }
      - { name: eth1, ip: 10.0.12.1/30, ospf: { area: 0, cost: 10 } }
      - { name: lo0, ip: 10.255.0.1/32, ospf: { area: 0, cost: 0 } }
    bgp:
      as: 65001
      neighbors:
        - { ip: 10.0.11.2, remote_as: 65001, description: "leaf1-ibgp" }
        - { ip: 10.0.12.2, remote_as: 65001, description: "leaf2-ibgp" }

  - name: spine2
    type: router
    router_id: 10.255.0.2
    interfaces:
      - { name: eth0, ip: 10.0.21.1/30, ospf: { area: 0, cost: 10 } }
      - { name: eth1, ip: 10.0.22.1/30, ospf: { area: 0, cost: 10 } }
      - { name: lo0, ip: 10.255.0.2/32, ospf: { area: 0, cost: 0 } }
    bgp:
      as: 65001
      neighbors:
        - { ip: 10.0.21.2, remote_as: 65001, description: "leaf1-ibgp" }
        - { ip: 10.0.22.2, remote_as: 65001, description: "leaf2-ibgp" }

  # Leaves (L3 Access)
  - name: leaf1
    type: router
    router_id: 10.255.1.1
    interfaces:
      - { name: spine1, ip: 10.0.11.2/30, ospf: { area: 0, cost: 10 } }
      - { name: spine2, ip: 10.0.21.2/30, ospf: { area: 0, cost: 10 } }
      - { name: servers, ip: 10.1.1.1/24, ospf: { area: 0, cost: 100 } }
      - { name: lo0, ip: 10.255.1.1/32, ospf: { area: 0, cost: 0 } }
    bgp:
      as: 65001
      neighbors:
        - { ip: 10.0.11.1, remote_as: 65001, description: "spine1-ibgp" }
        - { ip: 10.0.21.1, remote_as: 65001, description: "spine2-ibgp" }

  - name: leaf2
    type: router
    router_id: 10.255.1.2
    interfaces:
      - { name: spine1, ip: 10.0.12.2/30, ospf: { area: 0, cost: 10 } }
      - { name: spine2, ip: 10.0.22.2/30, ospf: { area: 0, cost: 10 } }
      - { name: servers, ip: 10.1.2.1/24, ospf: { area: 0, cost: 100 } }
      - { name: lo0, ip: 10.255.1.2/32, ospf: { area: 0, cost: 0 } }
    bgp:
      as: 65001
      neighbors:
        - { ip: 10.0.12.1, remote_as: 65001, description: "spine1-ibgp" }
        - { ip: 10.0.22.1, remote_as: 65001, description: "spine2-ibgp" }

  # Hosts
  - name: web1
    type: host
    interfaces:
      - { name: eth0, ip: 10.1.1.10/24, gateway: 10.1.1.1 }

  - name: db1
    type: host
    interfaces:
      - { name: eth0, ip: 10.1.2.10/24, gateway: 10.1.2.1 }

links:
  # Spines to Leaves
  - endpoints: [spine1:eth0, leaf1:spine1]
  - endpoints: [spine1:eth1, leaf2:spine1]
  - endpoints: [spine2:eth0, leaf1:spine2]
  - endpoints: [spine2:eth1, leaf2:spine2]
  # Hosts to Leaves
  - endpoints: [leaf1:servers, web1:eth0]
  - endpoints: [leaf2:servers, db1:eth0]

script:
  # Initial convergence check
  - at: converged
    device: spine1
    command: show ip route

  - at: converged
    device: web1
    command: ping 10.1.2.10

  # Failure scenario: shut spine1 link to leaf1
  - at: converged + 100
    device: leaf1
    command: interface shutdown spine1

  # Check reconvergence via spine2
  - at: converged + 500
    device: leaf1
    command: show ip route

  - at: converged + 600
    device: web1
    command: ping 10.1.2.10

  # Trace path (should show spine2)
  - at: converged + 1s
    device: web1
    command: traceroute 10.1.2.10

  # Restore link
  - at: converged + 2s
    device: leaf1
    command: interface no shutdown spine1

```

### chaos-impairments.yaml

```yaml
name: chaos-impairments-demo
description: |
  A demo showing link impairments: latency and packet loss.
  One link has high latency (50ms) and another has packet loss ().

devices:
  - name: h1
    type: host
    interfaces:
      - name: eth0
        ip: 10.0.1.10/24
        gateway: 10.0.1.1

  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: eth0
        ip: 10.0.1.1/24
      - name: eth1
        ip: 10.0.2.1/24

  - name: h2
    type: host
    interfaces:
      - name: eth0
        ip: 10.0.2.10/24
        gateway: 10.0.2.1

links:
  # Link with high latency
  - endpoints: ["h1:eth0", "r1:eth0"]
    latency_ms: 50

  # Link with packet loss
  - endpoints: ["r1:eth1", "h2:eth0"]
    loss_percent: 10

script:
  # Ping from h1 to h2 (50ms + 1ms processing = 50ms+ RTT)
  # Some packets will drop because of loss on the second link
  - at: converged
    device: h1
    command: ping 10.0.2.10

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

---

## Visuals

### Basic Validation
![Simulator Demo](/images/netsim-basic-demo.gif)

### Interactive Daemon Mode
![Daemon Demo](/images/netsim-daemon-demo.gif)

### Enterprise Case Study
![Enterprise Case Study](/images/netsim-case-study-enterprise.gif)

---

## Usage

```bash
# Run simulation
netsim run examples/ospf-triangle.yaml

# JSON output for CI/CD
netsim run topology.yaml -f json -o results.json

# Daemon mode (interactive)
netsim daemon --topology topology.yaml

# Connect with CLI
netsim cli --target localhost:50051
```

<details class="code-collapse">
<summary>Python bindings</summary>

```python
import netsim_py

engine = netsim_py.Engine()
engine.load_topology("topology.yaml")
engine.run_until_converged()
engine.execute_command("router1", "show ip route")
```

</details>

---

## Architecture

<div class="mermaid">
flowchart LR
    A[Deliver<br/>Packets] --> B[Process<br/>Routers]
    B --> C{Quiescent?}
    C -->|No| D[Increment<br/>Clock]
    D --> A
    C -->|Yes| E[Converged]
</div>

Parallel tick-based execution with adaptive thresholds and device-per-tick processing. Deterministic packet ordering via timestamps. Quiescence-based convergence detection with programmable hooks.

**RIB/FIB separation** mirrors real router behavior — all learned routes go to the RIB, best paths are installed in the FIB. Admin distance selection across protocols.

**Wires as devices** — links are first-class simulation participants with latency, loss, and jitter modeling.

~247,000 lines of Rust. 2,192 tests. 13 milestones shipped.

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
| **Stack** | Rust |

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

**Shipped:** v2.1 Enterprise & Campus (2026-03-04) + v1.11 Advanced Analysis (2026-03-06)
- ~247,000 lines of Rust
- 80 phases, 311 plans across 13 milestones shipped
- 2,192 tests passing
- 13 milestones shipped (v1.0 through v1.11, v2.0-v2.1)

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

## # Validated (v2.1 Enterprise & Campus — shipped 2026-03-04)

- [x] DHCP relay agent with Option 82 (Circuit ID + Remote ID) — v2.1
- [x] VRRPv2/v3 master election with virtual MAC and preemption — v2.1
- [x] IPv6 VRRP with Unsolicited Neighbor Advertisement — v2.1
- [x] Interface tracking with dynamic priority adjustment — v2.1
- [x] VRF-aware DHCP relay with VRRP GIADDR integration — v2.1

---

## # Validated (v1.11 Advanced Analysis — shipped 2026-03-06)

- [x] Declarative assertion framework with CI/CD exit codes — v1.11
- [x] Topology diff with change impact analysis — v1.11
- [x] Link capacity and utilization model with bottleneck detection — v1.11
- [x] Visual path tracing with anomaly detection (loops, blackholes, asymmetry) — v1.11

---

## Current Milestone: v2.2 Advanced Transport

**Goal:** Add SRv6, MPLS-TP, and TWAMP protocols to extend the simulator's transport and measurement capabilities.

**Target features:**
- SRv6 with Segment Routing Header, SID lists, End/End.X/End.DT behaviors, and SRv6 Policy
- MPLS-TP with static LSPs, OAM (CC/CV/RDI), and linear protection switching (1+1/1:1)
- TWAMP with control + test protocols, session negotiation, and bidirectional latency/jitter/loss measurement

---

## Future Milestones (Proposed)

- **v2.3 Multicast** — IGMP/MLD, PIM-SM
- **v2.4 Chaos Engineering & Performance**
- **v2.5 Intelligent Simulation & Scale**
- **v2.6 Ecosystem & Digital Twin**
- **v2.7 Production-Grade E2E Test Suite**
- **v2.8 Security & Policy Framework**
- **v2.11 Optical & Transport Layer**
- **v2.12 Modern Management Plane**

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. netsim provides protocol simulation and routing validation — the "simulate" stage of the pipeline.

**Role:** Validate routing convergence and protocol behavior for topologies generated by [topogen](../topogen) or modeled by [ank-pydantic](../ank-pydantic). Export FIBs and routing state for traffic analysis by [netflowsim](../netflowsim).

**Key integration points:**
- Consumes topology from [topogen](../topogen) (direct netsim YAML export) or [ank-pydantic](../ank-pydantic) (`export_netsim()`)
- FIB/routing matrix export feeds [netflowsim](../netflowsim) for traffic engineering analysis
- Workbench orchestrates simulation via subprocess and gRPC daemon
- BMP telemetry and PCAP capture provide observability

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities
- [Cross-Project Data Contracts](../../topogen/.planning/ARCHITECTURE.md) — ownership boundaries and format specifications

*Last updated: 2026-03-06 after starting v2.2 Advanced Transport milestone*

---

## Current Status

2026-03-08 — Completed 127-04 show mpls-tp lsp/oam CLI commands

---

## Roadmap

- **v1.10 Engine Hardening & Protocol Fidelity** (Proposed) — Phases 111-115
- **v2.3 Multicast** (Proposed)
- **v2.4 Chaos Engineering & Performance** (Proposed)
- **v2.5 Intelligent Simulation & Scale** (Proposed)
- **v2.6 Ecosystem & Digital Twin** (Proposed)
