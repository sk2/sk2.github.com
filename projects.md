---
layout: default
title: Projects
---

# Projects

Focused on network engineering, autonomous systems, and signal processing.

---

<div class="search-container"><input type="text" id="projectSearch" placeholder="Search projects, stack, or descriptions..." onkeyup="filterProjects()"></div>

## Recent Activity

<ul class="recent-activity-list">
<li><strong>2026-03-11</strong>: <a href="projects/netassure">Network Analysis Engine</a> — <em>plan, 2 files)</em></li>
<li><strong>2026-03-11</strong>: <a href="projects/psytrance">Overtone</a> — <em>Completed  (Ableton MIDI Export Upgrades).</em></li>
<li><strong>2026-03-10</strong>: <a href="projects/signals">Spectrum Analysis</a> — <em>Completed  (3D Propagation Bounce Visualization).</em></li>
<li><strong>2026-03-09</strong>: <a href="projects/matrix-time-series">matrix-profile-rs</a> — <em>Completed 15-01-PLAN.md: MultiStreamingState core + Join distance kernels + Batch Join STOMP</em></li>
<li><strong>2026-03-09</strong>: <a href="projects/rf-signal-analysis">Signal Reflection - KrakenSDR Multi-Beam System</a> — <em>Completed 40-04-PLAN.md</em></li>
</ul>

---

## Network Engineering

<div class="project-grid">
<div class="project-card" data-search="brownfield ingestion vendor translation layer that decouples network configuration from vendor-specific syntax. uses llm-powered rag to extract network-level intent and topology relationships from vendor documentation and cli configurations, normalizing them into a vendor-neutral topology graph model. the intermediate representation is topology-centric (protocol adjacencies, link roles, vlan membership) rather than device-centric like yang, enabling genuine vendor abstraction. python configparsing">
  <h3 class="card-title"><a href="projects/configparsing">Brownfield Ingestion</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Vendor translation layer that decouples network configuration from vendor-specific syntax. Uses LLM-powered RAG to extract network-level intent and topology relationships from vendor documentation and CLI configurations, normalizing them into a vendor-neutral topology graph model. The intermediate representation is topology-centric (protocol adjacencies, link roles, VLAN membership) rather than device-centric like YANG, enabling genuine vendor abstraction.</p>
</div>

<div class="project-card" data-search="cli parser parsing engine for network device cli output. transforms semi-structured text (show commands, routing tables, bgp summaries) into structured data (json/yaml) using an optimized rust state machine. provides full compatibility with the industry-standard ntc-templates library while offering 10–50x faster execution than python-based alternatives like textfsm. rust cliscrape">
  <h3 class="card-title"><a href="projects/cliscrape">CLI Parser</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Parsing engine for network device CLI output. Transforms semi-structured text (show commands, routing tables, BGP summaries) into structured data (JSON/YAML) using an optimized Rust state machine. Provides full compatibility with the industry-standard ntc-templates library while offering 10–50x faster execution than Python-based alternatives like TextFSM.</p>
</div>

<div class="project-card" data-search="configuration generation (autonetkit) a compiler-based framework for automated network provisioning. autonetkit transforms high-level network designs into validated device configurations across heterogeneous hardware and protocol environments. traditional network configuration is manual and vendor-specific. python polars autonetkit">
  <h3 class="card-title"><a href="projects/autonetkit">Configuration Generation (AutoNetkit)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">A compiler-based framework for automated network provisioning. AutoNetkit transforms high-level network designs into validated device configurations across heterogeneous hardware and protocol environments. Traditional network configuration is manual and vendor-specific.</p>
</div>

<div class="project-card" data-search="device interaction framework a rust library and cli for network device interaction and automated testing. provides the essential pyats capabilities — testbed management, cli output parsing, and state verification — without the complexity. connects to devices (real, simulated, or mocked), executes commands, parses structured output, and verifies correctness with the type safety of compiled rust. rust deviceinteraction">
  <h3 class="card-title"><a href="projects/deviceinteraction">Device Interaction Framework</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">A Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities — testbed management, CLI output parsing, and state verification — without the complexity. Connects to devices (real, simulated, or mocked), executes commands, parses structured output, and verifies correctness with the type safety of compiled Rust.</p>
</div>

<div class="project-card" data-search="network analysis engine graph neural network (gnn) based network analytics module that extends topology analysis with real-time learning and prediction. subscribes to the network topology engine's websocket stream for live topology updates, runs gnn models on graph data, and exposes analytics through multiple interfaces (websocket streaming, rest api, rust library, event queue). built on an existing rust+python analysis toolkit that includes formal verification (z3 smt solver), graph algorithms (centrality, community detection, cascade modeling), and python bindings via pyo3. rust netassure">
  <h3 class="card-title"><a href="projects/netassure">Network Analysis Engine</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Graph Neural Network (GNN) based network analytics module that extends topology analysis with real-time learning and prediction. Subscribes to the Network Topology Engine's WebSocket stream for live topology updates, runs GNN models on graph data, and exposes analytics through multiple interfaces (WebSocket streaming, REST API, Rust library, event queue). Built on an existing Rust+Python analysis toolkit that includes formal verification (Z3 SMT solver), graph algorithms (centrality, community detection, cascade modeling), and Python bindings via PyO3.</p>
</div>

<div class="project-card" data-search="network automation ecosystem - overall architecture definition this project defines the architecture of the network automation ecosystem: how its tools connect, what data flows between them, and where the system is headed. the ecosystem comprises nine repositories that form a composable toolchain. each tool handles one concern -- topology generation, simulation, configuration parsing, visualization, analysis -- and communicates through pinned contract schemas (rfc-01, rfc-02).  automationarch">
  <h3 class="card-title"><a href="projects/automationarch">Network Automation Ecosystem - Overall Architecture Definition</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> </div>
  <p class="card-description">This project defines the architecture of the Network Automation Ecosystem: how its tools connect, what data flows between them, and where the system is headed. The ecosystem comprises nine repositories that form a composable toolchain. Each tool handles one concern -- topology generation, simulation, configuration parsing, visualization, analysis -- and communicates through pinned contract schemas (RFC-01, RFC-02).</p>
</div>

<div class="project-card" data-search="network automation workbench orchestration platform that integrates the ank ecosystem tools — [topology generator](/projects/topogen), [network modeling & configuration library](/projects/ank-pydantic), [network simulator](/projects/netsim), [network visualization engine](/projects/netvis) — into a single web interface. engineers define topologies, generate configurations, run simulations, and inspect results without switching between cli tools. ```
┌──────────────────────────────────────────────────────────────────┐
│                  network automation workbench                    │
│         (orchestration · web ui · workflow management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   topogen    │  [ank-pydantic](../ank-pydantic)│   simulator  │    netvis    │ │
│   └──────────────┴──────────────┴──────────────┴──────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

the workflow follows a linear pipeline: generate or model a topology, run a simulation against it, visualize the results, and export device configurations. python typescript ank-workbench">
  <h3 class="card-title"><a href="projects/ank-workbench">Network Automation Workbench</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Orchestration platform that integrates the ANK ecosystem tools — [Topology Generator](/projects/topogen), [Network Modeling & Configuration Library](/projects/ank-pydantic), [Network Simulator](/projects/netsim), [Network Visualization Engine](/projects/netvis) — into a single web interface. Engineers define topologies, generate configurations, run simulations, and inspect results without switching between CLI tools. ```
┌──────────────────────────────────────────────────────────────────┐
│                  Network Automation Workbench                    │
│         (Orchestration · Web UI · Workflow Management)           │
│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│   │   TopoGen    │  [ank-pydantic](../ank-pydantic)│   Simulator  │    NetVis    │ │
│   └──────────────┴──────────────┴──────────────┴──────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

The workflow follows a linear pipeline: generate or model a topology, run a simulation against it, visualize the results, and export device configurations.</p>
</div>

<div class="project-card" data-search="network configuration framework network configuration framework is a rust cli that compiles declarative yaml blueprints into vendor-neutral configuration artifacts. a single binary orchestrates the full pipeline: blueprint parsing, topology transformation, deviceir generation, template rendering, and traceable config file emission. the core problem is determinism. rust ank-netcfg">
  <h3 class="card-title"><a href="projects/ank-netcfg">Network Configuration Framework</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Network Configuration Framework is a Rust CLI that compiles declarative YAML blueprints into vendor-neutral configuration artifacts. A single binary orchestrates the full pipeline: blueprint parsing, topology transformation, DeviceIR generation, template rendering, and traceable config file emission. The core problem is determinism.</p>
</div>

<div class="project-card" data-search="network modeling & configuration library the network modeling & configuration library represents network topologies as typed python objects backed by a rust graph engine. you define nodes, edges, and layers using pydantic models. the library stores them in the [network topology engine](/projects/ank-nte) and exposes a composable query api that builds lazy evaluation plans in python and executes them in rust. python polars ank-pydantic">
  <h3 class="card-title"><a href="projects/ank-pydantic">Network Modeling & Configuration Library</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">The Network Modeling & Configuration Library represents network topologies as typed Python objects backed by a Rust graph engine. You define nodes, edges, and layers using Pydantic models. The library stores them in the [Network Topology Engine](/projects/ank-nte) and exposes a composable query API that builds lazy evaluation plans in Python and executes them in Rust.</p>
</div>

<div class="project-card" data-search="network simulator deterministic tick-based network protocol simulator validating configurations before production deployment. it provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full vm emulation. unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. rust netsim">
  <h3 class="card-title"><a href="projects/netsim">Network Simulator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation. Unlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**.</p>
</div>

<div class="project-card" data-search="network topology engine rust-based graph topology engine with python bindings via pyo3. takes network topologies — nodes, edges, layers, metadata — and stores them in a dual-write architecture: structural graph (petgraph stabledigraph) plus columnar attribute store (polars dataframes). mutations update both atomically; if either write fails, the transaction rolls back. rust python typescript polars ank-nte">
  <h3 class="card-title"><a href="projects/ank-nte">Network Topology Engine</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Rust-based graph topology engine with Python bindings via PyO3. Takes network topologies — nodes, edges, layers, metadata — and stores them in a dual-write architecture: structural graph (petgraph StableDiGraph) plus columnar attribute store (Polars DataFrames). Mutations update both atomically; if either write fails, the transaction rolls back.</p>
</div>

<div class="project-card" data-search="network visualization engine rust-based network topology layout and visualization engine. takes multi-layer network topologies (via petgraph) and renders them using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical or geographic structure. outputs svg, pdf, and png with interactive browser embedding via wasm. rust python typescript netvis">
  <h3 class="card-title"><a href="projects/netvis">Network Visualization Engine</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-24</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <img src="../images/hero-diagram.svg" class="project-thumbnail" alt="Network Visualization Engine diagram" />
  <p class="card-description">Rust-based network topology layout and visualization engine. Takes multi-layer network topologies (via petgraph) and renders them using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical or geographic structure. Outputs SVG, PDF, and PNG with interactive browser embedding via WASM.</p>
</div>

<div class="project-card" data-search="orchestrator (device interaction runner) orchestration engine for coordinating device interactions across real and testbed networks. executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots). uses [device interaction framework](../deviceinteraction) as a library for transports, parsing, and test primitives — the orchestrator owns run coordination, persistence, and event streaming. python orchestrator">
  <h3 class="card-title"><a href="projects/orchestrator">Orchestrator (Device Interaction Runner)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Orchestration engine for coordinating device interactions across real and testbed networks. Executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots). Uses [Device Interaction Framework](../deviceinteraction) as a library for transports, parsing, and test primitives — the orchestrator owns run coordination, persistence, and event streaming.</p>
</div>

<div class="project-card" data-search="performance simulator network flow simulator uses analytic queuing models and monte carlo simulation to evaluate network performance without packet-level discrete event simulation. given a topology and traffic demands, it pushes billions of flow iterations through queuing models in seconds, identifying congestion bottlenecks probabilistically and projecting capacity headroom across carrier-scale networks (100k+ nodes). the core tradeoff: sacrifice per-packet fidelity for orders-of-magnitude speed improvement. rust netflowsim">
  <h3 class="card-title"><a href="projects/netflowsim">Performance Simulator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Network Flow Simulator uses analytic queuing models and Monte Carlo simulation to evaluate network performance without packet-level discrete event simulation. Given a topology and traffic demands, it pushes billions of flow iterations through queuing models in seconds, identifying congestion bottlenecks probabilistically and projecting capacity headroom across carrier-scale networks (100k+ nodes). The core tradeoff: sacrifice per-packet fidelity for orders-of-magnitude speed improvement.</p>
</div>

<div class="project-card" data-search="topology generator rust-based network topology generator with python bindings. takes a declarative yaml config describing the desired topology type, scale, and parameters, and produces a validated network graph with realistic structure — proper tier hierarchies, vendor-specific interface naming, geographic placement, and bandwidth profiles. consolidates topology generation logic that was previously scattered across autonetkit, the [network simulator](/projects/netsim), and the [network visualization engine](/projects/netvis) into a single library. rust python topogen">
  <h3 class="card-title"><a href="projects/topogen">Topology Generator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Rust-based network topology generator with Python bindings. Takes a declarative YAML config describing the desired topology type, scale, and parameters, and produces a validated network graph with realistic structure — proper tier hierarchies, vendor-specific interface naming, geographic placement, and bandwidth profiles. Consolidates topology generation logic that was previously scattered across AutoNetKit, the [Network Simulator](/projects/netsim), and the [Network Visualization Engine](/projects/netvis) into a single library.</p>
</div>

</div>

## Radio Systems

<div class="project-grid">
<div class="project-card" data-search="radio streaming server cross-platform server (targeting raspberry pi) that manages multiple sdr devices (rtl-sdr, airspy hf+) and streams raw iq samples over the network using the `rtl_tcp` protocol. a single binary replaces multiple c-based streaming tools, adding a tui for live device management, toml configuration, and safe concurrency across all connected radios. existing c implementations (`rtl_tcp`, `hfp_tcp`) are single-threaded and require separate processes per device. rust rtltcp">
  <h3 class="card-title"><a href="projects/rtltcp">Radio Streaming Server</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-22</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Cross-platform server (targeting Raspberry Pi) that manages multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the `rtl_tcp` protocol. A single binary replaces multiple C-based streaming tools, adding a TUI for live device management, TOML configuration, and safe concurrency across all connected radios. Existing C implementations (`rtl_tcp`, `hfp_tcp`) are single-threaded and require separate processes per device.</p>
</div>

<div class="project-card" data-search="signal reflection - krakensdr multi-beam system distributed multi-beam signal reflection analysis system built on krakensdr hardware. a raspberry pi handles data acquisition and streams iq data over udp; a mac or linux workstation runs compute-intensive dsp. all four surveillance channels process in parallel with independent range-doppler visualization, per-beam configuration, and real-time performance monitoring. rust python rf-signal-analysis">
  <h3 class="card-title"><a href="projects/rf-signal-analysis">Signal Reflection - KrakenSDR Multi-Beam System</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Distributed multi-beam signal reflection analysis system built on KrakenSDR hardware. A Raspberry Pi handles data acquisition and streams IQ data over UDP; a Mac or Linux workstation runs compute-intensive DSP. All four surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.</p>
</div>

<div class="project-card" data-search="sound array audio processing system using raspberry pi and microphone arrays for spatial sound analysis. captures multi-channel audio from usb/hat arrays (respeaker, matrix), computes time of arrival (toa) for sound localization, and applies beamforming for directional isolation. classifies sources — vehicles (engine sounds), aircraft, wildlife (birds) — and streams processed audio or metadata to a remote desktop for analysis.  soundarray">
  <h3 class="card-title"><a href="projects/soundarray">Sound Array</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> </div>
  <p class="card-description">Audio processing system using Raspberry Pi and microphone arrays for spatial sound analysis. Captures multi-channel audio from USB/HAT arrays (ReSpeaker, Matrix), computes Time of Arrival (ToA) for sound localization, and applies beamforming for directional isolation. Classifies sources — vehicles (engine sounds), aircraft, wildlife (birds) — and streams processed audio or metadata to a remote desktop for analysis.</p>
</div>

<div class="project-card" data-search="spectrum analysis automated signal census system that transforms raw radio spectrum data into classified, searchable signal inventories. combines sdr acquisition, ml classification, and vector search to detect, identify, and catalog signals across monitored bands. python signals">
  <h3 class="card-title"><a href="projects/signals">Spectrum Analysis</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <img src="../images/search_topk_example.png" class="project-thumbnail" alt="Spectrum Analysis diagram" />
  <p class="card-description">Automated signal census system that transforms raw radio spectrum data into classified, searchable signal inventories. Combines SDR acquisition, ML classification, and vector search to detect, identify, and catalog signals across monitored bands.</p>
</div>

<div class="project-card" data-search="wi-fi signal reflection (krakensdr) through-wall human detection and localization using existing wi-fi [signals](../signals) as illumination sources. built on the krakensdr five-channel coherent receiver, processing heimdall daq iq streams to detect movement through obstacles in indoor environments. bridges theoretical signal reflection research with a portable, real-time hardware implementation. rust python wifi-signal-analysis">
  <h3 class="card-title"><a href="projects/wifi-signal-analysis">Wi-Fi Signal Reflection (KrakenSDR)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Through-wall human detection and localization using existing Wi-Fi [signals](../signals) as illumination sources. Built on the KrakenSDR five-channel coherent receiver, processing Heimdall DAQ IQ streams to detect movement through obstacles in indoor environments. Bridges theoretical signal reflection research with a portable, real-time hardware implementation.</p>
</div>

</div>

## Health & Biometrics

<div class="project-grid">
<div class="project-card" data-search="healthypi ecosystem modular health monitoring ecosystem that translates raw biometric data from healthypi hardware (pi hat and wearable) into structured metrics for agent-driven analysis. swift collectors on apple devices capture healthkit data, publish to a nats broker, and python agents in containers run analysis pipelines — all coordinated by the [multi-agent](../multi-agent) orchestrator. python healthypi">
  <h3 class="card-title"><a href="projects/healthypi">HealthyPi Ecosystem</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-20</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Modular health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (Pi HAT and wearable) into structured metrics for agent-driven analysis. Swift collectors on Apple devices capture HealthKit data, publish to a NATS broker, and Python agents in containers run analysis pipelines — all coordinated by the [multi-agent](../multi-agent) orchestrator.</p>
</div>

</div>

## Astrophotography

<div class="project-grid">
<div class="project-card" data-search="aurora advisor decision tool for australian aurora observers that answers "should i drive 60 minutes to a dark site tonight?" combines real-time solar wind data (noaa swpc), substorm trigger detection (bz drops + hemispheric power jumps), and local weather forecasts (access-g model via open-meteo) into a single go/no-go score that accounts for both space weather potential and terrestrial conditions (cloud cover, moon phase, travel time). typescript auroradata">
  <h3 class="card-title"><a href="projects/auroradata">Aurora Advisor</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Decision tool for Australian aurora observers that answers "should I drive 60 minutes to a dark site tonight?" Combines real-time solar wind data (NOAA SWPC), substorm trigger detection (Bz drops + hemispheric power jumps), and local weather forecasts (ACCESS-G model via Open-Meteo) into a single Go/No-Go score that accounts for both space weather potential and terrestrial conditions (cloud cover, moon phase, travel time).</p>
</div>

<div class="project-card" data-search="auroraphoto automated astrophotography system for capturing aurora and night sky imagery. raspberry pi nodes connect via usb to sony a7r v / a7 iv cameras, controlled by an iphone companion app over wi-fi. the system provides automated focus using half-flux radius (hfr) star sharpness monitoring, exposure sequencing optimized for aurora bursts, and multi-node coordination from a single mobile interface.  auroraphoto">
  <h3 class="card-title"><a href="projects/auroraphoto">AuroraPhoto</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> </div>
  <p class="card-description">Automated astrophotography system for capturing aurora and night sky imagery. Raspberry Pi nodes connect via USB to Sony a7R V / a7 IV cameras, controlled by an iPhone companion app over Wi-Fi. The system provides automated focus using Half-Flux Radius (HFR) star sharpness monitoring, exposure sequencing optimized for aurora bursts, and multi-node coordination from a single mobile interface.</p>
</div>

<div class="project-card" data-search="eclipsephoto autonomous solar eclipse photography controller for raspberry pi. coordinates a camera (via gphoto2) and equatorial mount (zwo am5 / benro polaris via indi) to capture a complete eclipse sequence from first contact (c1) to fourth contact (c4) without manual intervention. the system handles solar guiding, exposure ramping, and error recovery so the photographer can watch the eclipse while the hardware secures the data. python eclipsephoto">
  <h3 class="card-title"><a href="projects/eclipsephoto">EclipsePhoto</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Autonomous solar eclipse photography controller for Raspberry Pi. Coordinates a camera (via gphoto2) and equatorial mount (ZWO AM5 / Benro Polaris via INDI) to capture a complete eclipse sequence from first contact (C1) to fourth contact (C4) without manual intervention. The system handles solar guiding, exposure ramping, and error recovery so the photographer can watch the eclipse while the hardware secures the data.</p>
</div>

<div class="project-card" data-search="eclipsestack alignment tool for solar eclipse hdr composites. takes hundreds of raw frames captured during totality and produces sub-pixel-aligned output ready for hdr stacking in pixinsight. addresses tracker drift by combining solar disk detection (computer vision) with temporal drift modeling from exif timestamps — the constant drift rate fills alignment gaps between confident frames. rust eclipsestack">
  <h3 class="card-title"><a href="projects/eclipsestack">EclipseStack</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Alignment tool for solar eclipse HDR composites. Takes hundreds of RAW frames captured during totality and produces sub-pixel-aligned output ready for HDR stacking in PixInsight. Addresses tracker drift by combining solar disk detection (computer vision) with temporal drift modeling from EXIF timestamps — the constant drift rate fills alignment gaps between confident frames.</p>
</div>

<div class="project-card" data-search="openastro core rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the openastro ecosystem. keeps coordinate math, imaging intelligence, and device behavior consistent across downstream applications (openastro node, photo tour). pure rust stack — no c toolchain required, testable without hardware. rust open-astro-core">
  <h3 class="card-title"><a href="projects/open-astro-core">OpenAstro Core</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. Keeps coordinate math, imaging intelligence, and device behavior consistent across downstream applications (OpenAstro Node, Photo Tour). Pure Rust stack — no C toolchain required, testable without hardware.</p>
</div>

<div class="project-card" data-search="openastro node headless, autonomous astrophotography controller for low-power linux devices (raspberry pi, jetson). manages camera and mount hardware, executes imaging sequences, and ensures rig safety through a "goodnight" protocol for unattended overnight sessions. uses openastro core for coordinate math, imaging intelligence, and device drivers. rust typescript open-astro-node">
  <h3 class="card-title"><a href="projects/open-astro-node">OpenAstro Node</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Headless, autonomous astrophotography controller for low-power Linux devices (Raspberry Pi, Jetson). Manages camera and mount hardware, executes imaging sequences, and ensures rig safety through a "Goodnight" protocol for unattended overnight sessions. Uses OpenAstro Core for coordinate math, imaging intelligence, and device drivers.</p>
</div>

<div class="project-card" data-search="satellites terminal-based satellite tracker that displays real-time positions on a world map, predicts passes over the user's location, and shows transmission frequencies. built with rust and ratatui, using the sgp4 orbital propagation algorithm to compute positions from two-line element (tle) data. a single binary with no gui dependencies — aimed at amateur radio operators and space enthusiasts. rust satellites">
  <h3 class="card-title"><a href="projects/satellites">Satellites</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Terminal-based satellite tracker that displays real-time positions on a world map, predicts passes over the user's location, and shows transmission frequencies. Built with Rust and ratatui, using the SGP4 orbital propagation algorithm to compute positions from Two-Line Element (TLE) data. A single binary with no GUI dependencies — aimed at amateur radio operators and space enthusiasts.</p>
</div>

</div>

## Photography

<div class="project-grid">
<div class="project-card" data-search="asiair import tool python script that automates post-imaging file organization for astrophotography. scans asiair backup locations (udisk/emmc across autorun, preview, plan, and live folders), reads fits headers to extract metadata, and organizes hundreds of frames by target and observation night into a directory structure ready for pixinsight's weighted batch preprocessing (wbpp) workflow.  import-asiair">
  <h3 class="card-title"><a href="projects/import-asiair">ASIAIR Import Tool</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-11</span> </div>
  <p class="card-description">Python script that automates post-imaging file organization for astrophotography. Scans ASIAIR backup locations (Udisk/EMMC across Autorun, Preview, Plan, and Live folders), reads FITS headers to extract metadata, and organizes hundreds of frames by target and observation night into a directory structure ready for PixInsight's Weighted Batch Preprocessing (WBPP) workflow.</p>
</div>

<div class="project-card" data-search="photo tour interactive photography assistant for field use on ios and ipados. provides live camera preview, manual motor control for landscape rigs, and a plugin architecture for composition overlays, exposure ramping, and intelligent triggering. built with swiftui and designed around a real-time control loop — see what the camera sees and act on it fast enough to improve the shot.  photo-tour">
  <h3 class="card-title"><a href="projects/photo-tour">Photo Tour</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> </div>
  <p class="card-description">Interactive photography assistant for field use on iOS and iPadOS. Provides live camera preview, manual motor control for landscape rigs, and a plugin architecture for composition overlays, exposure ramping, and intelligent triggering. Built with SwiftUI and designed around a real-time control loop — see what the camera sees and act on it fast enough to improve the shot.</p>
</div>

</div>

## Autonomous Systems

<div class="project-grid">
<div class="project-card" data-search="cycle agent native swiftui training application for ipad and apple tv that bridges a wahoo kickr core smart trainer with ai-driven workout logic. the app communicates with the trainer over bluetooth (ftms protocol) for real-time resistance control and telemetry, while a nats message bridge connects to an external agent for dynamic workout decisions. a scenekit-rendered infinite terrain visualization runs at 60fps on apple tv, with heart rate relay from apple watch completing the sensor loop.  cycle">
  <h3 class="card-title"><a href="projects/cycle">Cycle Agent</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-21</span> </div>
  <p class="card-description">Native SwiftUI training application for iPad and Apple TV that bridges a Wahoo KICKR Core smart trainer with AI-driven workout logic. The app communicates with the trainer over Bluetooth (FTMS protocol) for real-time resistance control and telemetry, while a NATS message bridge connects to an external agent for dynamic workout decisions. A SceneKit-rendered infinite terrain visualization runs at 60fps on Apple TV, with heart rate relay from Apple Watch completing the sensor loop.</p>
</div>

<div class="project-card" data-search="secure multi-agent personal assistant a security-first multi-agent system that coordinates specialized containerized agents through a nats message broker. each agent runs in isolation with minimal privileges — separate containers, scoped credentials, no direct agent-to-agent communication. the orchestrator uses cloud llm reasoning (gpt-4/claude) while agents remain lightweight and deterministic. python multi-agent">
  <h3 class="card-title"><a href="projects/multi-agent">Secure Multi-Agent Personal Assistant</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-21</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">A security-first multi-agent system that coordinates specialized containerized agents through a NATS message broker. Each agent runs in isolation with minimal privileges — separate containers, scoped credentials, no direct agent-to-agent communication. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.</p>
</div>

</div>

## Data & Utilities

<div class="project-grid">
<div class="project-card" data-search="nas cleanup & intelligence rust cli for managing large-scale synology nas file systems. performs duplicate detection (bit-for-bit and fuzzy), astrophotography file optimization (asiair workflow cleanup), conventional raw/sidecar management, and intelligent organization. designed for docker or native execution on dsm to minimize network latency during scanning. rust nascleanup">
  <h3 class="card-title"><a href="projects/nascleanup">NAS Cleanup & Intelligence</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Rust CLI for managing large-scale Synology NAS file systems. Performs duplicate detection (bit-for-bit and fuzzy), astrophotography file optimization (ASIair workflow cleanup), conventional RAW/sidecar management, and intelligent organization. Designed for Docker or native execution on DSM to minimize network latency during scanning.</p>
</div>

<div class="project-card" data-search="omnifocus db cli (omnifocus-db) python cli that reads directly from the omnifocus 4 sqlite database on macos, bypassing applescript and omni automation layers. provides near-instant retrieval of projects, inbox items, and tasks in structured, token-efficient formats (json/text) for agent consumption. read-only access by default to prevent database corruption while omnifocus is active. python typescript omnifocus-db">
  <h3 class="card-title"><a href="projects/omnifocus-db">OmniFocus DB CLI (omnifocus-db)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-16</span> <span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Python CLI that reads directly from the OmniFocus 4 SQLite database on macOS, bypassing AppleScript and Omni Automation layers. Provides near-instant retrieval of projects, inbox items, and tasks in structured, token-efficient formats (JSON/text) for agent consumption. Read-only access by default to prevent database corruption while OmniFocus is active.</p>
</div>

<div class="project-card" data-search="tileserver polars (rust optimized) dynamic vector tile server for massive geospatial datasets. serves mapbox vector tiles (mvt) from millions of points with sub-second latency, enabling interactive visualization in kepler.gl without pre-rendering static tilesets. python (fastapi) handles the api layer; rust (via pyo3) handles coordinate transformation and mvt encoding; polars provides in-memory filtering and aggregation. rust python polars tileserver">
  <h3 class="card-title"><a href="projects/tileserver">Tileserver Polars (Rust Optimized)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Dynamic vector tile server for massive geospatial datasets. Serves Mapbox Vector Tiles (MVT) from millions of points with sub-second latency, enabling interactive visualization in Kepler.gl without pre-rendering static tilesets. Python (FastAPI) handles the API layer; Rust (via PyO3) handles coordinate transformation and MVT encoding; Polars provides in-memory filtering and aggregation.</p>
</div>

<div class="project-card" data-search="weather (bom access pipeline) data engineering pipeline that fetches, processes, and serves weather model data from the australian bureau of meteorology. targets access (australian community climate and earth-system simulator) model outputs, bypassing bom's ftp delivery and binary formats (grib2/netcdf) to provide a queryable interface for localized weather forecasts. initial geographic focus on south australia. python polars weather">
  <h3 class="card-title"><a href="projects/weather">Weather (BOM ACCESS Pipeline)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-14</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Data engineering pipeline that fetches, processes, and serves weather model data from the Australian Bureau of Meteorology. Targets ACCESS (Australian Community Climate and Earth-System Simulator) model outputs, bypassing BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a queryable interface for localized weather forecasts. Initial geographic focus on South Australia.</p>
</div>

<div class="project-card" data-search="matrix-profile-rs matrix profile algorithms (stomp, scrimp++, scamp) in native rust for motif discovery and anomaly detection in time series data. achieves 2.5x speedup via simd (avx2/neon), handles datasets exceeding ram through memory-budgeted tiling, and integrates with polars as a native dataframe operation. 8,700 lines of rust. rust polars matrix-time-series">
  <h3 class="card-title"><a href="projects/matrix-time-series">matrix-profile-rs</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in native Rust for motif discovery and anomaly detection in time series data. Achieves 2.5x speedup via SIMD (AVX2/NEON), handles datasets exceeding RAM through memory-budgeted tiling, and integrates with Polars as a native DataFrame operation. 8,700 lines of Rust.</p>
</div>

</div>

## Wellness & Sound

<div class="project-grid">
<div class="project-card" data-search="overtone generative psytrance synthesis engine with real-time tui controls. creates complete tracks driven by a multi-level energy model (macro, meso, micro), with live playback, step editing, and wav export. procedural synthesis generates kick, bass, hihat, and clap patterns; an effects chain (sidechain compression, delay, reverb, hpf, limiter) and humanization (velocity jitter, micro-timing) produce output that sounds like a produced track rather than a sequencer demo. rust psytrance">
  <h3 class="card-title"><a href="projects/psytrance">Overtone</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model (macro, meso, micro), with live playback, step editing, and WAV export. Procedural synthesis generates kick, bass, hihat, and clap patterns; an effects chain (sidechain compression, delay, reverb, HPF, limiter) and humanization (velocity jitter, micro-timing) produce output that sounds like a produced track rather than a sequencer demo.</p>
</div>

<div class="project-card" data-search="wave (stillstate & flowstate) ambient audio ecosystem spanning apple watch and mac, designed for sleep and deep work. **stillstate** (watchos) is an adaptive sleep sounds app that generates procedural noise (white, brown, blended) with binaural beats, personalized frequency calibration, and heartbeat synchronization. microphone monitoring detects environmental noise for adaptive masking.  watch-noise">
  <h3 class="card-title"><a href="projects/watch-noise">Wave (StillState & FlowState)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-21</span> </div>
  <p class="card-description">Ambient audio ecosystem spanning Apple Watch and Mac, designed for sleep and deep work. **StillState** (watchOS) is an adaptive sleep sounds app that generates procedural noise (white, brown, blended) with binaural beats, personalized frequency calibration, and heartbeat synchronization. Microphone monitoring detects environmental noise for adaptive masking.</p>
</div>

</div>

## Experimental

<div class="project-grid">
<div class="project-card" data-search="rust tui gtd todo (omnifocus-inspired) keyboard-driven rust tui task manager built around a gtd workflow. stores tasks in a local sqlite database with support for projects, hierarchical tags, and availability-based next-action computation. optimized for rapid inbox processing — single-key field mode for triage, project/tag assignment, and batch operations with sub-second interactions at 10,000+ actions. rust todo">
  <h3 class="card-title"><a href="projects/todo">Rust TUI GTD Todo (OmniFocus-inspired)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-25</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Keyboard-driven Rust TUI task manager built around a GTD workflow. Stores tasks in a local SQLite database with support for projects, hierarchical tags, and availability-based next-action computation. Optimized for rapid inbox processing — single-key field mode for triage, project/tag assignment, and batch operations with sub-second interactions at 10,000+ actions.</p>
</div>

</div>


<!-- Styles in assets/css/main.css -->
<script>
function filterProjects() {
    var input, filter, cards, card, i, txtValue;
    input = document.getElementById('projectSearch');
    filter = input.value.toLowerCase();
    cards = document.getElementsByClassName('project-card');
    for (i = 0; i < cards.length; i++) {
        card = cards[i];
        txtValue = card.getAttribute('data-search');
        if (txtValue.indexOf(filter) > -1) { card.style.display = ""; } else { card.style.display = "none"; }
    }
}
</script>
    