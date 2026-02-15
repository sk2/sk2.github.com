---
layout: default
section: photography
---

# OpenAstro Node

<span class="status-badge status-active">Phase 2/4 — Control & Safety</span>

[← Back to Photography](../photography)

---

## Concept

A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety — set up, start the sequence, and go to sleep with confidence.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 2/4 — Control & Safety |
| **Language** | Rust + React (TypeScript) |
| **Started** | 2026 |

---

## What This Is

An autonomous astrophotography controller that runs on Raspberry Pi or Jetson, managing cameras (via INDI/gphoto2) and mounts (ZWO AM5, Benro Polaris). It provides both a responsive web UI and a terminal TUI for remote control, with a "Goodnight Protocol" safety system that monitors star quality, battery, and weather to protect equipment.

## Key Features

- **INDI Hardware Abstraction**: Unified camera and mount control with discovery and failover
- **Reactive Safety ("Goodnight Protocol")**: Monitors star quality (HFR), battery levels, and weather — parks, warms, and closes if conditions degrade
- **Dual Interface**: React web UI with night vision mode (strict true-red) and Rust TUI for SSH control
- **Real-Time State**: WebSocket snapshots at ~1Hz with immediate events, UI prefs persistence
- **Precision Tracking**: PHD2 guiding integration, meridian flip, plate-solving via ASTAP

## Architecture

```
React Web UI / Rust TUI
    ↕ WebSocket + REST API
Rust Backend (Axum)
    ├── State & Sequencing Manager
    ├── Hardware Control (INDI)
    │   ├── Camera Imager
    │   ├── Mount Controller
    │   └── Guiding (PHD2)
    ├── Smart Logic Engine
    └── Database (SQLite)
```

## Milestones

**Phase 1: Foundation** (Complete — 8/8 plans)
INDI integration, camera/mount hardware abstraction, target management, background storage.

**Phase 2: Control & Safety** (Complete — 9/9 plans)
Web UI with night vision mode, TUI for SSH, real-time state transport, targets CRUD.

**Roadmap:**

- **Phase 3: Autonomous Imaging** — Guided calibration wizard (darks/flats), Goodnight Protocol safety shutdown
- **Phase 4: Precision** — Advanced sequencing (wait for altitude, loop until time), multi-rig sync between nodes

## Tech Stack

Rust (Axum, Tokio, SQLite), React (TypeScript, Tailwind CSS), INDI, PHD2, ASTAP plate-solving

---

[← Back to Photography](../photography)
