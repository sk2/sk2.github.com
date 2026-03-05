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

- [What This Is](#what-this-is)
- [Core Value](#core-value)
- [Current Milestone: v2.0 Production-Grade Translation Layer](#current-milestone-v20-production-grade-translation-layer)
- [Requirements](#requirements)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## What This Is

A network automation framework that decouples network configuration from vendor-specific syntax. It uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model inspired by AutoNetKit. The system enables cross-vendor configuration generation and validation through semantic simulation.

---

## Core Value

Extract network-level topology relationships (protocol adjacencies, link roles, VLAN membership) from vendor-specific CLI and documentation with high accuracy, enabling truly vendor-independent network configuration.

---

## Current Milestone: v2.0 Production-Grade Translation Layer

**Goal:** Become the universal, production-ready vendor translation layer for the network automation ecosystem

**Target features:**
- Broader vendor coverage (Juniper, Nokia, F5, Palo Alto) and protocols (MPLS, SR, SRv6)
- Higher extraction accuracy with reduced HITL burden
- Ecosystem integration (RFC-01 compliance, autonetkit interop)
- Production hardening (observability, batch processing, error handling)

---

## Requirements



---

## # Validated

**v1.0 Core Pipeline (shipped 2026-02-22):**
- ✓ PDF/HTML to Markdown conversion for vendor manuals — v1.0 Phase 1
- ✓ Vector database indexing for RAG retrieval — v1.0 Phase 1
- ✓ Layout-aware parsing for CLI syntax tables — v1.0 Phase 1
- ✓ Extract network-level intent and relationships from natural language using RAG — v1.0 Phase 2
- ✓ Parse vendor-specific CLI into vendor-neutral topology model — v1.0 Phase 2
- ✓ Validate LLM outputs against topology schema to prevent hallucinations — v1.0 Phase 2
- ✓ Calculate confidence scores for every extraction — v1.0 Phase 2
- ✓ Flag low-confidence extractions for human review — v1.0 Phase 3
- ✓ Web-based UI for viewing, editing, and approving extracted topology — v1.0 Phase 3
- ✓ Feedback loop from human corrections to improve model performance — v1.0 Phase 3
- ✓ Generate vendor-specific CLI from topology model — v1.0 Phase 4
- ✓ Support cross-vendor config generation (Cisco IOS, Arista EOS) — v1.0 Phase 4
- ✓ Integrate Batfish for semantic validation — v1.0 Phase 4

---

## # Active

**v2.0 (in progress):**
- (To be defined during requirements gathering)

---

## # Out of Scope

- Real-time streaming telemetry integration — defer to future milestone
- On-device configuration deployment/rollback — compilation only, not deployment
- Network discovery/topology mapping from live networks — focuses on configuration abstraction, not discovery
- Support for legacy/EoL vendor platforms — focuses on modern platforms with good documentation

---

## Context

**v1.0 Status (shipped 2026-02-22):** Full pipeline working end-to-end. Proven that LLM-powered extraction with RAG and human-in-the-loop can successfully translate vendor CLI to/from topology IR. System validated with real-world configs. Built with Python 3.12, FastAPI, ChromaDB, LangChain, and LLM APIs (Claude/GPT-4).

**Ecosystem Position:** This tool is the **vendor translation layer** in a larger network automation ecosystem (automationarch). It consumes vendor documentation and CLI, produces topology IR that feeds into autonetkit for modeling/simulation/visualization. Complementary to (not overlapping with) tools like autonetkit-config (design/compilation), netsim (protocol simulation), and netvis (visualization).

**Key architectural insight:** The intermediate representation is a topology-centric graph model, NOT a device-centric model like YANG. Network-level relationships (OSPF adjacencies, BGP peerings) are genuinely vendor-independent, while device-level configuration varies wildly across vendors. This enables true vendor abstraction.

**v1.0 Learnings:** LLM + RAG is viable for extracting topology-level intent from unstructured documentation. Human-in-the-loop is essential to manage hallucination risks. Batfish provides semantic validation to ensure compiled configs behave correctly. Confidence scoring and evidence citation are critical for production use.

---

## Constraints

- **Tech stack**: Python 3.12, FastAPI, ChromaDB, LangChain, MinerU — established in Phase 1
- **LLM costs**: Token usage must be monitored; consider local models for high-volume extraction
- **Hallucination risk**: LLM outputs must include confidence scores and require validation before use in production
- **Vendor coverage**: Initial focus on Cisco IOS/IOS-XE and Arista EOS (most common enterprise platforms)

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Topology-centric IR (not YANG) | YANG is device-centric; network relationships are truly vendor-independent | ✓ Good — enables genuine vendor abstraction |
| RAG + LLM for extraction | Handles diverse, unstructured vendor documentation better than rule-based parsers | ✓ Good — v1.0 validated with real-world configs |
| Batfish for validation | Industry-standard network simulator, validates semantic correctness | ✓ Good — v1.0 integration working, optional behind flag |
| Dual-engine PDF parsing | pymupdf4llm fast path + MinerU layout-aware fallback | ✓ Good — handles diverse PDF formats |
| ChromaDB vector store | Lightweight, embedded, good for RAG workloads | ✓ Good — fast retrieval, stable |
| HITL for quality assurance | LLMs hallucinate; human review essential for production | ✓ Good — v1.0 demonstrated viability with review UI |
| Confidence + evidence citation | Every extraction needs confidence score and doc/config evidence | ✓ Good — enables intelligent routing to HITL |
| Ecosystem integration focus | Translation layer only, not orchestration/intent/deployment | ✓ Good — clear boundaries with automationarch tools |

*Last updated: 2026-02-22 after v1.0 completion and v2.0 milestone initialization*

---

## Current Status

2026-03-05 — Completed 07-01-PLAN.md

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
