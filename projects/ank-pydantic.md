---
layout: default
section: network-automation
---

# Network Modeling & Configuration Library

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [Usage](#usage)
- [Architecture](#architecture)
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

## Concept

The Network Modeling & Configuration Library represents network topologies as typed Python objects backed by a Rust graph engine. You define nodes, edges, and layers using Pydantic models. The library stores them in the [Network Topology Engine](/projects/ank-nte) and exposes a composable query API that builds lazy evaluation plans in Python and executes them in Rust.

The core abstraction is a two-stage transformation: Whiteboard (sketch the topology) to Plan (assign protocols and addresses) to Protocol Layers (ISIS, MPLS, EVPN, L3VPN). Each stage produces a typed, queryable topology. Mutations write through to Rust automatically via `__setattr__` interception on Pydantic base models.

The library ships with domain models for common protocol stacks in its `blueprints/` module: ISIS underlay, MPLS transport, EVPN overlay, BGP peering, and hierarchical IP allocation. These are composable building blocks, not monolithic templates.

---

## Code Samples

### Loading a topology from YAML

```python
from pathlib import Path
from ank_pydantic import Topology
from examples.house_network.models import (
    EDGE_TYPE_MAPPING, NODE_TYPE_MAPPING,
    EthernetInterface, Host, Router,
)

topology = Topology.from_yaml(
    Path("examples/house_network/house_topology.yaml"),
    type_mapping=NODE_TYPE_MAPPING,
    edge_type_mapping=EDGE_TYPE_MAPPING,
)

nodes = topology.get_node_models()
print("Routers:", sum(isinstance(n, Router) for n in nodes))
print("Hosts:", sum(isinstance(n, Host) for n in nodes))
```

<details class="code-collapse">
<summary>Querying with the fluent API</summary>

```python
from ank_pydantic import q

# Find all core routers with Cisco vendor
core_cisco = topology.query(
    q.field("layer") == "core",
    q.field("vendor") == "Cisco",
)

# Traverse neighbors within 2 hops
neighbors = topology.within_hops_of(node_id=1, hops=2)
```

</details>

---

## Visuals

![Topology visualization](/images/5_10.png)

![Layer hierarchy](/images/figure_4_43.png)

![Protocol stack](/images/figure_6_2.png)

---

## Usage

<details class="code-collapse">
<summary>Creating a topology from scratch</summary>

```python
from ank_pydantic import Topology

# Create from scratch
topo = Topology()
topo.add_router("r1", vendor="Cisco", layer="core")
topo.add_router("r2", vendor="Arista", layer="access")
topo.add_link("r1", "r2", bandwidth=10_000)

# Apply protocol blueprint
from ank_pydantic.blueprints import isis_underlay
isis_underlay.apply(topo, area="49.0001")

# Export for simulation
topo.export_netsim("topology.yaml")
```

</details>

---

## Architecture

The system has three layers:

**Python API** — Pydantic models define the schema for nodes, endpoints, and edges. A manager-first facade keeps `Topology` small (under 400 lines); specialised managers handle nodes, edges, links, layers, and ancestors. The query API follows Polars conventions: `q.field()` expressions, lazy evaluation, and method chaining.

**Rust Engine (NTE)** — The [Network Topology Engine](/projects/ank-nte) stores the graph in petgraph, executes queries via a `QuerySpec` DTO passed across the FFI boundary, and handles traversal algorithms (reachable_from, within_hops_of, paths_to). Neighbour discovery runs at under 5ms for 10,000-node topologies.

**Hydration Layer** — Rust structs are converted back to Pydantic models via `NodeHydrator`. An Identity Map ensures stable Python object references across queries. Write-through keeps Rust and Python in sync without explicit save calls.

<div class="mermaid">
block-beta
    columns 1
    block:python["Python API"]
        columns 3
        A["Pydantic Models"] B["Managers"] C["q.field() Queries"]
    end
    block:ffi["Hydration Layer"]
        columns 3
        D["QuerySpec DTO"] E["Write-through"] F["Identity Map"]
    end
    block:rust["Rust Engine (NTE)"]
        columns 3
        G["petgraph"] H["Polars DataFrames"] I["Traversal Algorithms"]
    end
    python --> ffi --> rust
</div>

---

## Current Status

v2.2 Polish & Developer Experience in progress. Previous: v2.1 Advanced Python Features shipped 2026-02-28.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/ank-pydantic-techreport.pdf)

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
