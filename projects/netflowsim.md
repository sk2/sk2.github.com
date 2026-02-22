---
layout: default
section: network-automation
---

# netflowsim

<span class="status-badge status-active">Phase 9/13 (0%)</span>

[← Back to Network Automation](../network-automation)

---


## Concept

`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 9/13 (0%) |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

Flow-based network simulator that uses analytic queuing models and Monte Carlo simulations for rapid topology and routing validation at massive scale.

## Why Flow-Based Simulation

Traditional approaches force a choice between:
- **Packet-level simulation** (high fidelity, slow, small scale)
- **Algorithmic analysis** (fast, limited accuracy)

`netflowsim` bridges this gap by modeling flows through queuing theory, achieving:
- **Speed**: 1M+ flows/second on multi-core hardware
- **Scale**: 10k+ node topologies
- **Accuracy**: Validated against theoretical benchmarks

## Key Features

### Phase 1: Foundation (✅ Complete)
- **Engine**: Rust + `petgraph` for graph operations
- **Parallel Processing**: `rayon` for multi-core utilization
- **Queuing Models**:
  - M/M/1 (Markov arrivals, Markov service)
  - M/D/1 (Markov arrivals, Deterministic service)
  - M/G/1 (Markov arrivals, General service)
- **Monte Carlo Simulation**: Billions of flow iterations in seconds
- **GeoJSON Export**: Congestion hotspot visualization
- **Statistics**: Mean latency, link utilization, throughput

### Phase 2: Routing & Path Tracing (✅ Complete)
- **Path Tracing Engine**: Calculate end-to-end paths from FIB data
- **Routing Matrix Generation**: Convert FIB tables to flow routing decisions
- **ECMP Support**: Equal-cost multi-path with recursive resolution
- **Cycle Detection**: Per-path loop detection for safe path exploration
- **FIB Ingestion**: Import forwarding tables from external sources
- **Interface-to-Link Mapping**: Automatic correlation of FIB interfaces with topology edges

### Phase 3: Simulator Interop (🔄 In Progress)
- Topology ingestion from `topogener`
- Bi-directional integration with packet-level network simulator
- Routing matrix exchange format

### Phase 4: Advanced Analysis (Planned)
- CDF plots for latency and throughput distributions
- Automated bottleneck identification
- Performance regression detection

### Phase 5: Dynamic Networks (Planned)
- Runtime topology changes (link failures, node additions)
- Dynamic routing matrix re-evaluation
- Failure scenario modeling

## Example Usage

```bash
# netflowsim
$ netflowsim simulate \
    --topology topology.json \
    --traffic traffic.json \
    --routing routing.json \
    --output results.json

Loaded topology: 128 nodes, 256 links
Loaded traffic: 10000 flows
Running Monte Carlo simulation (1M iterations)...
Completed in 1.2s

Results written to results.json
GeoJSON visualization: network.geojson
```

```bash
# netflowsim
$ netflowsim generate-routing \
    --topology topology.json \
    --fibs examples/fibs/ \
    --output routing.json

Loaded topology: 128 nodes
Ingested FIBs for 128 routers
Traced 16384 source-destination pairs
ECMP paths found: 2841
Routing matrix written to routing.json
```

## Performance Metrics

- **Throughput**: 1M+ flows/second (baseline)
- **Scale**: Tested with 10k+ node topologies
- **Latency**: Sub-second results for typical network sizes
- **Accuracy**: Validated against M/M/1 and M/D/1 theoretical values

## Tech Stack

- **Language**: Rust
- **Graph Library**: Petgraph
- **Parallelism**: Rayon (multi-core processing)
- **Serialization**: Serde (JSON), GeoJSON
- **Visualization**: Martin (Tileserver), MVT (Mapbox Vector Tiles)

## Use Cases

- **Topology Validation**: Test network designs before deployment
- **Routing Strategy Comparison**: Evaluate different routing algorithms
- **Capacity Planning**: Identify congestion points under load
- **What-If Analysis**: Model link failures and capacity changes
- **Integration Testing**: Validate packet simulator routing logic

---

[← Back to Network Automation](../network-automation)
