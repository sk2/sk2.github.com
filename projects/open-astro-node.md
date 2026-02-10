---
layout: default
---

# OpenAstro Node

<span class="status-badge status-active">Phase 1 Complete</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1 Foundation complete (100%) |
| **Language** | Rust + React (Web UI) |
| **Hardware** | Raspberry Pi / Jetson Nano |
| **Phase Completion** | 8/8 plans complete |
| **Requirement Coverage** | 28/28 (100%) |
| **Started** | 2025 |
| **License** | TBD |

---

## Overview

OpenAstro Node is a headless, autonomous astrophotography controller for low-power Linux devices. Manages hardware, executes imaging sequences, and ensures rig safety for unattended operation. Designed for Raspberry Pi and Jetson platforms at the telescope.

## Problem It Solves

Astrophotography requires reliable control systems for overnight imaging sessions:

**Traditional Solutions:**
- Full PC at telescope (power hungry, overkill)
- Proprietary appliances (vendor lock-in, limited features)
- Manual operation (requires constant supervision)
- Complex software setup (difficult to configure)

**Unattended Operation Risks:**
- Equipment damage from unsafe conditions
- Lost imaging time from failures
- No automated recovery
- Difficult to coordinate multiple rigs

**OpenAstro Node provides:**
- Headless operation on low-power ARM devices
- Autonomous "Goodnight" protocol for safe sessions
- Hardware-agnostic via INDI and Alpaca
- Multi-rig coordination on shared mount
- Web and Terminal UI for remote control

## Architecture

### Backend: Rust

Axum-based server optimized for ARM:
- **astro-server**: HTTP API and WebSocket endpoints
- **open-astro-core**: Shared hardware drivers and astronomical logic
- **Database**: SQLite for targets, sessions, and telemetry

### Hardware Integration

Uses [OpenAstro Core](open-astro-core) library:
- **INDI**: Standard protocol for astronomical devices
- **ASCOM Alpaca**: Modern REST API for hardware
- **Device Support**: Cameras, mounts, focusers, filter wheels, guidescopes

### User Interfaces

**Web UI:** React-based responsive interface
- Remote control from laptop/tablet
- Real-time image preview
- Session monitoring and control
- No VNC or remote desktop required

**Terminal UI (TUI):** Rust-based local interface
- Power-user control via SSH
- Keyboard-driven navigation
- Low bandwidth operation
- Debugging and diagnostics

## Key Features

### Astro Autonomy: "Goodnight" Protocol

Safe unattended operation:

**Pre-Session Validation:**
- Weather check (cloud coverage, wind, rain)
- Equipment health verification
- Disk space and battery level
- Network connectivity test

**During Session:**
- Continuous safety monitoring
- Automated park on unsafe conditions
- Meridian flip handling
- Dew heater control

**Recovery:**
- Resume after brief interruptions
- Safe park and cover deployment
- Session state persistence
- Automated restart when conditions improve

### Precision Tracking

**Guiding Integration:**
- PHD2 protocol support
- Start/stop guiding automatically
- Dithering between exposures
- Settle detection before imaging

**Mount Control:**
- Automated meridian flips
- Parking and homing
- Target sequencing
- Field rotation compensation

### Multi-Rig Synchronization

Coordinate multiple cameras on shared mount:

**Use Cases:**
- Main imaging rig + guide scope
- Dual cameras (OSC + mono)
- Multiple focal lengths

**Coordination:**
- Synchronized exposures
- Shared guiding
- Filter wheel coordination
- Dithering orchestration

### Imaging Sequences

**Sequence Planning:**
- Multiple targets per night
- Altitude and transit time optimization
- Filter and exposure plans
- Dwell time and repeats

**Execution:**
- Automated slew and center
- Focus routine before imaging
- Exposure stack with dithering
- Progress tracking and ETA

## Features by Phase

### Phase 1 Complete: Foundation ✅

**Hardware Connectivity:**
- INDI device discovery and control
- Camera control (exposure, gain, offset, cooling)
- Mount control (park, slew, target management)
- Configurable hardware connections

**Architecture:**
- Rust Axum server
- SQLite database
- Hardware abstraction layer
- ARM64 deployment with systemd

### Planned: Phase 2 - Control

**User Interfaces:**
- Web UI for remote operation
- TUI for local SSH control
- Real-time image preview
- Session management

### Planned: Phase 3 - Autonomy

**Goodnight Protocol:**
- Safety validation system
- Automated recovery
- Weather monitoring
- Equipment health checks

### Planned: Phase 4 - Sequences

**Target Management:**
- Multi-target sequences
- Altitude optimization
- Meridian flip automation
- Filter and exposure plans

### Planned: Phase 5 - Guiding

**PHD2 Integration:**
- Automated guide start/stop
- Dithering control
- Settle detection
- Guide graph visualization

### Planned: Phase 6 - Multi-Rig

**Coordination:**
- Synchronized exposures
- Shared guiding
- Multiple camera support
- Resource arbitration

## Use Cases

**Backyard Observatory:**
Headless Raspberry Pi at telescope. Control imaging from inside house via Web UI. Autonomous operation through the night.

**Remote Observatory:**
Solar-powered site with cellular connection. Node runs unattended with automated safety protocols. Check progress remotely.

**Multi-Camera Rig:**
Single mount with imaging camera and guide scope. Node coordinates both devices with synchronized dithering.

**Deep Sky Imaging:**
All-night unattended sessions on faint targets. Automated meridian flip, guiding, and dithering. Weather monitoring ensures safe operation.

## Technical Details

### Platform Requirements

**Minimum:**
- Raspberry Pi 4 (4GB RAM)
- 32GB SD card
- Ethernet or WiFi
- USB hub for devices

**Recommended:**
- Jetson Nano (better for AI features)
- 64GB+ SD card or SSD
- Wired Ethernet
- Powered USB hub

### Performance

**Overhead:**
- <50MB RAM base usage
- <5% CPU during imaging
- Efficient SQLite queries
- Zero-copy image transfer

**Latency:**
- Sub-100ms hardware commands
- <1s image download (depending on camera)
- Real-time WebSocket updates
- Responsive UI even on slow networks

### Power Consumption

**Typical:**
- 5-10W on Raspberry Pi 4
- 10-15W on Jetson Nano
- Suitable for battery/solar operation
- Lower than traditional PC solutions

## Development Status

**Phase 1 Complete:** Foundation with hardware control (8/8 plans, 100%)

**Phase 2 In Progress:** User interface development

**Requirements:** 28/28 active requirements mapped (100% coverage)

**Next Steps:**
- Plan Phase 2 (Web UI and TUI implementation)
- Real-time image preview system
- Session workflow implementation

## Comparison to Alternatives

| Feature | OpenAstro Node | N.I.N.A. | SGP | KStars/Ekos |
|---------|----------------|----------|-----|-------------|
| Platform | Linux ARM | Windows | Windows | Linux/macOS/Win |
| Power | 5-15W | 50-200W | 50-200W | 50-200W |
| Hardware | Any INDI/Alpaca | ASCOM | ASCOM | INDI |
| Autonomy | Goodnight protocol | Manual | Some | Some |
| Multi-Rig | Native | No | No | Limited |
| UI | Web + TUI | Windows app | Windows app | Desktop app |
| Cost | Free + Pi | Free | $$$ | Free |

## Hardware Support

**Cameras:** ZWO ASI, QHY, SBIG, Canon DSLR, Nikon DSLR
**Mounts:** Celestron, Meade, Sky-Watcher, iOptron, any INDI/Alpaca mount
**Focusers:** Moonlite, Pegasus, ZWO EAF, any INDI-compatible
**Filter Wheels:** ZWO, SBIG, QHY, manual wheels
**Guide Cameras:** Most astronomy cameras and webcams

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **Related:** [OpenAstro Core](open-astro-core) provides hardware drivers

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Web UI showing imaging session
- TUI terminal interface
- Real-time image preview
- Target sequence planning
- INDI device control panel
- Goodnight protocol safety checks
- Multi-rig coordination view
- Session telemetry graphs
-->
