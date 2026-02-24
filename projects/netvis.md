---
layout: default
section: network-automation
---

# NetVis

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

### What This Is

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.

### Core Value

Transform network topologies into clear, information-dense visualizations using algorithms that minimize edge crossings, bundle related connections, and respect hierarchical/geographic structure — enabling understanding of networks that would otherwise be visual noise.

---

## Tech Stack

Rust, petgraph, fjadra (d3-force port), SVG/PDF/PNG rendering, WASM-ready

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
