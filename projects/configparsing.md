---
layout: default
section: network-automation
---

# Brownfield Ingestion & Analysis

<span class="status-badge status-active">Recently Updated</span>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

A specialized framework for **Brownfield Modernization** and **Automated Audits**. It extracts high-level architectural intent and topology relationships from legacy network state—including vendor-specific CLI configurations and unstructured PDF documentation—normalizing them into a vendor-neutral model.

This system bridges the gap between existing "un-automated" deployments and the modern, declarative ANK toolchain. By leveraging LLM-powered RAG pipelines, it identifies complex protocol relationships and link roles that are often hidden in thousands of lines of manual configuration.

Extract network-level intent (protocol adjacencies, link roles, VLAN membership) from legacy data with high accuracy, enabling truly vendor-independent network modernization and compliance verification.

---

## Use Cases

- **Automated Network Audit**: Rapidly identify inconsistencies and compliance drifts across legacy multi-vendor estates.
- **Migration Planning**: Automatically generate "As-Is" topology models and protocol relationships for hardware refresh or greenfield migrations.
- **Intent Extraction**: Transform manual, "pet-like" device configurations into structured, "cattle-like" declarative models.

---

## Technical Depth

The system acts as the 'External Discovery' input for the Workbench, bridging the gap between existing brownfield deployments and the modern, declarative design toolchain.

---

## Current Status

2026-02-23 — Completed 05-06: Multi-Vendor Integration Testing

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
