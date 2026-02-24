---
layout: default
section: signal-processing
---

# Radio Streaming Server

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Concept

### What This Is

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

### Core Value

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

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
