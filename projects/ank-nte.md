---
layout: default
section: network-automation
---

# Network Topology Engine

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span> <span class="stack-badge">Polars</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Query API](#query-api)
- [Policy Validation](#policy-validation)
- [Visuals](#visuals)
- [Usage](#usage)
- [Status](#status)
- [Technical Reports](#technical-reports)

## Concept

Rust-based graph topology engine with Python bindings via PyO3. Takes network topologies — nodes, edges, layers, metadata — and stores them in a dual-write architecture: structural graph (petgraph StableDiGraph) plus columnar attribute store (Polars DataFrames). Mutations update both atomically; if either write fails, the transaction rolls back.

The engine backs the [Network Modeling & Configuration Library](ank-pydantic) and can be consumed directly by other tools in the ecosystem for zero-conversion topology loading.

A 14-crate Cargo workspace with pluggable datastore backends (Polars, DuckDB, Lite), a query engine that compiles filter specs into efficient backend operations, and an HTTP/WebSocket server mode for remote execution.

---

## Architecture

**Dual-write model.** Every topology mutation is a paired operation: update the petgraph graph structure *and* update the attribute DataFrame. A RAII `DualWriteGuard` ensures atomicity — if the DataFrame insert fails after the graph was already modified, the graph mutation rolls back automatically. State divergence between the two stores is structurally impossible.

**Stable identity.** Node and edge IDs survive insertions and removals. This matters for long-lived topologies where you add and remove devices over time — references to existing nodes stay valid. Internally, the engine maps user-facing external IDs to petgraph's `NodeIndex` via a bidirectional index.

**Columnar attributes.** Node and edge properties live in Polars DataFrames rather than per-node hashmaps. This means filtering 10,000 nodes by vendor, layer, or any custom field runs as a vectorized column scan rather than iterating node-by-node. Schema evolves dynamically — adding a new property to one node extends the column across the DataFrame.

**Pluggable backends.** The `TopologyBackend` trait abstracts the attribute store. Polars is the default (fast filtering, zero-copy access). DuckDB provides SQL-based querying for complex analytics. Lite is an in-memory store for small topologies and testing.

**Event sourcing.** A ring-buffer EventStore records every mutation (add node, remove edge, update property) for audit trails and potential replay.

---

## Query API

The query API uses a Polars-inspired fluent builder pattern. Queries are immutable — deriving a filtered subset returns a new query without modifying the original.

```python
from ank_nte import Topology
from src.query import Expr, QueryNamespace

t = Topology()
q = QueryNamespace(t)

# Filter by type and layer
core_routers = q.nodes().of_type("Router").in_layer("core")
print("Core routers:", core_routers.ids())

# Expression-based filtering
high_bw = q.nodes().filter(Expr.field("bandwidth") > 10_000)
spines = q.nodes().filter(
    (Expr.field("role") == "spine")
    & Expr.field("label").contains("dc1")
)

# Link queries between node sets
cross_links = q.links().between([1, 2], [4, 5])

# Composable: derive from a base query without modifying it
routers = q.nodes().of_type("Router")
edge_routers = routers.in_layer("edge")    # routers is unchanged
core_routers = routers.in_layer("core")    # still unchanged
```

The expression DSL supports comparison operators, string operations (`contains`, `startswith`, `matches`), null checks, membership testing (`is_in`), arithmetic, and compound boolean expressions with `&`, `|`, `~`.

---

## Policy Validation

Declarative policy rules validate topology attributes and structure before deployment:

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

Policies run as pre-commit checks — structural and attribute violations surface before the topology is committed to the datastore.

---

## Visuals

![Query builder output](/images/5_8.png)
*Node and edge filtering with the fluent query API.*

![Topology structure](/images/5_9.png)
*Graph structure with layered node groups.*

![Datastore view](/images/5_10.png)
*Columnar attribute store showing node properties across a topology.*

---

## Usage

```python
import ank_nte

# Create and populate a topology
topo = ank_nte.Topology()
topo.add_nodes_with_metadata(
    ids=[1, 2, 3, 4],
    types=["Router", "Router", "Switch", "Switch"],
    layers=["core", "core", "access", "access"],
)

# Update properties
topo.update_node_properties(1, {"vendor": "Cisco", "bandwidth": 40_000})

# Save and load
topo.save("topology.zip")     # ZIP archive with NDJSON
loaded = ank_nte.Topology.load("topology.zip")
```

**Server mode** runs the engine as an HTTP/WebSocket service for remote topology operations:

```bash
# Start the NTE server
nte-server --bind 0.0.0.0:8080 --topology topology.zip
```

---

## Status

**Current**: v1.0 Engine Hardening — structured logging (Rust-Python bridge), domain-specific Python exceptions, GIL release for O(N) operations, CI/CD pipeline.

**Completed:**
- Zero-copy mmap CSR serialization and traversal (March 2026)
- Dual-write safety with RAII rollback guard
- Pluggable backends (Polars, DuckDB, Lite)
- Fluent query API with expression DSL
- Event sourcing and mutation tracking
- Topology archive save/load (ZIP + NDJSON)
- Axum HTTP/WebSocket server

14-crate Cargo workspace. 10,000+ lines of Rust.

---

## Technical Reports

- [Download Technical Report: nte-techreport.pdf](/assets/docs/ank-nte-nte-techreport.pdf)

---

[← Back to Projects](../projects)
