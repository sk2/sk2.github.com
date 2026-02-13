---
layout: default
---

# Projects

Focusing on network automation, high-performance signal processing, and secure multi-agent architectures.

---

## 🌐 Network Engineering

> **[View Network Automation Ecosystem →](/network-automation)**
> High-performance tools for topology modeling, deterministic protocol simulation, and visualization.

### [ANK Workbench](projects/ank-workbench)
<span class="status-badge status-active">Phase 18/19 (98%)</span>
A unified orchestration and visualization platform for enterprise network designs. Integrates topology modeling, simulation, and visualization into a single deterministic workflow.

### [ank_pydantic](projects/ank-pydantic)
<span class="status-badge status-active">Phase 59/62 (100%)</span>
Type-safe topology modeling with a high-performance Rust core. Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers) and a composable lazy query API.

### [Network Simulator](projects/network-simulator)
<span class="status-badge status-active">Active Development</span>
A deterministic, tick-based Rust simulator for protocol validation. Provides protocol-level fidelity (OSPF, BGP, IS-IS) at a fraction of the footprint of full emulation.

### [NetVis](projects/netvis)
<span class="status-badge status-active">Active Development</span>
A Rust-based topology layout engine. Transforms complex multi-layer network graphs into information-dense, publication-quality visualizations through automated layout algorithms.

### [TopoGen](projects/topogen)
<span class="status-badge status-active">Phase 18/24 (15%)</span>
Automated generation of realistic data center and WAN topologies using structural design patterns and graph algorithms.

### [AutoNetkit](projects/autonetkit)
<span class="status-badge status-active">PhD 2017</span>
The original compiler-based network automation tool. Introduced declarative network design via the Whiteboard → Plan → Build model.

---

## 📊 Data Science & Simulation

> **[View Data Analytics Ecosystem →](/data-analytics)**
> High-performance tools for large-scale geospatial analytics and time-series pattern discovery.

### [AuroraData](projects/auroradata)
<span class="status-badge status-active">Active Development</span> · **TypeScript**
Aurora planning advisor for Australian observers. Combines real-time NOAA space weather (solar wind, hemispheric power), ACCESS-G local weather forecasts, and travel time logic to provide actionable "Go/No-Go" recommendations for aurora observation sites.

### [matrix-profile-rs](projects/matrix-time-series)
<span class="status-badge status-active">Phase 2/5 (50%)</span>
Native Rust implementation of Matrix Profile algorithms. Guarantees discovery of motifs and anomalies in univariate time series without domain-specific parameter tuning.

### [Tileserver Polars](projects/tileserver)
<span class="status-badge status-active">Active Development</span>
Dynamic vector tile (MVT) generation directly from Polars DataFrames. Enables interactive visualization of millions of geospatial points with sub-second latency.

### [Traffic Simulator](projects/netflowsim)
<span class="status-badge status-active">Active Development</span>
Massive-scale network performance analysis using analytic queuing models and Monte Carlo simulations.

### [Weather (BOM ACCESS Pipeline)](projects/weather)
<span class="status-badge status-planning">Planning</span>
Data engineering pipeline to fetch, process, and serve high-resolution weather model data using Polars for high-performance processing.

---

## 🤖 AI & Agents

> **[View Agentic Systems Ecosystem →](/agentic-systems)**
> Security-first architectures for multi-agent coordination and isolated automation.

### [Multi-Agent Assistant](projects/multi-agent)
<span class="status-badge status-active">Phase 18/20 (84%)</span>
A secure framework for coordinating specialized, containerized agents. Focuses on capability-based security, strict isolation via NATS, and comprehensive audit trails.

### [Cycle](projects/cycle)
<span class="status-badge status-active">Phase 1/5 (80%)</span>
Native SwiftUI training application bridging professional cycling hardware with dynamic AI-driven workout logic via NATS.

---

## 📡 Signal Processing & RF

> **[View Signal Processing Ecosystem →](/signal-processing)**
> SDR spectrum monitoring and biometric signal processing using modular acquisition pipelines.

### [Project Spectra](projects/signals)
<span class="status-badge status-active">Active Development</span>
Automated spectrum monitoring that transforms raw radio data into an actionable Signal Census through ML-based detection and classification.

### [Illumination Reflection Tracking](projects/passive)
<span class="status-badge status-active">Phase 3/4 (100%)</span>
Multi-beam signal reflection analysis system using coherent SDR hardware and broadcast transmissions for spatial tracking.

### [rtltcp-rust](projects/rtltcp)
<span class="status-badge status-active">Active Development</span>
High-performance Rust implementation of the `rtl_tcp` protocol with concurrent multi-device support.

### [Wi-Fi Radar](projects/wifi-radar)
<span class="status-badge status-active">Active Development</span>
Through-wall human detection and localization using existing Wi-Fi signal reflections analyzed via coherent SDR arrays.

---

## 🔭 Experimental & Hobbies

Projects in exploratory phases or related to technical hobbies.

### [OpenAstro Core](projects/open-astro-core)
Rust library for astronomical coordinate math and device protocol consistency across the OpenAstro ecosystem.

### [Wave](projects/watch-noise)
<span class="status-badge status-active">v1.1 Shipped</span>
Adaptive audio synthesis for Apple Watch, integrating real-time synthesis with HealthKit biometric feedback.

### [nascleanup](projects/nascleanup)
Rust-based indexing and deduplication for large file shares, optimized for resource-constrained NAS environments.

### [OmniFocus DB CLI](projects/omnifocus-db)
<span class="status-badge status-planning">Planning</span> · **Python**
High-performance CLI for direct OmniFocus 4 SQLite database access. Provides near-instant retrieval of projects and tasks in token-efficient formats optimized for AI agent context, bypassing slow AppleScript layers with ~200x performance improvement.

### [Photo Tour](projects/photo-tour)
Interactive photography assistant focusing on composition and automated capture workflows.

### [soundarray](projects/soundarray)
Microphone array-based spatial audio processing on Raspberry Pi for beamforming and sound localization.

### [AuroraPhoto](projects/auroraphoto)
Automated aurora photography system using Raspberry Pi nodes and intelligent capture sequencing.

<style>
.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }
.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }
.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
h3 { margin-bottom: 0.1em; }
h3 + .status-badge { margin-top: 0; }
section { margin-bottom: 2em; }
blockquote { margin: 1em 0; padding: 0.5em 1em; border-left: 2px solid #495057; background: #f8f9fa; font-style: normal; font-size: 0.9em; }
</style>
