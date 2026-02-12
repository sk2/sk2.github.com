# Projects

My work focuses on network automation tools, signal processing systems, and multi-agent architectures.

---

## 🌐 Network Engineering

> **[View Network Automation Ecosystem →](/network-automation)**
> Tools for topology modeling, deterministic protocol simulation, and high-performance visualization.

### [ANK Workbench](projects/ank-workbench)
<span class="status-badge status-active">Phase 18/19 (98%)</span>
A unified network simulation and visualization platform for enterprise network engineers. ANK Workbench integrates existing ANK Pydantic models, simulator, and visualization components into a seamless end-to-end workflow.

### [AutoNetkit](projects/autonetkit)
<span class="status-badge status-active">PhD 2017</span>
The original compiler-based network automation tool.

### [NetVis](projects/netvis)
<span class="status-badge status-active">Active Development</span>
A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity.

### [Network Simulator](projects/network-simulator)
<span class="status-badge status-active">Active Development</span>
A Rust-based network simulator that models packet-level behavior for routing protocols. Validate network configurations at scale with protocol-level fidelity before deploying to real infrastructure.

### [TopoGen - Network Topology Generator](projects/topogen)
<span class="status-badge status-active">Phase 18/24 (15%)</span>
A Rust-based network topology generator that generates realistic data center, WAN, and random graph topologies with proper structure and design patterns.

### [ank_pydantic](projects/ank-pydantic)
<span class="status-badge status-active">Phase 59/62 (100%)</span>
A Python library for modeling and querying network topologies, backed by a high-performance Rust core. Features a two-stage transformation model and a composable lazy query API.

---

## 📡 Signal Processing & RF

> **[View Signal Processing Ecosystem →](/signal-processing)**
> Experimental projects exploring SDR spectrum monitoring and biometric signal processing.

### [Passive Radar - KrakenSDR Multi-Beam System](projects/passive)
<span class="status-badge status-active">Phase 3/4 (100%)</span>
A multi-beam passive radar system based on KrakenSDR hardware, extending an abandoned prototype to reliably track aircraft.

### [Project Spectra](projects/signals)
<span class="status-badge status-active">Active Development</span>
Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.

### [Wi-Fi Radar](projects/wifi-radar)
<span class="status-badge status-active">Active Development</span>
Passive radar system that utilizes existing Wi-Fi signals for through-wall human detection and localization.

### [rtltcp-rust](projects/rtltcp)
<span class="status-badge status-active">Active Development</span>
A high-performance, multi-threaded Rust implementation of the `rtl_tcp` protocol with concurrent multi-device support.

### [HealthyPi Ecosystem](projects/healthypi)
<span class="status-badge status-active">Active Development</span>
A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware into actionable insights.

---

## 🤖 AI & Agents

> **[View Agentic Systems Ecosystem →](/agentic-systems)**
> Security-first multi-agent architectures for personal and infrastructure automation.

### [Cycle Agent](projects/cycle)
<span class="status-badge status-active">Phase 1/5 (80%)</span>
A native SwiftUI training application that bridges professional cycling hardware with dynamic AI-driven workout logic via NATS.

### [Multi-Agent Assistant](projects/multi-agent)
<span class="status-badge status-active">Phase 18/20 (83%)</span>
A security-first multi-agent system that coordinates specialized containerized agents through a message broker architecture with strict isolation.

---

## 📊 Data Science & Simulation

> **[View Data Analytics Ecosystem →](/data-analytics)**
> High-performance tools for processing massive datasets and discovering patterns in time series.

### [matrix-profile-rs](projects/matrix-time-series)
<span class="status-badge status-active">Phase 2/5 (16%)</span>
A high-performance Rust implementation of Matrix Profile algorithms for pattern discovery, anomaly detection, and similarity search in time series.

### [netflowsim](projects/netflowsim)
<span class="status-badge status-active">Active Development</span>
Rapid, massive-scale network performance analysis using analytic queuing models and Monte Carlo simulations.

### [Tileserver Polars](projects/tileserver)
<span class="status-badge status-active">Active Development</span>
Serve dynamic vector tiles (MVT) from massive geospatial datasets with sub-second latency using Polars.

---

## 🔭 Astrophotography

### [ASIAIR Import Tool](projects/import-asiair)
<span class="status-badge status-active">Phase 1/1 (0%)</span>
Automates post-imaging-session file organization for astrophotography.

### [OpenAstro Core](projects/open-astro-core)
<span class="status-badge status-active">Active Development</span>
High-performance Rust library providing shared astronomical logic and hardware drivers.

### [OpenAstro Node](projects/open-astro-node)
<span class="status-badge status-active">Active Development</span>
A headless, autonomous astrophotography controller designed for low-power Linux devices.

---

## 📷 Photography

### [Photo Tour](projects/photo-tour)
<span class="status-badge status-active">Active Development</span>
A smart, interactive photography assistant designed for field use.

---

## 🌊 Wellness & Sound

### [WatchNoise](projects/watchnoise)
<span class="status-badge status-active">v1.1 Shipped</span>
An Apple Watch sleep sounds application featuring adaptive audio and HealthKit integration.

### [Wave](projects/watch-noise)
<span class="status-badge status-active">Active Development</span>
An evolutionary ambient audio ecosystem designed to manage the user's sensory environment.

---

## 🛠️ Utilities

### [nascleanup](projects/nascleanup)
<span class="status-badge status-active">Active Development</span>
A Rust-based CLI tool for deduplicating and organizing large file shares, optimized for Docker on DSM.

<style>
.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }
.status-active { background-color: #e7f3ff; color: #007bff; border: 1px solid #cce5ff; }
.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
h3 { margin-bottom: 0.2em; }
h3 + .status-badge { margin-top: 0; }
section { margin-bottom: 2em; }
blockquote { margin: 1em 0; padding: 0.5em 1em; border-left: 4px solid #007bff; background: #f8f9fa; }
</blockquote >