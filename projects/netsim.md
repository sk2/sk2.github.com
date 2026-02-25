---
layout: default
section: network-automation
---

# Network Simulator

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Automation](#automation)
- [Current Status](#current-status)
- [Roadmap](#roadmap)

## Concept

A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation. Used for smoke testing and design validation of network configurations.

**Current state:** v1.7 shipped. Planning v1.8.
**Future Roadmap Ideas:** See [.planning/FUTURE_IDEAS.md](FUTURE_IDEAS.md) for long-term innovation and technical debt backlog.

Validate network configurations at scale with protocol-level fidelity before deploying to real infrastructure.

---

## Automation

**Python bindings (PyO3):**

```python
import netsim_py

engine = netsim_py.Engine()
engine.load_topology("topology.yaml")
engine.run_until_converged()
engine.execute_command("router1", "show ip route")
```

---

## Current Status

2026-02-25 — Completed 67-04-PLAN.md

---

## Roadmap

- **v1.9 Advanced Impairments & Topology Patterns** (Proposed) — Phases 97-100
- **v1.10 Engine Hardening & Protocol Fidelity** (Proposed) — Phases 111-115
- **v1.11 Advanced Analysis & Assertions** (Proposed) — Phases 116-119
- **v2.0 IPv6 Foundation** (Proposed) — Phases 68-72
- **v2.1 Enterprise & Campus Protocols** (Proposed) — Phases 73-74

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
