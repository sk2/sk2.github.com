---
layout: default
---

# Network Automation

A modular toolchain for the modeling, simulation, and analysis of large-scale data networks. This ecosystem bridges the gap between high-level architectural intent and technical execution through formal graph transformations and deterministic execution.

The tools are designed to work together as a pipeline, allowing engineers to move from initial topology generation to protocol-level verification and performance analysis within a unified workflow.

## The Toolchain

We build specialized engines that handle specific stages of the network lifecycle—from **ingesting brownfield state** to final protocol-level validation.

```
      ┌────────────────────────┐               ┌────────────────────┐
      │ Source of Truth Products │             │ Brownfield / Legacy │
      │ (NetBox / YAML)        │               │ CLI / PDF Ingest    │
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

- **[Network Simulator:](/projects/netsim)** A deterministic engine for **pre-deployment verification**. It simulates the packet-level behavior of routing protocols like OSPF, IS-IS, and BGP, enabling engineers to verify convergence and failover scenarios before deployment.
- **[Brownfield Ingestion & Analysis:](/projects/configparsing)** A framework for extracting structured intent from legacy vendor-specific CLI data. It bridges the gap between existing deployments and modern automation, enabling automated audits and migration workflows.
- **[Configuration Generation (AutoNetkit):](/projects/autonetkit)** A framework for automated network provisioning. It transforms high-level design specifications into validated device configurations through a compiler-based transformation pipeline.
- **[Network Visualization Engine:](/projects/netvis)** A layout engine that transforms dense, multi-layer topologies into clear, structured diagrams. It employs advanced algorithms to reduce visual complexity, making the architecture of large systems intuitive and actionable.
- **[Automation Workbench:](/projects/ank-workbench)** A unified web interface that integrates the individual tools into a cohesive engineering environment for interactive topology editing and real-time protocol observability.

## Specialized Tools

- **[Topology Core (NTE):](/projects/ank-nte)** The high-performance graph engine at the center of the ecosystem. It handles large-scale topology operations and queries with high precision and speed.
- **[Topology Generator:](/projects/topogen)** A tool for quickly creating realistic network structures. It supports standard patterns for data centers, backbones, and random graph models for large-scale testing.
- **[CLI Parser:](/projects/cliscrape)** A fast, ergonomic tool for extracting structured data from network device outputs, turning unstructured text into actionable information for analysis and validation.
- **[Performance Simulator:](/projects/netflowsim)** An analytic engine for massive-scale network performance analysis. It uses queuing models and Monte Carlo simulations to identify bottlenecks and test resilience.
- **[Configuration Analysis:](/projects/configparsing)** A framework for extracting intent and relationships from existing vendor-specific CLI data, normalizing them into vendor-neutral network models.

## Foundations

The principles of this ecosystem are grounded in my PhD research on automated network configuration. This work introduced the "Whiteboard to Build" model, which continues to inform the development of modern, intent-based networking tools.

- **[Network Modeling Foundations:](/projects/autonetkit-foundation)** The original research and implementation details that established the core abstractions for automated configuration.

---

[← Back to Projects](projects)
