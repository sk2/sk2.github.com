---
layout: default
section: network-automation
---

# Network Automation Workbench

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Screenshots](#screenshots)
- [Features](#features)
- [Status](#status)
- [Technical Reports](#technical-reports)

## Concept

Orchestration platform that integrates the ANK ecosystem tools — [Topology Generator](../topogen), [Network Modeling & Configuration Library](../ank_pydantic), [Network Simulator](../netsim), [Network Visualization Engine](../netvis) — into a single web interface. Engineers define topologies, generate configurations, run simulations, and inspect results without switching between CLI tools.

```
┌──────────────────────────────────────────────────────────────────┐
│                  Network Automation Workbench                    │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │ ank_pydantic │   Simulator  │    NetVis    │ │
│   └──────────────┴──────────────┴──────────────┴──────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

The workflow follows a linear pipeline: generate or model a topology, run a simulation against it, visualize the results, and export device configurations. Each stage delegates to a specialized tool; the workbench coordinates the handoffs and presents a unified project context across all stages.

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

## Features

**Project Management.**
Create, save, and load network projects with full state persistence. A curated sample gallery provides starter topologies (spine-leaf, hub-spoke, mesh, ring, campus 3-tier) so new users can begin working immediately.

**Topology Editing.**
Drag-and-drop device placement on a canvas. Hold Shift and drag to draw links between nodes, which generates the underlying logical interfaces automatically. YAML editor with live validation sits alongside the visual editor. Topology generation supports parameterized patterns with preview before committing.

**Configuration Generation.**
Generate device configurations from [Network Modeling & Configuration Library](../ank_pydantic) models with syntax-highlighted preview. Download individual configs as `.txt` or batch-export as `.zip`. Vendor config language support covers Arista and Cisco syntax.

**Simulation Control.**
Start, stop, and reset the [Network Simulator](../netsim) with a lifecycle state machine. Protocol event timeline shows OSPF, IS-IS, and BGP convergence. Click any node to open an interactive terminal session via WebSocket relay.

**Visualization.**
Explore topology, physical, logical, and protocol layers. Routing table inspection per device. Export to SVG and PDF. Configurable overlays for protocol state and traffic flow.

**Container Lab Integration.**
Deploy topologies to Container Lab for full device emulation. Lifecycle management handles deploy, destroy, orphan detection, and Docker preflight checks. Click-to-terminal access into running containers.

**CI/CD and IaC Export.**
Export GitOps bundles with generated GitHub Actions and GitLab CI validation pipelines. Generate Terraform HCL and Ansible playbooks from the internal topology model.

**Command Palette.**
`Cmd+K` palette for keyboard-driven access to exports, pipeline runs, and navigation.

---

## Status

**Current version:** v4.2 — shipped 2026-03-04.

93 phases across 5 major milestones completed. The project is functionally complete, type-safe, and covered by end-to-end Playwright tests.

Recent releases:

| Version | Date | Summary |
|---------|------|---------|
| v4.2 | 2026-03-04 | Toast notifications, command palette, visual link drawing, contextual tooltips |
| v4.1 | 2026-03-04 | Strict mypy pass (200+ warnings resolved), code deduplication, Playwright E2E tests |
| v4.0 | 2026-03-04 | CI/CD export, IaC generation (Terraform, Ansible), JWT-based RBAC |
| v3.2 | 2026-03-04 | Monte Carlo flow simulation, distributed multi-host execution, capacity pre-flight |
| v3.1 | 2026-03-04 | NetAuto manifest persistence, external provider import, dissonance remediation |

**Stack:** FastAPI backend, React frontend, WebSocket event bus for real-time progress.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/ank-workbench-techreport.pdf)

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
