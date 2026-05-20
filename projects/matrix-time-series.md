---
layout: default
section: data-analytics
description: "The matrix profile is a single transform that exposes a time series' repeated patterns and its anomalies."
---

# matrix-profile-rs

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-04-30</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Polars</span>
</div>

---

## Contents

- [Concept](#concept)
- [Visuals](#visuals)
- [Architecture](#architecture)
- [Features](#features)
- [Current Status](#current-status)

## Concept

The matrix profile is a single transform that exposes a time series' repeated
patterns and its anomalies. It annotates every subsequence with the distance to
its nearest match elsewhere in the series: low values mark **motifs** (a shape
that recurs), high values mark **discords** (a shape unlike any other). It
needs no training, no labelled data, and no domain-specific parameters.

matrix-profile-rs implements the STOMP, SCAMP, and SCRIMP++ algorithms in
native Rust — 8,700 lines, 58 tests. SIMD kernels (AVX2 and NEON) give a 2.5x
speedup over the scalar path, and memory-budgeted tiling keeps series larger
than RAM within a fixed footprint.

---

## Visuals

![Electricity-demand signal with matrix-profile annotations](/images/matrix-annotated-profile.png)
*Top: an electricity-demand signal with the discovered discord and matching motifs boxed. Bottom: the matrix profile — its lowest point locates the strongest motif, its highest point the clearest anomaly.*

![Steam-generator signal with motif arcs](/images/matrix-motif-arc-fanout.png)
*Motif arc fan-out: arcs connect each occurrence of a recurring shape across a steam-generator sensor trace, with the matrix profile below.*

---

## Architecture

Three algorithms cover the exact-and-anytime spectrum:

- **STOMP** — iterative exact algorithm using a QT recurrence for sliding dot products.
- **SCAMP** — parallel exact algorithm with centered kernels for numerical stability.
- **SCRIMP++** — anytime algorithm whose approximate result improves with budget.

Data flows from a Rust `Array1<f64>` or a Polars `Series` into a single
computation kernel — SIMD-accelerated when the data is contiguous, parallelised
across cores by Rayon, tiled when the series exceeds the memory budget. The
result is a `MatrixProfile` struct: distances, indices, and metadata, exposing
`.top_k_motifs()` and `.top_k_discords()` for discovery.

The Polars integration exposes the computation through a `.mp()` namespace on
`Series`, so motif and discord discovery composes with the rest of a Polars
pipeline:

```python
import polars as pl

df = pl.read_parquet("sensor_data.parquet")
result = df.select(pl.col("vibration").mp().stomp(m=20))
```

---

## Features

- Three Matrix Profile algorithms: STOMP, SCAMP, SCRIMP++
- Motif and discord discovery with deterministic tie-breaking
- Rayon parallel execution across all algorithms
- SIMD vectorisation (AVX2 and NEON) with transparent dispatch
- Memory-efficient tiling for datasets larger than RAM (N > 10⁶ validated under 64 MB)
- Polars plugin: `df.select(pl.col("ts").mp().stomp(m=20))`
- Feature-gated Polars integration keeps the default build dependency-light

---

## Current Status

**Implementation status:** Feature work complete through 
**Current focus:** documentation/release reconciliation, not missing streaming functionality
**Release posture:** v1.0 shipped; v2.0-level streaming and multi-stream features are implemented in repo


*Last updated: 2026-04-09 after  completion and documentation reconciliation*

---

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-04-30 |
| **Stack** | Rust, Polars |

---

## Current Status

** 2026-04-30 — Published v2.0.0 release (commits and tags pushed to main)
