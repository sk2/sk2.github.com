---
layout: default
---

# Projects

Focused on network engineering, autonomous systems, and signal processing.

---

## 🌐 Network Engineering

### [Automation Workbench](projects/ank-workbench)

**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow. ANK Workbench is the **glue layer** that coordinates the entire network automation pipeline. Engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results—all from a unified web interface.


### [Brownfield Ingestion & Analysis](projects/configparsing)

A network automation framework that decouples network configuration from vendor-specific syntax. It uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model inspired by AutoNetKit. The system enables cross-vendor configuration generation and validation through semantic simulation.


### [Device Interaction Framework](projects/deviceinteraction)

A fast, simple, and ergonomic Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities—testbed management, CLI parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit.


### [Network Configuration Framework](projects/ank-netcfg)

Deterministic, auditable, CI/CD-friendly Rust CLI for compiling declarative YAML network blueprints into vendor-neutral configuration artifacts. The `netcfg` binary orchestrates: blueprint parsing → topology transformation → DeviceIR generation → template rendering → traceable config file emission.


### [Network Modeling & Configuration Library](projects/ank-pydantic)

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.


### [Network Simulator](projects/netsim)

Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation. Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**.


### [Orchestrator (Device Interaction Runner)](projects/orchestrator)

An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem. v1 is explicitly **device-focused** and **uses `deviceinteraction` as a library** for transports/parsing/test primitives.


### [PROJECT: Network Automation Ecosystem - Overall Architecture Definition](projects/automationarch)

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product. The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.


### [Topology Engine Core](projects/ank-nte)

NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite). This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement.


### [Topology Generator](projects/topogen)

A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters. Outputs custom YAML format for use across the network engineering tool ecosystem.


### [Visualization Engine](projects/netvis)

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.


## 📡 Radio Systems

### [Project: Wi-Fi Signal Reflection (KrakenSDR)](projects/wifi-signal-analysis)




### [Radio Streaming Server](projects/rtltcp)

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.


### [Signal Reflection - KrakenSDR Multi-Beam System](projects/rf-signal-analysis)

A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.


### [Spectrum Analysis](projects/signals)




## 🏥 Health & Biometrics

### [HealthyPi Ecosystem](projects/healthypi)




## 🔭 Astrophotography

### [Aurora Advisor](projects/auroradata)

A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.


### [AuroraPhoto](projects/auroraphoto)

An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.


### [EclipseStack](projects/eclipsestack)

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.


### [OpenAstro Core](projects/open-astro-core)

OpenAstro Core ("Core SDK") is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math, imaging intelligence, and device/protocol behavior consistent across downstream OpenAstro apps.


### [OpenAstro Node](projects/open-astro-node)

A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.


### [Project: EclipsePhoto](projects/eclipsephoto)

A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.


### [Satellites](projects/satellites)

A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm. Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead.


## 📷 Photography

### [Photo Tour](projects/photo-tour)

Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.


## 🤖 Autonomous Systems

### [Project: Cycle Agent](projects/cycle)




### [Secure Multi-Agent Personal Assistant](projects/multi-agent)

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.


## 📊 Data & Utilities

### [CLI Parser](projects/cliscrape)

A high-performance parsing engine for network device output. It transforms semi-structured CLI text into structured data (JSON/YAML) using an optimized state machine. Designed as a modern, ergonomic alternative to legacy tools like TextFSM, it provides significantly faster execution while maintaining full compatibility with existing template libraries.


### [PROJECT: Tileserver Polars (Rust Optimized)](projects/tileserver)




### [Performance Simulator](projects/netflowsim)




### [Project: NAS Cleanup & Intelligence](projects/nascleanup)




### [Project: OmniFocus DB CLI (omnifocus-db)](projects/omnifocus-db)

A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.


### [Project: Weather (BOM ACCESS Pipeline)](projects/weather)

A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.


### [matrix-profile-rs](projects/matrix-time-series)

Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.


## 🧘 Wellness & Sound

### [Psytrance Generator](projects/psytrance)

A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently.


### [Wave (StillState & FlowState)](projects/watch-noise)

**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. 1. **StillState (Watch):** An adaptive sleep sounds app for Apple Watch with personalized frequency calibration, heartbeat synchronization, and microphone-based environmental monitoring.


## 🧪 Experimental

### [ASIAIR Import Tool](projects/import-asiair)

A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.


### [Network Analysis Engine](projects/netassure)

A Graph Neural Network (GNN) based network analytics module that extends NetAssure's existing topology analysis capabilities with real-time learning and prediction. Integrates with the NTE (Network Topology Engine) to provide anomaly detection, traffic prediction, and topology learning through multiple consumption interfaces.


### [Rust TUI GTD Todo (OmniFocus-inspired)](projects/todo)

A fast, keyboard-driven Rust text UI (TUI) task manager inspired by OmniFocus, built around a GTD workflow. It stores data in an owned SQLite database, supports projects and hierarchical contexts/tags, and is optimized for rapid inbox processing (triage + tagging) with minimal friction. An OmniFocus 4 `.ofocus-package` importer provides one-time migration into the local database so the tool can replace OmniFocus for day-to-day use.


### [Sound Array](projects/soundarray)

An exploration-focused audio processing system using Raspberry Pi and microphone arrays. It focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.

