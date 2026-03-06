---
layout: default
section: network-automation
---

# Visualization Engine

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Gallery](#gallery)
- [Layout Algorithms](#layout-algorithms)
- [Features](#features)
- [Usage](#usage)
- [Status](#status)
- [Technical Reports](#technical-reports)

## Concept

Rust-based network topology layout and visualization engine. Takes multi-layer network topologies (via petgraph) and renders them using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical or geographic structure. Outputs SVG, PDF, and PNG with interactive browser embedding via WASM.

Design follows Tufte's principles: maximize information density, minimize chartjunk. An automated WCAG 3:1 contrast system ensures accessibility without manual tuning.

---

## Gallery

### Enterprise Campus
![Enterprise campus network with hierarchical layout](/images/netvis-enterprise-campus.png)
*Multi-tier enterprise campus topology with building groups and aggregation layers.*

### Data Center Fabric
![Large-scale data center leaf-spine topology](/images/netvis-datacenter-large.png)
*Leaf-spine data center fabric with edge bundling to reduce visual noise.*

### ISP Backbone
![ISP backbone with geographic positioning](/images/netvis-isp-backbone.png)
*ISP backbone topology with geographic node positioning and traffic-weighted edges.*

### Geographic Layout
![European backbone with geographic coordinates](/images/netvis-geo-europe-backbone.png)
*European backbone network rendered at actual geographic coordinates.*

### Isometric Multi-Layer
![Multi-layer stacked view: Physical to BGP](/images/netvis-isometric-multi-layer.png)
*Isometric stacking of Physical, L2, IP, OSPF, iBGP, and eBGP layers with cross-layer associations.*

### Radial Layout
![Radial tree layout for hierarchical structures](/images/netvis-showcase-radial-layout.png)
*Radial tree layout showing AS containment groups and peering relationships.*

### Theme Showcase
![Light and dark theme comparison](/images/netvis-theme-showcase.png)
*Theme-aware rendering with automatic contrast adjustment.*

### Annotated NOC View
![NOC diagram with annotations and callouts](/images/annotated-noc-demo.svg)
*Annotation overlay with text notes, circle/box/arrow callouts anchored to nodes.*

### Traffic Visualization
![Traffic flow with color-coded utilization](/images/traffic-noc-demo.svg)
*CSS dot-particle animation showing traffic flow with NOC color mapping (green/amber/red).*

---

## Layout Algorithms

- **Force-directed** — weighted edge simulation via fjadra (Rust port of d3-force) for organic layouts
- **Hierarchical** — Sugiyama-style layered layout for tiered topologies (core/distribution/access)
- **Radial tree** — starburst layout for containment groups (ASes, data centers, VLANs)
- **Geographic** — latitude/longitude positioning for WAN and backbone topologies
- **Isometric multi-layer** — stacked protocol layers (Physical → L2 → IP → OSPF → iBGP → eBGP)
- **Edge bundling** — hierarchical and force-directed bundling to reduce visual clutter
- **Bezier routing** — curved edge paths with crossing and collision reduction

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

## Status

**Current**: v1.9 Scale & Export — Barnes-Hut O(n log n) force repulsion for 10K-node topologies in <10s, single-file interactive HTML export.

**Recently shipped:**
- v1.8 — Timeline mode, temporal queries, traffic animation, annotation overlays, filter composition (March 2026)
- v1.7 — Interactive browser editor with WASM embedding
- v1.4 — Production scale, real-world integration
- v1.2 — Visual polish, SVG effects, WCAG accessibility, label placement

51,000+ lines of Rust across 8 shipped milestones.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/netvis-techreport.pdf)

---

[← Back to Projects](../projects)
