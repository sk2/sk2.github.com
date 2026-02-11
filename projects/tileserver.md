---
layout: default
---

# tileserver

<span class="status-badge status-active">Planning</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Planning |
| **Language** | Python (FastAPI), Rust (PyO3), Polars, Kepler.gl |
| **Started** | 2025 |

---

## The Insight

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

## Problem It Solves

Traditional tile servers pre-render static image tiles, leading to:
- Large storage requirements for high-resolution data.
- Slow updates for dynamic datasets.
- Limited interactivity on the client side.

Dynamic vector tiles solve this by transmitting raw data efficiently, allowing client-side rendering and interactive exploration.

## Architecture

- **Data Source**: Optimized columnar data stores (e.g., Apache Parquet, Polars) for fast querying.
- **Backend**: FastAPI with Rust (PyO3) for high-performance data processing and MVT generation.
- **Client**: Kepler.gl for interactive geospatial visualization.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)