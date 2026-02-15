---
layout: default
---

# Projects

Focusing on network automation, signal processing, and secure multi-agent architectures.

---

## [Network Automation →](/network-automation)

Tools for topology modeling, deterministic protocol simulation, and visualization. Includes Network Simulator, Network Visualization Engine, Network Modeling & Configuration Library, Network Topology Engine, Network Automation Workbench, Topology Generator, and more.

## [Signal Processing & RF →](/signal-processing)

SDR spectrum monitoring, biometric signal processing, and spatial audio using modular acquisition pipelines. Includes Project Spectra, Multi-SDR Streaming Server, HealthyPi, Wi-Fi Signal Reflection, and more.

## [Data Analytics →](/data-analytics)

Tools for large-scale geospatial analytics and time-series pattern discovery. Includes Tileserver Polars, matrix-profile-rs, and more.

## [Agentic Systems →](/agentic-systems)

Security-first architectures for multi-agent coordination and isolated automation. Includes the Secure Multi-Agent Personal Assistant and Cycle Agent.

## [Photography & Astrophotography →](/photography)

Integrated tools for field photography, astrophotography automation, and image processing. Includes AuroraPhoto, OpenAstro Node, EclipseStack, Photo Tour, and more.

---

## Other Projects

### [AuroraData — Aurora Planning & Substorm Advisor](projects/auroradata)

<span class="status-badge status-active">v1.0 Complete</span>

A planning tool for Australian aurora observers that answers "should I leave now?" Combines real-time solar wind monitoring (NOAA SWPC), substorm trigger detection (Bz/HP trends), site-specific weather (ACCESS-G model), and LLM-generated advice to produce a "Go/No-Go" score. Includes Telegram bot for automated alerts and historical playback for backtesting against real storm events.

### [EclipsePhoto](projects/eclipsephoto)

<span class="status-badge status-active">Phase 1 — Hardware & Data Foundation</span>

A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. Coordinates camera (via gphoto2) and mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.

### [Wave](projects/watchnoise)

<span class="status-badge status-active">Phase 21 — 55/60 Plans</span>
· **Swift (SwiftUI)**

An evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. **StillState** reclaims silence through intelligent, adaptive audio. **FlowState** achieves and maintains focus through task-linked audio and genetic evolution.

### [OmniFocus DB CLI](projects/omnifocus-db)

<span class="status-badge status-active">Phase 1 — Foundation & DB Safety</span>

A Python CLI that reads directly from the OmniFocus SQLite database on macOS, bypassing slow AppleScript layers. Provides structured, token-efficient data (JSON/Text) for agent-driven project listing, inbox analysis, and context gathering. Read-only by default.

### [nascleanup](projects/nascleanup)

<span class="status-badge status-active">Active Development</span>
· **Rust**

A Rust-based CLI tool for deduplicating and organizing large file shares. Optimized for Docker execution on Synology DSM, using an indexing layer for fast file comparison and metadata management.

### [Psytrance Generator — Algorithmic Music Engine](projects/psytrance)

<span class="status-badge status-active">Phase 1 Complete</span>
· **Rust**

A Rust engine that generates full psytrance tracks from scratch using a multi-level energy model. Hand-written DSP synthesis (oscillators, biquad filters, envelopes) drives kick, bass, hi-hat, and clap elements. Energy curves control pattern density, filter modulation, and accent placement to produce tracks with intentional structure. Five mood presets (dark, mysterious, euphoric, melancholy, aggressive) with configurable BPM, key, and scale. Includes TUI playback with energy visualization.

### [Weather (BOM ACCESS Pipeline)](projects/weather)

<span class="status-badge status-active">Phase 1/4 (50%)</span>

A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology. Targets the ACCESS model outputs, providing a clean, queryable interface (API/DuckDB) for localized weather insights.

<style>
.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }
.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }
.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
h3 { margin-bottom: 0.1em; }
h3 + .status-badge { margin-top: 0; }
section { margin-bottom: 2em; }
blockquote { margin: 1em 0; padding: 0.5em 1em; border-left: 2px solid #495057; background: #f8f9fa; font-style: normal; font-size: 0.9em; }
</style>
