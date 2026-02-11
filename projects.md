---
layout: default
---

# Projects

My work focuses on network automation tools, signal processing systems, and multi-agent architectures.

---

## Network Engineering

> **[View Network Automation Ecosystem →](network-automation)**
> Explore the complete network automation toolchain — from topology modeling to protocol simulation to visualization. See how the tools integrate and work together.

---

### [ANK Workbench](projects/ank-workbench)

<span class="status-badge status-active">Phase 18/19 (98%)</span>
 · **Python backend (FastAPI or Flask) · React or Vue frontend — Leverages existing Python ecosystem for ANK components · meets modern UX expectations**


A unified network simulation and visualization platform for enterprise network engineers. ANK Workbench integrates existing ANK Pydantic models, simulator, and visualization components into a seamless end-to-end workflow.

Network engineers can design, validate, and visualize network changes in one complete workflow without switching between separate tools or manually gluing components together.


### [AutoNetkit](projects/autonetkit)

<span class="status-badge status-active">PhD 2017</span>
 · **Python**



### [NetVis](projects/netvis)

<span class="status-badge status-active">Active Development</span>


A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity.

Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling. Transform network topologies into clear, information-dense visualizations using algorithms that minimize edge crossings, bundle related connections, and respect hierarchical/geographic structure — enabling understanding of networks that would otherwise be visual noise.


### [Network Simulator](projects/network-simulator)

<span class="status-badge status-active">Active Development</span>


A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation.

Used for smoke testing and design validation of network configurations. Validate network configurations at scale with protocol-level fidelity before deploying to real infrastructure.


### [TopoGen - Network Topology Generator](projects/topogen)

<span class="status-badge status-active">Phase 17/24 (11%)</span>


A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters.

Outputs custom YAML format for use across the network engineering tool ecosystem. Network engineers can quickly generate realistic, validated network topologies without implementing complex algorithms from scratch.


### [ank_pydantic](projects/ank-pydantic)

<span class="status-badge status-active">Phase 59/62 (99%)</span>


A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution.

Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module. A clean, consistent API where there's one obvious way to perform each topology operation — predictable naming, return types, and method signatures across the entire public surface.


## Signal Processing & SDR

> **[View Signal Processing & RF Ecosystem →](signal-processing)**
> Explore real-time biometric analysis, passive radar systems, and RF spectrum monitoring. Transform raw sensor data into actionable intelligence.

---

### [HealthyPi Ecosystem](projects/healthypi)

<span class="status-badge status-active">Active Development</span>


A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.


### [Passive Radar - KrakenSDR Multi-Beam System](projects/passive)

<span class="status-badge status-active">Phase 2/4 (56%)</span>


A multi-beam passive radar system based on KrakenSDR hardware, extending an abandoned prototype to reliably track aircraft. Currently focused on establishing a clean, stable foundation before adding advanced multi-beam correlation capabilities.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.


### [Project Spectra](projects/signals)

<span class="status-badge status-active">Active Development</span>


Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.


### [Wi-Fi Radar](projects/wifi-radar)

<span class="status-badge status-active">Active Development</span>


Passive radar system that utilizes existing Wi-Fi signals for through-wall human detection and localization, leveraging the KrakenSDR coherent radio array.


## Astrophotography

### [ASIAIR Import Tool](projects/import-asiair)

<span class="status-badge status-active">Phase 1/1 (0%)</span>


A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.

Eliminates manual file sorting after imaging sessions - scan hundreds of frames, organize by target/filter/date, validate calibration frame availability, and go straight to PixInsight processing.


### [OpenAstro Core](projects/open-astro-core)

<span class="status-badge status-active">Active Development</span>


OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

Downstream apps can rely on correct, consistent coordinate math and device/protocol primitives.


### [OpenAstro Node](projects/open-astro-node)

<span class="status-badge status-active">Active Development</span>


A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.


## Photography

### [Photo Tour](projects/photo-tour)

<span class="status-badge status-active">Active Development</span>


Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.

In the field, you can see what the camera sees and get actionable guidance/control fast enough to improve the shot.


## AI & Agents

> **[View Agentic Systems Ecosystem →](agentic-systems)**
> Explore security-first multi-agent architectures with 13+ specialized agents. Container isolation, capability-based authorization, and comprehensive audit trails.

---

### [Cycle Agent](projects/cycle)

<span class="status-badge status-active">Phase 1/5 (80%)</span>


A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.


### [Multi-Agent Assistant](projects/multi-agent)

<span class="status-badge status-active">Phase 17/20 (79%)</span>


A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments.

The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic. Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.


## Data & Utilities

> **[View Data Analytics & Visualization Ecosystem →](data-analytics)**
> Explore high-performance tools for geospatial analytics and time series pattern discovery. Process millions of rows interactively with Polars-native implementations.

---

### [Tileserver Polars](projects/tileserver)

<span class="status-badge status-active">Active Development</span>


Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.


### [matrix-profile-rs](projects/matrix-time-series)

<span class="status-badge status-active">Phase 2/5 (16%)</span>
 · **Rust · ndarray · rayon · Polars integration planned**


A high-performance Rust implementation of Matrix Profile algorithms for time series analysis. Enables pattern discovery (motifs), anomaly detection (discords), and similarity search in univariate time series with native performance and Polars integration.

Provides production-quality implementations of STOMP, SCAMP, and SCRIMP++ algorithms with clean APIs (`.motifs(k=3)`) and seamless DataFrame operations for time series pattern analysis.


### [nascleanup](projects/nascleanup)

<span class="status-badge status-active">Active Development</span>
 · **Rust**


A Rust-based CLI tool for deduplicating and organizing large file shares. Optimized for Docker execution on DSM, it uses an indexing layer for fast file comparison and metadata management.


## Wellness & Sound

### [WatchNoise](projects/watchnoise)

<span class="status-badge status-active">v1.1 Shipped</span>
 · **Swift (SwiftUI)**


An Apple Watch sleep sounds application featuring adaptive audio. It uses a custom audio unit graph for real-time synthesis and integrates with HealthKit for heart rate synchronization.


### [Wave](projects/watch-noise)

<span class="status-badge status-active">Active Development</span>


**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. - **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio.

- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution.


<style>
.status-badge { display: inline-block; padding: 0.3em 0.8em; margin: 0.5em 0; border-radius: 4px; font-size: 0.85em; font-weight: 600; }
.status-active { background-color: #007bff; color: white; }
.status-planning { background-color: #ffc107; color: #343a40; }
</style>