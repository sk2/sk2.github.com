---
layout: default
section: signal-processing
---

# Project Spectra

<span class="status-badge status-active">Phase 6/7 — Operational Readiness</span>

[← Back to Signal Processing](../signal-processing)

---

## The Insight

Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 6/7 — Operational Readiness |
| **Language** | Python, Rust, Swift |
| **Started** | 2026 |

---

## What This Is

A high-performance SDR client for spectrum monitoring and automated signal discovery. Spectra transforms raw IQ samples into a "Signal Census" through automated detection, ML classification, and distributed acquisition across Raspberry Pi edge nodes with Mac mini core processing.

The system provides both high-level signal census data and low-level waterfall analysis for deep-dive signal inspection.

![Spectra Waterfall](/images/spectra-waterfall.png)
*High-resolution waterfall display showing temporal signal patterns across the monitored band.*

**Tech Stack:** Python, Rust (Axum backend), numpy, scipy, RTL-SDR, Airspy, PyTorch (classification), DuckDB (Signal Census)

---

[← Back to Signal Processing](../signal-processing)
