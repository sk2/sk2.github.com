---
layout: default
title: Network Automation
description: Modular toolchain from whiteboard sketch to validated network configuration. Topology engine, protocol simulator, configuration compiler, and visualization.
---

# Network Automation

A modular toolchain that takes a network design from whiteboard sketch to validated, deployable configuration. Each tool handles one stage of the lifecycle; together they form an end-to-end pipeline.

![Network Simulator running OSPF convergence](/images/netsim-basic-demo.gif)
*OSPF convergence in the Network Simulator — one stage in the pipeline.*

## Contents
- [Pipeline](#pipeline)
- [Core Platform](#core-platform) — Topology Engine, Simulator, Configuration Framework, Visualization Engine
- [Supporting Tools](#supporting-tools) — Modeling Library, Brownfield Ingestion, and five more
- [Foundations](#foundations) — Research origins and design rationale

---

## Pipeline

<div class="mermaid">
flowchart TD
    BF["Brownfield CLI"] --> TG
    GF["Greenfield Design"] --> TG
    TG["Topology Generation<br/><small>TopoGen · Config Parsing</small>"]
    TG --> MOD["Modeling & Queries<br/><small>Modeling Library + NTE</small>"]
    MOD --> CFG["Config Generation<br/><small>Config Framework</small>"]
    MOD --> SIM["Protocol Simulation<br/><small>Simulator</small>"]
    CFG --> DEP["Device Deploy & Test"]
    SIM --> PERF["Performance Simulation"]
    DEP --> VIS["Visualization & Analysis<br/><small>Visualization Engine · Workbench · Analysis Engine</small>"]
    PERF --> VIS
</div>

---

## Core Platform

The four Rust engines that form the automation pipeline: model a topology, generate configurations, simulate protocol convergence, and visualize the result.

<div class="project-grid">
<div class="project-card">
  <h3 class="card-title"><a href="/projects/ank-nte">Network Topology Engine</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Graph engine (14-crate workspace, petgraph StableDiGraph) ensuring every topological mutation is structurally sound. Pluggable datastores: Polars, DuckDB, Lite.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/netsim">Network Simulator</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Deterministic, tick-based protocol simulator that validates routing configurations (OSPF, IS-IS, BGP) before deployment. Same topology, same results — every time.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/ank-netcfg">Network Configuration Framework</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Compiles vendor-neutral graph models into device-specific configurations (Arista EOS, Cisco IOS-XR) through a deterministic blueprint-to-template pipeline.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/netvis">Network Visualization Engine</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Layout engine for dense, multi-layer network topologies. Edge bundling, hierarchical stacking, and SVG/PDF/PNG output with browser embedding via WASM.</p>
</div>
</div>

## Supporting Tools

**[Network Modeling & Configuration Library](/projects/ank-pydantic)** — Type-safe Python API for defining network topologies, backed by the Network Topology Engine. Composable query system with domain models for IS-IS, MPLS, EVPN.

**[Brownfield Ingestion](/projects/configparsing)** — Extracts structured intent from legacy multi-vendor CLI configurations using LLM-powered RAG. Produces a vendor-neutral topology model.

**[Topology Generator](/projects/topogen)** — Generates realistic topologies (Clos fabrics, WAN meshes, random graphs) in milliseconds. Rust engine with Python bindings.

**[Device Interaction Framework](/projects/deviceinteraction)** — Deploys generated configurations to lab environments. Testbed management, CLI parsing, and state verification.

**[Performance Simulator](/projects/netflowsim)** — Queueing-theoretic and Monte Carlo analysis on simulated routing tables. Identifies congestion points and blast radii under failure scenarios.

**[Network Analysis Engine](/projects/netassure)** — Formal verification (Z3 theorem proving), GNN-based prediction, and failure cascade modeling across static design, simulation results, and live telemetry.

**[Network Automation Workbench](/projects/ank-workbench)** — Web UI integrating the full pipeline: design, simulate, visualize, and audit from a single interface.

---

## Foundations

The toolchain grew from PhD research on automated network configuration — compiling declarative intent into validated device configurations through formal graph transformations.

- **[Network Modeling Foundations](/projects/autonetkit-foundation)** — Original research establishing the core abstractions.
- **[AutoNetKit](/projects/autonetkit)** — Legacy configuration generation from the thesis-era work.
- **[Tick-Based Determinism vs. Full Emulation](/insights/tick-based-determinism)** — Why the Network Simulator uses a custom Rust tick engine instead of Containerlab.

---

[← Back to Projects](projects) | [Signal Processing](signal-processing) | [Photography](photography) | [Data & Analytics](data-analytics) | [Autonomous Systems](agentic-systems)
