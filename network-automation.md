---
layout: default
---

# Network Automation

A modular toolchain for the modeling, simulation, and analysis of large-scale data networks. This ecosystem bridges the gap between high-level architectural intent and technical execution through formal graph transformations and deterministic execution.

The tools are designed to work together as a composable pipeline, allowing engineers to move from initial topology generation to protocol-level verification and performance analysis within a unified workflow.

## The Toolchain

We build specialized engines that handle specific stages of the network lifecycle.

```
┌─────────────────────────────────────────────────────────┐
│              Network Automation Workbench               │
│             Design · Simulate · Visualize               │
└───────────────────────────┬─────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
    ┌───────▼───────┐               ┌───────▼───────┐
    │    Design     │               │   Analysis    │
    │  Modeling &   │               │ Simulation &  │
    │ Configuration │               │ Visualization │
    └───────┬───────┘               └───────┬───────┘
            │                               │
    ┌───────▼───────┐               ┌───────▼───────┐
    │  Modeling Lib │               │   Simulator   │
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

**Data flows from design to analysis.** The Workbench provides a single interface for the entire process—from editing a topology to running a simulation and viewing the results.

## Primary Systems

- **[Configuration Generation (AutoNetkit):](/projects/autonetkit)** A framework for automated network provisioning. It uses a compiler-based approach to transform high-level design specifications into validated device configurations, supporting a wide range of network protocols and hardware vendors.
- **[Network Modeling Library:](/projects/ank-pydantic)** A modern framework for defining and querying network intent. Built with type-safe Pydantic models and a fast Rust core, it provides a consistent, programmable way to manage large-scale topology data.
- **[Network Simulator:](/projects/network-simulator)** A deterministic engine for validating network designs. It simulates the packet-level behavior of routing protocols like OSPF, IS-IS, and BGP, enabling engineers to verify convergence and failover scenarios before deployment.
- **[Network Visualization Engine:](/projects/netvis)** A layout engine that transforms dense, multi-layer topologies into structured diagrams. It employs advanced algorithms to reduce visual complexity, making the architecture of large systems intuitive and actionable.
- **[Automation Workbench:](/projects/ank-workbench)** A unified web interface that integrates the individual tools into a cohesive engineering environment. It allows for interactive topology editing, simulation control, and real-time protocol observability.

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
