---
layout: default
section: network-automation
---

# Brownfield Ingestion & Analysis

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Use Cases](#use-cases)
- [Technical Depth](#technical-depth)
- [Current Status](#current-status)

## Concept

A specialized framework for **Brownfield Ingestion and Analysis**. It extracts high-level architectural intent and topology relationships from legacy network state—including vendor-specific CLI configurations and unstructured PDF documentation—normalizing them into a vendor-neutral model.

This system bridges the gap between existing deployments and the modern, declarative ANK toolchain. By leveraging LLM-powered RAG pipelines, it identifies complex protocol relationships and link roles that are often hidden in thousands of lines of manual configuration.

A network automation framework that decouples network configuration from vendor-specific syntax. It uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model inspired by AutoNetKit. The system enables cross-vendor configuration generation and validation through semantic simulation.

Extract network-level topology relationships (protocol adjacencies, link roles, VLAN membership) from vendor-specific CLI and documentation with high accuracy, enabling truly vendor-independent network configuration.

---

## Use Cases

- **Automated Network Audit**: Identify inconsistencies and compliance drifts across legacy multi-vendor estates.
- **Migration Planning**: Automatically generate "As-Is" topology models and protocol relationships for hardware refresh or greenfield migrations.
- **Intent Extraction**: Transform manual device configurations into structured, declarative models.

---

## Technical Depth

The system acts as the 'External Discovery' input for the Workbench, bridging the gap between existing brownfield deployments and the modern, declarative design toolchain.

---

## Current Status

2026-02-23 — Completed 05-06: Multi-Vendor Integration Testing

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
