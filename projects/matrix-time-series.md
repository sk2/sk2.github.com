---
layout: default
---

# matrix-profile-rs

<span class="status-badge status-active">Phase 1/5 (90%)</span>

[← Back to Projects](../projects)

---

## The Insight

Developing...

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1/5 (90%) |
| **Language** | N/A |
| **Started** | 2026 |

---
## What This Is

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Think of it as "find repeating patterns and anomalies in any time series data" with a simple API: `df.select(pl.col("ts").mp.stomp(m=20))` for Polars users, or direct Rust APIs for maximum performance.

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
- Native performance (no JIT warmup)
- Clean APIs (`.motifs(k=3)` instead of array indexing)
- Easy distribution (single binary, no Python runtime)
- Polars integration (treat Matrix Profiles as DataFrame operations)

## Features

**Phase 1: Parallel Core Engine** (25% complete)
- ✅ STOMP implementation with QT recurrence
- ✅ Basic parallel execution via Rayon
- 🔄 SCAMP kernels for numerical stability
- 🔄 Exclusion zone logic

**Phase 2: Discovery Ergonomics** (In Progress)
- 🔄 `MatrixProfile` result type with metadata
- ⏳ `.motifs(k)` and `.discords(k)` methods
- ⏳ Interpretable output structures

**Phase 3: Anytime Insights** (Planned)
- ⏳ SCRIMP++ for progressive refinement
- ⏳ Early stopping with confidence bounds

**Phase 4: Hardware Optimization** (Planned)
- ⏳ SIMD vectorization (AVX2/NEON)
- ⏳ Memory-efficient tiling for large datasets

**Phase 5: Ecosystem Integration** (Planned)
- ⏳ Polars plugin with `.mp.stomp()` syntax
- ⏳ Zero-copy result conversion
- ⏳ Python bindings via PyO3

## Architecture

### Algorithm Stack
- **STOMP**: Iterative exact algorithm using QT recurrence for sliding dot products
- **SCAMP**: Parallel exact algorithm optimized for multi-core CPUs
- **SCRIMP++** (planned): Anytime algorithm providing approximate results that improve over time

### Data Flow
```
Time Series Data
    ↓
Matrix Profile Calculation (STOMP/SCAMP/SCRIMP++)
    ↓
MatrixProfile struct (distances, indices, metadata)
    ↓
Discovery APIs → motifs() / discords() / to_polars()
```

### Key Components
- **Core Engine**: Parallel computation using Rayon, SIMD-optimized kernels
- **Result Type**: Binding-friendly `MatrixProfile` with Vec-backed buffers
- **Discovery API**: High-level methods for pattern extraction
- **Polars Plugin** (Phase 5): Native integration with Polars DataFrames

## Use Cases

**Predictive Maintenance:**
- Find recurring degradation patterns before failure
- Detect anomalous sensor behavior

**Healthcare:**
- Identify irregular heartbeat patterns
- Find repeating movement patterns in activity data

**Finance:**
- Discover recurring market microstructures
- Detect anomalous trading patterns

**Operations:**
- Find repeating load patterns for capacity planning
- Detect anomalous system behavior

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
