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

## Concept

This project defines the architecture of the Network Automation Ecosystem: how its tools connect, what data flows between them, and where the system is headed.

The ecosystem comprises nine repositories that form a composable toolchain. Each tool handles one concern -- topology generation, simulation, configuration parsing, visualization, analysis -- and communicates through pinned contract schemas (RFC-01, RFC-02). The architecture document formalizes these relationships and identifies future sub-projects.

---

## Code Samples

### README.md

```markdown
# Examples: Canonical Fixture Projects

This directory holds canonical, reviewable fixture *projects* for the pinned RFC contracts.

Each fixture is intended to be:

- Self-contained (inputs + committed expected outputs)
- Deterministic (expected outputs are stable for re-audit)
- Enforceable by one repo-local command

See also: [RFC-01.md](RFC-01.md), [RFC-02.md](RFC-02.md), [rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md](rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md).

## Fixture Layout (Canonical)

One directory per fixture project:

```
examples/
  minimal-lab/
    netauto.project
    network.topo.yaml
    network.design.yaml
    README.md
    expected/
      *.operational.json
      overlay/
        golden.ndjson
        overlay.view.json
```

`scripts/check-fixtures` considers a directory a *fixture root* if it is under `examples/*/` and contains `netauto.project`.

## Inputs vs Expected Outputs

Inputs (human-authored or tool inputs):

- `netauto.project` (RFC-02 manifest concept)
- `*.topo.yaml` (RFC-01 topology sidecar)
- `*.design.yaml` (RFC-01 design sidecar)
- Optional `README.md` narrative per fixture

Expected outputs (committed, stable artifacts for review and re-audit):

- `expected/**/*.operational.json`
  - Must validate against the pinned OperationalTopology v1.0 schema: `rfc/rfc-01/operational-topology/v1.0/schema.json`
- `expected/overlay/golden.ndjson`
  - Must validate line-by-line against the pinned Live Overlay Stream v1.0 schema: `rfc/rfc-02/live-overlay-stream/v1.0/schema.json`
- `expected/overlay/overlay.view.json`
  - Must match a deterministic fold of `golden.ndjson` as recomputed by `scripts/check-fixtures`

## Derived Overlay View Contract (`netauto/overlay-view/v0`)

The fixture gate recomputes a derived overlay view from `expected/overlay/golden.ndjson` and compares it (semantic JSON equality) to `expected/overlay/overlay.view.json`.

The derived view is a plain JSON object with stable top-level keys:

- `schema`: constant `netauto/overlay-view/v0`
- `topology_id`: final scoped topology id
- `fold`: `{dedupe_by: "event_id", order: "transcript", last_event_id: ...}`
- `topology`: `{nodes: [...], edges: [...]}` (sorted lists)
- `telemetry`: `{nodes: {...}, edges: {...}}` (maps)
- `errors`: list (may be empty)

High-level fold rules:

- Process events in transcript order.
- Dedupe by `event_id` (first occurrence wins).
- `topology.snapshot` replaces the topology node/edge sets.
- `topology.node.add/remove` and `topology.edge.add/remove` mutate topology idempotently.
- `telemetry.snapshot` replaces node/edge telemetry maps.
- `telemetry.delta` merges metrics (keys present overwrite; absent unchanged; `null` allowed).
- `error` events append to `errors` and do not mutate topology or telemetry.

Lightweight cross-checks enforced by the gate:

- All overlay events in a fixture must share the same `topology_id`.
- Telemetry references must exist in the final folded topology state.

## Reviewer Workflow (One Command)

Install pinned validation dependencies:

```bash
python3 -m pip install -r rfc/rfc-02/live-overlay-stream/v1.0/requirements.txt
```

Validate all fixtures:

```bash
python3 scripts/check-fixtures
```

Validate one fixture:

```bash
python3 scripts/check-fixtures --fixture examples/minimal-lab
```

```

### README.md

```markdown
# Edge Cases Fixture: Error + Reconnect/Dedupe (RFC-02)

This fixture is intentionally small and "semantic": it exists to make RFC-02 reconnect/replay and dedupe behavior reviewable and deterministic.

- Pinned RFC-02 contract: `netauto/live-overlay-stream/v1.0`
  - Schema: `rfc/rfc-02/live-overlay-stream/v1.0/schema.json`
  - Semantics: [rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md](rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md)
- Pinned RFC-01 contract: `netauto/operational-topology/v1.0`
  - Schema: `rfc/rfc-01/operational-topology/v1.0/schema.json`

## What This Fixture Demonstrates

### 1) Reconnect / Backfill

In this transcript, a reconnect/backfill is represented by replaying a snapshot with:

- `replay: true`
- `cursor.after_event_id` set to the last event id the consumer had processed (exclusive)

See `expected/overlay/golden.ndjson` for the replayed `topology.snapshot` and `telemetry.snapshot` events.

### 2) Deduplication (event_id first-wins)

Consumers MUST dedupe by `event_id` (idempotency under retries/replays). The repo-local gate (`scripts/check-fixtures`) folds the NDJSON transcript in order and ignores duplicate `event_id` values (first occurrence wins).

This fixture includes at least one duplicated `event_id` line in `expected/overlay/golden.ndjson` to make that behavior explicit and reviewable.

### 3) In-band Error Event

The transcript includes an in-band `error` event (`type: "error"`). The derived overlay view produced by `scripts/check-fixtures`:

- Appends error details to `errors[]`
- Does not mutate topology or telemetry state

See `expected/overlay/overlay.view.json` for the folded `errors` list.

## How To Validate

Install pinned validation deps:

```bash
python3 -m pip install -r rfc/rfc-02/live-overlay-stream/v1.0/requirements.txt
```

Validate this fixture end-to-end:

```bash
python3 scripts/check-fixtures --fixture examples/edge-cases
```

```

### network.design.yaml

```yaml
schema: netauto/design/v2.0
base_topology: network.topo.yaml
topology_id: edge-cases-01
description: "Minimal intent for the tiny edge-cases topology."

protocols:
  ospf:
    area: 0
    interfaces:
      - node: ec-spine-01:p1
        cost: 10
      - node: ec-spine-01:p2
        cost: 10
      - node: ec-leaf-01:p1
        cost: 10
      - node: ec-leaf-02:p1
        cost: 10

```

### network.topo.yaml

```yaml
schema: netauto/topology/v2.0
topology_id: edge-cases-01
description: "Tiny topology used to exercise RFC-02 overlay semantics."

nodes:
  - id: ec-spine-01
    role: spine
    site: lab
    interfaces:
      - id: p1
        vendor_name: Ethernet1
      - id: p2
        vendor_name: Ethernet2

  - id: ec-leaf-01
    role: leaf
    site: lab
    interfaces:
      - id: p1
        vendor_name: Ethernet1

  - id: ec-leaf-02
    role: leaf
    site: lab
    interfaces:
      - id: p1
        vendor_name: Ethernet1

links:
  - id: ec-spine-01:p1--ec-leaf-01:p1
    endpoints:
      - node_id: ec-spine-01
        interface_id: p1
      - node_id: ec-leaf-01
        interface_id: p1

  - id: ec-spine-01:p2--ec-leaf-02:p1
    endpoints:
      - node_id: ec-spine-01
        interface_id: p2
      - node_id: ec-leaf-02
        interface_id: p1

```

### README.md

```markdown
# Leaf/Spine Fixture: Topology Mutations + Telemetry Overlays

This fixture is a small-but-realistic leaf/spine fabric intended to be a credible review artifact beyond the tiny lab.

- Pinned RFC-02 contract: `netauto/live-overlay-stream/v1.0`
  - Schema: `rfc/rfc-02/live-overlay-stream/v1.0/schema.json`
  - Semantics: `rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md`
- Pinned RFC-01 contract: `netauto/operational-topology/v1.0`
  - Schema: `rfc/rfc-01/operational-topology/v1.0/schema.json`

## Topology Intent

`network.topo.yaml` describes a modest DC fabric:

- 2 spines: `ls-spine-01`, `ls-spine-02`
- 4 leaves: `ls-leaf-01` .. `ls-leaf-04`
- Leaves are dual-homed to both spines (uplinks are modeled as logical interfaces `p1`, `p2`).

The inputs are designed to be readable and to keep IDs stable and predictable.

## Overlay Scenarios Covered (RFC-02)

The overlay transcript `expected/overlay/golden.ndjson` is the mutation showcase:

1. Baseline `topology.snapshot` for the initial fabric (2 spines + 3 leaves).
2. Topology mutations:
   - `topology.node.add` + `topology.edge.add`: a new leaf (`ls-leaf-04`) is added and dual-homed.
   - `topology.edge.remove`: an uplink is removed (maintenance / failure).
   - `topology.node.remove` (with explicit `topology.edge.remove`): a leaf (`ls-leaf-03`) is decommissioned.
3. Telemetry overlays:
   - `telemetry.snapshot`: initial metrics for nodes and edges in the final folded topology.
   - `telemetry.delta`: incremental metric updates (merge semantics per `rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md`).

The derived view `expected/overlay/overlay.view.json` is a deterministic fold of the transcript as recomputed by `scripts/check-fixtures`.

## How To Validate

Install pinned validation deps:

```bash
python3 -m pip install -r rfc/rfc-02/live-overlay-stream/v1.0/requirements.txt
```

Validate this fixture end-to-end:

```bash
python3 scripts/check-fixtures --fixture examples/leaf-spine
```

```

### network.design.yaml

```yaml
schema: netauto/design/v2.0
base_topology: network.topo.yaml
topology_id: leaf-spine-01
description: "Minimal intent for the leaf/spine fabric (OSPF underlay)."

protocols:
  ospf:
    area: 0
    interfaces:
      - node: ls-spine-01:p1
        cost: 10
      - node: ls-spine-01:p2
        cost: 10
      - node: ls-spine-01:p3
        cost: 10
      - node: ls-spine-01:p4
        cost: 10
      - node: ls-spine-02:p1
        cost: 10
      - node: ls-spine-02:p2
        cost: 10
      - node: ls-spine-02:p3
        cost: 10
      - node: ls-spine-02:p4
        cost: 10
      - node: ls-leaf-01:p1
        cost: 10
      - node: ls-leaf-01:p2
        cost: 10
      - node: ls-leaf-02:p1
        cost: 10
      - node: ls-leaf-02:p2
        cost: 10
      - node: ls-leaf-03:p1
        cost: 10
      - node: ls-leaf-03:p2
        cost: 10
      - node: ls-leaf-04:p1
        cost: 10
      - node: ls-leaf-04:p2
        cost: 10

```

### network.topo.yaml

```yaml
schema: netauto/topology/v2.0
topology_id: leaf-spine-01
description: "Small-but-realistic leaf/spine fabric (2 spines, 4 leaves)."

nodes:
  - id: ls-spine-01
    role: spine
    site: dc1
    vendor: arista
    model: 7800R
    interfaces:
      - id: p1
        vendor_name: Ethernet1
      - id: p2
        vendor_name: Ethernet2
      - id: p3
        vendor_name: Ethernet3
      - id: p4
        vendor_name: Ethernet4

  - id: ls-spine-02
    role: spine
    site: dc1
    vendor: arista
    model: 7800R
    interfaces:
      - id: p1
        vendor_name: Ethernet1
      - id: p2
        vendor_name: Ethernet2
      - id: p3
        vendor_name: Ethernet3
      - id: p4
        vendor_name: Ethernet4

  - id: ls-leaf-01
    role: leaf
    site: dc1
    vendor: arista
    model: 7050X
    interfaces:
      - id: p1
        vendor_name: Ethernet49
      - id: p2
        vendor_name: Ethernet50

  - id: ls-leaf-02
    role: leaf
    site: dc1
    vendor: arista
    model: 7050X
    interfaces:
      - id: p1
        vendor_name: Ethernet49
      - id: p2
        vendor_name: Ethernet50

  - id: ls-leaf-03
    role: leaf
    site: dc1
    vendor: arista
    model: 7050X
    interfaces:
      - id: p1
        vendor_name: Ethernet49
      - id: p2
        vendor_name: Ethernet50

  - id: ls-leaf-04
    role: leaf
    site: dc1
    vendor: arista
    model: 7050X
    interfaces:
      - id: p1
        vendor_name: Ethernet49
      - id: p2
        vendor_name: Ethernet50

links:
  - id: ls-spine-01:p1--ls-leaf-01:p1
    endpoints:
      - node_id: ls-spine-01
        interface_id: p1
      - node_id: ls-leaf-01
        interface_id: p1

  - id: ls-spine-02:p1--ls-leaf-01:p2
    endpoints:
      - node_id: ls-spine-02
        interface_id: p1
      - node_id: ls-leaf-01
        interface_id: p2

  - id: ls-spine-01:p2--ls-leaf-02:p1
    endpoints:
      - node_id: ls-spine-01
        interface_id: p2
      - node_id: ls-leaf-02
        interface_id: p1

  - id: ls-spine-02:p2--ls-leaf-02:p2
    endpoints:
      - node_id: ls-spine-02
        interface_id: p2
      - node_id: ls-leaf-02
        interface_id: p2

  - id: ls-spine-01:p3--ls-leaf-03:p1
    endpoints:
      - node_id: ls-spine-01
        interface_id: p3
      - node_id: ls-leaf-03
        interface_id: p1

  - id: ls-spine-02:p3--ls-leaf-03:p2
    endpoints:
      - node_id: ls-spine-02
        interface_id: p3
      - node_id: ls-leaf-03
        interface_id: p2

  - id: ls-spine-01:p4--ls-leaf-04:p1
    endpoints:
      - node_id: ls-spine-01
        interface_id: p4
      - node_id: ls-leaf-04
        interface_id: p1

  - id: ls-spine-02:p4--ls-leaf-04:p2
    endpoints:
      - node_id: ls-spine-02
        interface_id: p4
      - node_id: ls-leaf-04
        interface_id: p2

```

### README.md

```markdown
# minimal-lab (canonical fixture)

This fixture is the smallest readable project that demonstrates:

- RFC-01 sidecars: `*.topo.yaml` + `*.design.yaml` and their stable ids
- RFC-02 manifest wiring (`netauto.project`) + the pinned overlay stream artifacts

If you only read one example, read this one.

## What this topology represents

A tiny 3-node routed lab:

- `r1` -- `r2` -- `r3`

Each node uses logical interface ids (`p1`, `p2`, ...) that are stable across runs.
Vendor interface names (if present) are metadata only.

## Files in this fixture

Inputs (human-authored):

- `netauto.project`
  - RFC-02 manifest example that wires layers and a telemetry hook.
- `network.topo.yaml`
  - RFC-01 topology sidecar (physical world + interface mapping).
- `network.design.yaml`
  - RFC-01 design sidecar (logical intent) referencing topology ids.

Committed expected outputs (review/re-audit artifacts):

- `expected/network.operational.json`
  - Must validate against the pinned OperationalTopology v1.0 schema.
- `expected/network.results.json`
  - Minimal illustrative output (no pinned schema; intentionally small).
- `expected/overlay/golden.ndjson`
  - Must validate line-by-line against the pinned LiveOverlayStream v1.0 schema.
- `expected/overlay/overlay.view.json`
  - Deterministic fold of `golden.ndjson` (recomputed by `scripts/check-fixtures`).

## Overlay scenarios covered

This transcript keeps the story short:

1. `topology.snapshot` baseline nodes/edges
2. `telemetry.snapshot` baseline metrics for the same ids
3. `telemetry.delta` updates a subset of metrics

## Fold rules used for overlay.view.json

These match the deterministic implementation in `scripts/check-fixtures`:

- Process events in transcript order.
- Dedupe by `event_id` (first occurrence wins).
- `topology.snapshot` replaces topology node/edge sets.
- `telemetry.snapshot` replaces telemetry maps.
- `telemetry.delta` merges metrics (keys present overwrite; absent unchanged; `null` allowed).
- `error` events append to `errors` and do not mutate topology/telemetry.
- Cross-check: telemetry references must exist in the final folded topology state.

## Review / verification

Install pinned validation deps:

```bash
python3 -m pip install -r rfc/rfc-02/live-overlay-stream/v1.0/requirements.txt
```

Validate this fixture:

```bash
python3 scripts/check-fixtures --fixture examples/minimal-lab
```

Useful references:

- `RFC-01.md`
- `RFC-02.md`
- `rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md`

```

### network.design.yaml

```yaml
# RFC-01 design sidecar (logical intent)
#
# There is no pinned schema for this file yet; it is included as a readable
# example of how design references stable topology ids.

schema: netauto/design/v2.0
base_topology: "./network.topo.yaml"

addressing:
  loopbacks:
    r1: "10.0.0.1/32"
    r2: "10.0.0.2/32"
    r3: "10.0.0.3/32"

protocols:
  ospf:
    area: 0
    interfaces:
      - node: "r1:p1"
        cost: 10
      - node: "r2:p1"
        cost: 10
      - node: "r2:p2"
        cost: 10
      - node: "r3:p1"
        cost: 10

```

### network.topo.yaml

```yaml
# RFC-01 topology sidecar (human-authored for this fixture)
#
# Purpose: demonstrate stable logical ids (node ids + interface ids) that can be
# referenced by other sidecars and by RFC-02 overlay events.

nodes:
  - id: r1
    role: router
    interfaces:
      - id: p1
        vendor_name: "Gi0/0"
      - id: p2
        vendor_name: "Gi0/1"

  - id: r2
    role: router
    interfaces:
      - id: p1
        vendor_name: "Gi0/0"
      - id: p2
        vendor_name: "Gi0/1"

  - id: r3
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

  - endpoints:
      - node: r2
        interface: p2
      - node: r3
        interface: p1

```

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## What This Is

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `[topogen](../topogen)`, `[autonetkit](../autonetkit)`, `[netsim](../netsim)`, `[netflowsim](../netflowsim)`, `[netvis](../netvis)`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

---

## Why We're Doing This

The Network Automation Ecosystem is evolving from a collection of specialized tools into a "Composable Network Toolchain." To effectively manage this evolution and ensure strategic alignment, it is critical to:

*   **Formalize Architectural Understanding:** Document the relationships, data flows, and integration points between all components.
*   **Identify Future Sub-Projects:** Clearly define opportunities for new tools or major enhancements (e.g., the Intelligence Layer, legacy ingestion, multi-interface orchestration) and their place within the ecosystem.
*   **Ensure Product Differentiation:** Research the broader ecosystem to identify unique selling points and areas for competitive advantage.
*   **Guide Strategic Development:** Provide a foundational architectural blueprint for decision-making regarding technology choices, integration patterns, and development priorities.
*   **Enhance Collaboration:** Create a shared understanding for all stakeholders, from engineers to product management.

This project directly supports the strategic vision outlined in `STRATEGY.md` and deepens the insights from `README.md`, `DATAFLOWS.md`, and `ECOSYSTEM_INTEROP.md`.

---

## Success Metrics

*   **Comprehensive Architectural Mapping:** Produce a clear and detailed architectural overview that integrates all current and proposed tools, data flows, and strategic pillars.
*   **Identified Sub-Projects:** Define at least 3-5 high-level future sub-projects with clear scope and rationale.
*   **Differentiated Value Proposition:** Clearly articulate the unique competitive advantages and differentiators of the ecosystem based on research.
*   **Stakeholder Alignment:** Achieve consensus among key stakeholders on the architectural vision and roadmap for the ecosystem.
*   **Foundational Research:** Complete thorough research into the general domain ecosystem, standard practices, and competitive landscape.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| **Project Scope** | To address the need for a holistic view of the Network Automation Ecosystem, the project will focus on defining the overall architecture, rather than a single component like the GNN. This provides a necessary foundation for future sub-projects. | Capture overall architecture and future sub-projects. |
| **Research Focus** | Initial research will prioritize understanding the general ecosystem, competitor offerings, and best practices in network automation to inform product differentiation and strategic direction. | Focus research on broader ecosystem and differentiation. |

---

## Documentation conventions

- Internal doc links use repo-root relative paths (no leading `/`), e.g. `.planning/research/ARCHITECTURE.md`.
- Use anchors (`#...`) when it improves precision.
- Do not use `./` or `../` for internal doc links.
- Run `.planning/scripts/check-links` before completing doc-heavy phases.
- Roadmap parity: `ROADMAP.md` and `.planning/ROADMAP.md` must remain byte-identical.

---

## Current State

**Latest Milestone:** v2.0 Advanced Architecture Capabilities (shipped 2026-03-01)

**What Was Delivered:**
- **Topology Management Module :** Policy evaluation format, inferred topology semantics, transition simulation (dry-run change plans), reactive event model (mutation vs recalculation taxonomy), active probing contracts
- **Verification Tooling :** Header Space Analysis (HSA) workflow, continuous verification harness with fault-injection scenarios, multi-format test reports (JUnit/HTML/JSON/YAML)
- **Intelligence Extensions :** GNN architecture extensions (GAT, TGN, HeteroGNN, GAE), blast radius modeling with causal chains, service impact differentiation, evaluation metrics framework
- **Interop Evolution :** Multi-domain stitching and reconciliation, three-stage identity resolution (deterministic → probabilistic → manual), conflict resolution policies with audit trails, RFC-01 provenance extensions
- **Visualization at Scale :** Headless GPU-accelerated layout service (forceatlas2 + wgpu, 80x CPU speedup), progressive coordinate streaming (WebSocket), cache-first topology hashing (SHA256)

**Quality Metrics:**
- 11/11 requirements satisfied with evidence
- 47/49 cross-phase integration touchpoints verified ()
- 6/7 end-to-end flows validated
- ~3,000 lines of documentation added

**Codebase State:**
- 9 tool repositories documented ([topogen](../topogen), [autonetkit](../autonetkit), [netsim](../netsim), [netflowsim](../netflowsim), [netvis](../netvis), Workbench, [configparsing](../configparsing), [deviceinteraction](../deviceinteraction), [netassure](../netassure))
- 5 ADRs (contract-first, interface representation, orchestration, [netvis](../netvis) scope, [netassure](../netassure) decomposition)
- 6 RFCs (RFC-01 Topology, RFC-02 Live Stream, RFC-03 Interface Representation, RFC-TELEM-01, RFC-INFER-01, RFC-PRED-01)
- 41,000+ lines of architecture documentation across 100+ files

---

## Current Milestone: v3.0 Implementation & Developer Enablement

**Goal:** Bridge the gap between architecture definition (v1.0-v2.0) and implementation by creating comprehensive implementation guides, API references, SDK design patterns, and developer onboarding materials.

**Strategic Shift:** From "what to build" (architecture specs) to "how to build it" (implementation guidance)

**Target capabilities:**
- **[netassure](../netassure) Implementation Guides** — API reference, formal verification cookbook, graph algorithm patterns, ML/GNN integration examples
- **Live Hook Developer SDK** — Client library design patterns, WebSocket protocol implementation guide, state reconciliation patterns, event replay handling
- **CLI Scrape Extension Kit** — Vendor integration guide (adding new platforms), parser development patterns, normalization rule authoring, multi-VRF edge case handling
- **Workbench Integration Patterns** — Workflow engine implementation guide, orchestration library usage, CLI/TUI feature parity checklist, error handling best practices

**Timeline:** 2-3 weeks (medium scope)

<details>
<summary>Previous Milestones</summary>

---

## # v1.1 Architecture Evolution & Refinement (shipped 2026-02-28)

- Resolved 3 open architectural questions (OQ-02, OQ-03, OQ-04) with ADRs and RFCs
- Created 9-tool ecosystem architecture (added [netassure](../netassure) as standalone advanced analysis engine)
- Defined comprehensive intelligence layer (telemetry infrastructure, GNN training pipeline, dual deployment, Live Hook integration)
- Architected CLI scrape tool (8-vendor legacy ingestion, normalization, diff engine, multi-VRF)
- Established Live Hook architecture (multiplexed WebSocket, fold-on-client state, retention/keyframes for timeline scrubbing)
- Documented 5 advanced analysis paradigms in [netassure](../netassure) (formal verification, graph algorithms, failure cascades, ML/GNN, optimization)
- Maintained architecture integrity across 38,206 lines of documentation (100+ Markdown files with passing link checks)

---

## # v1.0 Initial Architecture Definition (shipped 2026-02-21)

- Architecture spine establishment (README, STRATEGY, DATAFLOWS alignment)
- Requirements traceability (ARCH-01 through ARCH-07 with evidence links)
- RFC-01 OperationalTopology Contract (pinned schema v1.0)
- RFC-02 Live Overlay Stream Contract (pinned schema + NDJSON validator)
- Canonical RFC fixture projects (minimal-lab, leaf-spine, edge-cases)
- All validation gates passing (check-fixtures, check-links)

</details>

---

## Requirements



---

## # Validated

<!-- Milestone v1.0: Initial Architecture Definition  -->

- ✓ **ARCH-01**: Document current state architecture of the Network Automation Ecosystem, including all existing tools and their interactions. — v1.0
- ✓ **ARCH-02**: Identify and document key data flows and integration interfaces between all ecosystem components. — v1.0
- ✓ **ARCH-03**: Research the broader network automation domain to identify current trends, competitor offerings, and best practices. — v1.0
- ✓ **ARCH-04**: Articulate the unique value proposition and product differentiation strategy for the ecosystem. — v1.0
- ✓ **ARCH-05**: Define high-level architectural principles and tenets guiding future development. — v1.0
- ✓ **ARCH-06**: Propose a structured approach for identifying and prioritizing future sub-projects (e.g., GNN Intelligence Layer, Legacy Ingestion). — v1.0
- ✓ **ARCH-07**: Summarize open architectural questions and areas requiring further deep-dive exploration. — v1.0

<!-- Milestone v1.1: Architecture Evolution & Refinement  -->

- ✓ **OQ-REQ-01, OQ-REQ-02, OQ-REQ-03**: Interface representation investigation (benchmarks, prototypes, RFC-03 decision) — v1.1
- ✓ **INT-REQ-01, INT-REQ-02, INT-REQ-03, INT-REQ-04**: Intelligence Layer architecture (telemetry, GNN training, inference, Live Hook) — v1.1
- ✓ **CLI-REQ-01, CLI-REQ-02, CLI-REQ-03, CLI-REQ-04**: CLI Scrape architecture (8-vendor, normalization, diff, multi-VRF) — v1.1
- ✓ **VIS-REQ-01, VIS-REQ-02, VIS-REQ-03**: [netvis](../netvis) decomposition (5 use cases, OQ-04 decision, Live Hook architecture) — v1.1
- ✓ **WB-REQ-01, WB-REQ-02, WB-REQ-03, WB-REQ-04**: Workbench orchestration (OQ-03 decision, workflows, parity, error handling) — v1.1

---

## # Active

<!-- Milestone v3.0: Implementation & Developer Enablement  -->

(Will be defined during v3.0 requirements phase)

---

## # Out of Scope

- **Immediate Code Changes:** The primary output is documentation and strategic guidance, not direct code modification.
- **Specific Model Training:** While the Intelligence Layer architecture will be defined, actual model training and tuning is implementation work.

*Last updated: 2026-02-28 after starting milestone v2.0*

---

## Current Status

2026-03-01 — v3.0 roadmap created with phases 18-22
