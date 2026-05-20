---
layout: default
section: network-automation
description: "Orchestration engine for coordinating device interactions across real and testbed networks."
sitemap: false
hand_written: true
---

# Project Reference

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Architecture](#architecture)
- [Features](#features)

## Concept

Orchestration engine for coordinating device interactions across real and testbed networks. Executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots). Uses [Device Interaction Framework](../deviceinteraction) as a library for transports, parsing, and test primitives — the orchestrator owns run coordination, persistence, and event streaming.

Inspired by Tower/AWX-style job execution, but purpose-built for reliable, replayable device runs with clean integration boundaries.

---

## Code Samples

### ospf_triangle.yaml

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
        ospf: { area: 0, cost: 1 }

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
      - name: eth2
        ip: 10.0.2.1/24
        ospf: { area: 0, cost: 1 }

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
        ospf: { area: 0, cost: 1 }

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

  - at: converged + 200
    device: h1
    command: traceroute 10.0.3.10

```

### scrape_topology.yaml

```yaml
namespace: reference
name: scrape_topology
dsl_version: v1
steps:
  - step_id: get_version
    adapter: [deviceinteraction](../deviceinteraction)
    inputs:
      command: show version
    depends_on: []
  - step_id: get_interfaces
    adapter: [deviceinteraction](../deviceinteraction)
    inputs:
      command: show interfaces
    depends_on: []
  - step_id: get_neighbors
    adapter: [deviceinteraction](../deviceinteraction)
    inputs:
      command: show lldp neighbors
    depends_on: []
  - step_id: build_topology
    adapter: topology_builder
    inputs: {}
    depends_on: [get_version, get_interfaces, get_neighbors]

```

### sim_scrape.yaml

```yaml
namespace: reference
name: sim_scrape
dsl_version: v1
steps:
  - step_id: get_version
    adapter: [netsim](../netsim)
    inputs:
      command: show version
    depends_on: []
  - step_id: get_interfaces
    adapter: [netsim](../netsim)
    inputs:
      command: show interfaces
    depends_on: []

```

---

## Architecture

The runner exposes an HTTP API as a headless execution engine. Clients (Network Automation Workbench, CLI, CI pipelines) submit device workflows as declarative YAML. The engine handles:

- **Bounded concurrency**: configurable parallelism across device targets
- **Retry semantics**: exponential backoff with configurable limits
- **Timeouts and cancellation**: per-step and per-run deadlines
- **Durable artifacts**: structured logs, command outputs, and device snapshots persisted per run

---

## Features

- API-first design — multiple clients share the same execution engine
- Declarative YAML workflow definitions
- Structured event streaming for real-time run monitoring
- Integration with the broader network automation ecosystem

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Python |
