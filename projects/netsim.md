---
layout: default
section: network-automation
---

# Network Simulator

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Demos](#demos)
- [How It Works](#how-it-works)
- [Protocols](#protocols)
- [Simulation Output](#simulation-output)
- [Usage](#usage)
- [Scale & Performance](#scale--performance)
- [Status](#status)
- [Technical Reports](#technical-reports)

## Concept

Deterministic tick-based network protocol simulator that validates routing configurations before production deployment. It runs OSPF, IS-IS, BGP, MPLS, EVPN, and Segment Routing convergence assertions on candidate designs — same topology, same results, every time.

Unlike packet-level simulators or VM-based emulation (Containerlab, GNS3), this engine focuses on **protocol convergence and state validation**. It mirrors real router behavior (RIB/FIB separation, LSDB synchronization, BGP best-path selection) without emulating the kernel. A 400-device enterprise topology converges in seconds, not minutes.

---

## Demos

### Basic Validation
![Basic validation: OSPF triangle with ping and traceroute](/images/netsim-basic-demo.gif)
*OSPF triangle topology with ping and traceroute verification.*

### Interactive Daemon Mode
![Daemon mode: IOS-like CLI with tab completion](/images/netsim-daemon-demo.gif)
*gRPC daemon with IOS-like CLI, tab completion, and live topology inspection.*

### TUI Dashboard
![TUI: real-time device state and routing tables](/images/netsim-tui-demo.gif)
*Terminal UI showing real-time device state, routing tables, and convergence progress.*

### Enterprise Case Study
![Enterprise: 400+ device three-tier topology](/images/netsim-case-study-enterprise.gif)
*Three-tier enterprise topology with 400+ devices, multi-area OSPF, and BGP.*

### Chaos Testing
![Chaos: link failure injection and reconvergence](/images/netsim-chaos-demo.gif)
*Declarative failure injection with cascading link failures and protocol reconvergence.*

### Self-Healing Network
![Self-healing: automatic rerouting after failure](/images/netsim-self-healing.gif)
*OSPF reconvergence after link failure, demonstrating automatic traffic rerouting.*

### L3VPN Isolation
![L3VPN: VRF isolation verification](/images/netsim-l3vpn-isolation.gif)
*BGP/MPLS L3VPN with VRF isolation — verifying traffic separation between VPNs.*

### Segment Routing
![SR-MPLS: label-switched path steering](/images/netsim-sr-steering.gif)
*SR-MPLS with Node-SID and SRGB, showing label-switched path forwarding.*

### Traceroute Visualization
![Traceroute: hop-by-hop path through network](/images/netsim-trace-demo.gif)
*Hop-by-hop traceroute through a multi-router OSPF domain.*

### Scale Testing
![Scale: 100+ device topology convergence](/images/netsim-scale-demo.gif)
*Parallel tick execution across 100+ devices with convergence timing.*

### Assertions
![Assertions: automated pass/fail verification](/images/netsim-assertion-demo.gif)
*Declarative assertions validating reachability, routing state, and protocol adjacencies.*

---

## Protocols

### Routing
- **OSPF** — adjacencies, LSA flooding (Types 1-5), SPF/Dijkstra, multi-area, DR/BDR, stub areas
- **IS-IS** — L1/L2 hierarchical routing, LSP flooding, wide metrics
- **BGP** — iBGP/eBGP, route reflectors, communities (NO_EXPORT, NO_ADVERTISE), ORIGINATOR_ID loop prevention, MP-BGP IPv6 Unicast
- **OSPFv3** — IPv6 routing with link-local adjacencies
- **BFD** — sub-second failure detection for OSPF and BGP sessions

### MPLS & Tunneling
- **LDP** — automatic label binding and distribution
- **MPLS** — label imposition/swap/pop, LFIB, OAM (LSP Ping/Traceroute)
- **SR-MPLS** — Segment Routing with SRGB, Node-SID, label-switched paths
- **RSVP-TE** — explicit-path traffic engineering tunnels
- **GRE** — Layer 3 overlay with keepalives and recursion checks
- **L3VPN** — BGP/MPLS VPN (RFC 4364) with VRF isolation

### Data Center Fabric
- **VXLAN** — RFC 7348 encap/decap with head-end replication
- **BGP EVPN** — Type-2 (MAC/IP), Type-3 (IMET), Type-5 (IP prefix), ARP suppression
- **EVPN Multi-Homing** — ESI, DF election (service-carving), Type-1/4 routes
- **L2 Bridge Domains** — per-BD FDB, MAC learning, aging, BUM flooding
- **LACP/LAG** — hash-based load distribution with PDU negotiation
- **LLDP** — neighbor discovery with TTL aging
- **IRB** — anycast gateway for inter-subnet routing

### Infrastructure
- **IPv4/IPv6** — dual-stack forwarding, ARP, NDP, ICMPv4/v6
- **Traffic Generation** — CBR, Poisson, burst patterns with gravity-model matrices
- **Failure Injection** — time-based, correlated, cascading failures with dry-run
- **Wire Impairments** — latency, jitter (uniform/Gaussian), pattern-based profiles
- **PCAP Export** — MPLS-aware packet capture
- **BMP** — BGP Monitoring Protocol telemetry
- **NetFlow/IPFIX** — flow export with configurable templates

---

## Simulation Output

After running a topology, verification commands produce structured output.

### Routing Table

```
Router: r1
Destination      Next-Hop       Protocol  Metric  Interface
10.0.0.0/30      directly       connected 0       eth0
10.0.1.0/30      directly       connected 0       eth1
10.0.2.0/30      10.0.0.2       OSPF      20      eth0
192.168.1.0/24   directly       connected 0       lo0
192.168.2.0/24   10.0.0.2       OSPF      11      eth0
192.168.3.0/24   10.0.1.2       OSPF      11      eth1
```

### Ping Verification

```
$ netsim verify ping h1 h2
PING h2 (192.168.2.1) from h1 (192.168.1.1):
  h1 -> r1 (eth0) -> r2 (eth1) -> h2
  RTT: 3 ticks (deterministic)
  Result: SUCCESS
```

### Traceroute

```
$ netsim verify traceroute h1 h3
Traceroute to h3 (192.168.3.1):
  1  r1      (10.0.0.1)    1 tick
  2  r3      (10.0.1.2)    2 ticks
  3  h3      (192.168.3.1) 3 ticks
```

---

## Usage

### Topology Definition (YAML)

```yaml
name: ospf-triangle
devices:
  - name: r1
    type: router
    router_id: 1.1.1.1
    interfaces:
      - name: eth0
        ip: 10.0.0.1/30
        ospf: { area: 0 }
      - name: eth1
        ip: 10.0.1.1/30
        ospf: { area: 0 }

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r1:eth1, r3:eth0]
  - endpoints: [r2:eth1, r3:eth1]

script:
  - at: converged
    device: r1
    command: show ip route
```

### CLI

```bash
# Run simulation
netsim run topology.yaml

# Validate syntax without running
netsim validate topology.yaml

# Interactive daemon mode
netsim daemon topology.yaml
```

### Python API

```python
import netsim_py

engine = netsim_py.Engine()
engine.load_topology("topology.yaml")
engine.run_until_converged()
engine.execute_command("r1", "show ip route")
```

---

## How It Works

The simulator advances in discrete **ticks** (~1ms simulated time). Every device processes its input queue in lockstep — all routers run SPF, all BGP speakers evaluate best paths, all links deliver buffered packets — then the tick completes. This lockstep model guarantees deterministic results: same topology, same sequence of events, same output on every run.

**RIB/FIB separation.** Each router maintains a Routing Information Base (learned routes from OSPF, BGP, static config) and a Forwarding Information Base (the winning route per prefix after admin-distance comparison). This mirrors how production routers work — OSPF routes at AD 110 lose to eBGP at AD 20, and the FIB only installs the winner. Protocol interactions like mutual redistribution or route leaking behave correctly because of this split.

**Convergence detection.** After a topology change (link failure, new route advertisement), the engine monitors every device's FIB. When no FIB entry changes for 5 consecutive ticks, the network is declared converged. Scripts and assertions can gate on this event — `at: converged` in a topology file means "run this command once all routing has stabilized."

**Wires as devices.** Links are not simple adjacency edges. Each link is a simulation participant with its own tick processing: it buffers packets, applies configured latency and jitter (uniform or Gaussian), drops packets according to loss rate, and delivers them at the correct future tick. This means a 10ms link actually delays packets by 10 ticks, and failure injection removes the wire from the simulation graph entirely.

**Parallel execution.** The tick loop runs on Tokio. For topologies above an adaptive threshold (~50 devices), device processing fans out across available cores. Smaller topologies run single-threaded to avoid scheduling overhead. The graph structure uses PetGraph's StableDiGraph, which supports stable node/edge indices across mutations — important for SPF recalculations after link failures.

**Export.** Packet captures (PCAP), BGP Monitoring Protocol (BMP) streams, and NetFlow/IPFIX records export through non-blocking sinks that run alongside the simulation without slowing it down.

---

## Scale & Performance

- **Codebase**: 200,000+ lines of Rust across 11 shipped milestones (v1.0 through v2.0)
- **Tests**: 2,200+ tests passing, including protocol conformance, convergence, and regression suites
- **Enterprise topology**: a 400-device three-tier network (core/distribution/access with multi-area OSPF and iBGP route reflectors) converges in under 10 seconds on a laptop
- **Tick throughput**: ~50,000 device-ticks per second on an 8-core machine for a mixed OSPF+BGP topology
- **Interfaces**: REST API (axum), gRPC daemon with IOS-like CLI, SSE event stream for live monitoring, Python bindings via PyO3

---

## Status

**Current**: v2.1 Enterprise & Campus Protocols — VRRP gateway redundancy and DHCP relay.

**Recently shipped:**
- v2.0 — IPv6 forwarding, NDP, ICMPv6, OSPFv3, MP-BGP IPv6 Unicast, dual-stack (March 2026)
- v1.8/v1.9 — Data center fabric (VXLAN, EVPN, LACP, LLDP), wire impairments, failure injection (February 2026)
- v1.7 — SR-MPLS, daemon mode with gRPC, IOS-like CLI (February 2026)
- v1.6 — L3VPN, RSVP-TE, BMP telemetry (February 2026)

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/netsim-techreport.pdf)

---

[← Back to Projects](../projects)
