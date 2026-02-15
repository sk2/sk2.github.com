---
layout: default
section: network-automation
---

# Network Automation Workbench

<span class="status-badge status-active">v1.3 — Tool Integration & Interactive Workflows</span>

[← Back to Network Automation](../network-automation)

---

## The Insight

Network engineers can design, validate, and visualize network changes in one complete workflow without switching between separate tools or manually gluing components together.

## Quick Facts

| | |
|---|---|
| **Status** | v1.3 — Tool Integration & Interactive Workflows |
| **Language** | Python backend (FastAPI), React frontend |
| **Started** | 2026 |

---

## What This Is

**An orchestration platform** that integrates the ecosystem tools (Topology Generator, Topology Modeling Library, Network Topology Engine, Network Simulator, Network Visualization Engine) into one seamless workflow.

The Network Automation Workbench is the **glue layer** that coordinates the entire network automation pipeline. Engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results — driven from YAML configuration, a text-based TUI, or the web interface.

**The Integration Vision:**
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              Network Automation Workbench                               │
│                    (Orchestration · Web UI · Workflow Management)                       │
│   ┌───────────────────┬──────────────────────┬─────────────────┬────────────────────┐  │
│   │ Topology Generator│ Topology Modeling     │ Network         │ Visualization      │  │
│   │                   │ Library + Engine      │ Simulator       │ Engine             │  │
└───┴───────────────────┴──────────────────────┴─────────────────┴────────────────────┴──┘
```

**Workflow:** Generate/model topology → Run simulation → Visualize results → Export configs

## Screenshots

![Projects](/images/workbench-projects.png)
*Projects landing page — create from scratch or start from curated sample topologies (spine-leaf, campus, OSPF multi-area, dual DC with BGP).*

![Topology Editor](/images/workbench-editor.png)
*Topology editor — drag devices from the palette, edit YAML directly with live validation, and browse sample configurations.*

![Workflow & Simulation](/images/workbench-workflow.png)
*Workflow view — configure simulation parameters (protocol, tick count, timeout), run simulations, and control the simulator lifecycle.*

![Visualization](/images/workbench-visualize.png)
*Visualization view — explore topology, physical, logical, and protocol layers with configurable overlays, routing table inspection, and multi-format export.*

## Milestones

**v1.0 Foundation** (Shipped Feb 4, 2026)
End-to-end workflow: define topology → simulate → visualize.

**v1.1 UX Polish & Onboarding** (Shipped Feb 9, 2026)
Help system, sample gallery, empty states, guided tour.

**v1.2 Scale-First Visualization** (98% complete)
Performance benchmarks, worker-first compute, GPU renderer, scale navigation.

**v1.3 Tool Integration & Interactive Workflows** (In Progress)
- Interactive device access — click a node to open a terminal into the simulated device
- Simulator integration & control — start/stop/reset, stream progress and state
- Config export pipeline — generate from the Topology Modeling Library, preview, download
- Topology generation — Topology Generator patterns available in UI
- Live simulation observability — watch protocol convergence and routing updates

**Roadmap:**

- **Complete v1.2 Scale-First Visualization** — Paused at 98% to focus on tool integration; remaining work includes stub indicators for hidden connections, scale-first view state persistence, and simulation overlays in scale-first mode
- **v1.4 and beyond** — Multi-user collaboration, version-controlled topology projects, CI/CD pipeline integration for topology validation workflows

---

[← Back to Network Automation](../network-automation)
