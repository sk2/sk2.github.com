---
layout: default
section: signal-processing
---

# Sound Array

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Concept

Audio processing system using Raspberry Pi and microphone arrays for spatial sound analysis. Captures multi-channel audio from USB/HAT arrays (ReSpeaker, Matrix), computes Time of Arrival (ToA) for sound localization, and applies beamforming for directional isolation. Classifies sources — vehicles (engine sounds), aircraft, wildlife (birds) — and streams processed audio or metadata to a remote desktop for analysis.

Runs on Raspberry Pi 4+ at standard sampling rates (44.1–48 kHz), targeting human-audible range.

---

## Capabilities

- Multi-channel audio capture from USB and HAT microphone arrays
- Time of Arrival estimation for sound source localization
- Beamforming for directional sound isolation and noise reduction
- Sound classification for vehicles, aircraft, and wildlife
- Streaming interface for raw or processed audio to remote desktop
- Integration with agent framework for structured audio analysis

---

[← Back to Signal Processing](../signal-processing)
