---
layout: default
section: signal-processing
---

# Spectrum Analysis

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Technical Reports

- [Download Technical Report: spectra-techreport.pdf](/assets/docs/signals-spectra-techreport.pdf)

---

## Concept

Automated signal census system that transforms raw radio spectrum data into classified, searchable signal inventories. Combines SDR acquisition, ML classification, and vector search to detect, identify, and catalog signals across monitored bands.

---

## Visuals

### Waterfall & TUI Interface

![Spectra Waterfall](/images/spectra-waterfall-screenshot.png)

### RF Fingerprinting Results

![RF Fingerprinting](/images/rf_fingerprinting_results.png)

### Vector Search (Top-K Matches)

![Vector Search](/images/search_topk_example.png)

---

## Architecture

The Python backend owns all SDR connections and runs as a central server. IQ data is processed into spectrum bins, signal detections, classifications, and demodulated audio server-side — only compact results cross the wire to clients.

A multiplexed WebSocket protocol streams all data types (spectrum, detections, classifications, demod audio, control) to both the TUI and web interfaces. Users select a detected signal in either client, the backend classifies it, and results appear in real time.

---

## Features

- Automated signal detection and ML classification
- Vector database indexing for signal fingerprint search (top-K matching)
- Audio content intelligence for demodulated signals
- Rust TUI with waterfall display and signal browser
- Web dashboard consuming the same WebSocket protocol
- Distributed acquisition across multiple SDR receivers

---

[← Back to Signal Processing](../signal-processing)
