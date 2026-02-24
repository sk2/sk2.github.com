---
layout: default
---

# Network Automation

A modular toolchain for the modeling, simulation, and analysis of large-scale data networks. This ecosystem bridges the gap between high-level architectural intent and technical execution through formal graph transformations and deterministic execution.

The tools are designed to work together as a pipeline, allowing engineers to move from initial topology generation to protocol-level verification and performance analysis within a unified workflow.

A typical workflow is: ingest topology + intent, compile candidate configurations, simulate convergence and failure scenarios, then visualize and audit outputs before deployment.

In practice the feedback loop is fast enough to feel interactive: many simulation runs complete in milliseconds for typical design iterations.

If you are new to the ecosystem: start with the **Network Modeling Engine**, then use the **Network Simulator** for verification and **Network Visualization Engine** for review.

**Inputs:** topology and high-level intent (plus brownfield state when available).

**Outputs:** reviewable configs/diffs, simulation results, diagrams, and audit artifacts.

## The Toolchain

We build specialized engines that handle specific stages of the network lifecycle—from **ingesting brownfield state** to final protocol-level validation.

```
      ┌────────────────────────┐               ┌────────────────────┐
      │ Source of Truth        │               │ Brownfield / Legacy │
      │ Products               │               │ CLI / PDF Ingest    │
      └────────┬───────────────┘               └───────┬────────────┘
              │                                       │
              └───────────────┬───────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────┐
│              Network Automation Workbench               │
│          Design · Verify · Audit · Visualize            │
└───────────────────────────┬─────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
    ┌───────▼───────┐               ┌───────▼───────┐
    │    Design     │               │    Verify     │
    │  Modeling &   │               │ Simulation &  │
    │ Configuration │               │ Visualization │
    └───────┬───────┘               └───────┬───────┘
            │                               │
    ┌───────▼───────┐               ┌───────▼───────┐
    │ Modeling Eng  │               │   Simulator   │
    │   Generator   │               │ Visualization │
    │   CLI Parser  │               │ Traffic Sim   │
    └───────┬───────┘               └───────┬───────┘
            │                               │
            └───────────────┬───────────────┘
                    ┌───────▼───────┐
                    │ Topology Core │
                    │ (NTE Engine)  │
                    └───────────────┘
```

**Data flows from design to validation.** The Workbench provides a single interface for the entire process—either starting from a clean slate using generators, or **modernizing existing state** through automated CLI parsing and configuration analysis.

## Primary Systems

- **[Network Simulator:](/projects/netsim)** Run deterministic protocol convergence and failover assertions on candidate designs before deployment.
- **[Brownfield Ingestion & Analysis:](/projects/configparsing)** Extract structured intent and topology relationships from legacy CLI and documentation for audits and migration workflows.
- **[Network Modeling Engine:](/projects/ank-pydantic)** Define intent and topology once, then query and transform it into protocol layers for the rest of the toolchain.
- **[Network Visualization Engine:](/projects/netvis)** Render large, multi-layer networks into diagrams for design review, topology validation, and analysis.
- **[Automation Workbench:](/projects/ank-workbench)** Use a single interface to design, simulate, visualize, and audit across the ecosystem.

## Specialized Tools

- **[Topology Core (NTE):](/projects/ank-nte)** The high-performance graph engine at the center of the ecosystem. It handles large-scale topology operations and queries with high precision and speed.
- **[Topology Generator:](/projects/topogen)** A tool for quickly creating realistic network structures. It supports standard patterns for data centers, backbones, and random graph models for large-scale testing.
- **[CLI Parser:](/projects/cliscrape)** A fast, ergonomic tool for extracting structured data from network device outputs, turning unstructured text into actionable information for analysis and validation.
- **[Performance Simulator:](/projects/netflowsim)** An analytic engine for massive-scale network performance analysis. It uses queuing models and Monte Carlo simulations to identify bottlenecks and test resilience.

## Legacy

- **[Configuration Generation (AutoNetkit):](/projects/autonetkit)** The original compiler-based configuration generator from the thesis-era work. It established the transformation pipeline and proved multi-vendor config generation at scale, but it is no longer the primary in-progress modeling layer. It remains useful as reference architecture and historical context.

## Foundations

This ecosystem borrows from earlier research on automated network configuration, including the "Whiteboard to Build" model. The goal here is practical: take a high-level intent and produce verifiable, reviewable outputs.

- **[Network Modeling Foundations:](/projects/autonetkit-foundation)** The original research and implementation details that established the core abstractions for automated configuration.

---

[← Back to Projects](projects)
