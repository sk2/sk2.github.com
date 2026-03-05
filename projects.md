---
layout: default
---

# Projects

Focused on network engineering, autonomous systems, and signal processing.

---

<div class="search-container"><input type="text" id="projectSearch" placeholder="Search projects, stack, or descriptions..." onkeyup="filterProjects()"></div>

## Recent Activity

<ul class="recent-activity-list">
<li><strong>2026-03-05</strong>: <a href="projects/configparsing">Brownfield Ingestion & Analysis</a> — <em>Completed 07-01-PLAN.md</em></li>
<li><strong>2026-03-05</strong>: <a href="projects/netassure">Network Analysis Engine</a> — <em>Completed 01-03-PLAN.md</em></li>
<li><strong>2026-03-05</strong>: <a href="projects/netflowsim">Performance Simulator</a> — <em>Archived Criterion 50k/75k/100k reports;  near-complete</em></li>
<li><strong>2026-03-05</strong>: <a href="projects/orchestrator">Orchestrator (Device Interaction Runner)</a> — <em>2026-03-05 - Completed 02-05-PLAN.md</em></li>
<li><strong>2026-03-04</strong>: <a href="projects/ank-nte">Topology Engine Core</a> — <em>Completed  (Zero-copy Mmap CSR Serialization and Traversal).</em></li>
</ul>

---

## 🌐 Network Engineering

<div class="project-grid">
<div class="project-card" data-search="automation workbench **an orchestration platform** that integrates the ank ecosystem tools (topogen, ank_pydantic, network simulator, netvis) into one seamless workflow. ank workbench is the **glue layer** that coordinates the entire network automation pipeline. engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results—all from a unified web interface. python typescript ank-workbench">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/ank-workbench">Automation Workbench</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow. ANK Workbench is the **glue layer** that coordinates the entire network automation pipeline. Engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results—all from a unified web interface.</p>
</div>

<div class="project-card" data-search="brownfield ingestion & analysis a network automation framework that decouples network configuration from vendor-specific syntax. it uses llm-powered rag to extract network-level intent and topology relationships from vendor documentation and cli configurations, normalizing them into a vendor-neutral topology graph model inspired by autonetkit. the system enables cross-vendor configuration generation and validation through semantic simulation. python configparsing">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/configparsing">Brownfield Ingestion & Analysis</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A network automation framework that decouples network configuration from vendor-specific syntax. It uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model inspired by AutoNetKit. The system enables cross-vendor configuration generation and validation through semantic simulation.</p>
</div>

<div class="project-card" data-search="device interaction framework a fast, simple, and ergonomic rust library and cli for network device interaction and automated testing. provides the essential pyats capabilities—testbed management, cli parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit. rust deviceinteraction">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/deviceinteraction">Device Interaction Framework</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A fast, simple, and ergonomic Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities—testbed management, CLI parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit.</p>
</div>

<div class="project-card" data-search="network configuration framework deterministic, auditable, ci/cd-friendly rust cli for compiling declarative yaml network blueprints into vendor-neutral configuration artifacts. the `netcfg` binary orchestrates: blueprint parsing → topology transformation → deviceir generation → template rendering → traceable config file emission. rust ank-netcfg">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/ank-netcfg">Network Configuration Framework</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">Deterministic, auditable, CI/CD-friendly Rust CLI for compiling declarative YAML network blueprints into vendor-neutral configuration artifacts. The `netcfg` binary orchestrates: blueprint parsing → topology transformation → DeviceIR generation → template rendering → traceable config file emission.</p>
</div>

<div class="project-card" data-search="network modeling & configuration library a python library for modeling and querying network topologies, backed by a high-performance rust core (`ank_nte`). features a two-stage transformation model (whiteboard → plan → protocol layers), type-safe pydantic models for nodes/edges/layers, and a composable lazy query api with rust-backed execution. ships with "batteries-included" domain models (isis, mpls, evpn, l3vpn, ixp) in the blueprints/ module. python polars ank-pydantic">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/ank-pydantic">Network Modeling & Configuration Library</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Features a two-stage transformation model (Whiteboard → Plan → Protocol Layers), type-safe Pydantic models for nodes/edges/layers, and a composable lazy query API with Rust-backed execution. Ships with "batteries-included" domain models (ISIS, MPLS, EVPN, L3VPN, IXP) in the blueprints/ module.</p>
</div>

<div class="project-card" data-search="network simulator deterministic tick-based network protocol simulator validating configurations before production deployment. it provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full vm emulation. unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. rust netsim">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/netsim">Network Simulator</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation. Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**.</p>
</div>

<div class="project-card" data-search="orchestrator (device interaction runner) an orchestration runner for coordinating **device interactions** across real/testbed networks. it executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem. v1 is explicitly **device-focused** and **uses `deviceinteraction` as a library** for transports/parsing/test primitives. python orchestrator">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/orchestrator">Orchestrator (Device Interaction Runner)</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem. v1 is explicitly **device-focused** and **uses `deviceinteraction` as a library** for transports/parsing/test primitives.</p>
</div>

<div class="project-card" data-search="project: network automation ecosystem - overall architecture definition this project aims to comprehensively define the **overall architecture of the network automation ecosystem**. this involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `workbench`), along with strategic initiatives like the "intelligence layer," integrate to form a cohesive, unified, and differentiated product. the output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.  automationarch">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/automationarch">PROJECT: Network Automation Ecosystem - Overall Architecture Definition</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> </div>
  <p style="font-size: 0.9em; margin-top: 0;">This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `topogen`, `autonetkit`, `netsim`, `netflowsim`, `netvis`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product. The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.</p>
</div>

<div class="project-card" data-search="topology engine core nte (network topology engine) is a rust-based graph topology engine with python bindings via pyo3, used as the backend for ank_pydantic. it provides a 14-crate cargo workspace built on petgraph stabledigraph with pluggable datastores (polars, duckdb, lite). this project covers two milestones: first hardening the existing engine for production reliability, then evaluating ladybugdb as a potential backend replacement. rust python typescript polars ank-nte">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/ank-nte">Topology Engine Core</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span><span class="stack-badge">Polars</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">NTE (Network Topology Engine) is a Rust-based graph topology engine with Python bindings via PyO3, used as the backend for ank_pydantic. It provides a 14-crate Cargo workspace built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite). This project covers two milestones: first hardening the existing engine for production reliability, then evaluating LadybugDB as a potential backend replacement.</p>
</div>

<div class="project-card" data-search="topology generator a rust-based network topology generator with python bindings that consolidates scattered topology generation logic from autonetkit, simulation tools, and visualization tools. generates realistic data center, wan, and random graph topologies with proper structure, design patterns, and realistic parameters. outputs custom yaml format for use across the network engineering tool ecosystem. rust python topogen">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/topogen">Topology Generator</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters. Outputs custom YAML format for use across the network engineering tool ecosystem.</p>
</div>

<div class="project-card" data-search="visualization engine a rust-based network topology layout and visualization engine. takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. outputs static formats (svg, pdf, png) for v1, with interactive browser embedding planned for future integration with other tooling. rust python typescript netvis">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/netvis">Visualization Engine</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <img src="../images/hero-diagram.svg" class="project-thumbnail" alt="Visualization Engine diagram" />
  <p style="font-size: 0.9em; margin-top: 0;">A Rust-based network topology layout and visualization engine. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. Outputs static formats (SVG, PDF, PNG) for v1, with interactive browser embedding planned for future integration with other tooling.</p>
</div>

</div>

## 📡 Radio Systems

<div class="project-grid">
<div class="project-card" data-search="project: wi-fi signal reflection (krakensdr)  rust python wifi-signal-analysis">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/wifi-signal-analysis">Project: Wi-Fi Signal Reflection (KrakenSDR)</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;"></p>
</div>

<div class="project-card" data-search="radio streaming server a cross-platform (targeted at raspberry pi) server that interfaces with multiple sdr devices (rtl-sdr, airspy hf+) and streams raw iq samples over the network using the industry-standard `rtl_tcp` protocol. it features a built-in tui for live configuration and device management. rust rtltcp">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/rtltcp">Radio Streaming Server</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.</p>
</div>

<div class="project-card" data-search="signal reflection - krakensdr multi-beam system a distributed multi-beam signal reflection analysis system based on krakensdr hardware. pi handles data acquisition, mac/linux handles compute-intensive dsp. all 4 reflection channels process in parallel with independent range-doppler visualization, per-beam configuration, and real-time performance monitoring. rust python rf-signal-analysis">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/rf-signal-analysis">Signal Reflection - KrakenSDR Multi-Beam System</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A distributed multi-beam signal reflection analysis system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 reflection channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.</p>
</div>

<div class="project-card" data-search="spectrum analysis  python signals">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/signals">Spectrum Analysis</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <img src="../images/search_topk_example.png" class="project-thumbnail" alt="Spectrum Analysis diagram" />
  <p style="font-size: 0.9em; margin-top: 0;"></p>
</div>

</div>

## 🏥 Health & Biometrics

<div class="project-grid">
<div class="project-card" data-search="healthypi ecosystem  python healthypi">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/healthypi">HealthyPi Ecosystem</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;"></p>
</div>

</div>

## 🔭 Astrophotography

<div class="project-grid">
<div class="project-card" data-search="aurora advisor a specialized tool for australian aurora observers that solves the "should i drive 60 minutes?" problem. it combines real-time solar wind data (noaa), substorm trigger logic (bz/hp trends), and local weather (access-g model) to provide actionable advice. typescript auroradata">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/auroradata">Aurora Advisor</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">TypeScript</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.</p>
</div>

<div class="project-card" data-search="auroraphoto an automated astrophotography system designed to capture high-quality aurora and night sky imagery. the project uses raspberry pi "nodes" connected via usb to sony a7r v/a7 iv cameras, controlled and assisted by an iphone companion app.  auroraphoto">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/auroraphoto">AuroraPhoto</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> </div>
  <p style="font-size: 0.9em; margin-top: 0;">An automated astrophotography system designed to capture high-quality aurora and night sky imagery. The project uses Raspberry Pi "nodes" connected via USB to Sony a7R V/a7 IV cameras, controlled and assisted by an iPhone companion app.</p>
</div>

<div class="project-card" data-search="eclipsestack eclipsestack is a rust-powered utility (with a web-based ui) specifically designed to align hundreds of raw solar eclipse images taken during totality. it addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on exif data. the goal is to produce a perfectly aligned set of frames ready for hdr stacking in professional tools like pixinsight. rust eclipsestack">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/eclipsestack">EclipseStack</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.</p>
</div>

<div class="project-card" data-search="openastro core openastro core ("core sdk") is a high-performance rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the openastro ecosystem. it exists to keep coordinate math, imaging intelligence, and device/protocol behavior consistent across downstream openastro apps. rust open-astro-core">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/open-astro-core">OpenAstro Core</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">OpenAstro Core ("Core SDK") is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It exists to keep coordinate math, imaging intelligence, and device/protocol behavior consistent across downstream OpenAstro apps.</p>
</div>

<div class="project-card" data-search="openastro node a headless, autonomous astrophotography controller designed for low-power linux devices (rpi/jetson). it manages hardware, executes imaging sequences, and ensures rig safety. rust typescript open-astro-node">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/open-astro-node">OpenAstro Node</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). It manages hardware, executes imaging sequences, and ensures rig safety.</p>
</div>

<div class="project-card" data-search="project: eclipsephoto a "fire and forget" raspberry pi-based controller for autonomous solar eclipse photography. it coordinates a camera (via gphoto2) and a high-end mount (zwo am5 / benro polaris via indi) to capture a complete eclipse sequence from c1 to c4 without manual intervention. python eclipsephoto">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/eclipsephoto">Project: EclipsePhoto</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A "fire and forget" Raspberry Pi-based controller for autonomous solar eclipse photography. It coordinates a camera (via gphoto2) and a high-end mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from C1 to C4 without manual intervention.</p>
</div>

<div class="project-card" data-search="satellites a terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. built with rust, ratatui, and the sgp4 orbital propagation algorithm. aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead. rust satellites">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/satellites">Satellites</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm. Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead.</p>
</div>

</div>

## 📷 Photography

<div class="project-grid">
<div class="project-card" data-search="photo tour photo tour is a smart, interactive photography assistant designed for field use. it helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.  photo-tour">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/photo-tour">Photo Tour</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> </div>
  <p style="font-size: 0.9em; margin-top: 0;">Photo Tour is a smart, interactive photography assistant designed for field use. It helps you compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.</p>
</div>

</div>

## 🤖 Autonomous Systems

<div class="project-grid">
<div class="project-card" data-search="project: cycle agent   cycle">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/cycle">Project: Cycle Agent</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> </div>
  <p style="font-size: 0.9em; margin-top: 0;"></p>
</div>

<div class="project-card" data-search="secure multi-agent personal assistant a security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying ai agents in security-critical infrastructure environments. the orchestrator uses cloud llm reasoning (gpt-4/claude) while agents remain lightweight and deterministic. python multi-agent">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/multi-agent">Secure Multi-Agent Personal Assistant</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.</p>
</div>

</div>

## 📊 Data & Utilities

<div class="project-grid">
<div class="project-card" data-search="cli parser a high-performance parsing engine for network device output. it transforms semi-structured cli text into structured data (json/yaml) using an optimized state machine. designed as a modern, ergonomic alternative to legacy tools like textfsm, it provides significantly faster execution while maintaining full compatibility with existing template libraries. rust cliscrape">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/cliscrape">CLI Parser</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A high-performance parsing engine for network device output. It transforms semi-structured CLI text into structured data (JSON/YAML) using an optimized state machine. Designed as a modern, ergonomic alternative to legacy tools like TextFSM, it provides significantly faster execution while maintaining full compatibility with existing template libraries.</p>
</div>

<div class="project-card" data-search="project: tileserver polars (rust optimized)  rust python polars tileserver">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/tileserver">PROJECT: Tileserver Polars (Rust Optimized)</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p style="font-size: 0.9em; margin-top: 0;"></p>
</div>

<div class="project-card" data-search="performance simulator  rust netflowsim">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/netflowsim">Performance Simulator</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;"></p>
</div>

<div class="project-card" data-search="project: nas cleanup & intelligence  rust nascleanup">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/nascleanup">Project: NAS Cleanup & Intelligence</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;"></p>
</div>

<div class="project-card" data-search="project: omnifocus db cli (omnifocus-db) a python-based cli that bypasses slow applescript/typescript layers to read directly from the omnifocus sqlite database on macos. it provides structured, token-efficient data (json/text) to agents for lightning-fast project listing, inbox analysis, and context gathering. python typescript omnifocus-db">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/omnifocus-db">Project: OmniFocus DB CLI (omnifocus-db)</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Last Active: 2026-02-16</span> <span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.</p>
</div>

<div class="project-card" data-search="project: weather (bom access pipeline) a data engineering pipeline to fetch, process, and serve high-resolution weather model data from the australian bureau of meteorology (bom). specifically targeting the access (australian community climate and earth-system simulator) model outputs. python polars weather">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/weather">Project: Weather (BOM ACCESS Pipeline)</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Last Active: 2026-02-14</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology (BOM). Specifically targeting the ACCESS (Australian Community Climate and Earth-System Simulator) model outputs.</p>
</div>

<div class="project-card" data-search="matrix-profile-rs time series analysis typically requires either slow python libraries or complex manual implementation. **matrix-profile-rs** provides matrix profile algorithms (stomp, scrimp++, scamp) in native rust with ergonomic apis for motif discovery and anomaly detection, achieving c-level performance with python-level usability through polars integration. rust polars matrix-time-series">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/matrix-time-series">matrix-profile-rs</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">Time series analysis typically requires either slow Python libraries or complex manual implementation. **matrix-profile-rs** provides Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust with ergonomic APIs for motif discovery and anomaly detection, achieving C-level performance with Python-level usability through Polars integration.</p>
</div>

</div>

## 🧘 Wellness & Sound

<div class="project-grid">
<div class="project-card" data-search="psytrance generator a generative psytrance synthesis engine with real-time tui controls. creates complete tracks driven by a multi-level energy model, with live playback, step editing, and wav export. currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently. rust psytrance">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/psytrance">Psytrance Generator</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently.</p>
</div>

<div class="project-card" data-search="wave (stillstate & flowstate) **wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. 1. **stillstate (watch):** an adaptive sleep sounds app for apple watch with personalized frequency calibration, heartbeat synchronization, and microphone-based environmental monitoring.  watch-noise">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/watch-noise">Wave (StillState & FlowState)</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> </div>
  <p style="font-size: 0.9em; margin-top: 0;">**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work. 1. **StillState (Watch):** An adaptive sleep sounds app for Apple Watch with personalized frequency calibration, heartbeat synchronization, and microphone-based environmental monitoring.</p>
</div>

</div>

## 🧪 Experimental

<div class="project-grid">
<div class="project-card" data-search="asiair import tool a python script that automates post-imaging-session file organization for astrophotography. it batch-imports fits files from asiair backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for pixinsight's wbpp (weighted batch preprocessing) workflow.  import-asiair">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/import-asiair">ASIAIR Import Tool</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Last Active: 2026-02-11</span> </div>
  <p style="font-size: 0.9em; margin-top: 0;">A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.</p>
</div>

<div class="project-card" data-search="network analysis engine a graph neural network (gnn) based network analytics module that extends netassure's existing topology analysis capabilities with real-time learning and prediction. integrates with the nte (network topology engine) to provide anomaly detection, traffic prediction, and topology learning through multiple consumption interfaces. rust polars netassure">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/netassure">Network Analysis Engine</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A Graph Neural Network (GNN) based network analytics module that extends NetAssure's existing topology analysis capabilities with real-time learning and prediction. Integrates with the NTE (Network Topology Engine) to provide anomaly detection, traffic prediction, and topology learning through multiple consumption interfaces.</p>
</div>

<div class="project-card" data-search="rust tui gtd todo (omnifocus-inspired) a fast, keyboard-driven rust text ui (tui) task manager inspired by omnifocus, built around a gtd workflow. it stores data in an owned sqlite database, supports projects and hierarchical contexts/tags, and is optimized for rapid inbox processing (triage + tagging) with minimal friction. an omnifocus 4 `.ofocus-package` importer provides one-time migration into the local database so the tool can replace omnifocus for day-to-day use. rust todo">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/todo">Rust TUI GTD Todo (OmniFocus-inspired)</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p style="font-size: 0.9em; margin-top: 0;">A fast, keyboard-driven Rust text UI (TUI) task manager inspired by OmniFocus, built around a GTD workflow. It stores data in an owned SQLite database, supports projects and hierarchical contexts/tags, and is optimized for rapid inbox processing (triage + tagging) with minimal friction. An OmniFocus 4 `.ofocus-package` importer provides one-time migration into the local database so the tool can replace OmniFocus for day-to-day use.</p>
</div>

<div class="project-card" data-search="sound array an exploration-focused audio processing system using raspberry pi and microphone arrays. it focuses on spatial audio (toa, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.  soundarray">
  <h3 style="margin-top:0; margin-bottom: 0.5rem;"><a href="projects/soundarray">Sound Array</a></h3>
  <div class="badges-row" style="margin-bottom: 0.8rem;"><span class="status-badge status-active">Active</span> </div>
  <p style="font-size: 0.9em; margin-top: 0;">An exploration-focused audio processing system using Raspberry Pi and microphone arrays. It focuses on spatial audio (ToA, beamforming) and classification (vehicles, wildlife) using an "analyst" agent approach.</p>
</div>

</div>


<style>
.project-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }
.project-card { border: 1px solid #dee2e6; border-radius: 8px; padding: 1.2rem; background: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.02); display: flex; flex-direction: column;}
.project-thumbnail { width: 100%; height: 120px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem; border: 1px solid #f1f3f5;}
.badges-row { display: flex; gap: 0.4rem; flex-wrap: wrap; align-items: center; }
.status-badge { padding: 0.2em 0.6em; border-radius: 4px; font-size: 0.75em; font-weight: 600; background-color: #e3f2fd; color: #495057; border: 1px solid #dee2e6; }
.stack-badge { padding: 0.2em 0.6em; border-radius: 4px; font-size: 0.75em; font-weight: 500; background-color: #f8f9fa; color: #6c757d; border: 1px solid #e9ecef;}
.search-container { margin-bottom: 2rem; }
#projectSearch { width: 100%; padding: 0.8rem 1rem; border-radius: 6px; border: 1px solid #ced4da; font-size: 1rem; box-sizing: border-box; outline: none; }
#projectSearch:focus { border-color: #80bdff; box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25); }
.recent-activity-list { line-height: 1.6; font-size: 0.95em; }
.recent-activity-list li { margin-bottom: 0.5rem; }
section { margin-bottom: 2em; }
</style>

<script>
function filterProjects() {
    var input, filter, cards, card, i, txtValue;
    input = document.getElementById('projectSearch');
    filter = input.value.toLowerCase();
    cards = document.getElementsByClassName('project-card');
    for (i = 0; i < cards.length; i++) {
        card = cards[i];
        txtValue = card.getAttribute('data-search');
        if (txtValue.indexOf(filter) > -1) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    }
}
</script>
    