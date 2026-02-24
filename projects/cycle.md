---
layout: default
section: agentic-systems
---

# Cycle Agent

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

A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.

---

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

---

## Tech Stack

Swift (SwiftUI, SceneKit, CoreBluetooth, HealthKit), NATS messaging, iPadOS/tvOS

---

## Key Features

- **KICKR Core Integration**: Bluetooth LE with FTMS protocol for real-time power, cadence, speed metrics and resistance/grade control
- **AI Agent Bridge**: NATS request-response for workout commands, pub/sub for telemetry updates with sub-500ms latency
- **3D Terrain Visualization**: Infinite procedurally-generated low-poly SceneKit terrain at sustained 60fps, visual speed synchronized with trainer output
- **Biometric Integration**: Heart rate relay from Apple Watch, HealthKit workout recording
- **TV-Optimized UI**: 10-foot viewing distance design, color-coded intensity zones, tvOS focus navigation

---

## Milestones

**% Complete)
BLE discovery, FTMS control, NATS connection, and live metrics display.

-  — Request-response workout commands, real-time telemetry streaming
-  — Infinite procedural terrain, visual speed synchronization
-  — Apple Watch integration, HealthKit storage
- **-foot UI

---

[← Back to Agentic Systems](../agentic-systems)

[← Back to Projects](../projects)
