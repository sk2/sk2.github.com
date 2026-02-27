---
layout: default
section: network-automation
---

# Topology Generator

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A Rust-based topology generation engine that consolidates complex network graph algorithms into a unified, high-performance library. It enables the creation of realistic, validated network structures ranging from small lab setups to massive data center and backbone environments.

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

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
