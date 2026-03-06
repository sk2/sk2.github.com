---
layout: default
section: projects
---

# EclipsePhoto

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Projects](../projects)

---

## Concept

Autonomous solar eclipse photography controller for Raspberry Pi. Coordinates a camera (via gphoto2) and equatorial mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from first contact (C1) to fourth contact (C4) without manual intervention. The system handles solar guiding, exposure ramping, and error recovery so the photographer can watch the eclipse while the hardware secures the data.

---

## Features

- **Holy Grail exposure ramping**: PI controller combining histogram analysis and TSL2591 light sensor data (600M:1 dynamic range) for smooth transitions through totality
- **Crescent-aware guiding**: OpenCV-based tracking (Hough circles and centroiding) to keep the sun centered throughout partial phases
- **INDI mount control**: native integration with AM5 and Polaris mounts
- **Mission Control**: mobile interface (FastAPI/BLE) for telemetry monitoring — guiding accuracy, exposure curves, sensor health
- **Resilience**: USB watchdog, auto-resume on power failure, best-effort background image backup

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Python |

---

## What This Is

A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.

---

## Core Value

Reliability and autonomy for a "one-shot" astronomical event. The system handles guiding, exposure ramping (Holy Grail), and error recovery (watchdogs) so the photographer can experience the eclipse while the system secures the data.

---

## Key Features

- **Holy Grail Exposure Ramping:** PI controller combining histogram analysis and TSL2591 light sensor data.
- **Crescent-Aware Guiding:** OpenCV-based tracking (Hough circles/centroiding) to keep the sun centered.
- **INDI Integration:** Native control for AM5 and Polaris mounts.
- **Mission Control Interface:** Mobile app (FastAPI/BLE) for telemetry (guiding accuracy, exposure curves, sensor health) rather than live-streaming.
- **Resilience:** USB watchdog, auto-resume on power failure, and "best-effort" background data backup.

---

## Requirements

---

## # Validated

- ✓ Core project structure and module separation — existing
- ✓ Basic PI controller logic for exposure ramping — existing
- ✓ Mock hardware wrappers for Camera and Mount — existing

---

## # Active

- [ ] **MOUNT-01:** Full INDI integration for AM5/Polaris mounts.
- [ ] **RAMP-01:** Sensor fusion for ramping (Histogram + TSL2591).
- [ ] **GUIDE-01:** Crescent-aware solar guiding logic.
- [ ] **SAFE-01:** Auto-resume on boot-up and USB watchdog recovery.
- [ ] **CONN-01:** FastAPI Mission Control API and BLE control channel.
- [ ] **DATA-01:** Best-effort background image backup from camera to Pi.

---

## # Out of Scope

- **Live Video Streaming:** High-bandwidth streaming is deprioritized over control stability and data integrity.
- **Custom Stepper Control:** Using INDI-compatible mounts only; no raw GPIO stepper logic.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| INDI Protocol | Standard, robust interface for high-end mounts like AM5/Polaris. | — Pending |
| TSL2591 Sensor | Extreme dynamic range (600M:1) necessary for eclipse transitions. | — Pending |
| PI Controller | PID derivative component causes too much flicker; PI is smoother for exposure. | — Pending |
| SD Card Primary | To avoid USB bottleneck issues seen in previous projects. | — Pending |
| Auto-Resume | Critical for power failure recovery during a timed event. | — Pending |

*Last updated: 2026-02-13 after initialization*

---

[← Back to Projects](../projects)
