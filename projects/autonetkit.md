---
layout: default
section: network-automation
---

# Configuration Generation (AutoNetkit)

<span class="status-badge status-active">Active</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A compiler-based framework for automated network provisioning. AutoNetkit transforms high-level network designs into validated device configurations across heterogeneous hardware and protocol environments.

Traditional network configuration is manual and vendor-specific. AutoNetkit introduces a declarative approach where engineers define the network design, and the engine handles the transformations required to generate protocol parameters and CLI commands.

---

## Architecture

AutoNetkit employs a multi-stage transformation pipeline:

1. **Specification Abstraction**: captures the high-level design intent
2. **Intermediate Representation**: a network-wide graph model that maintains cross-vendor consistency, separating design requirements from device-specific implementation
3. **Device Specialization**: transforms the abstract model into device-specific protocol state through explicit, reversible compiler passes
4. **Template Assembly**: generates final CLI commands using verified vendor templates with deterministic ordering for diff-friendly output

---

## Features

- Automated IP addressing: loopback and link subnet allocation across protocol layers
- Protocol orchestration: OSPF areas, IS-IS levels, BGP peering (iBGP/eBGP) generated from design intent
- Multi-vendor output: Cisco (IOS, XR, NX-OS), Juniper (JunOS), Arista (EOS)
- Multi-target backends: vendor CLIs and structured formats (JSON/YAML) for tooling and audit workflows
- Visual feedback: topological diagrams for verifying physical and logical structure

---

## Impact

Earlier iterations of AutoNetkit were integrated into industry tooling for automated lab provisioning. That integration reflects the lineage of the approach, not the current in-progress implementation.

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
