---
layout: default
section: network-automation
---

# Performance Simulator

<span class="status-badge status-active">Recently Updated</span>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Use Cases](#use-cases)
- [Technical Depth](#technical-depth)
- [Tech Stack](#tech-stack)
- [Current Status](#current-status)

## Concept

A performance analysis engine that utilizes analytic queuing models and Monte Carlo simulations to validate network capacity at scale. Unlike packet-level simulators, netflowsim focuses on probabilistic outcomes across billions of traffic flows.

`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds, identify bottlenecks probabilistically, and test network resilience under failure scenarios.

---

## Use Cases

- **Capacity Planning**: Identify bottleneck links and compute-bound nodes before traffic growth impacts production.
- **Resilience Testing**: Probabilistically analyze the impact of link or node failures on overall network throughput and latency.
- **Routing Strategy Validation**: Compare the performance of different traffic engineering strategies (e.g., ECMP vs RSVP-TE) against realistic demand matrices.

---

## Technical Depth

The engine uses M/M/1 and M/D/1 queuing models implemented in a highly parallelized Rust execution environment. It leverages the Rayon crate to distribute Monte Carlo iterations across all available CPU cores, enabling the analysis of massive traffic scenarios in seconds.

---

## Tech Stack

- **Language:** Rust
- **Graph Library:** Petgraph
- **Parallelism:** Rayon
- **Serialization:** Serde (JSON), GraphML
- **Visualization:** Martin (Tileserver), MVT (Mapbox Vector Tiles)

---

## Current Status

2026-02-24 — Completed 10-02 time-series integration into simulation loops

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)
