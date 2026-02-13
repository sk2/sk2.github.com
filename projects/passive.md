---
layout: default
---

# Passive Radar — Bistatic Target Detection

<span class="status-badge status-active">Phase 3/4 (100%)</span>

[← Back to Projects](../projects)

---

## The Insight

Passive radar exploits existing radio transmissions as illuminators of opportunity, detecting targets through their reflections without requiring dedicated transmitters. This approach enables covert surveillance and target tracking using ambient RF signals.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 3/4 (100%) |
| **Language** | Python, Signal Processing |
| **Started** | 2026 |

---

## What This Is

A passive radar system that detects and tracks targets by analyzing reflections of ambient radio signals. The system processes coherent multi-channel RF data to extract bistatic range and Doppler information, enabling real-time target detection without active transmission.

## Core Principles

**Illumination and Reflection:**
- **Illuminators of Opportunity**: Uses existing transmitters (FM radio, DVB-T, cellular) as non-cooperative illumination sources
- **Bistatic Geometry**: Separates transmitter, target, and receiver — targets reflect illuminator signals toward receiver
- **Cross-Correlation Processing**: Correlates reference channel (direct signal) with surveillance channels (reflections) to extract target echoes
- **Range-Doppler Processing**: Maps targets in bistatic range and Doppler shift dimensions

**Signal Processing Chain:**
1. **Direct Signal Acquisition**: Capture clean reference from illuminator
2. **Surveillance Channel Processing**: Receive reflected signals with target echoes
3. **Adaptive Cancellation**: Remove direct signal and multipath interference
4. **Cross-Correlation**: Extract target echoes via time-delay cross-correlation
5. **Doppler Analysis**: Apply FFT to detect moving targets
6. **Detection & Tracking**: Threshold detections and form tracks over time

**Key Advantages:**
- **Covert Operation**: No active transmission reveals receiver location
- **Cost-Effective**: Leverages existing RF infrastructure
- **Multi-Target Tracking**: Simultaneous detection of multiple targets
- **Resilience**: Difficult to jam without disrupting commercial services

## Current Status

Clean, understandable, stable codebase that reliably tracks aircraft in real-time. Currently focused on establishing a solid foundation with single-channel processing before expanding to advanced multi-beam correlation capabilities.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
