---
layout: default
section: photography
---

# OpenAstro Node

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Milestones](#milestones)

## Concept

A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.

---

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

---

## Tech Stack

Rust (Axum, Tokio, SQLite), React (TypeScript, Tailwind CSS), INDI, PHD2, ASTAP plate-solving

---

## Key Features

- **INDI Hardware Abstraction**: Unified camera and mount control with discovery and failover
- **Reactive Safety ("Goodnight Protocol")**: Monitors star quality (HFR), battery levels, and weather — parks, warms, and closes if conditions degrade
- **Dual Interface**: React web UI with night vision mode (strict true-red) and Rust TUI for SSH control
- **Real-Time State**: WebSocket snapshots at ~1Hz with immediate events, UI prefs persistence
- **Precision Tracking**: PHD2 guiding integration, meridian flip, plate-solving via ASTAP

---

## Milestones

**/8 plans)
INDI integration, camera/mount hardware abstraction, target management, background storage.

**/9 plans)
Web UI with night vision mode, TUI for SSH, real-time state transport, targets CRUD.

-  — Guided calibration wizard (darks/flats), Goodnight Protocol safety shutdown
-  — Advanced sequencing (wait for altitude, loop until time), multi-rig sync between nodes

---

[← Back to Projects](../projects)
