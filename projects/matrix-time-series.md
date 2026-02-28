---
layout: default
section: projects
---

# matrix-profile-rs

<span class="status-badge status-active">Recently Updated</span>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Use Cases](#use-cases)
- [Current Milestone: v1.1 Streaming](#current-milestone-v11-streaming)
- [Key Decisions](#key-decisions)
- [Why Rust + Polars?](#why-rust-polars)
- [Technical Details](#technical-details)
- [Current Status](#current-status)

## Concept

Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis with SIMD acceleration, out-of-memory tiling support, and Polars ecosystem integration. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Think of it as "find repeating patterns and anomalies in any time series data" with a simple API: `df.select(pl.col("ts").mp().stomp(m=20))` for Polars users, or direct Rust APIs for maximum performance and scale.

Time series analysis requires identifying:
- **Repeating patterns** (motifs): "This sensor pattern happened 15 times before failure"
- **Anomalies** (discords): "This heartbeat segment is unlike any other"
- **Similar segments**: "Find all sequences similar to this known good pattern"

Existing solutions:
- **Python libraries (stumpy)**: Slow, JIT dependencies, awkward array manipulation
- **Manual implementation**: Complex algorithms, easy to get wrong, poor performance
- **Academic prototypes**: Not production-ready, missing ergonomics

matrix-profile-rs provides production-quality implementations with:
- Native performance (2.5x SIMD speedup, no JIT warmup)
- Clean APIs (`.motifs(k=3)` instead of array indexing)
- Scalability (N>10^6 via memory-efficient tiling)
- Polars integration (treat Matrix Profiles as DataFrame operations)

**Performance at scale with ergonomic APIs** — achieve 2.5x speedup via SIMD, handle datasets larger than RAM via tiling, while maintaining simple `.motifs(k)` / `.discords(k)` interfaces.

Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis with SIMD acceleration, out-of-memory tiling support, and Polars ecosystem integration. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Think of it as "find repeating patterns and anomalies in any time series data" with a simple API: `df.select(pl.col("ts").mp().stomp(m=20))` for Polars users, or direct Rust APIs for maximum performance and scale.

Time series analysis requires identifying:
- **Repeating patterns** (motifs): "This sensor pattern happened 15 times before failure"
- **Anomalies** (discords): "This heartbeat segment is unlike any other"
- **Similar segments**: "Find all sequences similar to this known good pattern"

Existing solutions:
- **Python libraries (stumpy)**: Slow, JIT dependencies, awkward array manipulation
- **Manual implementation**: Complex algorithms, easy to get wrong, poor performance
- **Academic prototypes**: Not production-ready, missing ergonomics

matrix-profile-rs provides production-quality implementations with:
- Native performance (2.5x SIMD speedup, no JIT warmup)
- Clean APIs (`.motifs(k=3)` instead of array indexing)
- Scalability (N>10^6 via memory-efficient tiling)
- Polars integration (treat Matrix Profiles as DataFrame operations)

**Performance at scale with ergonomic APIs** — achieve 2.5x speedup via SIMD, handle datasets larger than RAM via tiling, while maintaining simple `.motifs(k)` / `.discords(k)` interfaces.

Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis with SIMD acceleration, out-of-memory tiling support, and Polars ecosystem integration. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Think of it as "find repeating patterns and anomalies in any time series data" with a simple API: `df.select(pl.col("ts").mp().stomp(m=20))` for Polars users, or direct Rust APIs for maximum performance and scale.

Time series analysis requires identifying:
- **Repeating patterns** (motifs): "This sensor pattern happened 15 times before failure"
- **Anomalies** (discords): "This heartbeat segment is unlike any other"
- **Similar segments**: "Find all sequences similar to this known good pattern"

Existing solutions:
- **Python libraries (stumpy)**: Slow, JIT dependencies, awkward array manipulation
- **Manual implementation**: Complex algorithms, easy to get wrong, poor performance
- **Academic prototypes**: Not production-ready, missing ergonomics

matrix-profile-rs provides production-quality implementations with:
- Native performance (2.5x SIMD speedup, no JIT warmup)
- Clean APIs (`.motifs(k=3)` instead of array indexing)
- Scalability (N>10^6 via memory-efficient tiling)
- Polars integration (treat Matrix Profiles as DataFrame operations)

**Performance at scale with ergonomic APIs** — achieve 2.5x speedup via SIMD, handle datasets larger than RAM via tiling, while maintaining simple `.motifs(k)` / `.discords(k)` interfaces.

Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis with SIMD acceleration, out-of-memory tiling support, and Polars ecosystem integration. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Think of it as "find repeating patterns and anomalies in any time series data" with a simple API: `df.select(pl.col("ts").mp().stomp(m=20))` for Polars users, or direct Rust APIs for maximum performance and scale.

Time series analysis requires identifying:
- **Repeating patterns** (motifs): "This sensor pattern happened 15 times before failure"
- **Anomalies** (discords): "This heartbeat segment is unlike any other"
- **Similar segments**: "Find all sequences similar to this known good pattern"

Existing solutions:
- **Python libraries (stumpy)**: Slow, JIT dependencies, awkward array manipulation
- **Manual implementation**: Complex algorithms, easy to get wrong, poor performance
- **Academic prototypes**: Not production-ready, missing ergonomics

matrix-profile-rs provides production-quality implementations with:
- Native performance (2.5x SIMD speedup, no JIT warmup)
- Clean APIs (`.motifs(k=3)` instead of array indexing)
- Scalability (N>10^6 via memory-efficient tiling)
- Polars integration (treat Matrix Profiles as DataFrame operations)

**Performance at scale with ergonomic APIs** — achieve 2.5x speedup via SIMD, handle datasets larger than RAM via tiling, while maintaining simple `.motifs(k)` / `.discords(k)` interfaces.

Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis with SIMD acceleration, out-of-memory tiling support, and Polars ecosystem integration. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Think of it as "find repeating patterns and anomalies in any time series data" with a simple API: `df.select(pl.col("ts").mp().stomp(m=20))` for Polars users, or direct Rust APIs for maximum performance and scale.

Time series analysis requires identifying:
- **Repeating patterns** (motifs): "This sensor pattern happened 15 times before failure"
- **Anomalies** (discords): "This heartbeat segment is unlike any other"
- **Similar segments**: "Find all sequences similar to this known good pattern"

Existing solutions:
- **Python libraries (stumpy)**: Slow, JIT dependencies, awkward array manipulation
- **Manual implementation**: Complex algorithms, easy to get wrong, poor performance
- **Academic prototypes**: Not production-ready, missing ergonomics

matrix-profile-rs provides production-quality implementations with:
- Native performance (2.5x SIMD speedup, no JIT warmup)
- Clean APIs (`.motifs(k=3)` instead of array indexing)
- Scalability (N>10^6 via memory-efficient tiling)
- Polars integration (treat Matrix Profiles as DataFrame operations)

**Performance at scale with ergonomic APIs** — achieve 2.5x speedup via SIMD, handle datasets larger than RAM via tiling, while maintaining simple `.motifs(k)` / `.discords(k)` interfaces.

---

## Features

**v1.0 Shipped (2026-02-22):**
- ✅ STOMP implementation with QT recurrence
- ✅ SCAMP kernels for numerical stability
- ✅ SCRIMP++ for progressive refinement
- ✅ Exclusion zone logic with configurable zones
- ✅ `MatrixProfile` result type with full metadata
- ✅ `.top_k_motifs(k)` and `.top_k_discords(k)` methods
- ✅ Deterministic selection with finite-only filtering
- ✅ Rayon parallel execution across all algorithms
- ✅ SIMD vectorization (AVX2/NEON) with 2.5x speedup
- ✅ Memory-efficient tiling for N>10^6 datasets
- ✅ Polars plugin with `.mp().stomp()` syntax
- ✅ DataFrame I/O with metadata columns

**Future Milestones (v1.1+):**
- ⏳ Python bindings via PyO3
- ⏳ Disk-backed tiling for N>10^8
- ⏳ Streaming API for real-time updates
- ⏳ Additional SIMD targets (AVX-512)

---

## Use Cases

**Predictive Maintenance:**
- Find recurring degradation patterns before failure
- Detect anomalous sensor behavior
- Example: Motor vibration patterns indicating bearing wear

**Healthcare:**
- Identify irregular heartbeat patterns
- Find repeating movement patterns in activity data
- Example: ECG anomaly detection for arrhythmia screening

**Finance:**
- Discover recurring market microstructures
- Detect anomalous trading patterns
- Example: Flash crash pattern recognition

**Operations:**
- Find repeating load patterns for capacity planning
- Detect anomalous system behavior
- Example: Server load pattern analysis for autoscaling

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current Milestone: v1.1 Streaming

**Goal:** Enable real-time Matrix Profile computation for live time series data.

**Target features:**
- Incremental updates: Append new data points, update affected profile regions efficiently
- Sliding window: Maintain fixed-size profile over rolling time window
- Callbacks/notifications: Alert when patterns or anomalies detected in real-time
- Polars integration: Streaming support in Polars extension trait

---

## # Validated

**Core Algorithms:**
- ✓ STOMP Implementation (CORE-01) — v1.0
- ✓ SCAMP Kernels for numerical stability (CORE-02) — v1.0
- ✓ SCRIMP++ anytime algorithm (CORE-03) — v1.0
- ✓ Exclusion zones for trivial match prevention (CORE-04) — v1.0

**Ergonomics & API:**
- ✓ Motif Discovery (API-01) — v1.0
- ✓ Discord Discovery (API-02) — v1.0
- ✓ Structured Results with MatrixProfile type (API-03) — v1.0

**Performance:**
- ✓ Multi-threading via Rayon (PERF-01) — v1.0
- ✓ SIMD Optimization (AVX2, NEON) achieving 2.5x speedup (PERF-02) — v1.0
- ✓ Tiling Support for N>10^6 datasets (PERF-03) — v1.0

**Ecosystem:**
- ✓ Polars Integration with Series.mp() extension trait (ECO-01) — v1.0

---

## # Active

**v1.1 Streaming (current milestone):**
- [ ] Incremental updates for growing time series
- [ ] Sliding window mode for fixed-size rolling profiles
- [ ] Callback/notification system for pattern detection
- [ ] Polars streaming integration

**Future Enhancements (v1.2+):**
- [ ] Python bindings via PyO3 (deferred from v1.0)
- [ ] Disk-backed tiling for N>10^8 (abstraction ready)
- [ ] Additional SIMD targets (AVX-512, explicit vector types)

---

## # Out of Scope

- **Multivariate Matrix Profiles** — univariate focus keeps implementation tractable
- **GPU acceleration** — CPU SIMD + tiling achieves production performance
- **Online/streaming by default** — batch-first approach, streaming is future enhancement
- **Approximate algorithms besides SCRIMP++** — three algorithms (STOMP, SCAMP, SCRIMP++) cover exact and anytime needs

---

## # Algorithm Stack

- **STOMP**: Iterative exact algorithm using QT recurrence for sliding dot products
- **SCAMP**: Parallel exact algorithm with centered kernels for numerical stability
- **SCRIMP++**: Anytime algorithm providing approximate results that improve over time (budget-based)

---

## # Data Flow

```
Time Series Data (Array1<f64> or Polars Series)
    ↓
Matrix Profile Calculation (STOMP/SCAMP/SCRIMP++)
    ↓ (SIMD acceleration transparent on contiguous data)
MatrixProfile struct (distances, indices, metadata)
    ↓
Discovery APIs → .top_k_motifs() / .top_k_discords()
    ↓
Polars DataFrame (via to_dataframe()) or Rust types
```

---

## # Key Components

- **Core Engine**: Parallel computation using Rayon, SIMD-optimized kernels (2.5x speedup)
- **Result Type**: Binding-friendly `MatrixProfile` with Vec-backed buffers and metadata
- **Discovery API**: High-level methods for pattern extraction with deterministic tie-breaking
- **Tiling Module**: Memory-efficient computation for datasets exceeding RAM
- **Polars Integration**: Native `.mp()` namespace on Series, DataFrame I/O with metadata columns

---

## # Codebase State

**Shipped v1.0 (2026-02-22):** 8,705 LOC Rust across 7 phases, 26 plans
- **matrix-profile-rs**: Primary crate with STOMP, SCAMP, SCRIMP++, SIMD, tiling, Polars integration
- **stump-rs**: Reference implementation used during porting 

**Tech Stack:**
- Rust 1.85+ (2024 edition)
- ndarray for array operations
- Rayon for multi-core parallelism
- Polars for DataFrame integration (feature-gated)
- Criterion for benchmarking

**Test Coverage:**
- 58 tests passing (5 ignored for CI performance: long-run stability, N=10k/100k/1M scale tests)
- Integration tests for all algorithms, SIMD correctness, tiling parity
- Polars integration tests including metadata recovery

---

## # Known Issues & Tech Debt

**Low-Priority (8 items documented in TECH-DEBT.md):**
- Ignored tests for CI performance (passing manually)
- Dead code warnings (TileStorage helpers, WindowStats fields) - future API expansion points
- Documentation mismatches in tiling module (memory_budget_bytes=0 behavior, progress semantics)

**Resolved:**
- Polars metadata persistence (resolved via Phase 7 metadata columns approach)

---

## # User Feedback

None yet — v1.0 is initial release. Expecting feedback on:
- Polars metadata column approach vs `*_with_meta` helpers
- SIMD performance across CPU architectures
- Tiling behavior with real-world large datasets

---

## Key Decisions

| Decision | Rationale | Outcome | Status |
|----------|-----------|---------|--------|
| Separate matrix-profile-rs and stump-rs crates | Port stump-rs for reference, build matrix-profile-rs fresh for API design freedom | Clean APIs, reference validation working | ✓ Good |
| Vec-backed MatrixProfile with sentinels | Binding-friendly, avoids Option overhead | Clean FFI surface, efficient | ✓ Good |
| SIMD transparent dispatch via contiguity check | Zero API changes, automatic acceleration | 2.5x speedup,  cases accelerated | ✓ Good |
| Metadata columns (mp_*) for Polars DataFrame | Polars schema API unstable, columns self-describing | DataFrames fully self-describing | ✓ Good |
| Tiling with memory budget | Enables N>10^6 datasets, user-controlled memory | Validated at N=10^6 under 64MB | ✓ Good |
| Ignore scale tests for CI | N=10k test takes 98s, larger tests minutes | Green CI, manual validation for releases | ✓ Good |
| Feature-gate Polars integration | Keep default build dependency-light | Default build green, Polars optional | ✓ Good |
| SCRIMP++ budget-based anytime | User-controlled trade-off: speed vs accuracy |  budget finds motifs  of time | ✓ Good |

---

## Why Rust + Polars?

**Performance:** Native compiled code achieving 2.5x speedup via SIMD, no JIT warmup, efficient memory usage
**Ergonomics:** Polars integration makes Matrix Profiles a DataFrame operation (`.mp().stomp(m)`)
**Distribution:** Single binary, no runtime dependencies, easy deployment
**Correctness:** Strong typing catches errors at compile time
**Scalability:** Tiling strategy handles datasets larger than RAM

---

## Technical Details

**Matrix Profile Basics:**
- For each subsequence in a time series, find its nearest neighbor
- Result: two arrays (distances to nearest neighbor, indices of nearest neighbors)
- Enables motif discovery (small distances = patterns) and discord detection (large distances = anomalies)

**Algorithm Complexity:**
- Naive: O(N²M) where N = series length, M = subsequence length
- STOMP: O(N²) with clever recurrence relations
- SCAMP: O(N²) parallelized across cores
- SCRIMP++: Anytime O(N²) with early stopping

**Performance Achieved (v1.0):**
- SIMD: 2.5x speedup on hot paths (408ns → 166ns for m=64)
- Multi-core: Linear scaling with available cores
- Memory: O(N) base + configurable tiling for N>10^6
- Tiling: N=10^6 validated under 64MB budget


*Last updated: 2026-02-22 after v1.0 milestone, v1.1 milestone started*

---

## Current Status

2026-02-24 — Completed 11-01-PLAN.md: Series.streaming(m) + PolarsStreamingState + mp_* schema

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)
