---
layout: default
---

# Wave

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Concept

- **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio.
- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution.

## Quick Facts

| | |
|---|---|
| **Status** | v1.1 Shipped (Feb 2026) |
| **Language** | Swift (SwiftUI) |
| **Platform** | watchOS, macOS (planned) |
| **Started** | 2026 |

---

## What This Is

**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work.

1. **StillState (Watch):** An adaptive sleep sounds app for Apple Watch with personalized frequency calibration, heartbeat synchronization, and microphone-based environmental monitoring.
2. **FlowState (Mac):** A productivity-focused menu bar app that links procedural audio to the user's active tasks and "Genetic System" TODO list (planned).

## Core Value

- **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio
- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution

## Current State: v1.1 Shipped

**Latest release:** v1.1 Adaptive Audio Features (2026-02-09)

**Key Features:**
- **Procedural Audio Engine**: White, brown, and blended noise with live hot-swap
- **Binaural Beats**: 5 presets + custom parameters with noise bed mixing
- **Ear-Print Calibration**: Interactive 10-step frequency sweep (20 Hz - 8 kHz) with personalized +4dB bias
- **Heartbeat Synchronization**: 4 BPM presets (50-65 BPM) with 5-8% amplitude modulation
- **Microphone Monitoring**: vDSP RMS-to-dB analysis with periodic 0.5s sampling
- **Smart Battery Preservation**: All features toggleable, defaults OFF, auto-disable on screen-off/disconnect
- **Bluetooth-Only Routing**: Auto-pause with stereo validation
- **Background Audio**: Overnight reliability (<12% base drain, <15% all features)

## Next Milestone: v1.2 Polish & Validation

**Goals:**
- Full adaptive masking algorithm (dynamic volume/frequency adjustment based on environmental noise)
- Tech debt resolution (CalibrationEngine timestamp, Settings reorganization)
- Hardware battery validation (overnight testing, confirm <15% drain targets)
- Adaptive feature tuning (calibration bias perception, heartbeat effectiveness, mic accuracy)
- TestFlight distribution for internal testing

## Use Cases

**StillState:** Sleeping on retreats or in shared dorms. Block human-centric noises (snoring) while respecting "noble silence" (no light/no watch speaker), with personalized frequency bias and optional heartbeat grounding.

**FlowState (Planned):** Deep work sessions at a desk. Noise serves as a "Flow State" trigger linked directly to productivity metrics and task DNA.

## Tech Stack

- **Platform**: SwiftUI for watchOS and macOS
- **Audio**: AVAudioEngine with procedural synthesis
- **Signal Processing**: vDSP for real-time RMS analysis
- **Audio Policy**: `.longFormAudio` for background playback

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
