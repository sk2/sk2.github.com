---
layout: default
---

# Network Topology Engine

<span class="status-badge status-active">Stable</span>

[← Back to Network Automation](../network-automation)

---

## The Insight

Graph operations on network topologies demand native performance — Python's NetworkX caps out on large topologies. NTE provides a Rust-native topology engine with Python bindings, giving ank_pydantic the speed of compiled code with the ergonomics of Python.

## Quick Facts

| | |
|---|---|
| **Status** | Stable — extracted as standalone project |
| **Language** | Rust (with PyO3 Python bindings) |
| **Architecture** | Workspace of specialized crates |

---

## What This Is

NTE (Network Topology Engine) is the Rust backend that powers ank_pydantic's graph operations. Originally embedded within ank_pydantic as `ank_nte`, it has been extracted into its own repository as the engine matured and its scope grew beyond a simple backing store.

NTE provides high-performance graph algorithms, query execution, and data storage for network topology operations. It uses `petgraph`'s `StableDiGraph` for topology representation and Polars for columnar data storage.

## Why It Was Split Out

As ank_pydantic evolved, the Rust core grew into a substantial system with its own architectural concerns:

- **Multiple storage backends** (Polars, DuckDB, Lite) requiring independent testing
- **Distributed compute support** via `nte-server` and `nte-backend`
- **Monte Carlo simulation** capabilities in `nte-monte-carlo`
- **Independent release cadence** — Rust compilation and Python wheel builds benefit from isolation

Separating NTE enables independent versioning, faster CI, and clearer ownership boundaries.

## Architecture

NTE is organized as a Cargo workspace with specialized crates:

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

NTE supports pluggable storage through the `nte-datastore-*` crates:

- **Polars** (`nte-datastore-polars`) — Primary backend. Columnar storage for efficient analytical queries over node/edge attributes.
- **DuckDB** (`nte-datastore-duckdb`) — SQL-based backend for complex analytical queries, joins, and aggregations. Useful when topology data needs to be correlated with external datasets.
- **Lite** (`nte-datastore-lite`) — Lightweight in-memory backend for small topologies and testing.

## Integration with ank_pydantic

ank_pydantic imports NTE as a Python package built with Maturin/PyO3. All graph mutations and queries flow through NTE's Rust engine:

```
ank_pydantic (Python API)
    │
    ▼
NTE Python bindings (PyO3)
    │
    ▼
nte-query → nte-core → nte-datastore-*
```

Python users interact with ank_pydantic's Pydantic models. NTE handles the performance-critical work underneath.

## Tech Stack

Rust, petgraph (StableDiGraph), Polars, DuckDB, PyO3/Maturin for Python bindings

---

[← Back to Network Automation](../network-automation)
