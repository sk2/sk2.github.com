---
layout: default
---

# network-simulator

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | Rust, Python bindings (PyO3) |
| **Started** | 2025 |

---

## The Insight

Validate network configurations at scale with protocol-level fidelity before deploying to real infrastructure.

## What This Is

A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab)—larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation. Use for smoke testing and design validation of network configurations.

## Protocols Implemented

- **Routing:** OSPF (point-to-point, Area 0, LSA Types 1/2, Dijkstra SPF), IS-IS (L1/L2 hierarchical, LSP flooding), BGP (iBGP/eBGP, communities, route propagation)
- **MPLS:** LDP label distribution, label push/swap/pop operations, MPLS OAM
- **Resilience:** BFD (bidirectional forwarding detection, async mode)
- **Tunneling:** GRE encapsulation, VRF isolation (L3VPN foundations)
- **Layer 2/3:** ARP request/reply, ICMP echo (ping), Time Exceeded (traceroute)

## Architecture

- **Tick-based execution:** Deterministic, reproducible simulations (~1ms per tick).
- **RIB/FIB separation:** Mirrors real router behavior.
- **Convergence detection:** Automatically detects network stabilization.
- **Scripted commands:** Diagnostics at specific ticks or after convergence.

## Performance

Simulates 100+ device topologies in seconds. JSON output for CI/CD integration.

## Current Status

v1.5 shipped. Planning v1.6.
**Future Roadmap Ideas:** See [.planning/FUTURE_IDEAS.md](FUTURE_IDEAS.md) for long-term innovation and technical debt backlog.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)