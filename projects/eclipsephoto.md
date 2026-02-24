---
layout: default
section: photography
---

# EclipsePhoto

<span class="status-badge status-active">** 1 - Hardware & Data Foundation</span>

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

Reliability and autonomy for a "one-shot" astronomical event. The system handles guiding, exposure ramping (Holy Grail), and error recovery (watchdogs) so the photographer can experience the eclipse while the system secures the data.

---

## Quick Facts

| | |
|---|---|
| **Status** | ** 1 - Hardware & Data Foundation |
| **Language** | N/A |

---

## What This Is

A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 (First Contact) to C4 (Fourth Contact) without manual intervention.

---

## Key Features

- **Holy Grail Exposure Ramping**: PI controller combining histogram analysis and TSL2591 light sensor data for smooth exposure transitions through the eclipse phases
- **Crescent-Aware Guiding**: OpenCV-based solar disk tracking (Hough circles/centroiding) to keep the sun centered throughout the event
- **INDI Mount Control**: Native integration for ZWO AM5 and Benro Polaris mounts
- **Mission Control**: Mobile app (FastAPI/BLE) for telemetry monitoring — no live-streaming, just status
- **Resilience**: USB watchdog, auto-resume on power failure, best-effort background data backup

---

## Architecture

```
Raspberry Pi
  ├── Sequencer (Asyncio) — Eclipse state machine, exposure loops
  ├── Guiding Engine (Multiprocessing) — Star/crescent detection, PID loop
  ├── Camera HAL — gphoto2 with failover support
  ├── Mount HAL — INDI protocol
  └── Mission Control API (FastAPI/BLE)
```

---

## Tech Stack

Python (asyncio, multiprocessing), OpenCV, INDI, gphoto2, TSL2591 light sensor, FastAPI, ZeroMQ

---

---

[← Back to Photography](../photography)

---

---

[← Back to Projects](../projects)

---

[← Back to Projects](../projects)
