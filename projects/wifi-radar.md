---
layout: default
section: signal-processing
---

# Wi-Fi Radar (KrakenSDR)

<span class="status-badge status-active">Active Development</span>

[← Back to Signal Processing](../signal-processing)

---

## Concept

Wi-Fi signals penetrate walls and reflect off human bodies, creating detectable Doppler shifts and signal disruptions. By processing these reflections with coherent multi-channel receivers, we can detect and localize human presence through walls — a signal processing challenge that relies entirely on existing Wi-Fi infrastructure.

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

An experimental signal processing system that analyzes reflections of ambient Wi-Fi signals (2.4 GHz / 5 GHz) for through-wall human detection and localization. The system uses coherent multi-channel RF receivers to process reflected Wi-Fi signals, extracting micro-Doppler signatures and bistatic range information to detect and localize human movement.

## Core Principles

**Wi-Fi as Illumination Source:**
- **Ubiquitous Coverage**: Wi-Fi access points provide dense, continuous illumination in urban/indoor environments
- **Wall Penetration**: 2.4 GHz signals penetrate common building materials (drywall, wood, brick)
- **Reflection Characteristics**: Human bodies create measurable reflections at Wi-Fi frequencies
- **Micro-Doppler Signatures**: Breathing, walking, and limb motion create characteristic Doppler patterns

**Bistatic Geometry:**
- **Wi-Fi AP as Transmitter**: Existing access points serve as non-cooperative illuminators
- **Target Reflection**: Human bodies reflect Wi-Fi signals toward receiver array
- **Coherent Processing**: Multiple receiver channels enable angle-of-arrival estimation and beamforming
- **Range-Doppler Mapping**: Cross-correlation extracts bistatic range; FFT reveals Doppler shifts from motion

**Signal Processing Challenges:**
- **Direct Signal Cancellation**: Remove strong direct path from AP to receiver (adaptive filtering)
- **Multipath Suppression**: Indoor environments create complex multipath reflections
- **Clutter Rejection**: Static objects (furniture, walls) must be filtered from moving targets
- **Low SNR Operation**: Human reflections are weak compared to direct signal and clutter

## Technical Approach

The system processes coherent multi-channel Wi-Fi signals using:
1. **Reference Signal Extraction**: Capture direct Wi-Fi signal from AP
2. **Surveillance Channel Processing**: Receive reflected signals from multiple antennas
3. **Adaptive Interference Cancellation**: Remove direct signal and static multipath
4. **Beamforming**: Spatial filtering to enhance target signals
5. **Range-Doppler Processing**: Extract target range and velocity
6. **Micro-Doppler Analysis**: Classify human activity patterns
7. **Tracking**: Maintain target tracks over time
---

[← Back to Signal Processing](../signal-processing)

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-complete {
  background-color: #28a745;
  color: white;
}
</style>
