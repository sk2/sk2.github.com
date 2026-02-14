---
layout: default
section: signal-processing
---

# Project Spectra

<span class="status-badge status-active">Phase 6/7 — Operational Readiness</span>

[← Back to Signal Processing](../signal-processing)

---


## The Concept

Manual radio spectrum monitoring is resource-intensive and prone to operator fatigue. **Project Spectra** automates wideband scanning and modulation identification using a distributed architecture. It uses Raspberry Pi nodes for edge acquisition and a Mac mini core for ML-based signal classification and historical "Signal Census" tracking.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 6/7 — Operational Readiness |
| **Language** | Python + Rust + Swift |
| **Started** | 2026 |

---

## What This Is

An autonomous distributed SIGINT system. It monitors the RF spectrum, identifies modulations via ML, and tracks aircraft (ADS-B) and satellites. It leverages NATS for coordination and Polars for high-performance data indexing.

## Architecture

### Edge Nodes: Raspberry Pi

Multiple Pi units with specialized SDRs:

**Airspy R2 (Primary Scanner):**
- 24 MHz - 1800 MHz coverage
- 10 MSPS bandwidth
- SpyServer protocol streaming

**Airspy HF Discovery:**
- 9 kHz - 31 MHz (HF/LF)
- Amateur radio bands
- Maritime, shortwave broadcast

**Coherent SDR Arrays:**
- Multi-channel phase-coherent capability
- Direction of arrival (DoA) analysis
- 24 MHz - 1766 MHz coverage

**RTL-SDR:**
- 1090 MHz ADS-B (aircraft)
- Utility scanning
- Low-cost backup

### Core: Mac mini M-Series

Central processing and ML inference:

**FastAPI Orchestrator:**
- Manages edge SDR connections
- Coordinates spectrum acquisition
- WebSocket streaming to clients

**ML Classification:**
- Leverages Neural Engine
- Signal modulation identification
- Automatic mode detection

**Signal Census:**
- Polars DataFrame tracking
- Historical activity database
- Frequency/modulation/time indexing

**Visualization:**
- PyQtGraph waterfall (desktop)
- WebGL waterfall (browser)
- Real-time spectrum display

### Network Architecture

```
Edge Pi → SpyServer/rtl_tcp → Mac mini Core
                                    ↓
                        Orchestrator → ML Pipeline
                                    ↓
                        Signal Census Database
                                    ↓
                Desktop/Web Visualizers
```

## Features

### Phase 1 Complete: Foundation ✅

**SDR Protocol Support:**
- SpyServer client (NumPy-based IQ streaming)
- rtl_tcp client (RTL-SDR network protocol)
- readsb (ADS-B Beast/SBS protocols)
- Kraken HTTP control API

**Orchestrator:**
- Asyncio TCP clients for streaming
- Per-device in-memory IQ buffers
- Bandwidth-friendly spectrum frames (uint8)
- Background task management

**Visualizations:**
- PyQtGraph real-time waterfall (desktop)
- WebSocket + WebGL browser waterfall
- Scroll speed control and throttling
- Per-bin max aggregation for smooth display

**Infrastructure:**
- Raspberry Pi bootstrap script (SDR drivers)
- systemd service configuration
- Network bandwidth optimization
- Mock servers for deterministic testing

### Phase 2 Complete: Intelligence ✅

**ML Classification:**
- CNN modulation classifier with CoreML inference on Mac Neural Engine
- Two-stage classification pipeline with confidence scoring
- Constellation diagram analysis for automatic mode identification

**Signal Census Database:**
- DuckDB-backed Signal Census for durable historical tracking
- SigIDWiki integration for known signal identification
- Frequency, bandwidth, modulation, and temporal indexing

**Audio Demodulation:**
- FM/AM/SSB demodulation pipeline
- Audio output for monitored signals

### Phase 3 Complete: Autonomy ✅

**Automated Collection:**
- Priority-based band sweeping and scheduled collection windows
- Satellite pass scheduling with TLE orbital prediction
- Direction of arrival (DoA) mapping with coherent arrays

**Persistent Monitoring:**
- Baseline and anomaly detection for new or unusual signals
- Signal Census maintenance with automated updates

### Phase 5 Complete: Spectrum Autopilot ✅

**Mission-Driven Scanning:**
- Automated scanning behavior driven by mission parameters
- Automated briefing generation

### Phase 6 Complete: Verification & Operational Readiness ✅

**Infrastructure Verification:**
- End-to-end verification harness with mock testing
- Health instrumentation (`/api/health/deep`)
- Auto-reconnect with exponential backoff (1s→30s) and per-device failure isolation
- Real hardware validation ready but deferred

### Roadmap

- **Phase 4: Research & Evolution** — Advanced ML/DSP including de-noising, blind signal separation, emitter identification, vector search, and beamforming
- **Phase 7: Performance Optimization** — GPU acceleration, waterfall ring buffer optimization, memory profiling, batch updates

---

[← Back to Signal Processing](../signal-processing)
