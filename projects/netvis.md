---
layout: default
section: network-automation
---

# Visualization Engine

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Current Milestone: v1.9 Scale & Export](#current-milestone-v19-scale-export)
- [Previous: v1.8 Temporal & Interaction (Shipped 2026-03-01)](#previous-v18-temporal-interaction-shipped-2026-03-01)
- [Planning Workflow](#planning-workflow)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Ecosystem Context](#ecosystem-context)
- [Current Status](#current-status)

## Concept

Network visualization often fails at scale because layout algorithms treat all nodes and edges equally, producing cluttered "hairball" diagrams. The **Network Visualization Engine** treats topologies as hierarchical structures and uses domain-aware layout constraints—including isometric views and edge bundling—to reflect engineering intent.

As a Rust-based engine, it takes complex multi-layer network topologies and renders them using advanced algorithms that reduce visual complexity while preserving structural clarity. Key features include:
- **Hierarchical Layouts**: Respects the natural structure of network layers.
- **Edge Bundling**: Minimizes crossings and bundles related connections to reduce noise.
- **Multi-Format Output**: Generates static SVG, PDF, and PNG files, with future plans for interactive browser embedding.
- **High Performance**: Optimized for processing massive datasets with sub-second latency.

The goal is to transform topologies into clear, information-dense visualizations that enable engineering insight instead of visual noise.

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.

Transform network topologies into clear, information-dense visualizations using algorithms that minimize edge crossings, bundle related connections, and respect hierarchical/geographic structure — enabling understanding of networks that would otherwise be visual noise.

---

## Architecture

- `petgraph`-backed graph wrapper with typed nodes/edges
- Layout algorithms: force-directed, Sugiyama hierarchical, radial tree
- Multi-layer support with isometric/starburst layouts
- Edge refinement: force-directed edge bundling (FDEB), obstacle-aware routing
- Customizable styling system with type-safe builder pattern

---

## Tech Stack

Rust, petgraph, fjadra (d3-force port), SVG/PDF/PNG rendering, WASM-ready

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current Milestone: v1.9 Scale & Export

**Goal:** Push NetVis to enterprise scale (10K-node topologies in <10s) and add single-file interactive HTML export for offline sharing — while closing v1.8 tech debt.

**Target features:**
- Barnes-Hut O(n log n) force repulsion + Rayon parallelization for 10K-node layouts
- Single-file interactive HTML export (embedded WASM + topology, no external deps)
- Timeline + filter composition gap closure (`netvis timeline --filter-*`)
- `TrafficDirection::Bidirectional` rendering

---

## Previous: v1.8 Temporal & Interaction (Shipped 2026-03-01)

All 4 phases complete (76–79), 10/10 requirements satisfied.

**What shipped:**
- `netvis timeline` — multi-snapshot SVG export with frozen layout + incremental diff SVGs
- `netvis query` — temporal entity history (when did X appear/change/disappear)
- `--filter-type/tag/group/layer` — show/hide topology subsets without re-layout; BFS path highlighting; reusable YAML filter rules
- `src/traffic/` — CSS dot-particle animation from YAML utilization data; NOC color mapping (green/amber/red); play/pause/speed controls in standalone SVG
- `src/annotation/` — text notes + circle/box/arrow callouts anchored to nodes; named layers with `--hide-layers`/`--show-layers`; SVG injection post-processing

**Previous Milestones:**
- v1.8 - Temporal & Interaction 
- v1.7 - Interactive Browser Editor 
- v1.4 - Production Scale & Real-World Integration 
- v1.3 - Embed Readiness & API Stability 
- v1.2 - Visual Polish & Production Hardening 
- v1.1 - Network Analysis & Operations 
- v1.0.0 - Release Preparation

---

## # Validated

All  features from original roadmap:
- ✓ petgraph-based input API for topology definition
- ✓ Isometric multi-layer layout (Physical → L2 → IP → OSPF → iBGP → eBGP stacking)
- ✓ Edge bundling (hierarchical and force-directed bundling algorithms)
- ✓ Bezier edge routing with crossing/collision reduction
- ✓ Starburst/radial layout for containment groups (ASes, data centers, VLANs)
- ✓ Force-directed positioning with weighted edges (peering-aware, using fjadra)
- ✓ Radial tree layout for hierarchical structures
- ✓ Multiple node type support (routers, switches, servers, broadcast domains)
- ✓ Edge weight visualization (line thickness, style differentiation)
- ✓ SVG output
- ✓ PDF output
- ✓ PNG output
- ✓ Configuration API for layout selection and parameters
- ✓ CLI tool with JSON/YAML topology loading

v1.2 Visual Polish & Production Hardening (shipped 2026-02-09):
- ✓ SVG filter infrastructure with signature-based deduplication — v1.2
- ✓ Visual effects (drop shadows, glow, gradients, inner shadows) with semantic guardrails — v1.2
- ✓ WCAG 3:1 non-text contrast enforcement via automated parameter tuning — v1.2
- ✓ High-Contrast theme with AAA (21:1) contrast and redundant emphasis channels — v1.2
- ✓ Label collision avoidance with perpendicular-FIRST edge placement strategy — v1.2
- ✓ Export quality diagnostics for SVG/PNG/PDF material diffs — v1.2

v1.3 Embed Readiness & API Stability (shipped 2026-02-16):
- ✓ Deterministic rendering with golden fixture suite (55 SVG + 8 PNG + 8 PDF baselines) — v1.3
- ✓ Structured diagnostics envelope (v1.0 schema) with JSON/YAML/NDJSON CLI output — v1.3
- ✓ Multi-surface embedding API: contracts::v1 boundary, Rust facade, WASM envelope — v1.3
- ✓ R*-tree spatial label placement with scored candidates and viewport-aware sizing — v1.3
- ✓ CI governance: overlap gate, API drift detection, SemVer checks, versioned JSON Schemas — v1.3
- ✓ Rust SVG quality analyzer with label distance metrics (zero Python dependency) — v1.3

v1.8 Temporal & Interaction (shipped 2026-03-01):
- ✓ `netvis timeline` CLI — snapshot discovery, frozen-layout rendering, incremental diff SVGs — v1.8
- ✓ `netvis query` CLI — temporal entity history (appear/change/disappear) with JSON/table output — v1.8
- ✓ Topology filter pipeline — show/hide by type/tag/group/layer; BFS path highlighting; reusable YAML filter files — v1.8
- ✓ CSS traffic animation — dot particles from YAML utilization data; NOC color mapping; play/pause/speed overlay; standalone SVG — v1.8
- ✓ Annotation markup — text notes + circle/box/arrow callouts; named layers with show/hide; anchor-relative positions survive re-layout — v1.8

---

## # Active

v1.9 Scale & Export:
- [ ] Barnes-Hut spatial indexing for O(n log n) force repulsion (replaces O(n²) all-pairs)
- [ ] Rayon-based parallelization of force simulation inner loop
- [ ] 10K-node layout completes in <10 seconds (validated by benchmark)
- [ ] `netvis export-html` — single-file interactive HTML with embedded WASM + topology data
- [ ] HTML export supports pan/zoom, search, hover tooltips with no external dependencies
- [ ] `netvis timeline` accepts `--filter-type/tag/group/layer` flags
- [ ] `TrafficDirection::Bidirectional` renders dot particles in both directions

---

## # Out of Scope

v1.0 feature development (complete):
- Python bindings — deferred to v1.1+ after release
- Browser/WASM embedding — deferred to v1.1+
- Interactive features (click events, zoom, show/hide) — deferred to v1.1+
- Topology discovery/parsing — users provide topology files
- Real-time animation — static output only

v1.0.0 release scope exclusions:
- Comprehensive library API documentation — CLI-first, defer detailed rustdoc to v1.1
- Examples for Rust library usage — have CLI examples, defer programmatic examples
- Advanced benchmarking (GPU, parallelization) — basic criterion benchmarks only
- Multi-platform CI testing — Linux/macOS only initially

---

## Planning Workflow

**Inbox Processing:**
Before starting milestone planning, review `inbox.md` in the project root for captured feature ideas and tasks. Categorize items as:
- **Current milestone:** Add to active requirements if critical
- **Future milestone:** Reference in out-of-scope or defer to next version
- **Research needed:** Flag for investigation before commitment

This ensures no ideas are lost and provides a backlog for future planning cycles.

---

## Context

**Background:**
This project builds on visualization concepts from academic work on Abstract Network Models, which represent networks across multiple protocol layers (Physical, Layer 2, IP Address, OSPF, iBGP, eBGP) with cross-layer associations. The goal is to make these visualizations programmatically accessible.

**Related project:**
Will eventually integrate with a "Topology Visualisation and Querying" tool (React-based) as an embedded visualization component with bidirectional communication (click events out, highlight commands in). This informs the need to design for browser embedding even though it's not v1 scope.

**Inspiration sources:**
- D3.js radial tree and hierarchical edge bundling
- Datashader/edgebundle hammer bundling algorithm
- Topology Zoo geographic network maps
- Edward Tufte's principles on information density and visual clarity
- fjadra (Rust port of d3-force) for force simulation

**Architecture vision:**
```
[Topology Sources] → [Input/petgraph] → [Core Layout Engine] → [Output/Render]
                                               ↓
                                    Multiple layout algorithms
                                    composable and configurable
```

---

## Constraints

- **Language**: Rust — required for performance of iterative layout algorithms (force-directed convergence, edge bundling optimization)
- **Graph library**: petgraph — well-maintained, performant, good API for network topology representation
- **Force simulation**: fjadra — Rust port of d3-force, WebAssembly-friendly, designed for interactive performance
- **Design philosophy**: Tufte-inspired — maximize information density, minimize chartjunk, clarity over decoration

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Rust for implementation | Iterative algorithms (force-directed, bundling) need performance; future WASM target | ✓ Good (v1.2: 51K LOC, WASM working) |
| petgraph for graph structure | Mature, performant, good Rust ecosystem fit | ✓ Good |
| fjadra for force simulation | d3-force semantics in Rust, WASM-ready, active development | ✓ Good |
| Library-first architecture | Primary use case is programmatic generation, not GUI tool | ✓ Good |
| Static output for v1 | Reduce scope; interactive features layered on later | ✓ Good |
| Defer Python bindings | Get core right first; bindings are mechanical once API is stable | ✓ Good (shipped v1.1) |
| SVG filters over raster post-processing (v1.2) | Maintain vector fidelity, theme-aware, resolution-independent | ✓ Good |
| Tufte-first design philosophy (v1.2) | Effects must enhance information, not decorate | ✓ Good (semantic guardrails prevent chartjunk) |
| Effect budget system >50 elements (v1.2) | Prevent performance cliff from excessive SVG filters | ✓ Good (auto-disable with warnings) |
| Signature-based filter deduplication (v1.2) | Reduce SVG bloat, share identical filter definitions | ✓ Good (O(1) reuse lookup) |
| Quantized EffectParams buckets (v1.2) | Enable WCAG tuning while preserving filter dedup | ✓ Good (0..=10 buckets) |
| WCAG 3:1 automated enforcement (v1.2) | Accessibility compliance without manual tuning | ✓ Good (auto-adjust + numeric warnings) |
| Text-anchor alignment for labels (v1.2) | Break geometric constraint (close + side + no truncation) | ✓ Good (10px spacing vs 150-233px) |
| Perpendicular-FIRST offset strategy (v1.2) | Keep edge labels visually connected while avoiding strokes | ✓ Good (zero overlap warnings) |
| SVG post-processing for traffic/annotation overlays (v1.8) | Inject traffic animation and annotation layers as final SVG transforms — no Scene contamination | ✓ Good (clean pipeline: render → traffic → annotations → write) |
| `TopologyYaml.annotations: Option<Vec<Annotation>>` flat list (v1.8) | Avoid double-nesting (`annotations.annotations:`) in YAML; wrap to `AnnotationConfig` at call site | ✓ Good (natural YAML authoring) |
| WASM-gated file I/O for timeline module (v1.8) | `#![cfg(not(target_arch = "wasm32"))]` on timeline/query — keeps file-system ops off WASM target | ✓ Good (consistent with adapters pattern) |
| Byte-level ISO 8601 date scanning (v1.8) | Avoids regex dependency for snapshot discovery; ISO dates are lexicographically sortable | ✓ Good (zero new deps for timeline) |
| Timeline dispatch before run() (v1.8) | `netvis timeline` dispatches from main() before filter pipeline — consequence: timeline cannot accept  filter flags | ⚠ Revisit (tech debt: timeline+filter composition gap) |

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. netvis provides topology visualization and rendering — the "visualize" stage of the pipeline.

**Role:** Render network topologies as high-quality static output (SVG/PNG/PDF) or interactive visualizations (WASM). Consume topology data from any upstream tool.

**Key integration points:**
- Renders topologies from topogen (YAML), ank-pydantic (JSON), or netflowsim (GeoJSON with stats)
- WASM target enables embedding directly in the workbench browser UI
- Python bindings (PyO3) for programmatic rendering in Python workflows
- Geographic layout mode consumes lat/lon coordinates from topogen's geo module
- Contract-first versioned API (`contracts::v1`) for stable embedding

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities

*Last updated: 2026-03-01 after v1.9 milestone start*

---

## Current Status

2026-03-02 —  complete, smart edge routing implemented.

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
