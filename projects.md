---
layout: default
---

# Projects

Focusing on network automation, high-performance signal processing, and secure multi-agent architectures.

---

## 🌐 Network Engineering

> **[View Ecosystem →](/network-automation)**
> High-performance tools for topology modeling, deterministic protocol simulation, and visualization.

### [ANK Workbench](projects/ank-workbench)

<span class="status-badge status-active">Phase 34/39 (42%)</span>
 · **Python backend (FastAPI or Flask) · React or Vue frontend — Leverages existing Python ecosystem for ANK components · meets modern UX expectations**


**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow. Network engineers can design, validate, and visualize network changes in one complete workflow without switching between separate tools or manually gluing components together.


### [AutoNetkit](projects/autonetkit)

<span class="status-badge status-active">v1.8 — Performance & Optimization</span>


Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. **AutoNetkit** eliminates this trade-off by using Pydantic for schema validation and a Rust core (`petgraph`) for graph traversals.

It is a modern reimagining of the original AutoNetkit research, reclaiming the name for a production-ready automation library. A Python library for modeling and querying network topologies with type-safe Pydantic models and a Rust core.

Expressive Python API backed by compiled graph algorithms (petgraph), with automatic configuration generation for multi-vendor network deployments.


### [AutoNetkit — The Foundation](projects/autonetkit-foundation)

<span class="status-badge status-active">PhD 2017</span>
 · **Python**


Developing...


### [Device Interaction Framework](projects/deviceinteraction)

<span class="status-badge status-active">Not started (defining requirements for v1.1)</span>


A fast, simple, and ergonomic Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities—testbed management, CLI parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit.

Enable rapid, type-safe validation of network device state through streamlined device interaction: connect to devices (real, simulated, or mocked), execute commands, parse structured output, and verify correctness—all with the performance and safety guarantees of Rust.


### [NTE: Engine Hardening & LadybugDB Evaluation](projects/ank-nte)

<span class="status-badge status-active">Phase 3/6 (100%)</span>


NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite).

This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement. The engine must be correct and observable — mutations never silently corrupt state, errors always surface meaningful information, and operations are traceable through logging.


### [NetVis](projects/netvis)

<span class="status-badge status-active">Phase 42.1 complete (data-source-adapters)</span>
 · **Rust**


A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity.

Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling. Transform network topologies into clear, information-dense visualizations using algorithms that minimize edge crossings, bundle related connections, and respect hierarchical/geographic structure — enabling understanding of networks that would otherwise be visual noise.


### [Network Configuration Parser](projects/ank-parse)

<span class="status-badge status-active">Phase 1 — Knowledge Base Ingestion</span>
 · **Python**


Developing... A framework for parsing and analyzing device configurations across multiple networking vendors.

The project bridges the gap between unstructured legacy CLI data and structured intent-based models. - **Syntax Fragmentation**: Every vendor (Cisco, Juniper, Arista, Nokia) has a different CLI structure for the same protocol (OSPF, BGP).

- **Manual Translation**: Engineers spend hours cross-referencing manuals to convert a "design" into "commands."
- **Data Silos**: Configuration state is locked in text files rather than queryable databases.


### [Network Configuration Parsing & Analysis Framework](projects/configparsing)

<span class="status-badge status-active">Phase 5/8 (50%)</span>


A network automation framework that decouples network configuration from vendor-specific syntax. It uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model inspired by AutoNetKit.

The system enables cross-vendor configuration generation and validation through semantic simulation. Extract network-level topology relationships (protocol adjacencies, link roles, VLAN membership) from vendor-specific CLI and documentation with high accuracy, enabling truly vendor-independent network configuration.


### [Network Simulator](projects/network-simulator)

<span class="status-badge status-active">Phase 62/67 (100%)</span>
 · **Rust**


A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation.

Used for smoke testing and design validation of network configurations. Validate network configurations at scale with protocol-level fidelity before deploying to real infrastructure.


### [Network Topology Engine](projects/nte)

<span class="status-badge status-active">Stable</span>
 · **Rust (with PyO3 Python bindings)**


Graph operations on network topologies demand native performance — Python's NetworkX caps out on large topologies. The Network Topology Engine provides a Rust-native topology engine with Python bindings, giving the Network Modeling & Configuration Library the speed of compiled code with the ergonomics of Python.

The Network Topology Engine is the Rust backend that powers the Network Modeling & Configuration Library's graph operations. Originally embedded within the Network Modeling & Configuration Library as `ank_nte`, it has been extracted into its own repository as the engine matured and its scope grew beyond a simple backing store.


### [TopoGen - Network Topology Generator](projects/topogen)

<span class="status-badge status-active">Not started (defining requirements)</span>


A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters.

Outputs custom YAML format for use across the network engineering tool ecosystem. Network engineers can quickly generate realistic, validated network topologies without implementing complex algorithms from scratch.


### [ank_pydantic](projects/ank-pydantic)

<span class="status-badge status-active">Phase 84/89</span>


A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution.

Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module. A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.


## 📡 Software Defined Radio

> **[View Ecosystem →](/signal-processing)**
> Autonomous spectrum monitoring, distributed SIGINT systems, and RF signal processing.

### [Passive Radar - KrakenSDR Multi-Beam System](projects/passive)

<span class="status-badge status-active">Phase 7/10 (60%)</span>


A distributed multi-beam passive radar system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP.

All 4 surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.


### [Project Context: rtltcp-rust](projects/rtltcp)

<span class="status-badge status-active">Phase 5/6 (100%)</span>


A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.


### [Project Spectra](projects/signals)

<span class="status-badge status-active">Phase 7/7</span>


Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.


### [Wi-Fi Radar (KrakenSDR)](projects/wifi-radar)

<span class="status-badge status-active">Active Development</span>


Passive radar system that utilizes existing Wi-Fi signals for through-wall human detection and localization, leveraging the KrakenSDR coherent radio array.


## 🏥 Health & Biometrics

> **[View Ecosystem →](/agentic-systems)**
> Modular health monitoring ecosystems and real-time biometric signal processing.

### [HRV Monitor](projects/hrv)

<span class="status-badge status-active">Active Development</span>


Heart Rate Variability (HRV) reveals stress, recovery, and autonomic nervous system state through timing variations between heartbeats. Most consumer devices only report derived metrics without providing the underlying RR interval data needed for analysis.

This Rust-based driver connects directly to Bluetooth LE heart rate monitors, streams raw RR intervals in real-time, computes time-domain HRV metrics, and logs sessions to columnar Parquet files for downstream analysis.


### [HealthyPi Ecosystem](projects/healthypi)

<span class="status-badge status-active">** Phase 7 - Ingest CLI + HealthyPi 6 Serial MVP</span>


A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.


## 🔭 Astrophotography

### [AuroraData - Aurora Planning & Substorm Advisor](projects/auroradata)

<span class="status-badge status-active">** Not started</span>


A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.

Providing a single, definitive "Go/No-Go" score that accounts for both space weather potential and local terrestrial conditions (travel time, clouds, moon).


### [AuroraPhoto](projects/auroraphoto)

<span class="status-badge status-active">** Phase 1: Star Sharpness Foundation</span>


An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.

Provides precise, automated control over exposure and focus specifically optimized for aurora "bursts" and star sharpness, while offering field-ready composition tools.


### [EclipsePhoto](projects/eclipsephoto)

<span class="status-badge status-active">** 1 - Hardware & Data Foundation</span>


A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.

Reliability and autonomy for a "one-shot" astronomical event. The system handles guiding, exposure ramping (Holy Grail), and error recovery (watchdogs) so the photographer can experience the eclipse while the system secures the data.


### [EclipseStack](projects/eclipsestack)

<span class="status-badge status-active">** 1 (Ingestion & Foundation)</span>


EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data.

The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight. Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.


### [OpenAstro Core](projects/open-astro-core)

<span class="status-badge status-active">Active Development</span>


OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.


### [OpenAstro Node](projects/open-astro-node)

<span class="status-badge status-active">** 2. Control</span>


A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.


### [Satellites](projects/satellites)

<span class="status-badge status-active">Phase 4/6 (100%)</span>


A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm.

Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead. Real-time satellite positions rendered on a terminal world map with pass predictions — a single binary, no browser, no GUI dependencies.


## 📷 Photography

### [Photo Tour](projects/photo-tour)

<span class="status-badge status-active">Active Development</span>


Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.

In the field, you can see what the camera sees and get actionable guidance/control fast enough to improve the shot.


## 🤖 AI & Agents

> **[View Ecosystem →](/agentic-systems)**
> Security-first architectures for multi-agent coordination and isolated automation.

### [Cycle Agent](projects/cycle)

<span class="status-badge status-active">Phase 4/5 (71%)</span>


A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.


### [Secure Multi-Agent Personal Assistant](projects/multi-agent)

<span class="status-badge status-active">Phase 21/23 (100%)</span>
 · **Agents can be Go · Python · or Rust**


A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments.

The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic. Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.


## 📊 Data & Utilities

> **[View Ecosystem →](/data-analytics)**
> High-performance tools for large-scale geospatial analytics and time-series pattern discovery.

### [GSD Project Monitor](projects/devmon)

<span class="status-badge status-active">Stable</span>
 · **Python**


Developing...


### [OmniFocus DB CLI (omnifocus-db)](projects/omnifocus-db)

<span class="status-badge status-active">** Phase 7: Interactive Inbox Triage TUI — COMPLETE</span>


A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.

- **Zero-Latency Context:** Near-instant retrieval of projects and tasks without the overhead of the OmniFocus app or AppleScript. - **Agent-Optimized:** Focused on providing dense, low-token representations of the user's task list.

- **Safety First:** Read-only access by default to prevent database corruption while OmniFocus is active.


### [Tileserver Polars (Rust Optimized)](projects/tileserver)

<span class="status-badge status-active">Active Development</span>


Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.


### [Weather (BOM ACCESS Pipeline)](projects/weather)

<span class="status-badge status-active">Phase 2/4 (75%)</span>


A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.

The primary goal is to bypass the complexity of BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a clean, queryable interface (API/DuckDB) for localized weather insights, starting with South Australia.


### [cliscrape](projects/cliscrape)

<span class="status-badge status-active">Phase 6/11 (45%)</span>


`cliscrape` is a high-performance CLI scraping and parsing tool for network devices, written in Rust. It provides a modern, ergonomic, and blazingly fast alternative to legacy tools like `TextFSM`, while maintaining first-class compatibility with existing templates.

The one thing that must work perfectly: **Extremely fast, reliable parsing of semi-structured CLI output into structured data, regardless of whether the template is legacy TextFSM or the new ergonomic format.**


### [matrix-profile-rs](projects/matrix-time-series)

<span class="status-badge status-active">Phase 8/11 (64%)</span>


Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.

A high-performance Rust implementation of Matrix Profile algorithms for time series analysis with SIMD acceleration, out-of-memory tiling support, and Polars ecosystem integration. Matrix Profiles enable pattern discovery, anomaly detection, and similarity search in univariate time series without domain knowledge or parameter tuning.

**Performance at scale with ergonomic APIs** — achieve 2.5x speedup via SIMD, handle datasets larger than RAM via tiling, while maintaining simple `.motifs(k)` / `.discords(k)` interfaces.


### [nascleanup](projects/nascleanup)

<span class="status-badge status-active">Active Development</span>
 · **Rust**


Developing... A Rust-based CLI tool for deduplicating and organizing large file shares.

Optimized for Docker execution on DSM, it uses an indexing layer for fast file comparison and metadata management.


### [netflowsim](projects/netflowsim)

<span class="status-badge status-active">Phase 9/13 (0%)</span>


`netflowsim` provides rapid, massive-scale network performance analysis by using analytic queuing models and Monte Carlo simulations instead of packet-level discrete event simulation. It enables network engineers to validate topologies and routing strategies against billions of flow iterations in seconds, identify bottlenecks probabilistically, and test network resilience under failure scenarios.


## 🧘 Wellness & Sound

### [Psytrance Generator](projects/psytrance)

<span class="status-badge status-active">Phase 1/5 (0%)</span>


A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export.

Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently. Energy-driven generative music that sounds professional and lets users quickly explore variations.


### [Wave](projects/watch-noise)

<span class="status-badge status-active">v1.1 — Adaptive Audio Features</span>
 · **Swift (SwiftUI)**


- **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio
- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution **Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work.


### [Wave (StillState & FlowState)](projects/watchnoise)

<span class="status-badge status-active">26 (FlowState Hotkeys + Quick Actions)</span>


**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. - **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio.

- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution.


## 🧪 Experimental

### [ASIAIR Import Tool](projects/import-asiair)

<span class="status-badge status-active">Phase 1/1 (0%)</span>


A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.

Eliminates manual file sorting after imaging sessions - scan hundreds of frames, organize by target/filter/date, validate calibration frame availability, and go straight to PixInsight processing.


### [Network Automation Ecosystem - Overall Architecture Definition](projects/automationarch)

<span class="status-badge status-active">Phase 10/12</span>


This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.


### [Orchestrator (Device Interaction Runner)](projects/orchestrator)

<span class="status-badge status-active">Phase 1/5 (0%)</span>


An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.

Run the same device workflow reliably across lab/real targets, with deterministic execution semantics and replayable artifacts.


### [Rust TUI GTD Todo (OmniFocus-inspired)](projects/todo)

<span class="status-badge status-active">Phase 5/7 (71%)</span>


A fast, keyboard-driven Rust text UI (TUI) task manager inspired by OmniFocus, built around a GTD workflow. It stores data in an owned SQLite database, supports projects and hierarchical contexts/tags, and is optimized for rapid inbox processing (triage + tagging) with minimal friction.

Process an inbox full of captures into correctly-organized next actions (project + tags + defer/due) at high speed, with sub-second interactions.


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