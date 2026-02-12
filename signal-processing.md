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

**Real-Time Visualization:**
The Spectra interface provides both high-level signal census data and low-level waterfall analysis for deep-dive signal inspection.

![Spectra Signal Census](/images/spectra-screenshot.png)
*Spectra Signal Census: Automated detection and classification of signals across the monitored band.*

![Spectra Waterfall](/images/spectra-waterfall.png)
*High-resolution waterfall display showing temporal signal patterns and frequency hopping.*

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
