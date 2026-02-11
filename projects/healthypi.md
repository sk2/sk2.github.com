---
layout: default
---

# healthypi

<span class="status-badge status-complete">Production Ready</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Production Ready |
| **Language** | Python, NATS, NeuroKit2 |
| **Started** | 2025 |

---

## The Insight

Health monitoring is often trapped in silos—either raw sensor data that is hard to interpret or consumer apps that offer "scores" without transparency. The **HealthyPi Ecosystem** treats biometrics as a stream of events for an intelligent agent. By integrating research-grade signal processing (HRV, EDA, ECG) with a multi-agent message bus, it turns a Raspberry Pi into an autonomous health observer capable of real-time intervention and longitudinal analysis.

## What This Is

Modular health monitoring ecosystem translating HealthyPi hardware biometric data (ECG, PPG, EDA, EEG, IMU) into insights through agentic intelligence.

## Architecture

- **Standardized data models**: Multi-modal biometric data with JSON/Parquet serialization.
- **Virtual Patient simulator**: NeuroKit2-based physiological signal generation for hardware-free development.
- **Real-time analysis engine**: HRV (time/frequency domain), EDA stress detection, activity classification.
- **NATS integration**: Publishes raw signals and processed metrics to the agent-framework message bus.

## Technical Depth

- 286 comprehensive tests validating signal processing and analysis algorithms.
- 6 physiological states with research-backed parameter ranges (WESAD dataset).
- Frequency-domain HRV: 4 Hz RR resampling, Hann window, rFFT PSD with LF/HF band integration.
- EDA tonic/phasic decomposition using SciPy primitives.
- Modular architecture: agents consume health trends and metrics.

## Hardware

HealthyPi 6 (Pi HAT), HealthyPi Move (wearable).

## Current Status

2026-02-10 - Completed 05-03-PLAN.md (Quick Glance dropdown + notifications + UX verified).

---

[← Back to Projects](../projects) | [Development Philosophy](../development)