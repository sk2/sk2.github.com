---
layout: default
section: network-automation
---

# Visualization Engine

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.

Transform network topologies into clear, information-dense visualizations using algorithms that minimize edge crossings, bundle related connections, and respect hierarchical/geographic structure — enabling understanding of networks that would otherwise be visual noise.

---

## Screenshots

![Enterprise Campus](/images/netvis-enterprise-campus.png)
*Enterprise Campus — Sugiyama hierarchical layout with group containment and obstacle-aware label placement.*

![Data Center Fabric](/images/netvis-datacenter-large.png)
*Data Center Fabric — Fat-tree topology rendered using force-directed layout with edge bundling to reduce visual complexity.*

![ISP Backbone](/images/netvis-isp-backbone.png)
*ISP Backbone — Large-scale core network visualization with force-directed positioning and metric-aware line styling.*

![Radial Layout](/images/netvis-showcase-radial-layout.png)
*Radial Layout — Circular hierarchical projection for symmetrical architectures like rings and star clusters.*

![Geographic European Backbone](/images/netvis-geo-europe-backbone.png)
*Geographic Backbone — Topology mapped to real-world coordinates with curved edge routing between nodes.*

![Isometric Multi-Layer](/images/netvis-isometric-multi-layer.png)
*Isometric View — Stacking multiple protocol layers (Physical, OSPF, BGP) to visualize cross-layer associations and dependencies.*

![Theme Showcase](/images/netvis-theme-showcase.png)
*Theme System — Different visual profiles including light, dark, and high-contrast modes with automated WCAG compliance.*

---

## Current Status

2026-02-24 — Completed 73-01-PLAN.md (EditorDocument persistence schema)

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
