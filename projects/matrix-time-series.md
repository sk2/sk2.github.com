---
layout: default
---

# matrix-profile-rs

<span class="status-badge status-active">Phase 8/11 (64%)</span>

[← Back to Projects](../projects)

---

## The Insight

**Performance at scale with ergonomic APIs** — achieve 2.5x speedup via SIMD, handle datasets larger than RAM via tiling, while maintaining simple `.motifs(k)` / `.discords(k)` interfaces.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 8/11 (64%) |
| **Language** | N/A |
| **Started** | 2026 |

---
## What This Is

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis with SIMD acceleration, out-of-memory tiling support, and Polars ecosystem integration. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Think of it as "find repeating patterns and anomalies in any time series data" with a simple API: `df.select(pl.col("ts").mp().stomp(m=20))` for Polars users, or direct Rust APIs for maximum performance and scale.

## Problem It Solves

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

## Architecture

### Algorithm Stack
- **STOMP**: Iterative exact algorithm using QT recurrence for sliding dot products
- **SCAMP**: Parallel exact algorithm with centered kernels for numerical stability
- **SCRIMP++**: Anytime algorithm providing approximate results that improve over time (budget-based)

### Data Flow
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

### Key Components
- **Core Engine**: Parallel computation using Rayon, SIMD-optimized kernels (2.5x speedup)
- **Result Type**: Binding-friendly `MatrixProfile` with Vec-backed buffers and metadata
- **Discovery API**: High-level methods for pattern extraction with deterministic tie-breaking
- **Tiling Module**: Memory-efficient computation for datasets exceeding RAM
- **Polars Integration**: Native `.mp()` namespace on Series, DataFrame I/O with metadata columns

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

[← Back to Projects](../projects) | [Development Philosophy](../development)
