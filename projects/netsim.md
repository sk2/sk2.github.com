---
layout: default
---

# netsim

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## The Insight

Network simulation usually falls into two traps: it's either too slow (VM-based emulation) or too abstract (mathematical models). **netsim** takes a middle path—deterministic, tick-based protocol simulation. It doesn't emulate the kernel; it simulates the *logic* of OSPF, IS-IS, and BGP. This allows you to validate massive topologies in seconds, ensuring that a configuration change won't cause a routing loop before it ever hits a real router.

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | Rust / Python |
| **Sim Type** | Tick-based, Deterministic |
| **Performance** | 100+ nodes in seconds |

---

## Overview

netsim is a deterministic, tick-based network protocol simulator that validates network configurations before production deployment. It provides protocol-level fidelity with guaranteed reproducibility: same topology always produces same results.

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

## Implemented Protocols

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

## Technical Details

### Determinism

Same input topology + same random seed = same results every time. Critical for regression testing in CI/CD pipelines.

### Performance

Simulates 100+ device topologies in seconds. Efficient event-driven architecture avoids unnecessary computation.

### Python Bindings

Python API available via PyO3 bindings in `crates/netsim-py` for programmatic access and integration with existing Python workflows.

## Examples

Repository includes examples for:
- Simple two-host connectivity
- OSPF triangle with three routers
- IS-IS hierarchical routing (L1/L2)
- MPLS/LDP label distribution
- BFD fast failure detection
- GRE overlay tunnels
- Traffic generation with statistics

## Development Status

Active development with regular protocol additions and improvements.

**Recently Added:**
- BGP support with communities
- Traffic generation and statistics
- IP name aliasing for scripts
- Enhanced JSON output

**Roadmap:**
- IPv6 support
- RSVP-TE for traffic engineering
- Enhanced MPLS L3VPN features
- VLANs and 802.1Q tagging

See `.planning/ROADMAP.md` for full roadmap.

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See `examples/` directory for runnable demos

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- CLI output showing OSPF convergence
- show ip route output example
- Ping/traceroute output
- JSON output sample
- show isis database example
-->
