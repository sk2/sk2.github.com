---
layout: default
---

# Projects

Focused on network engineering, autonomous systems, and signal processing.

---

## 🌐 Network Engineering

### [Configuration Generation (AutoNetkit)](projects/autonetkit)

<span class="status-badge status-active">Active</span>


A compiler-based framework for automated network provisioning. AutoNetkit transforms high-level network designs into validated device configurations across heterogeneous hardware and protocol environments.


### [Brownfield Ingestion & Analysis](projects/configparsing)

<span class="status-badge status-active">Recently Updated</span>


A specialized framework for **Brownfield Ingestion and Analysis**. It extracts high-level architectural intent and topology relationships from legacy network state—including vendor-specific CLI configurations and unstructured PDF documentation—normalizing them into a vendor-neutral model.


### [Visualization Engine](projects/netvis)

<span class="status-badge status-active">Recently Updated</span>


A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.


### [Topology Engine Core](projects/ank-nte)

<span class="status-badge status-active">Recently Updated</span>


The fast graph core that powers the ANK ecosystem. NTE (Network Topology Engine) provides a native Rust implementation of multi-layer network graphs, optimized for low-latency queries and complex topological transformations.


### [Topology Generator](projects/topogen)

<span class="status-badge status-active">Recently Updated</span>


A Rust-based topology generation engine that consolidates complex network graph algorithms into a unified, fast library. It enables the creation of realistic, validated network structures ranging from small lab setups to massive data center and backbone environments.


### [Automation Workbench](projects/ank-workbench)

<span class="status-badge status-active">Recently Updated</span>


**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow.


### [Network Modeling Foundations](projects/autonetkit-foundation)

<span class="status-badge status-active">Active</span>


The original research that established the principles of automated network configuration. This work introduced the **Whiteboard → Plan → Build** transformation model, which allows engineers to work with high-level design abstractions while the system handles the technical implementation details.


### [Network Simulator](projects/netsim)

<span class="status-badge status-active">Recently Updated</span>


A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation. Used for smoke testing and design validation of network configurations.


### [Configuration Engine](projects/ank-pydantic)

<span class="status-badge status-active">Recently Updated</span>


A modern configuration engine for defining a network model and compiling it into a consistent, reviewable plan for downstream tooling. Built with type-safe Pydantic models and a fast Rust core (NTE), it provides a predictable, programmable way to manage large-scale topology data and derived configuration state.


### [Orchestrator (Device Interaction Runner)](projects/orchestrator)

<span class="status-badge status-active">Recently Updated</span>


An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.


### [Device Interaction Framework](projects/deviceinteraction)

<span class="status-badge status-active">Recently Updated</span>


A fast, simple, and ergonomic Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities—testbed management, CLI parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit.


### [Network Automation Ecosystem - Overall Architecture Definition](projects/automationarch)

<span class="status-badge status-active">Recently Updated</span>


This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.


## 📡 Radio Systems

### [Radio Streaming Server](projects/rtltcp)

<span class="status-badge status-active">Recently Updated</span>


A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.


### [Passive Radar - KrakenSDR Multi-Beam System](projects/rf-signal-analysis)

<span class="status-badge status-active">Recently Updated</span>


A distributed multi-beam passive radar system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.


### [Spectrum Analysis](projects/signals)

<span class="status-badge status-active">Recently Updated</span>


Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.


### [Wi-Fi Radar (KrakenSDR)](projects/wifi-signal-analysis)

<span class="status-badge status-active">Active</span>


Passive radar system that utilizes existing Wi-Fi signals for through-wall human detection and localization, leveraging the KrakenSDR coherent radio array.


## 🏥 Health & Biometrics

### [HealthyPi Ecosystem](projects/healthypi)

<span class="status-badge status-active">Recently Updated</span>


A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.


## 🔭 Astrophotography

### [OpenAstro Core](projects/open-astro-core)

<span class="status-badge status-active">Active</span>


OpenAstro Core is a fast Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.


### [Aurora Advisor](projects/auroradata)

<span class="status-badge status-active">Active</span>


A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.


### [Satellites](projects/satellites)

<span class="status-badge status-active">Recently Updated</span>


A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm. Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead.


### [AuroraPhoto](projects/auroraphoto)

<span class="status-badge status-active">Active</span>


An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.


### [EclipsePhoto](projects/eclipsephoto)

<span class="status-badge status-active">Active</span>


A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.


### [EclipseStack](projects/eclipsestack)

<span class="status-badge status-active">Active</span>


EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.


### [OpenAstro Node](projects/open-astro-node)

<span class="status-badge status-active">Active</span>


A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.


## 📷 Photography

### [Photo Tour](projects/photo-tour)

<span class="status-badge status-active">Active</span>


Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.


## 🤖 Autonomous Systems

### [Secure Multi-Agent Personal Assistant](projects/multi-agent)

<span class="status-badge status-active">Recently Updated</span>


A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.


### [Cycle Agent](projects/cycle)

<span class="status-badge status-active">Recently Updated</span>


A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a fast SceneKit environment.


## 📊 Data & Utilities

### [matrix-profile-rs](projects/matrix-time-series)

<span class="status-badge status-active">Recently Updated</span>


Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.


### [CLI Parser](projects/cliscrape)

<span class="status-badge status-active">Active</span>


A fast parsing engine for network device output. It transforms semi-structured CLI text into structured data (JSON/YAML) using an optimized state machine. Designed as a modern, ergonomic alternative to legacy tools like TextFSM, it provides significantly faster execution while maintaining full compatibility with existing template libraries.


### [Performance Simulator](projects/netflowsim)

<span class="status-badge status-active">Recently Updated</span>


A performance analysis engine that utilizes analytic queuing models and Monte Carlo simulations to validate network capacity at scale. Unlike packet-level simulators, netflowsim focuses on probabilistic outcomes across billions of traffic flows.


### [OmniFocus DB CLI (omnifocus-db)](projects/omnifocus-db)

<span class="status-badge status-active">Last Active: 2026-02-16</span>


A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.


### [Weather (BOM ACCESS Pipeline)](projects/weather)

<span class="status-badge status-active">Last Active: 2026-02-14</span>


A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.


### [Tileserver Polars (Rust Optimized)](projects/tileserver)

<span class="status-badge status-active">Active</span>


Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.


## 🧘 Wellness & Sound

### [Psytrance Generator](projects/psytrance)

<span class="status-badge status-active">Recently Updated</span>


A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently.


## 🧪 Experimental

### [Wave (StillState & FlowState)](projects/watch-noise)

<span class="status-badge status-active">Recently Updated</span>


**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work.


### [Rust TUI GTD Todo (OmniFocus-inspired)](projects/todo)

<span class="status-badge status-active">Recently Updated</span>


A fast, keyboard-driven Rust text UI (TUI) task manager inspired by OmniFocus, built around a GTD workflow. It stores data in an owned SQLite database, supports projects and hierarchical contexts/tags, and is optimized for rapid inbox processing (triage + tagging) with minimal friction.


### [ASIAIR Import Tool](projects/import-asiair)

<span class="status-badge status-active">Last Active: 2026-02-11</span>


A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.


### [Sound Array](projects/soundarray)

<span class="status-badge status-active">Active</span>


An exploration-focused audio processing system using Raspberry Pi and microphone arrays. It focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.


<style>
.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }
.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }
section { margin-bottom: 2em; }
</style>