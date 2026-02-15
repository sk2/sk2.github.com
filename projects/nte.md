---
layout: default
section: network-automation
---

# Network Topology Engine

<span class="status-badge status-active">Stable</span>

[← Back to Network Automation](../network-automation)

---

## The Insight

Graph operations on network topologies demand native performance — Python's NetworkX caps out on large topologies. The Network Topology Engine provides a Rust-native topology engine with Python bindings, giving the Topology Modeling Library the speed of compiled code with the ergonomics of Python.

## Quick Facts

| | |
|---|---|
| **Status** | Stable — extracted as standalone project |
| **Language** | Rust (with PyO3 Python bindings) |
| **Architecture** | Workspace of specialized crates |

---

## What This Is

The Network Topology Engine is the Rust backend that powers the Topology Modeling Library's graph operations. Originally embedded within the Topology Modeling Library as `ank_nte`, it has been extracted into its own repository as the engine matured and its scope grew beyond a simple backing store.

It provides high-performance graph algorithms, query execution, and data storage for network topology operations. It uses `petgraph`'s `StableDiGraph` for topology representation and Polars for columnar data storage.

## Why It Was Split Out

As the Topology Modeling Library evolved, the Rust core grew into a substantial system with its own architectural concerns:

- **Multiple storage backends** (Polars, DuckDB, Lite) requiring independent testing
- **Distributed compute support** via `nte-server` and `nte-backend`
- **Monte Carlo simulation** capabilities in `nte-monte-carlo`
- **Independent release cadence** — Rust compilation and Python wheel builds benefit from isolation

Separating the Network Topology Engine enables independent versioning, faster CI, and clearer ownership boundaries.

## Architecture

The Network Topology Engine is organized as a Cargo workspace with specialized crates:

| Crate | Purpose |
|-------|---------|
| **nte-core** | Graph topology primitives, node/edge types |
| **nte-query** | Query engine for composable topology queries |
| **nte-domain** | Network domain models (protocols, devices) |
| **nte-backend** | Backend abstraction layer |
| **nte-datastore-polars** | Polars-backed columnar storage |
| **nte-datastore-duckdb** | DuckDB storage backend |
| **nte-datastore-lite** | Lightweight in-memory backend |
| **nte-server** | Distributed computation support |
| **nte-monte-carlo** | Monte Carlo simulation engine |

## Query Engine (nte-query)

The `nte-query` crate provides a composable query API that executes against the topology graph. Queries are built as chains of filter, select, and aggregate operations that compile down to efficient graph traversals:

- **Node/edge filtering** by attribute predicates (role, type, layer membership)
- **Path queries** — shortest path, all paths, constrained walks
- **Aggregation** — count, group-by, statistical summaries over topology subsets
- **Lazy evaluation** — queries build an execution plan, only materializing results on `.collect()`

Queries execute in Rust and return results to Python via PyO3, avoiding the overhead of Python-side graph traversal.

## Storage Backends

The Network Topology Engine supports pluggable storage through the `nte-datastore-*` crates:

- **Polars** (`nte-datastore-polars`) — Primary backend. Columnar storage for efficient analytical queries over node/edge attributes.
- **DuckDB** (`nte-datastore-duckdb`) — SQL-based backend for complex analytical queries, joins, and aggregations. Useful when topology data needs to be correlated with external datasets.
- **Lite** (`nte-datastore-lite`) — Lightweight in-memory backend for small topologies and testing.
- **LadybugDB** (Potential) — Under evaluation as an embedded analytical database backend, offering fast columnar queries with a smaller footprint than DuckDB.

## Integration with the Topology Modeling Library

The Topology Modeling Library imports the Network Topology Engine as a Python package built with Maturin/PyO3. All graph mutations and queries flow through the engine's Rust core:

```
Topology Modeling Library (Python API)
    │
    ▼
NTE Python bindings (PyO3)
    │
    ▼
nte-query → nte-core → nte-datastore-*
```

Python users interact with the Topology Modeling Library's Pydantic models. The Network Topology Engine handles the performance-critical work underneath.

## Tech Stack

Rust, petgraph (StableDiGraph), Polars, DuckDB, PyO3/Maturin for Python bindings

---

[← Back to Network Automation](../network-automation)
