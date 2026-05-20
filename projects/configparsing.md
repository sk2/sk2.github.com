---
layout: default
section: network-automation
description: "Vendor translation layer that decouples network configuration from vendor-specific syntax."
---

# Brownfield Ingestion

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-05-05</span>
  <span class="stack-badge">Python</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Architecture](#architecture)
- [Current Status](#current-status)

## Concept

Vendor translation layer that decouples network configuration from vendor-specific syntax. Uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model. The intermediate representation is topology-centric (protocol adjacencies, link roles, VLAN membership) rather than device-centric like YANG, enabling genuine vendor abstraction.

---

## Code Samples

### README.md

```markdown
# Example configurations (br-hzt0)

Curated, known-good vendor configs used for:

- **Smoke testing the extraction pipeline** — every example here must
  extract end-to-end without raising exceptions.
- **Demos and onboarding** — reach for these instead of writing toy
  configs from scratch.
- **Regression coverage** — `tests/test_phase2_examples.py` runs the
  full Phase 2 pipeline against each example to catch regressions
  in the deterministic vendor parsers.

## Layout

```
examples/
├── cisco_ios/
│   ├── basic.txt              hostname + 3 interfaces
│   └── ospf_single_area.txt   adds OSPF process in area 0
├── arista_eos/
│   ├── basic.txt
│   └── ospf_single_area.txt
├── juniper_junos/
│   ├── basic.txt
│   └── ospf_single_area.txt
└── nokia_sros/
    ├── basic.txt
    └── ospf_single_area.txt
```

## CLI

```bash
# List available examples
configparsing-phase2 examples list

# Extract a specific example into a temporary run dir
configparsing-phase2 examples extract cisco_ios/ospf_single_area
```

The `extract` subcommand prints the resulting `device_id`, vendor,
confidence, and run directory path so you can inspect the artifacts.

## Adding new scenarios

1. Drop the config under `examples/<vendor>/<scenario>.txt`.
2. Add a one-line entry to `tests/test_phase2_examples.py` if the
   scenario warrants its own assertion (otherwise the directory walk
   in that test will pick it up automatically).
3. Keep configs minimal — every line in the example should serve the
   scenario. A 200-line "real" config makes a poor onboarding
   reference.

```

---

## Architecture

The pipeline has four stages:

1. **Document ingestion**: PDF/HTML vendor manuals converted to Markdown, indexed into a vector database (ChromaDB) for RAG retrieval. Dual-engine parsing — pymupdf4llm for fast extraction, MinerU for layout-aware fallback.

2. **Intent extraction**: LLM + RAG extracts topology-level relationships from unstructured documentation and CLI configurations. Every extraction carries a confidence score and evidence citation.

3. **Human-in-the-loop review**: Low-confidence extractions routed to a web UI for operator review. Corrections feed back to improve model accuracy.

4. **Configuration generation**: Topology model compiled to vendor-specific CLI (Cisco IOS, Arista EOS). Batfish validates semantic correctness — compiled configs are simulated to verify they produce the intended forwarding behavior.

Built with Python 3.12, FastAPI, ChromaDB, LangChain.

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Python |

---

## What This Is

A network automation framework that decouples network configuration from vendor-specific syntax. It uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model inspired by AutoNetKit. The system enables cross-vendor configuration generation and validation through semantic simulation.

---

## Core Value

Extract network-level topology relationships (protocol adjacencies, link roles, VLAN membership) from vendor-specific CLI and documentation with high accuracy, enabling truly vendor-independent network configuration.

---

## Current Milestone: v2.0 Production-Grade Translation Layer

**Goal:** Become the universal, production-ready vendor translation layer for the network automation ecosystem

**Status:** In progress -  not started (27/30 plans completed)

**Target features:**
- Broader vendor coverage (Juniper, Nokia, F5, Palo Alto) and protocols (MPLS, SR, SRv6)
- Higher extraction accuracy with reduced HITL burden
- Ecosystem integration (RFC-01 compliance, [autonetkit](../autonetkit) interop)
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
- ✓ Plugin-based vendor architecture and version-aware RAG foundation — Phase 5
- ✓ Juniper JunOS and Nokia SR OS parsing support — Phase 5
- ✓ Evidence tracing and hallucination detection improvements — Phase 6
- ✓ RFC-01 schema vendoring, versioned loading, and validation harness — 
- ✓ RFC-01 OperationalTopology exporter and report output — 
- ✓ CLI export command with strict/best-effort validation flow — 
- → Next: `, `configparsing-yhp`, `configparsing-8ws`)

---

## # Out of Scope

- Real-time streaming telemetry integration — defer to future milestone
- On-device configuration deployment/rollback — [compilation](../compilation) only, not deployment
- Network discovery/topology mapping from live networks — focuses on configuration abstraction, not discovery
- Support for legacy/EoL vendor platforms — focuses on modern platforms with good documentation

---

## Context

**v1.0 Status (shipped 2026-02-22):** Full pipeline working end-to-end. Proven that LLM-powered extraction with RAG and human-in-the-loop can successfully translate vendor CLI to/from topology IR. System validated with real-world configs. Built with Python 3.12, FastAPI, ChromaDB, LangChain, and LLM APIs (Claude/GPT-4).

**v2.0 Status (in progress):** Multi-vendor foundation, accuracy optimization, and RFC-01 ecosystem export are complete. Remaining work is Phase 8 production hardening and vendor expansion.

**Current runtime caveat:** The vendor plugin registry parses/detects Cisco IOS, Arista EOS, Juniper JunOS, and Nokia SR OS, and registry tests cover all four. The main `Phase2Engine.extract_from_config_text()` CLI/API path is still wired to the legacy Cisco/Arista-only parser/report path, so Juniper/Nokia are plugin-layer capabilities until `configparsing-45w` updates that runtime path.

**Current planning caveat:**  requirement work is tracked by `configparsing-do2`, `configparsing-yhp`, and `configparsing-8ws`.

**Ecosystem Position:** This tool is the **vendor translation layer** in a larger network automation ecosystem ([automationarch](../automationarch)). It consumes vendor documentation and CLI, produces topology IR that feeds into [autonetkit](../autonetkit) for modeling/simulation/visualization. Complementary to (not overlapping with) tools like [autonetkit](../autonetkit)-config (design/[compilation](../compilation)), [netsim](../netsim) (protocol simulation), and [netvis](../netvis) (visualization).

**Key architectural insight:** The intermediate representation is a topology-centric graph model, NOT a device-centric model like YANG. Network-level relationships (OSPF adjacencies, BGP peerings) are genuinely vendor-independent, while device-level configuration varies wildly across vendors. This enables true vendor abstraction.

**v1.0 Learnings:** LLM + RAG is viable for extracting topology-level intent from unstructured documentation. Human-in-the-loop is essential to manage hallucination risks. Batfish provides semantic validation to ensure compiled configs behave correctly. Confidence scoring and evidence citation are critical for production use.

---

## Constraints

- **Tech stack**: Python 3.12, FastAPI, ChromaDB, LangChain, MinerU — established in Phase 1
- **LLM costs**: Token usage must be monitored; consider local models for high-volume extraction
- **Hallucination risk**: LLM outputs must include confidence scores and require validation before use in production
- **Vendor coverage**: Cisco IOS/IOS-XE and Arista EOS are wired through the main Engine wiring. Future expansion targets F5 and Palo Alto.

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
| Ecosystem integration focus | Translation layer only, not orchestration/intent/deployment | ✓ Good — clear boundaries with [automationarch](../automationarch) tools |

*Last updated: 2026-04-12 after reality check against code and tests*

---

## Current Status

2026-05-05 - Verified vks/45w/do2/yhp closure against code; resynced docs with bead state.
