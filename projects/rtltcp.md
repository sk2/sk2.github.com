---
layout: default
---

# Project Context: rtltcp-rust

<span class="status-badge status-active">v1 — Core Streaming & Hardware</span>

[← Back to Projects](../projects)

---


## The Concept

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

## Quick Facts

| | |
|---|---|
| **Status** | v1 — Core Streaming & Hardware |
| **Language** | N/A |
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

- **Language**: Rust (2021 edition)
- **Async Runtime**: `tokio` for high-performance concurrency
- **Hardware Interface**: `libusb` via FFI wrapping of `librtlsdr` and `libairspyhf`
- **Networking**: TCP implementing the `rtl_tcp` protocol
- **UI**: Terminal User Interface via `ratatui`
- **Config**: TOML file-backed persistence
- **Target**: Raspberry Pi (cross-compiled with `cross` tool)

## Development Roadmap

### v1: Core Streaming & Hardware (Current Focus)

**Hardware Access:**
- Wrap `librtlsdr` for RTL-SDR device control
- Wrap `libairspyhf` for AirSpy HF+ device control
- Multi-threaded IQ sample acquisition with high-performance buffering

**Networking:**
- Implement `rtl_tcp` protocol (command parsing and binary IQ streaming)
- Support multiple concurrent streams (one per device)
- Basic connection management (heartbeats, clean disconnects)

**Interface & Config:**
- Basic TUI showing connected devices and active stream status
- Real-time frequency and gain adjustment via TUI
- Persistent configuration in `config.toml`

### v2: Optimization & Advanced Features (Planned)

**Bandwidth Reduction Strategies:**

The raw IQ stream from an RTL-SDR at 2.4 MSPS with 8-bit samples produces 4.8 MB/s (2.4M samples × 2 channels (I+Q) × 1 byte). Over a network, this translates to ~38 Mbps, which can saturate modest internet connections or Wi-Fi links. Several compression approaches can reduce this significantly with minimal CPU impact:

1. **Delta Encoding (Planned)**
   - **Concept**: Send the difference between consecutive samples instead of absolute values
   - **Rationale**: IQ samples change gradually in frequency domain; deltas are typically small
   - **Implementation**: `delta[n] = sample[n] - sample[n-1]`
   - **Benefit**: Deltas compress better (more zeros/small values) → 20-40% reduction with zstd
   - **CPU Impact**: Minimal (single subtract per sample)
   - **Trade-off**: Requires client-side reconstruction (accumulate deltas)

2. **Lossless Compression (Planned)**
   - **Algorithms under evaluation**:
     - **zstd** (level 1-3): Fast, good compression ratio, widely supported
     - **LZ4**: Fastest, moderate compression, lowest CPU overhead
     - **Brotli** (level 1-4): Better compression than LZ4, moderate speed
   - **Benchmark target**: Compress 4.8 MB/s stream with < 10% CPU on Raspberry Pi 4
   - **Expected reduction**: 30-50% for typical RF signals (varies by signal content)
   - **Per-frame compression**: Compress 16KB chunks for low latency

3. **Adaptive Bit Depth Reduction (Research)**
   - **Concept**: RTL-SDR provides 8-bit samples, but many signals have < 8 bits of dynamic range
   - **Approach**: Analyze signal statistics, reduce to 6-7 bits when SNR allows
   - **Benefit**: 25% bandwidth reduction when applicable
   - **Challenge**: Requires real-time SNR estimation, client-side bit expansion

4. **UDP Transport with FEC (Future)**
   - **Motivation**: TCP's retransmission overhead on lossy links (Wi-Fi, cellular)
   - **Approach**: UDP + Forward Error Correction (Raptor codes)
   - **Benefit**: Tolerate packet loss without retransmissions, lower latency
   - **Trade-off**: More complex client-side recovery logic

**Compression Performance Estimates:**

| Method | Bandwidth Reduction | CPU Overhead (RPi4) | Latency Impact |
|--------|---------------------|---------------------|----------------|
| None (baseline) | 0% (4.8 MB/s) | 0% | 0ms |
| LZ4 | 30-35% | 5-8% | < 1ms |
| zstd (level 1) | 35-45% | 8-12% | < 2ms |
| Delta + zstd | 40-50% | 10-15% | < 3ms |
| Bit depth reduction | 25% | 3-5% | 0ms |

**Current Focus:** v1 core streaming must be stable before adding compression. Compression will be opt-in (via config flag) to maintain protocol compatibility with standard `rtl_tcp` clients.

---

**Other v2 Features:**
- **Remote Management**: Tunnel client for Mac/desktop control over SSH
- **Multi-client support**: Broadcast same stream to multiple receivers
- **Automatic failover**: Switch between redundant SDRs on hardware failure

## Getting Started

### Building

```bash
# Project Context: rtltcp-rust
cargo build --release

# Project Context: rtltcp-rust
cross build --target armv7-unknown-linux-gnueabihf --release
```

### Prerequisites
- Rust toolchain
- `libusb-1.0-0-dev`
- `librtlsdr-dev` and `libairspyhf-dev`

## Use Cases

- **Remote monitoring stations**: Place SDRs near antennas, stream to compute server
- **Multi-channel reception**: Monitor multiple frequencies simultaneously
- **Headless operation**: Run on Raspberry Pi without display
- **Network distribution**: Share SDR hardware across multiple users/applications

---

[← Back to Projects](../projects)
