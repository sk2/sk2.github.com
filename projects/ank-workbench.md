---
layout: default
---

# ANK Workbench

<span class="status-badge status-active">Phase 34/39 (42%)</span>

[← Back to Projects](../projects)

---

## The Insight

Network engineers can design, validate, and visualize network changes in one complete workflow without switching between separate tools or manually gluing components together.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 34/39 (42%) |
| **Language** | Python backend (FastAPI or Flask), React or Vue frontend — Leverages existing Python ecosystem for ANK components, meets modern UX expectations |
| **Started** | 2026 |

---
## What This Is

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

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
