---
layout: default
section: network-automation
---

# Performance Simulator

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A performance analysis engine that utilizes analytic queuing models and Monte Carlo simulations to validate network capacity at scale. Unlike packet-level simulators, netflowsim focuses on probabilistic outcomes across billions of traffic flows.

---

## Use Cases

- **Capacity Planning**: Identify bottleneck links and compute-bound nodes before traffic growth impacts production.
- **Resilience Testing**: Probabilistically analyze the impact of link or node failures on overall network throughput and latency.
- **Routing Strategy Validation**: Compare the performance of different traffic engineering strategies (e.g., ECMP vs RSVP-TE) against realistic demand matrices.

---

## Technical Depth

The engine uses M/M/1 and M/D/1 queuing models implemented in a highly parallelized Rust execution environment. It leverages the Rayon crate to distribute Monte Carlo iterations across all available CPU cores, enabling the analysis of massive traffic scenarios in seconds.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
