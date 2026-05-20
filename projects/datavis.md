---
layout: default
section: data-analytics
description: "DataRaster — a Rust-native engine for rendering massive spatial datasets into density maps and raster tiles, with CLI, server, Python, and WASM surfaces."
hand_written: true
---

# DataRaster

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">WASM</span>
</div>

---

## Concept

DataRaster turns massive spatial datasets into density maps, raster tiles, and analysis layers. It is a compiled backend for the kind of dense point, line, and polygon rendering that browser-side SVG and notebook-driven Python pipelines stop scaling at.

The shortest framing, for anyone who knows Datashader: DataRaster is a deployment-friendly backend for the same class of dense spatial rendering, with a tile server, Python bindings, and diagnostics built around it. It reads source data — Parquet or CSV, directly from S3, R2, GCS, or Azure Blob — and renders or serves without an intermediate ingestion step.

---

## Visuals

![Global biodiversity density rendered by DataRaster, 3.62 billion GBIF records](/images/datavis-gbif-3b.png)
*GBIF species occurrences — **3.62 billion records** (consolidated 2026-05-01 release) — rendered through the true-KDE splatting path with a Gaussian kernel of σ=2 px and log transfer on a 4096×2048 canvas. **End-to-end wall time 239.62 s** (12-thread Apple M4 Pro, 24 GB host, peak resident 1.96 GB). The count-only path renders the same dataset in **38.16 s** (~95M rows/s on zstd-compressed Parquet). The raw release is consolidated from 7,948 parquet parts into 16 first — the renderer's glob fan-out limit is the binding constraint, not the row count.*

![Global earthquake density rendered by DataRaster, 782K events](/images/datavis-earthquakes.png)
*Earthquake catalogue — **782K events**. Plate boundaries surface as ridge structure in the density field without any per-point drawing.*

![Flight-path density rendered by DataRaster, 67K great-circle segments](/images/datavis-flights.jpg)
*OpenFlights routes — **67K great-circle segments** aggregated into a single line-density layer.*

![Urban trip density rendered by DataRaster, 5.1M Citibike trip starts](/images/datavis-citibike.png)
*Citibike trip starts, October 2024 — **5.1M points** at city scale.*

---

[← Back to Data & Analytics](../data-analytics)
