---
layout: default
section: data-analytics
description: "A dynamic Mapbox Vector Tile server for massive geospatial datasets — Polars in-memory, Rust over PyO3 for per-point math, FastAPI on top."
---

# Tileserver Polars

<div class="badges-row">
  <span class="status-badge status-complete">Superseded</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

<div class="callout">
<p><strong>Superseded by <a href="/projects/datavis">DataRaster</a>.</strong>
DataRaster covers the same dense-spatial-rendering problem with a broader
surface — a tile server, Python and WASM front ends, and a Polars plugin — in
one ten-crate Rust workspace. This page is kept for context on the original
approach.</p>
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

## Why It Was Superseded

The split-language design — FastAPI on top of a PyO3 extension on top of Polars —
was load-bearing for the tile-serving use case, but rebuilding around the same
architecture every time DataRaster needed a different output (static PNG, raster
tile, WASM render, density layer) was not. DataRaster generalises the engine:
one Rust core, one render plan, multiple front ends (CLI, server, Python, WASM)
over the same compute path. The tile-server use case is one mode within it.

---

[← Back to Data Analytics](../data-analytics)
