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
- [Architecture](#architecture)
- [Protocols Implemented](#protocols-implemented)
- [Automation](#automation)
- [Usage](#usage)
- [Development Status](#development-status)
- [Roadmap](#roadmap)
- [Current Status](#current-status)
- [Roadmap](#roadmap)

## Concept

Network simulation usually falls into two traps: it's either too slow (VM-based emulation) or too abstract (mathematical models). **netsim** takes a middle path-deterministic, tick-based protocol simulation. It doesn't emulate the kernel; it simulates the logic of routing protocols. This allows you to validate massive topologies in seconds, ensuring that a configuration change won't cause a routing loop before it ever hits a real router.

netsim is a deterministic, tick-based network protocol simulator that validates network configurations before production deployment. It provides protocol-level fidelity with guaranteed reproducibility: same topology always produces same results.

Network engineers need to validate configurations before deploying to production. Current options:

- **Full emulation** (Containerlab, GNS3, EVE-NG): Runs device images and real network stacks. Slower and more resource-intensive than protocol simulation.
- **Real hardware labs**: Expensive, requires physical space, limited scale.
- **Production testing**: Risky, causes outages when configs have errors.

netsim provides fast, deterministic simulation with protocol-level fidelity. Catch routing loops, unreachable hosts, and misconfigurations before touching production.

---

## Architecture

### Tick-Based Execution

Simulation advances in discrete time units ("ticks", ~1ms simulated time). All devices process packets in lockstep for determinism.

### RIB/FIB Separation

Mirrors real router behavior:

- **RIB** (Routing Information Base): Holds all learned routes from protocols
- **FIB** (Forwarding Information Base): Holds active best paths used for forwarding

### Convergence Detection

Automatically detects when network stabilizes (no routing changes for N ticks). Scripts can trigger commands "at: converged" or "converged + 100" ticks.

### Wires as Devices

Links are first-class simulation participants, enabling future latency/loss modeling without architectural changes.

---

## Protocols Implemented

### Routing Protocols

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

### MPLS & Tunneling

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

### Resilience

**BFD (Bidirectional Forwarding Detection):**

- Subsecond failure detection
- Async mode with configurable timers
- Integration with OSPF for fast convergence

### Layer 2/3

**ARP:** Request/reply with proper cache management
**ICMP:** Echo (ping), Time Exceeded (traceroute), Destination Unreachable
**IPv4:** Forwarding, TTL handling, fragmentation not supported

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

## Usage

### YAML Topology Definition

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

### CLI Usage

```bash
# Run simulation
netsim run examples/ospf-triangle.yaml

# JSON output for CI/CD
netsim run topology.yaml -f json -o results.json

# Set tick limit for long simulations
netsim run large-topology.yaml --max-ticks 50000
```

### Available Commands

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

### Output Formats

**ASCII:** Human-readable tables (default)
**JSON:** Machine-parseable for scripting and CI/CD

---

## Development Status

Active development with regular protocol additions and improvements.

**Recently Added:**

- BGP support with communities
- Traffic generation and statistics
- IP name aliasing for scripts
- Enhanced JSON output

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

### Validated

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

### Out of Scope

- Vendor bug replication — idealized behavior only
- TCP congestion algorithms — not the goal
- GUI/visual topology editor — text-based only
- SCTP transport for IPFIX — UDP sufficient for simulator

---

## Current Status

2026-02-25 — Completed 67-04-PLAN.md

---

## Roadmap

- **v1.9 Advanced Impairments & Topology Patterns** (Proposed) — Phases 97-100
- **v1.10 Engine Hardening & Protocol Fidelity** (Proposed) — Phases 111-115
- **v1.11 Advanced Analysis & Assertions** (Proposed) — Phases 116-119
- **v2.0 IPv6 Foundation** (Proposed) — Phases 68-72
- **v2.1 Enterprise & Campus Protocols** (Proposed) — Phases 73-74

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
