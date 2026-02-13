---
layout: default
---

# Weather (BOM ACCESS Pipeline)

<span class="status-badge status-planning">Planning</span>

[← Back to Projects](../projects)

---


## The Concept

High-resolution weather model data from Australia's Bureau of Meteorology exists, but it's buried in complex FTP delivery systems and binary formats (GRIB2/NetCDF). This pipeline automates the fetch-process-serve workflow to provide clean, queryable weather insights for South Australia.

## Quick Facts

| | |
|---|---|
| **Status** | Planning |
| **Language** | Python, Rust |
| **Started** | 2026 |

---

## What This Is

A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targets the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.

## Core Value

Bypass the complexity of BOM's FTP delivery and binary formats to provide a clean, queryable interface (API/DuckDB) for localized weather insights.

## Key Features

### Data Ingestion
- **Automated FTP Polling**: Monitor BOM FTP for ACCESS model updates (~6-hour refresh cycles)
- **Format Conversion**: Transform GRIB2/NetCDF binary formats to Parquet/DuckDB
- **High-Performance Processing**: Polars-based pipeline for large multidimensional datasets

### Query Interface
- **JSON API**: Point-location weather queries with simple HTTP interface
- **DuckDB Backend**: Efficient analytical queries over processed weather data
- **CLI Dashboard**: Polars-based analysis tools for data exploration

### Future Capabilities (v2)
- **Agentic Event System**: Weather alert triggers for automation workflows
- **Tile Server**: Spatial visualization of weather model outputs
- **Geographic Expansion**: Scale from South Australia to national coverage

## Use Cases

- **Photography Planning**: Query cloud cover, visibility, wind for aurora/landscape shoots
- **Automation Integration**: Feed weather data to agentic systems for context-aware decisions
- **Research**: Local access to high-resolution ACCESS model data for analysis

## Architecture

```
┌──────────────────────────────────────────┐
│         BOM FTP Server                    │
│    (ACCESS Model GRIB2/NetCDF)           │
└────────────┬─────────────────────────────┘
             │ 6-hour refresh
    ┌────────▼────────┐
    │  FTP Poller     │
    │  (Automated)    │
    └────────┬────────┘
             │
    ┌────────▼────────────────┐
    │  Ingestion Pipeline     │
    │  (GRIB2/NetCDF → DuckDB)│
    │  Polars Processing      │
    └────────┬────────────────┘
             │
    ┌────────▼────────────────┐
    │     DuckDB Storage      │
    │  (Queryable Weather DB) │
    └────────┬────────────────┘
             │
    ┌────────┼────────┬────────┐
    │        │        │        │
┌───▼──┐ ┌──▼───┐ ┌──▼───┐ ┌──▼────┐
│ API  │ │ CLI  │ │Agents│ │Future │
│      │ │      │ │      │ │ Tiles │
└──────┘ └──────┘ └──────┘ └───────┘
```

## Geographic Focus

**v1:** South Australia
- Reduces initial data volume and complexity
- Proves pipeline architecture
- Provides coverage for local photography/automation needs

**v2:** Potential expansion to national coverage once pipeline is validated

## Tech Stack

- **Ingestion**: Python or Rust FTP client
- **Processing**: Polars (high-performance DataFrame operations)
- **Storage**: DuckDB (analytical SQL database)
- **API**: FastAPI or Axum (Rust)
- **Hosting**: Mac Mini (development/polling), AWS (future visualization)

## Data Source

**Bureau of Meteorology (BOM) - ACCESS Model:**
- High-resolution numerical weather prediction
- ~6-hour update cycles
- Delivered via FTP in GRIB2/NetCDF formats
- Multidimensional gridded data (temperature, precipitation, wind, cloud cover, etc.)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
