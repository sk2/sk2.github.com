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

![GBIF global biodiversity density rendered by DataRaster](/images/datavis-gbif-3b.png)
*The full GBIF release — 3.62 billion species-occurrence records — rendered as a single density layer with an equalized-histogram transfer and the inferno colormap. The Parquet release is read directly from S3, with no intermediate aggregation step.*

![Global earthquake density rendered by DataRaster](/images/datavis-earthquakes.png)
*Every recorded earthquake epicentre as a density map. Plate boundaries emerge from the raw point cloud with no point-by-point drawing.*

![Flight-path density rendered by DataRaster](/images/datavis-flights.jpg)
*Line rendering: hundreds of thousands of great-circle flight paths aggregated into a single density layer.*

![Urban trip density rendered by DataRaster](/images/datavis-citibike.png)
*Point density at city scale — bike-share trip endpoints across a metro area.*

---

[← Back to Data & Analytics](../data-analytics)
