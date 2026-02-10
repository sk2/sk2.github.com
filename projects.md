---
layout: default
---

# Current Projects

I'm currently working on several projects that explore the intersection of AI agents, security-first architectures, and real-time signal processing. Each project demonstrates production-ready patterns for deploying intelligent systems in security-critical or performance-sensitive environments.

---

## Secure Multi-Agent Personal Assistant

<span class="status-badge status-active">Active Development</span>

A security-first multi-agent system that coordinates specialized containerized agents through a message broker architecture. Demonstrates production-ready patterns for deploying AI agents in security-critical infrastructure environments.

**Tech Stack:** Python · Docker · NATS · Swift · OpenTelemetry

### Overview

Each agent runs in strict isolation with minimal privileges and communicates only through validated message queues. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) for planning while agents remain lightweight and deterministic. Complete isolation ensures that compromise of one agent cannot cascade to others or the orchestrator.

### Key Features

- **Zero-Trust Architecture**: Agents treated as potentially compromised; runtime constraints enforced through containers, network policies, and capability tokens
- **Message Broker Communication**: NATS with TLS 1.3, per-subject ACLs, and JetStream for durable messaging
- **Capability-Based Authorization**: Short-lived, signed tokens per action with one-time nonce validation
- **Complete Audit Trail**: All agent actions, message flows, and security events logged to SQLite WAL
- **Containerized Isolation**: Each agent runs with seccomp deny-by-default, read-only filesystem, and no-new-privileges
- **Observability**: Structured logging with correlation IDs and OpenTelemetry traces exported to Jaeger

### Current Agents

- Health monitoring (Apple HealthKit integration)
- Home automation (Hue lights)
- Data aggregation (calendar, weather, RSS)
- Screen Time tracking
- Backup integrity monitoring
- Financial summaries

[View on GitHub →](https://github.com/sk2/multi-agent-assistant)

---

## HealthyPi Ecosystem

<span class="status-badge status-active">Phase 4/6 (88% complete)</span>

A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware into actionable insights and automated interventions.

**Tech Stack:** Python · NATS · PyArrow · NeuroKit2 · NumPy

### Overview

Bridges the gap between high-fidelity biometric hardware (HealthyPi 6 Pi HAT and HealthyPi Move wearable) and daily health management through synthetic data simulation, advanced analysis, and agentic intelligence. Integrates with the Multi-Agent Personal Assistant framework using NATS for communication.

### Key Features

- **Standardized Data Models**: Multi-modal biometric data (ECG, PPG, EDA, EEG, IMU) with JSON/Parquet serialization
- **Virtual Patient Simulator**: Hardware-free development with NeuroKit2-based physiological signal generation
- **Real-Time Analysis Engine**: HRV analysis (time/frequency domain), EDA stress detection, activity classification
- **NATS Integration**: Publishes both raw signals and processed metrics to agent-framework message bus
- **Scenario Framework**: Configurable physiological states (resting, stress, sleep) with patient personas

### Technical Highlights

- 286 comprehensive tests validating signal processing and analysis algorithms
- Supports 6 physiological states with research-backed parameter ranges (WESAD dataset)
- Frequency-domain HRV with proper 4 Hz RR resampling and Welch PSD estimation
- EDA tonic/phasic decomposition using SciPy primitives
- Modular architecture allowing agents to consume health trends and metrics

### Current Progress

- ✅ Phase 1: Foundation & Data Models (complete)
- ✅ Phase 2: Virtual Patient Simulator (complete)
- ✅ Phase 3: Core Analysis Engine (complete)
- 🔄 Phase 4: Agentic Framework Integration (in progress)

---

## Project Spectra

<span class="status-badge status-planning">Phase 1 Planning</span>

An autonomous, distributed SIGINT system that monitors the radio spectrum, identifies modulations using ML, tracks aircraft and satellites, and maintains a "Signal Census" of all RF activity.

**Tech Stack:** Python · Rust · Swift · ML Frameworks

### Overview

Transforms raw radio spectrum data into an actionable "Signal Census" through automated detection, ML classification, and distributed acquisition. Designed as an edge-to-core architecture with Raspberry Pi SDR servers streaming to Mac mini for processing and visualization.

### Hardware Configuration

**Edge SDRs (Raspberry Pi 4/5):**
- Airspy R2 (primary wideband scanner)
- Airspy HF Discovery (HF/LF coverage)
- KrakenSDR (5-channel phase-coherent for Direction of Arrival)
- RTL-SDR (utility/ADS-B reception)

**Antennas:**
- TA1 Turnstile (satellite/VHF)
- Diamond D-130 Discone (broadband scanner)
- MLA-30 Loop (LF/HF)

**Core Processing:**
- Mac mini M-Series (ML inference, storage, visualization)
- Mini-Kits LNA for satellite reception

### Planned Features

- **Real-Time Streaming**: High-performance waterfall visualization with multi-SDR switching
- **Automated Classification**: ML-based modulation detection with SigIDWiki pattern matching
- **Autonomous Scanning**: Designated frequency bands with persistent Signal Census database
- **Satellite Tracking**: Automatic NOAA/Meteor recording based on orbital pass calculations
- **Direction Finding**: KrakenSDR integration for spatial RF mapping
- **ADS-B Integration**: Aircraft tracking on unified geographical display

### Development Philosophy

Edge-first architecture leveraging Raspberry Pi for acquisition and Mac Neural Engine for ML workloads. Focus on sustainable, always-on spectrum monitoring with minimal manual intervention.

---

## Cycle Agent

<span class="status-badge status-planning">Planning</span>

A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit environment.

**Tech Stack:** SwiftUI · SceneKit · FTMS (BLE) · NATS

### Overview

Brings the Multi-Agent Personal Assistant architecture to indoor cycling by connecting KICKR Core smart trainer to agent-driven workout orchestration. Demonstrates "Agent Bridge" pattern for real-time hardware control through message bus coordination.

### Key Design Goals

- **Low-Latency Control**: Direct BLE resistance control of KICKR Core following FTMS standards
- **Agent Coordination**: Real-time telemetry and commands via NATS Agent Bridge
- **High-Performance Visualization**: Smooth 60fps infinite terrain rendering on Apple TV
- **Apple Watch Integration**: Heart rate relay through iOS/tvOS lifecycle-aware NATS connection

### Technical Architecture

- Native SwiftUI/Swift for tvOS and iPadOS
- Bluetooth communication using Fitness Machine Service (FTMS) standards
- NATS connection handling iOS/tvOS backgrounding and lifecycle events
- SceneKit for procedural terrain generation and camera following

### Target Experience

Dynamic, AI-led training sessions where agents adjust resistance based on real-time performance data, integrated workout planning, and physiological metrics from Apple Health ecosystem.

---

## Development Workflow

My current workflow emphasizes **modular architecture**, **security-first design**, and **systematic development** through the GSD (Get Stuff Done) methodology:

- **Planning-First**: Each project maintains `.planning/` directories with structured roadmaps, requirements, and phase plans
- **Verification Loops**: Formal verification documents confirm phase completion against original goals
- **Message Bus Architecture**: NATS as universal communication layer enables agent coordination across projects
- **Test-Driven**: Comprehensive test suites validate correctness (286 tests in HealthyPi, security validation in multi-agent)
- **Documentation as Design**: Architecture decisions captured in PROJECT.md and decision logs in STATE.md
