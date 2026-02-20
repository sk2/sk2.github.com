---
layout: default
---

# Network Configuration Parser

<span class="status-badge status-active">Phase 1 — Knowledge Base Ingestion</span>

[← Back to Projects](../projects)

---

## The Insight

Developing...

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1 — Knowledge Base Ingestion |
| **Language** | Python |
| **Started** | 2026 |

---
## What This Is

A framework for parsing and analyzing device configurations across multiple networking vendors. The project bridges the gap between unstructured legacy CLI data and structured intent-based models. 

Phase 1 focuses on building the **Knowledge Base**: ingesting thousands of pages of vendor manuals (PDFs) and converting them into high-fidelity Markdown. This creates a searchable, semantically-indexed reference that AI agents can use to accurately interpret vendor-specific syntax.

## Problem It Solves

- **Syntax Fragmentation**: Every vendor (Cisco, Juniper, Arista, Nokia) has a different CLI structure for the same protocol (OSPF, BGP).
- **Manual Translation**: Engineers spend hours cross-referencing manuals to convert a "design" into "commands."
- **Data Silos**: Configuration state is locked in text files rather than queryable databases.

## Features

- **Layout-Aware Ingestion**: Uses `pymupdf4llm` and `MinerU` to preserve tables, hierarchies, and code blocks from vendor PDFs.
- **Semantic Search**: Vector store integration (ChromaDB) enables "Search by Intent"—find how to configure a feature by describing its function, not just its command.
- **Unified Model Target**: Designed to output standardized YANG/OpenConfig models, enabling downstream tools like the Network Modeling & Configuration Library to consume legacy state.
- **API-First**: FastAPI backend provides endpoints for ingestion pipelines and search queries.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
