---
layout: default
section: signal-processing
---

# HealthyPi Ecosystem

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Agentic Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Milestones](#milestones)

## Concept

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

## Key Features

- **Multimodal Biometric Processing**: ECG/PPG heart rate and HRV (SDNN, RMSSD, LF/HF), EDA stress scoring, IMU activity classification, EEG meditation scoring
- **Analysis Engine**: HRV time-domain and frequency-domain calculations, stress level scoring (EDA + HRV fusion), sleep quality scoring, baseline learning with deviation detection
- **Virtual Patient Simulator**: Synthetic waveform generation via NeuroKit2 with scriptable scenarios (resting, stress response, deep sleep) — mock interface indistinguishable from real hardware at the NATS level
- **Agentic Integration**: Registered with the multi-agent orchestrator for autonomous health queries, capability-based authorization with Ed25519 tokens
- **Desktop & Mobile Interfaces**: macOS menu bar app with real-time health status, iOS/WatchOS prototype with HealthKit sync

---

## Milestones

 (Complete)
Pydantic schemas for ECG, EEG, EDA, PPG, IMU with validation suite.

 (Complete)
CLI tool (`healthypi-sim`) with scenario support and mock BLE/Serial interface.

 (Complete)
HRV analysis, stress scoring, sleep quality, baseline learning, and deviation detection.

 (Complete)
Agent scaffold with NATS integration, task handlers, and orchestrator registration.

 (Complete)
macOS menu bar app with real-time ambient health status (Green/Yellow/Red).

**/7 plans)
- HealthyPiKit Swift package with NATS subscriber (complete)
- Reconnection handling and test coverage (complete)
- HealthKit bidirectional sync, iOS dashboard, WatchOS app (remaining)

---

[← Back to Agentic Systems](../agentic-systems)

[← Back to Projects](../projects)
