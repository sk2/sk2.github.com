---
layout: default
---

# ANK Workbench

<span class="status-badge status-active">Phase 36/39 (44%)</span>

[← Back to Projects](../projects)

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
