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
- [Current Milestone: v1.1 Architecture Evolution & Refinement](#current-milestone-v11-architecture-evolution-refinement)
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

## Current Milestone: v1.1 Architecture Evolution & Refinement

**Goal:** Evolve the architecture through open question resolution, sub-project deep-dives, and ongoing maintenance as tools develop.

**Target features:**
- Complete OQ-02 investigation (interface representation) with benchmark, prototype, and RFC-03 decision
- Define detailed architecture for Intelligence Layer (GNN + Telemetry integration)
- Define detailed architecture for CLI Scrape (legacy ingestion across 8 vendors)
- Resolve OQ-04 with detailed netvis decomposition and Live Hook architecture
- Resolve OQ-03 with Workbench orchestration architecture (shared vs web-only)
- Maintain and evolve core architecture docs as implementation proceeds

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

---

## # Active

<!-- Milestone v1.1: Architecture Evolution & Refinement -->

(Will be defined in REQUIREMENTS.md during milestone initialization)

---

## # Out of Scope

- **Immediate Code Changes:** The primary output is documentation and strategic guidance, not direct code modification.
- **Specific Model Training:** While the Intelligence Layer architecture will be defined, actual model training and tuning is implementation work.

*Last updated: 2026-02-21 after milestone v1.0 completion and v1.1 initialization*

---

## Current Status

2026-02-25 - Completed plan 11-03

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
