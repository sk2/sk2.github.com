---
layout: default
---

# Projects

My work focuses on network automation, signal processing, and multi-agent systems.

---

## Network Engineering

### [NetVis](projects/netvis)
<span class="status-badge status-complete">Production Ready</span>

Network topology visualization library for Rust. Force-directed, hierarchical, and radial layouts. 582 tests passing.

**Stack:** Rust · petgraph · SVG/PNG/PDF

---

### [ank-pydantic](projects/ank-pydantic)
<span class="status-badge status-active">Active</span>

Type-safe network topology modeling with Pydantic and Rust-backed graph engine. Multi-vendor config generation for 11+ platforms.

**Stack:** Python · Rust (PyO3) · Pydantic · petgraph

---

### [ANK Workbench](projects/ank-workbench)
<span class="status-badge status-active">v1.1 Complete</span>

Unified network simulation and visualization platform. Declarative design with lightweight mathematical simulation.

**Stack:** Python (FastAPI) · React · TypeScript

---

### [TopoGen](projects/topogen)
<span class="status-badge status-active">v0.10</span>

Network topology generator with CLI, Python API, and config-driven interfaces. Data center, WAN, and random graph topologies.

**Stack:** Rust · Python (PyO3)

---

### [netsim](projects/netsim)
<span class="status-badge status-active">Active</span>

Deterministic network protocol simulator. Implements OSPF, IS-IS, BGP, MPLS/LDP, BFD, GRE, VRF.

**Stack:** Rust · Python bindings

---

## Geospatial & Visualization

### [Vector Tile Server](projects/tileserver)
<span class="status-badge status-planning">Planning</span>

High-performance MVT server for dynamic vector tiles from large datasets. Datashader-like aggregation with sub-second latency.

**Stack:** Python (FastAPI) · Rust (PyO3) · Polars · Kepler.gl

---

## Signal Processing & Hardware

### [Astro](projects/astro)
<span class="status-badge status-planning">Planning</span>

Open-source astrophotography control system for Linux/Raspberry Pi. Alternative to ZWO ASIAir.

**Stack:** Rust

---

### [HealthyPi Ecosystem](projects/healthypi)
<span class="status-badge status-active">Phase 4/6 (88%)</span>

Biometric data processing ecosystem with virtual patient simulator and real-time analysis engine.

**Stack:** Python · NATS · NeuroKit2 · NumPy

---

### [Project Spectra](projects/spectra)
<span class="status-badge status-planning">Planning</span>

Autonomous radio spectrum monitoring with ML-based signal classification. Edge SDRs to Mac mini core.

**Stack:** Python · Rust · Swift · ML

---

## Personal Apps

### [WatchNoise](projects/watchnoise)
<span class="status-badge status-active">v1.1 Shipped</span>

Apple Watch sleep sounds app with adaptive audio. Frequency calibration, heartbeat sync, and environmental noise monitoring.

**Stack:** Swift (SwiftUI) · watchOS · Procedural Audio

---

## AI & Agents

### [Multi-Agent Assistant](projects/multi-agent)
<span class="status-badge status-active">Active</span>

Security-first multi-agent system with containerized agents and capability-based authorization.

**Stack:** Python · Docker · NATS · Swift · OpenTelemetry

[GitHub](https://github.com/sk2/multi-agent-assistant)

---

### [Cycle Agent](projects/cycle-agent)
<span class="status-badge status-planning">Planning</span>

SwiftUI training app connecting KICKR Core to AI-driven workout logic via NATS.

**Stack:** SwiftUI · SceneKit · FTMS (BLE) · NATS

---

## Legacy

### [AutoNetkit](projects/autonetkit)
<span class="status-badge status-complete">PhD 2017</span>

Network configuration automation tool from PhD research. Used in Cisco's VIRL project.

**Stack:** Python

---

**Development:** [Philosophy and approach](development)
