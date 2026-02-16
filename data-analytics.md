---
layout: default
---

# Data Analytics & Visualization Ecosystem

Tools for processing massive datasets, discovering patterns in time series, and creating information-dense visualizations that transform raw data into actionable insights.

## Contents
- [The Vision](#the-vision)
- [How They Work Together](#how-they-work-together)
- [The Tools](#the-tools)
  - [Tileserver Polars — Geospatial Analytics at Scale](#tileserver-polars--geospatial-analytics-at-scale)
  - [matrix-profile-rs — Time Series Pattern Discovery](#matrix-profile-rs--time-series-pattern-discovery)
- [Philosophy: Why This Approach?](#philosophy-why-this-approach)
- [Open Source & Contributions](#open-source--contributions)

---

## The Vision

Modern data analysis fragments across disconnected tools: extract data with one tool, analyze with another, visualize with a third. This ecosystem provides an integrated workflow built on Rust and Polars with a focus on three key problems:

1. **Scale**: Process millions of rows interactively, not in overnight batch jobs
2. **Signal**: Find patterns and anomalies automatically, not through manual exploration
3. **Clarity**: Generate visualizations that reveal structure, not just plot points

**Core Philosophy:**
- **Performance without compromise**: Native Rust implementations with Python ergonomics
- **Streaming where possible**: Process data larger than RAM through chunked operations
- **Opinionated defaults**: Tools should work out of the box for common cases
- **Interoperability**: Built on Arrow/Polars for zero-copy data exchange

## How They Work Together

```
┌────────────────────────────────────────────────────────────┐
│              Raw Data Sources                              │
│   (Geospatial · Time Series · Large CSVs · Streams)       │
└────────────┬───────────────────────────┬───────────────────┘
             │                           │
    ┌────────▼─────────┐        ┌────────▼─────────┐
    │ Tileserver Polars│        │ matrix-profile-rs│
    │  (Geospatial)    │        │  (Time Series)   │
    └────────┬─────────┘        └────────┬─────────┘
             │                           │
             └──────────┬────────────────┘
                        │
          ┌─────────────▼──────────────┐
          │   Interactive Frontends    │
          │  (Kepler.gl · Dashboards)  │
          └────────────────────────────┘
```

**Typical Workflow:**
1. **Ingest**: Load massive datasets (geospatial points, time series) into Polars DataFrames
2. **Analyze**: Use matrix-profile-rs for pattern discovery or Tileserver for spatial queries
3. **Visualize**: Render interactive visualizations with sub-second query latency
4. **Iterate**: Refine analysis based on visual feedback without waiting for batch jobs

---

## The Tools

### Tileserver Polars — Geospatial Analytics at Scale

<span class="status-badge status-complete">Phase 7 — Complete</span> · [Full Details →](projects/tileserver)

**What It Is:**
Tile server that renders vector tiles (MVT) from Polars DataFrames for interactive geospatial visualization.

**Key Features:**
- **Polars-native**: Direct DataFrame-to-MVT conversion without intermediate formats
- **Spatial indexing**: R-tree acceleration for fast bounding box queries
- **Adaptive simplification**: Point clustering and line simplification at low zoom levels
- **Sub-second latency**: Typical tile generation in 50-200ms for million-point datasets

**Example Workflow:**

Load data:
```python
import polars as pl
from tileserver_polars import TileServer

# Load massive point dataset
df = pl.read_csv("earthquakes_10M.csv")

# Start tile server
server = TileServer(df, lon_col="longitude", lat_col="latitude")
server.start(port=8080)
```

Configure Kepler.gl:
```javascript
// Add custom tile layer
{
  type: "mvt",
  url: "http://localhost:8080/tiles/{z}/{x}/{y}.mvt",
  renderSubLayers: true
}
```

Query dynamically:
```python
# Filter by magnitude on the fly
server.set_filter(pl.col("magnitude") > 5.0)
# Tiles regenerate automatically with filtered data
```

**Performance:**
- **10M points**: 800ms full-extent render
- **1M points in viewport**: 120ms tile generation
- **Streaming CSV**: Process 100M rows in 5GB chunks

**Use Cases:**
- **Urban planning**: Visualize 50M building footprints with attribute filtering
- **IoT analytics**: Map 100M+ sensor readings updated in real-time
- **Logistics**: Interactive route visualization for million-delivery datasets
- **Environmental monitoring**: Render gridded climate data as point layers

**Current Status:** Production-ready for point geometries, adding polygon/line support.

**Tech Stack:** Rust, Polars, protobuf for MVT encoding, Actix-web for HTTP

---

### matrix-profile-rs — Time Series Pattern Discovery

<span class="status-badge status-active">Phase 2/5 (16%)</span> · [Full Details →](projects/matrix-time-series)

**What It Is:**
A Rust implementation of Matrix Profile algorithms for time series analysis. Automatically discovers repeating patterns (motifs) and anomalies (discords) in univariate time series without domain knowledge or parameter tuning.

**The Problem:**
Time series analysis traditionally requires:
- **Domain expertise**: Know what patterns to look for in advance
- **Manual exploration**: Try different techniques until something works
- **Slow tools**: Python libraries with JIT warmup and poor performance
- **Awkward APIs**: Low-level array manipulation instead of high-level operations

**The Solution:**
Matrix Profiles provide a universal representation:
- **Motif discovery**: "This sensor pattern repeated 15 times before failure"
- **Anomaly detection**: "This heartbeat segment is unlike any other"
- **Similarity search**: "Find all sequences matching this known pattern"
- **No parameters**: Works on any univariate time series automatically

**Key Features:**
- **Multiple algorithms**:
  - STOMP: Exact computation with QT recurrence
  - SCAMP: Parallel exact algorithm for multi-core CPUs
  - SCRIMP++ (planned): Anytime algorithm for progressive refinement
- **Clean API**: `.motifs(k=3)` instead of manual array indexing
- **Polars integration** (Phase 5): `df.select(pl.col("ts").mp.stomp(m=20))`
- **Native performance**: 100x faster than Python equivalents

**Example: Predictive Maintenance**

Input time series (vibration sensor):
```rust
use matrix_profile::{MatrixProfile, stomp};

// Load sensor data
let vibration_data: Vec<f64> = load_sensor_readings();

// Compute matrix profile (window size: 100 samples)
let mp = stomp(&vibration_data, 100)?;

// Find top 3 repeating patterns
let motifs = mp.motifs(3)?;
for (rank, motif) in motifs.iter().enumerate() {
    println!("Motif {}: occurs at indices {:?}",
             rank + 1, motif.occurrences);
    println!("  Distance: {:.4}", motif.distance);
}

// Find top 3 anomalies
let discords = mp.discords(3)?;
for (rank, discord) in discords.iter().enumerate() {
    println!("Anomaly {}: at index {}",
             rank + 1, discord.index);
    println!("  Severity: {:.4}", discord.distance);
}
```

Output:
```
Motif 1: occurs at indices [1234, 2456, 3678, 4890, ...]
  Distance: 0.0234
Motif 2: occurs at indices [890, 1890, 2890]
  Distance: 0.0456

Anomaly 1: at index 5432
  Severity: 12.3456
Anomaly 2: at index 7890
  Severity: 11.2345
```

Interpretation:
- **Motif 1**: Degradation pattern that appears multiple times (pre-failure signature)
- **Anomaly 1**: Unusual vibration spike (investigate further)

**Polars Integration (Planned):**
```python
import polars as pl

df = pl.read_csv("sensor_data.csv")

# Compute matrix profile as DataFrame operation
result = df.with_columns([
    pl.col("vibration").mp.stomp(window=100).alias("mp_distance"),
    pl.col("vibration").mp.motifs(k=3).alias("top_motifs"),
    pl.col("vibration").mp.discords(k=3).alias("anomalies")
])
```

**Performance Targets:**
- **N=10⁴ samples**: < 100ms
- **N=10⁵ samples**: < 5s
- **N=10⁶ samples**: < 2 minutes (with parallelization)

**Use Cases:**
- **Predictive maintenance**: Find degradation patterns in sensor data
- **Healthcare**: Detect irregular heartbeat or movement patterns
- **Finance**: Discover recurring market microstructures
- **Operations**: Identify anomalous system behavior for alerting

**Current Status:** Phase 2 (Discovery Ergonomics) - building high-level APIs for motif/discord extraction.

**Tech Stack:** Rust, ndarray, rayon for parallelization, PyO3 for Python bindings

---

## Philosophy: Why This Approach?

### Performance Enables Interactivity
Sub-second query latency transforms the analysis workflow. Instead of "run batch job, wait, inspect results, adjust, repeat," you get "adjust filter, see results immediately." This tight feedback loop enables exploratory analysis that's impossible with slow tools.

### Rust + Polars for the Data Layer
Polars provides:
- **Zero-copy operations**: No serialization overhead between tools
- **Streaming execution**: Process data larger than RAM
- **Expression API**: Write `pl.col("x") > 5` instead of manual loops
- **Native speed**: Rust implementation without Python GIL limitations

### Algorithms, Not Heuristics
Matrix Profiles are mathematically sound—they *guarantee* finding the true nearest neighbor for every subsequence. This eliminates "tune epsilon until it looks right" parameter hell common in clustering/anomaly detection.

### Composable Tools
Each tool solves one problem well:
- **Tileserver**: Geospatial visualization at scale
- **matrix-profile-rs**: Time series pattern discovery
- **Polars**: Underlying data engine

Use the full stack or just the pieces you need. All built on Arrow for interoperability.

---

## Open Source & Contributions

Active development, contributions welcome:

- **Tileserver Polars**: [github.com/sk2/tileserver-polars](https://github.com/sk2/tileserver-polars)
- **matrix-profile-rs**: [github.com/sk2/matrix-profile-rs](https://github.com/sk2/matrix-profile-rs)

---

[← Back to Projects](projects) | [View CV](cv) | [Network Automation](network-automation) | [Signal Processing](signal-processing) | [Agentic Systems](agentic-systems)

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
.status-planning {
  background-color: #ffc107;
  color: #343a40;
}
.status-complete {
  background-color: #28a745;
  color: white;
}
</style>
