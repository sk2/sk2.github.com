---
layout: default
---

# OpenAstro Core

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Concept

Astrophotography software often suffers from inconsistent coordinate math and brittle hardware drivers. **OpenAstro Core** provides a high-performance Rust library for astronomical logic and device primitives, ensuring mathematical and protocol consistency across the ecosystem.

## Quick Facts

| | |
|---|---|
| **Status** | v0.1 Celestial Math |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

## Core Value

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

## Current Milestone: v0.1 Celestial Math

**Goal:** Ship a unified `astro-core` coordinate math foundation (types + transforms + tests) that other crates can build on.

**Target features:**
- Robust angle/RA/Dec primitives with safe conversions and formatting
- Coordinate transforms (e.g. equatorial ↔ horizontal) with time/location inputs
- Time helpers needed for transforms (Julian date / sidereal time as required)
- Test coverage for correctness and edge cases

## Components

- **astro-core**: Shared types (RA, Dec, Angles) and utility functions
- **astro-indi**: INDI protocol client and device abstraction
- **astro-alpaca**: ASCOM Alpaca REST client for modern hardware support
- **sony-sdk-rs** (Planned): Rust bindings for Sony Camera Remote SDK
- **polaris-proto** (Planned): Native implementation of the Benro Polaris protocol

## Goals

1. **Consistency**: Ensure both the Node and Photo Tour use identical math and driver logic
2. **Performance**: Minimal overhead for high-speed triggering and imaging
3. **Safety**: Robust error handling for hardware communication

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
