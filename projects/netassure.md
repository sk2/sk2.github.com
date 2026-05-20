---
layout: default
section: network-automation
description: "Graph Neural Network (GNN) based network analytics module that extends topology analysis with real-time learning and prediction."
sitemap: false
hand_written: true
---

# Network Analysis Engine

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">TypeScript</span>
</div>

---

## Concept

Graph Neural Network (GNN) based network analytics module that extends topology analysis with real-time learning and prediction. Subscribes to the Network Topology Engine's WebSocket stream for live topology updates, runs GNN models on graph data, and exposes analytics through multiple interfaces (WebSocket streaming, REST API, Rust library, event queue).

Built on an existing Rust+Python analysis toolkit that includes formal verification (Z3 SMT solver), graph algorithms (centrality, community detection, cascade modeling), and Python bindings via PyO3.

---

## Code Samples

### README.md

```markdown
# NetAssure Examples

This directory contains sample topology snapshots, event streams, multi-modal
contexts, and a small REST API client.

## Files

- `topology-snapshot.json`: small RFC-01 `Snapshot` message for static CLI checks.
- `clos-fabric.json`: two-tier leaf-spine fabric with role metadata.
- `bgp-leak-topology.json`: topology for route-leak-style cascade experiments.
- `temporal-events.json`: temporal edge events for TGN inference.
- `multimodal-context.json`: input context for multi-modal anomaly scoring.
- `v2.1-test-topology.json`: larger topology used for graph algorithm benchmarks.
- `target-hubs-scenario.json`: scenario configuration for targeted cascade runs.
- `query_api.py`: REST API example covering status, alert/anomaly listing, and feedback.

## Static CLI Examples

```bash
netassure verify examples/topology-snapshot.json
netassure analyze examples/topology-snapshot.json
netassure cascade examples/topology-snapshot.json --scenario random-failure-pct --params '{"node_failure_pct": 10}' --json
netassure predict-temporal examples/topology-snapshot.json examples/temporal-events.json --model models/tgn_model.pt --json
netassure predict-multimodal examples/multimodal-context.json --explain --json
```

Model-backed commands require the corresponding model files and Python dependencies.

## Live API Example

Start NetAssure against a real or test NTE WebSocket endpoint:

```bash
netassure ingest --ws ws://localhost:9000 --api-addr 127.0.0.1:8080
```

Then query the REST API:

```bash
python3 examples/query_api.py
```

Dry-run mode is for validating a live WebSocket stream without forwarding events into
the full analysis pipeline:

```bash
netassure ingest --ws ws://localhost:9000 --dry-run --duration-secs 60
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

NetAssure is a Rust/Python network analytics platform. It ingests NTE topology
updates, keeps a live graph model, runs deterministic graph and verification
analysis, supports cascade/what-if simulation, and exposes operator workflows
through a Rust CLI, REST API, optional WebSocket streaming, PyO3 bindings, and
Python ML/agent tools.

---

## Core Value

Enable practical GNN-assisted network operations while keeping hard guarantees
in deterministic Rust engines: verification results constrain what may be true,
and ML/agent outputs rank what is likely worth investigating.

---

## Requirements



---

## # Validated

- [x] NTE topology snapshots and deltas via WebSocket ingestion.
- [x] Shared RFC-01 topology model with tolerant unknown-delta handling.
- [x] Formal verification for reachability, loops, isolation, and equivalence.
- [x] Graph analytics for centrality, robustness, path diversity, spectral clustering,
  motif census, diff/playback, layout, routing, trends, capacity, design suggestions,
  and intent optimization.
- [x] Cascade simulation, what-if failure analysis, fragility heatmaps, and temporal
  degradation simulation.
- [x] REST API for topology, analytics, verification, cascade, alerts, predictions,
  remediation, and metrics.
- [x] SQLite-backed alert/anomaly/blueprint persistence.
- [x] CLI for static topology workflows and live API interaction.
- [x] PyO3 bindings for Python integration.
- [x] Python ML and operator scaffolds for anomaly scoring, TGN/fusion training,
  [multi-agent](../multi-agent) chat, and remediation RL experimentation.

---

## # Active

- [ ] Finish RL remediation integration: decide whether Rust should call a separate
  Python service, a subprocess CLI, or a native policy artifact instead of embedding
  Python directly.
- [ ] Add end-to-end verification for the Multi-Agent NOC -> remediation -> blueprint
  workflow.
- [ ] Decide whether the simplified OSPF routing model is sufficient or needs explicit
  convergence-loop integration in shadow topology verification.
- [ ] Add a real visualization frontend or document NetViz as an external consumer only.
- [ ] Tighten model-backed workflows with explicit fixtures/model-loading smoke tests.

---

## Context

**Current state (reality check 2026-04-12):** the workspace builds with
`cargo check --workspace`. The main gap is not the Rust analytics surface, but proof
and integration depth around optional ML/agent workflows and visualization.

**Tech stack:**

- Rust: petgraph, axum, tokio, tch-rs, rustworkx-core, rusqlite, PyO3.
- Python: PyTorch/PyTorch Geometric, Gymnasium, stable-baselines3, LangGraph/LangChain.
- External systems: NTE WebSocket stream, optional NATS, optional OpenAI API, optional
  `[netsim](../netsim)` high-fidelity simulator.

---

## Key Decisions

| Decision | Rationale | Current Outcome |
|---|---|---|
| Use NTE WebSocket for topology ingestion | Avoid duplicating topology discovery | Implemented |
| Keep deterministic analysis in Rust | Performance and clearer failure modes | Implemented |
| Use Python for ML/agent workflows | Ecosystem maturity | Implemented, optional dependencies required |
| Store alerts/anomalies/blueprints in SQLite | Durable API history and restart behavior | Implemented |
| Treat ML outputs as hypotheses | Avoid presenting predictions as proofs | Reflected in report/docs |
| Use tolerant delta decoding | Avoid ingest crashes on NTE protocol evolution | Implemented |
| Do not ship placeholder frontend as NetViz | Prevent docs from overstating UI status | Current docs mark visualization as missing |

*Last updated: 2026-04-12 after reality check and docs refresh*
