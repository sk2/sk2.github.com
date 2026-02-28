---
layout: default
section: network-automation
---

# Network Modeling & Configuration Library

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Current Milestone: v1.12 Production Deployment](#current-milestone-v112-production-deployment)
- [Active Milestones (Parallel Work)](#active-milestones-parallel-work)
- [Planned Milestone: v1.13 Design Validation Framework](#planned-milestone-v113-design-validation-framework)
- [Latest Shipped: v2.0 Ergonomics, Performance & Decoupling (2026-02-24)](#latest-shipped-v20-ergonomics-performance-decoupling-2026-02-24)
- [Previous Shipped: v1.8 Performance & Optimization (2026-02-16)](#previous-shipped-v18-performance-optimization-2026-02-16)
- [Key Decisions](#key-decisions)
- [Context](#context)
- [Constraints](#constraints)
- [Ecosystem Context](#ecosystem-context)
- [Current Status](#current-status)

## Concept

A Python-native configuration engine for defining a network model and compiling it into a consistent, reviewable plan. It solves the 'type safety vs performance' problem by combining the ergonomics of Pydantic models with a fast Rust graph core (NTE).

As one of the two primary modeling tools in the ecosystem, it offers a high-level, developer-friendly interface for building complex network designs. It uses an explicit intermediate representation and transformation passes (design -> plan -> protocol layers) to ensure architectural consistency across the entire topology.

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.

---

## Features

- **Type-Safe Modeling**: Device, interface, and relationship models with strict Pydantic validation.
- **Rust-Backed Operations**: High-performance graph traversals and queries via PyO3 and petgraph.
- **Rich Query API**: Chainable filters and traversals that replace manual graph walking with declarative intent.
- **Multi-Layer Support**: Native modeling of physical, logical, and protocol views within a single graph structure.
- **Multi-Vendor Generation**: Compiles intent into validated configurations for 11+ major networking platforms.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current Milestone: v1.12 Production Deployment

**Goal:** Deploy to real network devices, not just simulators. Real vendor compiler support and deployment workflows.

**Target features:**
- Cisco IOS-XR compiler (industry standard for SP/DC)
- Juniper JunOS compiler (enterprise/SP standard)
- Arista EOS compiler (DC standard)
- ContainerLab exporter (real device testing environment)
- Deployment workflows (push configurations, verify, rollback)

**Status:** Not started (defining requirements)

**Note:** v1.10 and v1.11 are also active in parallel.

---

## Active Milestones (Parallel Work)

**v1.10: Protocol Design Validation & Config Generation** —  complete (phases 72-74 remaining)
- Protocol-specific design rules, FRR compiler, netsim exporter
- Full pipeline: design → validate → compile → simulate

**v1.11: Performance & Ergonomics** — In progress (7/27 plans complete)
- DataFrame caching, query optimization, FFI batching
- Flattened API imports, typed accessors, improved errors

---

## Planned Milestone: v1.13 Design Validation Framework

**Goal:** Comprehensive "linter for network designs" - validation system with rules engine, severity levels, and auto-fix suggestions.

**Target features:**
- Rules engine with severity levels and categories
- Validation hooks in design workflow
- Pre-commit checks for design changes
- Validation reports with actionable fixes
- Plugin system for custom validation rules

---

## Latest Shipped: v2.0 Ergonomics, Performance & Decoupling (2026-02-24)

**Key Achievements (v2.0):**
- Dynamic model registration and fluent connectivity templates
- Proxied `node.data` write-through (including batch-mode safety)
- Rust push-down for string/regex query evaluation with benchmark evidence
- Data Mapper + Identity Map for stable Python object identities
- Advanced analytics surface: centrality, weighted paths (NetworkX fallback), and detached extraction

---

## Previous Shipped: v1.8 Performance & Optimization (2026-02-16)

**Key Achievements (v1.8):**
- Profiling baseline and scale fixtures (10k/100k)
- LadybugDB (Kuzu) evaluated as alternative backend; decision: optimise petgraph
- Backend Abstraction Layer (trait-based TopologyBackend)
- paths_to optimised to <5ms at 10k via Rust-backed neighbour discovery
- LazyFrame-based QuerySpec with early termination
- CI performance gates for automated regression detection

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

<!-- v1.10 Protocol Design Validation & Config Generation ( complete, phases 72-74 remaining) -->

- [ ] FRR compiler end-to-end (interfaces, OSPF, BGP, ISIS, static routes with Jinja2 templates)
- [ ] Netsim environment exporter (device configs, topology description, simulation parameters)
- [ ] Integration: standard ruleset + golden-path example (design → validate → compile → simulate)

<!-- v1.11 Performance & Ergonomics (planned) -->

- [ ] Performance baseline and regression infrastructure (profiling, memory analysis, benchmark suite, CI enforcement)
- [ ] DataFrame caching layer (LRU cache with mutation invalidation, 80- latency reduction)
- [ ] QuerySpec result caching (hash-based query result caching with invalidation)
- [ ] FFI call batching (batch mutation API, reduce 29k → 300 calls, 50- speedup)
- [ ] Flattened public API (from ank_pydantic import Router, q, Topology)
- [ ] Typed field accessors (replace getattr/setattr with node.data.field and node.update_fields())
- [ ] Improved error messages (actionable suggestions, difflib-based recommendations)
- [ ] Documentation and polish (quickstart guide, API reference, performance guide, migration guide)

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
- ~960K LOC Python, Rust backend (ank_nte + nte-query + nte-domain)
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

**Role:** Transform structural topologies into protocol-configured, vendor-specific network designs. Bridge between topology generation (topogen) and simulation/deployment targets (netsim, ContainerLab).

**Key integration points:**
- Consumes topologies from topogen (AutoNetKit YAML export with topology_type, tier, role metadata)
- Depends on ank_nte as Rust graph engine backend
- Exports to netsim (`export_netsim()`) for protocol validation
- Blueprint system (dc-ebgp, wan-ospf, isp-bgp-ospf) adds protocol config to structural topologies
- IP addressing is owned by ank-pydantic, not topogen (Decision D-1)

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities
- [Cross-Project Data Contracts](../../topogen/.planning/ARCHITECTURE.md) — ownership boundaries and format specifications

*Last updated: 2026-02-21 after v1.11 scope definition*

---

## Current Status

2026-02-27 -- Completed 72-05 with canonical fixtures, golden tests, and idempotency validation

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
