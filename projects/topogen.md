---
layout: default
section: network-automation
---

# Topology Generator

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Technical Depth](#technical-depth)
- [Current Milestone: v1.5 - Intent-Based Overlays & Schematic Enrichment](#current-milestone-v15-intent-based-overlays-schematic-enrichment)
- [Next Milestone Goals](#next-milestone-goals)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Ecosystem Context](#ecosystem-context)

## Concept

A Rust-based topology generation engine that consolidates complex network graph algorithms into a unified, high-performance library. It enables the creation of realistic, validated network structures ranging from small lab setups to massive data center and backbone environments.

A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters. Outputs custom YAML format for use across the network engineering tool ecosystem.

Network engineers can quickly generate realistic, validated network topologies without implementing complex algorithms from scratch.

---

## Features

- **Data Center Patterns**: Generate leaf-spine and fat-tree topologies with realistic tier ratios and oversubscription parameters.
- **WAN & Backbone Models**: Create ring, mesh, POP-based, and hierarchical structures based on real-world ISP patterns.
- **Random Graph Models**: Support for Barabási-Albert (scale-free) and Watts-Strogatz (small-world) algorithms for research and scale testing.
- **Traffic Matrix Generation**: Automatically produce demand matrices using gravity models and distance-based weighting.

---

## Technical Depth

The engine is implemented in Rust for maximum performance, allowing for the sub-second generation of 10,000+ node graphs. It exports a standardized YAML format that is consumed across the entire ANK ecosystem, ensuring structural consistency from design to simulation.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current Milestone: v1.5 - Intent-Based Overlays & Schematic Enrichment

**Goal:** Transform topologies from simple graphs into rich semantic models by formalizing intent-based "overlays" and hierarchical design patterns.

**Target features:**
- **Multi-Overlay Tagging**: Formalize `BGP`, `OSPF`, and `Physical` overlay properties on nodes/edges.
- **Intent-Based Role Assignment**: Automatically tag roles (`spine`/`leaf`, `p`/`pe`/`rr`, `provider`/`customer`) in all generators.
- **Schematic Grouping**: Formalize "Site", "Pod", and "Zone" hierarchies to support downstream visual grouping.
- **Relationship Intent**: Tag edges with semantic relationships (`peering`, `upstream`, `transit`) and `SRLG` (fate-sharing) intent.
- **Whiteboard-Level Property Mapping**: Ensure property names and structures align with AutoNetKit (ANK) whiteboard expectations.

---

## Next Milestone Goals

- Define v1.1 requirements (fresh `.planning/REQUIREMENTS.md`)
- Execute v1.1 Perf+Stability milestone

---

## # Validated

**v1.0-alpha :**
- ✓ Generate data center topologies (fat-tree, leaf-spine) — v1.0-alpha
- ✓ Generate WAN/backbone topologies (ring, mesh, hierarchical) — v1.0-alpha
- ✓ Generate random graph topologies (Erdős-Rényi, Barabási-Albert, Watts-Strogatz) — v1.0-alpha
- ✓ Output custom YAML format with nodes, edges, interfaces, and attributes — v1.0-alpha
- ✓ YAML format stores interfaces under nodes (not edge-centric) — v1.0-alpha
- ✓ Python bindings for programmatic topology generation — v1.0-alpha
- ✓ Validate generated topologies (structural correctness) — v1.0-alpha
- ✓ Validate graph properties (degree distribution, clustering, diameter) — v1.0-alpha
- ✓ Validate design pattern compliance (topology-specific rules) — v1.0-alpha
- ✓ Realistic parameters (bandwidth, latency appropriate for DC vs WAN) — v1.0-alpha
- ✓ Topologies follow network design best practices — v1.0-alpha

**v0.9 :**
- ✓ CLI tool for command-line topology generation — v0.9
- ✓ Config file driven generation (YAML/TOML input) — v0.9
- ✓ Vendor-specific interface naming conventions — v0.9
- ✓ Example topology gallery with sample configs — v0.9
- ✓ Algorithm documentation with parameter guidance — v0.9
- ✓ Typed Python exception hierarchy for better error handling — v0.9
- ✓ Installation guide and quickstart tutorial — v0.9
- ✓ Complete user documentation (CLI, Python API, config files) — v0.9
- ✓ Technical documentation with algorithm formulations and complexity analysis — v0.9
- ✓ Enhanced CLI help text with parameter ranges and examples — v0.9
- ✓ Shell completions for bash, zsh, and fish — v0.9
- ✓ Improved error messages with JSON diagnostics — v0.9
- ✓ Cross-interface parity tests and consistency validation — v0.9

**v0.10 :**
- ✓ Expose Erdos-Renyi generator via CLI, config, and Python API — v0.10
- ✓ Integrate topology-specific structural validators into validation flows — v0.10
- ✓ Complete .10

---

## # Active

**v1.1 Perf+Stability:**
- [ ] Improve large-topology performance across generators, validation, and exporters
- [ ] Add stable performance regression coverage (non-flaky, budgeted)
- [ ] Reduce memory spikes in large runs (generation + export)
- [ ] Improve CLI-level predictability for large workflows (clear limits, consistent diagnostics)

---

## # Deferred / Tech Debt

- Stderr/diagnostics contract consistency: make "stderr empty on success" true everywhere; migrate remaining ad-hoc stderr output into structured warning/reporting.

---

## # Out of Scope

- GNN-based topology generation — Future: graph neural network based generation (research-heavy)
- AutoNetKit loop-back integration — Future: use AutoNetKit itself to generate multi-layer topologies
- Interactive visualization — Handled by separate visualization tool in ecosystem
- Real-time topology updates — Future: dynamic topology modification APIs
- Topology diff/merge — Future: version control for topology configs

---

## Context

**Consolidation:** Topology generation code currently exists in three separate places:
- AutoNetKit (graph-based topology generation)
- Simulation engine (topology setup for network simulation)
- Visualization tool (topology generation for network diagrams)

This tool unifies that logic into a single, high-performance library.

**Integration:** Will likely become a dependency or part of the AutoNetKit workflow engine in the future. Designed to be the "whiteboard view" that other tools build from.

**Architecture Model:** Following AutoNetKit's "whiteboard" concept - one graph with annotations where interfaces are stored under nodes in the YAML format rather than edge-centric representation. This is more extensible than classical graph interchange formats.

**Users:**
- Primary: Network engineers who need realistic topologies for testing, validation, and simulation
- Secondary: Research community (though they often have their own methodologies)
- Internal: The tool ecosystem (AutoNetKit, simulation engine, visualization tools)

**Inspirations:**
- NetworkX AS-level graph generation
- Topology Zoo examples
- Network design best practices and patterns
- ContainerLab YAML format (but defining our own optimized structure)

---

## Constraints

- **Tech Stack - Core**: Rust for performance (fast generation of large topologies) and cross-platform binary distribution
- **Tech Stack - Bindings**: Python bindings required for integration with existing Python-based tools in the ecosystem
- **Output Format**: Custom YAML format (not constrained to existing formats, can design ideal structure)

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Rust core + Python bindings | Performance for large topology generation + cross-platform binary, while maintaining Python integration for existing tool ecosystem | ✓ Good - PyO3 FFI works well, maturin build smooth |
| Custom YAML format for v1 | Design ideal format for this use case, build converters to other formats (ContainerLab, AutoNetKit) later | ✓ Good - Interface-centric model proved extensible |
| Interfaces under nodes (not edge-centric) | Following AutoNetKit whiteboard model - more extensible than classical graph formats for network topologies with device types, interface naming, future BGP sessions/VPNs | ✓ Good - More natural for network topology use cases |
| All three interfaces (CLI, Python API, config-driven) | Maximum flexibility - engineers want CLI for quick generation, Python API for workflow integration, config files for complex/repeatable setups | ✓ Good - Parity tests ensure consistency |
| Documentation-first for v0.9 | Focus on making existing functionality discoverable rather than adding new features | ✓ Good - mdBook + doc-tests prevent drift |
| InterfaceSpec source-of-truth | Centralized parameter metadata prevents interface drift | ✓ Good - Parity tests validate automatically |

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. topogen provides topology generation — the "generate" stage of the pipeline.

**Role:** Generate realistic, validated network topologies with vendor naming, geographic placement, and traffic matrices. Feed topologies into ank-pydantic (modeling), netsim (simulation), netflowsim (traffic analysis), and netvis (visualization).

**Key integration points:**
- Exports to ank-pydantic via AutoNetKit YAML (with topology_type, tier, role, region metadata)
- Exports to netsim directly (netsim YAML with device/wire/traffic structure)
- Exports to ContainerLab YAML for lab deployment
- Traffic matrix (CSV/JSON) feeds netflowsim
- GeoJSON export for geographic visualization in netvis

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities
- [Cross-Project Data Contracts](ARCHITECTURE.md) — ownership boundaries and format specifications

*Last updated: 2026-02-21 after v1.1 milestone start*

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
