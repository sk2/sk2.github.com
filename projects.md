---
layout: default
---

# Projects

My work focuses on network automation tools, signal processing systems, and multi-agent architectures.

---

## Network Engineering

### NetVis

<span class="status-badge status-complete">Production Ready</span>

Library-first network topology visualization engine for Rust. Transforms network topologies into clear, information-dense visualizations using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical structure.

**Stack:** Rust, petgraph, SVG/PNG/PDF export

**Architecture:**
- `petgraph`-backed graph wrapper with typed nodes/edges
- Layout algorithms: force-directed, Sugiyama hierarchical, radial tree
- Multi-layer support with isometric/starburst layouts
- Edge refinement: force-directed edge bundling (FDEB), obstacle-aware routing
- Customizable styling system with type-safe builder pattern

**Metrics:** 582 tests (554 unit + 28 integration), 17 example topologies, CLI tool

All 10 phases complete. Production-ready for network topology visualization at scale.

---

### ank-pydantic

<span class="status-badge status-active">Active</span>

Type-safe network topology modeling with Pydantic models backed by Rust graph engine (petgraph). Solves the "type safety vs performance" problem in network topology definition and analysis.

**Stack:** Python, Rust (PyO3), Pydantic, petgraph

**Problem It Solves:**
- Graph libraries (NetworkX, rustworkx): fast but untyped, easy to create invalid structures
- Source-of-truth tools (NetBox, Nautobot): great for inventory but not designed for topology analysis
- Custom solutions: full control but must build validation, storage, and query layers

**Features:**
- Type-safe device, interface, relationship models with Pydantic validation
- Rust-backed graph operations for performance with Python ergonomics
- Rich query API: chainable filters and traversals without manual graph walking
- Multi-layer modeling: separate physical, logical, protocol views
- Multi-vendor config generation for 11+ platforms
- Optional API server, CLI, visualization

**Use Cases:** Design validation before deployment, multi-vendor config generation, architecture compliance checking, SDN controller prototyping

---

### ANK Workbench

<span class="status-badge status-active">v1.1 Complete</span>

Unified network simulation and visualization platform integrating ANK Pydantic models, simulator, and visualization. Modern alternative to GNS3 and Cisco Modeling Labs emphasizing declarative design and lightweight simulation over VM emulation.

**Stack:** Python (FastAPI), React, TypeScript

**Core Value:** Design, validate, and visualize network changes in one workflow without switching tools or manual integration.

**v1.1 Features** (Feb 9, 2026):
- Persistent help system: non-modal drawer, 16 contextual tips, route-aware visibility
- Sample gallery: 5 offline topologies (2-node starter to 12-node spine-leaf DC)
- Intelligent empty states: cause-specific, outcome preview pattern
- Guided tour: 8-step workflow coverage with CSS-only spotlight
- Production-ready onboarding: 101 files modified, 30 commits, 50/50 audit score

**Workflow:** Declarative Pydantic models → lightweight simulation → integrated topology/config/behavior visualization

---

### TopoGen

<span class="status-badge status-active">v0.10</span>

Network topology generator consolidating scattered generation logic into high-performance Rust library with Python bindings.

**Stack:** Rust, Python (PyO3), maturin

**Topology Types:**
- Data center: fat-tree, leaf-spine with realistic parameters
- WAN/backbone: ring, mesh, hierarchical
- Random graphs: Erdős-Rényi, Barabási-Albert, Watts-Strogatz

**Interfaces:**
- CLI: quick generation from command line
- Python API: workflow integration
- Config-driven: YAML for complex/repeatable setups
- Parity tests ensure interface consistency

**Validation:** Structural correctness, design pattern compliance, realistic parameters (bandwidth, latency, interface naming conventions)

**Latest:** v0.9 User Interfaces (Feb 5, 2026) with mdBook documentation and doc-tests

---

### netsim

<span class="status-badge status-active">Active</span>

Deterministic tick-based network protocol simulator validating configurations before production deployment. Protocol-level fidelity with same-topology-same-results guarantees.

**Stack:** Rust, Python bindings (PyO3)

**Protocols Implemented:**
- Routing: OSPF (point-to-point, Area 0, LSA Types 1/2, Dijkstra SPF), IS-IS (L1/L2 hierarchical, LSP flooding), BGP (iBGP/eBGP, communities, route propagation)
- MPLS: LDP label distribution, label push/swap/pop operations, MPLS OAM
- Resilience: BFD (bidirectional forwarding detection, async mode)
- Tunneling: GRE encapsulation, VRF isolation (L3VPN foundations)
- Layer 2/3: ARP request/reply, ICMP echo (ping), Time Exceeded (traceroute)

**Architecture:**
- Tick-based execution: deterministic, reproducible simulations (~1ms per tick)
- RIB/FIB separation: mirrors real router behavior
- Convergence detection: automatically detects network stabilization
- Scripted commands: diagnostics at specific ticks or after convergence

**Performance:** Simulates 100+ device topologies in seconds. JSON output for CI/CD integration.

---

## Signal Processing & Hardware

### Astro

<span class="status-badge status-planning">Planning</span>

Open-source astrophotography control system for Linux devices (Raspberry Pi) attached to telescope setups. Alternative to proprietary systems like ZWO ASIAir.

**Stack:** Rust

**Mission:**
- Core competence: rock-solid imaging, guiding, mount control
- Extensibility: inject custom logic ("Stop imaging if HFR degrades by 20%")
- Intelligence: automated cloud handling, adaptive gain/exposure, real-time data quality analysis
- Hardware agnostic: wide hardware support via INDI or ASCOM Alpaca

**Design:**
- Headless: runs as system service on telescope computer
- Remote interface: modern web UI (iPad/laptop/phone browser), no VNC required
- Terminal TUI: robust local debugging and power-user control via SSH
- Reactive: real-time push of images and status to client

**Why Build This:** Proprietary systems restrict hardware choices and feature innovation. Full Windows PCs (NINA) require more power/maintenance than headless embedded binary. Advanced users need specific triggers (weather, star safety, custom sequences) that simple appliances don't offer.

---

### HealthyPi Ecosystem

<span class="status-badge status-active">Phase 4/6 (88%)</span>

Modular health monitoring ecosystem translating HealthyPi hardware biometric data (ECG, PPG, EDA, EEG, IMU) into insights through agentic intelligence.

**Stack:** Python, NATS, PyArrow/Parquet, NeuroKit2, NumPy, SciPy

**Architecture:**
- Standardized data models: multi-modal biometric data with JSON/Parquet serialization
- Virtual Patient simulator: NeuroKit2-based physiological signal generation for hardware-free development
- Real-time analysis engine: HRV (time/frequency domain), EDA stress detection, activity classification
- NATS integration: publishes raw signals and processed metrics to agent-framework message bus

**Technical Depth:**
- 286 comprehensive tests validating signal processing and analysis algorithms
- 6 physiological states with research-backed parameter ranges (WESAD dataset)
- Frequency-domain HRV: 4 Hz RR resampling, Hann window, rFFT PSD with LF/HF band integration
- EDA tonic/phasic decomposition using SciPy primitives
- Modular architecture: agents consume health trends and metrics

**Hardware:** HealthyPi 6 (Pi HAT), HealthyPi Move (wearable)

**Progress:** Foundation ✅ | Virtual Patient ✅ | Analysis Engine ✅ | Agent Integration 🔄

---

### Project Spectra

<span class="status-badge status-planning">Planning</span>

Autonomous distributed SIGINT system monitoring radio spectrum with ML-based signal classification and spatial RF mapping. Transforms raw RF data into actionable "Signal Census" through automated detection and distributed acquisition.

**Stack:** Python, Rust (planned), Swift (visualization), ML frameworks

**Architecture:**
- Edge: Raspberry Pi 4/5 with multiple SDRs streaming IQ data
- Core: Mac mini M-Series for ML inference, storage, visualization (leveraging Neural Engine)
- Network: low-latency local network for IQ streaming

**Hardware Configuration:**

*SDRs:*
- Airspy R2 (primary wideband scanner)
- Airspy HF Discovery (HF/LF coverage)
- KrakenSDR (5-channel phase-coherent for Direction of Arrival)
- RTL-SDR (utility/ADS-B reception)

*Antennas:*
- TA1 Turnstile (satellite/VHF)
- Diamond D-130 Discone (broadband scanner)
- MLA-30 Loop (LF/HF)
- Mini-Kits LNA for satellite reception

**Planned Features:**
- Real-time waterfall visualization with multi-SDR switching
- Automated modulation detection with SigIDWiki pattern matching
- Autonomous frequency band scanning with persistent Signal Census database
- Automatic NOAA/Meteor satellite recording based on orbital calculations
- KrakenSDR Direction of Arrival for spatial RF mapping
- ADS-B aircraft tracking on unified geographical display

**Philosophy:** Edge-first architecture, sustainable always-on monitoring, minimal manual intervention

---

## AI & Agents

### Secure Multi-Agent Personal Assistant

<span class="status-badge status-active">Active Development</span>

Multi-agent system where specialized agents run in isolated containers and communicate through a message broker. Zero-trust architecture: agents treated as potentially compromised.

**Stack:** Python, Docker, NATS, Swift (macOS collectors), OpenTelemetry

**Security Model:**
- Containerized isolation: each agent runs with seccomp deny-by-default, read-only filesystem, no-new-privileges
- NATS broker: TLS 1.3, per-subject ACLs, JetStream for durable messaging
- Capability-based authorization: short-lived signed tokens per action with one-time nonce validation
- Complete audit trail: all agent actions, message flows, security events logged to SQLite WAL
- Per-agent network policies: sensitive agents get no internet, API agents get scoped access only

**Architecture:**
- Orchestrator: LLM planning (GPT-4/Claude), workflow DAG execution, NATS dispatch
- Agents: lightweight and deterministic; orchestrator does reasoning
- macOS collectors: Swift binaries for HealthKit/EventKit (host-only integrations)
- Observability: structured logs with correlation IDs, OpenTelemetry traces to Jaeger

**Current Agents:** health monitoring (HealthKit), home automation (Hue), data aggregation (calendar/weather/RSS), screen time tracking, backup integrity monitoring, financial summaries

[GitHub](https://github.com/sk2/multi-agent-assistant)

---

### Cycle Agent

<span class="status-badge status-planning">Planning</span>

Native SwiftUI training app bridging KICKR Core smart trainer with AI-driven workout logic via NATS. Demonstrates "Agent Bridge" pattern for real-time hardware control through message bus coordination.

**Stack:** SwiftUI, SceneKit, FTMS (BLE), NATS

**Architecture:**
- Low-latency BLE resistance control following FTMS (Fitness Machine Service) standards
- Real-time telemetry and commands via NATS Agent Bridge
- Smooth 60fps infinite terrain rendering on Apple TV with SceneKit
- Apple Watch heart rate relay through iOS/tvOS lifecycle-aware NATS connection
- NATS connection handles iOS/tvOS backgrounding and lifecycle events

**Target Experience:** Dynamic AI-led training sessions where agents adjust resistance based on real-time performance data, integrated workout planning, and physiological metrics from Apple Health ecosystem.

**Platforms:** Native for iPadOS and tvOS

---

## Legacy

### AutoNetkit

<span class="status-badge status-complete">Legacy (PhD 2017)</span>

Network configuration automation tool transforming high-level specifications into device configurations using compiler-based approach with multi-stage transformations.

**Stack:** Python

**Architecture:** Specification abstraction → intermediate network-wide state representation → low-level device configuration → template assembly

**Impact:**
- Used in Cisco's VIRL project for topology configuration generation
- Open source: [github.com/sk2/autonetkit](https://github.com/sk2/autonetkit)
- Presented at PyCon AU 2013: [YouTube recording](https://www.youtube.com/watch?v=EGK5jjyUBCQ)
- Tested on European academic network scale: valid configs for 1000+ devices generated in seconds

**Research Contribution:** Demonstrated extensibility to wide range of protocols (OSPF, IS-IS, BGP) and devices, scalability to core-network sizes, and practical utility in industry tools.

Now superseded by ank-pydantic (modern Pydantic + Rust implementation with type safety and performance).

**Full thesis:** [Abstractions and Transformations for Automated Data Network Configuration](thesis)

---

**Development:** [Philosophy and approach](development)
