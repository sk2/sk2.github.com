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
- [Primary Objectives](#primary-objectives)
- [Milestones](#milestones)
- [Current Milestone: v2.0 Production-Grade Scale](#current-milestone-v20-production-grade-scale)
- [Ecosystem Context](#ecosystem-context)
- [Current State](#current-state)
- [Key Decisions](#key-decisions)
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

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Primary Objectives

1. **Performance:** Utilize Rust and Rayon to maximize multi-core hardware utilization.
2. **Scalability:** Handle massive topologies via Petgraph and efficient data structures.
3. **Decoupling:** Clearly separate the Routing Matrix generation (packet-sim logic) from the Flow Simulation (queuing logic).
4. **Visibility:** Provide high-performance geographic visualization via MVT/Martin.

---

## Milestones

- ✅ **v1.0 MVP**  — Shipped 2026-02-20
- ✅ **v1.1 Enhanced Queuing Models**  — Shipped 2026-02-22
- 🚧 **v2.0 Production-Grade Scale** (In Progress)

See `.planning/MILESTONES.md` for full milestone history.

---

## Current Milestone: v2.0 Production-Grade Scale

**Goal:** Transform netflowsim into a production-grade platform capable of analyzing massive carrier-scale networks (100k+ nodes) with enhanced analytical capabilities and multi-region geographic modeling.

**Motivation:** Ecosystem completion - aligning netflowsim capabilities with topogener/netsim to enable seamless end-to-end workflows at production scale.

**Target features:**
- **Scale & Performance:** Optimize for 100k+ node networks, eliminate memory/traversal bottlenecks, maintain 1M+ flows/sec throughput
- **Enhanced Analysis:** Time-series behavior tracking, correlation analysis, capacity planning projections, cascading failure detection
- **Multi-Region Support:** Geographic topology modeling, inter-region links with latency zones, geo-distributed traffic patterns

**Success criteria:**
- Performance targets met: 100k+ nodes analyzed in <10min, 1M+ flows/sec throughput maintained
- Ready for real-world deployment in production network planning
- All three capability areas fully implemented and validated
- Seamless ecosystem integration (topogener → netsim → netflowsim → netvis)

---

## # Validated (v1.0)

- ✓ Simulate 1M+ flows through 10k+ nodes in under 1 second — v1.0 
- ✓ Support standard graph formats (GraphML/JSON) — v1.0 
- ✓ Accurate analytic modeling (M/M/1, M/D/1) validated against theoretical benchmarks — v1.0 
- ✓ Real-time visualization of congestion hotspots — v1.0 
- ✓ FIB ingestion and routing matrix generation — v1.0 
- ✓ Path tracing with ECMP support and loop detection — v1.0 
- ✓ Integration with topogener and packet simulators — v1.0 
- ✓ Statistical analysis with percentiles (p50/p90/p95/p99) — v1.0 
- ✓ CDF plot generation for latency, throughput, queueing delay, link utilization — v1.0 
- ✓ Automated bottleneck detection with Top-K ranking — v1.0 
- ✓ Dynamic simulation with link/node failure events — v1.0 
- ✓ Convergence tracking and success rate monitoring — v1.0 
- ✓ N-1 failure analysis for critical component identification — v1.0

---

## # Validated (v1.1)

- ✓ M/G/1 queuing model with Pollaczek-Khinchine formula — v1.1 
- ✓ Heavy-tailed distributions (Pareto, LogNormal, Weibull) — v1.1 
- ✓ Custom distribution framework with automatic CV² calculation — v1.1 
- ✓ Queuing model validation suite (Little's Law, K-S tests, regression benchmarks) — v1.1 
- ✓ Performance comparison across queuing models (parallel execution) — v1.1 
- ✓ Schema evolution with backward compatibility (v1.0 → v1.1) — v1.1 
- ✓ CLI config-driven execution with reproducible results — v1.1

---

## # Active (v2.0)

- [ ] Performance optimization for 100k+ node networks
- [ ] Memory-efficient graph traversal for massive topologies
- [ ] Time-series analysis of network behavior over simulation duration
- [ ] Correlation analysis between link utilization and failures
- [ ] Capacity planning projections and threshold detection
- [ ] Cascading failure detection and analysis
- [ ] Multi-region topology support with geographic zones
- [ ] Inter-region link modeling with latency penalties
- [ ] Geo-distributed traffic patterns

---

## # Future Milestones

- [ ] Enhanced visualization options (interactive plots, dashboards)
- [ ] Additional M/G/1 distributions (Gamma, Beta, custom user-defined)
- [ ] Real-time monitoring integration
- [ ] Machine learning for anomaly detection

---

## # Out of Scope

- Real-time packet-level simulation — use dedicated packet simulators
- GUI interface — CLI-first approach with programmatic access
- Network configuration management — focus on analysis, not orchestration

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. netflowsim provides flow-based traffic analysis — the "analyze" stage of the pipeline.

**Role:** Validate network capacity and performance at scale using analytic queuing models and Monte Carlo simulation. Consume topologies and traffic demands from topogen; consume FIBs from netsim for path tracing.

**Key integration points:**
- Consumes GeoJSON topology and traffic CSV from topogen
- Consumes (planned) FIB routing matrices from netsim for post-simulation traffic analysis
- Exports GeoJSON with link utilization statistics for netvis geographic rendering
- CLI: `netflowsim simulate | generate-routing | verify-routing`

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities

---

## Current State

**Version:** v1.1 (shipped 2026-02-22)
**Codebase:** 8,010 lines of Rust
**Tech Stack:** Rust, Petgraph (StableGraph), Rayon, Serde, Plotters, Criterion, approx, kolmogorov_smirnov
**CLI Commands:** `simulate`, `compare`, `generate-routing`, `report`, `n1-analysis`

**Shipped Features (v1.0 + v1.1):**
- High-performance Monte Carlo simulation (1M+ flows/sec)
- M/G/1 queuing theory with Pollaczek-Khinchine formula
- General service time distributions (Pareto, LogNormal, Weibull, Exponential, Deterministic)
- Automatic CV² calculation from distribution parameters
- Parallel comparison mode across multiple queuing models
- Routing matrix generation from distributed FIBs
- Path tracing with ECMP and loop detection
- Advanced statistical analysis (percentiles, CDFs)
- CDF plot rendering with theoretical overlays (PNG + SVG)
- Bottleneck detection (links and nodes)
- Dynamic simulation with events
- N-1 failure analysis
- Validation suite (Little's Law, K-S tests, regression benchmarks)
- Config-driven execution with `--config` flag
- JSON error envelopes for CLI failures
- Schema evolution with v1.0 backward compatibility
- Reproducible results (embedded + sidecar run_config)

**Known Limitations:**
- Dynamic simulation results use different schema than static (by design)
- No interactive visualization (plots are static images)
- Weibull throughput benchmark missing (same code path as other M/G/1 models)

**Next Milestone Planning:**
- Additional M/G/1 distributions or visualization enhancements
- Performance optimization for >100k node networks
- Multi-region topology support

---

## Key Decisions

| Decision | Rationale | Outcome | Status |
|----------|-----------|---------|--------|
| Recursive path tracing with ECMP | Handles multi-path routing correctly | Works well, cycle detection robust | ✓ Good |
| Interface-to-link resolution via subnet matching | Automates FIB-to-topology mapping | Eliminates manual configuration | ✓ Good |
| Nearest-rank percentiles | Avoids interpolation complexity | Simple, robust, accurate | ✓ Good |
| Node bottleneck scoring: 1.0 - ∏(1-p) | Captures "at least one incident link congested" | Identifies aggregate hotspots | ✓ Good |
| StableGraph for dynamic mutations | Enables runtime topology changes | Zero breaking changes to earlier phases | ✓ Good |
| Separate schemas for static/dynamic | Different modes track different metrics | Clean separation, documented limitation | ✓ Good |
| Warn for Pareto α ≤ 2 (infinite variance) | Retains user flexibility for heavy-tailed exploration | Allows analysis with caveats | ✓ Good |
| Automatic CV² calculation via distribution methods | Eliminates manual input errors | Correct queuing theory application | ✓ Good |
| Deterministic seeded traffic for comparison mode | Ensures fair cross-model results | Reproducible performance comparisons | ✓ Good |
| Config-first merge (config → CLI → defaults) | Deterministic merge order for errors | Clear validation feedback | ✓ Good |
| Dual persistence (embedded + sidecar run_config) | Self-contained results + easy extraction | Perfect reproducibility | ✓ Good |
| Additive v1.1 schema with serde defaults | v1.0 backward compatibility | Seamless version migration | ✓ Good |


*Last updated: 2026-02-22 — v2.0 milestone goals refined with success criteria*

---

## Current Status

2026-02-24 —  verified passed

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)
