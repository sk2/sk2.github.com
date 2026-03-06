---
layout: default
section: signal-processing
---

# Spectrum Analysis

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Contents

- [Technical Reports](#technical-reports)
- [Visuals](#visuals)
- [Concept](#concept)
- [Current Milestone: v2.0 — Central Server Integration](#current-milestone-v20-central-server-integration)
- [Stakeholders](#stakeholders)
- [Constraints & Assumptions](#constraints-assumptions)
- [Current Status](#current-status)

![Hero Image](/images/search_topk_example.png)


---

## Technical Reports

- [Download Technical Report: spectra-techreport.pdf](/assets/docs/signals-spectra-techreport.pdf)

---

## Visuals

### Waterfall & TUI Interface

![Spectra Waterfall](/images/spectra-waterfall-screenshot.png)

### RF Fingerprinting Results

![RF Fingerprinting](/images/rf_fingerprinting_results.png)

### Vector Search (Top-K Matches)

![Vector Search](/images/search_topk_example.png)

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## Concept

Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.

---

## Current Milestone: v2.0 — Central Server Integration

**Goal:** Make the Python backend the single central server that owns all SDR connections, processes IQ into spectrum/classifications/demod, and streams compact results to thin clients (TUI + Web) over WebSocket. No raw IQ crosses the wire to clients. No double handling.

**Target features:**
- Multiplexed WebSocket protocol (spectrum bins + signal detections + classifications + demod audio + control)
- Python backend enrichment: single-connection SDR ownership, on-demand classification, demod streaming
- TUI advanced mode: receives pre-processed spectrum from Python backend (basic mode preserved)
- Web client updates: consumes same WebSocket protocol as TUI
- End-to-end flow: user selects signal in TUI/Web → Python classifies → result displayed

---

## Stakeholders

- **User:** Solo operator/developer

---

## Constraints & Assumptions

- **Edge Hardware:** Raspberry Pi 4/5.
- **SDRs:** 
  - Airspy R2 (Primary Scanner)
  - Airspy HF Discovery (HF/LF)
  - KrakenSDR (5-channel phase-coherent for DoA)
  - RTL-SDR (Utility/ADS-B)
- **Antennas:**
  - TA1 Turnstile (Satellite/VHF)
  - Diamond D-130 Discone (Broadband Scanner)
  - MLA-30 Loop (LF/HF)
- **RF Chain:** Mini-Kits LNA for Satellite reception.
- **Core Hardware:** Mac mini M-Series (Processing/ML/Storage).
- **Network:** Low-latency local network for IQ streaming.
- **ML:** Leverages Mac Neural Engine.

---

## Current Status

** 2026-03-04 — Completed  Audio Content Intelligence

---

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
