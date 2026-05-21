---
layout: default
section: photography
description: "AuroraPhoto — automated multi-camera capture for aurora and night-sky imagery, with HFR-based focus, burst-triggered exposure sequencing, and a single mobile-app control surface."
hand_written: true
---

# AuroraPhoto

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">Swift</span>
</div>

---

## Concept

Automated capture for aurora and other night-sky imagery. A small edge node sits behind each camera, drives it over USB, and maintains focus by watching the Half-Flux Radius of stars in test frames. When the aurora bursts — the moment most worth capturing — exposure sequencing fires automatically, so the photographer can watch the sky instead of the back of the camera.

The control surface is one phone app, regardless of how many camera nodes are running. Adding another rig is one more entry in a list, not another laptop in the field.

---

## Architecture

<div class="mermaid">
flowchart TD
    CAM["Mirrorless Camera<br/><small>USB tethered</small>"]
    NODE["Capture Node<br/><small>focus loop · exposure scheduler</small>"]
    HFR["HFR Star Sharpness<br/><small>focus drift detection</small>"]
    BURST["Aurora Burst Trigger<br/><small>activity-driven sequencing</small>"]
    COORD["Multi-Node Coordinator<br/><small>fan-out across rigs</small>"]
    APP["iOS Companion App<br/><small>live preview · framing · status</small>"]
    CAM --> NODE
    NODE --> HFR
    NODE --> BURST
    HFR --> NODE
    BURST --> NODE
    NODE --> COORD
    COORD --> APP
</div>

Focus and burst-detection are local to each node — the phone app is a control plane, not a data path, so the system keeps working if the phone walks out of range.

---

[← Back to Photography & Astrophotography](../photography)
