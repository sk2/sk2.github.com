---
layout: default
section: network-automation
---

# Network Modeling & Configuration Library

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

The Network Modeling & Configuration Library represents network topologies as typed Python objects backed by a Rust graph engine. You define nodes, edges, and layers using Pydantic models. The library stores them in a Rust-native topology engine (`ank_nte`) and exposes a composable query API that builds lazy evaluation plans in Python and executes them in Rust.

The core abstraction is a two-stage transformation: Whiteboard (sketch the topology) to Plan (assign protocols and addresses) to Protocol Layers (ISIS, MPLS, EVPN, L3VPN). Each stage produces a typed, queryable topology. Mutations write through to Rust automatically via `__setattr__` interception on Pydantic base models.

The library ships with domain models for common protocol stacks in its `blueprints/` module: ISIS underlay, MPLS transport, EVPN overlay, BGP peering, and hierarchical IP allocation. These are composable building blocks, not monolithic templates.

---

## Architecture

The system has three layers:

**Python API** -- Pydantic models define the schema for nodes, endpoints, and edges. A manager-first facade keeps `Topology` small (under 400 lines); specialised managers handle nodes, edges, links, layers, and ancestors. The query API follows Polars conventions: `q.field()` expressions, lazy evaluation, and method chaining.

**Rust Engine (NTE)** -- The Network Topology Engine stores the graph in petgraph, executes queries via a `QuerySpec` DTO passed across the FFI boundary, and handles traversal algorithms (reachable_from, within_hops_of, paths_to). Neighbour discovery runs at under 5ms for 10,000-node topologies.

**Hydration Layer** -- Rust structs are converted back to Pydantic models via `NodeHydrator`. An Identity Map ensures stable Python object references across queries. Write-through keeps Rust and Python in sync without explicit save calls.

```
┌─────────────────────────────────────────┐
│  Python: Pydantic Models + Query API    │
│  (Topology, Managers, q.field())        │
├─────────────────────────────────────────┤
│  FFI: QuerySpec DTO + Write-through     │
├─────────────────────────────────────────┤
│  Rust: petgraph + Polars DataFrames     │
│  (NTE, nte-query, nte-domain)           │
└─────────────────────────────────────────┘
```

---

## Model Hierarchy

```
BaseTopologyNode
├── Router (vendor, model, asn)
├── Switch (endpoints, speed)
└── Host (os)

BaseTopologyEndpoint
└── EthernetInterface (speed, ip)

BaseInternodeEdge
└── EthernetConnection
```

Topologies are defined in YAML using the `TopologySchema` format, or built programmatically by registering models and adding nodes.

---

## Usage

### Loading a topology from YAML

```python
from pathlib import Path
from ank_pydantic import Topology
from examples.house_network.models import (
    NODE_TYPE_MAPPING,
    EDGE_TYPE_MAPPING,
    Router,
    Host,
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

### Building a topology with protocol layers

```python
from ank_pydantic import Topology
from ank_pydantic.blueprints.designs.isis import build_isis_layer
from ank_pydantic.blueprints.designs.mpls import build_mpls_layer
from ank_pydantic.blueprints.designs.evpn import build_evpn_layer

topo = Topology()
topo.nodes.register_models([Router, Interface])
topo.edges.register_models([Link])

# Build physical layer, then stack protocols
build_isis_layer(topo, level=2, area="49.0001",
                 parent_layer="physical", layer_name="isis_dc")
build_mpls_layer(topo, igp_layer="isis_dc", layer_name="mpls_dc")
build_evpn_layer(topo, site="DC1",
                 parent_layer="mpls_dc", layer_name="evpn_dc")
```

### Querying

```python
from ank_pydantic import q

# Find all spine routers, sorted by loopback address
spines = (
    topo.query.nodes()
    .of_type(Router)
    .in_layer("physical")
    .where(role="spine")
    .sort(by="loopback")
    .models()
)

# Cross-set link queries
spine_set = topo.query.nodes().of_type(Router).where(role="spine")
leaf_set = topo.query.nodes().of_type(Router).where(role="leaf")
links = topo.query.links().in_layer("physical").between(spine_set, leaf_set)
```

---

## Visuals

![5_10](/images/5_10.png)

![5_8](/images/5_8.png)

![figure_4_43](/images/figure_4_43.png)

![figure_6_2](/images/figure_6_2.png)

---

## Status

**Current version: v2.1** (released 2026-02-28)

v2.1 added automated attribute allocation in the design engine, semantic topology diffing with collision reporting, remote topology sync with event replay, and a declarative validation engine with repair hints.

**v2.0** (2026-02-24) introduced dynamic model registration, fluent connectivity templates, proxied write-through with batch-mode safety, and Rust push-down for string and regex query evaluation.

**v1.10** (2026-02-28) shipped protocol design rules (ISIS, BGP, OSPF), an FRR compiler with template-based config generation, multi-vendor template support (IOS-XR, JunOS, EOS), and a netsim environment exporter.

**v1.8** (2026-02-16) established profiling infrastructure at 10k/100k scale, optimised `paths_to` to under 5ms, introduced LazyFrame-based query plans with early termination, and added CI performance gates.

**Next milestone: v2.2** -- Architecture cleanup, developer experience improvements, and updated case studies.

---

## Technical Reports

- [Download Technical Report: ank-techreport.pdf](/assets/docs/ank-pydantic-ank-techreport.pdf)

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
