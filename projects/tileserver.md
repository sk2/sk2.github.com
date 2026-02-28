---
layout: default
section: projects
---

# Tileserver Polars (Rust Optimized)

<span class="status-badge status-active">Active</span>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Vision](#vision)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)

## Concept

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

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

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)
