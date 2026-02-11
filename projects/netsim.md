---
layout: default
---

# netsim

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---


## The Insight

Network simulation typically involves a trade-off between the resource intensity of VM-based emulation and the abstraction of mathematical models. **netsim** implements deterministic, tick-based protocol simulation. It simulates the logic of OSPF, IS-IS, and BGP rather than emulating the kernel, allowing for high-fidelity validation of large topologies in seconds.

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | N/A |
| **Started** | 2025 |

---

## What This Is

A deterministic, tick-based network protocol simulator for validating configurations. It provides protocol-level fidelity with guaranteed reproducibility, allowing engineers to detect routing loops and reachability issues before deployment.

## Problem It Solves

Network engineers need to validate configurations before deploying to production. Current options:
- **Full emulation** (GNS3, EVE-NG): Runs actual device images. Slow, resource-intensive, requires licensing.
- **Real hardware labs**: Expensive, requires physical space, limited scale.
- **Production testing**: Risky, causes outages when configs have errors.

netsim provides fast, deterministic simulation with protocol-level fidelity. Catch routing loops, unreachable hosts, and misconfigurations before touching production.

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

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
