---
layout: default
section: projects
---

# Weather (BOM ACCESS Pipeline)

<span class="status-badge status-active">Phase 2/4 — Ingestion Pipeline</span>

[← Back to Projects](../projects)

---

## Concept

The primary goal is to bypass the complexity of BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a clean, queryable interface for localized weather insights, starting with South Australia.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 2/4 — Ingestion Pipeline |
| **Language** | Python |
| **Started** | 2026 |

---

## What This Is

An automated data engineering pipeline that fetches, processes, and serves high-resolution weather model data from the Australian Bureau of Meteorology (BOM). It converts raw ACCESS (Australian Community Climate and Earth-System Simulator) GRIB2 files into queryable Parquet format with DuckDB analytics, focused on South Australia.

## Key Features

- **GRIB2 Decoding**: Automated conversion of binary meteorological data to structured Parquet via cfgrib
- **Spatial Subsetting**: Automatic filtering to South Australia region with proper ACST/ACDT timezone handling
- **FTP Ingestion**: Automated BOM FTP polling with "polite" constraints (passive mode, 20-second delays)
- **Metadata Tracking**: DuckDB catalog for model run deduplication and audit trails
- **Hive Partitioning**: Date-partitioned Parquet files for efficient time-range querying

## Data Flow

```
BOM FTP Server (GRIB2)
    ↓ Automated polling (6-hourly)
cfgrib Decoder → xarray Dataset
    ↓ Spatial filtering (SA region)
Polars Normalization (K→C, Pa→hPa)
    ↓ Hive partitioning
Parquet Storage + DuckDB Catalog
    ↓ (Phase 3)
FastAPI Query Endpoint
```

## Milestones

**Phase 1: Decoding Engine** (Complete)
GRIB2 to Parquet conversion, spatial subsetting, timezone handling, unit normalization.

**Phase 2: Ingestion Pipeline** (Complete)
BOM FTP client, metadata catalog, Hive-partitioned storage, scheduling and CLI.

**Roadmap:**

- **Phase 3: API & Query** — FastAPI endpoint for coordinate-based weather queries, DuckDB SQL interface, sub-500ms query performance
- **Phase 4: Analysis Utility** — CLI tool for daily weather summaries, agentic webhooks for weather alerts

## Tech Stack

Python (cfgrib, xarray, Polars, DuckDB), BOM ACCESS model data, Hive-partitioned Parquet

---

[← Back to Projects](../projects)
