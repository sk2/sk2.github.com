---
layout: default
---

# ANK Workbench

<span class="status-badge status-active">v1.1 Complete</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | v1.1 shipped (Feb 9, 2026) |
| **Stack** | Python (FastAPI) + React + TypeScript |
| **Latest Release** | v1.1 UX Polish + Onboarding |
| **Milestone Score** | 50/50 (100%) |
| **Started** | 2025 |
| **License** | Commercial/TBD |

---

## Overview

ANK Workbench is a unified network simulation and visualization platform for enterprise network engineers. It integrates ANK Pydantic models, simulator, and visualization into a seamless end-to-end workflow.

## Problem It Solves

Network engineers need to test designs before production deployment. Current challenges:

**Fragmented Workflows:**
- Separate tools for design, simulation, and visualization
- Manual integration between components
- Context switching between applications
- Inconsistent data formats

**Manual Testing:**
- Error-prone CLI configuration
- Difficult to reproduce scenarios
- Time-consuming to test changes
- Risk of production outages

**ANK Workbench provides:**
- Declarative network design with Pydantic models
- Lightweight mathematical simulation
- Integrated visualization (topology, config, behavior)
- Single unified workflow

## Core Value

Design, validate, and visualize network changes in one complete workflow without switching between tools or manual integration.

## Architecture

### Tech Stack

**Backend:** FastAPI (Python)
- REST API for topology operations
- Simulation orchestration
- Configuration generation
- WebSocket for real-time updates

**Frontend:** React + TypeScript
- Modern web UI (no VNC required)
- Real-time visualization updates
- Interactive topology editor
- Guided onboarding system

**Integration:**
- ANK Pydantic for type-safe models
- ANK simulator for lightweight simulation
- netvis for topology visualization

### Workflow

```
Design → Simulate → Visualize
  ↓         ↓          ↓
Pydantic  Light-    Integrated
 Models   weight     Topology +
          Sim       Config + Behavior
```

No context switching between tools. Everything in one interface.

## Features

### v1.1 UX Polish + Onboarding (Feb 9, 2026)

**Persistent Help System:**
- Non-modal help drawer accessible from all screens
- 16 contextual tips with route-aware visibility
- Per-route dismissal persistence
- Markdown documentation with safe local navigation
- First-time indicator (blue pulse) on Help button
- Reset onboarding control for testing/demos

**Curated Sample Gallery:**
- 5 offline sample topologies:
  - 2-node starter topology
  - Enterprise campus network
  - Data center spine-leaf (12 nodes)
  - WAN routing scenario
  - Protocol demonstration
- Search/filter by name, description, tags
- Copy semantics preserve original samples
- Deterministic offline loading (no network required)

**Intelligent Empty States:**
- Cause-specific empty states (no projects, no topology defined, simulation not run)
- Outcome preview pattern (explains what will appear after action)
- Inline actions (Add Router button) and navigation links (Browse Samples)
- Professional text-focused design for technical audience

**Guided Tour System:**
- 8-step tour covering full workflow:
  1. Intro to ANK Workbench
  2. Create new project
  3. Edit topology (add devices, links)
  4. View YAML representation
  5. Generate configurations
  6. Run simulation
  7. Visualize results
  8. Export configs
- CSS-only spotlight (no layout shift, aria-modal=false)
- 3 resilience fallback strategies (skip/text-only/end)
- Multiple entry points (Help drawer, Get Started page, first-run auto-offer)
- State persistence across browser sessions

**Metrics:**
- 101 files modified
- 30 feature commits
- 8.6 hours execution time
- 28 integration points verified

### Core Capabilities

**Declarative Design:**
Define networks using type-safe Pydantic models. Validation at definition time catches errors early.

**Lightweight Simulation:**
Mathematical simulation (not VM emulation). Faster iteration cycles, lower resource requirements. Validates routing, reachability, and behavior.

**Integrated Visualization:**
- Topology view: Network structure with devices and links
- Configuration view: Generated device configs
- Simulation view: Routing tables, packet flows, convergence

**Save/Load Projects:**
Full state persistence. Save topology, configs, simulation results. Load and continue later.

**Export Configurations:**
Generate device configs for production deployment. Multi-vendor support via ANK Pydantic compilers.

## Use Cases

**Pre-Deployment Validation:**
Test network changes before production. Verify routing, check reachability, validate failover scenarios.

**Network Design Exploration:**
Try different topologies and configurations. Compare approaches. Make informed decisions before implementation.

**Training and Learning:**
Safe environment to learn network protocols and behavior. Experiment without breaking production.

**Documentation:**
Generate network diagrams and configuration documentation from single source of truth.

## Development Status

**v1.1 Complete** (Feb 9, 2026) - Production-ready onboarding experience

**Active Requirements:**
- Define network topologies using declarative Pydantic models
- Configure devices with type-safe, validated configurations
- Run lightweight network simulations
- Visualize topology, config state, simulation results
- Save/load projects with full state persistence
- Export generated device configurations
- Web UI, API, and CLI interfaces

**Next:** Planning v1.2 milestone (TBD)

## Target Users

**Enterprise Network Engineers:**
- Test network designs before production deployment
- Troubleshoot and replicate production issues in safe environment
- Design and plan network changes with validation
- Learn and experiment with network behavior

## Links

- **GitHub:** Private (commercial product)
- **Related:** [ank-pydantic](ank-pydantic) provides model layer

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Main UI with topology editor
- Sample gallery with topologies
- Guided tour in action
- Help drawer with contextual tips
- Empty state examples
- Visualization views (topology, config, simulation)
- Configuration export
-->
