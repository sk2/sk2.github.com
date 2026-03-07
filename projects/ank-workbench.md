---
layout: default
section: network-automation
---

# Network Automation Workbench

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Screenshots](#screenshots)
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

## Concept

Orchestration platform that integrates the ANK ecosystem tools — [Topology Generator](/projects/topogen), [Network Modeling & Configuration Library](/projects/ank-pydantic), [Network Simulator](/projects/netsim), [Network Visualization Engine](/projects/netvis) — into a single web interface. Engineers define topologies, generate configurations, run simulations, and inspect results without switching between CLI tools.

```
┌──────────────────────────────────────────────────────────────────┐
│                  Network Automation Workbench                    │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │  ank-pydantic│   Simulator  │    NetVis    │ │
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

## Screenshots

![Projects](/images/workbench-projects.png)
*Projects landing page — create from scratch or start from curated sample topologies.*

![Topology Editor](/images/workbench-editor.png)
*Topology editor — drag devices, edit YAML with live validation, browse sample configurations.*

![Workflow & Simulation](/images/workbench-workflow.png)
*Workflow view — configure simulation parameters, run simulations, control the simulator lifecycle.*

![Visualization](/images/workbench-visualize.png)
*Visualization view — explore layers with configurable overlays, routing tables, and multi-format export.*

---

## Current Status

v4.2 UX Polish & Accessibility shipped 2026-03-04. 93 phases across 5 milestones completed. Now in maintenance phase.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/ank-workbench-techreport.pdf)

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
