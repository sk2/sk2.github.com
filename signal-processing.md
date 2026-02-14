---
layout: default
---

# Signal Processing & RF Ecosystem

Experimental projects exploring SDR spectrum monitoring and biometric signal processing.

---

## Software Defined Radio

### Illumination Reflection Tracking

<span class="status-badge status-active">Phase 2/4 (56%)</span> · [Full Details →](projects/passive)

**What It Is:**
Building on open source implementations to analyze reflections of existing broadcast transmissions using coherent multi-channel SDR hardware.

**Current Status:** Phase 2 (Clean, stable foundation for reliable tracking)

**Tech Stack:** Python, numpy, scipy, Rust (planned migration)

---
### Project Spectra — SDR Client

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/signals)

**What It Is:**
A high-performance SDR client for spectrum monitoring and automated signal discovery. Spectra transforms raw IQ samples into a "Signal Census" using real-time ML classification.

![Spectra Waterfall](/images/spectra-waterfall.png)
*Spectra WebGL waterfall — real-time spectrum analysis with heat palette, streaming from a remote RTL-SDR.*

**Current Status:** Active development of ML classification engine.

**Tech Stack:** Python, numpy, scipy, RTL-SDR, HackRF, PyTorch (classification)

---

### Wi-Fi Radar — Through-Wall Detection

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/wifi-radar)

**What It Is:**
Using coherent SDR arrays for through-wall human detection via Wi-Fi signal phase analysis.

**Current Status:** Proof-of-concept detection working

**Tech Stack:** Rust

---

### rtltcp-rust — SDR Network Streaming

<span class="status-badge status-active">v1 — Core Streaming & Hardware</span> · [Full Details →](projects/rtltcp)

**What It Is:**
A high-performance Rust server that streams raw IQ samples from multiple SDR devices (RTL-SDR, AirSpy HF+) over the network using the industry-standard `rtl_tcp` protocol, with a built-in TUI for live configuration.

**Key Features:**
- Multi-threaded architecture for concurrent streaming from multiple SDRs
- Terminal User Interface (TUI) for real-time frequency, gain, and sample rate adjustments
- TOML-based persistent configuration
- Cross-platform with Raspberry Pi target for headless remote stations

**Current Status:** Building v1 core streaming — hardware access (librtlsdr/libairspyhf wrapping), rtl_tcp protocol implementation, TUI interface, and persistent configuration.

**Tech Stack:** Rust, tokio, ratatui (TUI), librtlsdr/libairspyhf (FFI)

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

## Open Source & Contributions

- **HealthyPi Ecosystem**: [github.com/sk2/healthypi](https://github.com/sk2/healthypi)
- **Project Spectra**: [github.com/sk2/spectra](https://github.com/sk2/spectra)
- **rtltcp-rust**: [github.com/sk2/rtltcp-rust](https://github.com/sk2/rtltcp-rust)
- **soundarray**: [github.com/sk2/soundarray](https://github.com/sk2/soundarray)
- **Illumination Reflection**: [github.com/sk2/passive-radar](https://github.com/sk2/passive-radar)
- **Wi-Fi Radar**: [github.com/sk2/wifi-radar](https://github.com/sk2/wifi-radar)

---

[← Back to Projects](projects) | [View CV](cv) | [Network Automation](network-automation) | [Data Analytics](data-analytics) | [Agentic Systems](agentic-systems)

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
