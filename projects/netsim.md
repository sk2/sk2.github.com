---
layout: default
section: network-automation
---

# Network Simulator

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [Usage](#usage)
- [Architecture](#architecture)
- [Protocols](#protocols)
- [Roadmap](#roadmap)
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

## Concept

Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.

Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.

---

## Code Samples

### OSPF triangle with failure injection

```yaml
name: ospf-triangle
description: Three OSPF routers with failure recovery

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

links:
  - endpoints: [r1:eth0, r2:eth0]
  - endpoints: [r1:eth1, r3:eth0]
  - endpoints: [r2:eth1, r3:eth1]

script:
  - at: converged
    device: r1
    command: show ip route
  - at: converged + 100
    device: r1
    command: interface shutdown eth0
  - at: converged + 500
    device: r1
    command: show ip route
```

### Assertion-based validation

```yaml
name: assertion-failure-demo
description: Catch misconfigurations with assertions

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
        # No OSPF configured — assertion will fail

links:
  - endpoints: ["r1:eth0", "r2:eth0"]

assertions:
  - type: ospf_neighbor_state
    router: r1
    interface: eth0
    expected_state: Full
```

---

## Visuals

### Basic Validation
![Simulator Demo](/images/netsim-basic-demo.gif)

### Interactive Daemon Mode
![Daemon Demo](/images/netsim-daemon-demo.gif)

### Enterprise Case Study
![Enterprise Case Study](/images/netsim-case-study-enterprise.gif)

### TUI Interface
![TUI Demo](/images/netsim-tui-demo.gif)

### Chaos Engineering
![Chaos Demo](/images/netsim-chaos-demo.gif)

### Self-Healing Network
![Self-Healing Demo](/images/netsim-self-healing-demo.gif)

### L3VPN Service Provider
![L3VPN Demo](/images/netsim-l3vpn-demo.gif)

### Segment Routing MPLS
![SR Demo](/images/netsim-sr-demo.gif)

### Path Tracing
![Trace Demo](/images/netsim-trace-demo.gif)

### Scale Test
![Scale Demo](/images/netsim-scale-demo.gif)

### Assertion Framework
![Assertion Demo](/images/netsim-assertion-demo.gif)

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

## Protocols

**Routing:** OSPF (Areas, DR/BDR, SPF), IS-IS (L1/L2 hierarchy), BGP (iBGP, eBGP, communities, route reflection), OSPFv3 (IPv6)

**MPLS & Tunneling:** LDP, MPLS forwarding, L3VPN (VRFs), SR-MPLS (Node-SID, SRGB), GRE, VXLAN

**Data Center:** BGP EVPN (Type-2/3/5), L2 bridge domains, LACP/LAG, LLDP, IRB with anycast gateway

**Resilience:** BFD (sub-second failover), VRRPv2/v3, DHCP relay with Option 82

**Layer 2/3:** ARP, NDP, IPv4, IPv6, ICMP, ICMPv6

**Analysis:** Declarative assertions, topology diff, path tracing, capacity modeling

---

## Roadmap

- **v2.2 Advanced Transport** — SRv6, MPLS-TP, TWAMP
- **v2.3 Multicast** — IGMP/MLD, PIM-SM
- **v2.4 Chaos Engineering & Performance**
- **v2.5 Intelligent Simulation & Scale**

---

## Current Status

v2.2 Advanced Transport in progress. Previous: v2.1 Enterprise & Campus (2026-03-04) + v1.11 Advanced Analysis (2026-03-06).

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/netsim-techreport.pdf)

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
