---
layout: default
---

# Projects

Tools for network engineering, signal processing, photography, and autonomous systems.

---

<div class="search-container"><input type="text" id="projectSearch" placeholder="Search projects, stack, or descriptions..." onkeyup="filterProjects()"></div>

## Recent Activity

<ul class="recent-activity-list">
<li><strong>2026-03-05</strong>: <a href="projects/configparsing">Brownfield Ingestion & Analysis</a> — <em>Completed 07-01-PLAN.md</em></li>
<li><strong>2026-03-05</strong>: <a href="projects/netassure">Network Analysis Engine</a> — <em>Completed 02-02-PLAN.md</em></li>
<li><strong>2026-03-05</strong>: <a href="projects/netflowsim">Performance Simulator</a> — <em>Archived Criterion 50k/75k/100k reports;  near-complete</em></li>
<li><strong>2026-03-05</strong>: <a href="projects/netsim">Network Simulator</a> — <em>Code hygiene + test stabilization + clippy cleanup PR merged</em></li>
<li><strong>2026-03-05</strong>: <a href="projects/orchestrator">Orchestrator (Device Interaction Runner)</a> — <em>2026-03-05 - Completed 02-05-PLAN.md</em></li>
</ul>

---

## Network Automation

<div class="project-grid">
<div class="project-card" data-search="automation workbench **an orchestration platform** that integrates the ank ecosystem tools (topogen, ank_pydantic, network simulator, netvis) into a unified workflow. ank workbench is the integration layer that coordinates the entire network automation pipeline. engineers can generate topologies, model networks declaratively, run lightweight simulations, and visualize results—all from a unified web interface. python typescript ank-workbench">
  <h3 class="card-title"><a href="projects/ank-workbench">Automation Workbench</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">An orchestration platform that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into a unified workflow for topology generation, declarative modeling, simulation, and visualization.</p>
</div>

<div class="project-card" data-search="brownfield ingestion & analysis a network automation framework that decouples network configuration from vendor-specific syntax. it uses llm-powered rag to extract network-level intent and topology relationships from vendor documentation and cli configurations, normalizing them into a vendor-neutral topology graph model inspired by autonetkit. the system enables cross-vendor configuration generation and validation through semantic simulation. python configparsing">
  <h3 class="card-title"><a href="projects/configparsing">Brownfield Ingestion & Analysis</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Extracts network-level intent and topology relationships from vendor documentation and CLI configurations using LLM-powered RAG, normalizing them into a vendor-neutral graph model for cross-vendor configuration generation.</p>
</div>

<div class="project-card" data-search="network simulator deterministic tick-based network protocol simulator validating configurations before production deployment. it provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full vm emulation. rust netsim">
  <h3 class="card-title"><a href="projects/netsim">Network Simulator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Deterministic tick-based protocol simulator that validates routing configurations (OSPF, IS-IS, BGP) before deployment. Protocol-level fidelity with same-topology-same-results guarantees.</p>
</div>

<div class="project-card" data-search="network modeling & configuration library a python library for modeling and querying network topologies, backed by a rust core. features a two-stage transformation model, type-safe pydantic models for nodes/edges/layers, and a composable lazy query api with rust-backed execution. python polars ank-pydantic">
  <h3 class="card-title"><a href="projects/ank-pydantic">Network Modeling & Configuration Library</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Python library for modeling and querying network topologies, backed by a Rust graph engine. Two-stage transformation model (Whiteboard to Plan to Protocol Layers) with composable lazy query API and domain models for IS-IS, MPLS, EVPN.</p>
</div>

<div class="project-card" data-search="visualization engine a rust-based network topology layout and visualization engine. takes complex multi-layer network topologies and renders them using advanced layout algorithms that reduce visual complexity while preserving structural clarity. rust python typescript netvis">
  <h3 class="card-title"><a href="projects/netvis">Visualization Engine</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <img src="../images/hero-diagram.svg" class="project-thumbnail" alt="Visualization Engine diagram" />
  <p class="card-description">Layout engine for dense, multi-layer network topologies. Edge bundling, hierarchical stacking, and geographic positioning with SVG, PDF, and PNG output.</p>
</div>

<div class="project-card" data-search="network configuration framework deterministic, auditable, ci/cd-friendly rust cli for compiling declarative yaml network blueprints into vendor-neutral configuration artifacts. rust ank-netcfg">
  <h3 class="card-title"><a href="projects/ank-netcfg">Network Configuration Framework</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Deterministic, auditable Rust CLI for compiling declarative YAML network blueprints into vendor-neutral configuration artifacts through a blueprint-to-template pipeline.</p>
</div>

<div class="project-card" data-search="topology engine core nte network topology engine rust-based graph topology engine with python bindings via pyo3. rust python typescript polars ank-nte">
  <h3 class="card-title"><a href="projects/ank-nte">Topology Engine Core</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Rust graph engine (14-crate workspace) with Python bindings via PyO3. Built on petgraph StableDiGraph with pluggable datastores (Polars, DuckDB, Lite).</p>
</div>

<div class="project-card" data-search="device interaction framework a rust library and cli for network device interaction and automated testing. rust deviceinteraction">
  <h3 class="card-title"><a href="projects/deviceinteraction">Device Interaction Framework</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Rust library and CLI for network device interaction and automated testing. Testbed management, CLI parsing, and state verification as a focused alternative to PyATS.</p>
</div>

<div class="project-card" data-search="orchestrator device interaction runner an orchestration runner for coordinating device interactions across real/testbed networks. python orchestrator">
  <h3 class="card-title"><a href="projects/orchestrator">Orchestrator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Orchestration runner for coordinating device interactions across real and testbed networks with retries, timeouts, bounded concurrency, and durable artifacts.</p>
</div>

<div class="project-card" data-search="topology generator rust-based network topology generator with python bindings. generates realistic data center, wan, and random graph topologies. rust python topogen">
  <h3 class="card-title"><a href="projects/topogen">Topology Generator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Generates realistic data center, WAN, and random graph topologies with proper structure and realistic parameters. Custom YAML output for the network engineering ecosystem.</p>
</div>

<div class="project-card" data-search="cli parser a parsing engine for network device output. transforms semi-structured cli text into structured data. rust cliscrape">
  <h3 class="card-title"><a href="projects/cliscrape">CLI Parser</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Transforms semi-structured network device CLI output into structured data (JSON/YAML) using an optimized state machine. Ergonomic alternative to TextFSM.</p>
</div>

<div class="project-card" data-search="performance simulator flow-level network performance simulation. rust netflowsim">
  <h3 class="card-title"><a href="projects/netflowsim">Performance Simulator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Flow-level network performance simulation for capacity planning and traffic analysis. Queuing models and Monte Carlo simulations across large topologies.</p>
</div>

<div class="project-card" data-search="network analysis engine gnn topology analysis anomaly detection traffic prediction rust polars netassure">
  <h3 class="card-title"><a href="projects/netassure">Network Analysis Engine</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">GNN-based network analytics extending the Network Topology Engine with anomaly detection, traffic prediction, and topology learning.</p>
</div>

<div class="project-card" data-search="network automation ecosystem architecture defines the architecture of the network automation ecosystem. automationarch">
  <h3 class="card-title"><a href="projects/automationarch">Ecosystem Architecture</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> </div>
  <p class="card-description">Defines how Topology Generator, AutoNetKit, Network Simulator, Performance Simulator, Visualization Engine, and Automation Workbench integrate into a cohesive pipeline.</p>
</div>

</div>

## Signal Processing

<div class="project-grid">
<div class="project-card" data-search="wi-fi signal reflection krakensdr signal reflection system wifi through-wall detection rust python wifi-signal-analysis">
  <h3 class="card-title"><a href="projects/wifi-signal-analysis">Wi-Fi Signal Reflection (KrakenSDR)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Signal reflection system using existing Wi-Fi signals for through-wall human detection and localization, leveraging the KrakenSDR coherent radio array.</p>
</div>

<div class="project-card" data-search="signal reflection krakensdr multi-beam system distributed multi-beam signal reflection analysis system. rust python rf-signal-analysis">
  <h3 class="card-title"><a href="projects/rf-signal-analysis">Signal Reflection - Multi-Beam System</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Distributed multi-beam signal reflection analysis based on KrakenSDR hardware. Four parallel reflection channels with independent Range-Doppler visualization and real-time monitoring.</p>
</div>

<div class="project-card" data-search="radio streaming server multi-sdr rtl_tcp protocol streaming server. rust rtltcp">
  <h3 class="card-title"><a href="projects/rtltcp">Radio Streaming Server</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Cross-platform server (Raspberry Pi-targeted) for streaming raw IQ samples from multiple SDR devices over the rtl_tcp protocol, with a built-in TUI for live configuration.</p>
</div>

<div class="project-card" data-search="spectrum analysis signal census radio spectrum monitoring python signals">
  <h3 class="card-title"><a href="projects/signals">Spectrum Analysis</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <img src="../images/search_topk_example.png" class="project-thumbnail" alt="Spectrum Analysis diagram" />
  <p class="card-description">Transforms raw radio spectrum data into an actionable signal census through automated detection, ML classification, and distributed acquisition.</p>
</div>

<div class="project-card" data-search="healthypi ecosystem biometric health monitoring ecg ppg python healthypi">
  <h3 class="card-title"><a href="projects/healthypi">HealthyPi Ecosystem</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-20</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Modular health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights through synthetic data simulation and agentic intelligence.</p>
</div>

<div class="project-card" data-search="psytrance generator generative psytrance synthesis engine tui controls rust psytrance">
  <h3 class="card-title"><a href="projects/psytrance">Psytrance Generator</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Generative psytrance synthesis engine with real-time TUI controls. Multi-level energy model drives complete track generation with live playback, step editing, and WAV export.</p>
</div>

<div class="project-card" data-search="wave stillstate flowstate ambient audio sleep sounds apple watch watch-noise">
  <h3 class="card-title"><a href="projects/watch-noise">Wave (StillState & FlowState)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> </div>
  <p class="card-description">Ambient audio ecosystem for managing sensory environment across rest and work. Adaptive sleep sounds on Apple Watch with frequency calibration and heartbeat synchronization.</p>
</div>

<div class="project-card" data-search="sound array spatial audio raspberry pi microphone arrays beamforming classification soundarray">
  <h3 class="card-title"><a href="projects/soundarray">Sound Array</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> </div>
  <p class="card-description">Audio processing system using Raspberry Pi and microphone arrays for spatial audio (ToA, beamforming) and sound classification (vehicles, wildlife).</p>
</div>

</div>

## Photography

<div class="project-grid">
<div class="project-card" data-search="openastro node headless autonomous astrophotography controller rpi jetson rust typescript open-astro-node">
  <h3 class="card-title"><a href="projects/open-astro-node">OpenAstro Node</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Headless, autonomous astrophotography controller for low-power Linux devices (RPi/Jetson). Manages hardware, executes imaging sequences, and ensures rig safety.</p>
</div>

<div class="project-card" data-search="openastro core shared astronomical logic hardware drivers protocol implementations rust open-astro-core">
  <h3 class="card-title"><a href="projects/open-astro-core">OpenAstro Core</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Rust library providing shared astronomical logic, hardware drivers, and protocol implementations (INDI, ASCOM Alpaca) for the OpenAstro ecosystem.</p>
</div>

<div class="project-card" data-search="auroraphoto automated aurora capture raspberry pi sony cameras iphone auroraphoto">
  <h3 class="card-title"><a href="projects/auroraphoto">AuroraPhoto</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> </div>
  <p class="card-description">Automated aurora photography system using Raspberry Pi nodes controlling Sony cameras via USB, with an iPhone companion app for multi-node management.</p>
</div>

<div class="project-card" data-search="aurora advisor australian aurora observers solar wind noaa weather typescript auroradata">
  <h3 class="card-title"><a href="projects/auroradata">Aurora Advisor</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Combines real-time solar wind data (NOAA), substorm trigger logic, and local weather (ACCESS-G) to advise Australian aurora observers on whether conditions warrant a trip.</p>
</div>

<div class="project-card" data-search="eclipsephoto autonomous solar eclipse photography raspberry pi gphoto2 indi python eclipsephoto">
  <h3 class="card-title"><a href="projects/eclipsephoto">EclipsePhoto</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Autonomous Raspberry Pi-based controller for solar eclipse photography. Coordinates camera and mount to capture a complete C1-to-C4 sequence without manual intervention.</p>
</div>

<div class="project-card" data-search="eclipsestack solar eclipse image alignment hdr stacking tracker drift rust eclipsestack">
  <h3 class="card-title"><a href="projects/eclipsestack">EclipseStack</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Aligns hundreds of RAW solar eclipse images by combining solar disk detection with temporal drift modeling from EXIF data, producing frames ready for HDR stacking in PixInsight.</p>
</div>

<div class="project-card" data-search="satellites terminal-based satellite tracker real-time positions sgp4 orbital propagation rust satellites">
  <h3 class="card-title"><a href="projects/satellites">Satellites</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Terminal-based satellite tracker displaying real-time positions on a world map with pass predictions, transmission data, and SGP4 orbital propagation.</p>
</div>

<div class="project-card" data-search="astrophotography site planner celestial events bortle light pollution adelaide typescript react siteplanning">
  <h3 class="card-title"><a href="projects/siteplanning">Astrophotography Site Planner</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">TypeScript</span><span class="stack-badge">React</span></div>
  <p class="card-description">Planning tool combining celestial event calculations with Bortle-scale light pollution data and 50+ surveyed Adelaide sites to recommend optimal astrophotography locations and times.</p>
</div>

<div class="project-card" data-search="photo tour interactive photography assistant field use composition workflow photo-tour">
  <h3 class="card-title"><a href="projects/photo-tour">Photo Tour</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> </div>
  <p class="card-description">Interactive field photography assistant for composing shots, automating repeatable workflows, and providing intelligent triggering and transition logic.</p>
</div>

<div class="project-card" data-search="asiair import tool astrophotography file organization fits wbpp pixinsight import-asiair">
  <h3 class="card-title"><a href="projects/import-asiair">ASIAIR Import Tool</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-11</span> </div>
  <p class="card-description">Automates post-session file organization for astrophotography. Batch-imports FITS files, organizes by target and observation night, and prepares directory structure for PixInsight WBPP.</p>
</div>

</div>

## Data & Analytics

<div class="project-grid">
<div class="project-card" data-search="tileserver polars geospatial vector tiles mvt kepler rust python polars tileserver">
  <h3 class="card-title"><a href="projects/tileserver">Tileserver Polars</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Serves dynamic vector tiles (MVT) from massive geospatial datasets with sub-second latency, enabling interactive Kepler.gl visualization without pre-rendering static tilesets.</p>
</div>

<div class="project-card" data-search="matrix-profile-rs time series analysis stomp scrimp scamp motif discovery anomaly detection rust polars matrix-time-series">
  <h3 class="card-title"><a href="projects/matrix-time-series">matrix-profile-rs</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Matrix Profile algorithms (STOMP, SCRIMP++, SCAMP) in Rust for time series motif discovery and anomaly detection. 2.5x SIMD speedup with Polars integration.</p>
</div>

<div class="project-card" data-search="weather bom access pipeline data engineering australian bureau of meteorology python polars weather">
  <h3 class="card-title"><a href="projects/weather">Weather (BOM ACCESS Pipeline)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-14</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Data engineering pipeline to fetch, process, and serve high-resolution weather model data from the Australian Bureau of Meteorology ACCESS model.</p>
</div>

<div class="project-card" data-search="nas cleanup intelligence synology duplicate detection astrophotography optimization rust nascleanup">
  <h3 class="card-title"><a href="projects/nascleanup">NAS Cleanup & Intelligence</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Rust CLI for managing large-scale Synology NAS file systems: duplicate detection, astrophotography optimization, RAW photography management, and intelligent organization.</p>
</div>

<div class="project-card" data-search="omnifocus db cli sqlite database macos python typescript omnifocus-db">
  <h3 class="card-title"><a href="projects/omnifocus-db">OmniFocus DB CLI</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-16</span> <span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Reads directly from the OmniFocus SQLite database on macOS, providing structured, token-efficient data to agents for project listing, inbox analysis, and context gathering.</p>
</div>

<div class="project-card" data-search="rust tui gtd todo omnifocus-inspired sqlite keyboard-driven task manager rust todo">
  <h3 class="card-title"><a href="projects/todo">GTD Todo (OmniFocus-inspired)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Keyboard-driven Rust TUI task manager built around GTD workflow. SQLite-backed with hierarchical contexts/tags and an OmniFocus 4 importer for one-time migration.</p>
</div>

</div>

## Autonomous Systems

<div class="project-grid">
<div class="project-card" data-search="secure multi-agent personal assistant containerized agents health monitoring home automation message broker python multi-agent">
  <h3 class="card-title"><a href="projects/multi-agent">Multi-Agent Personal Assistant</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Security-first multi-agent system coordinating containerized agents (health, home, data, workflow) through a message broker architecture with isolation and validated message queues.</p>
</div>

<div class="project-card" data-search="cycle agent swiftui training application ipad apple tv kickr core nats scenekit cycle">
  <h3 class="card-title"><a href="projects/cycle">Cycle Agent</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Recently Updated</span> </div>
  <p class="card-description">Native SwiftUI training application for iPad and Apple TV bridging professional cycling hardware (KICKR Core) with AI-driven workout logic via NATS, visualized in SceneKit.</p>
</div>

</div>


<!-- Styles moved to assets/css/main.css -->
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
