---
layout: default
section: data-analytics
---

# matrix-profile-rs

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Polars</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Concept

Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust for motif discovery and anomaly detection in time series data. Achieves 2.5x speedup via SIMD (AVX2/NEON), handles datasets exceeding RAM through memory-budgeted tiling, and integrates with Polars as a native DataFrame operation.

8,700 lines of Rust. 58 tests.

---

## How It Works

```
Time Series (Array1<f64> or Polars Series)
    ↓
Matrix Profile Computation (STOMP / SCAMP / SCRIMP++)
    ↓  SIMD acceleration on contiguous data
MatrixProfile struct (distances, indices, metadata)
    ↓
Discovery APIs → .top_k_motifs(k) / .top_k_discords(k)
    ↓
Polars DataFrame (via to_dataframe()) or Rust types
```

The three algorithms cover different use cases:

- **STOMP**: exact algorithm using QT recurrence for sliding dot products — O(N²)
- **SCAMP**: parallel exact algorithm with centered kernels for numerical stability — O(N²) across cores via Rayon
- **SCRIMP++**: anytime algorithm with budget-based early stopping — returns approximate results that improve over time

SIMD dispatch is transparent: contiguous data is automatically accelerated (408ns to 166ns for m=64). For datasets exceeding RAM, the tiling module partitions computation into memory-budgeted chunks — validated at N=10^6 under a 64MB budget.

---

## Features

- Three Matrix Profile algorithms (STOMP, SCAMP, SCRIMP++)
- Motif and discord discovery with deterministic tie-breaking
- Rayon parallel execution across all algorithms
- SIMD vectorization (AVX2/NEON) with transparent dispatch
- Memory-efficient tiling for large datasets (N > 10^6)
- Polars plugin: `df.select(pl.col("ts").mp().stomp(m=20))`
- Feature-gated Polars integration keeps default build dependency-light

---

## Status

**v1.0 shipped** (February 2026): all three algorithms, SIMD, tiling, Polars integration.

**v1.1 in progress**: streaming API for incremental updates, sliding window mode, async callbacks for real-time pattern detection.

---

[← Back to Data Analytics](../data-analytics)
