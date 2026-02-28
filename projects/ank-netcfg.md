---
layout: default
section: network-automation
---

# Network Configuration Framework

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A modern, type-safe configuration engine that serves as a successor and sibling to the original AutoNetkit research. It implements the same 'Whiteboard -> Plan -> Build' transformation model but utilizes a modern, schema-enforced pipeline to ensure configuration correctness across heterogeneous network fleets.

Deterministic, auditable, CI/CD-friendly network compiler.

---

## Technical Depth

Sitting alongside the core ANK toolchain, ank_netcfg focuses on the high-fidelity transformation of network intent into vendor-specific device states. It provides the protocol-level intelligence needed to generate consistent OSPF, BGP, and MPLS configurations while maintaining strict type safety via a Pydantic-based model layer.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current State

complete. Foundation established for declarative transformation engine and vendor-neutral configuration generation.

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
