---
layout: default
section: network-automation
---

# Network Configuration Parser

<span class="status-badge status-active">Phase 1 — Knowledge Base Ingestion</span>

[← Back to Network Automation](../network-automation)

---

## Concept

Network automation is often blocked by the "Legacy Wall"—thousands of lines of vendor-specific CLI configuration that must be understood before they can be automated. The **Network Configuration Parser** (ank-parse) acts as a "Digital Archaeologist," using LLM-assisted ingestion and semantic search to normalize legacy configurations into vendor-agnostic YANG/OpenConfig models.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1 — Knowledge Base Ingestion |
| **Language** | Python |
| **Tech Stack** | FastAPI, ChromaDB, pymupdf4llm, MinerU |
| **Role** | Normalization & Ingestion |

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

## Integration

The Network Configuration Parser sits at the beginning of the automation pipeline:
1. **Ingest**: Read legacy configs and vendor manuals.
2. **Normalize**: Convert to generic models via `ank-parse`.
3. **Model**: Import into the **Network Modeling & Configuration Library**.
4. **Validate**: Run through the **Network Simulator**.

## Tech Stack

- **FastAPI**: Asynchronous API for ingestion and search.
- **ChromaDB**: Vector database for storing and retrieving manual embeddings.
- **all-MiniLM-L6-v2**: Efficient sentence embeddings for semantic search.
- **pymupdf4llm / MinerU**: Advanced PDF-to-Markdown extraction.

---

[← Back to Network Automation](../network-automation)
