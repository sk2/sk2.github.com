---
layout: default
section: signal-processing
---

# Wave (StillState & FlowState)

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Swift</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Concept

Ambient audio ecosystem spanning Apple Watch and Mac, designed for sleep and deep work.

**StillState** (watchOS) is an adaptive sleep sounds app that generates procedural noise (white, brown, blended) with binaural beats, personalized frequency calibration, and heartbeat synchronization. Microphone monitoring detects environmental noise for adaptive masking. Bluetooth-only routing, overnight reliability, and battery-first design (all features default off, individually toggleable).

**FlowState** (macOS, planned) links procedural audio to active tasks through a menu bar app, evolving audio parameters based on session productivity metrics.

---

## Features

**Audio engine:**
- Procedural noise synthesis with live hot-swap between noise types
- Binaural beats (5 presets + custom parameters + noise bed mixing)
- Wrapper composition pattern: effects stack without modifying base generators

**Personalization:**
- 10-step frequency calibration sweep (20 Hz–8 kHz) with +4 dB preference bias
- Heartbeat synchronization (4 BPM presets, 50–65 BPM, amplitude modulation)
- Microphone monitoring (vDSP RMS-to-dB analysis, 0.5s periodic sampling)

**Reliability:**
- Bluetooth-only routing with auto-pause on disconnect and stereo validation
- Background audio with overnight reliability
- Battery preservation: all features toggleable, defaults off, auto-disable on screen-off

---

## Status

**Current**: v1.2 — adaptive masking algorithm (dynamic volume/frequency adjustment based on environmental noise), hardware battery validation.

**Shipped:**
- v1.1 — frequency calibration, heartbeat sync, microphone monitoring infrastructure (February 2026)
- v1.0 — procedural audio engine, binaural beats, Bluetooth routing, background playback (February 2026)

---

[← Back to Signal Processing](../signal-processing)
