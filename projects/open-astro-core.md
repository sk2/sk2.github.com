---
layout: default
section: photography
---

# OpenAstro Core

<span class="status-badge status-active">v0.1 — Celestial Math & Native Drivers</span>

[← Back to Photography](../photography)

---

## The Insight

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives — keeping astronomical logic and hardware drivers in a single shared Rust library rather than duplicated across applications.

## Quick Facts

| | |
|---|---|
| **Status** | v0.1 — Celestial Math & Native Drivers |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem (OpenAstro Node, AuroraPhoto, Photo Tour). It provides coordinate transforms, time calculations, and native drivers for Sony cameras and Benro Polaris mounts.

## Workspace Crates

| Crate | Purpose |
|-------|---------|
| **astro-core** | Coordinate primitives (RA, Dec, angles), equatorial/horizontal transforms, Julian date and sidereal time |
| **astro-indi** | INDI protocol client for standardized telescope/camera control |
| **astro-alpaca** | ASCOM Alpaca REST client for modern hardware |
| **sony-sdk-rs** | Safe Rust bindings for Sony Camera Remote SDK with high-speed triggering and live-view streaming |
| **polaris-proto** | Native Benro Polaris protocol — framed codec with async client correlation, bypassing Alpaca bridge for low-latency mount control |

## Milestones

**Phase 1: Foundation** (Complete)
Coordinate primitives, HMS/DMS parsing, equatorial-horizontal transforms, Julian date and sidereal time.

**Phase 2: Native Drivers** (89% Complete)
Sony SDK safe wrapper with optional-link build, Polaris framed codec with transport abstraction and mocked tests.

**Roadmap:**

- **Phase 3: Advanced Logic** — FITS/RAW image parsing with auto-stretching, AI triggering module for Sentinel hardware classification

## Tech Stack

Rust, Tokio (feature-gated async), INDI protocol, ASCOM Alpaca, Sony Camera Remote SDK, CI-friendly no-hardware builds

---

[← Back to Photography](../photography)
