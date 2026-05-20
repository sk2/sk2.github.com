---
layout: default
section: network-automation
description: "Orchestration platform that integrates the ANK ecosystem tools — Topology Generator, Network Modeling & Configuration Library, Network Simulator, Network…"
---

# Network Automation Workbench

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-04-06</span>
  <span class="stack-badge">Python</span>
</div>

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Current Status](#current-status)
- [Roadmap](#roadmap)

## Concept

Orchestration platform that integrates the ANK ecosystem tools — [Topology Generator](/projects/topogen), [Network Modeling & Configuration Library](/projects/ank-pydantic), [Network Simulator](/projects/netsim), [Network Visualization Engine](/projects/netvis) — into a single web interface. Engineers define topologies, generate configurations, run simulations, and inspect results without switching between CLI tools.

```
┌──────────────────────────────────────────────────────────────────┐
│                  Network Automation Workbench                    │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │  [ank-pydantic](../ank-pydantic)│   Simulator  │    NetVis    │ │
│   └──────────────┴──────────────┴──────────────┴──────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

The workflow follows a linear pipeline: generate or model a topology, run a simulation against it, visualize the results, and export device configurations. Each stage delegates to a specialized tool; the workbench coordinates the handoffs and presents a unified project context across all stages.

---

## Features

**Topology Editing.** Drag-and-drop device placement on a canvas. Hold Shift and drag to draw links between nodes. YAML editor with live validation alongside the visual editor.

**Configuration Generation.** Generate device configurations from models with syntax-highlighted preview. Download individual configs or batch-export as `.zip`. Arista EOS and Cisco IOS-XR support.

**Simulation Control.** Start, stop, and reset the [Network Simulator](/projects/netsim) with a lifecycle state machine. Protocol event timeline shows OSPF, IS-IS, and BGP convergence. Click any node for interactive terminal via WebSocket relay.

**Visualization.** Explore topology, physical, logical, and protocol layers. Routing table inspection per device. Export to SVG and PDF.

**Container Lab Integration.** Deploy topologies to Container Lab for full device emulation. Lifecycle management, orphan detection, and click-to-terminal access.

**CI/CD & IaC Export.** Export GitOps bundles with GitHub Actions/GitLab CI pipelines. Generate Terraform HCL and Ansible playbooks.

**Command Palette.** `Cmd+K` for keyboard-driven access to exports, pipeline runs, and navigation.

---

## Current Status

**Last shipped:** v9.0 DPI UI, Validation Pre-Flight Gate, Batch Simulation, Dry-Run Mode, Dissonance Visualizer, Error Boundary, Terminal Search, Anomaly Detection, Typed Chaos Scenarios, JWT Refresh Tokens, Rate Limiting — shipped through 2026-04-19
**v9.0 status:** All four strategic pillars complete as of 2026-04-19

---

## Roadmap



---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Python, TypeScript |

---

## What This Is

**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, [ank_pydantic](../ank_pydantic), Network Simulator, NetVis) into one seamless workflow.

ANK Workbench is the **glue layer** that coordinates the entire network automation pipeline. Engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results—all from a unified web interface. No more context switching between separate tools or manually stitching components together.

**The Integration Vision:**
```
┌──────────────────────────────────────────────────────────────────┐
│                        ANK Workbench                             │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │ [ank_pydantic](../ank_pydantic) │   Simulator  │    NetVis    │ │
└───┴──────────────┴──────────────┴──────────────┴──────────────┴─┘
```

**Workflow:** Generate/model topology → Run simulation → Visualize results → Export configs
**Value:** Complete pipeline in one interface, no tool-switching or manual integration

---

## Core Value

Network engineers can design, validate, and visualize network changes in one complete workflow without switching between separate tools or manually gluing components together.

---

## Screenshots

![Projects](../screenshots/02-projects.png)
*Projects landing page with editorial typography, template gallery, and project showcase cards.*

![Topology Editor](../screenshots/05-editor.png)
*Topology editor with live validation, policy violation badges, and design hint tooltips.*

![Workspace](../screenshots/04-workspace.png)
*Project workspace with pipeline controls, canvas, and YAML panel.*

![Visualization](../screenshots/06-visualize.png)
*Visualization view with configurable overlays, workflow stepper, and multi-format export.*

---

## What We've Built



---

## # v4.2 UX Polish & Accessibility (Complete)

*Toast notifications, Cmd+K palette, Visual link drawing, Contextual tooltips.*

---

## Requirements



---

## # Out of Scope

- Multi-host/distributed Container Lab deployments — Single-host labs only for v1.6
- Automatic remediation application for policy violations — v9.0 focuses on visualization and hints.

*Last updated: 2026-03-14 after adding future work ideas*

---

## Current Status

** 2026-04-06 - Completed 120-03-PLAN.md (hardware polling API endpoint)
