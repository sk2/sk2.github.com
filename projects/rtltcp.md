---
layout: default
section: signal-processing
---

# Radio Streaming Server

<span class="status-badge status-active">Recently Updated</span>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Why It Exists](#why-it-exists)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Concept

A single Rust binary that auto-detects every connected SDR, streams each over the standard `rtl_tcp` protocol, and provides a TUI dashboard and HTTP API for monitoring and control — designed for headless Raspberry Pi deployment.

A multi-SDR streaming server that replaces the separate C-based servers (`rtl_tcp`, `hfp_tcp`, `airspy_tcp`) with a single async Rust binary. It auto-detects all connected hardware, assigns each device its own TCP port, and streams raw IQ samples using the industry-standard `rtl_tcp` protocol. Any existing SDR client (GQRX, SDR#, CubicSDR) connects without modification.

![rtltcp-rust TUI](/images/rtltcp-server-tui.png)
*TUI dashboard showing 8 RTL-SDR devices and an AirSpy HF+ streaming on a Raspberry Pi.*

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

---

## Architecture

```
                    ┌─────────────────────────┐
                    │     rtltcp-rust          │
                    │                          │
   USB ─────────── │  Device Manager          │
   RTL-SDR 0..N    │    ├─ RTL-SDR driver     │ ──── TCP :1234
   AirSpy HF+      │    ├─ AirSpy HF+ driver │ ──── TCP :1235
   AirSpy           │    └─ AirSpy driver     │ ──── TCP :1236
                    │                          │
                    │  HTTP API (:8080)        │ ──── REST endpoints
                    │  TUI Dashboard           │ ──── SSH terminal
                    │  Config (TOML)           │
                    └─────────────────────────┘
```

Each device runs in its own tokio task with dedicated USB I/O and TCP streaming threads. The TUI and HTTP API share device state through `Arc<Mutex<>>` with 1 Hz status broadcasts.

---

## Tech Stack

- **Language**: Rust (2021 edition)
- **Async Runtime**: tokio
- **HTTP API**: axum
- **TUI**: ratatui + crossterm
- **Hardware FFI**: rtlsdr_sys, libairspyhf, libairspy
- **Cross-compilation**: `cross` + custom Docker images
- **Config**: TOML with serde

---

## Quick Facts

| | |
|---|---|
| **Status** |  () |
| **Language** | N/A |

---

## Why It Exists

Existing C-based implementations (like `rtl_tcp` and `hfp_tcp`) are often single-threaded, difficult to manage when running multiple devices, and lack modern observability/control features. This project aims to:
- Leverage Rust for safety and high-performance concurrency.
- Simplify multi-SDR management through a single binary.
- Provide a responsive TUI for real-time adjustments (frequency, gain, etc.).
- Enable future network optimizations (compression, error correction).

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
- [ ] Cross-compilation pipeline for Raspberry Pi (ARM).

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
