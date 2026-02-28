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
- [Performance](#performance)
- [Automation](#automation)
- [Examples](#examples)
- [Development Status](#development-status)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Current Milestone: v1.8 Data Center Fabric & EVPN](#current-milestone-v18-data-center-fabric-evpn)
- [Future Milestones (Proposed)](#future-milestones-proposed)
- [Ecosystem Context](#ecosystem-context)
- [Current Status](#current-status)
- [Roadmap](#roadmap)

## Concept

Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.

Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.

Network simulation usually falls into two traps: it's either too slow (VM-based emulation) or too abstract (mathematical models). **netsim** takes a middle path-deterministic, tick-based protocol simulation. It doesn't emulate the kernel; it simulates the logic of routing protocols. This allows you to validate massive topologies in seconds, ensuring that a configuration change won't cause a routing loop before it ever hits a real router.

netsim is a deterministic, tick-based network protocol simulator that validates network configurations before production deployment. It provides protocol-level fidelity with guaranteed reproducibility: same topology always produces same results.

Network engineers need to validate configurations before deploying to production. Current options:

- **Full emulation** (Containerlab, GNS3, EVE-NG): Runs device images and real network stacks. Slower and more resource-intensive than protocol simulation.
- **Real hardware labs**: Expensive, requires physical space, limited scale.
- **Production testing**: Risky, causes outages when configs have errors.

netsim provides fast, deterministic simulation with protocol-level fidelity. Catch routing loops, unreachable hosts, and misconfigurations before touching production.

---

## Architecture

- **Tick-based execution**: Deterministic, reproducible simulations (~1ms per tick).
- **RIB/FIB separation**: Mirrors real router behavior for high-fidelity state validation.
- **Convergence detection**: Automatically detects network stabilization to minimize simulation time.
- **Scripted commands**: Diagnostics can be executed at specific ticks or immediately after convergence.

---

## Protocols Implemented

- **Routing**: OSPF (point-to-point, Area 0, LSA Types 1/2, Dijkstra SPF), IS-IS (L1/L2 hierarchical, LSP flooding), BGP (iBGP/eBGP, communities, route propagation).
- **MPLS**: LDP label distribution, label push/swap/pop operations, MPLS OAM.
- **Resilience**: BFD (bidirectional forwarding detection, async mode).
- **Tunneling**: GRE encapsulation, VRF isolation (L3VPN foundations).
- **Layer 2/3**: ARP request/reply, ICMP echo (ping), Time Exceeded (traceroute).

---

## Performance

Simulates 100+ device topologies in seconds. Generates structured JSON output for seamless integration into CI/CD pipelines.

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

## Quick Facts

| | |
|---|---|
| **Status** | Active |

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

- BGP support with communities
- Traffic generation and statistics
- IP name aliasing for scripts
- Enhanced JSON output

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

---

## # Out of Scope

- Vendor bug replication — idealized behavior only
- TCP congestion algorithms — not the goal
- GUI/visual topology editor — text-based only
- SCTP transport for IPFIX — UDP sufficient for simulator

---

## Context

**Shipped:** v1.7 SR-MPLS, Daemon Mode & Routing Matrix (2026-02-16)
- ~192,000 lines of Rust
- 56 phases, 235 plans across 7 milestones
- 1,350+ tests passing
- 8 milestones shipped (v1.0 through v1.7)

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

## Current Milestone: v1.8 Data Center Fabric & EVPN

**Goal:** Model data center fabric topologies with VXLAN overlay, BGP EVPN control plane, link aggregation, and L2 forwarding — enabling pre-deployment validation of DC designs with machine-readable output.

**Target features:**
- L2 forwarding model (bridge domains, MAC learning, FDB tables) as foundation for overlay
- LACP/LAG link aggregation with member failure handling and hash-based load distribution
- LLDP neighbor discovery with topology validation
- VXLAN data plane (encap/decap, VTEP endpoints, VNI-to-bridge-domain mapping)
- BGP EVPN control plane (Type 2 MAC/IP, Type 3 inclusive multicast, Type 5 IP prefix)
- EVPN multi-homing with ESI, designated forwarder election, and mass withdrawal
- JSON output for all show commands (machine-readable automation surface)

---

## Future Milestones (Proposed)

- **v1.9 Advanced Impairments & Topology Patterns** — Phases 97-100
- **v1.10 Engine Hardening & Protocol Fidelity** — Phases 111-115
- **v1.11 Advanced Analysis & Assertions** — Phases 116-119
- **v2.0 IPv6 Foundation** — Phases 68-72
- **v2.1 Enterprise & Campus Protocols** — Phases 73-74
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

*Last updated: 2026-02-24 after creating milestone v1.11 and v2.12*

---

## Current Status

2026-02-28 — Completed 71-02 (IPv6 Loc-RIB and FIB installation)

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
