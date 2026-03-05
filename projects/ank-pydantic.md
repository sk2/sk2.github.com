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

## Contents

- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Visuals](#visuals)
- [What This Is](#what-this-is)
- [Core Value](#core-value)
- [Current Milestone: v2.2 Polish & Developer Experience](#current-milestone-v22-polish-developer-experience)
- [Previous Milestone: Realignment and Cleanup (Post-netc Split)](#previous-milestone-realignment-and-cleanup-post-netc-split)
- [Latest Shipped: v2.1 Advanced Python Features (2026-02-28)](#latest-shipped-v21-advanced-python-features-2026-02-28)
- [Previous Shipped](#previous-shipped)
- [Requirements](#requirements)
- [Key Decisions](#key-decisions)
- [Context](#context)
- [Constraints](#constraints)
- [Ecosystem Context](#ecosystem-context)
- [Current Status](#current-status)

## Technical Reports

- [Download Technical Report: ank-techreport.pdf](/assets/docs/ank-pydantic-ank-techreport.pdf)

---

## Code Samples

### README.md

```markdown
# Examples

Example topologies demonstrating ank-pydantic usage patterns.

This directory contains a mix of:
- Schema-based YAML examples (recommended): load via `Topology.from_yaml()`
- Legacy role-based YAML examples: kept for reference

## Contents

| Example | Description |
|---------|-------------|
| `house_network/` | Schema-based YAML example with custom models + type mappings |
| `vlans/` | VLAN topology (legacy role-based YAML format) |
| `two_hosts/` | Minimal topology (legacy role-based YAML format) |
| `monte_carlo_reliability/` | Monte Carlo reliability example (Python module) |
| `themes/` | Theme configuration files used by rendering examples |

## Usage

### Quick start (schema-based YAML)

From the repo root, load the `house_network` schema-based topology:

```python
from pathlib import Path

from [ank_pydantic](../ank_pydantic) import Topology
from examples.house_network.models import (
    EDGE_TYPE_MAPPING,
    NODE_TYPE_MAPPING,
    EthernetInterface,
    Host,
    Router,
)

topology = Topology.from_yaml(
    Path("examples/house_network/house_topology.yaml"),
    type_mapping=NODE_TYPE_MAPPING,
    edge_type_mapping=EDGE_TYPE_MAPPING,
)

nodes = topology.get_node_models()

print("Routers:", sum(isinstance(n, Router) for n in nodes))
print("Hosts:", sum(isinstance(n, Host) for n in nodes))
print("Interfaces:", sum(isinstance(n, EthernetInterface) for n in nodes))
```

Expected output:

```text
Routers: 1
Hosts: 3
Interfaces: 9
```

```

---

## Visuals

![5_10](/images/5_10.png)

![5_8](/images/5_8.png)

![5_9](/images/5_9.png)

![figure_4_43](/images/figure_4_43.png)

![figure_6_2](/images/figure_6_2.png)

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## What This Is

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`[ank_nte](../ank_nte)`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

---

## Core Value

A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.

---

## Current Milestone: v2.2 Polish & Developer Experience

**Goal:** Clear accumulated technical debt, improve developer experience via better examples and case studies, and complete architectural cleanup started in v1.3.

**Target features:**
- ARCH-01: topology.py reduced to <400 lines by moving remaining methods to managers
- ARCH-02: `packages/ank_pydantic_extras/` analyzed with each component assigned a documented path
- EXMP-01/02: `batteries_included/` module with sample topologies (datacenter, WAN, campus) and example models/compilers
- EXMP-03/04: All 6 case studies updated to current Query API; all TODO markers resolved
- API-01/02: Design functions exposed as fluent Query methods; blueprints/ design rules use Query API
- DEBT-01/02/03: mypy overload errors, Rust warnings, and NTE workarounds cleaned up

**Status:** In progress (defining requirements)

---

## Previous Milestone: Realignment and Cleanup (Post-netc Split)

**Goal:** Clean up the repository and realign the focus of `[ank_pydantic](../ank_pydantic)` as the "Community Frontend" (Python API) for modeling, rapid prototyping, and hacking, acknowledging that the rigid compiler and "linter" functionality has moved to the `netc` Rust project.

**Status:** Completed

---

## Latest Shipped: v2.1 Advanced Python Features (2026-02-28)

**Key Achievements (v2.1):**
- Intelligent design engine with automated attribute allocation
- Semantic topology diffing with collision reporting
- Remote topology parity with real-time sync (events, offline replay)
- Declarative validation engine with repair hints

---

## Previous Shipped

**v2.0 Ergonomics, Performance & Decoupling (2026-02-24):**
- Dynamic model registration and fluent connectivity templates
- Proxied `node.data` write-through (including batch-mode safety)
- Rust push-down for string/regex query evaluation with benchmark evidence
- Data Mapper + Identity Map for stable Python object identities
- Advanced analytics surface: centrality, weighted paths (NetworkX fallback), and detached extraction

**v1.10 Protocol Design & Config Generation (2026-02-28):**
- Protocol design rules (ISIS/BGP, OSPF, overlay/service, infrastructure)
- FRR compiler with template-based config generation
- Multi-vendor template development (IOS-XR, JunOS, EOS)
- Netsim environment exporter for simulation workflows
- Integration golden path (design → validate → compile → simulate)
- Performance infrastructure with DataFrame and QuerySpec caching

**v1.8 Performance & Optimization (2026-02-16):**

**Key Achievements (v1.8):**
- Profiling baseline and scale fixtures (10k/100k)
- LadybugDB (Kuzu) evaluated as alternative backend; decision: optimise petgraph
- Backend Abstraction Layer (trait-based TopologyBackend)
- paths_to optimised to <5ms at 10k via Rust-backed neighbour discovery
- LazyFrame-based QuerySpec with early termination
- CI performance gates for automated regression detection

---

## Requirements



---

## # Validated

<!-- Shipped and working -->

**v1.8 Performance & Optimization (2026-02-16):**
- ✓ PERF-01..04: Profiling infrastructure, benchmark harness, performance baseline, memory profiling at 10k+ — v1.8
- ✓ BACK-01: LadybugDB evaluated with real workloads (decision: optimise petgraph) — v1.8
- ✓ BACK-02: Backend abstraction layer (TopologyBackend trait, NteBackend, BackendStack) — v1.8
- ✓ QOPT-01: paths_to regression resolved (<5ms at 10k nodes) — v1.8
- ✓ QOPT-02: CI performance regression detection (pytest-benchmark gates) — v1.8
- ✓ QOPT-04: Query plan optimisation (LazyFrame pipeline, filter reordering, early termination) — v1.8
- ✓ SCALE-01: 10k+ node validation complete — v1.8
- ~ QOPT-03: Materialised view cache (1.28x vs 100x target; Rust access needed) — v1.8 partial

**v1.5 API Ergonomics & Polish (2026-02-03):**
- ✓ QUERY-06 to QUERY-10: Query API completion (traversal, sorting, between queries) — v1.5
- ✓ MUT-01 to MUT-03: Mutation ergonomics (cascade delete with DeletionPlan, batch operations) — v1.5
- ✓ API-01 to API-04: API consistency (q.field migration, ids/models migration, parameter ordering) — v1.5
- ✓ CODE-01 to CODE-03: Code consolidation (dead code removal, pattern validation) — v1.5
- ✓ Blueprint designs migrated to declarative Query API — v1.5

**v1.7 API Usability & Ergonomics (2026-02-09):**
- ✓ COPY-01 to COPY-04: Layer copy ergonomics (explicit collision policies, CopyResult with mappings, lineage queries, endpoint/link semantics) — v1.7
- ✓ TRAV-01 to TRAV-04: Traversal ergonomics (safe bounds defaults, explicit directionality, deterministic ordering, output format shaping) — v1.7
- ✓ IO-01 to IO-04: I/O workflow ergonomics (round-trip contracts, PathLike support, type mapping hooks, ID mapping exposure) — v1.7
- ✓ BP-01 to BP-04: Blueprint ergonomics (idempotent re-runs, validation hooks with fail-fast/collect, canonical primitives, script/function equivalence) — v1.7
- ✓ TYPE-01 to TYPE-04: Type ergonomics (query type narrowing with Generic[T_co], minimized Any leakage via .pyi stubs, reduced typing pain points, actionable runtime errors) — v1.7

**v1.6 Documentation & Adoption (+ Gap Closure) (2026-02-05):**
- ✓ MkDocs documentation site using Diataxis structure with strict builds
- ✓ Tested documentation examples in CI (Sybil + docstring doctests allowlist)
- ✓ Domain examples + case studies + versioned docs (mike) + linkcheck harness

**v1.4 Native Foundation (2026-02-01):**
- ✓ RUST-01 to RUST-07: Rust domain structs (Node, Link, Endpoint) with behavior methods — v1.4
- ✓ PYINT-01 to PYINT-06: Python write-through integration via Pydantic models — v1.4
- ✓ QUERY-01 to QUERY-05: Query API consolidation to single path — v1.4
- ✓ FIX-01 to FIX-04: NTE bug fixes (endpoint corruption, node update, cache removal) — v1.4
- ✓ ARCH-01 to ARCH-04: Architecture cleanup (nte-domain crate, managers as thin coordinators) — v1.4

**v1.3 Whiteboard-to-Blueprint (2026-01-31):**
- ✓ TYPE-01: Base Device class that Router, Switch, etc. derive from — v1.3
- ✓ TYPE-02: Query for Device type returns routers and switches — v1.3
- ✓ TYPE-03: Pydantic mechanics support type inheritance in queries — v1.3
- ✓ TYPE-04: Blueprint can contain elements for multiple layers — v1.3
- ✓ Two-stage transformation: Whiteboard → Plan → Protocol Layers — v1.3
- ✓ Rust query engine (nte-query) with QuerySpec DTO pattern — v1.3
- ✓ Manager-first API facade (Topology.py <400 lines) — v1.3

**v1.2 Foundations Extraction (2026-01-27):**
- ✓ FEXT-01: Created blueprints/ module structure (models/, designs/, compilers/, environments/, rules/, topologies/) — v1.2
- ✓ FEXT-02: Moved domain models to blueprints/models/ — v1.2
- ✓ FEXT-03: Moved design functions to blueprints/designs/ — v1.2
- ✓ FEXT-04: Moved compilers to blueprints/compilers/ — v1.2
- ✓ FEXT-05: Created example topologies in blueprints/topologies/ — v1.2
- ✓ FEXT-06: Clean break (no deprecation shims) — v1.2
- ✓ FEXT-07: Updated all internal imports — v1.2
- ✓ FEXT-08: Updated documentation with new import patterns — v1.2

**v1.1 Batteries-Included (2026-01-25):**
- ✓ XFRM-01: Complete transform.split() operation — v1.1
- ✓ XFRM-02: Complete transform.explode() operation — v1.1
- ✓ XFRM-03: Complete where_same()/where_different() query filters — v1.1
- ✓ XFRM-04: Complete transform.remove_where_same() mutation — v1.1
- ✓ HELP-01: allocate_loopbacks() helper function — v1.1
- ✓ HELP-02: allocate_p2p_addresses() helper function — v1.1
- ✓ DEMO-01: 5+ Query API feature demonstrations (6 demos) — v1.1

**v1.0 API Polish (2026-01-24):**
- ✓ MAPI-01 to MAPI-05: Standardized manager API methods — v1.0
- ✓ QAPI-01 to QAPI-09: Query API as primary interface with rich operators — v1.0
- ✓ DEPR-01 to DEPR-06: All deprecated code cleanup — v1.0
- ✓ LAYR-01 to LAYR-04: Layer system polish — v1.0

**Pre-existing:**
- ✓ Create topologies with typed Pydantic node/edge models
- ✓ Register custom node types with schema flattening
- ✓ Add, retrieve, and remove nodes/edges by ID
- ✓ Query nodes with lazy, composable Query API
- ✓ Multi-layer topology support
- ✓ Rust-backed graph store for performance

---

## # Active

<!-- v2.2 Polish & Developer Experience -->

**Architecture & Cleanup:**
- ARCH-01: topology.py <400 lines (move remaining methods to managers)
- ARCH-02: `ank_pydantic_extras/` components assigned documented paths (integrate / split / deprecate)

**Examples & Documentation:**
- EXMP-01: `batteries_included/` module with sample topologies for 3 scenarios (datacenter, WAN, campus)
- EXMP-02: `batteries_included/` example models and compilers users can study and extend
- EXMP-03: All 6 case studies updated to current Query API (zero `.dataframe()` calls, no `topology.match()`)
- EXMP-04: All TODO markers in case studies resolved (addressed, deleted, or deferred with rationale)

**API Ergonomics:**
- API-01: Design functions (split, explode) exposed as fluent methods on Query results
- API-02: Design rule implementations in `blueprints/` use Query API instead of imperative for-loops

**Technical Debt:**
- DEBT-01: `overload-cannot-match` mypy errors fixed in NodeManager and EndpointManager `add()` methods
- DEBT-02: Rust diagnostic warnings eliminated (deprecated `add_edge`, dead code in sampler.rs, benchmark harness)
- DEBT-03: NTE workarounds documented with clear comments and upstream issue references

---

## # Out of Scope

<!-- Explicitly deferred -->

- Module consolidation / file sprawl cleanup — deferred to v1.5
- Hostname generation (`generate_hostnames()`) — deferred from v1.1
- ank_pydantic_extras package — separate future package for advanced features
- I/O operations polish (GraphML, YAML, NetworkX) — future milestone
- Visualization and rendering — future milestone
- API server (FastAPI) — future milestone
- TUI (Textual) — future milestone
- External documentation — after API stabilizes

---

## Key Decisions

| ID | Decision | Rationale | Outcome |
|----|----------|-----------|---------|
| [DEC-009](codebase/DECISIONS.md#dec-009-safe-to-risky-progression-for-migrations) | Safe-to-risky progression | Migration before removal, low-risk naming before high-risk layer changes | ✓ Good |
| [DEC-005](codebase/DECISIONS.md#dec-005-q-module-namespace) | q module as namespace | Follows Polars pl.col() pattern for expression building | ✓ Good |
| [DEC-006](codebase/DECISIONS.md#dec-006-immutable-accessor-pattern) | Immutable accessor pattern | of_type() returns new instance, enables composition | ✓ Good |
| [DEC-015](codebase/DECISIONS.md#dec-015-endpoint-parent-caching) | Endpoint parent caching | Workaround for NTE create_link() corruption bug | ✓ Resolved v1.4 |
| [DEC-008](codebase/DECISIONS.md#dec-008-batteries-stay-in-package) | Batteries stay in package | Not separate ank_pydantic_extras; extras is for future advanced features | ✓ Good |
| DEC-016 | Clean break over deprecation shims | Simpler codebase, immediate error if wrong import used | ✓ Good |
| DEC-017 | Manager-first API facade | Methods on managers not Topology; smaller core, clearer ownership | ✓ Good |
| DEC-018 | Rust query execution via DTO | Python builds QuerySpec, Rust executes; type-safe FFI boundary | ✓ Good |

*Full decision records with context and consequences: [codebase/DECISIONS.md](codebase/DECISIONS.md)*

---

## Context

**Codebase state (v1.8):**
- ~960K LOC Python, Rust backend ([ank_nte](../ank_nte) + nte-query + nte-domain)
- blueprints/ module with domain models organised by type
- Manager-first API: Topology delegates to specialised managers
- **Rust-first architecture**: CoreTopology is single source of truth
- **Write-through**: Python mutations automatically persist to Rust via `__setattr__`
- **Query API complete**: Sorting, between queries, graph traversal (reachable_from, within_hops_of, paths_to)
- **Performance**: paths_to <5ms at 10k nodes, LazyFrame executor, CI perf gates
- **Backend abstraction**: TopologyBackend trait with NteBackend + BackendStack selection
- **Hydration**: Rust structs converted to Pydantic models via NodeHydrator

**Known tech debt:**
- LinkQuery.models() not yet migrated to Rust hydration (deferred from v1.4)
- Performance regression 25- vs DataFrame path (acceptable tradeoff)
- mypy overload-cannot-match errors in managers

**Architectural Notes (from design discussions):**

*Caching, Transactions & Event Sourcing:*
- Mutation caching layer avoids rebuilding Polars structures on every change
- Flush cache before queries (CQRS pattern — commands and queries separated)
- Implicit transactions (start on first mutation, commit on query)
- Explicit transactions for multi-user scenarios with user locking
- Replicas need caching to avoid churn from every event
- Deep clone for dry runs: clone topology with event log off, run commands, verify, then apply
- Real-time topologies should limit update frequency (e.g., 100ms)
- Stream processing use cases should use dedicated stream processor
- Event emission for real-time subscribers (separate from Polars source)

*Network Topology Engine (NTE) Core Architecture:*
- Rust layer data model: Links, endpoints, nodes, internal nodes as structs
- Return structs from topology, mapped to Python objects (not raw petgraph nodes/edges)
- Use `into` trait for type mapping where possible
- Pydantic for schema definition (not direct model usage)
- Support YAML, TOML via schema; optional `_topology` parameter when added
- Hijack `__setattr__` on base model to write through to Rust
- Hydration approach preferred over on-the-fly retrieval

*Edge & Relationship Handling:*
- Bonded edges: dependencies across different layers
- Shared link groups, bidirectional edge handling
- Edge ID for bidirectional edges
- Store multi-parent relationships in separate lookup table (not graph operations)
- Consider Cypher-based model approaches for complex relationships

*Graph Querying Strategies:*
- Prefer petgraph traversal over Polars adjacency matrices
- Adjacency matrices cause O(n²) column explosion — not suited for Polars
- Use Polars for advanced filtering, petgraph for graph algorithms
- Query flow: graph query → results to Polars → filter by properties → continue

*Path Query Optimization:*
- Find all paths between node types, then post-filter
- Pass allowed/denied node sets (whichever is smaller)
- Fast-fail on denied nodes during iteration
- Parallelizable: paths are independent, deny/allow lists are immutable
- Custom iterator with reference to allow/deny sets
- Consider graph masking to limit traversal to specific layers

*Concurrency & Locking:*
- Modification lock on topology during queries or mutations
- Prevents race conditions when query informs subsequent mutation
- Single-user implicit; explicit locks for multi-user
- May expand to operation-overlap checking if lock becomes bottleneck

*Performance vs Complexity Trade-offs:*
- Avoid premature optimization
- Keep query logic trimmed down initially
- Enterprise features (HA, multi-user transactions) could be separate offering
- Skeletons in open source, fleshed out in enterprise version

*Sources: Recording 9 2, Recording 10 2 (from INBOX.md architectural notes)*

---

## Constraints

- **Backward compatibility**: Changes should not break existing internal usage without clear migration path
- **Rust boundary**: v1.4 is expanding the Rust boundary — Python API should become thinner, not thicker
- **Performance**: API changes must not degrade query/traversal performance
- **One obvious way**: Query API consolidation should result in a single clear path, not additional options

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. ank-pydantic provides network modeling and configuration generation — the "model" stage of the pipeline.

**Role:** Transform structural topologies into protocol-configured, vendor-specific network designs. Bridge between topology generation ([topogen](../topogen)) and simulation/deployment targets ([netsim](../netsim), ContainerLab).

**Key integration points:**
- Consumes topologies from [topogen](../topogen) (AutoNetKit YAML export with topology_type, tier, role metadata)
- Depends on [ank_nte](../ank_nte) as Rust graph engine backend
- Exports to [netsim](../netsim) (`export_netsim()`) for protocol validation
- Blueprint system (dc-ebgp, wan-ospf, isp-bgp-ospf) adds protocol config to structural topologies
- IP addressing is owned by ank-pydantic, not [topogen](../topogen) (Decision D-1)

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities
- [Cross-Project Data Contracts](../../topogen/.planning/ARCHITECTURE.md) — ownership boundaries and format specifications

*Last updated: 2026-02-28 starting milestone v2.2 Polish & Developer Experience*

---

## Current Status

2026-03-01 —  executed (batteries_included module: datacenter, WAN, campus, ISP topologies)

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
