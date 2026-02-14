---
layout: default
section: projects
---

# Wave

<span class="status-badge status-active">v1.1 — Adaptive Audio Features</span>

[← Back to Projects](../projects)

---

## The Insight

- **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio
- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution

## Quick Facts

| | |
|---|---|
| **Status** | v1.1 — Adaptive Audio Features |
| **Language** | Swift (SwiftUI) |
| **Started** | 2026 |

---

## What This Is

**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work.

1. **StillState (Watch):** An adaptive sleep sounds app for Apple Watch with personalized frequency calibration, heartbeat synchronization, and microphone-based environmental monitoring.
2. **FlowState (Mac):** A productivity-focused menu bar app that links procedural audio to active tasks and a genetic evolution system (planned).

## StillState Features

- **Procedural Noise Engine**: White, brown, and blended noise with live hot-swap
- **Binaural Beats**: 5 presets plus custom parameters with noise bed compositing
- **Ear-Print Calibration**: Interactive 10-step frequency sweep (20 Hz - 8 kHz) with personalized +4dB bias
- **Heartbeat Synchronization**: 4 BPM presets (50-65 BPM) with conservative 5-8% amplitude modulation
- **Adaptive Masking**: Microphone-based ambient noise monitoring with vDSP-accelerated analysis, dynamic volume adjustment (1.0-1.5x)
- **Sleep-Optimized UI**: Large touch targets, Bluetooth-only routing, indefinite background playback

## Audio Architecture

```
Base Generator (White / Brown / Blended)
  └─ BiasedNoiseGenerator (if calibration enabled)
      └─ HeartbeatModulatedGenerator (if enabled)
          └─ AdaptiveMaskingGenerator (v1.2)
              └─ BinauralBeatsGenerator (optional)
```

All wrappers use pre-allocated buffers with lock-free parameter reads — no allocations in the audio thread.

## Milestones

**v1.0 MVP** (Shipped Feb 8, 2026)
Procedural audio synthesis, binaural beats, overnight reliability, Bluetooth routing, sleep-optimized UI.

**v1.1 Adaptive Audio Features** (Shipped Feb 9, 2026)
Ear-print calibration, heartbeat synchronization, microphone monitoring infrastructure, adaptive masking foundation.

**v1.2 Polish & Validation** (In Progress)
- Full adaptive masking algorithm (FFT frequency analysis, dynamic volume/frequency adjustment)
- Hardware battery validation (target: <15% drain/hour with all features)
- TestFlight distribution setup

**Roadmap:**

- **v1.3 Distribution & Enhancement** — Advanced adaptive sensitivity, user feedback integration
- **FlowState (macOS)** — Genetic system integration, audio DNA evolution, flow-locking with task coupling, pomodoro synchronization

## Tech Stack

Swift (SwiftUI, AVAudioEngine, Accelerate/vDSP), watchOS, CoreAudio, HealthKit

---

[← Back to Projects](../projects)
