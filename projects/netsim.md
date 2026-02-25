---
layout: default
section: network-automation
---

# Network Simulator

<span class="status-badge status-active">Phase 05/05 (100%)</span>

[← Back to Network Automation](../network-automation)

---

## Concept

Network simulation typically involves a trade-off between the resource intensity of VM-based emulation and the abstraction of mathematical models. The **Network Simulator** implements deterministic, tick-based protocol simulation. It simulates the logic of OSPF, IS-IS, and BGP rather than emulating the kernel, allowing for high-fidelity validation of large topologies in seconds.

## Quick Facts

| | |
|---|---|
| **Status** | v1.6 shipped, v1.7 in planning |
| **Language** | Rust |
| **Lines of Code** | ~126,000 |
| **Test Coverage** | 1,350+ tests |
| **Requirements Met** | 122 (35 MVP + 87 advanced) |
| **Started** | 2026 |

---

## What This Is

A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation. Used for smoke testing and design validation of network configurations.

## Problem It Solves

Network engineers need to validate configurations before deploying to production. Current options:
- **Full emulation** (GNS3, EVE-NG): Runs actual device images. Slow, resource-intensive, requires licensing.
- **Real hardware labs**: Expensive, requires physical space, limited scale.
- **Production testing**: Risky, causes outages when configs have errors.

The Network Simulator provides fast, deterministic simulation with protocol-level fidelity. Catch routing loops, unreachable hosts, and misconfigurations before touching production.

## Architecture

### Tick-Based Execution

Simulation advances in discrete time units ("ticks", ~1ms simulated time). All devices process packets in lockstep for determinism. Parallel execution via Tokio with adaptive thresholds avoids overhead on small topologies while enabling multi-core utilization for large networks.

### RIB/FIB Separation

Mirrors real router behavior:
- **RIB** (Routing Information Base): Holds all learned routes from protocols
- **FIB** (Forwarding Information Base): Holds active best paths used for forwarding

Admin distance determines route selection when multiple protocols offer routes to the same destination.

### Convergence Detection

Automatically detects when network stabilizes via FIB stability monitoring (no routing changes for N ticks). Scripts can trigger commands "at: converged" or "converged + 100" ticks. Quiescence detection tracks control plane packet activity (OSPF, BGP, ARP) and ignores data plane traffic for precise convergence signaling.

### Wires as Devices

Links are first-class simulation participants with queues and processing logic, enabling future latency/loss modeling without architectural changes. Each wire can inject delay, drop packets probabilistically, or reorder based on jitter models.

### Dynamic Topology Modification

Safe wire and device removal during simulation via deferred removal queue. Removals execute at Phase 0 (before device processing) to avoid mid-tick corruption. Supports graceful shutdown (drain queues) or immediate removal.

## Protocols Implemented

### Data Link & Network Layer
- **Ethernet**: 802.3 framing with 6-byte MAC addresses
- **ARP**: Address resolution with cache, timeout, request/reply
- **IPv4**: Routing, fragmentation, TTL decrement
- **ICMP**: Echo (ping), TTL Exceeded (traceroute), Destination Unreachable

### Interior Gateway Protocols
- **OSPF**: Multi-area support, DR/BDR election on multi-access segments, LSA flooding, SPF calculation via Dijkstra on PetGraph
- **IS-IS**: *(Planned for v1.7)*

### Border Gateway Protocol
- **BGP**: iBGP and eBGP with route reflection, AS-path validation, next-hop resolution
- **BGP Communities**: Standard and extended communities for policy control
- **Planned**: BMP (BGP Monitoring Protocol) telemetry export (v1.6)

### MPLS & Traffic Engineering
- **Planned (v1.6)**: MPLS L3VPN with VRF support (RFC 4364)
- **Planned (v1.6)**: RSVP-TE for explicit-path TE tunnels (RFC 3209)
- **Planned (v1.7)**: Segment Routing MPLS with IGP distribution

## Features

### Traffic Generation
- **CBR** (Constant Bit Rate): Fixed packets per tick
- **Poisson**: Exponentially distributed inter-arrival times with deterministic seeding
- **Burst**: Load testing with controlled packet bursts

Traffic sources respect simulator determinism via SmallRng seeded from device_id.

### Observability & Export

**Packet Capture:**
- Pcap/pcapng export with Wireshark compatibility
- Wall-clock timestamps (microsecond/nanosecond precision)
- Per-interface filtering with glob patterns

**NetFlow v9:**
- 5-tuple flow aggregation (src/dst IP, src/dst port, protocol)
- Tick-based flow timeouts (deterministic, not wall-clock)
- Template and data record generation via netgauze-flow-pkt
- UDP streaming to port 2055

**IPFIX (RFC 7011):**
- Version 10 headers with 90%+ code reuse from NetFlow implementation
- Enterprise IE registration API for custom fields
- Non-blocking I/O via ExportSink trait

**Structured Logging:**
- Tracing-based logging with correlation IDs
- OpenTelemetry export support
- Event streaming via Server-Sent Events (SSE)

### Automation

**Python Bindings (PyO3):**
```python
import netsim_py

engine = netsim_py.Engine()
engine.load_topology("topology.yaml")
engine.run_until_converged()
engine.execute_command("router1", "show ip route")
```

**REST API:**
- Axum-based HTTP server for remote control
- OpenAPI documentation
- Real-time event streaming

**Scheduled Events:**
- Trigger commands at specific ticks
- Convergence-relative scheduling ("converged + 500")
- Programmable hooks for topology changes

## Technical Depth

### Performance Optimizations

**Parallel Execution:**
- Tokio async runtime with spawn_blocking for CPU-bound work
- Adaptive parallelism thresholds (only parallelize large topologies)
- Device-per-tick processing prevents data races

**Packet Ordering:**
- Timestamp-based deterministic ordering during parallel execution
- Avoids complex sub-tick modeling while maintaining reproducibility

**Memory Management:**
- VecDeque ring buffers with MemoryBudget limits
- Latency samples capped at 10k to prevent unbounded growth
- Tick-based flush windows for export sinks

### Testing Strategy

**1,350+ tests covering:**
- Protocol state machines (OSPF adjacency, BGP session establishment)
- Convergence correctness (routing loops, black holes)
- Determinism (identical runs produce identical results)
- Scale (100+ device topologies)
- Export correctness (NetFlow/IPFIX compliance)

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **FIB stability for convergence** | Clean signal without tracking protocol internals |
| **Packet timestamps for ordering** | Solves parallel processing without sub-tick complexity |
| **Wires as first-class devices** | Uniform abstraction, latency/loss hooks ready |
| **BTreeMap for LSDB** | Deterministic iteration order for reproducible SPF |
| **Quiescence window = 5 ticks** | Conservative default ensures real stability |
| **Non-blocking export I/O** | Never stall simulation on export backpressure |
| **FlowTable re-export for IPFIX** | 90%+ code reuse between NetFlow v9 and IPFIX |

## Requirements Validated

**v1.0 MVP (35 requirements):**
- Tick-based execution with deterministic ordering
- Queue-based packet flow between devices
- Convergence detection via FIB stability
- Device trait with interfaces, queues, and counters
- RIB/FIB separation with admin distance selection
- Ethernet framing and IPv4 forwarding
- ARP resolution with cache and request/reply
- ICMP echo, TTL exceeded, destination unreachable
- ping, traceroute, show commands
- OSPF adjacency, LSA flooding, SPF calculation
- Multi-hop routing via LSDB synchronization

**v1.1 Scale & Features (15 requirements):**
- Tokio parallel device processing
- 100+ device topology benchmarks
- YAML/JSON topology file loading
- Structured logging with tracing
- Packet capture export
- Multi-access OSPF with DR/BDR
- Latency/loss modeling hooks
- iBGP and eBGP routing protocol
- Name resolution via centralized registry
- Traffic generation (CBR, Poisson, Burst)

**v1.2 Engine Hardening (14 requirements):**
- Quiescence detection (control plane packet tracking)
- Custom convergence hooks (enter/sustain/exit callbacks)
- Dynamic wire removal with graceful/immediate modes
- Dynamic device removal with cascade cleanup
- Tick Phase 0 integration for safe removal

**v1.3 Automation (11 requirements):**
- Scheduled events at specific simulation ticks
- Python bindings via PyO3 (netsim-py package)
- REST API for remote simulation control
- OpenAPI documentation and SSE real-time events

**v1.4 Observability & Export (47 requirements):**
- Export Infrastructure with SimulationClock, ExportSink trait, MemoryBudget
- Pcap/pcapng file export with Wireshark compatibility
- NetFlow v9 with 5-tuple flow aggregation and UDP streaming
- IPFIX RFC 7011 compliance with enterprise IE registration

## Current Milestone: v1.7 - Segment Routing

Adding SR-MPLS foundations with deterministic label/SID handling and IGP-based distribution:
- SR label stack imposition and processing
- OSPF/IS-IS extensions for SR distribution
- Deterministic SID/label allocation
- Operator show surface for SR state (SRGB/SIDs, policies)
- Integration tests proving SR steering and determinism

## Tech Stack

- **Rust** — Performance critical for large-scale simulation
- **Tokio** — Parallel async runtime
- **PetGraph** — Graph algorithms for SPF/Dijkstra
- **ipnet** — CIDR notation and IP math
- **comfy-table** — CLI table formatting
- **tracing** — Structured logging
- **pcap-file** — Packet capture export
- **netgauze-flow-pkt** — NetFlow/IPFIX encoding
- **axum** — REST API server
- **pyo3** — Python bindings

---

[← Back to Network Automation](../network-automation)
