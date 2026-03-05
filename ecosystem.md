---
layout: default
title: Network Automation Ecosystem
---

# Network Automation Ecosystem

<div class="search-container">
  <p><strong>A modular, multi-paradigm approach to network validation.</strong></p>
</div>

The engineering philosophy behind this toolchain is simple: **decouple intent from implementation, and validate aggressively.** By breaking the network lifecycle down into discrete, specialized engines, we can achieve CI/CD-style rigor for physical networks.

Below is the architecture of the platform, tracking the lifecycle from a conceptual "Whiteboard" design through to protocol simulation and formal validation.

---

## The Pipeline

<div class="visual-card" style="padding: 2rem; background: #fff; border: 1px solid #e9ecef; border-radius: 8px; margin-bottom: 2rem; overflow-x: auto;">
  <pre style="background: transparent; color: #212529; font-size: 14px; line-height: 1.5; margin: 0;">
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           ANK Workbench                                │
  │          (Orchestration · Web UI · Workflow Management)                │
  └──────────────────────────────────┬─────────────────────────────────────┘
                                     │
  ┌────────────────┐         ┌───────▼────────┐          ┌─────────────────┐
  │   Brownfield   │         │    TopoGen     │          │    NetVis       │
  │   Ingestion    ├────────►│   (Generator)  ├─────────►│ (Visualization) │
  │(configparsing) │         └───────┬────────┘          └─────────────────┘
  └────────────────┘                 │
                             ┌───────▼────────┐
                             │  ank_pydantic  │
                             │ (Graph Models) │
                             └───────┬────────┘
                                     │
                             ┌───────▼────────┐
                             │    ank_nte     │
                             │ (Rust Engine)  │
                             └───────┬────────┘
                                     │
                   ┌─────────────────┴─────────────────┐
                   │                                   │
           ┌───────▼────────┐                  ┌───────▼────────┐
           │     netcfg     │                  │     netsim     │
           │  (Generation)  │                  │  (Simulation)  │
           └───────┬────────┘                  └───────┬────────┘
                   │                                   │
           ┌───────▼────────┐                  ┌───────▼────────┐
           │   device      │                  │  netflowsim    │
           │ interaction   │                  │ (Performance)  │
           └───────┬────────┘                  └───────┬────────┘
                   │                                   │
                   └─────────────────┬─────────────────┘
                             ┌───────▼────────┐
                             │   netassure    │
                             │  (Validation)  │
                             └────────────────┘
  </pre>
</div>

### 1. Ingestion & Generation
The pipeline begins with creating the raw topological structure.
*   **[Brownfield Ingestion (configparsing)](projects/configparsing):** Uses LLM-powered RAG pipelines to extract semantic intent from legacy multi-vendor CLI configurations, turning unstructured configuration into a clean "As-Is" topology model.
*   **[Topology Generator (topogen)](projects/topogen):** For greenfield designs, this Rust engine generates massive, mathematically rigorous topologies (e.g., Clos fabrics, WAN meshes, Barabási–Albert random graphs) in milliseconds.

### 2. Modeling & Core Engine
Raw structures need to be mapped to network protocols (OSPF, BGP, EVPN).
*   **[Network Modeling (ank_pydantic)](projects/ank-pydantic):** A Python DSL that provides type-safe, ergonomic modeling of nodes, edges, and protocol layers. It allows engineers to query and mutate the design using a Polars-inspired query API.
*   **[Topology Engine Core (ank_nte)](projects/ank-nte):** The high-performance Rust graph engine sitting underneath `ank_pydantic`. It ensures that every topological mutation is structurally sound, executing multi-layer graph traversals without the Python overhead.

### 3. Execution (The Fork)
Once the design is complete and structurally valid, it splits into two paths:
*   **Path A: Configuration Generation ([netcfg](projects/ank-netcfg)):** A Rust-based compiler that transforms the vendor-neutral graph into highly specific, templated device configurations (e.g., Arista EOS, Cisco IOS-XR).
*   **Path B: Protocol Simulation ([netsim](projects/netsim)):** A deterministic, tick-based network simulator. Before a single config is deployed, `netsim` runs the exact control-plane protocols (OSPF, BGP, IS-IS) to verify that the network will converge and that routing policies won't cause loops.

### 4. Validation & Analysis
The final stage ensures the network meets its performance and resilience constraints.
*   **[Device Interaction Framework](projects/deviceinteraction):** Automatically deploys the generated configurations to lab environments and executes testbeds to assert operational state.
*   **[Performance Simulator (netflowsim)](projects/netflowsim):** Uses analytic queueing theory and Monte Carlo simulations on the routing tables generated by `netsim` to detect congestion points and calculate blast radii under failure scenarios.
*   **[Network Analysis Engine (netassure)](projects/netassure):** The final gate. It aggregates data from the static design, simulation runs, and live telemetry to perform formal verification (e.g., Z3 theorem proving) and predictive failure analysis.

### 5. Orchestration & Observability
These horizontal layers provide visibility across the entire lifecycle.
*   **[Visualization Engine (netvis)](projects/netvis):** A Rust layout engine that untangles massive "hairball" topologies, rendering clear SVG/PNG diagrams for physical, logical, and BGP/OSPF protocol layers.
*   **[Automation Workbench](projects/ank-workbench):** The unified Web UI that integrates all the above tools into a single, cohesive workflow, allowing engineers to design, simulate, and deploy from one pane of glass.

---

[← Back to Projects](projects)
