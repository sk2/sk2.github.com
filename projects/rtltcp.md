---
layout: default
---

# Project Context: rtltcp-rust

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Insight

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

## Quick Facts

| | |
|---|---|
| **Status** | Active Development |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

## Why It Exists

Existing C-based implementations (`rtl_tcp`, `hfp_tcp`) are single-threaded, difficult to manage when running multiple devices, and lack modern observability features. This project provides:

- **High-performance concurrency** through Rust's async runtime
- **Multi-SDR management** via a single binary
- **Responsive TUI** for real-time frequency, gain, and sample rate adjustments
- **Network optimizations** including future support for compression and error correction

## Key Features

### Supported Hardware
- **RTL-SDR**: RTL2832U-based USB dongles (via `librtlsdr`)
- **AirSpy HF+**: High-performance HF/VHF SDR (via `libairspyhf`)

### Multi-threaded Architecture
- Concurrent streaming from multiple SDRs
- Separate threads for USB I/O, network transmission, and UI
- Efficient buffer management to prevent sample drops

### Terminal User Interface
- Live device status monitoring (frequency, gain, sample rate)
- Real-time configuration adjustments without restart
- Multi-device management in a single view
- Connection status and bandwidth monitoring

### Network Protocol
- Industry-standard `rtl_tcp` protocol compatibility
- Works with existing SDR clients (GQRX, SDR#, SDR++)
- TCP-based streaming with future compression support

### Configuration Management
- TOML-based persistent configuration
- Per-device settings (frequency, gain, PPM correction)
- Network settings (ports, buffer sizes)
- Easy editing and version control friendly

## Tech Stack

- **Language**: Rust
- **Hardware Interface**: `libusb` via FFI wrapping of `librtlsdr` and `libairspyhf`
- **Networking**: TCP implementing the `rtl_tcp` protocol
- **UI**: Terminal User Interface via `ratatui`
- **Config**: TOML file-backed persistence
- **Target**: Raspberry Pi (cross-compiled from macOS/Linux)

## Use Cases

- **Remote monitoring stations**: Place SDRs near antennas, stream to compute server
- **Multi-channel reception**: Monitor multiple frequencies simultaneously
- **Headless operation**: Run on Raspberry Pi without display
- **Network distribution**: Share SDR hardware across multiple users/applications

---

[← Back to Projects](../projects)
