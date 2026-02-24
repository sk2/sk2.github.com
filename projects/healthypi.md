---
layout: default
section: signal-processing
---

# HealthyPi Ecosystem

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Agentic Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Concept

### Core Value

A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.

---

## Architecture

```
HealthyPi Hardware (BLE/Serial)
    ↓
NATS Broker (biometric.raw.*)
    ↓
Analysis Engine (HRV, stress, sleep, baseline)
    ↓
NATS (health.healthypi.*)
    ├── macOS Menu Bar App
    ├── iOS/WatchOS App
    └── Multi-Agent Orchestrator
```

---

## Tech Stack

Python (Pydantic, NeuroKit2, SciPy), Swift (SwiftUI, HealthKit), NATS messaging, pytest (286 tests)

---

[← Back to Agentic Systems](../agentic-systems)

[← Back to Projects](../projects)
