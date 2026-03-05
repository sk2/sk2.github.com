---
layout: default
section: projects
---

# AuroraPhoto

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Contents

- [What This Is](#what-this-is)
- [Core Value](#core-value)
- [Success Criteria](#success-criteria)
- [Requirements](#requirements)
- [Key Decisions](#key-decisions)

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## What This Is

An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.

---

## Core Value

Provides precise, automated control over exposure and focus specifically optimized for aurora "bursts" and star sharpness, while offering field-ready composition tools.

---

## Success Criteria

- **Precise Focus:** Automated "Star Sharpness" (HFR) monitoring and remote focus adjustment via USB.
- **Exposure Quality:** Capture sequences that preserve aurora beam definition without overblowing or underexposing.
- **Reliable Field Connection:** Robust communication between iOS and multiple Pi nodes via Wi-Fi/Hotspot.
- **Composition Assistance:** Functional iPhone overlay with compass and ML-assisted framing.

---

## Requirements



---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] **USB Camera Control:** Reliable communication with Sony a7R V/a7 IV (ISO, Shutter, Focus).
- [ ] **Star Sharpness Logic:** Algorithm to detect and maintain pin-sharp star focus remotely.
- [ ] **Capture Sequencing:** Logic to trigger optimized sequences during aurora bursts.
- [ ] **Multi-Node Support:** Architecture for managing multiple PIs from a single interface.
- [ ] **Mobile Interface:** iOS app for live preview, composition overlay, and compass.
- [ ] **External Integration:** Hook into separate alerting system for "burst" triggers.

---

## # Out of Scope

- **Holy Grail Ramping:** Complex day-to-night ramping (handled by existing separate apps).
- **Primary Alerting System:** The discovery of aurora activity (handled by a separate existing service).

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| USB Connection | Sony a7R V/a7 IV provide robust control and charging over USB-C. | Pending |
| Wi-Fi Hotspot | Better range and reliability than BT for remote field setups. | Pending |
| HFR Focus Check | Industry standard for measuring star sharpness in astrophotography. | Pending |

*Last updated: 2026-02-13 after initialization*

---

[← Back to Projects](../projects)
