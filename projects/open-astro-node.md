---
layout: default
section: photography
---

# OpenAstro Node

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">TypeScript</span>
</div>

[← Back to Projects](../projects)

---

## Concept

Headless, autonomous astrophotography controller for low-power Linux devices (Raspberry Pi, Jetson). Manages camera and mount hardware, executes imaging sequences, and ensures rig safety through a "Goodnight" protocol for unattended overnight sessions. Uses OpenAstro Core for coordinate math, imaging intelligence, and device drivers.

---

## Features

- **Autonomous sessions**: "Goodnight" protocol handles shutdown, meridian flips, and weather safety without intervention
- **Precision tracking**: PHD2 guiding integration with automated meridian flip management
- **Multi-rig coordination**: synchronizes multiple nodes sharing a mount
- **Hardware support**: full INDI and ASCOM Alpaca device control via `open-astro-core`
- **Web UI**: responsive React interface for remote control
- **Terminal UI**: local SSH-based power-user interface via `ratatui`

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust, TypeScript |

---

## Overview

A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.

---

## Key Features

- **Astro Autonomy**: The "Goodnight" protocol for safe, unattended sessions.
- **Precision Tracking**: Guiding integration (PHD2) and automated meridian flips.
- **Multi-Rig Sync**: Coordination between multiple nodes on a shared mount.
- **Hardware Integration**: Full INDI and Alpaca support via `open-astro-core`.

---

## User Interfaces

- **Web UI**: Responsive React interface for remote control.
- **Terminal UI (TUI)**: Local power-user control over SSH.

---

[← Back to Projects](../projects)
