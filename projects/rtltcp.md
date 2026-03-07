---
layout: default
section: signal-processing
---

# Radio Streaming Server

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Current Status](#current-status)

## Concept

Cross-platform server (targeting Raspberry Pi) that manages multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the `rtl_tcp` protocol. A single binary replaces multiple C-based streaming tools, adding a TUI for live device management, TOML configuration, and safe concurrency across all connected radios.

Existing C implementations (`rtl_tcp`, `hfp_tcp`) are single-threaded and require separate processes per device. This server manages all SDRs through one binary with real-time frequency and gain adjustment from the terminal.

---

## Features

- RTL-SDR and AirSpy HF+ support via `librtlsdr`/`libairspyhf` FFI wrappers
- Multi-threaded architecture for concurrent SDR streams (Tokio async)
- Standard `rtl_tcp` network protocol — compatible with existing SDR clients
- TUI for live status, frequency/gain adjustment, and device management
- TOML-based persistent configuration
- Cross-[compilation](../compilation) pipeline for Raspberry Pi (ARM)

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust |

---

## What This Is

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

---

## Why It Exists

Existing C-based implementations (like `rtl_tcp` and `hfp_tcp`) are often single-threaded, difficult to manage when running multiple devices, and lack modern observability/control features. This project aims to:
- Leverage Rust for safety and high-performance concurrency.
- Simplify multi-SDR management through a single binary.
- Provide a responsive TUI for real-time adjustments (frequency, gain, etc.).
- Enable future network optimizations (compression, error correction).

---

## Core Value

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

---

## Tech Stack

- **Language:** Rust
- **Hardware Interface:** `libusb` (via FFI wrapping of `librtlsdr` and `libairspyhf`)
- **Networking:** TCP (implementing the `rtl_tcp` protocol)
- **UI:** Terminal User Interface (TUI) via `ratatui` or similar
- **Config:** TOML file-backed persistence
- **Target:** Raspberry Pi (cross-compiled from macOS/Linux)

---

## Requirements



---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] Support for RTL-SDR hardware via `librtlsdr` wrapping.
- [ ] Support for AirSpy HF+ hardware via `libairspyhf` wrapping.
- [ ] Implementation of the `rtl_tcp` network protocol.
- [ ] Multi-threaded architecture to handle multiple SDR streams concurrently.
- [ ] TUI for viewing status and updating configuration live.
- [ ] Persistent configuration stored in a TOML file.
- [ ] Cross-[compilation](../compilation) pipeline for Raspberry Pi (ARM).

---

## # Out of Scope

- **Pure Rust Drivers:** (Initial phase) Using C-library wrapping instead for faster time-to-market.
- **Advanced Network Coding:** (Initial phase) Delta compression and Raptor codes are deferred to later optimizations.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Wrapping C Libs | Faster implementation of hardware logic while focusing on the Rust networking/UI layer. | Pending |
| Monolithic Binary | Easier to manage and deploy initially via SSH. | Pending |
| TOML Config | Human-readable and easy to edit or programmatically update. | Pending |

*Last updated: 2026-02-12 after initialization*

---

## Current Status

2026-02-22 - Completed 05-04-PLAN.md

---
