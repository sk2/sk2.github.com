---
layout: default
section: photography
---

# OpenAstro Core

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Photography](../photography)

[← Back to Projects](../projects)

---

## Concept

Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. Keeps coordinate math, imaging intelligence, and device behavior consistent across downstream applications (OpenAstro Node, Photo Tour). Pure Rust stack — no C toolchain required, testable without hardware.

8,030 lines of Rust across 7 crates. 163+ unit tests.

---

## Crates

- **astro-core**: angle/RA/Dec primitives, coordinate transforms, celestial planning, visibility, session utilities
- **astro-vision**: FITS/RAW/SER I/O, image statistics, background estimation, star detection, calibration, stacking, registration, exposure intelligence
- **astro-sentinel**: AI classification bridge, trigger rules engine, and pipeline API for Sentinel hardware
- **astro-indi**: INDI protocol client and device abstraction
- **astro-alpaca**: ASCOM Alpaca REST client for modern hardware
- **sony-sdk-rs**: Rust bindings for Sony Camera Remote SDK
- **polaris-proto**: native implementation of the Benro Polaris protocol

---

## Status

**Current**: v0.3 Advanced Astro — plate solving, co-axial calibration, mosaic planning, planetary imaging, focus/collimation analysis, pointing models.

**Shipped:**
- v0.2 — imaging intelligence engine: sky analysis, exposure recommendations, calibration, celestial planning (March 2026)
- v0.1 — celestial math foundation: coordinate transforms, time helpers, INDI/Alpaca clients, native drivers, sentinel triggering (February 2026)

---

[← Back to Photography](../photography)
