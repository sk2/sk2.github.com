---
layout: default
section: network-automation
---

# Brownfield Ingestion & Analysis

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span>
</div>

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Current Status](#current-status)

## Concept

Vendor translation layer that decouples network configuration from vendor-specific syntax. Uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model. The intermediate representation is topology-centric (protocol adjacencies, link roles, VLAN membership) rather than device-centric like YANG, enabling genuine vendor abstraction.

---

## Architecture

The pipeline has four stages:

1. **Document ingestion**: PDF/HTML vendor manuals converted to Markdown, indexed into a vector database (ChromaDB) for RAG retrieval. Dual-engine parsing — pymupdf4llm for fast extraction, MinerU for layout-aware fallback.

2. **Intent extraction**: LLM + RAG extracts topology-level relationships from unstructured documentation and CLI configurations. Every extraction carries a confidence score and evidence citation.

3. **Human-in-the-loop review**: Low-confidence extractions routed to a web UI for operator review. Corrections feed back to improve model accuracy.

4. **Configuration generation**: Topology model compiled to vendor-specific CLI (Cisco IOS, Arista EOS). Batfish validates semantic correctness — compiled configs are simulated to verify they produce the intended forwarding behavior.

Built with Python 3.12, FastAPI, ChromaDB, LangChain.

---

## Current Status

v2.0 Production-Grade Translation Layer in progress. v1.0 shipped 2026-02-22 with full end-to-end pipeline validated against real-world configs.

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
