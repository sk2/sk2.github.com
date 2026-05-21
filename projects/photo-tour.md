---
layout: default
section: photography
description: "Photo Tour — an iOS / iPadOS field assistant: live camera preview, manual motor control for landscape rigs, and a plugin surface for composition, exposure, and trigger logic."
hand_written: true
---

# Photo Tour

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Swift</span>
</div>

---

## Concept

A field-side assistant for photographers using motorised landscape rigs. The control surface is a live preview of what the camera sees, with touch slewing on top and a plugin layer underneath. Each plugin reads the same frame stream and acts on it: composition overlays, Holy-Grail exposure transitions, focus stacking, AI-assisted wildlife triggering — the plugin is what differs, the loop is not.

Astronomical calculations come from OpenAstro Core, so when the next shot is a celestial event the planning numbers don't need to be re-derived in the app.

---

## Architecture

<div class="mermaid">
flowchart TD
    CAM["Tethered Camera<br/><small>live frame stream</small>"]
    MOTOR["Motorised Rig<br/><small>slew · directional · velocity</small>"]
    LOOP["Real-Time Control Loop<br/><small>frame in · command out</small>"]
    UI["SwiftUI Interface<br/><small>preview · status · history</small>"]
    PLUG["Plugin Surface<br/><small>composition · exposure · stacking · triggers</small>"]
    OAC["OpenAstro Core<br/><small>celestial math when needed</small>"]
    CAM --> LOOP
    LOOP --> UI
    UI --> MOTOR
    LOOP --> PLUG
    PLUG --> UI
    OAC --> PLUG
</div>

The plugin layer is what makes the app worth carrying into the field: each plugin is small enough to be specific, but they all share the same frame loop and the same control surface, so the photographer doesn't switch apps when the shot type changes.

---

[← Back to Photography & Astrophotography](../photography)
