---
layout: default
section: signal-processing
---

# Multi-SDR Streaming Server

<span class="status-badge status-active">Phase 3/4 — TUI & Live Config (90%)</span>

[← Back to Signal Processing](../signal-processing)

---

## Concept

A single Rust binary that auto-detects every connected SDR, streams each over the standard `rtl_tcp` protocol, and provides a TUI dashboard and HTTP API for monitoring and control — designed for headless Raspberry Pi deployment.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 3/4 — TUI & Live Config (90%) |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A multi-SDR streaming server that replaces the separate C-based servers (`rtl_tcp`, `hfp_tcp`, `airspy_tcp`) with a single async Rust binary. It auto-detects all connected hardware, assigns each device its own TCP port, and streams raw IQ samples using the industry-standard `rtl_tcp` protocol. Any existing SDR client (GQRX, SDR#, CubicSDR) connects without modification.

![rtltcp-rust TUI](/images/rtltcp-server-tui.png)
*TUI dashboard showing 8 RTL-SDR devices and an AirSpy HF+ streaming on a Raspberry Pi.*

## Why a Unified Server

Existing C-based implementations have three problems:

- **One process per device**: Running 8 RTL-SDR dongles means managing 8 separate processes, each with its own PID, config, and failure mode.
- **No observability**: No way to see aggregate bandwidth, client connections, or device health without external tooling.
- **No live reconfiguration**: Changing frequency or gain requires restarting the stream, disconnecting all clients.

This server manages all devices from a single process with shared state, a TUI for live adjustment over SSH, and an HTTP API for programmatic monitoring.

## Supported Hardware

| Device | Default Sample Rate | Bits | Port Assignment |
|--------|-------------------|------|-----------------|
| RTL-SDR | 2.048 MHz | 8-bit | 1234, 1235, ... |
| AirSpy HF+ | 768 kHz | 18-bit (native) | continues after RTL-SDR |
| AirSpy | 6 MHz | 12-bit (native) | continues after AirSpy HF+ |

All three device types are auto-detected on startup. AirSpy HF+ and AirSpy support are compile-time features enabled by default.

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

## TUI Dashboard

The TUI provides real-time monitoring and live control over SSH:

- **System stats**: CPU, memory, temperature, uptime
- **Device list**: Frequency, gain, sample rate, bandwidth, client count per device
- **Interactive controls**: Change frequency (`f`), gain (`g`), sample rate (`s`), toggle devices (`t`)
- **Log viewer**: Tabbed view with scrollable log output
- **Status feedback**: Color-coded confirmation of commands

## HTTP API

REST API starts on port 8080 by default:

```bash
curl http://localhost:8080/api/v1/devices
```

```json
{
  "devices": [
    {
      "name": "rtlsdr-0",
      "device_type": "rtlsdr",
      "frequency_hz": 100000000,
      "sample_rate_hz": 2048000,
      "clients_connected": 1,
      "running": true,
      "bandwidth_mbps": 3.84
    }
  ]
}
```

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/health` | Liveness check |
| GET | `/api/v1/server` | Version, uptime, device count |
| GET | `/api/v1/devices` | All devices with status |
| GET | `/api/v1/devices/:name` | Single device by name |

## Raspberry Pi Deployment

Docker-based cross-compilation for all Pi models:

```bash
# Build cross-compilation Docker images
./docker/build-images.sh aarch64

# Cross-compile
cross build --release

# Deploy (checks deps, installs missing libs, offers to run)
STRIP=1 ./deploy-to-pi.sh pi@raspberrypi.local
```

| Target | Pi Model |
|--------|----------|
| `aarch64-unknown-linux-gnu` | Pi 3/4/5 (64-bit) |
| `armv7-unknown-linux-gnueabihf` | Pi 2/3 (32-bit) |
| `arm-unknown-linux-gnueabihf` | Pi Zero/1 |

## Development Roadmap

### Phase 1: Hardware Foundation (Complete)
FFI wrappers for `librtlsdr`, basic TCP streaming, `rtl_tcp` protocol compliance. Verified with GQRX and SDR#.

### Phase 2: Multi-SDR & AirSpy (Complete)
`libairspyhf` and `libairspy` FFI wrappers, multi-device architecture with per-device ports, graceful shutdown with signal handling.

### Phase 3: TUI & Live Config (90%)
Ratatui-based dashboard, interactive frequency/gain/sample rate adjustment, channel-based command dispatch, HTTP REST API. Remaining: config save/reload.

### Phase 4: Network Optimization (Planned)
Compression (LZ4/zstd), UDP transport with Forward Error Correction, "Mac Tunnel" client for remote desktop control.

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
