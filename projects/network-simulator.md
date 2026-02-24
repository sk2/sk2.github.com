---
layout: default
section: network-automation
---

# Network Simulator

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Use Cases](#use-cases)
- [Tech Stack](#tech-stack)
- [Roadmap](#roadmap)

## Concept

### What This Is

A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation. Used for smoke testing and design validation of network configurations.

**Current state:** v1.7 shipped. Planning v1.8.
**Future Roadmap Ideas:** See [.planning/FUTURE_IDEAS.md](FUTURE_IDEAS.md) for long-term innovation and technical debt backlog.

### Core Value

Validate network configurations at scale with protocol-level fidelity before deploying to real infrastructure.

---

## Use Cases

- **Agentic AI & Network Automation Development**: Rapidly prototype and test automation agents, DevOps pipelines, and AI-driven network operations with seconds-long iteration cycles instead of minutes spinning up containers
- **Configuration Generation Testing**: Validate Network Modeling & Configuration Library-generated configs in simulation before deploying to Containerlab — catch errors in the generation logic early
- **Network Automation Prototyping**: Develop configuration management tools, automated provisioning systems, and orchestration scripts against realistic network topologies without infrastructure overhead
- **Pre-deployment Validation**: Catch routing loops, black holes, and misconfigurations before production
- **Convergence Analysis**: Measure failover time and validate backup paths
- **Training**: Safe environment for learning routing protocol behavior and automation development

---

## Tech Stack

Rust, Tokio for async execution, petgraph for topology representation, gRPC for daemon IPC, ratatui for TUI

---

## Roadmap

- v1.9 Advanced Impairments & Topology Patterns
- v1.10 Engine Hardening & Protocol Fidelity
- v1.11 Advanced Analysis & Assertions

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
