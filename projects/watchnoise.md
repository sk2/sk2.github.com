---
layout: default
---

# WatchNoise

<span class="status-badge status-active">v1.1 Shipped</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | v1.1 Shipped |
| **Language** | Swift (SwiftUI) |
| **Started** | 2025 |

---

## The Insight

Convenient access to sleep sounds from your wrist without needing your phone nearby.

## What This Is

Apple Watch sleep sounds app with adaptive audio. Frequency calibration, heartbeat sync, and environmental noise monitoring.

## Architecture

- **Audio Engine**: Custom audio unit graph for real-time synthesis and mixing.
- **Ambient Noise Generation**: White, brown, and blended noise via procedural audio synthesis.
- **Bluetooth Event Handling**: Monitors headphone connection/disconnection for auto-pause.
- **HealthKit Integration**: Accesses heart rate for adaptive audio modulation.
- **User Interface**: SwiftUI for intuitive watchOS experience.

## Features

- **Procedural Audio Synthesis**: Generates high-quality ambient sounds without large audio files.
- **Adaptive Audio**: Adjusts sound characteristics based on heart rate or environmental noise.
- **Auto-Pause/Resume**: Seamlessly pauses when headphones disconnect and resumes when reconnected.
- **Simple Controls**: Focuses on minimal interaction for sleep-focused use.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)