---
layout: default
section: photography
---

# AuroraPhoto

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)

## Concept

An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.

Provides precise, automated control over exposure and focus specifically optimized for aurora "bursts" and star sharpness, while offering field-ready composition tools.

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

## Key Features

- **HFR Star Sharpness Monitor**: Half-Flux Radius analysis via SEP (Source Extractor) ensures pin-sharp stars with automated focus correction
- **Aurora Burst Logic**: ML-assisted aurora detection dynamically shortens shutter speed (2s-5s) during active bursts to preserve beam definition
- **Multi-Node Sync**: Coordinates multiple Pi capture nodes for simultaneous shots or panoramic views
- **iPhone Companion App**: Low-latency live preview, remote health monitoring, compass/AR overlay for framing
- **Thermal Protection**: Hardware temperature monitoring with performance management for extreme conditions

---

[← Back to Projects](../projects)
