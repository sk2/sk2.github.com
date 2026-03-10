---
layout: default
section: signal-processing
---

# Wi-Fi Signal Reflection (KrakenSDR)

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span>
</div>

---

## Concept

Through-wall human detection and localization using existing Wi-Fi [signals](../signals) as illumination sources. Built on the KrakenSDR five-channel coherent receiver, processing Heimdall DAQ IQ streams to detect movement through obstacles in indoor environments. Bridges theoretical signal reflection research with a portable, real-time hardware implementation.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust, Python |

---

## Core Value

Signal reflection system that utilizes existing Wi-Fi [signals](../signals) for through-wall human detection and localization, leveraging the KrakenSDR coherent radio array.

---

## Vision

To bridge the gap between theoretical signal reflection research and a portable, real-time hardware implementation capable of "seeing" movement through obstacles using ubiquitous Wi-Fi [signals](../signals).

---

## Constraints

- Hardware: KrakenSDR (5-channel coherent receiver).
- Software: Python-based processing pipeline.
- Input: Heimdall DAQ IQ data streams.
- Environment: Indoor/Through-wall (high clutter).
