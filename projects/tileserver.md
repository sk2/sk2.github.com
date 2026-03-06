---
layout: default
section: data-analytics
---

# Tileserver Polars

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

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

[← Back to Data Analytics](../data-analytics)
