---
layout: default
---

# open-astro-core

<span class="status-badge status-planning">Planning</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Planning |
| **Language** | Rust, INDI, ASCOM Alpaca |
| **Started** | 2025 |

---

## The Insight

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

## What This Is

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

## Mission

- **Core Competence:** Rock-solid imaging, guiding, mount control.
- **Extensibility:** Inject custom logic ("Stop imaging if HFR degrades by 20%").
- **Intelligence:** Automated cloud handling, adaptive gain/exposure, real-time data quality analysis.
- **Hardware Agnostic:** Wide hardware support via INDI or ASCOM Alpaca.

## Design

- **Rust-centric:** Leveraging Rust's performance and safety features for core logic.
- **Modular:** Clear separation of concerns for easy extension and maintenance.
- **Protocol Implementations:** INDI (Instrument-Neutral Distributed Interface) and ASCOM Alpaca for broad hardware compatibility.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)