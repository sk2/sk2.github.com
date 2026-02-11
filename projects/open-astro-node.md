---
layout: default
---

# open-astro-node

<span class="status-badge status-active">Phase 1 Complete</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1 Complete |
| **Language** | Rust, React, INDI/Alpaca |
| **Started** | 2025 |

---

## Mission

- **Core competence:** Rock-solid imaging, guiding, mount control.
- **Extensibility:** Inject custom logic ("Stop imaging if HFR degrades by 20%").
- **Intelligence:** Automated cloud handling, adaptive gain/exposure, real-time data quality analysis.
- **Hardware agnostic:** Wide hardware support via INDI or ASCOM Alpaca.

## Design

- **Headless:** Runs as system service on telescope computer.
- **Remote interface:** Modern web UI (iPad/laptop/phone browser), no VNC required.
- **Terminal TUI:** Robust local debugging and power-user control via SSH.
- **Reactive:** Real-time push of images and status to client.

## Why Build This

Proprietary systems restrict hardware choices and feature innovation. Full Windows PCs (NINA) require more power/maintenance than headless embedded binaries. Advanced users need specific triggers (weather, star safety, custom sequences) that simple appliances don't offer.

## Overview

A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)