---
layout: default
---

# Network Automation Ecosystem

A unified ecosystem of seven Rust and Python tools for network topology generation, modeling, protocol simulation, traffic analysis, and visualization.

## Contents
- [Overview](#overview)
- [The Composable Toolchain](#the-composable-toolchain)
- [The Tools](#the-tools)
  - [Topology Generator](#topology-generator)
  - [Network Configuration Parser](#network-configuration-parser)
  - [AutoNetkit](#autonetkit)
  - [Network Topology Engine](#network-topology-engine)
  - [Network Simulator](#network-simulator--protocol-validation)
  - [Network Traffic Simulator](#network-traffic-simulator--flow-based-performance-analysis)
  - [Network Visualization Engine](#network-visualization-engine)
  - [Network Automation Workbench](#network-automation-workbench)
  - [AutoNetkit — The Foundation](#autonetkit--the-foundation)
- [Workflows](#workflows)
- [Source Code](#source-code)

---

## Overview

The ecosystem is evolving from a collection of standalone tools into a **Composable Network Toolchain**. It follows the Linux philosophy—specialized tools that do one thing well—orchestrated by an IDE-level experience (The Workbench).

### Core Architectural Tenets

1. **Standard-Agnostic Core:** The Network Topology Engine (NTE) acts as a universal translator, capable of ingesting data from NetBox, ContainerLab, or custom sources.
2. **Logical-to-Physical Decoupling:** We split Physical Topology from Logical Intent, decoupling engineering logic from specific vendor hardware.
3. **Hyper-Composable Entry Points:** Pull from a Source of Truth $\rightarrow$ Visualize; Generate from scratch $\rightarrow$ Simulate; Capture live state $\rightarrow$ Analyze capacity.

## The Composable Toolchain

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     Network Automation Workbench                        │
│              (FastAPI + React · Orchestration · Web UI)                  │
│                                                                         │
│  ┌──────────┐  ┌──────────────┐  ┌────────────┐  ┌──────────────────┐  │
│  │ Topology │  │  Modeling &  │  │  Protocol  │  │ Visualisation    │  │
│  │ Editor   │  │  Config      │  │  Simulator │  │ Explorer         │  │
│  └────┬─────┘  └──────┬───────┘  └─────┬──────┘  └────────┬─────────┘  │
└───────┼────────────────┼────────────────┼──────────────────┼────────────┘
        │                │                │                  │
   subprocess        Python API      subprocess         subprocess
        │                │                │                  │
┌───────▼────────┐ ┌─────▼──────────┐ ┌──▼───────────┐ ┌───▼──────────┐
│   topogen      │ │  autonetkit    │ │   netsim     │ │   netvis     │
│                │ │                │ │              │ │              │
│ 9 generators   │ │ Pydantic models│ │ OSPF, IS-IS  │ │ 5 layout     │
│ Traffic matrix │ │ Query DSL     │ │ BGP, MPLS    │ │ algorithms   │
│ Vendor naming  │ │ Config gen    │ │ SR, RSVP-TE  │ │ SVG/PNG/PDF  │
│ ContainerLab   │ │ Blueprints    │ │ L3VPN, BFD   │ │ WASM target  │
│ export         │ │ Compiler      │ │ gRPC daemon  │ │ Edge bundling│
└───────┬────────┘ └──────┬────────┘ │ BMP telemetry│ └──────────────┘
        │                 │          └──────────────┘
        │           ┌─────▼────────┐
        │           │     NTE      │
        │           │              │
        │           │ petgraph     │
        │           │ Polars DFs   │
        │           │ Query engine │
        │           │ Pluggable    │
        │           │ datastores   │
        │           └──────────────┘
        │
┌───────▼────────┐
│  netflowsim    │
│                │
│ Queuing models │
│ Monte Carlo    │
│ FIB path trace │
│ Rayon parallel │
└────────────────┘
```

**Data flows top-to-bottom.** The Workbench sits above all tools as the orchestration layer. autonetkit consumes NTE as a Rust dependency. topogen feeds generated topologies into autonetkit, netsim, netflowsim, and netvis. netsim validates routing behavior. netflowsim analyzes traffic performance. netvis renders the results.

---

## The Tools

### Topology Generator

<span class="status-badge status-active">v0.10 — Phase 21/24</span> · [Full Details →](projects/topogen)

**What It Is:**
A Rust library with Python bindings for generating realistic network topologies. Supports data center (fat-tree, leaf-spine), WAN/backbone (ring, mesh, hierarchical, POP), and random graph patterns (Barabasi-Albert, Watts-Strogatz). Includes traffic matrix generation using gravity models and ContainerLab output converters.

---

### CLI Scrape — Network Device Output Parser

<span class="status-badge status-active">Phase 1 — Foundation</span> · [Full Details →](projects/cliscrape)

**What It Is:**
Rust-based CLI scraping and parsing tool for network devices. TextFSM-compatible state machine parser with 10-50x faster execution than Python implementations. Includes interactive TUI debugger for template development and modern YAML/TOML template format.

**Key Features:**
- Full TextFSM compatibility (use existing ntc-templates library)
- Native Rust performance with parallel processing
- Interactive TUI debugger for template development
- Zero-copy parsing and pre-compiled regex patterns

**Current Status:** Phase 1 — defining lexer/parser for TextFSM files

**Tech Stack:** Rust, regex, ratatui

---

### Network Configuration Parser

<span class="status-badge status-active">Phase 1 — Ingestion</span> · [Full Details →](projects/ank-parse)

**What It Is:**
A framework for parsing legacy CLI configurations into vendor-agnostic models. Uses layout-aware PDF extraction (MinerU) to build a searchable knowledge base of vendor manuals in ChromaDB, enabling AI-assisted normalization of legacy state.

---

### AutoNetkit

<span class="status-badge status-active">v1.8 — Shipped | v1.10 in progress</span> · [Full Details →](projects/autonetkit)

**What It Is:**
A Python library for modeling and querying network topologies with type-safe Pydantic models and a Rust core. Expressive Python API backed by compiled graph algorithms (petgraph), with automatic configuration generation for multi-vendor network deployments (Cisco, Juniper, Arista, Nokia, SONiC).

---

### Network Topology Engine

<span class="status-badge status-active">Stable</span> · [Full Details →](projects/nte)

**What It Is:**
The Rust graph engine that powers the ecosystem. Provides native-speed topology operations exposed to Python through PyO3 bindings. Features a workspace of specialized crates for graph primitives (`nte-graph`), query execution (`nte-query`), and pluggable storage backends (Polars, DuckDB, Lite).

---

### Network Simulator — Protocol Validation

<span class="status-badge status-active">v1.8 — Data Center Fabric & EVPN</span> · [Full Details →](projects/network-simulator)

**What It Is:**
A deterministic, tick-based network simulator for rapid prototyping. Simulates OSPF, IS-IS, BGP, MPLS/LDP, and Segment Routing with packet-level accuracy. Enables sub-second validation of network convergence without the overhead of container-based emulation.

---

### Network Traffic Simulator — Flow-Based Performance Analysis

<span class="status-badge status-active">Phase 3/5 — Active Development</span> · [Full Details →](projects/netflowsim)

**What It Is:**
Flow-based network traffic simulator using analytic queuing models (M/M/1, M/D/1) and Monte Carlo simulations. Validates topologies and routing strategies against billions of flow iterations in seconds, providing massive-scale network performance analysis.

---

### Network Visualization Engine

<span class="status-badge status-active">v1.3 — Embed Readiness & API Stability</span> · [Full Details →](projects/netvis)

**What It Is:**
A Rust-based network topology layout and visualization engine. Renders complex multi-layer networks using advanced layout algorithms (force-directed, hierarchical, geographic, radial, isometric) with high-quality static output (SVG, PDF, PNG) and WASM targets.

---

### Network Automation Workbench

<span class="status-badge status-active">v1.3 — Tool Integration & Interactive Workflows</span> · [Full Details →](projects/ank-workbench)

**What It Is:**
A platform that integrates the entire network automation ecosystem into a single workflow. Driven from YAML, a text-based TUI, or the web interface—upload topology YAML, visualize the network, run simulations, and analyze results without switching between tools.

---

### Orchestrator (Device Interaction Runner)

<span class="status-badge status-active">Phase 1/5 (0%)</span> · [Full Details →](projects/orchestrator)

**What It Is:**
An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.

---

### Network Automation Ecosystem - Overall Architecture Definition

<span class="status-badge status-active">Phase 10/12</span> · [Full Details →](projects/automationarch)

**What It Is:**
This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

---

### AutoNetkit — The Foundation

<span class="status-badge status-active">PhD 2017</span> · [Full Details →](projects/autonetkit-foundation)

**What It Is:**
The original compiler-based network automation tool from my PhD research. Introduced declarative network design with the Whiteboard → Plan → Build transformation model. Integrated into Cisco's VIRL platform for automated multi-vendor lab provisioning.

---

### 1. Rapid Prototyping
Generate a topology structure with `topogen`, validate that protocols converge in `netsim` in seconds, and visualize the resulting state with `netvis`.

### 2. Design-to-Deploy
Model a network declaratively in `autonetkit`, transform through protocol layers (ISIS, MPLS, EVPN), generate multi-vendor configurations, and validate the entire design in `netsim` before deploying to production or container labs.

### 3. Traffic Engineering
Analyze capacity at scale by computing forwarding paths from `netsim` FIBs, running Monte Carlo simulations in `netflowsim` against traffic demands, and visualizing link utilization heatmaps in `netvis`.

### 4. Interactive Exploration
Use the **Workbench** as a unified interface to edit topology YAML with live validation, trigger simulations, and attach to interactive device terminals via the `netsim` gRPC daemon.

---


[← Back to Projects](projects)

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
.status-planning {
  background-color: #ffc107;
  color: #343a40;
}
</style>
