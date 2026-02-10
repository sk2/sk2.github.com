---
layout: default
---

# Projects

My work spans **AI agents**, **network engineering**, and **signal processing**—with emphasis on production-ready implementations that demonstrate security-first architectures and systematic development practices.

---

## AI & Agents

### Secure Multi-Agent Personal Assistant

<span class="status-badge status-active">Active Development</span>

A security-first multi-agent system that coordinates specialized containerized agents through a message broker architecture. Demonstrates production-ready patterns for deploying AI agents in security-critical infrastructure environments.

**Tech Stack:** Python · Docker · NATS · Swift · OpenTelemetry

**Key Features:**
- Zero-trust architecture with capability-based authorization
- NATS message broker with TLS 1.3 and per-subject ACLs
- Containerized isolation (seccomp, read-only filesystem, no-new-privileges)
- Complete audit trail and OpenTelemetry observability
- Agents: health monitoring, home automation, data aggregation, backup integrity

[View on GitHub →](https://github.com/sk2/multi-agent-assistant)

---

### HealthyPi Ecosystem

<span class="status-badge status-active">Phase 4/6 (88% complete)</span>

Modular health monitoring ecosystem translating HealthyPi hardware biometric data into actionable insights through agentic intelligence.

**Tech Stack:** Python · NATS · PyArrow · NeuroKit2 · NumPy

**Key Features:**
- Multi-modal biometric data models (ECG, PPG, EDA, EEG, IMU)
- Virtual Patient simulator with NeuroKit2-based signal generation
- Real-time HRV analysis (time/frequency domain), EDA stress detection
- 286 comprehensive tests, 6 physiological state scenarios
- Integrates with Multi-Agent framework via NATS

**Progress:** Foundation ✅ | Virtual Patient ✅ | Analysis Engine ✅ | Agent Integration 🔄

---

### Project Spectra

<span class="status-badge status-planning">Phase 1 Planning</span>

Autonomous distributed SIGINT system monitoring radio spectrum with ML-based signal classification and spatial RF mapping.

**Tech Stack:** Python · Rust · Swift · ML Frameworks

**Architecture:**
- Edge SDRs: Airspy R2, HF Discovery, KrakenSDR (5-ch DoA), RTL-SDR
- Core: Mac mini M-Series for ML inference and visualization
- Features: Real-time waterfall, automated modulation detection, satellite tracking, ADS-B integration

---

### Cycle Agent

<span class="status-badge status-planning">Planning</span>

Native SwiftUI training app bridging KICKR Core with AI-driven workout logic via NATS.

**Tech Stack:** SwiftUI · SceneKit · FTMS (BLE) · NATS

**Design:** Low-latency BLE control, agent-coordinated resistance adjustment, 60fps terrain rendering on Apple TV, Apple Watch heart rate integration.

---

## Network Engineering

### NetVis

<span class="status-badge status-complete">Production Ready</span>

Library-first network topology visualization engine for Rust with multiple layout algorithms and export formats.

**Tech Stack:** Rust · SVG/PNG/PDF export

**Features:**
- Layout algorithms: force-directed, Sugiyama hierarchical, radial tree, multi-layer
- Edge bundling (FDEB) and obstacle-aware routing
- 582 tests (554 unit + 28 integration)
- CLI tool and library API

All 10 phases complete. Production-ready for network topology visualization at scale.

---

### ank-pydantic

<span class="status-badge status-active">Active Development</span>

Network topology modeling with type-safe Pydantic models backed by Rust graph engine (petgraph).

**Tech Stack:** Python · Rust (PyO3) · Pydantic

**Features:**
- Type-safe device, interface, and relationship models
- Rust-backed graph operations for performance
- Multi-vendor configuration generation (11+ platforms)
- Rich query API for topology analysis
- Multi-layer modeling (physical, logical, protocol views)

Solves the "type safety vs performance" problem in network topology definition and analysis.

---

### ANK Workbench

<span class="status-badge status-active">v1.1 Complete</span>

Unified network simulation and visualization platform integrating ANK Pydantic models, simulator, and visualization into seamless workflow.

**Tech Stack:** Python (FastAPI) · React · TypeScript

**Features:**
- Declarative network design with Pydantic models
- Lightweight simulation (vs heavy VM emulation like GNS3)
- Integrated topology, config state, and behavior visualization
- Guided tour system, sample gallery, contextual help
- Modern web UI with programmatic API access

**Latest:** v1.1 UX Polish + Onboarding (Feb 9, 2026) - production-ready first-run experience.

---

### TopoGen

<span class="status-badge status-active">v0.10 Gap Closure</span>

Network topology generator consolidating scattered generation logic into high-performance Rust library with Python bindings.

**Tech Stack:** Rust · Python (PyO3)

**Features:**
- Data center: fat-tree, leaf-spine
- WAN/backbone: ring, mesh, hierarchical
- Random graphs: Erdős-Rényi, Barabási-Albert, Watts-Strogatz
- Three interfaces: CLI, Python API, config-driven YAML
- Structural validation and design pattern compliance
- Realistic parameters (bandwidth, latency, interface naming)

**Latest:** v0.9 User Interfaces (Feb 5, 2026)

---

### netsim (Network Simulator)

<span class="status-badge status-active">Active Development</span>

Deterministic tick-based network protocol simulator validating configurations at scale before production deployment.

**Tech Stack:** Rust · Python bindings

**Protocols:**
- Routing: OSPF, IS-IS, BGP
- MPLS: LDP label distribution, LFIB operations
- Resilience: BFD fast failure detection
- Tunneling: GRE, VRF isolation
- Diagnostics: ICMP (ping/traceroute), ARP

**Design:** Protocol-level fidelity with deterministic execution. Simulate 100+ device topologies in seconds. JSON output for CI/CD integration.

---

## Legacy Projects

### AutoNetkit

<span class="status-badge status-complete">Legacy (PhD 2017)</span>

Original network configuration automation tool from PhD research. Transforms high-level network specifications into device configurations using compiler-based approach.

**Tech Stack:** Python

**Impact:**
- Used in Cisco's VIRL project
- Open source on [GitHub](https://github.com/sk2/autonetkit)
- Presented at PyCon AU 2013 ([YouTube](https://www.youtube.com/watch?v=EGK5jjyUBCQ))

Now superseded by ank-pydantic (modern Pydantic + Rust implementation).

Full thesis available: [Abstractions and Transformations for Automated Data Network Configuration](thesis)

---

## Development Philosophy

My workflow emphasizes **modular architecture**, **security-first design**, and **systematic development**:

- **Planning-First**: Structured roadmaps in `.planning/` directories with phase-based execution
- **Verification Loops**: Formal verification documents confirm goal achievement
- **Message Bus Architecture**: NATS enables agent coordination across projects
- **Test-Driven**: Comprehensive test suites (286 tests in HealthyPi, 582 in netvis)
- **Documentation as Design**: Architecture decisions captured in PROJECT.md and STATE.md
