---
layout: default
---

# High-Performance Vector Tile Server

<span class="status-badge status-planning">Phase 0 - Planning</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 0 - Planning complete |
| **Language** | Python + Rust (PyO3) |
| **Stack** | FastAPI · Polars · Rust · Protobuf |
| **Frontend** | Kepler.gl |
| **Performance Target** | <100ms tile latency (millions of points) |
| **Started** | 2026 |
| **License** | TBD |

---

## Overview

High-performance vector tile (MVT) server that efficiently serves dynamic vector tiles from large datasets using modern stack (Polars/Rust/FastAPI). Enables real-time visualization of massive geospatial data in Kepler.gl with Datashader-like aggregation and sub-second latency.

## Problem It Solves

Visualizing large-scale geospatial datasets in web maps has performance challenges:

**Traditional Tile Servers:**
- Pre-generate static tiles (time-consuming, storage-intensive)
- Cannot aggregate data dynamically
- No real-time filtering or queries
- Limited to pre-defined zoom levels

**Database-Backed Rendering:**
- PostGIS queries slow for large datasets
- High database load for tile requests
- Difficult to scale to millions of points
- Latency increases with data volume

**Client-Side Rendering:**
- Browser memory limits
- Poor performance with large datasets
- Cannot handle millions of points
- Slow pan/zoom interactions

**Vector Tile Server provides:**
- On-the-fly tile generation from large datasets
- Sub-second latency (<100ms) for millions of points
- Dynamic aggregation (count, sum) within tiles
- Efficient filtering using Polars DataFrames
- Rust-optimized MVT encoding
- Kepler.gl integration for smooth visualization

## Architecture

### FastAPI Web Layer

Modern async Python framework:

**Endpoints:**
```python
GET /tiles/{z}/{x}/{y}.mvt
  - Returns Mapbox Vector Tile (Protobuf)
  - Query params: filters, aggregation

GET /health
  - Server health check

GET /
  - Basic web interface with map viewer
```

**Features:**
- Async request handling
- Query parameter validation
- CORS for web clients
- OpenAPI documentation

### Polars Data Engine

High-speed data manipulation:

**In-Memory Dataset:**
- Load large CSV/Parquet files efficiently
- Multi-threaded DataFrame operations
- Memory-efficient columnar storage

**Tile Filtering:**
```python
# Efficient bounding box filter
tile_bbox = calculate_tile_bounds(z, x, y)
filtered = df.filter(
    (pl.col("longitude") >= tile_bbox.west) &
    (pl.col("longitude") < tile_bbox.east) &
    (pl.col("latitude") >= tile_bbox.north) &
    (pl.col("latitude") < tile_bbox.south)
)
```

**Aggregation:**
- Count points per tile
- Sum numeric attributes
- Statistical aggregations (mean, median, percentiles)
- Group by categorical fields

### Rust Performance Layer (PyO3)

Critical path optimization:

**Coordinate Math:**
- Lat/lon to tile coordinates conversion
- Tile bounds calculation
- Web Mercator projection
- All in Rust for maximum speed

**MVT Encoding:**
- Mapbox Vector Tile Protobuf generation
- Geometry encoding (points, lines, polygons)
- Feature property serialization
- Optimized for high throughput

**PyO3 Bridge:**
```rust
#[pyfunction]
fn encode_mvt(points: Vec<(f64, f64)>, properties: HashMap<String, Value>) -> PyResult<Vec<u8>> {
    // Rust MVT encoding logic
    Ok(protobuf_bytes)
}
```

### Kepler.gl Integration

Web visualization client:

**MVT Layer:**
- Add custom MVT tile layer
- Dynamic zoom and pan
- Interactive filtering
- Large dataset support

**Features:**
- 3D visualizations
- Time series animations
- Multi-layer composition
- Export to images/video

## Features

### Planned: Phase 1 - Foundation

**Project Setup:**
- FastAPI application structure
- Basic configuration management
- Health check endpoint
- Polars dataset loading

**Initial Endpoints:**
- `/health` for monitoring
- Basic tile endpoint structure
- Dataset info API

### Planned: Phase 2 - Coordinate System

**Rust Integration:**
- PyO3 module setup
- Python-Rust bridge
- Build system (maturin)

**Coordinate Math:**
- Lat/lon to tile coordinates (Rust)
- Tile bounds calculation (Rust)
- Web Mercator utilities
- Performance-critical geometry operations

### Planned: Phase 3 - Tile Engine

**BBox Filtering:**
- Efficient Polars filtering by tile bounds
- Multi-threaded processing
- Memory-efficient operations

**Aggregation:**
- Count aggregation within tiles
- Sum aggregation for numeric fields
- Support for categorical grouping

### Planned: Phase 4 - MVT Encoding

**Protobuf Generation:**
- Python MVT encoding (initial)
- Mapbox Vector Tile spec compliance
- Feature properties support
- Geometry encoding (points focus)

### Planned: Phase 5 - Optimization

**Rust MVT Encoder:**
- Replace Python encoder with Rust
- High-throughput tile generation
- Optimized Protobuf serialization

**Benchmarking:**
- Automated performance suite
- Latency measurements
- Throughput testing
- Optimization of bottlenecks

### Planned: Phase 6 - Visualization

**Kepler.gl Integration:**
- MVT layer configuration
- Dynamic tile loading
- Interactive controls

**Web Interface:**
- Simple map viewer
- Dataset selector
- Filter controls
- Performance metrics display

## Use Cases

**Large Point Dataset Visualization:**
Visualize millions of GPS points, sensor readings, or location data with smooth pan/zoom. Aggregate data dynamically based on zoom level.

**Real-Time Geospatial Analytics:**
Filter and aggregate large datasets on-the-fly. See results instantly as you change filters or zoom levels.

**Urban Planning Data:**
Display building footprints, census data, infrastructure points. Aggregate statistics by region at different zoom levels.

**Environmental Monitoring:**
Visualize sensor networks, weather stations, pollution measurements. Time series animation of environmental changes.

**Network Infrastructure:**
Display network nodes, fiber routes, cell towers. Aggregate coverage or capacity by region.

## Technical Details

### Performance Targets

**Tile Latency:**
- <100ms for tiles with millions of points
- <50ms for typical zoom levels
- <10ms for cached/aggregated tiles

**Data Scale:**
- Support datasets with 10M+ points
- Efficient memory usage (columnar storage)
- Multi-threaded processing

**Throughput:**
- Handle concurrent tile requests
- Async FastAPI for high concurrency
- Rust parallelism for CPU-bound work

### MVT Specification

**Mapbox Vector Tile Format:**
- Protobuf-encoded tiles
- Standard web map compatibility
- Feature properties preserved
- Geometry encoding optimizations

**Tile Coordinates:**
- Standard Z/X/Y tile addressing
- Web Mercator projection (EPSG:3857)
- Zoom levels 0-22 support

### Data Pipeline

```
Dataset (CSV/Parquet)
       ↓
  Polars DataFrame (in-memory)
       ↓
Tile Request (/tiles/z/x/y.mvt)
       ↓
BBox Filter (Polars + Rust)
       ↓
Aggregation (if enabled)
       ↓
MVT Encoding (Rust)
       ↓
Protobuf Response → Kepler.gl
```

## Development Status

**Phase 0 Complete:** Planning and roadmap (100%)

**Phase 1 Pending:** Project foundation (FastAPI + Polars setup)

**Roadmap:** 6 phases defined with clear requirements

**Requirements:** 12 requirements mapped across phases

**Next Steps:**
- Execute Phase 1 (FastAPI setup, health check, Polars integration)
- Plan Phase 2 (Rust/PyO3 coordinate math)
- Begin development

## Comparison

| Feature | Vector Tile Server | Datashader | Tippecanoe | PostGIS Tile Server |
|---------|-------------------|------------|------------|---------------------|
| Dynamic Tiles | On-the-fly | Raster only | Pre-generate | Query-based |
| Performance | <100ms (target) | Fast | N/A (offline) | Slow for large data |
| Data Engine | Polars | Pandas/Dask | N/A | PostgreSQL |
| Aggregation | Yes (in-tile) | Yes | No | Limited |
| Vector Format | MVT (Protobuf) | PNG | MVT | MVT |
| Scale | Millions of points | Billions | Any | Depends on DB |
| Real-Time | Yes | Yes | No | Yes |
| Language | Python + Rust | Python | C++ | SQL + Server |

## Integration

**Kepler.gl:**
Primary visualization client. Add custom MVT layer pointing to tile server endpoint.

**Polars:**
Leverages Polars DataFrame for efficient filtering and aggregation. Columnar storage and multi-threading.

**Rust (PyO3):**
Critical performance paths (coordinate math, MVT encoding) implemented in Rust. Python bindings via PyO3.

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **Related:** Uses similar Rust/Python architecture as [ank-pydantic](ank-pydantic)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Kepler.gl with MVT layer visualization
- Performance benchmarks (latency vs data size)
- FastAPI OpenAPI documentation
- Web interface map viewer
- Tile request/response examples
- Polars DataFrame filtering code
- Rust MVT encoding implementation
- Architecture diagram (FastAPI → Polars → Rust → MVT)
- Comparison with static tiles
- Large dataset aggregation demo
-->
