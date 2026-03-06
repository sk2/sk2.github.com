---
layout: default
section: signal-processing
---

# Radio Streaming Server

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Why It Exists](#why-it-exists)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-02-22 |

---

## Concept

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

---

## Why It Exists

Existing C-based implementations (like `rtl_tcp` and `hfp_tcp`) are often single-threaded, difficult to manage when running multiple devices, and lack modern observability/control features. This rewrite:
- Uses Rust for safe concurrency across multiple SDR devices.
- Manages all SDRs through a single binary.
- Provide a responsive TUI for real-time adjustments (frequency, gain, etc.).
- Enable future network optimizations (compression, error correction).

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

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
