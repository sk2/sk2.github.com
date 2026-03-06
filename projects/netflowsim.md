---
layout: default
section: network-automation
---

# Performance Simulator

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Primary Objectives](#primary-objectives)
- [Milestones](#milestones)
- [Current Milestone: v2.1 Performance Optimization](#current-milestone-v21-performance-optimization)
- [Current State](#current-state)
- [Requirements](#requirements)
- [Tech Stack](#tech-stack)
- [Ecosystem Context](#ecosystem-context)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## Concept

`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds, identify bottlenecks probabilistically, test network resilience under failure scenarios, and project capacity headroom for carrier-scale networks (100k+ nodes).

---

## Primary Objectives

1. **Performance:** Utilize Rust and Rayon to maximize multi-core hardware utilization.
2. **Scalability:** Handle massive carrier-scale topologies (100k+ nodes) via Petgraph and efficient data structures.
3. **Decoupling:** Clearly separate the Routing Matrix generation (packet-sim logic) from the Flow Simulation (queuing logic).
4. **Visibility:** Provide high-performance geographic visualization via MVT/Martin with multi-region support.

---

## Milestones

- ✅ **v1.0 MVP**  — Shipped 2026-02-20
- ✅ **v1.1 Enhanced Queuing Models**  — Shipped 2026-02-22
- ✅ **v2.0 Production-Grade Scale**  — Shipped 2026-03-01

See `.planning/MILESTONES.md` for full milestone history.

---

## Current Milestone: v2.1 Performance Optimization

**Goal:** Reduce memory footprint, runtime overhead, and restore throughput while maintaining all v2.0 features.

**Target features:**
- Memory optimization to <6GB at 100k nodes (from 8.37GB)
- Feature overhead reduction to < vs baseline (from )
- Throughput recovery to >500k flows/sec with all features (from 53.2k)

---

## Current State

**Version:** v2.0 (shipped 2026-03-01)
**Codebase:** 14,813 lines of Rust (+ from v1.1)
**Tech Stack:** Rust, Petgraph (StableGraph), Rayon, Serde, Plotters, Criterion, approx, kolmogorov_smirnov, statrs
**CLI Commands:** `simulate`, `compare`, `generate-routing`, `report`, `n1-analysis`

**Shipped Features (v1.0 + v1.1 + v2.0):**
- High-performance Monte Carlo simulation (4.5M flows/sec baseline at 100k nodes)
- M/G/1 queuing theory with Pollaczek-Khinchine formula
- General service time distributions (Pareto, LogNormal, Weibull, Exponential, Deterministic)
- Automatic CV² calculation from distribution parameters
- Parallel comparison mode across multiple queuing models
- Routing matrix generation from distributed FIBs
- Path tracing with ECMP and loop detection
- Advanced statistical analysis (percentiles, CDFs)
- CDF plot rendering with theoretical overlays (PNG + SVG)
- **[v2.0] Time-series behavior tracking** with bounded memory and adaptive sampling
- **[v2.0] Bottleneck detection and ranking** with  utilization threshold
- **[v2.0] Correlation analysis** with time-lagged causality detection
- **[v2.0] Capacity planning projections** with linear regression and saturation timeline
- **[v2.0] Cascading failure detection** with BFS depth/breadth metrics
- **[v2.0] Multi-region geographic topology modeling** with latency zones
- **[v2.0] Region-aware traffic generation** with configurable locality bias
- **[v2.0] Region-filtered statistics and bottlenecks**
- **[v2.0] GeoJSON export with region metadata** for [netvis](../netvis) visualization
- **[v2.0] Comprehensive validation suite** (30 scenario feature matrix, 16 Little's Law tests)
- Dynamic simulation with events
- N-1 failure analysis
- Validation suite (Little's Law, K-S tests, regression benchmarks)
- Config-driven execution with `--config` flag
- JSON error envelopes for CLI failures
- Schema evolution with v1.0/v1.1 backward compatibility
- Reproducible results (embedded + sidecar run_config)
- Incremental routing cache for topology changes
- Checkpointing system for long-running simulations

**Performance Characteristics (100k nodes, 1000 iterations, all v2.0 features):**
- Runtime: 187.93s (well under 10min target)
- Memory: 8.37GB (2.1× over 4GB target - feature overhead documented)
- Throughput: 53.2k flows/sec ( overhead from v2.0 features vs baseline)

**Known Limitations:**
- Dynamic simulation results use different schema than static (by design)
- No interactive visualization (plots are static images)
- v2.0 feature overhead:  runtime increase,  throughput reduction vs baseline (optimization opportunity for v2.1)
- Placeholder link IDs in bottleneck/capacity analysis (infrastructure ready for per-link tracking)

**User Feedback Themes:**
- Functional correctness:  validation success (feature matrix, Little's Law, backward compatibility)
- Performance at scale: Runtime targets met, memory/throughput gaps documented and non-blocking

**Technical Debt:**
- Memory optimization opportunities (8.37GB vs 4GB target at 100k nodes)
- Feature overhead reduction ( runtime increase from time-series + analysis modules)
- Per-link tracking enhancement (replace placeholder link IDs)
- Statistical equivalence test requires v1.0 baseline archive

---

## Requirements



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

## # Validated (v2.0)

- ✓ 100k+ nodes analyzed in <10min — v2.0 
- ✓ Multi-scale profiling infrastructure (25k-125k nodes) — v2.0 
- ✓ Incremental routing cache for topology changes — v2.0 
- ✓ Post-execution checkpointing with deterministic resume — v2.0 
- ✓ Time-series behavior tracking over simulation duration — v2.0 
- ✓ Bounded memory streaming with adaptive sampling — v2.0 
- ✓ Rolling window metrics (mean/max/count) — v2.0 
- ✓ Trend plot generation (utilization, bottlenecks, latency percentiles) — v2.0 
- ✓ Bottleneck detection with  utilization threshold — v2.0 
- ✓ Correlation analysis with time-lagged causality detection — v2.0 
- ✓ Capacity planning projections with saturation timeline — v2.0 
- ✓ Cascading failure detection with BFS depth/breadth metrics — v2.0 
- ✓ Geographic zone definitions (region_id, availability_zone) — v2.0 
- ✓ Inter-region latency zones (WAN link classification) — v2.0 
- ✓ Region-aware traffic generation with locality bias — v2.0 
- ✓ Region-filtered statistics and bottlenecks — v2.0 
- ✓ GeoJSON export with region metadata — v2.0 
- ✓ Feature matrix validation (30/30 scenarios passed) — v2.0 
- ✓ Queuing theory correctness (16/16 Little's Law tests) — v2.0 
- ✓ Backward compatibility (v1.0/v1.1 → v2.0 schema migration) — v2.0

---

## # Active (v2.1)

- [ ] Memory optimization to <6GB at 100k nodes (currently 8.37GB)
- [ ] Feature overhead reduction to < vs baseline (currently )
- [ ] Throughput recovery to >500k flows/sec with features (currently 53.2k)

---

## # Active (Future Work)

- [ ] Per-link tracking to replace placeholder link IDs
- [ ] Mid-execution checkpoint/resume (post-execution complete)
- [ ] Enhanced visualization options (interactive plots, dashboards)
- [ ] Additional M/G/1 distributions (Gamma, Beta, custom user-defined)

---

## # Out of Scope

- Real-time packet-level simulation — use dedicated packet simulators
- GUI interface — CLI-first approach with programmatic access
- Network configuration management — focus on analysis, not orchestration
- 4GB memory target — revised to 8-10GB for full feature set (architectural constraint)
- 1M flows/sec with all features — baseline achievable, feature overhead optimization deferred to v2.1

---

## Tech Stack

- **Language:** Rust
- **Graph Library:** Petgraph (StableGraph for dynamic mutations)
- **Parallelism:** Rayon (parallel Monte Carlo execution)
- **Serialization:** Serde (JSON), Bincode (checkpoints), Postcard (future)
- **Visualization:** Plotters (PNG/SVG), Martin (Tileserver), MVT (Mapbox Vector Tiles)
- **Profiling:** DHAT (heap profiling with feature flag)
- **Math:** statrs (distributions), manual implementations (Pearson correlation, linear regression)

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. netflowsim provides flow-based traffic analysis — the "analyze" stage of the pipeline.

**Role:** Validate network capacity and performance at scale using analytic queuing models and Monte Carlo simulation. Consume topologies and traffic demands from [topogen](../topogen); consume FIBs from [netsim](../netsim) for path tracing.

**Key integration points:**
- Consumes GeoJSON topology and traffic CSV from [topogen](../topogen)
- Consumes (planned) FIB routing matrices from [netsim](../netsim) for post-simulation traffic analysis
- Exports GeoJSON with link utilization statistics for [netvis](../netvis) geographic rendering
- CLI: `netflowsim simulate | generate-routing | verify-routing`

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities

---

## Key Decisions

| Decision | Rationale | Outcome | Status |
|----------|-----------|---------|--------|
| Recursive path tracing with ECMP | Handles multi-path routing correctly | Works well, [cycle](../cycle) detection robust | ✓ Good |
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
| **[v2.0] DHAT profiling via feature flag** | Avoids production overhead while enabling allocation tracking | No runtime penalty, profiling when needed | ✓ Good |
| **[v2.0] Tick(u64) as unified time index** | Single time axis works across Monte Carlo and dynamic modes | Simplifies time-series collection | ✓ Good |
| **[v2.0] Adaptive sampling + fixed point budget** | Min-interval plus change-triggered emission with downsampling | Prevents memory explosion at scale | ✓ Good |
| **[v2.0] Bottleneck threshold util>=0.80** | Industry standard threshold balances sensitivity with actionability | Effective bottleneck detection | ✓ Good |
| **[v2.0] Manual Pearson correlation (~30 LOC)** | Avoids external dependency bloat (linfa/polars) | Lightweight, maintainable | ✓ Good |
| **[v2.0] Adaptive max_lag using 2× median interval** | Prevents false positives in correlation analysis | Robust causality detection | ✓ Good |
| **[v2.0] Manual linear regression (least squares)** | Avoids linfa/polars for simple use case | ~40 LOC, no external deps | ✓ Good |
| **[v2.0] RegionLocalityConfig with locality_factor (0.0-1.0)** | Controls same-region traffic bias | Flexible geo-distributed patterns | ✓ Good |
| **[v2.0] Graceful degradation for nodes without region_id** | Enables parallel plan execution and backward compatibility | Seamless v1.x → v2.0 migration | ✓ Good |
| **[v2.0] LatencyZone enum for WAN links** | Type-safe representation prevents invalid values | Clear inter-region link classification | ✓ Good |
| **[v2.0] Optimized pairwise coverage (30 scenarios vs 540)** | Keeps validation time under 40 minutes | Comprehensive validation without exhaustive tests | ✓ Good |
| **[v2.0] Document failures honestly** | SCALE-02 and SCALE-03 marked FAILED based on empirical evidence | Transparent performance characteristics | ⚠️ Revisit (v2.1 optimization) |
| **[v2.0] Accept partial phase goal achievement** | 1/3 performance targets met (runtime), 2/3 failed (memory, throughput) | Functional completeness prioritized over perf | ⚠️ Revisit (v2.1 optimization) |
| **[v2.0] Arc<String> for immutable flow fields** | Eliminates 300k allocations in Monte Carlo hot path | Improved baseline performance | ✓ Good |
| **[v2.0] HashMap::with_capacity() for known sizes** | Eliminates reallocation overhead at scale | Reduced allocation churn | ✓ Good |
| **[v2.0] Iteration-specific seed derivation (base_seed + index)** | Deterministic parallel execution without rayon hooks | Reproducible parallel Monte Carlo | ✓ Good |
| **[v2.0] Restart-with-seed resume semantics** | Simpler than incremental, avoids rayon hooks | Post-execution checkpoints complete | — Pending (mid-execution deferred) |


*Last updated: 2026-03-01 after v2.1 milestone start*

---

## Current Status

2026-03-05 — Archived Criterion 50k/75k/100k reports;  near-complete

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)
