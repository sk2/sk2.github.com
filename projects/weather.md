---
layout: default
section: projects
---

# Weather (BOM ACCESS Pipeline)

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-02-14</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Current Status](#current-status)

## Concept

Data engineering pipeline that fetches, processes, and serves weather model data from the Australian Bureau of Meteorology. Targets ACCESS (Australian Community Climate and Earth-System Simulator) model outputs, bypassing BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a queryable interface for localized weather forecasts. Initial geographic focus on South Australia.

---

## Features

- Automated FTP polling and ingestion of ACCESS model data (~6-hour refresh cycles)
- GRIB2/NetCDF conversion to Parquet/DuckDB for columnar querying
- JSON API endpoints for point-location weather queries
- Polars-based analysis for large multidimensional weather datasets

---

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-02-14 |
| **Stack** | Python, Polars |

---

## Overview

A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.

---

## Core Value

The primary goal is to bypass the complexity of BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a clean, queryable interface (API/DuckDB) for localized weather insights, starting with South Australia.

---

## Objectives

- Automated FTP polling and ingestion of ACCESS model data.
- High-performance processing using Polars and DuckDB.
- API and JSON endpoints for easy consumption.
- (Future) Agentic event system for weather alerts.
- (Future) Tile server for spatial visualization.

---

## Context

- **Geographic Focus:** South Australia (Initial).
- **Environment:** Local Mac Mini (Development), potentially AWS (Production visualization).
- **Data Source:** BOM FTP (ACCESS model, ~6-hour refresh cycles).

---

## Requirements



---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] Automated FTP client to poll and download ACCESS model files.
- [ ] Ingestion pipeline to convert GRIB2/NetCDF to Parquet/DuckDB.
- [ ] JSON API endpoint for point-location weather queries.
- [ ] Basic CLI or dashboard for data analysis using Polars.

---

## # Out of Scope (v1)

- Global/National scale (Focusing on SA first to manage data volume).
- Live Tile Server visualization (Deferred to v2).
- Complex agentic event triggers (Deferred to v2).

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| South Australia Focus | Reduces initial data volume and complexity while proving the pipeline. | — Pending |
| Polars/DuckDB | High-performance processing suited for large multidimensional weather datasets. | — Pending |
| Mac Mini Hosting | Utilizes existing local hardware for dev/polling before scaling to cloud. | — Pending |

*Last updated: 2026-02-13 after initialization*

---

## Current Status

** 2026-02-14 - Completed 02-04-PLAN.md

---
