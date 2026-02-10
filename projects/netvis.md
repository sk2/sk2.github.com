---
layout: default
---

# NetVis

<span class="status-badge status-complete">Production Ready</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Production ready - all 10 phases complete |
| **Language** | Rust |
| **Tests** | 582 (554 unit + 28 integration) |
| **Started** | 2025 |
| **License** | MIT/Apache-2.0 |

---

## Overview

NetVis is a library-first network topology visualization engine for Rust. It transforms network topologies represented as graphs into renderer-friendly scenes using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical structure.

## Problem It Solves

Network engineers need to visualize complex topologies to understand structure, identify issues, and communicate designs. Existing tools either:
- Require manual node placement (tedious, doesn't scale)
- Use simplistic layouts that produce cluttered diagrams
- Lack programmatic access for automated workflows

NetVis provides high-quality automated layouts with a clean Rust API.

## Architecture

**Core Design:** Layout algorithms produce `Scene` (geometry), renderers consume `Scene` (output format). This separation enables clean composition and multiple output formats.

**Key Modules:**
- **Graph Core** (`src/graph/`): petgraph wrapper with typed nodes/edges
- **Layouts** (`src/layout/`): Force-directed, hierarchical, radial tree, multi-layer
- **Scene** (`src/geometry/scene/`): Intermediate representation with positioned shapes
- **Rendering** (`src/rendering/`): SVG renderer with styling support
- **Export** (`src/export/`): PNG/PDF export with quality presets
- **Config** (`src/config/`): Type-safe configuration builder and layout dispatcher
- **CLI** (`src/bin/netvis.rs`): Command-line tool

## Features

### Layout Algorithms

**Force-Directed:** Physics-based simulation treating edges as springs and nodes as charged particles. Good for general-purpose layouts.

**Sugiyama Hierarchical:** Layered layout for directed graphs. Minimizes edge crossings and respects flow direction.

**Radial Tree:** Circular layout with root at center and children arranged in concentric rings. Good for tree-structured topologies.

**Multi-Layer:** Isometric and starburst layouts for topologies with explicit layer/group structure (e.g., data center spine-leaf).

### Edge Refinement

**Force-Directed Edge Bundling (FDEB):** Groups related edges together to reduce visual clutter in dense graphs.

**Obstacle-Aware Routing:** Routes edges around nodes to improve readability.

### Rendering & Export

**SVG:** Vector output with customizable styling system
**PNG:** Raster export with quality presets
**PDF:** Publication-ready vector export
**CLI:** Quick visualization from YAML/JSON topology files

### Configuration

Type-safe builder pattern with error hints. Layout parameters can be tuned for specific topology characteristics.

## Usage Examples

### Library API

```rust
use netvis::prelude::*;

// Create graph
let mut graph = NetVisGraph::new();
let a = graph.add_node(NodeData::new("Server A"));
let b = graph.add_node(NodeData::new("Server B"));
graph.add_edge(a, b, EdgeData::default());

// Layout and render
let scene = ForceDirectedLayout::new().layout(&graph)?;
let svg = SvgRenderer::default().render(&scene, 800.0, 600.0)?;
```

### CLI

```bash
# Visualize a topology file
netvis examples/topologies/basic.yaml

# Use config file for advanced options
netvis --config examples/configs/balanced.json examples/topologies/datacenter.yaml

# List available examples
netvis list-examples
```

## Technical Details

**Graph Backend:** Built on petgraph, a production-ready graph data structure library for Rust.

**Performance:** Efficient algorithms with O(n log n) or O(n²) complexity depending on layout. Handles topologies with hundreds of nodes.

**Testing:** Comprehensive test suite with unit tests for individual components and integration tests for end-to-end workflows.

**Examples:** 17 example topologies covering common network patterns (star, ring, mesh, datacenter, enterprise).

## Development Status

All 10 development phases complete:
1. Graph foundation ✅
2. Force-directed layout ✅
3. Hierarchical layout ✅
4. Radial tree layout ✅
5. Multi-layer support ✅
6. Edge refinement ✅
7. Rendering system ✅
8. Export formats ✅
9. Configuration API ✅
10. CLI tool ✅

Production-ready for network topology visualization at scale.

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See `docs/` directory in repository
- **Examples:** See `examples/` directory in repository

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Example force-directed layout output
- Hierarchical layout comparison
- Edge bundling demonstration
- CLI usage with output
-->
