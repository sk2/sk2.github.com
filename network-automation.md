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
    └───────────────┘               └───────────────┘
```

**Data flows from design to analysis.** The Workbench provides a single interface for the entire process—from editing a topology to running a simulation and viewing the results.

---

## Tools

### Topology Generator
[Full Details →](projects/topogen)
Quickly create realistic network structures for testing. Supports common patterns for data centers and backbone networks.

---

### CLI Parser
[Full Details →](projects/cliscrape)
Extract structured data from network device outputs. A fast tool for turning text into information.

---

### Configuration Modeling
[Full Details →](projects/ank-pydantic)
A library for modeling network designs. It provides a consistent way to define and query network topologies.

---

### Network Simulator
[Full Details →](projects/network-simulator)
A tool for validating network designs. It simulates how data moves through a network to catch errors before they reach production.

---

### Visualization Engine
[Full Details →](projects/netvis)
Transform complex network data into clear diagrams. It uses layout algorithms to make large networks easy to understand.

---

### Automation Workbench
[Full Details →](projects/ank-workbench)
A unified interface for the entire toolchain. Design, simulate, and visualize networks in a single workflow.

---

### Network Modeling Foundations
[Full Details →](projects/autonetkit-foundation)
The original research that established the principles of automated network configuration.

---

[← Back to Projects](projects)
