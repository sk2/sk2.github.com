---
layout: default
---

# cycle

<span class="status-badge status-planning">Planning</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Planning |
| **Language** | SwiftUI, SceneKit, FTMS (BLE), NATS |
| **Started** | 2025 |

---

## The Insight

A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.

## Architecture

- **Low-latency BLE resistance control**: Following FTMS (Fitness Machine Service) standards.
- **Real-time telemetry and commands**: Via NATS Agent Bridge.
- **Smooth 60fps infinite terrain rendering**: On Apple TV with SceneKit.
- **Apple Watch heart rate relay**: Through iOS/tvOS lifecycle-aware NATS connection.
- **NATS connection**: Handles iOS/tvOS backgrounding and lifecycle events.

## Target Experience

Dynamic AI-led training sessions where agents adjust resistance based on real-time performance data, integrated workout planning, and physiological metrics from the Apple Health ecosystem.

## Platforms

Native for iPadOS and tvOS.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)