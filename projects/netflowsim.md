---
layout: default
section: network-automation
---

# Performance Simulator

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds, identify bottlenecks probabilistically, and test network resilience under failure scenarios.

---

## Tech Stack

- **Language:** Rust
- **Graph Library:** Petgraph
- **Parallelism:** Rayon
- **Serialization:** Serde (JSON), GraphML
- **Visualization:** Martin (Tileserver), MVT (Mapbox Vector Tiles)

---

## Current Status

2026-02-23 — Completed 09-07 simulation throughput optimization

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
