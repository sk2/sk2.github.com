---
layout: default
section: signal-processing
---

# HealthyPi Ecosystem

<span class="status-badge status-active">v1.0 — Apple Ecosystem Integration</span>

[← Back to Signal Processing](../signal-processing)

---

## The Insight

A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware into actionable insights and automated interventions — bridging high-fidelity biometric wearables with daily health management.

## Quick Facts

| | |
|---|---|
| **Status** | v1.0 — Apple Ecosystem Integration |
| **Language** | Python + Swift |
| **Started** | 2026 |

---

## What This Is

A health monitoring platform that connects HealthyPi hardware (HealthyPi 6 Pi HAT and HealthyPi Move wearable) to an analysis engine, virtual patient simulator, and agentic intelligence layer. It processes ECG, PPG, EDA, IMU, and EEG signals for HRV analysis, stress scoring, and sleep quality assessment — with a virtual patient simulator for hardware-free development.

## Key Features

- **Multimodal Biometric Processing**: ECG/PPG heart rate and HRV (SDNN, RMSSD, LF/HF), EDA stress scoring, IMU activity classification, EEG meditation scoring
- **Analysis Engine**: HRV time-domain and frequency-domain calculations, stress level scoring (EDA + HRV fusion), sleep quality scoring, baseline learning with deviation detection
- **Virtual Patient Simulator**: Synthetic waveform generation via NeuroKit2 with scriptable scenarios (resting, stress response, deep sleep) — mock interface indistinguishable from real hardware at the NATS level
- **Agentic Integration**: Registered with the multi-agent orchestrator for autonomous health queries, capability-based authorization with Ed25519 tokens
- **Desktop & Mobile Interfaces**: macOS menu bar app with real-time health status, iOS/WatchOS prototype with HealthKit sync

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

## Milestones

**Phase 1: Foundation & Data Models** (Complete)
Pydantic schemas for ECG, EEG, EDA, PPG, IMU with validation suite.

**Phase 2: Virtual Patient Simulator** (Complete)
CLI tool (`healthypi-sim`) with scenario support and mock BLE/Serial interface.

**Phase 3: Core Analysis Engine** (Complete)
HRV analysis, stress scoring, sleep quality, baseline learning, and deviation detection.

**Phase 4: Agentic Framework Integration** (Complete)
Agent scaffold with NATS integration, task handlers, and orchestrator registration.

**Phase 5: Desktop Menu Bar Prototype** (Complete)
macOS menu bar app with real-time ambient health status (Green/Yellow/Red).

**Phase 6: Apple Ecosystem & Sync** (In Progress)
- HealthyPiKit Swift package with NATS subscriber
- HealthKit bidirectional sync, iOS dashboard, WatchOS app (planned)

## Tech Stack

Python (Pydantic, NeuroKit2, SciPy), Swift (SwiftUI, HealthKit), NATS messaging, pytest (286 tests)

---

[← Back to Signal Processing](../signal-processing)
