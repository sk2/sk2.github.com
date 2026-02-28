---
layout: default
section: projects
---

# OpenAstro Core

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Components](#components)
- [Current Milestone: v0.1 Celestial Math](#current-milestone-v01-celestial-math)
- [Goals](#goals)

## Concept

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

---

## Components

- **astro-core**: Shared types (RA, Dec, Angles) and utility functions.
- **astro-indi**: INDI protocol client and device abstraction.
- **astro-alpaca**: ASCOM Alpaca REST client for modern hardware support.
- **sony-sdk-rs (Planned)**: Rust bindings for Sony Camera Remote SDK.
- **polaris-proto (Planned)**: Native implementation of the Benro Polaris protocol.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current Milestone: v0.1 Celestial Math

**Goal:** Ship a unified `astro-core` coordinate math foundation (types + transforms + tests) that other crates can build on.

**Target features:**
- Robust angle/RA/Dec primitives with safe conversions and formatting
- Coordinate transforms (e.g. equatorial <-> horizontal) with time/location inputs
- Time helpers needed for transforms (Julian date / sidereal time as required)
- Test coverage for correctness and edge cases

---

## Goals

1. **Consistency**: Ensure both the Node and Photo Tour use identical math and driver logic.
2. **Performance**: Minimal overhead for high-speed triggering and imaging.
3. **Safety**: Robust error handling for hardware communication.

*Last updated: 2026-02-10 after starting milestone v0.1*

---

[← Back to Projects](../projects)
