---
layout: default
section: data-analytics
---

# Weather (BOM ACCESS Pipeline)

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Concept

Data engineering pipeline that fetches, processes, and serves weather model data from the Australian Bureau of Meteorology. Targets ACCESS (Australian Community Climate and Earth-System Simulator) model outputs, bypassing BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a queryable interface for localized weather forecasts. Initial geographic focus on South Australia.

---

## Features

- Automated FTP polling and ingestion of ACCESS model data (~6-hour refresh cycles)
- GRIB2/NetCDF conversion to Parquet/DuckDB for columnar querying
- JSON API endpoints for point-location weather queries
- Polars-based analysis for large multidimensional weather datasets

---

[← Back to Data Analytics](../data-analytics)
