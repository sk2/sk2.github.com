---
layout: default
section: photography
---

# AuroraPhoto

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Concept

### What This Is

An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.

### Core Value

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

[← Back to Projects](../projects)
