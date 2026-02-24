---
layout: default
section: agentic-systems
---

# Cycle Agent

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Agentic Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Concept

### Core Value

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

[← Back to Agentic Systems](../agentic-systems)

[← Back to Projects](../projects)
