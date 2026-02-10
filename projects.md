---
layout: default
---

# Projects

My work spans AI agents, network engineering, and signal processing. I build systems that balance security, performance, and systematic development.

---

## AI & Agents

### Secure Multi-Agent Personal Assistant

<span class="status-badge status-active">Active Development</span>

A multi-agent system where specialized agents run in isolated containers and communicate through a message broker. Each agent validates capability-based authorization tokens before executing actions.

**Stack:** Python, Docker, NATS, Swift, OpenTelemetry

**Architecture:**
- Containerized agents with seccomp, read-only filesystem, no-new-privileges
- NATS broker with TLS 1.3 and per-subject ACLs
- Short-lived capability tokens with nonce validation
- SQLite audit trail and OpenTelemetry traces

**Agents:** health monitoring (HealthKit), home automation (Hue), data aggregation (calendar/weather/RSS), backup integrity

[GitHub](https://github.com/sk2/multi-agent-assistant)

---

### HealthyPi Ecosystem

<span class="status-badge status-active">Phase 4/6 (88%)</span>

Translates HealthyPi hardware biometric data (ECG, PPG, EDA, EEG, IMU) into insights through agentic intelligence.

**Stack:** Python, NATS, PyArrow, NeuroKit2, NumPy

**Features:**
- Virtual Patient simulator with NeuroKit2 signal generation
- HRV analysis (time/frequency domain), EDA stress detection
- 286 tests, 6 physiological state scenarios
- NATS integration with Multi-Agent framework

**Status:** Foundation ✅ | Virtual Patient ✅ | Analysis Engine ✅ | Agent Integration 🔄

---

### Project Spectra

<span class="status-badge status-planning">Planning</span>

Autonomous radio spectrum monitoring with ML-based signal classification and spatial RF mapping.

**Stack:** Python, Rust, Swift, ML

**Hardware:**
- Edge: Airspy R2, HF Discovery, KrakenSDR (5-ch DoA), RTL-SDR
- Core: Mac mini M-Series (ML inference, visualization)

**Features:** Real-time waterfall, modulation detection, satellite tracking, ADS-B integration

---

### Cycle Agent

<span class="status-badge status-planning">Planning</span>

SwiftUI training app connecting KICKR Core to AI-driven workout logic via NATS.

**Stack:** SwiftUI, SceneKit, FTMS (BLE), NATS

**Design:** Low-latency BLE control, agent-coordinated resistance, 60fps terrain on Apple TV, Apple Watch heart rate integration

---

## Network Engineering

### NetVis

<span class="status-badge status-complete">Production Ready</span>

Network topology visualization library for Rust with multiple layout algorithms.

**Stack:** Rust, SVG/PNG/PDF export

**Features:**
- Layouts: force-directed, Sugiyama hierarchical, radial tree, multi-layer
- Edge bundling (FDEB), obstacle-aware routing
- 582 tests
- CLI and library API

All 10 phases complete.

---

### ank-pydantic

<span class="status-badge status-active">Active</span>

Type-safe network topology modeling with Pydantic models and Rust graph engine (petgraph).

**Stack:** Python, Rust (PyO3), Pydantic

**Features:**
- Type-safe device, interface, relationship models
- Rust-backed graph operations
- Multi-vendor config generation (11+ platforms)
- Rich query API
- Multi-layer modeling (physical, logical, protocol)

---

### ANK Workbench

<span class="status-badge status-active">v1.1 Complete</span>

Unified network simulation and visualization platform integrating ANK Pydantic, simulator, and visualization.

**Stack:** Python (FastAPI), React, TypeScript

**Features:**
- Declarative network design with Pydantic models
- Lightweight simulation vs VM emulation
- Integrated topology, config, behavior visualization
- Guided tour, sample gallery, contextual help

v1.1 (Feb 9, 2026): production-ready onboarding experience

---

### TopoGen

<span class="status-badge status-active">v0.10</span>

Network topology generator with Python bindings.

**Stack:** Rust, Python (PyO3)

**Features:**
- Data center: fat-tree, leaf-spine
- WAN: ring, mesh, hierarchical
- Random: Erdős-Rényi, Barabási-Albert, Watts-Strogatz
- Three interfaces: CLI, Python API, config YAML
- Structural validation, design pattern compliance

v0.9 (Feb 5, 2026)

---

### netsim

<span class="status-badge status-active">Active</span>

Deterministic network protocol simulator validating configurations before production.

**Stack:** Rust, Python bindings

**Protocols:** OSPF, IS-IS, BGP, MPLS/LDP, BFD, GRE, VRF, ICMP, ARP

**Design:** Protocol-level fidelity, deterministic execution, 100+ device topologies in seconds, JSON output for CI/CD

---

## Legacy

### AutoNetkit

<span class="status-badge status-complete">Legacy (PhD 2017)</span>

Network configuration automation tool transforming high-level specifications into device configurations.

**Stack:** Python

**Impact:**
- Used in Cisco's VIRL project
- [GitHub](https://github.com/sk2/autonetkit)
- [PyCon AU 2013 talk](https://www.youtube.com/watch?v=EGK5jjyUBCQ)

Now superseded by ank-pydantic.

Thesis: [Abstractions and Transformations for Automated Data Network Configuration](thesis)

---

## Development Approach

I plan work in `.planning/` directories with phase-based execution. I verify completeness with formal documents. I use NATS for message coordination. I write comprehensive tests. I document architecture decisions in PROJECT.md and STATE.md.
