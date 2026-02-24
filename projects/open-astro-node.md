---
layout: default
section: photography
---

# OpenAstro Node

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Concept

### Overview

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

[← Back to Projects](../projects)
