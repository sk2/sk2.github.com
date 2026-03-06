---
layout: default
section: network-automation
---

# Network Flow Simulator

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [How It Works](#how-it-works)
- [Key Features](#key-features)
- [Usage](#usage)
- [Scale](#scale)
- [Ecosystem Integration](#ecosystem-integration)
- [Status](#status)
- [Technical Reports](#technical-reports)

## Concept

Network Flow Simulator uses analytic queuing models and Monte Carlo simulation to evaluate network performance without packet-level discrete event simulation. Given a topology and traffic demands, it pushes billions of flow iterations through queuing models in seconds, identifying congestion bottlenecks probabilistically and projecting capacity headroom across carrier-scale networks (100k+ nodes).

The core tradeoff: sacrifice per-packet fidelity for orders-of-magnitude speed improvement. An M/G/1 queuing model with Pollaczek-Khinchine mean value analysis produces utilization, delay, and loss estimates that are analytically exact for the modeled traffic class — and runs in seconds where a packet simulator would take hours.

---

## How It Works

**Flow generation.** Traffic demands are expressed as origin-destination flow matrices. The simulator supports gravity model generation (flow proportional to node capacity) and region-aware traffic with configurable locality bias, where a `locality_factor` between 0.0 and 1.0 controls the fraction of traffic that stays within the same geographic region.

**Path resolution.** Flows are routed through the topology using forwarding tables (FIBs). The path tracer handles ECMP with recursive resolution, loop detection, and interface-to-link mapping via subnet matching. An incremental routing cache avoids recomputation when only parts of the topology change.

**Queuing analysis.** Each link is modeled as a queue. Supported models:

- **M/M/1** — Poisson arrivals, exponential service
- **M/D/1** — Poisson arrivals, deterministic service
- **M/G/1** — Poisson arrivals, general service time distributions (Pareto, LogNormal, Weibull, Exponential, Deterministic) using the Pollaczek-Khinchine formula with automatic CV² calculation

**Monte Carlo iteration.** Traffic volumes are sampled stochastically across iterations, executed in parallel via Rayon. Each iteration produces per-link utilization, delay, and loss. Deterministic seeding (base seed + iteration index) ensures reproducibility even under parallel execution.

**Statistical output.** Results are aggregated into percentile distributions (p50/p90/p95/p99), CDFs with theoretical overlays, and time-series trend plots. Outputs render to PNG and SVG via Plotters.

---

## Key Features

**Bottleneck detection and ranking.** Links exceeding 80% utilization are flagged and ranked. Node-level scoring uses `1 - product(1 - p)` to capture the probability that at least one incident link is congested.

**Correlation analysis.** Time-lagged Pearson correlation identifies causality between link utilization patterns — whether congestion on one link predicts congestion on another. Adaptive max-lag (2x median interval) prevents false positives.

**Capacity planning projections.** Linear regression on utilization time-series extrapolates saturation timelines per link, answering "when does this link hit capacity at current growth rates?"

**Cascading failure detection.** BFS-based analysis measures failure propagation depth and breadth when links or nodes are removed, quantifying blast radius.

**N-1 failure analysis.** Systematically removes each network element and re-evaluates performance, identifying single points of failure.

**Dynamic simulation.** Supports link and node failure/recovery events during simulation, with convergence tracking and success rate monitoring.

**Multi-region geographic modeling.** Nodes carry region and availability zone metadata. Inter-region links are classified by latency zone. GeoJSON export includes region metadata for geographic visualization.

**Checkpointing.** Post-execution checkpoints with deterministic resume. Bincode serialization for compact state snapshots.

---

## Usage

```bash
# Run a Monte Carlo simulation
netflowsim simulate --topology network.graphml --iterations 1000

# Compare queuing models side by side
netflowsim compare --topology network.graphml --models mm1,md1,mg1-pareto

# Generate routing matrix from FIBs
netflowsim generate-routing --fibs routing-tables/

# Run N-1 failure analysis
netflowsim n1-analysis --topology network.graphml

# Generate report with all analysis modules
netflowsim report --config simulation.json
```

Configuration is driven by JSON config files (`--config`), with CLI flags overriding config values, and defaults filling the rest.

---

## Scale

Performance at 100k nodes, 1,000 iterations, all analysis features enabled:

| Metric | Value |
|--------|-------|
| **Runtime** | 187.9s |
| **Throughput** | 53.2k flows/sec (with all v2.0 analysis modules) |
| **Baseline throughput** | 4.5M flows/sec (Monte Carlo only, no analysis) |
| **Memory** | 8.4 GB |

The gap between baseline and full-feature throughput reflects the cost of time-series tracking, correlation analysis, and capacity planning modules running on every iteration. The Monte Carlo engine itself sustains millions of flows per second.

---

## Ecosystem Integration

Part of the [network automation ecosystem](../automationarch). The simulator consumes topologies and traffic demands from [Topology Generator](../topogen) and exports GeoJSON with link utilization statistics for [Network Visualization Engine](../netvis) geographic rendering.

**Data flow:**
- **In:** GeoJSON topology, traffic CSV from Topology Generator; FIB routing matrices from [Network Simulator](../netsim)
- **Out:** GeoJSON with utilization overlays, statistical reports (JSON), CDF/trend plots (PNG/SVG)

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Rust (14,813 lines) |
| Graph engine | Petgraph (StableGraph for dynamic mutations) |
| Parallelism | Rayon |
| Serialization | Serde (JSON), Bincode (checkpoints) |
| Visualization | Plotters (PNG/SVG) |
| Statistics | statrs (distributions), manual Pearson correlation and linear regression |
| Profiling | DHAT (heap profiling, feature-flagged) |

---

## Status

**Current version:** v2.0 (shipped 2026-03-01)

**Release history:**
- **v2.0** (2026-03-01) — Multi-region modeling, time-series tracking, bottleneck detection, correlation analysis, capacity planning, cascading failure detection, 30-scenario validation suite
- **v1.1** (2026-02-22) — M/G/1 queuing with Pollaczek-Khinchine, heavy-tailed distributions, parallel model comparison, schema evolution
- **v1.0** (2026-02-20) — Monte Carlo simulation, M/M/1 and M/D/1 queuing, ECMP path tracing, N-1 analysis, CDF plots

---

## Technical Reports

Criterion benchmark reports archived for 50k, 75k, and 100k node topologies. See the project repository for full profiling data.

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
