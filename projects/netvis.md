---
layout: default
section: network-automation
---

# Network Visualization Engine

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [Usage](#usage)
- [Features](#features)
- [Current Status](#current-status)

![Hero Image](/images/hero-diagram.svg)

---

## Concept

Rust-based network topology layout and visualization engine. Takes multi-layer network topologies (via petgraph) and renders them using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical or geographic structure. Outputs SVG, PDF, and PNG with interactive browser embedding via WASM.

Design follows Tufte's principles: maximize information density, minimize chartjunk. An automated WCAG 3:1 contrast system ensures accessibility without manual tuning.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/netvis-techreport.pdf)

---

## Code Samples

### README.md

```markdown
# Adapter Examples

This directory contains runnable scripts that demonstrate the end-to-end workflow:

external data -> `netvis import` -> topology YAML -> `netvis --input` -> SVG

All outputs are written to `target/` (gitignored by default).

## LLDP/CDP discovery JSON

Script: `examples/adapters/lldp-import.sh`

Runs an LLDP import from a JSON file and renders an SVG.

Run (from repo root):

```bash
bash examples/adapters/lldp-import.sh
```

Optional: pass a custom discovery JSON path:

```bash
bash examples/adapters/lldp-import.sh /path/to/discovery.json
```

Expected outputs:

- `target/lldp-imported.yaml`
- `target/lldp-imported.svg`

Sample input: `examples/adapters/sample-lldp.json`

## NetBox

Script: `examples/adapters/netbox-import.sh`

Requires a NetBox API token via env var (the script never prints it).

Environment variables:

- `NETBOX_TOKEN` (required)
- `NETBOX_URL` (recommended)

Run:

```bash
export NETBOX_URL=https://netbox.example.com
export NETBOX_TOKEN=...   # read-only token
bash examples/adapters/netbox-import.sh
```

You can also pass the NetBox URL as the first argument to override `NETBOX_URL`:

```bash
bash examples/adapters/netbox-import.sh https://netbox.example.com
```

Expected outputs:

- `target/netbox-imported.yaml`
- `target/netbox-imported.svg`

## Notes

- These scripts run `cargo run --features cli --bin netvis ...`. The first run may take a while to compile.
- If you have a `netvis` binary on your PATH already, you can run the equivalent `netvis import ...` commands directly.

```

### pdf-export.yaml

```yaml
# PDF Export Configuration for Documents and Presentations
#
# This YAML shows recommended PDF export settings for different use cases.
# Use with the Rust API: PdfOptions::default().page_size(...).title(...)
#
# For CLI usage, the output file extension (.pdf) triggers PDF export:
#   netvis --input topology.yaml --output diagram.pdf
#
# The settings below document PdfOptions API fields.

# Document Metadata (embedded in PDF properties)
metadata:
  title: "Network Topology Diagram"
  author: "NetVis"
  subject: "Infrastructure Documentation"
  keywords: "network, topology, diagram"

# Page Settings
page_size: content_size   # Options: content_size (default), a4, letter, custom
# For custom size:
# page_size:
#   custom:
#     width_mm: 297
#     height_mm: 210

# Margins (in millimeters)
margins_mm: 5.0

# DPI for coordinate mapping (default: 72.0)
dpi: 72.0

# Recommended render settings for PDF output
render:
  theme: print            # Print theme has high contrast for paper
  width: 1200
  height: 900

# Use Cases:
#
# 1. Technical Documentation:
#    - page_size: a4 or letter
#    - margins_mm: 10-15 for binding
#    - theme: print (black lines on white)
#
# 2. Presentations:
#    - page_size: content_size (fits slide exactly)
#    - theme: light or network
#    - Larger width (1600+) for detail
#
# 3. Posters/Large Format:
#    - page_size: custom (A1, A0, etc.)
#    - margins_mm: 20+
#    - High DPI (150-300) for quality

```

### png-print.yaml

```yaml
# PNG Export Configuration for High-Quality Printing
#
# This YAML shows recommended PNG settings for print output.
# Optimized for physical documents, posters, and professional printing.
#
# Use with the Rust API: PngOptions::default().dpi(300).scale(2.0)...
#
# CLI export example:
#   netvis --input topology.yaml --output diagram.png --width 2550 --height 3300
#
# The settings below document PngOptions API fields.

# High Resolution for Print
dpi: 300                  # Print standard (300 DPI minimum)
scale: 2.0                # 2x rasterization for crisp edges

# Dimensions (pixels at 300 DPI)
# Letter size: 8.5" x 11" at 300 DPI = 2550 x 3300 pixels
# A4 size: 210mm x 297mm at 300 DPI = 2480 x 3508 pixels
width: 2550
height: 3300

# Quality Settings
compression: high         # Best compression for archival quality
                          # Larger file but maximum quality

# Background for Paper
background: white         # White for standard paper printing
                          # Use theme background color for specialty paper

# Antialiasing
antialias: true           # Smooth edges are critical for print

# Recommended render settings for print
render:
  theme: print            # High contrast, optimized for paper
  width: 1200             # Scene width (scaled to print dimensions)
  height: 900
  labels: label

# Common Print Sizes at 300 DPI:
#
# Letter (8.5" x 11"):
#   width: 2550, height: 3300 (portrait)
#   width: 3300, height: 2550 (landscape)
#
# A4 (210mm x 297mm):
#   width: 2480, height: 3508 (portrait)
#   width: 3508, height: 2480 (landscape)
#
# Tabloid (11" x 17"):
#   width: 3300, height: 5100
#
# A3 (297mm x 420mm):
#   width: 3508, height: 4961
#
# Use Cases:
#
# 1. Technical Document Insert:
#    - width: 2550, height: 1800 (half page)
#    - dpi: 300
#    - theme: print
#
# 2. Wall Poster (A1/A0):
#    - width: 7016+ (A1 at 300 DPI)
#    - dpi: 150-200 (can reduce for very large)
#    - scale: 3.0 or higher
#
# 3. Presentation Handout:
#    - dpi: 150 (sufficient for handouts)
#    - compression: balanced

```

### png-web.yaml

```yaml
# PNG Export Configuration for Web Display
#
# This YAML shows recommended PNG settings for web/screen use.
# Optimized for dashboards, documentation sites, and embedding.
#
# Use with the Rust API: PngOptions::default().dpi(72).compression(...)
#
# CLI export is automatic when output ends in .png:
#   netvis --input topology.yaml --output diagram.png --width 1200 --height 800
#
# The settings below document PngOptions API fields.

# Resolution
dpi: 72                   # Web standard (72 or 96 DPI)
scale: 1.0                # 1x for web, 2x for retina

# Dimensions (in pixels)
width: 1200
height: 800

# Compression
compression: fast         # Options: fast, balanced (default), high
                          # 'fast' is fine for web - smaller file, quick load

# Background
background: white         # Options: white, transparent, or hex color (#rrggbb)
                          # Use 'transparent' for overlays on colored backgrounds

# Antialiasing
antialias: true           # Always true for smooth edges on screen

# Recommended render settings for web PNG
render:
  theme: dark             # Dark theme common for dashboards/NOC displays
  width: 1200
  height: 800
  labels: label

# Use Cases:
#
# 1. Dashboard/NOC Display:
#    - theme: dark
#    - width: 1920, height: 1080 (full HD)
#    - scale: 1.0
#
# 2. Documentation Site:
#    - theme: light
#    - width: 800-1200
#    - compression: fast
#    - background: white
#
# 3. Retina/HiDPI Display:
#    - scale: 2.0 (doubles pixel count)
#    - Keeps file sizes reasonable with good quality
#
# 4. Email Attachment:
#    - width: 800 (smaller for email clients)
#    - compression: high
#    - background: white

```

### production-view.yaml

```yaml
name: "Production Infrastructure"
show:
  tags: [production]
hide:
  types: [hub]
  tags: [decommissioned]

```

### routers-only.yaml

```yaml
show:
  types: [router, firewall]

```

### README.md

```markdown
# NetVis Example Gallery

This directory contains pre-rendered SVG outputs for layout template examples and the v1.2 visual effects showcase.

## v1.2 Effects Showcase

The gallery demonstrates visual effects (drop shadows, glow) across different topology types and real-world scenarios.

### Topology Types

| Topology | File | Description |
|----------|------|-------------|
| Mesh | `gallery-mesh-effects.yaml` | Dense mesh with emphasis on critical paths |
| Ring | `gallery-ring-effects.yaml` | Ring topology with root node highlight |
| Tree | `gallery-tree-effects.yaml` | Hierarchical layout with tiered shadows |
| Geographic | `gallery-geo-effects.yaml` | WAN with geographic positioning |

### Effect Comparison

| File | Purpose |
|------|---------|
| `gallery-effects-comparison.yaml` | Side-by-side comparison of no effects, subtle, and emphasis |

### Real-World Scenarios

| Scenario | File | Key Effects |
|----------|------|-------------|
| Datacenter | `gallery-datacenter-realworld.yaml` | Spine emphasis, firewall glow |
| Campus | `gallery-campus-realworld.yaml` | Core emphasis, wireless controller glow |
| WAN | `gallery-wan-realworld.yaml` | HQ selection glow, regional hierarchy |

### Rendering Gallery Examples

All examples render in both light and dark themes:

```bash
# Light theme
netvis -i examples/topologies/gallery-mesh-effects.yaml --theme light -o examples/outputs/gallery-mesh-effects-light.svg

# Dark theme
netvis -i examples/topologies/gallery-mesh-effects.yaml --theme dark -o examples/outputs/gallery-mesh-effects-dark.svg
```

### Available Effects

- `drop-shadow-subtle`: Subtle depth for secondary elements
- `drop-shadow-emphasis`: Strong depth for primary elements
- `glow-selection`: Highlight selected/active elements

---

## Template Example Outputs

Pre-rendered SVG outputs for all layout template examples.

## Files

### Spine-Leaf Template

- `template-spine-leaf-small.svg` (12 nodes) - 2-tier datacenter fabric
- `template-spine-leaf-medium.svg` (30 nodes) - 3-tier fabric with pods
- `template-spine-leaf-large.svg` (556 nodes) - 5-tier mega datacenter

### Hub-Spoke Template

- `template-hub-spoke-small.svg` (9 nodes) - Enterprise WAN
- `template-hub-spoke-medium.svg` (25 nodes) - Global regional hierarchy
- `template-hub-spoke-large.svg` (620 nodes) - Global enterprise WAN

### Ring Template

- `template-ring-small.svg` (8 nodes) - Campus backbone ring
- `template-ring-medium.svg` (20 nodes) - Metro dual ring
- `template-ring-large.svg` (500 nodes) - 5 metro transport rings

### Multi-Tier Template

- `template-multi-tier-small.svg` (10 nodes) - 3-tier web app
- `template-multi-tier-medium.svg` (35 nodes) - Production microservices
- `template-multi-tier-large.svg` (550 nodes) - Large Kubernetes cluster

## How to Regenerate

To regenerate these outputs, run:

```bash
# Small/Medium examples with template specified
netvis --input examples/topologies/template-spine-leaf-small.yaml --template spine-leaf --output examples/outputs/template-spine-leaf-small.svg
netvis --input examples/topologies/template-hub-spoke-small.yaml --template hub-spoke --output examples/outputs/template-hub-spoke-small.svg
netvis --input examples/topologies/template-multi-tier-small.yaml --template multi-tier --output examples/outputs/template-multi-tier-small.svg

# Ring uses force_directed from the YAML file
netvis --input examples/topologies/template-ring-small.yaml --output examples/outputs/template-ring-small.svg

# Large examples (500+ nodes each)
netvis --input examples/topologies/template-spine-leaf-large.yaml --template spine-leaf --output examples/outputs/template-spine-leaf-large.svg
netvis --input examples/topologies/template-hub-spoke-large.yaml --template hub-spoke --output examples/outputs/template-hub-spoke-large.svg
netvis --input examples/topologies/template-ring-large.yaml --output examples/outputs/template-ring-large.svg
netvis --input examples/topologies/template-multi-tier-large.yaml --template multi-tier --output examples/outputs/template-multi-tier-large.svg
```

## Notes

- Ring examples use `layout: force_directed` instead of the ring template because the radial layout algorithm requires tree-like graphs, and rings have cycles.
- Large examples (500+ nodes) are programmatically generated and may take 1-2 seconds to render.
- All SVG files can be viewed in any modern web browser.

```

### quality-report.md

```markdown
# SVG Quality Analysis Report

**Files analyzed:** 8

## Summary

| File | Status | Text | Font Range | Overlaps | Vision | Issues | Warnings |
|------|--------|------|------------|----------|--------|--------|----------|
| gallery-effects-comparison-light.svg | ISSUES | 21 | 9-22px | 32 | - | 2 | 1 |
| gallery-campus-realworld-light.svg | ISSUES | 32 | 14-22px | 18 | - | 1 | 1 |
| gallery-geo-effects-light.svg | ISSUES | 9 | 11-11px | 2 | - | 1 | 0 |
| gallery-mesh-effects-light.svg | ISSUES | 31 | 14-22px | 10 | - | 1 | 1 |
| gallery-ring-effects-light.svg | ISSUES | 21 | 14-22px | 22 | - | 1 | 1 |
| gallery-wan-realworld-light.svg | ISSUES | 15 | 14-14px | 14 | - | 1 | 1 |
| gallery-datacenter-realworld-light.svg | OK | 0 | - | 0 | - | 0 | 0 |
| gallery-tree-effects-light.svg | OK | 0 | - | 0 | - | 0 | 0 |

## Issues Requiring Attention

### gallery-campus-realworld-light.svg

- 6 critical text overlap(s) (> overlap)

### gallery-effects-comparison-light.svg

- 9 text element(s) with font-size < 10px (too small)
- 18 critical text overlap(s) (> overlap)

### gallery-geo-effects-light.svg

- 2 critical text overlap(s) (> overlap)

### gallery-mesh-effects-light.svg

- 6 critical text overlap(s) (> overlap)

### gallery-ring-effects-light.svg

- 6 critical text overlap(s) (> overlap)

### gallery-wan-realworld-light.svg

- 6 critical text overlap(s) (> overlap)

```

### README.md

```markdown
# Rendering Verification Artifacts

These files are generated to visually verify NetVis rendering quality (anti-aliasing, stroke crispness, and scale behavior) before + visual effects work.

## How To Regenerate

Run:

```bash
cargo test verification::rendering_quality::generate_visual_reference -- --ignored --nocapture
```

## Visual Inspection Checklist

- Curves: no stair-stepping on Bezier curves at 1x/2x/3x (zoom in and pan along long edges)
- Strokes: 1px strokes look crisp (no gray blur) at typical viewer zoom levels
- Text: labels remain readable; glyph edges look smooth (not jagged)

## Expected Passing Characteristics

- Smooth edges on curves and node outlines (anti-aliasing active)
- 2x and 3x PNGs are exact pixel-scale multiples of 1x
- SVG `viewBox` + `preserveAspectRatio` preserve layout when viewport size changes

## Source

- Topology: `examples/topologies/basic.yaml`
- Renderer: `src/render/svg.rs` via `SvgRenderer::render`

## Metadata

- Generated (unix seconds): 1770157724

```

### basic_topology.py

```python
#!/usr/bin/env python3
"""Basic topology example using NetVis Python bindings.

This example demonstrates:
- Creating a topology with nodes and edges
- Using the attrs parameter for custom metadata
- Using different layout algorithms
- Rendering to SVG, PNG, and PDF
"""

import netvis

def main():
    # Create a simple spine-leaf datacenter topology
    topo = netvis.Topology()

    # Add spine switches with custom attrs for inventory tracking
    topo.add_node(
        "spine-1",
        node_type="switch",
        label="Spine 1",
        attrs={
            "vendor": "arista",
            "model": "7050X3",
            "rack": "R01",
            "serial": "SPN001ABC",
            "mgmt_ip": "10.0.0.1",
        },
    )
    topo.add_node(
        "spine-2",
        node_type="switch",
        label="Spine 2",
        attrs={
            "vendor": "arista",
            "model": "7050X3",
            "rack": "R01",
            "serial": "SPN002DEF",
            "mgmt_ip": "10.0.0.2",
        },
    )

    # Add leaf switches
    for i in range(1, 5):
        topo.add_node(
            f"leaf-{i}",
            node_type="switch",
            label=f"Leaf {i}",
            attrs={
                "vendor": "arista",
                "model": "7280R3",
                "rack": f"R0{((i - 1) // 2) + 2}",
                "serial": f"LEF{i:03d}XYZ",
            },
        )

    # Add servers with custom attributes
    for i in range(1, 9):
        leaf_num = ((i - 1) // 2) + 1
        topo.add_node(
            f"server-{i}",
            node_type="server",
            label=f"Server {i}",
            attrs={
                "os": "ubuntu-22.04",
                "cpu_cores": 64,
                "memory_gb": 256,
                "role": "compute" if i % 2 == 0 else "storage",
            },
        )
        # Add edge with cable/connection metadata
        topo.add_edge(
            f"server-{i}",
            f"leaf-{leaf_num}",
            from_interface="eno1",
            to_interface=f"Eth1/{i % 48}",
            attrs={"speed": "25G", "cable_type": "DAC", "length_m": 3},
        )

    # Connect leaves to spines (full mesh) with fabric links
    for leaf in range(1, 5):
        topo.add_edge(
            f"leaf-{leaf}",
            "spine-1",
            from_interface="Eth1/49",
            to_interface=f"Eth1/{leaf}",
            attrs={
                "speed": "100G",
                "cable_type": "single-mode-fiber",
                "length_m": 15,
                "circuit_id": f"FAB-L{leaf}-S1",
            },
        )
        topo.add_edge(
            f"leaf-{leaf}",
            "spine-2",
            from_interface="Eth1/50",
            to_interface=f"Eth1/{leaf}",
            attrs={
                "speed": "100G",
                "cable_type": "single-mode-fiber",
                "length_m": 15,
                "circuit_id": f"FAB-L{leaf}-S2",
            },
        )

    print(f"Topology: {topo.node_count()} nodes, {topo.edge_count()} edges")

    # Render with different layouts
    print("Rendering with hierarchical layout...")
    topo.render_to_file("spine-leaf-hierarchical.svg", layout="hierarchical")

    print("Rendering with force-directed layout...")
    topo.render_to_file("spine-leaf-force.svg", layout="force-directed")

    print("Rendering to PNG...")
    topo.render_to_file("spine-leaf.png", layout="hierarchical", scale=2.0)

    print("Done! Check output files.")

if __name__ == "__main__":
    main()

```

---

## Visuals

### Network Visualisation Examples

![Geographic WAN](/images/geographic_wan.png)

![Bundled Mesh](/images/bundled_mesh.png)

![Hierarchical Datacenter](/images/hierarchical_datacenter.png)

![Labels Dense](/images/labels_dense.png)

![Force Directed Basic](/images/force_directed_basic.png)

---

## Usage

```bash
# Render a topology to SVG
netvis --input topology.yaml --output network.svg

# Geographic layout
netvis --input backbone.yaml --layout geographic --output map.svg

# Multi-layer isometric view
netvis --input datacenter.yaml --layout isometric --layers physical,l2,ospf --output layers.svg

# Import from LLDP discovery
netvis import --format lldp --input discovery.json --output topology.yaml

# Timeline across snapshots
netvis timeline --input snapshots/ --output timeline.svg
```

---

## Features

**Rendering:**
- SVG, PDF, PNG output
- WASM target for browser embedding
- SVG filter effects (drop shadows, glow) with Tufte-inspired guardrails
- Effect budget system prevents performance cliffs on large topologies
- Signature-based filter deduplication reduces SVG file size

**Analysis:**
- Path highlighting via BFS
- Traffic utilization overlays with NOC color mapping
- Timeline mode for multi-snapshot SVG export with incremental diffs
- Temporal entity queries (when did a node appear/change/disappear)
- Filter by type, tag, group, or layer without re-running layout

**Integration:**
- Python bindings via PyO3
- YAML/JSON topology input
- Adapters for LLDP/CDP discovery JSON and NetBox import
- Contract-versioned API for stable embedding

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust, Python, TypeScript |

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
- Renders topologies from [topogen](../topogen) (YAML), [ank-pydantic](../ank-pydantic) (JSON), or [netflowsim](../netflowsim) (GeoJSON with stats)
- WASM target enables embedding directly in the workbench browser UI
- Python bindings (PyO3) for programmatic rendering in Python workflows
- Geographic layout mode consumes lat/lon coordinates from [topogen](../topogen)'s geo module
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
