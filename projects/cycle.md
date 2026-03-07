---
layout: default
section: agentic-systems
---

# Cycle Agent

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-02-21</span>
  
</div>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Current Status](#current-status)

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

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## Core Value

A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.

---

## Target Audience

- Indoor cyclists using Apple ecosystem (iPad/Apple TV).
- Users wanting dynamic, agent-led training sessions.
- Developers/Enthusiasts experimenting with "Agent Bridge" architectures.

---

## Success Criteria

- Low-latency resistance control of KICKR Core via BLE.
- Real-time telemetry and command loop via NATS Agent Bridge.
- Smooth 60fps infinite terrain visualization on Apple TV.
- Reliable heart rate relay from Apple Watch.

---

## Constraints

- Must be native SwiftUI/Swift.
- Must support tvOS and iPadOS.
- Bluetooth communication must follow FTMS (Fitness Machine Service) standards.
- NATS connection must handle iOS/tvOS lifecycle (backgrounding).

---

## Current Status

2026-02-21 - Completed 04-01-PLAN.md

---

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)
