---
layout: default
section: network-automation
---

# Network Configuration Parser

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

Ingestion pipeline for vendor documentation and configuration files. Extracts structured, searchable knowledge from PDFs and CLI output, making vendor-specific configuration details accessible to downstream automation tools.

---

## Features

- Layout-aware PDF ingestion (pymupdf4llm + MinerU) preserving tables, hierarchies, and code blocks
- Semantic search via ChromaDB vector store — find configuration guidance by describing intent, not memorizing commands
- Standardized output targeting YANG/OpenConfig models for consumption by the Network Modeling & Configuration Library
- FastAPI backend with endpoints for ingestion pipelines and search queries

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
