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

## Tech Stack

- **Language:** Rust
- **Hardware Interface:** `libusb` (via FFI wrapping of `librtlsdr` and `libairspyhf`)
- **Networking:** TCP (implementing the `rtl_tcp` protocol)
- **UI:** Terminal User Interface (TUI) via `ratatui` or similar
- **Config:** TOML file-backed persistence
- **Target:** Raspberry Pi (cross-compiled from macOS/Linux)

---

## Current Status

2026-02-22 - Completed 05-04-PLAN.md

---

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
