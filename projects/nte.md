---
layout: default
---

# Network Topology Engine

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Concept

Graph operations on network topologies demand native performance — Python's NetworkX caps out on large topologies. The Network Topology Engine provides a Rust-native topology engine with Python bindings, giving the Network Modeling & Configuration Library the speed of compiled code with the ergonomics of Python.

### What This Is

The Network Topology Engine is the Rust backend that powers the Network Modeling & Configuration Library's graph operations. Originally embedded within the Network Modeling & Configuration Library as `ank_nte`, it has been extracted into its own repository as the engine matured and its scope grew beyond a simple backing store.

It provides native-speed graph algorithms, query execution, and data storage for network topology operations. It uses `petgraph`'s `StableDiGraph` for topology representation and Polars for columnar data storage.

---

---

---

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

---

---

---

## Tech Stack

Rust, petgraph (StableDiGraph), Polars, DuckDB, PyO3/Maturin for Python bindings

---

[← Back to Network Automation](../network-automation)

---



---

[← Back to Projects](../projects)

---



---

[← Back to Projects](../projects)

---

[← Back to Projects](../projects)
