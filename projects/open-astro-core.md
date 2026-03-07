---
layout: default
section: projects
---

# OpenAstro Core

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Projects](../projects)

---

## Concept

Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. Keeps coordinate math, imaging intelligence, and device behavior consistent across downstream applications (OpenAstro Node, Photo Tour). Pure Rust stack — no C toolchain required, testable without hardware.

8,030 lines of Rust across 7 crates. 163+ unit tests.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust |

---

## What This Is

OpenAstro Core ("Core SDK") is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math, imaging intelligence, and device/protocol behavior consistent across downstream OpenAstro apps.

---

## Core Value

Downstream apps can rely on correct, consistent coordinate math, imaging intelligence, and device/protocol primitives.

---

## Architecture Boundary (Core SDK vs Node Runtime)

- **Core SDK (this repo):** pure libraries that compute/decide and are testable without hardware.
- **Node Runtime (`open-astro-node`):** the running system that orchestrates devices/workflows and calls into the Core SDK.

---

## Current State

**Shipped:** v0.2 Imaging Intelligence (2026-03-02)
**Next milestone:** v0.3 Advanced Astro 

8,030 lines of Rust across 7 crates. 163+ unit tests. Pure Rust stack (no C toolchain required).

---

## Milestones



---

## # v0.1 Celestial Math *(shipped 2026-02-11)*

Unified `astro-core` coordinate math foundation — angle/RA/Dec primitives, coordinate transforms, time helpers, INDI/Alpaca clients, native drivers, image processing basics, and sentinel triggering.

---

## # v0.2 Imaging Intelligence *(shipped 2026-03-02)*

Full imaging intelligence engine — sky analysis, exposure recommendations, calibration, celestial planning, and expanded file I/O.

---

## # v0.3 Advanced Astro *(planned — Phases 11-16)*

Plate solving consumption, co-axial calibration, mosaic planning, planetary imaging, focus/collimation analysis, and pointing models. The features that make this a professional-grade library.

---

## Components

- **astro-core**: Shared types (RA, Dec, Angles), coordinate transforms, celestial planning, visibility, and session utilities.
- **astro-vision**: Image processing — FITS/RAW/SER I/O, statistics, background estimation, star detection, calibration, stacking, registration, exposure intelligence, FITS writing.
- **astro-sentinel**: AI classification bridge, trigger rules engine, and pipeline API for Sentinel hardware.
- **astro-indi**: INDI protocol client and device abstraction.
- **astro-alpaca**: ASCOM Alpaca REST client for modern hardware support.
- **sony-sdk-rs**: Rust bindings for Sony Camera Remote SDK.
- **polaris-proto**: Native implementation of the Benro Polaris protocol.

---

## Goals

1. **Consistency**: Ensure both the Node and Photo Tour use identical math and driver logic.
2. **Performance**: Minimal overhead for high-speed triggering and imaging.
3. **Safety**: Robust error handling for hardware communication.

*Last updated: 2026-03-02 after v0.2 milestone*

---

[← Back to Projects](../projects)
