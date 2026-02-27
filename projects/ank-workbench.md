---
layout: default
section: network-automation
---

# Automation Workbench

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Key Capabilities](#key-capabilities)
- [Screenshots](#screenshots)
- [Visuals](#visuals)

## Concept

**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow. It serves as the **glue layer** that coordinates the entire network automation pipeline, allowing engineers to generate topologies, model networks declaratively, run lightweight simulations, and visualize results from a unified interface.

```
┌──────────────────────────────────────────────────────────────────┐
│                        ANK Workbench                             │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │ ank-pydantic │   Simulator  │    NetVis    │ │
└───┴──────────────┴──────────────┴──────────────┴──────────────┴─┘
```

---

## Key Capabilities

- **Design-First Workflow**: Declarative Pydantic models → lightweight simulation → integrated topology/config/behavior visualization.
- **Persistent Help System**: Non-modal drawer with contextual tips and route-aware visibility.
- **Sample Gallery**: Curated offline topologies ranging from 2-node starters to 12-node spine-leaf data centers.
- **Intelligent Empty States**: Cause-specific UI patterns with outcome previews to guide new users.
- **Guided Tour**: 8-step workflow coverage with CSS-only spotlight for rapid onboarding.

---

## Screenshots

![Projects](/images/workbench-projects.png)
*Projects landing page — create from scratch or start from curated sample topologies (spine-leaf, campus, OSPF multi-area, dual DC with BGP).*

![Topology Editor](/images/workbench-editor.png)
*Topology editor — drag devices from the palette, edit YAML directly with live validation, and browse sample configurations.*

![Workflow & Simulation](/images/workbench-workflow.png)
*Workflow view — configure simulation parameters (protocol, tick count, timeout), run simulations, and control the simulator lifecycle.*

![Visualization](/images/workbench-visualize.png)
*Visualization view — explore topology, physical, logical, and protocol layers with configurable overlays, routing table inspection, and multi-format export.*

---

## Visuals

The Workbench provides real-time feedback through integrated NetVis overlays, allowing for the inspection of physical, logical, and protocol layers alongside routing table state and simulation diagnostics.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
