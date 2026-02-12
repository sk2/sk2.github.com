---
layout: default
---

# Signal Processing & RF Ecosystem

Experimental projects exploring SDR spectrum monitoring and biometric signal processing.

---

## Software Defined Radio

### Passive Radar — KrakenSDR Multi-Beam System

<span class="status-badge status-active">Phase 2/4 (56%)</span> · [Full Details →](projects/passive)

**What It Is:**
Building on open source passive radar implementations to track aircraft using KrakenSDR (5-channel coherent SDR) by analyzing reflections of existing FM radio transmissions.

**Current Status:** Phase 2 (Clean, stable foundation for reliable tracking)

**Tech Stack:** Python, numpy, scipy, KrakenSDR firmware, Rust (planned migration)

---

### Project Spectra — SDR Client

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/signals)

**What It Is:**
An SDR client for spectrum monitoring and signal analysis using RTL-SDR and HackRF hardware.

**Features:**
- Wide-band scanning with RTL-SDR and HackRF
- Signal detection and classification
- Real-time waterfall display

![Spectra Signal Census](images/spectra-screenshot.png)

![Spectra Waterfall](images/spectra-waterfall.png)

**Current Status:** Active development

**Tech Stack:** Python, numpy, scipy, RTL-SDR, HackRF

---

### Wi-Fi Radar — Through-Wall Detection

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/wifi-radar)

**What It Is:**
Using KrakenSDR for through-wall human detection via Wi-Fi signal phase analysis.

**Current Status:** Proof-of-concept detection working

**Tech Stack:** Rust, KrakenSDR

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
- **Passive Radar**: [github.com/sk2/passive-radar](https://github.com/sk2/passive-radar)
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
