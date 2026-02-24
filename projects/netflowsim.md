---
layout: default
section: network-automation
---

# Network Performance Simulator

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Concept

### Core Value

`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds, identify bottlenecks probabilistically, and test network resilience under failure scenarios.

---

## Use Cases

- **Topology Validation**: Test network designs before deployment
- **Routing Strategy Comparison**: Evaluate different routing algorithms
- **Capacity Planning**: Identify congestion points under load
- **What-If Analysis**: Model link failures and capacity changes
- **Integration Testing**: Validate packet simulator routing logic

---

## Tech Stack

- **Language**: Rust
- **Graph Library**: Petgraph
- **Parallelism**: Rayon (multi-core processing)
- **Serialization**: Serde (JSON), GeoJSON
- **Visualization**: Martin (Tileserver), MVT (Mapbox Vector Tiles)

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)
