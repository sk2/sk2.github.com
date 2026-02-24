---
layout: default
section: photography
---

# EclipsePhoto

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Concept

### What This Is

A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.

### Core Value

Reliability and autonomy for a "one-shot" astronomical event. The system handles guiding, exposure ramping (Holy Grail), and error recovery (watchdogs) so the photographer can experience the eclipse while the system secures the data.

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

[← Back to Projects](../projects)
