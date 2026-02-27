---
layout: default
---

# Projects

Focused on network engineering, autonomous systems, and signal processing.

---

## 🌐 Network Engineering

### [Network Simulator](projects/netsim)

<span class="status-badge status-active">Active</span>


Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.


### [Configuration Generation (AutoNetkit)](projects/autonetkit)

<span class="status-badge status-active">Active</span>


A compiler-based framework for automated network provisioning. AutoNetkit transforms high-level network designs into validated device configurations across heterogeneous hardware and protocol environments.


### [Network Compilation Engine](projects/compilation)

<span class="status-badge status-active">Active</span>


A native Rust-based configuration compiler that serves as a fast alternative to the Python-based modeling engine. While sharing the same underlying data models and 'Whiteboard -> Build' philosophy, this tool is built for maximum execution speed and formal verification during the compilation process.


### [Configuration Engine (netC)](projects/netC)

<span class="status-badge status-active">Active</span>


A modern, type-safe configuration engine that serves as a successor and sibling to the original AutoNetkit research. It implements the same 'Whiteboard -> Plan -> Build' transformation model but utilizes a modern, schema-enforced pipeline to ensure configuration correctness across heterogeneous network fleets.


### [Brownfield Ingestion & Analysis](projects/configparsing)

<span class="status-badge status-active">Active</span>


A specialized framework for **Brownfield Ingestion and Analysis**. It extracts high-level architectural intent and topology relationships from legacy network state—including vendor-specific CLI configurations and unstructured PDF documentation—normalizing them into a vendor-neutral model.


### [Network Visualization Engine](projects/netvis)

<span class="status-badge status-active">Active</span>


Network visualization often fails at scale because layout algorithms treat all nodes and edges equally, producing cluttered "hairball" diagrams. The **Network Visualization Engine** treats topologies as hierarchical structures and uses domain-aware layout constraints—including isometric views and edge bundling—to reflect engineering intent.


### [Topology Engine Core](projects/ank-nte)

<span class="status-badge status-active">Active</span>


The fast graph core that powers the ANK ecosystem. NTE (Network Topology Engine) provides a native Rust implementation of multi-layer network graphs, optimized for low-latency queries and complex topological transformations.


### [Topology Generator](projects/topogen)

<span class="status-badge status-active">Active</span>


A Rust-based topology generation engine that consolidates complex network graph algorithms into a unified, fast library. It enables the creation of realistic, validated network structures ranging from small lab setups to massive data center and backbone environments.


### [Automation Workbench](projects/ank-workbench)

<span class="status-badge status-active">Active</span>


**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow. It serves as the **glue layer** that coordinates the entire network automation pipeline, allowing engineers to generate topologies, model networks declaratively, run lightweight simulations, and visualize results from a unified interface.


### [CLI Parser](projects/cliscrape)

<span class="status-badge status-active">Active</span>


A fast parsing engine for network device output. It transforms semi-structured CLI text into structured data (JSON/YAML) using an optimized state machine. Designed as a modern, ergonomic alternative to legacy tools like TextFSM, it provides significantly faster execution while maintaining full compatibility with existing template libraries.


### [Performance Simulator](projects/netflowsim)

<span class="status-badge status-active">Active</span>


A performance analysis engine that utilizes analytic queuing models and Monte Carlo simulations to validate network capacity at scale. Unlike packet-level simulators, netflowsim focuses on probabilistic outcomes across billions of traffic flows.


### [Network Modeling Foundations](projects/autonetkit-foundation)

<span class="status-badge status-active">Active</span>


The original research that established the principles of automated network configuration. This work introduced the **Whiteboard → Plan → Build** transformation model, which allows engineers to work with high-level design abstractions while the system handles the technical implementation details.


### [Network Modeling & Configuration Library](projects/ank-pydantic)

<span class="status-badge status-active">Active</span>


A Python-native configuration engine for defining a network model and compiling it into a consistent, reviewable plan. It solves the 'type safety vs performance' problem by combining the ergonomics of Pydantic models with a fast Rust graph core (NTE).


### [Device Interaction Framework](projects/deviceinteraction)

<span class="status-badge status-active">Active</span>


A fast, simple, and ergonomic Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities—testbed management, CLI parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit.


### [Network Automation Ecosystem - Overall Architecture Definition](projects/automationarch)

<span class="status-badge status-active">Active</span>


This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.


## 📡 Radio Systems

### [Project Spectra](projects/spectra)

<span class="status-badge status-active">Active</span>


Developing...


### [SDR Streaming Server](projects/rtltcp)

<span class="status-badge status-active">Active</span>


A single Rust binary that auto-detects every connected SDR, streams each over the standard `rtl_tcp` protocol, and provides a TUI dashboard and HTTP API for monitoring and control — designed for headless Raspberry Pi deployment.


### [Signal Reflection - KrakenSDR Multi-Beam System](projects/rf-signal-analysis)

<span class="status-badge status-active">Active</span>


A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.


### [Spectrum Analysis](projects/signals)

<span class="status-badge status-active">Active</span>


Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.


### [Wi-Fi Radar (KrakenSDR)](projects/wifi-signal-analysis)

<span class="status-badge status-active">Active</span>


Signal reflection system that utilizes existing Wi-Fi signals for through-wall human detection and localization, leveraging the KrakenSDR coherent radio array.


## 🤖 Autonomous Systems

### [Secure Multi-Agent Personal Assistant](projects/multi-agent)

<span class="status-badge status-active">Active</span>


Multi-agent coordination requires strict security boundaries to prevent lateral movement. This assistant demonstrates **containerized isolation** where agents (HealthKit, Home Automation, etc.) coordinate via a NATS message broker. By using per-subject ACLs and a "deny-by-default" security posture, the system ensures that compromise of a single agent cannot cascade through the infrastructure.


### [HRV Monitor](projects/hrv)

<span class="status-badge status-active">Active</span>


Developing...


### [Cycle Agent](projects/cycle)

<span class="status-badge status-active">Active</span>


A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a fast SceneKit environment.


### [HealthyPi Ecosystem](projects/healthypi)

<span class="status-badge status-active">Active</span>


A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.


## 🧪 Experimental

### [matrix-profile-rs](projects/matrix-time-series)

<span class="status-badge status-active">Active</span>


Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.


### [GSD Project Monitor](projects/devmon)

<span class="status-badge status-active">Active</span>


Developing...


### [Network Topology Engine](projects/nte)

<span class="status-badge status-active">Active</span>


Graph operations on network topologies demand native performance — Python's NetworkX caps out on large topologies. The Network Topology Engine provides a Rust-native topology engine with Python bindings, giving the Network Modeling & Configuration Library the speed of compiled code with the ergonomics of Python.


### [OpenAstro Core](projects/open-astro-core)

<span class="status-badge status-active">Active</span>


OpenAstro Core is a fast Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.


### [Wave (StillState & FlowState)](projects/watchnoise)

<span class="status-badge status-active">Active</span>





### [nascleanup](projects/nascleanup)

<span class="status-badge status-active">Active</span>


Developing...


### [Network Configuration Parser](projects/ank-parse)

<span class="status-badge status-active">Active</span>


Developing...


### [Orchestrator (Device Interaction Runner)](projects/orchestrator)

<span class="status-badge status-active">Active</span>


An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.


### [Test Project](projects/test-project)

<span class="status-badge status-active">Active</span>


This is a test project concept from external source.


### [Wave (StillState & FlowState)](projects/watch-noise)

<span class="status-badge status-active">Active</span>


**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work.


### [OmniFocus DB CLI (omnifocus-db)](projects/omnifocus-db)

<span class="status-badge status-active">Active</span>


A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.


### [Photo Tour](projects/photo-tour)

<span class="status-badge status-active">Active</span>


Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.


### [ASIAIR Import Tool](projects/import-asiair)

<span class="status-badge status-active">Active</span>


A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.


### [Aurora Advisor](projects/auroradata)

<span class="status-badge status-active">Active</span>


A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.


### [AuroraPhoto](projects/auroraphoto)

<span class="status-badge status-active">Active</span>


An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.


### [EclipsePhoto](projects/eclipsephoto)

<span class="status-badge status-active">Active</span>


A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.


### [EclipseStack](projects/eclipsestack)

<span class="status-badge status-active">Active</span>


EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.


### [Psytrance Generator](projects/psytrance)

<span class="status-badge status-active">Active</span>


A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently.


### [Satellites](projects/satellites)

<span class="status-badge status-active">Active</span>


A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm. Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead.


### [Sound Array](projects/soundarray)

<span class="status-badge status-active">Active</span>


An exploration-focused audio processing system using Raspberry Pi and microphone arrays. It focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.


### [Weather (BOM ACCESS Pipeline)](projects/weather)

<span class="status-badge status-active">Active</span>


A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.


### [OpenAstro Node](projects/open-astro-node)

<span class="status-badge status-active">Active</span>


A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.


### [Tileserver Polars (Rust Optimized)](projects/tileserver)

<span class="status-badge status-active">Active</span>


Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.


<style>
.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }
.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }
section { margin-bottom: 2em; }
</style>