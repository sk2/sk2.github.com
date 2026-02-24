---
layout: default
section: network-automation
---

# Automation Workbench

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow.

ANK Workbench is the **glue layer** that coordinates the entire network automation pipeline. Engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results—all from a unified web interface. No more context switching between separate tools or manually stitching components together.

**The Integration Vision:**
```
┌──────────────────────────────────────────────────────────────────┐
│                        ANK Workbench                             │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │ ank_pydantic │   Simulator  │    NetVis    │ │
└───┴──────────────┴──────────────┴──────────────┴──────────────┴─┘
```

**Workflow:** Generate/model topology → Run simulation → Visualize results → Export configs
**Value:** Complete pipeline in one interface, no tool-switching or manual integration

Network engineers can design, validate, and visualize network changes in one complete workflow without switching between separate tools or manually gluing components together.

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

## Current Status

2026-02-24 — Completed 43-06-PLAN.md

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
