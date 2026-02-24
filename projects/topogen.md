---
layout: default
section: network-automation
---

# Topology Generator

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Technical Depth](#technical-depth)
- [Current Status](#current-status)
- [Roadmap](#roadmap)

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

## Current Status

2026-02-22 — Completed 30-04 (CLI integration with collect-all, error export, threshold config)

---

## Roadmap

- **Plans:** 5 plans

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
