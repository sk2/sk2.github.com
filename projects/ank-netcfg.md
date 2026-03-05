---
layout: default
section: network-automation
---

# Network Configuration Framework

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Technical Depth](#technical-depth)
- [Current Milestone: v1.3 Advanced Topology & Production Readiness](#current-milestone-v13-advanced-topology-production-readiness)
- [Current State (v1.2 Front & Back Ends — shipped)](#current-state-v12-front-back-ends-shipped)
- [Key Decisions](#key-decisions)
- [Constraints](#constraints)

## Concept

A modern, type-safe configuration engine that serves as a successor and sibling to the original AutoNetkit research. It implements the same 'Whiteboard -> Plan -> Build' transformation model but utilizes a modern, schema-enforced pipeline to ensure configuration correctness across heterogeneous network fleets.

Deterministic, auditable, CI/CD-friendly Rust CLI for compiling declarative YAML network blueprints into vendor-neutral configuration artifacts. The `netcfg` binary orchestrates: blueprint parsing → topology transformation → DeviceIR generation → template rendering → traceable config file emission.

Single-binary network compiler: design, transform, and generate configs from YAML blueprints without Python.

---

## Technical Depth

Sitting alongside the core ANK toolchain, ank_netcfg focuses on the high-fidelity transformation of network intent into vendor-specific device states. It provides the protocol-level intelligence needed to generate consistent OSPF, BGP, and MPLS configurations while maintaining strict type safety via a Pydantic-based model layer.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current Milestone: v1.3 Advanced Topology & Production Readiness

**Goal:** Elevate the compiler to production readiness by introducing advanced primitives (route reflectors, edge cloning), an auditable state validation mode, rigorous benchmarking, and decoupling repository dependencies for crate publication.

**Target features:**
- Advanced Primitives — `mesh_nodes` partial meshes and `build_protocol_layer` overlay edge cloning
- State Validation — `netcfg validate` mode enforcing addressing plans without mutation
- Performance & Publishing — `criterion` benchmarking suites and `ank_nte` repository absorption/decoupling

---

## Current State (v1.2 Front & Back Ends — shipped)

The front and back ends of the compiler are fully functional end-to-end:
- **** (The Rendering Engine): Vendor-specific config synthesis via MiniJinja template loading and `data_json` injection.
- **** (The CLI Application): Core `netcfg plan` and `netcfg generate` commands orchestrating the full pipeline and writing `.cfg` artifacts.
- **** (Rich Terminal Diagnostics): `miette`-powered source-snippet error reporting for blueprint validation and IP pool exhaustion.

**Known tech debt (v1.3):**
- Path dependency on `ank_nte` prevents standalone crate publication
- Benchmarks for large topologies (10,000+ nodes) are missing
- `edge_properties` in `mesh_nodes` remains deferred

---

## # Active (v1.3)

- [ ] Partial Meshes (hub-and-spoke/route reflectors) (MESH-V2-01)
- [ ] Overlay Edge Cloning (PROT-V2-01)
- [ ] State Validation Mode: `netcfg validate` (IPAM-V2-01)
- [ ] Addressing Plan Enforcement (IPAM-V2-02)
- [ ] Benchmarking suites for Diff/Render engines (PERF-01)
- [ ] Repository Decoupling of `ank_nte` (PUB-01)

---

## # Deferred (v2.0+)

- IPv6 pool support (IPAM-V2-03)
- Interface name derivation in `mesh_nodes` (MESH-V2-02)
- LSP server (`nte-lsp`) integration (LSP-01)

---

## # Validated (v1.0 - v1.2)

- ✓ Mapping DSL to populate stanza-based `DeviceIR` models
- ✓ Native template rendering via MiniJinja
- ✓ Strict data lineage
- ✓ Declarative YAML Graph Blueprints
- ✓ Stateful diff engine
- ✓ Single-binary capability
- ✓ Cross-phase integration
- ✓ `build_protocol_layer` implemented
- ✓ `provision_ips` implemented
- ✓ `mesh_nodes` implemented
- ✓ CLI `plan` and `generate`
- ✓ `miette` terminal diagnostics

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| `Topology::from_core()` wrapper bridges `CoreTopology` into Evaluator | Evaluator tightly coupled to Python-wrapper type; wrapping at phase boundary is cleanest | ✓ Good |
| `NamedTempFile::new_in(parent)` for transactional output | Same-filesystem guarantee enables atomic POSIX rename | ✓ Good |
| Clap 4 `Args` wrapper struct (`ConfigCommand`) containing `Subcommand` enum | Matches Clap 4 nested subcommand pattern, consistent with `BlueprintCommand` | ✓ Good |
| `RenderEngine::render_node` per-node API | Clean separation between transformation and configuration generation | ✓ Good |
| `miette` for diagnostic reporting | Provides out-of-the-box snippet and span highlighting for YAML errors | ✓ Good |

---

## Constraints

- Rust stable only — no nightly features
- British English in all documentation
- GSD workflow for phase-based planning

*Last updated: 2026-03-01 after v1.2 Front & Back Ends milestone*

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
