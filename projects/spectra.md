---
layout: default
section: signal-processing
---

# Project Spectra

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Capabilities](#capabilities)
- [Status](#status)

## Concept

Distributed spectrum monitoring system built on Raspberry Pi edge nodes and a Mac mini core. Multiple SDR receivers (Airspy, RTL-SDR, KrakenSDR) stream IQ data to a central orchestrator that runs ML classification, signal census tracking, and real-time waterfall visualization. The system autonomously sweeps bands, identifies signal modulations, and maintains a historical database of spectrum activity.

---

## Architecture

```
Edge Pi (SDR) → SpyServer/rtl_tcp → Mac mini Core
                                         ↓
                             Orchestrator → ML Pipeline
                                         ↓
                             Signal Census Database
                                         ↓
                         Desktop/Web Visualizers
```

**Edge nodes** run on Raspberry Pi units, each with a specialized SDR:
- Airspy R2 (24 MHz–1.8 GHz, 10 MSPS) — primary scanner
- Airspy HF Discovery (9 kHz–31 MHz) — HF/amateur bands
- KrakenSDR — coherent multi-channel array for direction-of-arrival
- RTL-SDR — ADS-B (1090 MHz) and utility scanning

**Core** runs on a Mac mini with Neural Engine:
- FastAPI orchestrator managing edge connections and spectrum acquisition
- CNN modulation classifier using CoreML inference
- DuckDB-backed Signal Census with SigIDWiki integration
- FM/AM/SSB audio demodulation pipeline

**Visualization** via PyQtGraph (desktop) and WebGL (browser) waterfall displays with per-bin max aggregation.

---

## Capabilities

- SDR protocol support: SpyServer, rtl_tcp, readsb (ADS-B), Kraken HTTP
- Two-stage ML classification pipeline with constellation diagram analysis
- Priority-based band sweeping with scheduled collection windows
- Satellite pass scheduling using TLE orbital prediction
- Direction of arrival (DoA) mapping with coherent arrays
- Baseline anomaly detection for new or unusual signals
- Automated briefing generation from scan results
- Health instrumentation with auto-reconnect and failure isolation

---

## Status

**Current**: Advanced ML/DSP — de-noising, blind signal separation, emitter identification, vector search, and beamforming.

**Completed:**
- Foundation — SDR protocol clients, asyncio orchestrator, waterfall visualization
- Intelligence — CNN classifier (CoreML), Signal Census (DuckDB), audio demodulation
- Autonomy — automated collection, satellite scheduling, DoA mapping
- Spectrum Autopilot — mission-driven scanning and automated briefings
- Verification — end-to-end test harness, health instrumentation, auto-reconnect

---

[← Back to Signal Processing](/signal-processing)

[← Back to Projects](/projects)
