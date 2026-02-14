---
layout: default
---

# Network Simulator

<span class="status-badge status-active">Active Development — v1.7 Segment Routing</span>

[← Back to Projects](../projects)

---

## The Insight

Developing agentic AI systems and network automation tools requires rapid iteration. Spinning up containers for every test cycle takes minutes; simulation takes seconds. This simulator enables fast prototyping of network automation agents, DevOps pipelines, and AI-driven network operations — validate configurations and agent logic in simulation before committing to heavyweight container deployments.

## Quick Facts

| | |
|---|---|
| **Status** | Active Development — v1.7 Segment Routing |
| **Language** | Rust |
| **Lines of Code** | 126,000+ |
| **Test Coverage** | 1,350+ protocol behavior tests |
| **Started** | 2026 |

---

## Why netsim?

- **Validate before deploying** — Catch routing loops, black holes, and misconfigurations in simulation
- **Deterministic execution** — Same topology, same results, every time
- **Protocol fidelity** — Real OSPF/IS-IS SPF calculations, MPLS label operations, BFD failure detection
- **Advanced features** — MPLS/LDP, SR-MPLS, RSVP-TE, GRE tunnels, L3VPN with VRFs, BFD, BMP telemetry
- **Daemon mode** — Run simulations as background services, attach interactive consoles with tab completion
- **Scriptable** — JSON output for CI/CD integration and automated testing
- **Fast** — Simulate 100+ device topologies in seconds

## Quick Start — Three-Router OSPF Example

Create `ospf-triangle.yaml`:

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
      - name: eth2
        ip: 10.0.3.1/24

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

Run the simulation:

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

**What just happened:**
1. Topology loaded — 3 routers, 2 hosts, 5 links
2. OSPF converged — Routers exchanged LSAs, computed SPF
3. Routes installed — FIBs populated with best paths
4. Commands executed — `show ip route`, `ping` ran at scripted times
5. Results output — ASCII tables showing routing tables and ping responses

---

## Daemon Mode — Real-Time Network Interaction

Run simulations as background daemons and interact with them in real-time — like `docker exec` for network simulations.

### Starting a Daemon

```bash
# Start a simulation as a background daemon
netsim daemon start my-network topology.yaml

# With custom tick rate (default: 100ms)
netsim daemon start my-network topology.yaml --tick-interval 50ms
```

The daemon runs continuously in the background, ticking the simulation at the specified interval.

### Execute One-Shot Commands

```bash
# Run a single command on a device
netsim exec my-network r1 "show ip route"
netsim exec my-network h1 "ping 10.0.3.10"
netsim exec my-network r2 "show ospf neighbors"
```

### Attach an Interactive Console

```bash
# Attach to a device for an interactive session
netsim attach my-network r1
```

Once attached, you get an interactive REPL with **Cisco IOS-style command abbreviation** and **tab completion**:

```
r1> sh ip ro
Destination       Next Hop        Metric  Interface
10.0.1.0/24       —               0       eth2 (connected)
10.0.12.0/24      —               0       eth0 (connected)
10.0.13.0/24      —               0       eth1 (connected)
10.0.3.0/24       10.0.13.3       11      eth1 (OSPF)
10.0.23.0/24      10.0.12.2       20      eth0 (OSPF)

r1> show interfaces
Interface  IP Address      MAC Address        Admin   Status
eth0       10.0.12.1/24    02:00:00:00:01:00  up      up
eth1       10.0.13.1/24    02:00:00:00:01:01  up      up
eth2       10.0.1.1/24     02:00:00:00:01:02  up      up

r1> ping 10.0.3.10
Ping 10.0.3.10: 5/5 packets received, 0% loss

r1> show ip route --json
[{"destination":"10.0.1.0/24","next_hop":"—","metric":0, ...}]

r1> int shut eth0
Interface eth0 admin-down
[OSPF adjacency r1<->r2 torn down]

r1> int no shut eth0
Interface eth0 admin-up
[OSPF adjacency r1<->r2 re-establishing...]

r1> exit
```

**Console Features:**
- **Abbreviated commands** — Cisco IOS-style prefix matching (`sh ip ro` → `show ip route`)
- **Tab completion** — Commands and subcommands
- **Interface management** — `interface shutdown/no shutdown` with protocol teardown
- **JSON output** — Append `--json` to any show command for structured output
- **Command history** — Arrow keys navigate previous commands

### TUI Selector

Running `netsim daemon` with no subcommand launches an interactive TUI that lets you browse running daemons, select devices, and attach — all without memorizing names.

### Daemon Management

```bash
# List all running daemons
netsim daemon list

# Check daemon status
netsim daemon status my-network

# Stop a daemon
netsim daemon stop my-network

# Clean up stale PID files from crashed daemons
netsim daemon list --clean
```

### Why Use Daemon Mode?

- **Agentic AI development**: Test automation agents against live network state without container overhead — agents can execute commands, parse responses, and iterate in seconds rather than minutes
- **Network automation prototyping**: Rapidly develop and test configuration management tools, DevOps scripts, and automated network operations
- **Fast iteration loop**: Design → Generate configs → Simulate → Iterate, all without spinning up containers until you're ready to deploy
- **CI/CD integration**: Start daemon, run automated tests via `exec`, collect JSON results, stop daemon
- **Development workflow**: Keep a topology running while you experiment with agent logic or automation scripts
- **Structured logging**: Daemon events logged to `~/.netsim/<name>/daemon.log` for debugging

---

## Protocol Support

### Layer 2

| Protocol | Status | Notes |
|----------|--------|-------|
| Ethernet | ✓ | MAC addressing, frame encapsulation |
| ARP | ✓ | Request/reply, cache management |

### Layer 3

| Protocol | Status | Notes |
|----------|--------|-------|
| IPv4 | ✓ | Forwarding, TTL decrement, fragmentation not supported |
| ICMP | ✓ | Echo (ping), Time Exceeded (traceroute), Destination Unreachable |

### Routing Protocols

| Protocol | Status | Notes |
|----------|--------|-------|
| Static | ✓ | Host default gateway |
| OSPF | ✓ | Point-to-point, Area 0, LSA Types 1 & 2, SPF via Dijkstra |
| IS-IS | ✓ | L1/L2 hierarchical routing, LSP flooding, SPF via Dijkstra |
| BGP | ✓ | iBGP/eBGP, communities, route reflectors, MP-BGP VPNv4 |

### MPLS & Tunneling

| Protocol | Status | Notes |
|----------|--------|-------|
| MPLS | ✓ | Label imposition/swap/pop/pop-continue, LFIB, multi-label stacks |
| LDP | ✓ | Label distribution, targeted sessions |
| SR-MPLS | ✓ | Segment Routing with SRGB, Node-SIDs, SR-owned LFIB precedence |
| RSVP-TE | ✓ | Explicit-path tunnels, deterministic refresh, convergence gating |
| GRE | ✓ | Generic routing encapsulation, overlay tunnels |
| VRF | ✓ | Virtual routing and forwarding, L3VPN with RD/RT |

### Resilience & Telemetry

| Protocol | Status | Notes |
|----------|--------|-------|
| BFD | ✓ | Bidirectional forwarding detection, async mode |
| BMP | ✓ | RFC 7854 BGP Monitoring Protocol, post-decision export |
| PCAP | ✓ | Packet capture with MPLS-aware filtering, Wireshark compatible |

### Available Commands

All commands support abbreviation (e.g., `sh ip ro`) and `--json` output:

- **Show commands**: `show ip route`, `show interfaces`, `show arp`, `show ospf neighbors`, `show isis database`, `show isis neighbors`, `show bgp neighbors`, `show bgp vpn`, `show mpls forwarding`, `show ldp bindings`, `show bfd sessions`, `show vrf`, `show sr`, `show traffic`
- **Diagnostics**: `ping <ip>`, `traceroute <ip>`
- **Configuration**: `route add <dest> via <nexthop>`, `interface shutdown <name>`, `interface no shutdown <name>`

---

## Example: IS-IS L1/L2 Hierarchy with Real Output

Service provider topology demonstrating IS-IS hierarchical routing:

```yaml
name: isis-hierarchy
description: IS-IS L1/L2 hierarchy with inter-area routing

devices:
  - name: r1
    type: router
    isis:
      net: "49.0001.0000.0000.0001.00"
      level: l1
    interfaces:
      - name: eth0
        ip: 10.1.0.1/24
        isis: { metric: 10 }
      - name: lo
        ip: 192.0.2.1/32
        isis: {}

  - name: r2
    type: router
    isis:
      net: "49.0001.0000.0000.0002.00"
      level: l1l2  # Area border router
    interfaces:
      - name: eth0
        ip: 10.1.0.2/24
        isis: { metric: 10 }
      - name: eth1
        ip: 10.0.0.2/24
        isis: { metric: 10 }
      - name: lo
        ip: 192.0.2.2/32
        isis: {}

  - name: r3
    type: router
    isis:
      net: "49.0002.0000.0000.0003.00"
      level: l2
    interfaces:
      - name: eth0
        ip: 10.0.0.3/24
        isis: { metric: 10 }
      - name: lo
        ip: 192.0.2.3/32
        isis: {}

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r2:eth1, r3:eth0]

script:
  - at: converged
    device: r2
    command: show isis neighbors
  - at: converged
    device: r2
    command: show isis database
  - at: converged
    device: r1
    command: show ip route
```

**Simulation Output:**

```bash
$ netsim run isis-hierarchy.yaml

[t=0ms] Network initialized: 3 devices, 2 links
[t=0ms] IS-IS: r1, r2, r3 sending IIH (IS-IS Hello)
[t=3ms] IS-IS: Adjacencies forming
[t=5ms] IS-IS: r1<->r2 L1 adjacency Up
[t=5ms] IS-IS: r2<->r3 L2 adjacency Up
[t=8ms] IS-IS: LSP flooding in progress
[t=12ms] IS-IS: SPF calculation complete (L1 and L2)
[t=12ms] Network converged

[t=12ms] r2> show isis neighbors
System ID       Interface  State  Level  Holdtime
0000.0000.0001  eth0       Up     L1     24s
0000.0000.0003  eth1       Up     L2     24s

[t=12ms] r2> show isis database
IS-IS Level-1 Link State Database:
LSPID                 LSP Seq Num  Checksum  Lifetime  Attributes
0000.0000.0001.00-00  0x00000003   0x4a2e    864       L1
0000.0000.0002.00-00  0x00000003   0x5c1a    864       L1L2

IS-IS Level-2 Link State Database:
LSPID                 LSP Seq Num  Checksum  Lifetime  Attributes
0000.0000.0002.00-00  0x00000003   0x7f3c    864       L1L2
0000.0000.0003.00-00  0x00000003   0x9a2b    864       L2

[t=12ms] r1> show ip route
Codes: C - connected, i L1 - IS-IS level-1, i L2 - IS-IS level-2

C    10.1.0.0/24 is directly connected, eth0
C    192.0.2.1/32 is directly connected, lo
i L1 192.0.2.2/32 [115/10] via 10.1.0.2, eth0
i L2 192.0.2.3/32 [115/20] via 10.1.0.2, eth0
     (route leaked from L2 to L1 by ABR r2)

Simulation complete: 15ms simulated, 0.008s real time
IS-IS events: 18 hellos, 4 LSPs, 2 SPF runs
```

---

## Use Cases

- **Agentic AI & Network Automation Development**: Rapidly prototype and test automation agents, DevOps pipelines, and AI-driven network operations with seconds-long iteration cycles instead of minutes spinning up containers
- **Configuration Generation Testing**: Validate ank_pydantic-generated configs in simulation before deploying to Containerlab — catch errors in the generation logic early
- **Network Automation Prototyping**: Develop configuration management tools, automated provisioning systems, and orchestration scripts against realistic network topologies without infrastructure overhead
- **Pre-deployment Validation**: Catch routing loops, black holes, and misconfigurations before production
- **Convergence Analysis**: Measure failover time and validate backup paths
- **Training**: Safe environment for learning routing protocol behavior and automation development

---

## Current Status

**v1.7 Segment Routing** (In Progress) — Phases 46-51
- SR-MPLS programming with SRGB and Node-SID model
- RSVP-TE explicit-path tunnels
- Multi-label stack forwarding

**v1.6 L3VPN & Interactive Console** (Shipped)
- L3VPN with VRFs, RD/RT, MP-BGP VPNv4
- Daemon mode with interactive console
- Tab completion, command abbreviation, interface management
- 126,000+ lines of Rust, 1,350+ tests

**Roadmap:**
- v1.8 Data Center Fabric & EVPN (Proposed)
- v1.9 Chaos Engineering & Performance (Proposed)

## Tech Stack

Rust, Tokio for async execution, petgraph for topology representation, gRPC for daemon IPC, ratatui for TUI

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
