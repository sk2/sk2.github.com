---
layout: default
section: data-analytics
description: "DataRaster — a Rust-native engine for rendering massive spatial datasets into density maps, raster tiles, and analysis layers, with CLI, server, and Python surfaces."
---

# DataRaster

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">WASM</span>
</div>

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Rendering & Analysis](#rendering--analysis)
- [Interfaces](#interfaces)
- [Current Status](#current-status)

## Concept

DataRaster turns massive spatial datasets into density maps, raster tiles, and
analysis outputs. It is built for the point where browser-side SVG, notebook
scripts, and hand-rolled Python pipelines stop scaling — a compiled backend for
dense point, line, and polygon rendering.

The shortest framing, for anyone who knows Datashader: DataRaster is a
deployment-friendly backend for the same class of dense spatial rendering, with
a tile server, Python bindings, and diagnostics built around it. It replaces the
rendering-and-serving middle of a typical stack — query, pull into Python,
render with Datashader or matplotlib, export tiles, serve them — with one engine
that reads the source data and renders or serves directly.

![Global earthquake density rendered by DataRaster](/images/datavis-earthquakes.png)
*Every recorded earthquake epicentre as a density map. Plate boundaries emerge
from the raw point cloud with no point-by-point drawing.*

---

## Architecture

A ten-crate Rust workspace — roughly 60,000 lines, 555 tests — separating the
core engine from its delivery surfaces:

- **Core engine** — point, line, and polygon rasterization; CPU execution with an
  optional `wgpu` GPU path.
- **Spec and plan** — a declarative document model describing views, layers, and
  projections, compiled into a render plan.
- **CLI, server, Python, WASM** — four front ends over the same engine.
- **Polars plugin** — rendering exposed as a native dataframe operation.

Datasets are read from Parquet and CSV, including directly from S3, R2, GCS, and
Azure Blob Storage as first-class sources — the same backend serves a local file
and a cloud-hosted table without a separate ingestion step.

![Flight-path density rendered by DataRaster](/images/datavis-flights.jpg)
*Line rendering: hundreds of thousands of great-circle flight paths aggregated
into a single density layer.*

---

## Rendering & Analysis

Beyond density maps, the engine carries the analysis stages a spatial workflow
usually bolts on afterwards:

- Contours, peak and hotspot detection, and change-detection workflows
- Multi-layer compositing, bivariate rendering, and edge bundling
- Semantic zoom — a view switches from aggregate heatmap to individual points
  once density drops below a threshold, blending the two across a transition band
- Profiling, diagnostics, and transfer-function and colormap recommendations,
  so a first result is good without manual tuning

![Urban trip density rendered by DataRaster](/images/datavis-citibike.png)
*Point density at city scale — bike-share trip endpoints across a metro area.*

---

## Interfaces

From a raw Parquet file, one command probes the data, picks columns, and
recommends a transfer function and colormap:

```bash
data-raster auto data/points.parquet -o out.png
```

The tile server runs the same engine against a local or cloud dataset:

```bash
data-raster-server serve s3://my-bucket/massive.parquet --port 3000
```

The Python bindings take Polars or pandas frames directly and keep the heavy
raster work in the Rust engine:

```python
import data_raster
import polars as pl

df = pl.read_parquet("benchmark_1m.parquet")
data_raster.render_to_file(
    df, "x", "y",
    output="benchmark_1m.png",
    transfer="eq_hist",
    colormap="plasma",
)
```

---

## Current Status

Active development across the core engine, tile server, and Python and WASM
front ends. Source: [github.com/sk2/datavis](https://github.com/sk2/datavis).

---

[← Back to Data Analytics](../data-analytics)
