---
layout: default
section: photography
description: "EclipsePhoto — an autonomous controller that captures a complete eclipse sequence from first to fourth contact: solar guiding, exposure ramping through totality, and unattended error recovery."
hand_written: true
---

# EclipsePhoto

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

---

## Concept

Autonomous capture of a complete solar eclipse, from first contact (C1) through totality to fourth contact (C4), without the photographer needing to look at the rig. A single controller drives the camera and an equatorial mount in lockstep, ramps exposure across the ~600 million-to-one dynamic range that an eclipse traverses, keeps the sun centred as a crescent through partial phases, and recovers cleanly when something unplugs or browns out.

The photographer's job during totality is to watch the sky. The controller's job is to make sure that decision doesn't cost the shots.

---

## Architecture

<div class="mermaid">
flowchart TD
    SENSE["TSL2591 Light Sensor<br/><small>~600M:1 dynamic range</small>"]
    HIST["Frame Histogram<br/><small>per-capture analysis</small>"]
    EXP["Holy-Grail Exposure Controller<br/><small>PI loop over light + histogram</small>"]
    CV["Crescent Tracker<br/><small>OpenCV Hough · centroiding</small>"]
    MOUNT["Equatorial Mount<br/><small>INDI drive</small>"]
    CAM["Camera<br/><small>gphoto2 control</small>"]
    SEQ["C1 → C2 → Totality → C3 → C4 Sequence"]
    UI["Mission Control<br/><small>telemetry · health · alerts</small>"]
    SENSE --> EXP
    HIST --> EXP
    EXP --> CAM
    CV --> MOUNT
    MOUNT --> SEQ
    CAM --> SEQ
    SEQ --> UI
</div>

The light sensor and the frame histogram are deliberately redundant: the sensor responds faster but the histogram is what's actually going on the card, so the controller leans on the sensor for prediction and the histogram for correction.

---

[← Back to Photography & Astrophotography](../photography)
