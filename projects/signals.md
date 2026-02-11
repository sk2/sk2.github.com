---
layout: default
---

# signals

<span class="status-badge status-complete">Production Ready</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Production Ready |
| **Language** | Python, Rust (planned), Swift (visualization), ML frameworks |
| **Started** | 2025 |

---

## The Insight

Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.

## Architecture

- **Edge**: Raspberry Pi 4/5 with multiple SDRs streaming IQ data.
- **Core**: Mac mini M-Series for ML inference, storage, visualization (leveraging Neural Engine).
- **Network**: Low-latency local network for IQ streaming.

## Hardware Configuration

*SDRs:*
- Airspy R2 (primary wideband scanner).
- Airspy HF Discovery (HF/LF coverage).
- KrakenSDR (5-channel phase-coherent for Direction of Arrival).
- RTL-SDR (utility/ADS-B reception).

*Antennas:*
- TA1 Turnstile (satellite/VHF).
- Diamond D-130 Discone (broadband scanner).
- MLA-30 Loop (LF/HF).
- Mini-Kits LNA for satellite reception.

## Planned Features

- Real-time waterfall visualization with multi-SDR switching.
- Automated modulation detection with SigIDWiki pattern matching.
- Autonomous frequency band scanning with persistent Signal Census database.
- Automatic NOAA/Meteor satellite recording based on orbital calculations.
- KrakenSDR Direction of Arrival for spatial RF mapping.
- ADS-B aircraft tracking on unified geographical display.

## Philosophy

Edge-first architecture, sustainable always-on monitoring, minimal manual intervention.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)