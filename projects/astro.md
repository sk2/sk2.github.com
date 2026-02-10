---
layout: default
---

# OpenAstroNode

<span class="status-badge status-planning">Phase 1 Complete</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1 Foundation complete |
| **Language** | Rust + React (Web UI) |
| **Hardware** | Raspberry Pi + INDI-compatible devices |
| **Phase Completion** | 8/8 plans complete (100%) |
| **Started** | 2025 |
| **License** | TBD |

---

## Overview

OpenAstroNode is an open-source astrophotography control system for Linux single-board computers. Alternative to proprietary systems like ZWO ASIAir. Provides rock-solid imaging, guiding, and mount control with extensibility for custom logic and intelligent automation.

## Problem It Solves

Astrophotographers need reliable control systems for telescope setups. Current options have limitations:

**Proprietary Appliances (ZWO ASIAir):**
- Closed ecosystem restricts hardware choices
- Limited feature innovation
- Vendor lock-in

**Windows PC Software (NINA, SGP):**
- Requires full PC at telescope
- Higher power consumption and maintenance
- Overkill for headless operation

**Existing Open Source:**
- Fragmented tool ecosystem
- Complex setup and configuration
- No intelligent automation features

**OpenAstroNode provides:**
- Hardware-agnostic control via INDI/ASCOM Alpaca
- Headless operation on low-power ARM devices
- Extensible platform for custom automation
- Intelligent features (cloud handling, adaptive exposure, data quality analysis)

## Architecture

### Backend: Rust

High-performance Axum-based server runs on Raspberry Pi:
- **astro-server**: HTTP API and WebSocket endpoints
- **astro-indi**: INDI protocol client and device discovery
- **astro-core**: Hardware abstractions and control logic

### Hardware Protocol: INDI

INDI (Instrument Neutral Distributed Interface) provides hardware abstraction:
- Standard protocol for astronomical devices
- Wide hardware support (cameras, mounts, focusers, filter wheels)
- Future support planned for ASCOM Alpaca

### Frontend Interfaces

**Web UI:** Modern React interface accessible from iPad/laptop/phone. No VNC required.

**TUI:** Rust-based terminal interface for local debugging and SSH control.

## Features

### Phase 1 Complete: Foundation

**Hardware Integration:**
- INDI device discovery and connectivity
- Configurable INDI server connection
- Camera control (exposure, gain, offset)
- Mount control (park, slew, target management)

**Architecture:**
- Rust workspace structure (server/indi/core)
- Axum HTTP API with WebSocket support
- Hardware abstraction layer
- Linux/ARM64 deployment with systemd

**Testing:**
- Mock hardware mode for development
- Integration tests for device control
- ARM64 smoke tests

### Planned Features

**Phase 2 - Control:**
- TUI and Web UI wiring to hardware API
- Real-time image preview
- Session management

**Phase 3 - Intelligence:**
- Automated cloud detection and handling
- Adaptive gain/exposure based on conditions
- HFR (Half-Flux Radius) monitoring for focus quality
- Dead frame prevention through real-time analysis

**Phase 4 - Sequences:**
- Target sequencing and scheduling
- Dithering between exposures
- Meridian flip handling

## Smart Features Vision

Unlike simple appliance controllers, OpenAstroNode aims to provide intelligence:

**Adaptive Imaging:**
- "Stop imaging if HFR degrades by 20%" (focus drift detection)
- Automatic gain adjustment based on sky conditions
- Exposure time optimization for target brightness

**Weather Response:**
- Cloud detection from image data
- Automatic park and shutdown on weather threats
- Resume operations when conditions improve

**Data Quality:**
- Real-time frame quality assessment
- Reject frames with excessive trailing or poor focus
- Prevent wasted imaging time on dead frames

## Use Cases

**Backyard Observatory:**
Run on Raspberry Pi attached to telescope. Control imaging sessions from iPad inside house.

**Remote Observatory:**
Headless operation with remote Web UI access. Low power consumption for solar-powered sites.

**Advanced Automation:**
Custom logic for specific workflows. Trigger actions based on conditions (weather, focus, star safety).

## Development Status

**Phase 1 Complete:** Hardware connectivity and control foundations (8/8 plans)

**Phase 2 In Progress:** User interface development

**Next Steps:**
- Plan Phase 2 (Control): TUI + Web UI wiring
- Real-time image preview
- Session workflow implementation

## Hardware Support

Supports any INDI-compatible device:
- **Cameras**: ZWO ASI, QHY, SBIG, Canon DSLR, Nikon DSLR
- **Mounts**: Celestron, Meade, Sky-Watcher, iOptron
- **Focusers**: Moonlite, Pegasus, ZWO EAF
- **Filter Wheels**: ZWO, SBIG, QHY
- **Guide Cameras**: Most webcams and astronomy cameras

Not limited to ZWO ecosystem. Use hardware from multiple vendors.

## Comparison

| Feature | OpenAstroNode | ZWO ASIAir | NINA (Windows) |
|---------|---------------|------------|----------------|
| Hardware Support | Any INDI device | ZWO focus | Any ASCOM/INDI |
| Platform | Linux SBC | Proprietary appliance | Windows PC |
| Power | Low (5-15W) | Low (10-20W) | High (50-200W) |
| Extensibility | Open platform | Closed | Plugin system |
| Intelligence | Adaptive automation | Basic sequences | Manual control |
| UI | Web + TUI | Mobile app | Windows desktop |
| Cost | Free + hardware | $$$ | Free + Windows |

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **INDI Protocol:** https://www.indilib.org/

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Web UI showing device control
- TUI terminal interface
- INDI device discovery output
- Camera control panel
- Mount control and slew
- Target list management
- Real-time image preview (Phase 2)
-->
