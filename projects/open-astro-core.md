---
layout: default
---

# OpenAstro Core

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Quick Facts](#quick-facts)
- [What This Is](#what-this-is)
- [Components](#components)
- [Core Value](#core-value)

---

## Concept

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Language** | N/A |

---

## What This Is

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

---

## Components

- **astro-core**: Shared types (RA, Dec, Angles) and utility functions.
- **astro-indi**: INDI protocol client and device abstraction.
- **astro-alpaca**: ASCOM Alpaca REST client for modern hardware support.
- **sony-sdk-rs (Planned)**: Rust bindings for Sony Camera Remote SDK.
- **polaris-proto (Planned)**: Native implementation of the Benro Polaris protocol.

---

## Core Value

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

---

[← Back to Projects](../projects)
