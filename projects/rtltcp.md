---
layout: default
section: signal-processing
---

# SDR Streaming Server

<span class="status-badge status-active">Active</span>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Concept

A single Rust binary that auto-detects every connected SDR, streams each over the standard `rtl_tcp` protocol, and provides a TUI dashboard and HTTP API for monitoring and control — designed for headless Raspberry Pi deployment.

A multi-SDR streaming server that replaces the separate C-based servers (`rtl_tcp`, `hfp_tcp`, `airspy_tcp`) with a single async Rust binary. It auto-detects all connected hardware, assigns each device its own TCP port, and streams raw IQ samples using the industry-standard `rtl_tcp` protocol. Any existing SDR client (GQRX, SDR#, CubicSDR) connects without modification.

![rtltcp-rust TUI](/images/rtltcp-server-tui.png)
*TUI dashboard showing 8 RTL-SDR devices and an AirSpy HF+ streaming on a Raspberry Pi.*

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

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
