---
layout: default
section: signal-processing
---

# soundarray

<span class="status-badge status-active">Active Development</span>

[← Back to Signal Processing](../signal-processing)

---

## Concept

The ability to capture, localize, and classify complex soundscapes on edge devices or via remote streaming, providing structured insights to an agent framework.

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

A spatial audio processing system using Raspberry Pi and microphone arrays. It combines sound source localization (Time of Arrival, beamforming) with ML-based classification (vehicles, wildlife) using ODAS for DSP and YAMNet for edge inference, publishing structured detections to an agent framework via MQTT.

## Key Features

- **Multi-Channel Audio Capture**: 4-8 channel USB/HAT microphone arrays (ReSpeaker, Matrix Creator)
- **Sound Source Localization**: GCC-PHAT and Kalman filter tracking for real-time azimuth and elevation
- **Adaptive Beamforming**: Directional sound isolation via ODAS — separate overlapping sources
- **Edge Classification**: YAMNet (521 classes) on TensorFlow Lite, optimized for ARM/NEON — vehicles, birds, bats, engines
- **Agent Integration**: JSON payloads to MQTT for analyst agent consumption with confidence scores

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

## Roadmap

- **Phase 1: Audio Foundation** — Multi-channel synchronized capture, remote streaming, valid WAV/PCM output
- **Phase 2: Spatial Intelligence** — Real-time azimuth reporting, beamformed mono isolation, moving source tracking
- **Phase 3: Intelligent Classification** — Vehicle/bird identification from beamformed audio, sustainable Pi CPU load, confidence scoring
- **Phase 4: Agent Dispatch & Monitoring** — MQTT payloads with spatial metadata, CLI dashboard, analyst agent integration

## Tech Stack

C++ (ODAS), Python (librosa, NumPy, PyAudio), TensorFlow Lite (YAMNet), MQTT (Mosquitto), Raspberry Pi

---

[← Back to Signal Processing](../signal-processing)
