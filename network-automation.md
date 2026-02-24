---
layout: default
---

# Network Automation

A toolchain for designing, simulating, and analyzing data networks.

## The Toolchain

We build specialized tools that handle specific parts of the network lifecycle, from initial design to final validation.

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
    │  autonetkit   │               │    netsim     │
    │   topogen     │               │    netvis     │
    │   ank-parse   │               │  netflowsim   │
    └───────┬───────┘               └───────┬───────┘
            │                               │
            └───────────────┬───────────────┘
                    ┌───────▼───────┐
                    │      NTE      │
                    │ Topology Core │
                    └───────────────┘
```

**Data flows from design to analysis.** The Workbench provides a single interface for the entire process—from editing a topology to running a simulation and viewing the results.

---

## Tools

### Automation Workbench
[Full Details →](projects/ank-workbench)
A unified interface for the entire toolchain. Design, simulate, and visualize networks in a single workflow. It integrates the individual tools into a cohesive engineering environment.

---

### Network Simulator
[Full Details →](projects/network-simulator)
A tool for validating network designs. It simulates how data moves through a network to catch errors before they reach production. Supports complex routing protocols and real-time interaction.

---

### Network Modeling Library
[Full Details →](projects/ank-pydantic)
A modern library for defining and querying network topologies. It provides a consistent, type-safe way to model network intent and generate configurations.

---

### Visualization Engine
[Full Details →](projects/netvis)
Transform complex network data into clear diagrams. It uses advanced layout algorithms to make large, multi-layer networks easy to understand.

---

### Topology Core (NTE)
[Full Details →](projects/ank-nte)
The high-performance graph engine that powers the ecosystem. It handles large-scale topology operations with speed and precision.

---

### Topology Generator
[Full Details →](projects/topogen)
Quickly create realistic network structures for testing. Supports common patterns for data centers, backbone networks, and random graph models.

---

### CLI Parser
[Full Details →](projects/cliscrape)
Extract structured data from network device outputs. A fast, ergonomic tool for turning unstructured text into actionable information.

---

### Performance Simulator
[Full Details →](projects/netflowsim)
Large-scale network performance analysis using analytic models. It validates topologies against billions of traffic flows to identify bottlenecks.

---

### Configuration Analysis
[Full Details →](projects/configparsing)
A framework for analyzing existing network configurations. It extracts intent and relationships from vendor-specific CLI data to normalize them into vendor-neutral models.

---

### Device Interaction
[Full Details →](projects/deviceinteraction)
A framework for communicating with network devices. It handles automated testing, state verification, and command execution across real and simulated hardware.

---

### AutoNetkit
[Full Details →](projects/autonetkit)
The production-ready reimagining of original research. It balances the flexibility of graph libraries with the structure of formal network models.

---

### Network Modeling Foundations
[Full Details →](projects/autonetkit-foundation)
The original PhD research that established the principles of automated network configuration and the "Whiteboard to Build" model.

---

[← Back to Projects](projects)
