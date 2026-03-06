---
layout: default
section: network-automation
---

# Network Automation Ecosystem Architecture

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

This project defines the architecture of the Network Automation Ecosystem: how its tools connect, what data flows between them, and where the system is headed.

The ecosystem comprises nine repositories that form a composable toolchain. Each tool handles one concern -- topology generation, simulation, configuration parsing, visualization, analysis -- and communicates through pinned contract schemas (RFC-01, RFC-02). The architecture document formalizes these relationships and identifies future sub-projects.

---

## Tools and Roles

| Tool | Role |
|------|------|
| [Topology Generator](../topogen) | Generates network topologies from high-level parameters |
| [autonetkit](../autonetkit) | Compiles topology + design intent into device configurations |
| [Network Simulator](../netsim) | Runs simulated networks from compiled topologies |
| [netflowsim](../netflowsim) | Simulates traffic flows across a topology |
| [Network Visualization Engine](../netvis) | Renders topology state and overlays in the browser |
| [Network Analysis Engine](../netassure) | Formal verification, graph algorithms, GNN-based inference |
| [Network Configuration Parser](../configparsing) | Parses vendor CLI output into normalized models |
| [deviceinteraction](../deviceinteraction) | Collects device state from live or lab networks |
| Network Automation Workbench | Orchestrates workflows across the toolchain (CLI/TUI) |

---

## Data Flow

The toolchain follows a linear pipeline with feedback loops:

1. **Topology definition.** Human-authored YAML sidecars (`*.topo.yaml`, `*.design.yaml`) declare nodes, links, and design intent using stable logical IDs.

2. **Compilation.** autonetkit reads topology + design and produces per-device configurations and an operational topology JSON (RFC-01 `netauto/operational-topology/v1.0`).

3. **Simulation.** The Network Simulator or netflowsim consumes operational topology to run forwarding or flow analysis.

4. **Live overlay stream.** Runtime state changes (topology mutations, telemetry deltas, errors) are expressed as an NDJSON event stream (RFC-02 `netauto/live-overlay-stream/v1.0`). Consumers fold events client-side into a materialized view.

5. **Visualization and analysis.** The Network Visualization Engine subscribes to the overlay stream via WebSocket. The Network Analysis Engine performs verification and inference against the same topology contracts.

6. **Legacy ingestion.** The Network Configuration Parser normalizes CLI scrapes from eight vendor platforms into the shared topology model, bridging existing networks into the toolchain.

---

## Contract System

Two pinned RFCs govern inter-tool communication:

- **RFC-01 (Operational Topology):** JSON schema for the compiled topology state. Nodes and edges carry stable IDs that all downstream tools reference.

- **RFC-02 (Live Overlay Stream):** NDJSON event protocol for runtime mutations. Supports snapshot, incremental add/remove, telemetry delta, and error events. Consumers deduplicate by `event_id` (first occurrence wins) and fold events in transcript order.

Canonical fixture projects under `examples/` validate these contracts. Each fixture contains input sidecars and committed expected outputs. A single command (`python3 scripts/check-fixtures`) runs schema validation, recomputes the deterministic fold, and checks cross-references.

---

## Architecture Decisions

Five ADRs and six RFCs document the key choices:

- Contract-first integration (schemas pinned before implementation)
- Logical interface representation (RFC-03)
- Workbench orchestration model
- Network Visualization Engine scope and decomposition
- Network Analysis Engine as a standalone analysis engine with five paradigms: formal verification, graph algorithms, failure cascade modeling, GNN inference, and optimization

---

## Status

**Current version:** v2.0 (shipped 2026-03-01)

v2.0 added topology policy evaluation, transition simulation with dry-run change plans, Header Space Analysis verification, GNN architecture extensions (GAT, TGN, HeteroGNN), multi-domain identity resolution, and a headless GPU-accelerated layout service using forceatlas2 + wgpu.

The v3.0 milestone shifts focus from architecture specification to implementation guidance: API references, SDK patterns, developer onboarding, and vendor integration kits.

**Codebase:** 41,000+ lines of architecture documentation across 100+ files, 6 RFCs, 5 ADRs.

---

## Technical Reports

- [Download Technical Report: ecosystem-techreport.pdf](/assets/docs/automationarch-ecosystem-techreport.pdf)

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
