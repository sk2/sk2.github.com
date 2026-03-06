---
layout: default
---

# Network Automation

A modular toolchain that takes a network design from whiteboard sketch to validated, deployable configuration. Each tool handles one stage of the lifecycle; together they form an end-to-end pipeline.

![Network Simulator running OSPF convergence](/images/netsim-basic-demo.gif)
*OSPF convergence in the Network Simulator — one stage in the pipeline.*

## Contents
- [Pipeline](#pipeline)
- [Core Platform](#core-platform) — Brownfield Ingestion, Modeling Library, Simulator, Visualization Engine
- [Supporting Tools](#supporting-tools) — Topology Engine, Configuration Framework, and five more
- [Foundations](#foundations) — Research origins and design rationale

---

## Pipeline

```
  Brownfield CLI ──┐          ┌── Greenfield Design
                   ▼          ▼
            ┌─────────────────────────┐
            │   Topology Generation   │   topogen / configparsing
            └────────────┬────────────┘
                         ▼
            ┌─────────────────────────┐
            │   Modeling & Queries    │   ank_pydantic + NTE (Rust)
            └────────────┬────────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
   ┌────────────────────┐ ┌────────────────────┐
   │  Config Generation │ │  Protocol Sim      │
   │  netcfg (Rust)     │ │  netsim (Rust)     │
   └─────────┬──────────┘ └─────────┬──────────┘
             │                      │
             ▼                      ▼
   ┌────────────────────┐ ┌────────────────────┐
   │  Device Deploy     │ │  Performance Sim   │
   │  + Test            │ │  netflowsim (Rust) │
   └─────────┬──────────┘ └─────────┬──────────┘
             └──────────┬───────────┘
                        ▼
            ┌─────────────────────────┐
            │   Visualization &       │   netvis + Workbench UI
            │   Analysis              │   netassure (GNN/Z3)
            └─────────────────────────┘
```

Code names in the diagram map to the full project names in the sections below.

---

## Core Platform

<div class="project-grid">
<div class="project-card">
  <h3 class="card-title"><a href="/projects/configparsing">Brownfield Ingestion</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Python</span></div>
  <p class="card-description">Extracts structured intent from legacy network configurations using LLM-powered RAG, identifying protocol relationships and topology from unstructured CLI output.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/ank-pydantic">Network Modeling Library</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Python</span><span class="stack-badge">Rust</span></div>
  <p class="card-description">Type-safe Python API for defining network topologies, backed by a Rust graph engine (NTE). Composable query system with domain models for IS-IS, MPLS, EVPN.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/netsim">Network Simulator</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Deterministic, tick-based protocol simulator that validates routing configurations (OSPF, IS-IS, BGP) before deployment. Models control-plane convergence at protocol level.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/netvis">Visualization Engine</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Layout engine for dense, multi-layer network topologies. Edge bundling, hierarchical stacking, and geographic positioning across thousands of nodes.</p>
</div>
</div>

## Supporting Tools

**[Topology Generator](/projects/topogen)** — Generates realistic topologies (Clos fabrics, WAN meshes, random graphs) in milliseconds. Rust engine with Python bindings.

**[Network Topology Engine](/projects/ank-nte)** — Rust graph engine (14-crate workspace, petgraph StableDiGraph) with pluggable datastores (Polars, DuckDB, Lite). Powers the modeling library.

**[Network Configuration Framework](/projects/ank-netcfg)** — Compiles vendor-neutral graph models into device-specific configurations (Arista EOS, Cisco IOS-XR) through a deterministic blueprint-to-template pipeline.

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
