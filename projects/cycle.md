---
layout: default
section: agentic-systems
---

# Cycle Agent

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Swift</span>
</div>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Concept

Native SwiftUI training application for iPad and Apple TV that bridges a Wahoo KICKR Core smart trainer with AI-driven workout logic. The app communicates with the trainer over Bluetooth (FTMS protocol) for real-time resistance control and telemetry, while a NATS message bridge connects to an external agent for dynamic workout decisions.

A SceneKit-rendered infinite terrain visualization runs at 60fps on Apple TV, with heart rate relay from Apple Watch completing the sensor loop.

---

## Features

- Low-latency BLE resistance control via Fitness Machine Service (FTMS) standard
- Real-time telemetry and command loop through NATS Agent Bridge
- Infinite terrain visualization in SceneKit on Apple TV
- Heart rate relay from Apple Watch
- Supports tvOS and iPadOS

---

[← Back to Autonomous Systems](../agentic-systems)
