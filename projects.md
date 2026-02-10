---
layout: default
---

# Projects

My work focuses on network automation tools, signal processing systems, and multi-agent architectures.

---

## Network Engineering

### WatchNoise

<span class="status-badge status-active">Phase 6/7 (100%)</span>

An Apple Watch app that generates ambient noise (white noise, brown noise, and a blended option) for sleeping through Bluetooth headphones. The app prioritizes simplicity with a single play/pause button on the main screen and noise type selection in settings. When headphones disconnect, playback automatically pauses.

---

### ank_pydantic

<span class="status-badge status-active">Phase 58/62 (99%)</span>

A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.

**Stack:** Python · Rust · FastAPI

---

### ank_workbench

<span class="status-badge status-active">Active Development</span>

A unified network simulation and visualization platform for enterprise network engineers. ANK Workbench integrates existing ANK Pydantic models, simulator, and visualization components into a seamless end-to-end workflow. Engineers can design networks declaratively, run lightweight simulations, and visualize topology, configuration state, and simulation results in one integrated environment. Built as a commercial product offering a modern alternative to traditional emulation-based tools like GNS3 and Cisco Modeling Labs.

**Stack:** Python backend (FastAPI or Flask) · React or Vue frontend — Leverages existing Python ecosystem for ANK components · meets modern UX expectations

---

### nascleanup

<span class="status-badge status-active">Active Development</span>

---

### netvis

<span class="status-badge status-active">Active Development</span>

A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.

**Stack:** Python · Rust

---

### network-simulator

<span class="status-badge status-active">Active Development</span>

A Rust-based network simulator that models packet-level behavior for routing protocols. It provides a middle ground between pure algorithmic analysis (like C-BGP) and full emulation (like Containerlab) — larger scale and smaller footprint than emulation, higher fidelity than algorithmic simulation. Used for smoke testing and design validation of network configurations.

**Stack:** Python

---

### photo-tour

<span class="status-badge status-active">Active Development</span>

Photo Tour is a smart, interactive photography assistant designed for field use.
It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.

---

### tileserver

<span class="status-badge status-active">Active Development</span>

Serve dynamic vector tiles (MVT) from massive geospatial datasets (millions of points) with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets.

---

### topogen

<span class="status-badge status-active">Phase 13/15 (87%)</span>

A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters. Outputs custom YAML format for use across the network engineering tool ecosystem.

**Stack:** Python

---

## Signal Processing & Hardware

### healthypi

<span class="status-badge status-complete">Production Ready</span>

A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.

**Current:** 2026-02-10 - Completed 04-07-PLAN.md (Health Context trend window + prompt formatting)

---

### open-astro-core

<span class="status-badge status-active">Active Development</span>

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.
It exists to keep coordinate math and device/protocol behavior consistent across downstream OpenAstro apps.

---

### open-astro-node

<span class="status-badge status-active">Active Development</span>

A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.

---

### signals

<span class="status-badge status-complete">Production Ready</span>

Transform raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition.

---

## AI & Agents

### cycle

<span class="status-badge status-active">Phase 1/5 (20%)</span>

A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.

---

### multi-agent-assistant

<span class="status-badge status-active">Phase 17/20 (79%)</span>

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

**Stack:** Rust · NATS

---

## Development Approach

I plan work in `.planning/` directories with phase-based execution. I verify completeness with formal documents. I use NATS for message coordination. I write comprehensive tests. I document architecture decisions in PROJECT.md and STATE.md.
