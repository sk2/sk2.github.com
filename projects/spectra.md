---
layout: default
---

# Project Spectra

<span class="status-badge status-active">Phase 2/3 (45%)</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1 complete, Phase 2 in progress |
| **Language** | Python + Rust + Swift |
| **Stack** | FastAPI · NumPy · Polars · PyQtGraph · ML |
| **Hardware** | Raspberry Pi 4/5 · Mac mini · Multiple SDRs |
| **Phase Completion** | 10/22 plans complete (45%) |
| **Started** | 2024 |
| **License** | TBD |

---

## Overview

Project Spectra is an autonomous distributed SIGINT system that monitors the radio spectrum, identifies modulations using ML, tracks aircraft and satellites, and maintains a "Signal Census" of all RF activity. Edge SDRs on Raspberry Pi units stream to Mac mini core for processing and classification.

## Problem It Solves

Radio spectrum monitoring requires expensive equipment and constant operator attention:

**Traditional SIGINT:**
- Manual scanning and identification
- Expensive professional receivers
- Single-location coverage
- No automated classification
- Operator fatigue from constant monitoring

**Hobbyist SDR:**
- Fragmented tools for each frequency range
- No unified view of spectrum activity
- Manual signal identification
- No persistent tracking or census
- Limited automation

**Project Spectra provides:**
- Automated 24/7 spectrum monitoring
- ML-based signal classification
- Distributed acquisition across frequency ranges
- Unified "Signal Census" database
- Real-time waterfall visualization
- Aircraft and satellite tracking
- Low-cost SDR hardware

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

**KrakenSDR:**
- 5-channel phase-coherent
- Direction of arrival (DoA)
- 24 MHz - 1766 MHz

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
- KrakenSDR DoA calculation
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

## Hardware Configuration

### SDR Units

| SDR | Frequency Range | Purpose | Antenna |
|-----|----------------|---------|---------|
| Airspy R2 | 24 MHz - 1.8 GHz | Primary scanner | Diamond D-130 Discone |
| Airspy HF+ | 9 kHz - 31 MHz | HF/Shortwave | MLA-30 Loop |
| KrakenSDR | 24 MHz - 1.7 GHz | Direction finding | 5x dipole array |
| RTL-SDR | 24 MHz - 1.7 GHz | ADS-B 1090 MHz | TA1 Turnstile |

### Antennas

**TA1 Turnstile:**
- VHF satellite reception (137 MHz)
- Circular polarization for rotating satellites
- Weather satellite images (NOAA, Meteor-M)

**Diamond D-130 Discone:**
- 25 MHz - 1300 MHz broadband
- Primary scanning antenna
- Omnidirectional coverage

**MLA-30 Loop:**
- 100 kHz - 30 MHz active loop
- Low-noise HF reception
- Small footprint for urban environments

**RF Chain:**
- Mini-Kits LNA for satellite reception
- Filtered power supply to reduce noise
- Quality coax (LMR-400) for low loss

## Use Cases

**24/7 Spectrum Monitoring:**
Continuous automated scanning with historical database of all activity.

**Aircraft Tracking:**
ADS-B reception with flight tracking and census integration.

**Satellite Reception:**
Automated tracking and recording of satellite passes (weather, amateur, ISS).

**Signal Intelligence:**
Identify unknown signals, track frequency usage patterns, detect anomalies.

**RF Mapping:**
Direction finding to locate signal sources and map RF environment.

## Technical Details

### Performance

- Real-time waterfall: 60 FPS display
- IQ bandwidth: 10 MSPS (Airspy R2)
- Latency: <100ms edge to core
- Census updates: Real-time as signals detected

### Data Pipeline

```
SDR → IQ Stream → FFT → Spectrum Frames → Waterfall Display
                   ↓
            Signal Detection → Census Database → ML Classifier
```

### Protocol Notes

**SpyServer:** TCP streaming, 5555 default port
**rtl_tcp:** TCP streaming, 1234 default port
**Beast:** ADS-B binary format, 30005 default port
**SBS:** ADS-B text format, 30002 default port
**Kraken:** HTTP control + data APIs

## Development Status

**Phase 1 Complete:** Foundation with SDR integration and visualization (10/10 plans)

**Phase 2 Active:** Intelligence features (0/12 plans)

**Next Steps:**
- Signal Census database implementation
- ML classifier training pipeline
- ADS-B integration with census
- Satellite TLE tracking

**Progress:** 45% overall (Phase 1: 100%, Phase 2: 0%)

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- PyQtGraph waterfall display showing spectrum
- WebGL browser waterfall with scroll control
- Textual TUI with live power meter
- Signal Census Polars DataFrame
- ADS-B aircraft tracking map
- Satellite pass prediction table
- KrakenSDR DoA visualization
- Bootstrap script output on Raspberry Pi
- systemd service status
- SpyServer connection logs
-->
