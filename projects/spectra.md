---
layout: default
section: signal-processing
---

# Project Spectra

<span class="status-badge status-active">Phase 2/3 (45%)</span>

[← Back to Signal Processing](../signal-processing)

---


## The Concept

Manual radio spectrum monitoring is resource-intensive and prone to operator fatigue. **Project Spectra** automates wideband scanning and modulation identification using a distributed architecture. It uses Raspberry Pi nodes for edge acquisition and a Mac mini core for ML-based signal classification and historical "Signal Census" tracking.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 2/3 (45%) |
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

### Phase 2 In Progress: Intelligence (0/12 plans)

**Signal Census Database:**
- Detect signals above noise floor
- Track frequency, bandwidth, modulation
- Historical activity logging
- Query interface for analysis

**ML Classification:**
- TensorFlow/PyTorch modulation classifier
- Training data collection pipeline
- Automatic mode identification
- Confidence scoring

**Aircraft Tracking:**
- ADS-B message decoding
- Flight tracking database
- Integration with Signal Census

**Satellite Tracking:**
- TLE (Two-Line Element) orbital prediction
- VHF/UHF satellite pass detection
- Doppler correction

### Phase 3 Planned: Autonomy

**Direction Finding:**
- Coherent array DoA calculation
- Signal source localization
- Azimuth estimation

**Automated Collection:**
- Priority-based scanning
- Anomaly detection and focus
- Scheduled collection windows

**Alerts:**
- Notification system for events
- New signal detection
- Aircraft proximity
- Satellite pass predictions

---

[← Back to Signal Processing](../signal-processing)
