---
layout: default
section: network-automation
description: "Graph Neural Network (GNN) based network analytics module that extends topology analysis with real-time learning and prediction."
---

# Network Analysis Engine

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Current Status](#current-status)

## Concept

Graph Neural Network (GNN) based network analytics module that extends topology analysis with real-time learning and prediction. Subscribes to the Network Topology Engine's WebSocket stream for live topology updates, runs GNN models on graph data, and exposes analytics through multiple interfaces (WebSocket streaming, REST API, Rust library, event queue).

Built on an existing Rust+Python analysis toolkit that includes formal verification (Z3 SMT solver), graph algorithms (centrality, community detection, cascade modeling), and Python bindings via PyO3.

---

## Code Samples

### README.md

```markdown
# NetAssure Examples

This directory contains example topologies, event streams, and scripts to help you get started with the NetAssure analysis engine.

## Topologies & Events

- `topology-snapshot.json`: A basic 4-node topology snapshot illustrating the RFC-01 schema.
- `clos-fabric.json`: A 2-tier leaf-spine data center fabric with AS numbers and role metadata.
- `bgp-leak-topology.json`: A topology specifically designed to simulate BGP route leak scenarios.
- `temporal-events.json`: A stream of temporal edge events for TGN (Temporal Graph Network) inference.
- `v2.1-test-topology.json`: A large-scale test topology used for benchmarking graph algorithms.

## Scripts

- `query_api.py`: A Python script demonstrating how to interact with the NetAssure REST API. Covers fetching status, filtering alerts/anomalies, and submitting operator feedback.

## Running the Examples

### 1. Start the NetAssure Daemon
You can run the ingestion system in "dry-run" mode using one of the example topologies:

```bash
# In one terminal, start the ingestor (simulating a live stream)
netassure ingest --ws ws://localhost:9000 --dry-run
```

### 2. Query via CLI
Once the system is running, you can use the CLI to query alerts:

```bash
netassure alerts --api http://localhost:8080 --status active
```

### 3. Query via Python
Ensure you have the `requests` library installed:

```bash
pip install requests
python3 examples/query_api.py
```

```

### query_api.py

```python
#!/usr/bin/env python3
"""
Example Python script to consume the NetAssure REST API.
"""

import requests
import json
import time
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8080"

def get_status():
    print("--- System Status ---")
    try:
        resp = requests.get(f"{BASE_URL}/status")
        resp.raise_for_status()
        print(json.dumps(resp.json(), indent=2))
    except Exception as e:
        print(f"Error fetching status: {e}")

def list_alerts(status=None, since=None):
    print(f"--- Alerts (filter: status={status}, since={since}) ---")
    params = {}
    if status:
        params["status"] = status
    if since:
        params["since"] = since
        
    try:
        resp = requests.get(f"{BASE_URL}/alerts", params=params)
        resp.raise_for_status()
        alerts = resp.json()
        print(f"Found {len(alerts)} alerts.")
        for a in alerts:
            print(f"[{a['status'].upper()}] {a['alert_id'][:8]}: {a['node_id']} - {a['message']}")
        return alerts
    except Exception as e:
        print(f"Error fetching alerts: {e}")
        return []

def list_anomalies(since=None):
    print(f"--- Recent Anomalies (since={since}) ---")
    params = {}
    if since:
        params["since"] = since
        
    try:
        resp = requests.get(f"{BASE_URL}/anomalies", params=params)
        resp.raise_for_status()
        anomalies = resp.json()
        print(f"Found {len(anomalies)} anomalies.")
        for a in anomalies:
            print(f"ID: {a['anomaly_id'][:8]}, Score: {a['score']:.3f}, Nodes: {a['contributing_node_ids']}")
    except Exception as e:
        print(f"Error fetching anomalies: {e}")

def post_feedback(alert_id, is_false_positive, notes=None):
    print(f"--- Posting Feedback for Alert {alert_id} ---")
    payload = {
        "is_false_positive": is_false_positive,
        "notes": notes
    }
    try:
        resp = requests.post(f"{BASE_URL}/alerts/{alert_id}/feedback", json=payload)
        resp.raise_for_status()
        print("Feedback submitted successfully.")
    except Exception as e:
        print(f"Error posting feedback: {e}")

if __name__ == "__main__":
    # Note: Assumes the netassure daemon is running on localhost:8080
    get_status()
    print()
    
    # List all active alerts
    alerts = list_alerts(status="active")
    print()
    
    # List anomalies from the last hour
    one_hour_ago = (datetime.utcnow() - timedelta(hours=1)).isoformat() + "Z"
    list_anomalies(since=one_hour_ago)
    print()
    
    # Example: Post feedback if we found an alert
    if alerts:
        target_id = alerts[0]["alert_id"]
        post_feedback(target_id, is_false_positive=False, notes="Confirmed BGP leak via manual inspection.")

```

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust, Polars |

---

## What This Is

A GNN-based real-time network analytics platform built in Rust+Python. Subscribes to NTE topology updates via WebSocket, runs GNN models for anomaly detection and traffic prediction, and exposes results through CLI, REST API, WebSocket streaming, and event queue interfaces. Includes formal verification (Z3), graph algorithms, and failure cascade modeling.

---

## Core Value

Enable exploration and practical application of GNN techniques on real network topology data, producing actionable insights that improve network reliability and security.

---

## Requirements



---

## # Validated

<!-- Shipped and confirmed valuable. -->

- ✓ Network topology analysis with formal verification (Z3 SMT solver) — v1.0
- ✓ Graph algorithms (centrality, community detection, cascade modeling) — v2.0
- ✓ Python bindings via PyO3 for ML/analysis integration — v1.0
- ✓ CLI interface for topology operations — v1.0
- ✓ Rust-based performance-critical operations with petgraph — v1.0
- ✓ Subscribe to NTE topology updates via WebSocket — v2.3
- ✓ GNN-based anomaly detection on network topology — v2.2
- ✓ Alert system with configurable triggers (anomaly, topology changes, performance) — v2.3
- ✓ REST API for on-demand analytics queries — v2.3
- ✓ Rust library API for embedded analytics — v2.3
- ✓ WebSocket streaming interface for real-time analytics results — v2.2
- ✓ Event queue integration for publishing analytics to message brokers — v2.2
- ✓ Near real-time processing (1-5s latency target) — v2.3

---

## # Active

<!-- Current scope. Building toward these. -->

- [ ] Cross-network topology comparison and diff analysis
- [ ] Historical trend tracking and pattern evolution
- [ ] Predictive capacity planning from temporal models
- [ ] Advanced graph algorithms (spectral clustering, motif detection)
- [ ] What-if analysis (link/node failure simulation without full cascade)

---

## Current Milestone: v2.4 Richer Analysis

**Goal:** Expand NetAssure's analytical depth with topology diffing, historical trends, advanced graph algorithms, capacity planning, and what-if simulation.

**Target features:**
- Topology snapshot diffing and comparison
- Time-windowed trend tracking for graph metrics
- Spectral clustering and network motif detection
- Temporal model-driven capacity predictions
- Lightweight what-if failure simulation

---

## # Out of Scope

- Visualization/UI layer — Other tools consume NetAssure analytics for visualization
- NTE topology engine implementation — NetAssure consumes from existing NTE ([ank_nte](../ank_nte))
- Historical data storage/replay — v2.4 adds bounded trend windows, not full replay
- Production deployment infrastructure (Docker, K8s) — working prototype scope

---

## Context

**Current State (v2.3 shipped):**
Rust+Python network analysis platform with ~15k LOC Rust across 6 crates, ~3k LOC Python ML layer. Full end-to-end pipeline: NTE WebSocket ingestion → topology event normalization → GNN inference → anomaly detection → alert generation → CLI/REST/WS delivery.

**Tech Stack:**
- Rust: petgraph, axum, tokio, tch-rs, rustworkx-core, PyO3
- Python: PyTorch, PyTorch Geometric, custom TGN C++ extension
- External: NTE ([ank_nte](../ank_nte)) WebSocket topology streaming

**Integration Point:**
NetAssure subscribes to NTE's WebSocket interface to receive real-time topology updates, runs GNN models on the graph data, and exposes analytics through multiple interfaces.

---

## Constraints

- **Technology**: Rust-based to align with NTE ecosystem
- **Integration**: Must consume topology via NTE WebSocket (external system)
- **Latency**: Near real-time processing target (1-5 seconds)
- **Architecture**: Analytics module only — no visualization, relies on external tools

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Use NTE WebSocket for topology ingestion | NTE already provides real-time streaming; avoid duplicating infrastructure | ✓ Good — v2.3 |
| Multiple output interfaces (WS/REST/API/Events) | Flexibility for different consumption patterns | ✓ Good — v2.3 |
| GNN over traditional ML | Network topology is naturally graph-structured | ✓ Good — v2.2 |
| TGN with custom C++ memory extension | Maintain temporal state across TorchScript inference | ✓ Good — v2.2 |
| `broadcast::Sender<AnalyticsEvent>` for multi-consumer | Decouples inference pipeline from downstream consumers | ✓ Good — v2.2 |
| Tolerant delta decoding (Unknown variant) | Avoid ingest crashes on NTE protocol evolution | ✓ Good — v2.3 |
| Ring buffers for alert/anomaly history | Bounded memory, simple shared state for API queries | ✓ Good — v2.3 |
| rustworkx-core for centrality | Already optimized with rayon; manual impl would regress | ✓ Good — v2.3 |

*Last updated: 2026-03-08 after v2.4 milestone start*

---

## Current Status

2026-03-09 —  executed: GET /analyze/trends endpoint (1 task, 1 file)
