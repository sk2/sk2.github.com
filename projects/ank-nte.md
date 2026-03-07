---
layout: default
section: network-automation
---

# Network Topology Engine

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span> <span class="stack-badge">Polars</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Architecture](#architecture)
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

## Concept

Rust-based graph topology engine with Python bindings via PyO3. Takes network topologies — nodes, edges, layers, metadata — and stores them in a dual-write architecture: structural graph (petgraph StableDiGraph) plus columnar attribute store (Polars DataFrames). Mutations update both atomically; if either write fails, the transaction rolls back.

The engine backs the [Network Modeling & Configuration Library](/projects/ank-pydantic) and can be consumed directly by other tools in the ecosystem for zero-conversion topology loading.

A 14-crate Cargo workspace with pluggable datastore backends (Polars, DuckDB, Lite), a query engine that compiles filter specs into efficient backend operations, and an HTTP/WebSocket server mode for remote execution.

---

## Code Samples

### Validation policies

```yaml
version: 1
policies:
  - id: "V001"
    category: "attribute"
    severity: "ERROR"
    expr: "attrs.vendor == 'Cisco'"
    message: "Vendor must be Cisco"
    repair_hints:
      - "Set 'vendor' to 'Cisco' in the node metadata"

  - id: "S001"
    category: "structural"
    severity: "WARNING"
    expr: "size(layers) > 0"
    message: "Topology should define at least one layer"
```

<details class="code-collapse">
<summary>Python API example</summary>

```python
import ank_nte

topo = ank_nte.Topology()
topo.add_nodes_with_metadata(
    ids=[1, 2, 3, 4],
    types=["Router", "Router", "Switch", "Switch"],
    layers=["core", "core", "access", "access"],
)

topo.update_node_properties(1, {"vendor": "Cisco", "bandwidth": 40_000})

# Save and load
topo.save("topology.zip")     # ZIP archive with NDJSON
loaded = ank_nte.Topology.load("topology.zip")
```

</details>

---

## Usage

```bash
# Start the NTE server
nte-server --bind 0.0.0.0:8080 --topology topology.zip
```

<details class="code-collapse">
<summary>Creating and persisting a topology</summary>

```python
import ank_nte

# Create and populate a topology
topo = ank_nte.Topology()
topo.add_nodes_with_metadata(
    ids=[1, 2, 3, 4],
    types=["Router", "Router", "Switch", "Switch"],
    layers=["core", "core", "access", "access"],
)

# Save and load
topo.save("topology.zip")
loaded = ank_nte.Topology.load("topology.zip")
```

</details>

---

## Architecture

<div class="mermaid">
flowchart LR
    M[Mutation] --> DWG[DualWriteGuard]
    DWG --> PG[petgraph<br/>Graph Structure]
    DWG --> PL[Polars<br/>Attribute DataFrame]
    PG -.->|rollback on failure| DWG
    PL -.->|rollback on failure| DWG
</div>

**Dual-write model.** Every topology mutation is a paired operation: update the petgraph graph structure *and* update the attribute DataFrame. A RAII `DualWriteGuard` ensures atomicity — if the DataFrame insert fails after the graph was already modified, the graph mutation rolls back automatically. State divergence between the two stores is structurally impossible.

**Stable identity.** Node and edge IDs survive insertions and removals. Internally, the engine maps user-facing external IDs to petgraph's `NodeIndex` via a bidirectional index.

**Columnar attributes.** Node and edge properties live in Polars DataFrames rather than per-node hashmaps. Filtering 10,000 nodes by vendor, layer, or any custom field runs as a vectorized column scan. Schema evolves dynamically — adding a new property to one node extends the column across the DataFrame.

**Pluggable backends.** The `TopologyBackend` trait abstracts the attribute store. Polars is the default (fast filtering, zero-copy access). DuckDB provides SQL-based querying for complex analytics. Lite is an in-memory store for small topologies and testing.

<div class="mermaid">
flowchart TD
    TB[TopologyBackend trait]
    TB --> Polars["Polars<br/><small>Fast filtering, zero-copy</small>"]
    TB --> DuckDB["DuckDB<br/><small>SQL analytics</small>"]
    TB --> Lite["Lite<br/><small>In-memory, testing</small>"]
</div>

**Event sourcing.** A ring-buffer EventStore records every mutation (add node, remove edge, update property) for audit trails and potential replay.

---

## Current Status

v1.0 Engine Hardening in progress. 14-crate workspace, ~126,000 lines of Rust, 1,350 tests.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/ank-nte-techreport.pdf)

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
