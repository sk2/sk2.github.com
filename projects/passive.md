---
layout: default
---

# RF Signal Reflection Experiments

<span class="status-badge status-active">Phase 3/4 (100%)</span>

[← Back to Projects](../projects)

---

## The Insight

Ambient RF signals reflect off objects in the environment. By processing these reflections with coherent multi-channel receivers, we can extract bistatic range and Doppler shift information — an interesting signal processing challenge.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 3/4 (100%) |
| **Language** | Python, Signal Processing |
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
- **Educational**: Practical exploration of bistatic radar concepts and signal processing techniques

## Current Status

Clean, stable codebase for processing multi-channel RF reflections. Currently focused on establishing a solid signal processing foundation with single-channel experiments.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
