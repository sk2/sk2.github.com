---
layout: default
section: photography
---

# Photo Tour

<div class="badges-row">
  <span class="status-badge status-active">Active</span>

</div>

[← Back to Projects](../projects)

---

## Concept

Interactive photography assistant for field use on iOS and iPadOS. Provides live camera preview, manual motor control for landscape rigs, and a plugin architecture for composition overlays, exposure ramping, and intelligent triggering. Built with SwiftUI and designed around a real-time control loop — see what the camera sees and act on it fast enough to improve the shot.

Uses OpenAstro Core for astronomical calculations when planning celestial shots.

---

## Features

- Live camera preview with end-to-end frame display and disconnect recovery
- Touch-driven slewing and directional controls for motorized rigs
- Session state monitoring (connection status, frame timing, command history)
- Plugin architecture for future modules: composition overlays, Holy Grail exposure transitions, focus stacking, AI-assisted wildlife triggering

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## What This Is

Photo Tour is a smart, interactive photography assistant designed for field use.
It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.

---

## Core Value

In the field, you can see what the camera sees and get actionable guidance/control fast enough to improve the shot.

---

## Current Milestone: v0.1 Interactive Foundation

**Goal:** Stand up a real iOS/iPadOS SwiftUI app with an end-to-end live preview and basic manual control loop.

**Target features:**
- SwiftUI app scaffold with navigation and a "Camera/Live" screen.
- Live-view integration (initially minimal: connect, show frames, handle disconnect).
- Basic manual motor/control surface (touch-driven slewing or directional controls) for the landscape rig.
- A thin abstraction layer so later modules (composition overlays, Holy Grail, sentinel) can plug in.

---

## Requirements

---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] Live preview works end-to-end on device (connect, display, recover from disconnect)
- [ ] Manual control works end-to-end (send a control command and observe motion/state)
- [ ] Basic session state is visible (connected/disconnected, last frame time, last command)

---

## # Out of Scope

- Full 8-point composition overlay suite — defer until the live-preview pipeline is stable
- Holy Grail exposure ramping — defer until camera control/telemetry is in place
- Wildlife/AI sentinel — defer until base app + integration seams exist

---

## Context

- Long-term feature set includes classical composition overlays, Holy Grail transitions, focus stacking, and AI-assisted triggering.
- Hardware ecosystem notes are captured in `.planning/INVENTORY.md`.

---

## Constraints

- **Platform**: iOS/iPadOS (SwiftUI) — primary target for field use
- **Brownfield reality**: Repo currently contains planning docs only; app code scaffold will be created during milestone execution

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Native iOS/iPadOS SwiftUI app | Best field UX and Apple ecosystem integration | — Pending |
| Start with Interactive Foundation (v0.1) | Enables all later modules to plug into a real live/control loop | — Pending |

*Last updated: 2026-02-10 after milestone v0.1 kickoff*

---

[← Back to Projects](../projects)
