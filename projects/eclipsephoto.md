---
layout: default
section: photography
---

# EclipsePhoto

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Photography](../photography)

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

[← Back to Photography](../photography)
