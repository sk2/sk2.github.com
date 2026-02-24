---
layout: default
section: signal-processing
---

# soundarray

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Key Features](#key-features)
- [Processing Pipeline](#processing-pipeline)
- [Tech Stack](#tech-stack)

## Concept

An exploration-focused audio processing system using Raspberry Pi and microphone arrays. It focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.

The ability to capture, localize, and classify complex soundscapes on edge devices or via remote streaming, providing structured insights to an agent framework.

---

## Key Features

- **Multi-Channel Audio Capture**: 4-8 channel USB/HAT microphone arrays (ReSpeaker, Matrix Creator)
- **Sound Source Localization**: GCC-PHAT and Kalman filter tracking for real-time azimuth and elevation
- **Adaptive Beamforming**: Directional sound isolation via ODAS — separate overlapping sources
- **Edge Classification**: YAMNet (521 classes) on TensorFlow Lite, optimized for ARM/NEON — vehicles, birds, bats, engines
- **Agent Integration**: JSON payloads to MQTT for analyst agent consumption with confidence scores

---

## Processing Pipeline

```
Mic Array (8-ch PCM via ALSA)
    ↓ FFT
GCC-PHAT (Localization)
    ↓ Azimuth/Elevation
Beamforming (Source Separation)
    ↓ Mono per source
Mel Spectrogram (librosa)
    ↓
YAMNet TFLite Inference
    ↓
JSON/MQTT → Agent Framework
```

---

## Tech Stack

C++ (ODAS), Python (librosa, NumPy, PyAudio), TensorFlow Lite (YAMNet), MQTT (Mosquitto), Raspberry Pi

---

[← Back to Projects](../projects)
