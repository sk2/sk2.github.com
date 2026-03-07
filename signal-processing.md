---
layout: default
---

# Signal Processing & Radio

Tools for radio spectrum monitoring, spatial audio analysis, and biometric signal processing — from SDR acquisition through ML classification to real-time visualization.

## Contents
- [How They Work Together](#how-they-work-together)
- [Radio Systems](#radio-systems)
- [Audio & Biometrics](#audio--biometrics)

---

## How They Work Together

<div class="mermaid">
flowchart TD
    HW["SDR Hardware Layer<br/><small>RTL-SDR · AirSpy HF+ · KrakenSDR · Microphone Arrays</small>"]
    HW --> SS["Streaming Server<br/><small>Multi-SDR Streaming Server</small>"]
    HW --> SR["Signal Reflection<br/><small>KrakenSDR</small>"]
    SS --> SA["Spectrum Analysis<br/><small>ML Classification + Vector Search</small>"]
    SR --> SA
</div>

**Typical workflow:** SDR hardware captures raw IQ samples → the streaming server distributes data over the network → spectrum analysis classifies and catalogs detected signals into a searchable inventory.

---

## Radio Systems

### Spectrum Analysis

<span class="status-badge status-active">Recently Updated</span> · <span class="stack-badge">Python</span> · [Full Details →](projects/signals)

Automated signal census system that transforms raw radio spectrum data into classified, searchable signal inventories. Combines SDR acquisition, ML classification, and vector search to detect, identify, and catalog signals across monitored bands.

![Spectrum waterfall](/images/spectra-waterfall.png)
*Real-time waterfall visualization of monitored spectrum.*

---

### Multi-SDR Streaming Server

<span class="status-badge status-active">Recently Updated</span> · <span class="stack-badge">Rust</span> · [Full Details →](projects/rtltcp)

Cross-platform server that manages multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the `rtl_tcp` protocol. A single Rust binary replaces multiple C-based streaming tools, adding a TUI for live device management and safe concurrency across all connected radios.

---

### Signal Reflection Analysis

<span class="status-badge status-active">Recently Updated</span> · <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> · [Full Details →](projects/rf-signal-analysis)

Distributed multi-beam signal reflection analysis system built on KrakenSDR hardware. A Raspberry Pi handles data acquisition and streams IQ data over UDP; a workstation runs compute-intensive DSP. All four channels process in parallel with independent Range-Doppler visualization and real-time performance monitoring.

---

## Audio & Biometrics

### Spatial Audio

<span class="status-badge status-active">Active</span> · [Full Details →](projects/soundarray)

Audio processing system using Raspberry Pi and microphone arrays for spatial sound analysis. Computes Time of Arrival (ToA) for sound localization and applies beamforming for directional isolation. Classifies sources — vehicles, aircraft, wildlife — and streams processed data for remote analysis.

---

### Heart Rate Analysis

<span class="status-badge status-active">Active</span> · <span class="stack-badge">Rust</span> · [Full Details →](projects/hrv)

Rust TUI application for real-time heart rate variability monitoring. Connects to BLE heart rate sensors via `btleplug`, computes time-domain HRV metrics (RMSSD, SDNN, pNN50), and stores session data in Apache Arrow/Parquet format for longitudinal analysis.

---

### Biometric Systems

<span class="status-badge status-active">Active</span> · <span class="stack-badge">Python</span> · [Full Details →](projects/healthypi)

Modular health monitoring ecosystem that translates raw biometric data from HealthyPi hardware into structured metrics. Swift collectors on Apple devices capture HealthKit data, publish to a NATS broker, and Python agents run analysis pipelines — coordinated by the [multi-agent orchestrator](/projects/multi-agent).

---

[← Back to Projects](projects) | [Network Automation](network-automation) | [Photography](photography) | [Data & Analytics](data-analytics) | [Autonomous Systems](agentic-systems)
