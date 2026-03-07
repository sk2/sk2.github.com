---
layout: default
section: network-automation
---

# Network Automation Ecosystem - Overall Architecture Definition

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>

</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

## Concept

This project defines the architecture of the Network Automation Ecosystem: how its tools connect, what data flows between them, and where the system is headed.

The ecosystem comprises nine repositories that form a composable toolchain. Each tool handles one concern -- topology generation, simulation, configuration parsing, visualization, analysis -- and communicates through pinned contract schemas (RFC-01, RFC-02). The architecture document formalizes these relationships and identifies future sub-projects.

### Pipeline Flow

<div class="mermaid">
flowchart LR
    TG[Topology<br/>Generator] --> MOD[Modeling<br/>Library]
    MOD --> CFG[Config<br/>Compiler]
    CFG --> SIM[Simulator]
    SIM --> VIS[Visualization<br/>Engine]
    VIS --> ANA[Analysis<br/>Engine]
    SIM --> ANA
</div>

### Contract Relationships

<div class="mermaid">
flowchart TD
    RFC01["RFC-01<br/>Operational Topology"]
    RFC02["RFC-02<br/>Live Overlay Stream"]
    RFC03["RFC-03<br/>Interface Representation"]

    TG[TopoGen] -->|produces| RFC01
    MOD[Modeling Library] -->|consumes/produces| RFC01
    CFG[Config Compiler] -->|consumes| RFC01
    SIM[Simulator] -->|consumes| RFC01
    SIM -->|produces| RFC02
    VIS[NetVis] -->|consumes| RFC01
    VIS -->|consumes| RFC02
    ANA[Analysis Engine] -->|consumes| RFC02
    RFC03 -.->|referenced by| RFC01
</div>

---

## Code Samples

### RFC-01 topology sidecar (minimal example)

```yaml
nodes:
  - id: r1
    role: router
    interfaces:
      - id: p1
        vendor_name: "Gi0/0"
  - id: r2
    role: router
    interfaces:
      - id: p1
        vendor_name: "Gi0/0"

links:
  - endpoints:
      - node: r1
        interface: p1
      - node: r2
        interface: p1
```

### Fixture validation

Three canonical fixture projects (minimal-lab, leaf-spine, edge-cases) verify contract compliance end-to-end:

```bash
python3 scripts/check-fixtures
```

Each fixture contains topology sidecars (RFC-01), overlay transcripts (RFC-02), and deterministic expected outputs. The gate validates schemas, replays fold rules, and checks telemetry cross-references.

---

## Scope

Nine tool repositories documented. 6 RFCs pinned with versioned schemas. 5 Architecture Decision Records. 41,000+ lines of architecture documentation across 100+ files.

### Fixture Structure

<div class="mermaid">
flowchart TD
    F[Fixture Project]
    F --> IN[Inputs]
    F --> EX[Expected Outputs]
    IN --> TP["*.topo.yaml<br/><small>RFC-01 topology</small>"]
    IN --> DS["*.design.yaml<br/><small>RFC-01 intent</small>"]
    IN --> MF["netauto.project<br/><small>RFC-02 manifest</small>"]
    EX --> OP["*.operational.json"]
    EX --> OV["overlay/golden.ndjson"]
</div>

---

## Current Status

v3.0 Implementation & Developer Enablement in progress — bridging architecture specs (v1.0–v2.0) to implementation guides, API references, and SDK patterns.

<details class="code-collapse">
<summary>Previous milestones</summary>

**v2.0 Advanced Architecture Capabilities** (shipped 2026-03-01) — topology management, verification tooling, GNN extensions, multi-domain interop, GPU-accelerated layout. 11/11 requirements satisfied.

**v1.1 Architecture Evolution & Refinement** (shipped 2026-02-28) — 9-tool ecosystem, intelligence layer, CLI scrape architecture, Live Hook design.

**v1.0 Initial Architecture Definition** (shipped 2026-02-21) — RFC-01/02 contracts, canonical fixtures, requirements traceability.

</details>

---

## Technical Reports

- [Download Technical Report: ecosystem-techreport.pdf](/assets/docs/automationarch-ecosystem-techreport.pdf)

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
