---
layout: default
section: signal-processing
---

# Multi-SDR Streaming Server

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

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
- Cross-compilation pipeline for Raspberry Pi (ARM)

---

[← Back to Signal Processing](../signal-processing)
