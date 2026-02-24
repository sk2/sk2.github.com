---
layout: default
---

# Projects

Focused on network engineering, autonomous systems, and signal processing.

---

## 🌐 Network Engineering

### [Network Simulator](projects/network-simulator)

<span class="status-badge status-updated">Recently Updated</span>


A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation. Used for smoke testing and design validation of network configurations.


### [NetVis](projects/netvis)

<span class="status-badge status-updated">Recently Updated</span>


A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.


### [TopoGen - Network Topology Generator](projects/topogen)

<span class="status-badge status-updated">Recently Updated</span>


A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters. Outputs custom YAML format for use across the network engineering tool ecosystem.


### [ANK Workbench](projects/ank-workbench)

<span class="status-badge status-updated">Recently Updated</span>


**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow.


### [Orchestrator (Device Interaction Runner)](projects/orchestrator)

<span class="status-badge status-updated">Recently Updated</span>


An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.


### [Network Topology Engine](projects/ank-nte)

<span class="status-badge status-updated">Recently Updated</span>


NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite). This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement.


### [Network Modeling Library](projects/ank-pydantic)

<span class="status-badge status-updated">Recently Updated</span>


A Python library for modeling and querying network topologies, backed by a fast Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.


### [Network Configuration Analysis](projects/configparsing)

<span class="status-badge status-updated">Recently Updated</span>


A network automation framework that decouples network configuration from vendor-specific syntax. It uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model inspired by AutoNetKit. The system enables cross-vendor configuration generation and validation through semantic simulation.


### [Device Interaction Framework](projects/deviceinteraction)

<span class="status-badge status-updated">Recently Updated</span>


A fast, simple, and ergonomic Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities—testbed management, CLI parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit.


### [Network Automation Ecosystem](projects/automationarch)

<span class="status-badge status-updated">Recently Updated</span>


This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.


## 📡 Radio Systems

### [Spectrum Analysis](projects/signals)

<span class="status-badge status-updated">Recently Updated</span>


Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.


### [Radio Streaming Server](projects/rtltcp)

<span class="status-badge status-updated">Recently Updated</span>


A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.


### [Signal Reflection Analysis](projects/rf-signal-analysis)

<span class="status-badge status-updated">Recently Updated</span>


A distributed multi-beam passive radar system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.


### [Wi-Fi Radar](projects/wifi-signal-analysis)

<span class="status-badge status-active">Active</span>


Passive radar system that utilizes existing Wi-Fi signals for through-wall human detection and localization, leveraging the KrakenSDR coherent radio array.


## 🏥 Health & Biometrics

### [HealthyPi Ecosystem](projects/healthypi)

<span class="status-badge status-updated">Recently Updated</span>


A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.


## 🔭 Astrophotography

### [Aurora Advisor](projects/auroradata)

<span class="status-badge status-active">Active</span>


A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.


### [Satellites](projects/satellites)

<span class="status-badge status-updated">Recently Updated</span>


A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm. Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead.


### [OpenAstro Node](projects/open-astro-node)

<span class="status-badge status-active">Active</span>


A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.


### [AuroraPhoto](projects/auroraphoto)

<span class="status-badge status-active">Active</span>


An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.


### [EclipsePhoto](projects/eclipsephoto)

<span class="status-badge status-active">Active</span>


A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.


### [OpenAstro Core](projects/open-astro-core)

<span class="status-badge status-active">Active</span>


OpenAstro Core is a fast Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.


### [EclipseStack](projects/eclipsestack)

<span class="status-badge status-active">Active</span>


EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.


## 📷 Photography

### [Photo Tour](projects/photo-tour)

<span class="status-badge status-active">Active</span>


Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.


## 🤖 Autonomous Systems

### [Secure Multi-Agent Personal Assistant](projects/multi-agent)

<span class="status-badge status-updated">Recently Updated</span>


A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.


### [Cycle Agent](projects/cycle)

<span class="status-badge status-updated">Recently Updated</span>


A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a fast SceneKit environment.


## 📊 Data & Utilities

### [OmniFocus DB CLI (omnifocus-db)](projects/omnifocus-db)

<span class="status-badge status-active">Last Active: 2026-02-16</span>


A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.


### [Network Performance Simulator](projects/netflowsim)

<span class="status-badge status-updated">Recently Updated</span>


`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds, identify bottlenecks probabilistically, and test network resilience under failure scenarios.


### [matrix-profile-rs](projects/matrix-time-series)

<span class="status-badge status-updated">Recently Updated</span>


Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.


### [CLI Parser](projects/cliscrape)

<span class="status-badge status-active">Active</span>


`cliscrape` is a fast CLI scraping and parsing tool for network devices, written in Rust. It provides a modern, ergonomic, and blazingly fast alternative to legacy tools like `TextFSM`, while maintaining first-class compatibility with existing templates.


### [Weather (BOM ACCESS Pipeline)](projects/weather)

<span class="status-badge status-active">Last Active: 2026-02-14</span>


A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.


### [Tileserver Polars (Rust Optimized)](projects/tileserver)

<span class="status-badge status-active">Active</span>


Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.


## 🧘 Wellness & Sound

### [Psytrance Generator](projects/psytrance)

<span class="status-badge status-updated">Recently Updated</span>


A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently.


### [Wave (StillState & FlowState)](projects/watchnoise)

<span class="status-badge status-updated">Recently Updated</span>


**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work.


## 🧪 Experimental

### [AutoNetkit](projects/autonetkit)

<span class="status-badge status-active">Active</span>


Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. **AutoNetkit** eliminates this trade-off by using Pydantic for schema validation and a Rust core (`petgraph`) for graph traversals. It is a modern reimagining of the original AutoNetkit research, reclaiming the name for a production-ready automation library.


### [Project Spectra](projects/spectra)

<span class="status-badge status-active">Active</span>


Developing...


### [AutoNetkit — The Foundation](projects/autonetkit-foundation)

<span class="status-badge status-active">Active</span>


Developing...


### [HRV Monitor](projects/hrv)

<span class="status-badge status-active">Active</span>


Heart Rate Variability (HRV) reveals stress, recovery, and autonomic nervous system state through timing variations between heartbeats. Most consumer devices only report derived metrics without providing the underlying RR interval data needed for analysis. This Rust-based driver connects directly to Bluetooth LE heart rate monitors, streams raw RR intervals in real-time, computes time-domain HRV metrics, and logs sessions to columnar Parquet files for downstream analysis.


### [Wave](projects/watch-noise)

<span class="status-badge status-active">Active</span>


- **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio
- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution


### [soundarray](projects/soundarray)

<span class="status-badge status-active">Active</span>


An exploration-focused audio processing system using Raspberry Pi and microphone arrays. It focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.


### [Network Configuration Parser](projects/ank-parse)

<span class="status-badge status-active">Active</span>


Developing...


### [GSD Project Monitor](projects/devmon)

<span class="status-badge status-active">Active</span>


Developing...


### [Rust TUI GTD Todo (OmniFocus-inspired)](projects/todo)

<span class="status-badge status-updated">Recently Updated</span>


A fast, keyboard-driven Rust text UI (TUI) task manager inspired by OmniFocus, built around a GTD workflow. It stores data in an owned SQLite database, supports projects and hierarchical contexts/tags, and is optimized for rapid inbox processing (triage + tagging) with minimal friction.


### [nascleanup](projects/nascleanup)

<span class="status-badge status-active">Active</span>


Developing...


### [ASIAIR Import Tool](projects/import-asiair)

<span class="status-badge status-active">Last Active: 2026-02-11</span>


A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.


<style>
.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }
.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }
.status-updated { background-color: #e3f2fd; color: #0d47a1; border: 1px solid #bbdefb; }
.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
h3 { margin-bottom: 0.1em; }
h3 + .status-badge { margin-top: 0; }
section { margin-bottom: 2em; }
</style>