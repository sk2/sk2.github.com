---
layout: default
section: network-automation
---

# Network Analysis Engine

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

Graph Neural Network (GNN) based network analytics module that extends topology analysis with real-time learning and prediction. Subscribes to the Network Topology Engine's WebSocket stream for live topology updates, runs GNN models on graph data, and exposes analytics through multiple interfaces (WebSocket streaming, REST API, Rust library, event queue).

Built on an existing Rust+Python analysis toolkit that includes formal verification (Z3 SMT solver), graph algorithms (centrality, community detection, cascade modeling), and Python bindings via PyO3.

---

## Capabilities

**Existing (shipped):**
- Formal verification of network properties via Z3 SMT solver
- Graph algorithms: centrality, community detection, cascade modeling
- Python bindings via PyO3 for ML/analysis integration
- CLI for topology operations
- Rust-based graph operations with petgraph

**In progress (v1):**
- GNN-based anomaly detection on network topology
- Traffic prediction from topology patterns
- Topology learning and pattern recognition
- Configurable alert system (anomaly threshold, topology changes, performance)
- Near real-time processing (1–5s latency target)

---

[← Back to Network Automation](../network-automation)
