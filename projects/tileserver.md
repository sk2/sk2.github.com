---
layout: default
section: data-analytics
description: "A dynamic vector tile server for massive geospatial datasets."
---

# Tileserver Polars (Rust Optimized)

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

---

## Concept

A dynamic vector tile server for massive geospatial datasets. It serves Mapbox
Vector Tiles (MVT) from millions of points with sub-second latency, enabling
interactive visualisation in Kepler.gl and MapLibre without pre-rendering a
static tile set. Python (FastAPI) handles the HTTP layer; Rust (via PyO3) does
coordinate projection and Protobuf encoding; Polars holds the data and runs the
spatial filters.

The argument was that pre-generating tiles for a large dataset is both
storage-intensive and inflexible: every change of filter or zoom strategy means
re-generating the pyramid. Dynamic tiling backed by columnar in-memory filtering
trades a small per-request cost for the ability to change the query at any
moment.

---

## Architecture

- **API layer** — FastAPI serving MVT/PBF tile requests over HTTP.
- **Compute layer** — A Rust extension via PyO3 for per-point coordinate projection
  and Protobuf MVT encoding, where Python overhead would dominate.
- **Data engine** — Polars for vectorised spatial filtering and aggregation
  against the in-memory dataset.
- **Consumers** — Mapbox Vector Tiles, consumed by Kepler.gl or MapLibre.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust, Python, Polars |
