---
layout: default
---

# OpenAstro Core

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Insight

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

## Core Value

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

## Components

- **astro-core**: Shared types (RA, Dec, Angles) and utility functions.
- **astro-indi**: INDI protocol client and device abstraction.
- **astro-alpaca**: ASCOM Alpaca REST client for modern hardware support.
- **sony-sdk-rs (Planned)**: Rust bindings for Sony Camera Remote SDK.
- **polaris-proto (Planned)**: Native implementation of the Benro Polaris protocol.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
