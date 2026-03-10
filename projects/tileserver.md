---
layout: default
section: data-analytics
description: "Dynamic vector tile server for massive geospatial datasets. Serves Mapbox Vector Tiles (MVT) from millions of points with sub-second latency, enabling…"
---

# Tileserver Polars (Rust Optimized)

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

---

## Concept

Dynamic vector tile server for massive geospatial datasets. Serves Mapbox Vector Tiles (MVT) from millions of points with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets. Python (FastAPI) handles the API layer; Rust (via PyO3) handles coordinate transformation and MVT encoding; Polars provides in-memory filtering and aggregation.

---

## Architecture

- **API**: FastAPI serving MVT/PBF tile requests
- **Computation**: Rust extension via PyO3 for per-point coordinate projection and Protobuf encoding
- **Data engine**: Polars for vectorized spatial filtering and aggregation
- **Output**: Mapbox Vector Tiles consumed by Kepler.gl and MapLibre

Dynamic tiling avoids the storage cost and inflexibility of pre-generated tile pyramids. Polars vectorized filtering handles the spatial queries; Rust handles the per-point math where Python overhead is prohibitive.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust, Python, Polars |

---

## Core Value

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

---

## Vision

A high-performance tile server that combines the speed of columnar data processing (Polars) with the efficiency of systems programming (Rust) to deliver a "Datashader-like" experience for vector data. It bridges the gap between data science workflows (Python) and high-performance web mapping.

---

## Constraints

- **Language**: Python (FastAPI) for the API layer.
- **Computation**: Rust (via PyO3) for coordinate transformation and MVT encoding.
- **Data Engine**: Polars for in-memory filtering and aggregation.
- **Output Format**: Mapbox Vector Tiles (MVT/PBF) consumed by Kepler.gl.
- **Latency**: Sub-second response times for tile requests.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| **Polars over Pandas** | Significantly faster filtering and lower memory overhead for large datasets. | Confirmed  |
| **Rust for Math** | Python overhead is too high for per-point coordinate projection in tight loops. | Confirmed  |
| **Dynamic Tiling** | Pre-generating tiles for large datasets is storage-intensive and inflexible. | Core Architecture |
| **MVT Protocol** | Standard format supported by Kepler.gl and MapLibre, more efficient than JSON. | Planned  |
