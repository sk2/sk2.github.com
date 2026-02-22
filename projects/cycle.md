---
layout: default
section: agentic-systems
---

# Cycle Agent

<span class="status-badge status-active">Phase 4/5 (71%)</span>

[← Back to Agentic Systems](../agentic-systems)

---

## Concept

A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a SceneKit environment.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 4/5 (71%) |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

An indoor cycling app that connects to a Wahoo KICKR Core via Bluetooth FTMS, receives AI-driven workout commands through a NATS agent bridge, and renders an immersive procedurally-generated 3D terrain synchronized to your effort. The AI agent controls trainer resistance in real-time based on workout logic, while the app provides live metrics and an engaging visual experience.

## Key Features

- **KICKR Core Integration**: Bluetooth LE with FTMS protocol for real-time power, cadence, speed metrics and resistance/grade control
- **AI Agent Bridge**: NATS request-response for workout commands, pub/sub for telemetry updates with sub-500ms latency
- **3D Terrain Visualization**: Infinite procedurally-generated low-poly SceneKit terrain at sustained 60fps, visual speed synchronized with trainer output
- **Biometric Integration**: Heart rate relay from Apple Watch, HealthKit workout recording
- **TV-Optimized UI**: 10-foot viewing distance design, color-coded intensity zones, tvOS focus navigation

## Architecture

```
NATS Agent (AI Workout Logic)
    ↕ Request/Response + Pub/Sub
SwiftUI App (iPad / Apple TV)
    ├── BLE/FTMS → KICKR Core
    ├── SceneKit → 3D Terrain
    ├── HealthKit → Apple Health
    └── WatchConnectivity → Heart Rate
```

## Milestones

**Phase 1: Core Connectivity** (80% Complete)
BLE discovery, FTMS control, NATS connection, and live metrics display.

**Roadmap:**

- **Phase 2: Agent Brain** — Request-response workout commands, real-time telemetry streaming
- **Phase 3: The World** — Infinite procedural terrain, visual speed synchronization
- **Phase 4: Heart Rate & Health** — Apple Watch integration, HealthKit storage
- **Phase 5: Polish & UI** — Polished HUD, tvOS optimization, 10-foot UI

## Tech Stack

Swift (SwiftUI, SceneKit, CoreBluetooth, HealthKit), NATS messaging, iPadOS/tvOS

---

[← Back to Agentic Systems](../agentic-systems)
