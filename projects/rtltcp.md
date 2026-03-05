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

A high-performance Rust binary that auto-detects connected SDR hardware (RTL-SDR, AirSpy HF+) and streams IQ samples over the network using the industry-standard `rtl_tcp` protocol. Designed for headless Raspberry Pi deployment, it replaces multiple separate C-based servers with a single async engine.

The system provides a TUI dashboard and HTTP API for real-time monitoring and control, automatically assigning each device its own TCP port. This allows existing SDR clients like GQRX or SDR# to connect without modification, enabling reliable, high-fidelity IQ streaming through a modern management interface.

![rtltcp-rust TUI](/images/rtltcp-server-tui.png)
*TUI dashboard showing 8 RTL-SDR devices and an AirSpy HF+ streaming on a Raspberry Pi.*

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

## Usage

**Start with Auto-Discovery:**
```bash
# Auto-detects all RTL-SDR and AirSpy devices
# Assigns ports starting at 1234
rtltcp-server --auto-discover
```

**Custom Port Mapping (TOML):**
```toml
# config.toml
[devices.rtl0]
serial = "00000001"
port = 1234
gain = 20.0

[devices.airspy]
type = "airspyhf"
serial = "74A064C832442F0B"
port = 1235
```

**Remote Connection:**
```bash
# Connect with GQRX or other clients
gqrx -c rtl_tcp=192.168.1.100:1234
```

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
