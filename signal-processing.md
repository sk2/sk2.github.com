---
layout: default
---

# Signal Processing & RF Ecosystem

Experimental projects exploring SDR spectrum monitoring and biometric signal processing.

---

## Software Defined Radio

### Project Spectra — Autonomous Spectrum Monitoring

<span class="status-badge status-active">Phase 9/12 — v2.0 Signal Intelligence</span> · [Full Details →](projects/signals)

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
- **v2.0 WebSocket Foundation**: Multiplexed WebSocket streaming, dual-mode TUI, web-based visualization

**Current Status:** v1.0 complete (58/58 plans). v2.0 Phase 9 in progress (11/55 plans complete) — central server architecture with WebSocket streaming and signal intelligence overlay.

**Tech Stack:** Python, Rust, TypeScript, FastAPI, React, DuckDB, PyTorch, Skyfield, WebSocket

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

<span class="status-badge status-active">Phase 6/10 — Track Management</span> · [Full Details →](projects/passive)

**What It Is:**
Analyzes reflections of existing broadcast transmissions using coherent multi-channel SDR hardware (KrakenSDR). Distributed multi-beam system with parallel surveillance channels for real-time aircraft tracking.

**Current Status:** Phase 6 — implementing track management and association logic. Phase 5 (CFAR detection) complete.

**Tech Stack:** Python, numpy, scipy, ProcessPoolExecutor

---

### Wi-Fi Signal Reflection — Through-Wall Detection

<span class="status-badge status-complete">Phase 5 — Complete</span> · [Full Details →](projects/wifi-radar)

**What It Is:**
Coherent SDR array processing for through-wall human detection via Wi-Fi signal reflection and phase analysis.

**Current Status:** Phase 5 complete — proof-of-concept detection operational

**Tech Stack:** Python, Signal Processing

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

### HRV Monitor — Real-Time Heart Rate Variability

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/hrv)

**What It Is:**
Rust-based BLE driver for heart rate variability monitoring. Connects to consumer HRV sensors (Elite HRV CorSense, Morpheus M7), streams raw RR intervals, computes time-domain metrics (RMSSD, SDNN, pNN50, AVNN) in real-time, and logs sessions to Parquet files for analysis.

**Key Features:**
- **Real-Time Metrics**: Live HRV computation with rolling 60-second windows
- **BLE Streaming**: Direct connection to standard Bluetooth Heart Rate Profile devices
- **Terminal Dashboard**: TUI with live charts and metric visualization
- **Session Logging**: Automatic Parquet export for DuckDB/Polars analysis

**Current Status:** Core functionality complete, Linux support and frequency-domain metrics planned

**Tech Stack:** Rust, btleplug, ratatui, cardio-rs, Apache Arrow/Parquet

---

### HealthyPi Biometric Signal Processing

<span class="status-badge status-active">Phase 6/6 — Apple Ecosystem (v1.0, 87%)</span> · [Full Details →](projects/healthypi)

**What It Is:**
Modular signal processing ecosystem using the [HealthyPi](https://www.crowdsupply.com/protocentral/healthypi-move) biometric hardware platform (developed by Protocentral) for ECG, PPG, respiration, and EEG analysis with NeuroKit2.

**Key Features:**
- Virtual patient simulator for development without hardware
- NATS message bus integration for agent coordination
- Pydantic models for ECG, PPG, EDA, EEG, IMU, and respiration
- HealthyPiKit Swift package for Apple ecosystem integration

**Current Status:** Phase 6, Plan 2/7 (87% complete) — Apple ecosystem integration. Phases 1-5 complete and verified.

**Tech Stack:** Python, Swift, NeuroKit2, numpy, scipy, NATS, Pydantic

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
.status-complete {
  background-color: #28a745;
  color: white;
}
</style>
