---
layout: default
section: signal-processing
---

# Signal Reflection - KrakenSDR Multi-Beam System

<span class="status-badge status-active">Recently Updated</span>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Current Milestone: v2.0 Target Tracking & Visualization](#current-milestone-v20-target-tracking-visualization)
- [Current State (v1.0 shipped 2026-02-16)](#current-state-v10-shipped-2026-02-16)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Concept

A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Current Milestone: v2.0 Target Tracking & Visualization

**Goal:** Turn raw Range-Doppler detections into persistent, geographically-visualized target tracks with ADS-B validation and detection recording.

**Target features:**
- Per-beam target detection and tracking (CFAR + track association)
- Track visualization overlaid on Range-Doppler plots
- Dedicated track display with metadata (speed, heading, duration)
- Geographic map overlay (beam geometry + range → lat/lon)
- ADS-B integration for track validation and ground truth
- Detection recording and playback for offline algorithm tuning

---

## Current State (v1.0 shipped 2026-02-16)

- 9,606 lines of Python, 468 lines of Shell
- Tech stack: Python 3.10, uv, asyncio, Pydantic, Dash/Plotly, numpy, pyapril, Heimdall
- 4 phases shipped (25 plans, 1.63 hours total execution)
- Distributed architecture operational: Pi DAQ → UDP streaming → Mac/Linux processing
- 4-beam parallel processing via ProcessPoolExecutor
- Real-time Dash dashboard with 2x2 Range-Doppler grid

---

## # Validated

- Streamlined installation process (uv, platform scripts) — v1.0
- Clean, maintainable Python codebase — v1.0
- Stable operation (specific exception handling, context managers, graceful shutdown) — v1.0
- Distributed processing architecture (Pi → Mac/Linux) — v1.0
- Expanded processing window size — v1.0
- Reliable single-beam aircraft tracking — v1.0
- All 4 surveillance channels processing simultaneously — v1.0
- Side-by-side range-Doppler plots (2x2 grid) — v1.0
- Per-beam configuration and monitoring — v1.0
- Performance metrics dashboard — v1.0
- Connection health monitoring — v1.0

---

## # Active

- [ ] Per-beam target detection extraction (CFAR or threshold-based)
- [ ] Frame-to-frame track association with persistent track IDs
- [ ] Track history trails overlaid on Range-Doppler plots
- [ ] Dedicated track display showing active tracks with metadata
- [x] Geographic projection of tracks onto map (beam geometry + range → lat/lon) — v2.0
- [x] ADS-B integration for radar-aircraft correlation and validation — v2.0
- [ ] Detection data recording for offline replay and algorithm tuning

---

## # Out of Scope / Deferred to Later Milestones

- GPU acceleration — Implemented in v3.0 High-Performance Edge Compute (CuPy / Rust)
- Remote/web access improvements — Deferred to v4.0 Field Operations (Web-Based Remote Monitoring)
- Cross-beam correlation and target fusion — Deferred to v5.0 3D Tracking (Hybrid Track Fusion)
- Multi-target tracking across beams (fused track picture) — Deferred to v5.0
- 3D Altitude Estimation (AoA vector + TDOA ellipsoid intersection) — Deferred to v5.0
- Nvidia Jetson IPC Foundation (NvSCI / Unified Memory for PyO3/Rust) — Deferred to v5.0
- KrakenSDR 2D DoA (MUSIC + Spatial Smoothing) — Deferred to v5.0
- Raw IQ recording — Storage requirements too large (GB/min), detection-level recording sufficient
- Mobile support — Desktop-focused (Web UI mobile-responsive in v4.0)
- Multi-user features — Single operator

---

## Context

**Hardware Setup:**
- KrakenSDR SDR with 5 receive channels
- 1 reference channel (direct signal from transmitter)
- 4 surveillance channels (Yagi antennas for reflections)
- Raspberry Pi (data acquisition)
- Mac and/or Linux PC (processing)
- Future Target: Nvidia Jetson for unified edge compute and zero-copy IPC (v5.0)

**Operational Environment:**
- Located south of airport (target: aircraft traffic to the north)
- Passive transmitter to the east (good geometry, minimal interference)
- Distributed processing needed due to Pi performance limitations
- ADS-B receiver available for ground truth correlation

**Codebase Architecture (v1.0):**
- Pi runs Heimdall DAQ, streams IQ via UDP (65-80 FPS)
- Mac/Linux receives IQ, processes with pyapril DSP
- TCP control channel for bidirectional commands
- mDNS service discovery with manual IP fallback
- Pydantic configuration validation (BeamConfig, MultiBeamConfig)
- ProcessPoolExecutor for 4-beam parallel processing
- Dash 2.0+ web dashboard with per-beam metrics
- systemd service for Pi auto-restart

---

## Constraints

- **Hardware**: KrakenSDR (5 RX channels), Raspberry Pi, Mac, Linux PC available
- **Compatibility**: Must maintain compatibility with Heimdall library (C-based DSP core)
- **Performance**: Raspberry Pi alone insufficient for processing, need distributed architecture
- **Architecture**: Pi handles data acquisition, Mac/Linux handles compute-intensive DSP
- **Numpy**: Locked to <1.24 due to numba 0.56.4 compatibility
- **Python**: Pinned to 3.10 for numba/ARM wheel compatibility
- **Tracking scope**: Per-beam only for v2 — no cross-beam fusion

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Phase 1 = foundation before features | Original codebase too unstable to extend | ✓ Good — clean base enabled rapid feature development |
| Distributed processing (Pi → Mac/Linux) | Pi performance insufficient for expanded processing | ✓ Good — 65-80 FPS streaming achieved |
| Keep Heimdall-based pipeline | Proven DSP library, avoid rewriting core algorithms | ✓ Good — stable DSP foundation |
| Defer cross-beam correlation to v5.0 | Requires multi-beam fusion research and coherent array operation (KrakenSDR DoA) | — Pending |
| UV for dependency management | Faster, more reliable than pip/conda | ✓ Good — reproducible environments |
| Asyncio-based distributed architecture | Non-blocking I/O for streaming + control | ✓ Good — clean concurrency model |
| ProcessPoolExecutor for multi-beam | True parallelism for CPU-bound DSP, bypasses GIL | ✓ Good — 4 beams process independently |
| Pydantic for configuration | Type-safe validation, environment variable support | ✓ Good — catches config errors at startup |
| Per-beam tracking before fusion (v2) | Simpler, independently useful, validates detection pipeline | — Pending |
| Both beam geometry and ADS-B for geo (v2) | Geometry gives approximate position, ADS-B validates accuracy | — Pending |
| Detection-level recording, not raw IQ (v2) | Manageable storage, sufficient for tracking algorithm tuning | — Pending |

*Last updated: 2026-03-04 after adding v5.0 research findings*

---

## Current Status

2026-03-01 — Completed  (Rust Intelligence).

---

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
