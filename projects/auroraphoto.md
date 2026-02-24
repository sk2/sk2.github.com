---
layout: default
section: photography
---

# AuroraPhoto

<span class="status-badge status-active">** Phase 1: Star Sharpness Foundation</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Quick Facts](#quick-facts)
- [What This Is](#what-this-is)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)

---

## Concept

Provides precise, automated control over exposure and focus specifically optimized for aurora "bursts" and star sharpness, while offering field-ready composition tools.

---

## Quick Facts

| | |
|---|---|
| **Status** | ** Phase 1: Star Sharpness Foundation |
| **Language** | N/A |

---

## What This Is

An automated aurora and night sky photography system using Raspberry Pi "nodes" connected via USB to Sony cameras (a7R V / a7 IV), controlled and assisted by an iPhone companion app. The system monitors star sharpness (HFR) in real-time, dynamically responds to aurora bursts by adjusting exposure, and coordinates multiple nodes for panoramic capture.

---

## Key Features

- **HFR Star Sharpness Monitor**: Half-Flux Radius analysis via SEP (Source Extractor) ensures pin-sharp stars with automated focus correction
- **Aurora Burst Logic**: ML-assisted aurora detection dynamically shortens shutter speed (2s-5s) during active bursts to preserve beam definition
- **Multi-Node Sync**: Coordinates multiple Pi capture nodes for simultaneous shots or panoramic views
- **iPhone Companion App**: Low-latency live preview, remote health monitoring, compass/AR overlay for framing
- **Thermal Protection**: Hardware temperature monitoring with performance management for extreme conditions

---

## Architecture

```
iPhone Controller (SwiftUI)
    ↕ Wi-Fi / Hotspot + MQTT
Raspberry Pi Capture Nodes
    ├── Sony Camera (USB) — RAW capture, focus motor
    ├── HFR Calculator (SEP) — Star quality monitoring
    ├── ML Aurora Detection — Burst response
    └── Telemetry Publisher (MQTT)
```

---

## Tech Stack

Python (SEP, OpenCV, Rawpy, FastAPI, MQTT), Sony Camera Remote SDK, Swift (SwiftUI), Raspberry Pi

---

---

[← Back to Photography](../photography)

---

---

[← Back to Projects](../projects)

---

---

[← Back to Projects](../projects)

---

[← Back to Projects](../projects)
