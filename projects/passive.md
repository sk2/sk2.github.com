---
layout: default
section: signal-processing
---

# Passive Radar - KrakenSDR Multi-Beam System

<span class="status-badge status-active">Phase 7/10 (60%)</span>

[← Back to Signal Processing](../signal-processing)

---

## Concept

Ambient RF signals reflect off objects in the environment. By processing these reflections with coherent multi-channel receivers, we can extract bistatic range and Doppler shift information — an interesting signal processing challenge.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 7/10 (60%) |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

An experimental signal processing project exploring how to analyze reflections of ambient radio signals. The system uses coherent multi-channel RF data to study bistatic geometry and Doppler effects.

## Core Principles

**Signal Reflection and Processing:**
- **Ambient Transmitters**: FM radio, DVB-T, or cellular signals serve as convenient RF sources
- **Bistatic Geometry**: Separates transmitter and receiver — objects reflect signals toward the receiver
- **Cross-Correlation Processing**: Correlates reference channel (direct signal) with surveillance channels (reflections)
- **Range-Doppler Mapping**: Extracts time-delay and frequency-shift information from reflections

**Signal Processing Chain:**
1. **Reference Signal Capture**: Acquire clean direct signal from transmitter
2. **Reflection Channel Processing**: Receive signals containing reflections
3. **Adaptive Interference Cancellation**: Remove direct signal and static multipath
4. **Cross-Correlation**: Extract reflection signatures via time-delay analysis
5. **Doppler Analysis**: Apply FFT to study frequency shifts from motion
6. **Detection Processing**: Threshold analysis and signal extraction

**Why This Approach:**
- **Cost-Effective**: Uses existing RF infrastructure for experiments
- **Educational**: Practical exploration of bistatic geometry and signal processing techniques

## Architecture

**v1.0 Foundation (Phases 1-4, Complete):**
Established distributed multi-beam architecture using ProcessPoolExecutor for parallel surveillance channels. CFAR detection (Phase 5) implemented and verified.

**v2.0 Real-Time Tracking (Phases 5-10, In Progress):**

Currently implementing track management and association logic (Phase 6). The system now maintains tracks across multiple beams with detection-level recording for storage efficiency.

**Key Features:**
- **Multi-Beam Processing**: Parallel surveillance channels across 5-channel coherent array
- **CFAR Detection**: Constant False Alarm Rate detection complete
- **Track Management**: Per-beam tracking with cross-beam fusion planned for v3
- **Real-Time Operation**: Aircraft tracking with sub-second latency

## Current Status

Phase 6 in progress. Clean, understandable, stable codebase that reliably tracks aircraft in real-time. Phase 5 (CFAR Detection) complete and verified.

---

[← Back to Signal Processing](../signal-processing)
