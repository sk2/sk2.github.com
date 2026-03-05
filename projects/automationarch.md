---
layout: default
section: network-automation
---

# Network Automation Ecosystem - Overall Architecture Definition

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Why We're Doing This](#why-were-doing-this)
- [Success Metrics](#success-metrics)
- [Key Decisions](#key-decisions)
- [Documentation conventions](#documentation-conventions)
- [Current State](#current-state)
- [Current Milestone: v3.0 Implementation & Developer Enablement](#current-milestone-v30-implementation-developer-enablement)
- [Current Status](#current-status)

## Concept

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

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
- 9 tool repositories documented (topogen, autonetkit, netsim, netflowsim, netvis, Workbench, configparsing, deviceinteraction, netassure)
- 5 ADRs (contract-first, interface representation, orchestration, netvis scope, netassure decomposition)
- 6 RFCs (RFC-01 Topology, RFC-02 Live Stream, RFC-03 Interface Representation, RFC-TELEM-01, RFC-INFER-01, RFC-PRED-01)
- 41,000+ lines of architecture documentation across 100+ files

---

## Current Milestone: v3.0 Implementation & Developer Enablement

**Goal:** Bridge the gap between architecture definition (v1.0-v2.0) and implementation by creating comprehensive implementation guides, API references, SDK design patterns, and developer onboarding materials.

**Strategic Shift:** From "what to build" (architecture specs) to "how to build it" (implementation guidance)

**Target capabilities:**
- **netassure Implementation Guides** — API reference, formal verification cookbook, graph algorithm patterns, ML/GNN integration examples
- **Live Hook Developer SDK** — Client library design patterns, WebSocket protocol implementation guide, state reconciliation patterns, event replay handling
- **CLI Scrape Extension Kit** — Vendor integration guide (adding new platforms), parser development patterns, normalization rule authoring, multi-VRF edge case handling
- **Workbench Integration Patterns** — Workflow engine implementation guide, orchestration library usage, CLI/TUI feature parity checklist, error handling best practices

**Timeline:** 2-3 weeks (medium scope)

<details>
<summary>Previous Milestones</summary>

---

## # v1.1 Architecture Evolution & Refinement (shipped 2026-02-28)

- Resolved 3 open architectural questions (OQ-02, OQ-03, OQ-04) with ADRs and RFCs
- Created 9-tool ecosystem architecture (added netassure as standalone advanced analysis engine)
- Defined comprehensive intelligence layer (telemetry infrastructure, GNN training pipeline, dual deployment, Live Hook integration)
- Architected CLI scrape tool (8-vendor legacy ingestion, normalization, diff engine, multi-VRF)
- Established Live Hook architecture (multiplexed WebSocket, fold-on-client state, retention/keyframes for timeline scrubbing)
- Documented 5 advanced analysis paradigms in netassure (formal verification, graph algorithms, failure cascades, ML/GNN, optimization)
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
- ✓ **VIS-REQ-01, VIS-REQ-02, VIS-REQ-03**: netvis decomposition (5 use cases, OQ-04 decision, Live Hook architecture) — v1.1
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

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
