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

- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [What This Is](#what-this-is)
- [Core Value](#core-value)
- [Current Milestone: v1.9 Scale & Export](#current-milestone-v19-scale-export)
- [Previous: v1.8 Temporal & Interaction (Shipped 2026-03-01)](#previous-v18-temporal-interaction-shipped-2026-03-01)
- [Requirements](#requirements)
- [Planning Workflow](#planning-workflow)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Ecosystem Context](#ecosystem-context)
- [Current Status](#current-status)

## Technical Reports

- [Download Technical Report: paper.pdf](/assets/docs/netvis-paper.pdf)
- [Download Technical Report: techreport.pdf](/assets/docs/netvis-techreport.pdf)

---

## Code Samples

### export_formats.rs

```rs
//! End-to-end export formats example.
//!
//! Demonstrates the complete workflow from graph creation through layout,
//! SVG rendering, and PNG/PDF export using the ExportBuilder API.
//!
//! Output files:
//! - target/export_example.png (Web quality)
//! - target/export_example_print.png (Print quality)
//! - target/export_example.pdf
//!
//! Run with: `cargo run --example export_formats`

use std::fs;
use std::path::Path;

// Import all types from crate root (not from export submodule)
use netvis::{
    EdgeData, ExportBuilder, ForceDirectedLayout, Layout, NetVisGraph, NodeData, PngOptions,
    QualityPreset, RenderOutput, Renderer, SvgRenderer,
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("NetVis Export Formats Example");
    println!("==============================\n");

    // Step 1: Create a simple network graph
    println!("Step 1: Creating network graph...");
    let mut graph = NetVisGraph::new();

    // Create a small network: router -> 2 switches -> 2 servers
    let router = graph.add_node(NodeData::new("router1").node_type("router"));
    let switch1 = graph.add_node(NodeData::new("switch1").node_type("switch"));
    let switch2 = graph.add_node(NodeData::new("switch2").node_type("switch"));
    let server1 = graph.add_node(NodeData::new("server1").node_type("server"));
    let server2 = graph.add_node(NodeData::new("server2").node_type("server"));

    // Connect the network
    graph.add_edge(router, switch1, EdgeData::new(1.0));
    graph.add_edge(router, switch2, EdgeData::new(1.0));
    graph.add_edge(switch1, server1, EdgeData::new(1.0));
    graph.add_edge(switch2, server2, EdgeData::new(1.0));
    graph.add_edge(switch1, switch2, EdgeData::new(0.5)); // Inter-switch link

    println!(
        "  Created graph with {} nodes and {} edges",
        graph.node_count(),
        graph.edge_count()
    );

    // Step 2: Apply force-directed layout
    println!("\nStep 2: Applying force-directed layout...");
    let layout = ForceDirectedLayout::new().seed(42); // Deterministic seed
    let scene = layout.layout(&graph)?;
    println!(
        "  Layout complete. Scene bounds: ({:.1}, {:.1}) to ({:.1}, {:.1})",
        scene.bounds.min.x, scene.bounds.min.y, scene.bounds.max.x, scene.bounds.max.y
    );

    // Step 3: Render to SVG
    println!("\nStep 3: Rendering to SVG...");
    let renderer = SvgRenderer::default();
    let output = renderer.render(&scene, 800.0, 600.0)?;
    let svg_string = match output {
        RenderOutput::String(s) => s,
        RenderOutput::Bytes(_) => panic!("Expected SVG string output"),
    };
    println!("  SVG rendered ({} bytes)", svg_string.len());

    // Ensure target directory exists
    fs::create_dir_all("target")?;

    // Step 4: Export to PNG using QualityPreset::Web (default)
    println!("\nStep 4: Exporting to PNG (Web quality)...");
    let png_web = ExportBuilder::new(&svg_string)
        .preset(QualityPreset::Web)
        .to_png_default()?;

    let web_path = Path::new("target/export_example.png");
    fs::write(web_path, &png_web)?;
    println!("  Saved: {} ({} bytes)", web_path.display(), png_web.len());

    // Step 5: Export to PNG using QualityPreset::Print (higher resolution)
    println!("\nStep 5: Exporting to PNG (Print quality)...");
    let png_print = ExportBuilder::new(&svg_string)
        .preset(QualityPreset::Print)
        .to_png_default()?;

    let print_path = Path::new("target/export_example_print.png");
    fs::write(print_path, &png_print)?;
    println!(
        "  Saved: {} ({} bytes)",
        print_path.display(),
        png_print.len()
    );
    println!(
        "  Print is {:.1}x larger than Web",
        png_print.len() as f64 / png_web.len() as f64
    );

    // Step 6: Export to PNG with explicit options (demonstrating options API)
    println!("\nStep 6: Exporting to PNG with explicit options...");
    let png_custom = ExportBuilder::new(&svg_string)
        .width(1920)
        .height(1080)
        .to_png(PngOptions::default().scale(1.0))?;

    let custom_path = Path::new("target/export_example_custom.png");
    fs::write(custom_path, &png_custom)?;
    println!(
        "  Saved: {} ({} bytes, 1920x1080)",
        custom_path.display(),
        png_custom.len()
    );

    // Step 7: Export to PDF
    println!("\nStep 7: Exporting to PDF...");
    let pdf = ExportBuilder::new(&svg_string)
        .preset(QualityPreset::Print)
        .to_pdf_default()?;

    let pdf_path = Path::new("target/export_example.pdf");
    fs::write(pdf_path, &pdf)?;
    println!("  Saved: {} ({} bytes)", pdf_path.display(), pdf.len());

    println!("\nExport complete!");
    println!("\nOutput files:");
    println!("  - target/export_example.png (Web quality)");
    println!("  - target/export_example_print.png (Print quality)");
    println!("  - target/export_example_custom.png (1920x1080)");
    println!("  - target/export_example.pdf");

    Ok(())
}

```

### profile_5000.rs

```rs
//! Release-mode profiling harness for the 5000-node acceptance pipeline.
//!
//! This example mirrors the end-to-end acceptance benchmark shape:
//! - Deterministic spine-leaf topology with ~5000 nodes
//! - Force-directed layout
//! - SVG render with auto LOD
//!
//! Prints a single parseable timing line for external capture:
//! ```text
//! PROFILE_5000 layout_ms=1234 render_ms=567 total_ms=1801
//! ```
//!
//! Usage:
//! ```bash
//! cargo run --release --example profile_5000
//! ```

use std::time::Instant;

use netvis::traits::{Layout, Renderer};
use netvis::{EdgeData, ForceDirectedLayout, NetVisGraph, NodeData, SvgRenderer};

/// Create a deterministic spine-leaf topology with approximately `n` nodes.
///
/// This is identical to the topology generator used in `benches/end_to_end.rs`
/// to ensure profiling reflects the acceptance benchmark workload.
fn create_spine_leaf(n: usize) -> NetVisGraph {
    let mut graph = NetVisGraph::with_capacity(n, n * 2);
    let mut ids = Vec::with_capacity(n);

    // Create spine layer (roughly sqrt(n)/5 spines, clamped).
    let spine_count = ((n as f64).sqrt() / 5.0).max(2.0) as usize;
    for i in 0..spine_count {
        ids.push(graph.add_node(NodeData::new(format!("spine-{}", i))));
    }

    // Create leaf layer and connect to spines.
    let leaf_count = spine_count * 5;
    for i in 0..leaf_count {
        let leaf_id = graph.add_node(NodeData::new(format!("leaf-{}", i)));
        ids.push(leaf_id);

        // Connect to primary spine.
        let spine_idx = i % spine_count;
        graph.add_edge(ids[spine_idx], leaf_id, EdgeData::default());

        // Connect to adjacent spine for redundancy.
        let alt_spine = (i + 1) % spine_count;
        graph.add_edge(ids[alt_spine], leaf_id, EdgeData::default());
    }

    // Fill remaining nodes as servers.
    let server_start = ids.len();
    let remaining = n.saturating_sub(server_start);
    for i in 0..remaining {
        let server_id = graph.add_node(NodeData::new(format!("srv-{}", i)));
        ids.push(server_id);

        // Connect to a leaf.
        let leaf_idx = spine_count + (i % leaf_count);
        graph.add_edge(ids[leaf_idx], server_id, EdgeData::default());
    }

    graph
}

fn main() {
    // Enable deterministic mode for repeatability.
    let _det = netvis::DeterministicMode::enable();

    let total_start = Instant::now();

    // Build the 5000-node spine-leaf topology.
    let graph = create_spine_leaf(5000);

    // Layout phase.
    let layout_start = Instant::now();
    let layout = ForceDirectedLayout::new();
    let scene = layout.layout(&graph).expect("layout failed");
    let layout_ms = layout_start.elapsed().as_millis() as u64;

    // Render phase with auto LOD (matching acceptance benchmark).
    let render_start = Instant::now();
    let renderer = SvgRenderer::default().with_auto_lod(scene.nodes.len());
    let _svg = renderer
        .render(&scene, 1920.0, 1080.0)
        .expect("render failed");
    let render_ms = render_start.elapsed().as_millis() as u64;

    let total_ms = total_start.elapsed().as_millis() as u64;

    // Print the parseable timing line.
    println!(
        "PROFILE_5000 layout_ms={} render_ms={} total_ms={}",
        layout_ms, render_ms, total_ms
    );
}

```

### quickstart.rs

```rs
use std::path::Path;

use netvis::{EdgeData, ForceDirectedLayout, Layout, NetVisGraph, NodeData, Renderer, SvgRenderer};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Tiny sample graph (6 nodes, 7 edges).
    let mut graph = NetVisGraph::new();

    let r1 = graph.add_node(NodeData::new("r1").node_type("router"));
    let r2 = graph.add_node(NodeData::new("r2").node_type("router"));
    let s1 = graph.add_node(NodeData::new("s1").node_type("switch"));
    let s2 = graph.add_node(NodeData::new("s2").node_type("switch"));
    let h1 = graph.add_node(NodeData::new("h1").node_type("host"));
    let h2 = graph.add_node(NodeData::new("h2").node_type("host"));

    graph.add_edge(r1, s1, EdgeData::new(1.0));
    graph.add_edge(r1, s2, EdgeData::new(1.0));
    graph.add_edge(r2, s1, EdgeData::new(1.0));
    graph.add_edge(r2, s2, EdgeData::new(1.0));
    graph.add_edge(s1, h1, EdgeData::new(1.0));
    graph.add_edge(s2, h2, EdgeData::new(1.0));
    graph.add_edge(s1, s2, EdgeData::new(0.5));

    // Deterministic seed keeps output stable across runs.
    let layout = ForceDirectedLayout::new().seed(42);
    let scene = layout.layout(&graph)?;

    if scene.is_empty() {
        println!("scene: empty (nothing to render)");
        return Ok(());
    }

    std::fs::create_dir_all("target")?;
    let out_path = Path::new("target/quickstart.svg");
    SvgRenderer::default().render_to_file(&scene, 800.0, 600.0, out_path)?;
    println!("svg: {}", out_path.display());

    println!("nodes: {}", graph.node_count());
    println!("edges: {}", graph.edge_count());

    let b = scene.bounds;
    println!(
        "bounds: min=({:.2},{:.2}) max=({:.2},{:.2})",
        b.min.x, b.min.y, b.max.x, b.max.y
    );

    Ok(())
}

```

### research_intersect.rs

```rs
use kurbo::{Line, Point};
use std::time::Instant;

fn segment_intersect(l1: Line, l2: Line) -> Option<Point> {
    let p = l1.crossing_point(l2)?;
    let is_on_segment = |l: Line, pt: Point| -> bool {
        let dx = l.p1.x - l.p0.x;
        let dy = l.p1.y - l.p0.y;
        let len2 = dx * dx + dy * dy;
        if len2 == 0.0 {
            return false;
        }
        let px = pt.x - l.p0.x;
        let py = pt.y - l.p0.y;
        let t = (px * dx + py * dy) / len2;
        (0.0..=1.0).contains(&t)
    };

    if is_on_segment(l1, p) && is_on_segment(l2, p) {
        Some(p)
    } else {
        None
    }
}

fn main() {
    let n = 10_000;
    let mut edges = Vec::with_capacity(n);
    for i in 0..n {
        let x1 = (i as f64) * 0.1;
        let y1 = (i as f64) * 0.2;
        let x2 = x1 + 10.0;
        let y2 = y1 + 5.0;
        edges.push(Line::new(Point::new(x1, y1), Point::new(x2, y2)));
    }

    let start = Instant::now();
    let mut intersections = 0;
    for i in 0..edges.len() {
        for j in i + 1..edges.len() {
            if segment_intersect(edges[i], edges[j]).is_some() {
                intersections += 1;
            }
        }
    }
    let elapsed = start.elapsed();
    println!(
        "Found {} intersections among {} edges in {:?}",
        intersections, n, elapsed
    );
}

```

---

## Visuals

![hero-diagram](/images/hero-diagram.svg)

![hero-diagram.DCMNxwfa](/images/hero-diagram.DCMNxwfa.svg)

![hero-diagram.DCMNxwfa_Z1HYzg2](/images/hero-diagram.DCMNxwfa_Z1HYzg2.svg)

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## What This Is

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.

---

## Core Value

Transform network topologies into clear, information-dense visualizations using algorithms that minimize edge crossings, bundle related connections, and respect hierarchical/geographic structure — enabling understanding of networks that would otherwise be visual noise.

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

## Requirements



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
