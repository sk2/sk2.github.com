---
layout: default
section: photography
description: "OpenAstro Core — a pure-Rust library of shared astronomical logic, hardware drivers, and protocol implementations that the rest of the OpenAstro ecosystem builds on."
hand_written: true
---

# OpenAstro Core

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Concept

The shared backbone for the OpenAstro tools: coordinate math, plate-solving glue, device drivers (INDI, ASCOM Alpaca), and the protocol surfaces every downstream app needs. The aim is that the imaging-intelligence and the device-control behaviour stay consistent across OpenAstro Node, Photo Tour, and anything else that lands on top — one library, not five reimplementations.

Pure Rust through the stack. No C toolchain to maintain, no shared mutable state across language boundaries, and the unit tests run against the abstractions instead of the hardware. The driver layer is the only part that needs a real device to validate.

---

## Architecture

<div class="mermaid">
flowchart TD
    COORD["Coordinate Math<br/><small>RA/Dec · alt/az · transforms</small>"]
    IMG["Imaging Intelligence<br/><small>HFR · plate-solve glue · sequencing primitives</small>"]
    DRV["Device Drivers<br/><small>INDI · ASCOM Alpaca</small>"]
    PROTO["Protocol Surfaces<br/><small>session · telemetry · safety</small>"]
    NODE["OpenAstro Node"]
    PT["Photo Tour"]
    EXT["Future tools"]
    COORD --> IMG
    DRV --> IMG
    IMG --> PROTO
    PROTO --> NODE
    PROTO --> PT
    PROTO --> EXT
</div>

About 8,000 lines of Rust across seven crates, with 160-plus unit tests that exercise the abstractions without requiring a mount or camera plugged in. Drivers sit behind trait boundaries so a downstream tool can mock the device cleanly when it needs to.

---

[← Back to Photography & Astrophotography](../photography)
