---
layout: default
---

# Network Automation

A modular toolchain that takes a network design from whiteboard sketch to validated, deployable configuration. Each tool handles one stage of the lifecycle; together they form an end-to-end pipeline.

**Inputs:** topology and high-level requirements (or legacy CLI configurations for brownfield).
**Outputs:** reviewable configs, simulation results, diagrams, and audit artifacts.

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

---

## The Tools

### Ingestion & Generation

**[Brownfield Ingestion](/projects/configparsing)** — Extracts structured intent from legacy multi-vendor CLI configurations using LLM-powered RAG. Produces a vendor-neutral "as-is" topology model.

**[Topology Generator](/projects/topogen)** — Generates realistic topologies (Clos fabrics, WAN meshes, random graphs) in milliseconds. Rust engine with Python bindings.

### Modeling

**[Network Modeling Library](/projects/ank-pydantic)** — Python DSL for type-safe modeling of nodes, edges, and protocol layers. Composable query API backed by the NTE Rust graph engine.

**[Topology Engine Core (NTE)](/projects/ank-nte)** — Rust graph engine (14-crate workspace, petgraph StableDiGraph) ensuring every topological mutation is structurally sound. Pluggable datastores: Polars, DuckDB, Lite.

### Configuration & Simulation

**[Network Configuration Framework](/projects/ank-netcfg)** — Rust compiler transforming vendor-neutral graph models into device-specific configurations (Arista EOS, Cisco IOS-XR) through a deterministic blueprint-to-template pipeline.

**[Network Simulator](/projects/netsim)** — Tick-based, deterministic protocol simulator. Runs OSPF, BGP, and IS-IS convergence assertions before deployment. Same topology, same results — every time.

### Validation

**[Performance Simulator](/projects/netflowsim)** — Queueing-theoretic and Monte Carlo analysis on simulated routing tables. Identifies congestion points and blast radii under failure scenarios.

**[Network Analysis Engine](/projects/netassure)** — Formal verification (Z3 theorem proving), GNN-based prediction, and failure cascade modeling across static design, simulation results, and live telemetry.

**[Device Interaction Framework](/projects/deviceinteraction)** — Deploys generated configurations to lab environments. Testbed management, CLI parsing, and state verification.

### Observability

**[Visualization Engine](/projects/netvis)** — Rust layout engine for dense, multi-layer topologies. Edge bundling, hierarchical stacking, SVG/PDF/PNG output.

**[Automation Workbench](/projects/ank-workbench)** — Unified web UI integrating the full pipeline: design, simulate, visualize, and audit from a single interface.

---

## Foundations

This toolchain grew from PhD research on automated network configuration — the "Whiteboard to Build" model that compiles declarative intent into validated device configurations through formal graph transformations.

- **[Network Modeling Foundations](/projects/autonetkit-foundation)** — Original research establishing the core abstractions.
- **[AutoNetKit](/projects/autonetkit)** — Legacy configuration generation from the thesis-era work.
- **[Tick-Based Determinism vs. Full Emulation](/insights/tick-based-determinism)** — Why a custom Rust protocol simulator instead of Containerlab.

---

[← Back to Projects](projects)
