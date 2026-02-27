---
layout: default
section: network-automation
---

# Network Simulator

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Protocols Implemented](#protocols-implemented)
- [Performance](#performance)

## Concept

Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.

Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.

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

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
