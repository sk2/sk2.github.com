---
layout: default
section: agentic-systems
---

# HealthyPi Ecosystem

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">Swift</span>
</div>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Concept

Modular health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (Pi HAT and wearable) into structured metrics for agent-driven analysis. Swift collectors on Apple devices capture HealthKit data, publish to a NATS broker, and Python agents in containers run analysis pipelines — all coordinated by the multi-agent orchestrator.

---

## Architecture

- **HealthyPi 6** (Pi HAT): ECG, PPG, SpO2, temperature via serial/USB
- **HealthyPi Move** (wearable): accelerometer, PPG via BLE
- **Ingest path**: hardware stream, normalize, publish to NATS (`biometric.raw.*`)
- **Agent integration**: leverages the multi-agent framework (NATS broker, TLS 1.3, capability tokens)
- **Visualization**: desktop (menu bar) and Apple ecosystem (iOS/Watch)

---

## Features

- Standardized data models for multi-modal biometrics
- Synthetic "Virtual Patient" for hardware-free development
- Real-time and historical analysis via agent pipeline
- Unified visualization across desktop and mobile

---

[← Back to Autonomous Systems](../agentic-systems)
