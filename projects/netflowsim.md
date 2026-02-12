---
layout: default
---

# netflowsim

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Insight

`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds.

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | Rust |
| **Started** | 2026 |

---

## Primary Objectives

1. **Performance:** Utilize Rust and Rayon to maximize multi-core hardware utilization.
2. **Scalability:** Handle massive topologies via Petgraph and efficient data structures.
3. **Decoupling:** Clearly separate the Routing Matrix generation (packet-sim logic) from the Flow Simulation (queuing logic).
4. **Analysis:** Provide accurate analytic modeling of network performance under load.

## Success Criteria

- Simulate 1M+ flows through 10k+ nodes in under 1 second.
- Support standard graph formats (GraphML/JSON).
- Accurate analytic modeling (M/M/1, M/D/1) validated against theoretical benchmarks.
- Real-time visualization of congestion hotspots.

## Tech Stack

- **Language:** Rust
- **Graph Library:** Petgraph
- **Parallelism:** Rayon
- **Serialization:** Serde (JSON), GraphML

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
