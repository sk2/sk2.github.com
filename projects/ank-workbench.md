---
layout: default
---

# ANK Workbench

<span class="status-badge status-active">v1.3 — Tool Integration & Interactive Workflows</span>

[← Back to Projects](../projects)

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

**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, NTE, Network Simulator, NetVis) into one seamless workflow.

ANK Workbench is the **glue layer** that coordinates the entire network automation pipeline. Engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results — all from a unified web interface.

**The Integration Vision:**
```
┌──────────────────────────────────────────────────────────────────┐
│                        ANK Workbench                             │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │ ank_pydantic │   Simulator  │    NetVis    │ │
│   │              │   + NTE      │              │              │ │
└───┴──────────────┴──────────────┴──────────────┴──────────────┴─┘
```

**Workflow:** Generate/model topology → Run simulation → Visualize results → Export configs

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
- Config export pipeline — generate from ank_pydantic, preview, download
- Topology generation — TopoGen patterns available in UI
- Live simulation observability — watch protocol convergence and routing updates

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)
