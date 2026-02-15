---
layout: default
---

# Signal Processing & RF Ecosystem

Experimental projects exploring SDR spectrum monitoring and biometric signal processing.

---

## Software Defined Radio

### Project Spectra — Autonomous Spectrum Monitoring

<span class="status-badge status-active">Phase 6/7 — Operational Readiness</span> · [Full Details →](projects/signals)

**What It Is:**
A distributed spectrum monitoring system that autonomously scans radio bands, classifies signals using ML, and maintains a persistent "Signal Census" database. Raspberry Pi edge nodes stream IQ samples to a Mac mini core for processing, classification, and visualization.

![Spectra TUI](/images/spectra-tui.png)
*Spectra Rust TUI — live spectrum, Kitty graphics waterfall, and device controls.*

**Key Features:**
- Two-stage ML classification pipeline (real-time + retrospective)
- Signal Census database (DuckDB) with anomaly detection
- Autonomous missions: bandplan sweeping, satellite pass scheduling
- Direction finding via Kraken SDR (5-channel coherent receiver)
- WebGL waterfall frontend, Rust TUI, and REST API

**Current Status:** 58/58 plans complete across Phases 1–6. Phase 7 (performance optimization) planned.

**Tech Stack:** Python, Rust, TypeScript, FastAPI, React, DuckDB, PyTorch, Skyfield

---

### Multi-SDR Streaming Server

<span class="status-badge status-active">Phase 3/4 — TUI & Live Config (90%)</span> · [Full Details →](projects/rtltcp)

**What It Is:**
A single Rust binary that auto-detects every connected SDR (RTL-SDR, AirSpy HF+, AirSpy), streams each over the standard `rtl_tcp` protocol, and provides a TUI dashboard and HTTP API for monitoring and control.

**Key Features:**
- Auto-detection and concurrent streaming from RTL-SDR, AirSpy HF+, and AirSpy devices
- TUI dashboard with live frequency, gain, and sample rate adjustment over SSH
- HTTP REST API for device status, health checks, and programmatic monitoring
**Current Status:** Phase 3 at 90% — TUI dashboard, interactive controls, and HTTP API complete. Config save/reload remaining.

**Tech Stack:** Rust, tokio, axum, ratatui

---

### Illumination Reflection Tracking

<span class="status-badge status-active">Phase 2/4 (56%)</span> · [Full Details →](projects/passive)

**What It Is:**
Building on open source implementations to analyze reflections of existing broadcast transmissions using coherent multi-channel SDR hardware.

**Current Status:** Phase 2 (Clean, stable foundation for reliable tracking)

**Tech Stack:** Python, numpy, scipy, Rust (planned migration)

---

### Wi-Fi Signal Reflection — Through-Wall Detection

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/wifi-radar)

**What It Is:**
Using coherent SDR arrays for through-wall human detection via Wi-Fi signal reflection and phase analysis.

**Current Status:** Proof-of-concept detection working

**Tech Stack:** Rust

---

## Audio Processing

### soundarray — Spatial Audio Processing

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/soundarray)

**What It Is:**
An exploration-focused audio processing system using Raspberry Pi and microphone arrays. Focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.

**Key Features:**
- **Time of Arrival (ToA) Estimation**: Localize sound sources using microphone array phase differences
- **Beamforming**: Directionally filter audio to enhance signals from specific angles
- **Sound Classification**: Classify vehicles and wildlife by acoustic signatures
- **Agent Integration**: Provides structured insights to analyst agent frameworks

**Current Status:** Exploring hardware options (ReSpeaker, Matrix arrays) and beamforming algorithms

**Tech Stack:** Python, numpy, scipy, PyTorch/TensorFlow (classification)

---

## Health & Biometrics

### HealthyPi Biometric Signal Processing

<span class="status-badge status-active">Experimental</span> · [Full Details →](projects/healthypi)

**What It Is:**
Experimental signal processing using the [HealthyPi](https://www.crowdsupply.com/protocentral/healthypi-move) biometric hardware platform (developed by Protocentral) for ECG, PPG, and respiration analysis with NeuroKit2.

**Current Status:** Phase 6 (NATS integration + reconnection handling + tests)

**Tech Stack:** Python, NeuroKit2, numpy, scipy, NATS

---

[← Back to Projects](projects)

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
.status-planning {
  background-color: #ffc107;
  color: #343a40;
}
</style>
