---
layout: default
section: signal-processing
---

# Signal Reflection Analysis

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Technical Reports

- [Download Technical Report](/assets/docs/rf-signal-analysis-passive-radar-techreport.pdf)

---

## Concept

Distributed multi-beam signal reflection analysis system built on KrakenSDR hardware. A Raspberry Pi handles data acquisition and streams IQ data over UDP; a Mac or Linux workstation runs compute-intensive DSP. All four surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.

---

## Architecture

The KrakenSDR provides five receive channels: one reference channel (direct signal from transmitter) and four surveillance channels (directional antennas capturing reflected signals). The Heimdall DAQ library runs on the Pi, streaming IQ at 65–80 FPS over UDP. The processing host receives IQ data, computes Range-Doppler maps using pyapril, and renders results in a Dash web dashboard.

Key design choices:

- **ProcessPoolExecutor** for true parallelism across four beams, bypassing the GIL
- **Asyncio** networking for non-blocking IQ streaming and control
- **Pydantic** configuration validation catches errors at startup
- **mDNS** service discovery with manual IP fallback

9,600 lines of Python. Four phases shipped across 25 plans.

---

## Features

**Shipped (v1.0):**
- Four-beam parallel processing with 2x2 Range-Doppler grid
- Distributed Pi-to-workstation streaming architecture
- Per-beam configuration and performance monitoring
- Connection health monitoring with graceful recovery

**In progress (v2.0 — target tracking):**
- Per-beam CFAR target detection and track association
- Geographic projection (beam geometry + range to lat/lon)
- ADS-B integration for track validation against ground truth
- Detection recording for offline algorithm tuning

---

[← Back to Signal Processing](../signal-processing)
