---
layout: default
section: signal-processing
---

# Spectrum Analysis

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Hardware](#hardware)
- [Tech Stack](#tech-stack)

## Concept

### Core Value

Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.

---

## Architecture

The system splits into edge and core nodes connected over Gigabit Ethernet:

```
┌─ EDGE (Raspberry Pi) ──────────────┐
│  SDR Hub (Airspy, RTL-SDR, HF+)    │
│  SpyServer · rtl_tcp · readsb      │
│  IQ streaming over LAN             │
└──────────────────┬──────────────────┘
                   │ Gigabit Ethernet
┌──────────────────▼──────────────────┐
│  CORE (Mac mini)                    │
│  Python Orchestrator (2,000+ lines) │
│  ML Classification Pipeline        │
│  Signal Census Database (DuckDB)   │
│  Web UI · Rust TUI · REST API      │
│  Autonomous Missions Engine        │
└─────────────────────────────────────┘
```

The edge node handles USB device access and raw IQ streaming. The core node runs all processing — FFT, classification, detection, demodulation, and persistence. This split keeps the Pi's job simple (stream bytes) while the Mac mini handles compute-intensive work.

### v2.0 Central Server Architecture

Version 2.0 adds a central WebSocket server that multiplexes real-time spectrum data, classification results, and control commands to multiple clients simultaneously. The TUI and web interface now operate as thin clients — the server streams FFT frames, waterfall data, and signal detection overlays over WebSocket channels. This enables:

- **Dual-mode operation**: TUI and web UI can run concurrently against the same backend
- **Remote monitoring**: Access spectrum data from any machine on the network
- **Signal intelligence overlay**: ML classification results stream in real-time with SigIDWiki enrichment
- **Unified control**: Device configuration, tuning, and mission control through WebSocket commands

 (Signal Intelligence Overlay) in progress — adding live classification stream and web-based detection visualization.

---

## Hardware

Four SDR types cover the spectrum from HF through L-band:

| SDR | Role | Coverage |
|-----|------|----------|
| **Kraken SDR** | Direction finding (5-channel coherent) | 24–1766 MHz |
| **Airspy R2** | Wideband scanning (10 MSPS) | 24–1700 MHz |
| **Airspy HF+ Discovery** | HF/VHF reception | 0.5–31 MHz, 60–260 MHz |
| **RTL-SDR v3/v4** | ADS-B (1090 MHz), satellite (137 MHz) | 24–1766 MHz |

Antenna array: Diamond D-130 discone (wideband), MLA-30 active loop (HF), TA1 turnstile (satellite), dedicated 1090 MHz (ADS-B), with mast-mounted Mini-Kits LNA for weak signals.

---

## Tech Stack

**Core (Python):** FastAPI, uvicorn, NumPy, SciPy, Polars, DuckDB, asyncio, Skyfield, httpx, Pydantic

**Frontend (TypeScript):** React 19, Vite, MapLibre GL, WebGL

**TUI (Rust):** ratatui, crossterm, rustfft, Kitty graphics protocol, axum (backend)

**ML:** CoreML, PyTorch, ONNX Runtime (RadioML 2018.01A training data)

**Infrastructure:** uv (package management), systemd (edge services), Docker (optional)

---

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
