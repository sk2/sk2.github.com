---
layout: default
---

# AuroraPhoto

<span class="status-badge status-planning">Planning</span>

[← Back to Projects](../projects)

---


## The Concept

Aurora photography requires split-second decisions during unpredictable "bursts" while maintaining perfect star focus in freezing conditions. **AuroraPhoto** provides automated control and intelligent capture sequencing through Raspberry Pi nodes controlling Sony cameras, managed via an iPhone companion app.

## Quick Facts

| | |
|---|---|
| **Status** | Planning |
| **Platform** | Raspberry Pi + iOS |
| **Started** | 2026 |

---

## What This Is

An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.

## Core Value

Provides precise, automated control over exposure and focus specifically optimized for aurora "bursts" and star sharpness, while offering field-ready composition tools.

## Success Criteria

- **Precise Focus**: Automated "Star Sharpness" (HFR) monitoring and remote focus adjustment via USB
- **Exposure Quality**: Capture sequences that preserve aurora beam definition without overblowing or underexposing
- **Reliable Field Connection**: Robust communication between iOS and multiple Pi nodes via Wi-Fi/Hotspot
- **Composition Assistance**: Functional iPhone overlay with compass and ML-assisted framing

## Key Features

### Camera Control
- **USB Communication**: Reliable control of Sony a7R V/a7 IV (ISO, Shutter, Focus) via USB-C
- **Star Sharpness**: HFR (Half-Flux Radius) algorithm for measuring and maintaining pin-sharp star focus
- **Capture Sequencing**: Optimized exposure sequences during aurora bursts

### Field Operation
- **Multi-Node Support**: Manage multiple Raspberry Pi controllers from single interface
- **Mobile Interface**: iOS app with live preview, composition overlay, and compass
- **External Integration**: Hook into separate alerting system for aurora "burst" triggers

## Architecture

```
┌─────────────────────────────────────────┐
│          iPhone Companion App            │
│    (Composition · Control · Preview)     │
└────────────┬────────────────────────────┘
             │ Wi-Fi/Hotspot
    ┌────────┼────────┬────────┐
    │        │        │        │
┌───▼──┐ ┌──▼───┐ ┌──▼───┐ ┌──▼───┐
│ Pi 1 │ │ Pi 2 │ │ Pi 3 │ │ Pi 4 │
│Node  │ │Node  │ │Node  │ │Node  │
└───┬──┘ └──┬───┘ └──┬───┘ └──┬───┘
    │       │        │        │
    │ USB-C │ USB-C  │ USB-C  │ USB-C
    │       │        │        │
┌───▼──┐ ┌──▼───┐ ┌──▼───┐ ┌──▼───┐
│Sony  │ │Sony  │ │Sony  │ │Sony  │
│a7R V │ │a7 IV │ │a7R V │ │a7 IV │
└──────┘ └──────┘ └──────┘ └──────┘
```

## Use Case: Aurora Burst

1. **Alert**: External monitoring system detects aurora activity spike
2. **Trigger**: AuroraPhoto receives burst notification
3. **Focus**: Automated HFR check ensures stars are pin-sharp
4. **Capture**: Execute optimized exposure sequence across all nodes
5. **Review**: Live preview on iPhone shows capture quality

## Tech Stack

- **Hardware**: Raspberry Pi 4/5, Sony a7R V/a7 IV
- **Connection**: USB-C for camera control, Wi-Fi for iOS communication
- **iOS App**: SwiftUI
- **Pi Software**: Python or Rust for camera control
- **Focus Algorithm**: HFR (Half-Flux Radius) for star sharpness measurement

## Out of Scope

- **Holy Grail Ramping**: Complex day-to-night exposure ramping (handled by existing separate apps)
- **Primary Alerting System**: Aurora activity discovery (handled by separate existing service)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
