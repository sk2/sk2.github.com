---
layout: default
---

# Projects

Focusing on network automation, high-performance signal processing, and secure multi-agent architectures.

---

## 🌐 Network Automation

> **[View Ecosystem →](/network-automation)**
> High-performance tools for topology modeling, deterministic protocol simulation, and visualization.

### [ANK Workbench](projects/ank-workbench)

<span class="status-badge status-active">v1.3 — Tool Integration & Interactive Workflows</span>
· **Python (FastAPI) · React frontend**

**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, NTE, Network Simulator, NetVis) into one seamless workflow. v1.0-v1.1 shipped with end-to-end workflow and UX polish. v1.2 added GPU-accelerated visualization at scale. v1.3 adds interactive device access, simulator integration, config export, and live simulation observability.

### [AutoNetkit](projects/autonetkit)

<span class="status-badge status-active">PhD 2017</span>
· **Python**

### [NetVis](projects/netvis)

<span class="status-badge status-active">v1.3 — Embed Readiness & API Stability</span>
· **Rust**

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity.

v1.2 shipped with SVG filter infrastructure, WCAG contrast enforcement, and label collision avoidance. Currently stabilizing the public API and output contracts for embedding in ANK Workbench.

![ISP Backbone](/images/netvis-isp-backbone.png)
*ISP backbone with path analysis — one of several layout styles available.*

### [Network Simulator](projects/network-simulator)

<span class="status-badge status-active">v1.7 — Segment Routing (SR-MPLS)</span>
· **Rust · 126,000+ LOC · 1,350+ tests**

A Rust-based network simulator that models packet-level behavior for routing protocols. Provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation.

v1.6 shipped with L3VPN, daemon mode with interactive console (attach to simulated devices with tab completion and Cisco IOS-style command abbreviation), and BMP telemetry. v1.7 adds SR-MPLS dataplane support.

### [TopoGen - Network Topology Generator](projects/topogen)

<span class="status-badge status-active">Phase 18/24 (15%)</span>

A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters.

Outputs custom YAML format for use across the network engineering tool ecosystem. Network engineers can quickly generate realistic, validated network topologies without implementing complex algorithms from scratch.

### [NTE — Network Topology Engine](projects/nte)

<span class="status-badge status-active">Stable — Rust Backend</span>
· **Rust**

The high-performance Rust engine that powers ank_pydantic's graph operations. Extracted into its own repository as the engine matured. Uses petgraph's StableDiGraph for topology representation and Polars for columnar storage. Organized as a Cargo workspace with specialized crates (nte-core, nte-query, nte-domain, nte-datastore-*, nte-server, nte-monte-carlo).

### [ank_pydantic](projects/ank-pydantic)

<span class="status-badge status-active">v1.8 — Performance & Optimization</span>

A Python library for modeling and querying network topologies, backed by the NTE Rust engine. Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution.

v1.7 shipped with API usability improvements. Currently optimizing query performance, adding profiling infrastructure, and validating at 10k+ node scale. Ships with domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

## 📊 Data Science & Simulation

> **[View Ecosystem →](/data-analytics)**
> High-performance tools for large-scale geospatial analytics and time-series pattern discovery.

### [Tileserver Polars (Rust Optimized)](projects/tileserver)

<span class="status-badge status-active">Active Development</span>

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

### [Weather (BOM ACCESS Pipeline)](projects/weather)

<span class="status-badge status-active">Phase 1/4 (50%)</span>

A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.

The primary goal is to bypass the complexity of BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a clean, queryable interface (API/DuckDB) for localized weather insights, starting with South Australia.

### [matrix-profile-rs](projects/matrix-time-series)

<span class="status-badge status-active">Phase 2/5 (50%)</span>

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

Time series analysis requires identifying:

- **Repeating patterns** (motifs): "This sensor pattern happened 15 times before failure"
- **Anomalies** (discords): "This heartbeat segment is unlike any other"
- **Similar segments**: "Find all sequences similar to this known good pattern"

### [netflowsim](projects/netflowsim)

<span class="status-badge status-active">Active Development</span>

`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds.

## 🤖 AI & Agents

> **[View Ecosystem →](/agentic-systems)**
> Security-first architectures for multi-agent coordination and isolated automation.

### [Cycle Agent](projects/cycle)

<span class="status-badge status-active">Phase 1/5 (80%)</span>

A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.

### [Secure Multi-Agent Personal Assistant](projects/multi-agent)

<span class="status-badge status-active">Phase 18/20 (84%)</span>
· **Agents can be Go · Python · or Rust**

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments.

The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic. Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

## 📡 Signal Processing & RF

> **[View Ecosystem →](/signal-processing)**
> SDR spectrum monitoring and biometric signal processing using modular acquisition pipelines.

### [HealthyPi Ecosystem](projects/healthypi)

<span class="status-badge status-active">Phase 6/6 (87%)</span>

A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.

### [RF Signal Reflection Experiments](projects/passive)

<span class="status-badge status-active">Phase 3/4 (100%)</span>

An experimental signal processing project exploring how to analyze reflections of ambient radio signals. The system uses coherent multi-channel RF data to study bistatic geometry and Doppler effects.

Practical exploration of bistatic radar concepts and signal processing techniques using existing RF infrastructure. Clean, stable codebase for processing multi-channel RF reflections.

### [rtltcp-rust](projects/rtltcp)

<span class="status-badge status-active">v1 — Core Streaming & Hardware</span>
· **Rust**

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. Features a built-in TUI for live configuration and device management, multi-threaded architecture for concurrent SDR streaming, and TOML-based persistent configuration.

### [Project Spectra](projects/signals)

<span class="status-badge status-active">\*\* Phase 3: Autonomy</span>

Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.

### [Wi-Fi Reflection sensing](projects/wifi-radar)

<span class="status-badge status-active">Active Development</span>

System that utilizes existing Wi-Fi signals for through-wall detection and localization, leveraging a coherent radio array.

## 🔭 Experimental & Hobbies

### [ASIAIR Import Tool](projects/import-asiair)

<span class="status-badge status-active">Phase 1/1 (0%)</span>

A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.

Eliminates manual file sorting after imaging sessions - scan hundreds of frames, organize by target/filter/date, validate calibration frame availability, and go straight to PixInsight processing.

### [AuroraData - Aurora Planning & Substorm Advisor](projects/auroradata)

<span class="status-badge status-active">\*\* 1 - Substorm Trigger Engine</span>

A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.

Providing a single, definitive "Go/No-Go" score that accounts for both space weather potential and local terrestrial conditions (travel time, clouds, moon).

### [AuroraPhoto](projects/auroraphoto)

<span class="status-badge status-active">\*\* Phase 1: Star Sharpness Foundation</span>

An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.

Provides precise, automated control over exposure and focus specifically optimized for aurora "bursts" and star sharpness, while offering field-ready composition tools.

### [EclipsePhoto](projects/eclipsephoto)

<span class="status-badge status-active">\*\* 1 - Hardware & Data Foundation</span>

A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.

Reliability and autonomy for a "one-shot" astronomical event. The system handles guiding, exposure ramping (Holy Grail), and error recovery (watchdogs) so the photographer can experience the eclipse while the system secures the data.

### [EclipseStack](projects/eclipsestack)

<span class="status-badge status-active">\*\* 1 (Ingestion & Foundation)</span>

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data.

The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight. Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

### [OmniFocus DB CLI (omnifocus-db)](projects/omnifocus-db)

<span class="status-badge status-active">\*\* Phase 1: Foundation & DB Safety</span>

A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.

- **Zero-Latency Context:** Near-instant retrieval of projects and tasks without the overhead of the OmniFocus app or AppleScript. - **Agent-Optimized:** Focused on providing dense, low-token representations of the user's task list.

- **Safety First:** Read-only access by default to prevent database corruption while OmniFocus is active.

### [OpenAstro Core](projects/open-astro-core)

<span class="status-badge status-active">Active Development</span>

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.

### [OpenAstro Node](projects/open-astro-node)

<span class="status-badge status-active">\*\* 2. Control</span>

A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.

### [Photo Tour](projects/photo-tour)

<span class="status-badge status-active">Active Development</span>

Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.

In the field, you can see what the camera sees and get actionable guidance/control fast enough to improve the shot.

### [Wave](projects/watch-noise)

<span class="status-badge status-active">Active Development</span>
· **Swift (SwiftUI)**

**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. - **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio

- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution

### [Wave (StillState & FlowState)](projects/watchnoise)

<span class="status-badge status-active">21 (Bluetooth Output Enforcement Hardening)</span>

**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. - **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio.

- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution.

### [nascleanup](projects/nascleanup)

<span class="status-badge status-active">Active Development</span>
· **Rust**

A Rust-based CLI tool for deduplicating and organizing large file shares. Optimized for Docker execution on DSM, it uses an indexing layer for fast file comparison and metadata management.

### [soundarray](projects/soundarray)

<span class="status-badge status-active">Active Development</span>

An exploration-focused audio processing system using Raspberry Pi and microphone arrays. It focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.

The ability to capture, localize, and classify complex soundscapes on edge devices or via remote streaming, providing structured insights to an agent framework.

<style>
.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }
.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }
.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
h3 { margin-bottom: 0.1em; }
h3 + .status-badge { margin-top: 0; }
section { margin-bottom: 2em; }
blockquote { margin: 1em 0; padding: 0.5em 1em; border-left: 2px solid #495057; background: #f8f9fa; font-style: normal; font-size: 0.9em; }
</style>

