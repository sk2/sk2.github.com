---
layout: default
section: signal-processing
## Current Status

2026-02-22 — Completed 07-04 Performance verification harness (multi-client WS perf verifier + usage notes)

---

# Project Spectra

<span class="status-badge status-active">Phase 7/7</span>

[← Back to Signal Processing](../signal-processing)

## Current Status

2026-02-22 — Completed 07-04 Performance verification harness (multi-client WS perf verifier + usage notes)

---

## Concept

Monitor the local radio spectrum autonomously, classify every detected signal using ML, and maintain a persistent "Signal Census" — a queryable database of all RF activity over time. Distributed across Raspberry Pi edge nodes and a Mac mini core, the system runs unattended, sweeping bands, scheduling satellite passes, and logging what it finds.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 7/7 |
| **Language** | N/A |
| **Started** | 2026 |

## Current Status

2026-02-22 — Completed 07-04 Performance verification harness (multi-client WS perf verifier + usage notes)

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

Phase 8 (WebSocket Foundation) complete. Phase 9 (Signal Intelligence Overlay) in progress — adding live classification stream and web-based detection visualization.

## Terminal Interface

![Spectra TUI](/images/spectra-tui.png)
*Rust TUI showing live spectrum, waterfall (Kitty graphics protocol), and device controls.*

The Rust TUI renders a pixel-level waterfall using the Kitty graphics protocol for true-color, full-resolution display directly in the terminal. Spectrum graphs use block-character rendering with configurable color palettes (twilight, inferno, viridis, ice, gray). Keyboard controls handle retuning, gain adjustment, and device switching without leaving the terminal.

## Hardware

Four SDR types cover the spectrum from HF through L-band:

| SDR | Role | Coverage |
|-----|------|----------|
| **Kraken SDR** | Direction finding (5-channel coherent) | 24–1766 MHz |
| **Airspy R2** | Wideband scanning (10 MSPS) | 24–1700 MHz |
| **Airspy HF+ Discovery** | HF/VHF reception | 0.5–31 MHz, 60–260 MHz |
| **RTL-SDR v3/v4** | ADS-B (1090 MHz), satellite (137 MHz) | 24–1766 MHz |

Antenna array: Diamond D-130 discone (wideband), MLA-30 active loop (HF), TA1 turnstile (satellite), dedicated 1090 MHz (ADS-B), with mast-mounted Mini-Kits LNA for weak signals.

## Signal Census

The core concept: every detected signal gets logged to a DuckDB database with timestamp, frequency, power, modulation classification, confidence score, SigIDWiki metadata matches, and bearing (from Kraken direction finding). This builds a persistent picture of the local RF environment over time.

Queries answer questions like:
- "What transmits on 148.7 MHz at 3 AM?"
- "Show all FM signals above -60 dBm in the last 24 hours"
- "Which frequencies had anomalous activity compared to baseline?"

Anomaly detection uses per-band/frequency/hour bucketing with p90+margin flagging — no tuning required.

## ML Classification

Two-stage pipeline:

1. **Real-time model**: Fast CNN inference on live IQ samples (2–5 ms latency). Classifies AM, FM, SSB, BPSK, QPSK, 16-QAM and others.
2. **Retrospective model**: Deeper CNN triggered on low-confidence detections, using larger sample windows (8,192 samples) for improved accuracy.

Classification augmented by:
- **Constellation analysis**: Mueller-Muller timing recovery for symbol extraction, EVM (Error Vector Magnitude) against ideal constellation points
- **SigIDWiki integration**: Semantic MediaWiki queries match detected signals against known frequency allocations, modulation types, and location data (cached with 30-day TTL)

## Autonomous Missions

The missions engine runs unattended scanning operations:

- **Bandplan sweeping**: Systematic frequency scanning across radio service allocations
- **Satellite scheduling**: Skyfield orbital mechanics calculate NOAA/Meteor pass windows, trigger automated recording during passes
- **Hit scoring**: Notability-based prioritization ranks signals by rarity and interest
- **Daily briefings**: Deterministic summary generation (no LLM — template-based)

Each mission logs events to `.logs/missions/{run_id}/events.jsonl` for post-session review.

## ADS-B Integration

Ingests Beast/SBS TCP feeds from readsb running on the Pi. Aircraft positions, altitudes, and callsigns appear on the tactical map alongside signal bearings and census hits. Historical observations are queryable via the API for replay.

## Direction Finding

The Kraken SDR's 5-channel coherent receiver enables phase-coherent direction-of-arrival estimation. Signal bearings render as lines on the tactical map, correlating with census entries and ADS-B aircraft positions.

## Web Frontend

![Spectra Waterfall](/images/spectra-waterfall.png)
*WebGL waterfall display with real-time spectrum analysis.*

React/TypeScript frontend with:
- **WebGL waterfall**: Efficient texture updates via `texSubImage2D` with ring-buffer scrolling
- **Classification panel**: Real-time signal list with confidence scores and SigIDWiki matches
- **Constellation diagram**: IQ scatter plot with timing recovery overlay
- **Tactical map**: MapLibre-based with GeoJSON layers for ADS-B aircraft, DoA bearings, and signal census hits
- **Signal Census view**: Queryable historical database with time-window filtering

## REST API

FastAPI backend with WebSocket support:

| Endpoint | Purpose |
|----------|---------|
| `GET /devices` | SDR registry and status |
| `PATCH /devices/{name}/settings` | Tune frequency, sample rate, gain |
| `WS /ws/waterfall/{device}` | Binary spectrum frames (uint8) |
| `GET /api/health/deep` | Structured health JSON |
| `GET /api/map/live` | ADS-B + DoA bearings + census hits |
| `POST /api/nlq` | Natural language queries (deterministic templates) |

WebSocket protocol: one JSON metadata message followed by binary uint8 spectrum frames at 10–20 FPS.

## Health and Resilience

- **Auto-reconnect**: Exponential backoff (1s → 30s cap) for all device connections
- **Per-device isolation**: One SDR failure does not affect others
- **Bounded queues**: Frame dropping under load keeps UI responsive
- **Health tracker**: Per-device connection, streaming, and frame freshness monitoring
- **E2E verification harness**: Automated testing across 4 data flows

## Development Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| 1 | Foundation — streaming, waterfall, device control | Complete |
| 2 | Intelligence — ML classification, constellation, demod | Complete |
| 3 | Autonomy — Signal Census, scanning, satellites, missions | Complete |
| 6 | Verification — health monitoring, auto-reconnect, E2E tests | Complete |
| 7 | Performance — ring buffer, GPU FFT, batch updates | Planned |

## Tech Stack

**Core (Python):** FastAPI, uvicorn, NumPy, SciPy, Polars, DuckDB, asyncio, Skyfield, httpx, Pydantic

**Frontend (TypeScript):** React 19, Vite, MapLibre GL, WebGL

**TUI (Rust):** ratatui, crossterm, rustfft, Kitty graphics protocol, axum (backend)

**ML:** CoreML, PyTorch, ONNX Runtime (RadioML 2018.01A training data)

**Infrastructure:** uv (package management), systemd (edge services), Docker (optional)

## Current Status

2026-02-22 — Completed 07-04 Performance verification harness (multi-client WS perf verifier + usage notes)

---

[← Back to Signal Processing](../signal-processing)
