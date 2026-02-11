---
layout: default
---

# WatchNoise

<span class="status-badge status-active">v1.1 Shipped</span>

[← Back to Projects](../projects)

---


## The Insight

Sleep sound applications typically rely on static loops and phone dependency. **WatchNoise** implements procedural audio synthesis on watchOS, enabling heartbeat-synced ambient noise and environmental adaptation directly from the wrist without requiring a nearby iPhone.

## Quick Facts

| | |
|---|---|
| **Status** | v1.1 Shipped |
| **Language** | Swift (SwiftUI) |
| **Started** | 2025 |

---

## What This Is

An Apple Watch sleep sounds application featuring adaptive audio. It uses a custom audio unit graph for real-time synthesis and integrates with HealthKit for heart rate synchronization.

## Features

- **Procedural Audio Synthesis**: Generates high-quality ambient sounds without large audio files.
- **Adaptive Audio**: Adjusts sound characteristics based on heart rate or environmental noise.
- **Auto-Pause/Resume**: Seamlessly pauses when headphones disconnect and resumes when reconnected.
- **Simple Controls**: Focuses on minimal interaction for sleep-focused use.

---

[← Back to Projects](../projects)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

## Architecture

- **Audio Engine**: Custom audio unit graph for real-time synthesis and mixing.
- **Ambient Noise Generation**: White, brown, and blended noise via procedural audio synthesis.
- **Bluetooth Event Handling**: Monitors headphone connection/disconnection for auto-pause.
- **HealthKit Integration**: Accesses heart rate for adaptive audio modulation.
- **User Interface**: SwiftUI for intuitive watchOS experience.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
