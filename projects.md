---
layout: default
title: Projects
---

# Projects

Focused on network engineering, autonomous systems, and signal processing.

---

<div class="search-container"><input type="text" id="projectSearch" placeholder="Search projects, stack, or descriptions..." onkeyup="filterProjects()"></div>


## Radio Systems

<div class="project-grid">
<div class="project-card" data-search="radio streaming server cross-platform server (targeting raspberry pi) that manages multiple sdr devices (rtl-sdr, airspy hf+) and streams raw iq samples over the network using the `rtl_tcp` protocol. a single binary replaces multiple c-based streaming tools, adding a tui for live device management, toml configuration, and safe concurrency across all connected radios. existing c implementations (`rtl_tcp`, `hfp_tcp`) are single-threaded and require separate processes per device. rust rtltcp">
  <h3 class="card-title"><a href="projects/rtltcp">Radio Streaming Server</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-22</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Cross-platform server (targeting Raspberry Pi) that manages multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the `rtl_tcp` protocol. A single binary replaces multiple C-based streaming tools, adding a TUI for live device management, TOML configuration, and safe concurrency across all connected radios. Existing C implementations (`rtl_tcp`, `hfp_tcp`) are single-threaded and require separate processes per device.</p>
</div>

<div class="project-card" data-search="signal reflection - krakensdr multi-beam system distributed multi-beam signal reflection analysis system built on krakensdr hardware. a raspberry pi handles data acquisition and streams iq data over udp; a mac or linux workstation runs compute-intensive dsp. all four surveillance channels process in parallel with independent range-doppler visualization, per-beam configuration, and real-time performance monitoring. rust python rf-signal-analysis">
  <h3 class="card-title"><a href="projects/rf-signal-analysis">Signal Reflection - KrakenSDR Multi-Beam System</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-09</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Distributed multi-beam signal reflection analysis system built on KrakenSDR hardware. A Raspberry Pi handles data acquisition and streams IQ data over UDP; a Mac or Linux workstation runs compute-intensive DSP. All four surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring.</p>
</div>

<div class="project-card" data-search="sound array audio processing system using raspberry pi and microphone arrays for spatial sound analysis. captures multi-channel audio from usb/hat arrays (respeaker, matrix), computes time of arrival (toa) for sound localization, and applies beamforming for directional isolation. classifies sources — vehicles (engine sounds), aircraft, wildlife (birds) — and streams processed audio or metadata to a remote desktop for analysis.  soundarray">
  <h3 class="card-title"><a href="projects/soundarray">Sound Array</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> </div>
  <p class="card-description">Audio processing system using Raspberry Pi and microphone arrays for spatial sound analysis. Captures multi-channel audio from USB/HAT arrays (ReSpeaker, Matrix), computes Time of Arrival (ToA) for sound localization, and applies beamforming for directional isolation. Classifies sources — vehicles (engine sounds), aircraft, wildlife (birds) — and streams processed audio or metadata to a remote desktop for analysis.</p>
</div>

<div class="project-card" data-search="spectrum analysis automated signal census system that transforms raw radio spectrum data into classified, searchable signal inventories. combines sdr acquisition, ml classification, and vector search to detect, identify, and catalog signals across monitored bands. rust python signals">
  <h3 class="card-title"><a href="projects/signals">Spectrum Analysis</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-10</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
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
<div class="project-card" data-search="healthypi ecosystem modular health monitoring ecosystem that translates raw biometric data from healthypi hardware (pi hat and wearable) into structured metrics for agent-driven analysis. swift collectors on apple devices capture healthkit data, publish to a nats broker, and python agents in containers run analysis pipelines over the resulting stream. python healthypi">
  <h3 class="card-title"><a href="projects/healthypi">HealthyPi Ecosystem</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-20</span> <span class="stack-badge">Python</span></div>
  <p class="card-description">Modular health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (Pi HAT and wearable) into structured metrics for agent-driven analysis. Swift collectors on Apple devices capture HealthKit data, publish to a NATS broker, and Python agents in containers run analysis pipelines over the resulting stream.</p>
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

<div class="project-card" data-search="eclipsestack: expertise-led solar alignment alignment tool for solar eclipse hdr composites. takes hundreds of raw frames captured during totality and produces sub-pixel-aligned output ready for hdr stacking in pixinsight. addresses tracker drift by combining solar disk detection (computer vision) with temporal drift modeling from exif timestamps — the constant drift rate fills alignment gaps between confident frames. rust typescript eclipsestack">
  <h3 class="card-title"><a href="projects/eclipsestack">EclipseStack: Expertise-Led Solar Alignment</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Alignment tool for solar eclipse HDR composites. Takes hundreds of RAW frames captured during totality and produces sub-pixel-aligned output ready for HDR stacking in PixInsight. Addresses tracker drift by combining solar disk detection (computer vision) with temporal drift modeling from EXIF timestamps — the constant drift rate fills alignment gaps between confident frames.</p>
</div>

<div class="project-card" data-search="openastro node headless, autonomous astrophotography controller for low-power linux devices (raspberry pi, jetson). manages camera and mount hardware, executes imaging sequences, and ensures rig safety through a "goodnight" protocol for unattended overnight sessions. uses openastro core for coordinate math, imaging intelligence, and device drivers. rust typescript open-astro-node">
  <h3 class="card-title"><a href="projects/open-astro-node">OpenAstro Node</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Headless, autonomous astrophotography controller for low-power Linux devices (Raspberry Pi, Jetson). Manages camera and mount hardware, executes imaging sequences, and ensures rig safety through a "Goodnight" protocol for unattended overnight sessions. Uses OpenAstro Core for coordinate math, imaging intelligence, and device drivers.</p>
</div>

<div class="project-card" data-search="satellites terminal-based satellite tracker that displays real-time positions on a world map, predicts passes over the user's location, and shows transmission frequencies. built with rust and ratatui, using the sgp4 orbital propagation algorithm to compute positions from two-line element (tle) data. a single binary with no gui dependencies — aimed at amateur radio operators and space enthusiasts. rust satellites">
  <h3 class="card-title"><a href="projects/satellites">Satellites</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-09</span> <span class="stack-badge">Rust</span></div>
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
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-16</span> </div>
  <p class="card-description">Native SwiftUI training application for iPad and Apple TV that bridges a Wahoo KICKR Core smart trainer with AI-driven workout logic. The app communicates with the trainer over Bluetooth (FTMS protocol) for real-time resistance control and telemetry, while a NATS message bridge connects to an external agent for dynamic workout decisions. A SceneKit-rendered infinite terrain visualization runs at 60fps on Apple TV, with heart rate relay from Apple Watch completing the sensor loop.</p>
</div>

</div>

## Data & Utilities

<div class="project-grid">
<div class="project-card" data-search="dataraster (data-raster) a rust-native server-side rasterization library and toolset for rendering datasets of millions to billions of points into density-aware raster images and map tiles. inspired by datashader's pioneering concepts but rebuilt from scratch on a modern polars/arrow/rayon stack, eliminating jit warmup latency, the numba/dask dependency chain, and python-only deployment constraints. shipped as v1.0: a rust library crate, cli tool, http tile server, and python package. rust polars datavis">
  <h3 class="card-title"><a href="projects/datavis">DataRaster (data-raster)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-22</span> <span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">A Rust-native server-side rasterization library and toolset for rendering datasets of millions to billions of points into density-aware raster images and map tiles. Inspired by Datashader's pioneering concepts but rebuilt from scratch on a modern Polars/Arrow/Rayon stack, eliminating JIT warmup latency, the Numba/Dask dependency chain, and Python-only deployment constraints. Shipped as v1.0: a Rust library crate, CLI tool, HTTP tile server, and Python package.</p>
</div>

<div class="project-card" data-search="nas cleanup & intelligence rust cli for managing large-scale synology nas file systems. performs duplicate detection (bit-for-bit and fuzzy), astrophotography file optimization (asiair workflow cleanup), conventional raw/sidecar management, and intelligent organization. designed for docker or native execution on dsm to minimize network latency during scanning. rust nascleanup">
  <h3 class="card-title"><a href="projects/nascleanup">NAS Cleanup & Intelligence</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-03</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Rust CLI for managing large-scale Synology NAS file systems. Performs duplicate detection (bit-for-bit and fuzzy), astrophotography file optimization (ASIair workflow cleanup), conventional RAW/sidecar management, and intelligent organization. Designed for Docker or native execution on DSM to minimize network latency during scanning.</p>
</div>

<div class="project-card" data-search="omnifocus db cli (omnifocus-db) python cli that reads directly from the omnifocus 4 sqlite database on macos, bypassing applescript and omni automation layers. provides near-instant retrieval of projects, inbox items, and tasks in structured, token-efficient formats (json/text) for agent consumption. read-only access by default to prevent database corruption while omnifocus is active. python typescript omnifocus-db">
  <h3 class="card-title"><a href="projects/omnifocus-db">OmniFocus DB CLI (omnifocus-db)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-16</span> <span class="stack-badge">Python</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Python CLI that reads directly from the OmniFocus 4 SQLite database on macOS, bypassing AppleScript and Omni Automation layers. Provides near-instant retrieval of projects, inbox items, and tasks in structured, token-efficient formats (JSON/text) for agent consumption. Read-only access by default to prevent database corruption while OmniFocus is active.</p>
</div>

<div class="project-card" data-search="tileserver polars (rust optimized) a dynamic vector tile server for massive geospatial datasets. it serves mapbox
vector tiles (mvt) from millions of points with sub-second latency, enabling
interactive visualisation in kepler.gl and maplibre without pre-rendering a
static tile set. python (fastapi) handles the http layer; rust (via pyo3) does
coordinate projection and protobuf encoding; polars holds the data and runs the
spatial filters. rust python polars tileserver">
  <h3 class="card-title"><a href="projects/tileserver">Tileserver Polars (Rust Optimized)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">A dynamic vector tile server for massive geospatial datasets. It serves Mapbox
Vector Tiles (MVT) from millions of points with sub-second latency, enabling
interactive visualisation in Kepler.gl and MapLibre without pre-rendering a
static tile set. Python (FastAPI) handles the HTTP layer; Rust (via PyO3) does
coordinate projection and Protobuf encoding; Polars holds the data and runs the
spatial filters.</p>
</div>

<div class="project-card" data-search="weather (bom access pipeline) data engineering pipeline that fetches, processes, and serves weather model data from the australian bureau of meteorology. targets access (australian community climate and earth-system simulator) model outputs, bypassing bom's ftp delivery and binary formats (grib2/netcdf) to provide a queryable interface for localized weather forecasts. initial geographic focus on south australia. python polars weather">
  <h3 class="card-title"><a href="projects/weather">Weather (BOM ACCESS Pipeline)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-14</span> <span class="stack-badge">Python</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Data engineering pipeline that fetches, processes, and serves weather model data from the Australian Bureau of Meteorology. Targets ACCESS (Australian Community Climate and Earth-System Simulator) model outputs, bypassing BOM's FTP delivery and binary formats (GRIB2/NetCDF) to provide a queryable interface for localized weather forecasts. Initial geographic focus on South Australia.</p>
</div>

<div class="project-card" data-search="matrix-profile-rs the matrix profile is a single transform that exposes a time series' repeated
patterns and its anomalies. it annotates every subsequence with the distance to
its nearest match elsewhere in the series: low values mark **motifs** (a shape
that recurs), high values mark **discords** (a shape unlike any other). it
needs no training, no labelled data, and no domain-specific parameters. rust polars matrix-time-series">
  <h3 class="card-title"><a href="projects/matrix-time-series">matrix-profile-rs</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-04-30</span> <span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">The matrix profile is a single transform that exposes a time series' repeated
patterns and its anomalies. It annotates every subsequence with the distance to
its nearest match elsewhere in the series: low values mark **motifs** (a shape
that recurs), high values mark **discords** (a shape unlike any other). It
needs no training, no labelled data, and no domain-specific parameters.</p>
</div>

</div>

## Wellness & Sound

<div class="project-grid">
<div class="project-card" data-search="overtone generative psytrance synthesis engine with real-time tui controls. creates complete tracks driven by a multi-level energy model (macro, meso, micro), with live playback, step editing, and wav export. procedural synthesis generates kick, bass, hihat, and clap patterns; an effects chain (sidechain compression, delay, reverb, hpf, limiter) and humanization (velocity jitter, micro-timing) produce output that sounds like a produced track rather than a sequencer demo. rust psytrance">
  <h3 class="card-title"><a href="projects/psytrance">Overtone</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span></div>
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
<div class="project-card" data-search="asana: real-time yoga pose analysis with rust a desktop and mobile application that uses a webcam or phone camera to provide real-time yoga pose estimation, alignment correction, biomechanical analysis, and intelligent sequence building. the system spans seven architectural layers: perception, intelligence, knowledge, feedback, longitudinal analytics, platform ecosystem, and creative frontiers. targets individual practitioners, instructors, and students. rust yoga">
  <h3 class="card-title"><a href="projects/yoga">Asana: Real-Time Yoga Pose Analysis with Rust</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-16</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">A desktop and mobile application that uses a webcam or phone camera to provide real-time yoga pose estimation, alignment correction, biomechanical analysis, and intelligent sequence building. The system spans seven architectural layers: perception, intelligence, knowledge, feedback, longitudinal analytics, platform ecosystem, and creative frontiers. Targets individual practitioners, instructors, and students.</p>
</div>

<div class="project-card" data-search="high-fidelity photometric synthesis suite a phd-led, professional-grade photometric synthesis engine for timelapse photography. it transforms raw sequences into cinematic video through a rigorous 16-bit linear pipeline, utilizing pchip temporal ramping, wide-gamut (rec.2020) color management, and stochastic dithering. it goes beyond simple "deflickering" to provide deep photometric insights, radial vignette normalization, and temporal "hallucination" for corrupt frame continuity. rust timelapse">
  <h3 class="card-title"><a href="projects/timelapse">High-Fidelity Photometric Synthesis Suite</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-03-30</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">A PhD-led, professional-grade photometric synthesis engine for timelapse photography. It transforms RAW sequences into cinematic video through a rigorous 16-bit linear pipeline, utilizing PCHIP temporal ramping, wide-gamut (Rec.2020) color management, and stochastic dithering. It goes beyond simple "deflickering" to provide deep photometric insights, radial vignette normalization, and temporal "hallucination" for corrupt frame continuity.</p>
</div>

<div class="project-card" data-search="musicbrain musicbrain is a desktop music-analysis workbench for studying recorded tracks and, in alpha form, live input. the implemented product already goes beyond the original offline-only brief: it includes offline analysis, report and dna export, session persistence, track comparison, an optional demucs cli stem workflow, and a live dashboard path. this file is now the authoritative current-scope document. rust musicanalysis">
  <h3 class="card-title"><a href="projects/musicanalysis">MusicBrain</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-04-10</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">MusicBrain is a desktop music-analysis workbench for studying recorded tracks and, in alpha form, live input. The implemented product already goes beyond the original offline-only brief: it includes offline analysis, report and DNA export, session persistence, track comparison, an optional Demucs CLI stem workflow, and a live dashboard path. This file is now the authoritative current-scope document.</p>
</div>

<div class="project-card" data-search="rust tui gtd todo (omnifocus-inspired) keyboard-driven rust tui task manager built around a gtd workflow. stores tasks in a local sqlite database with support for projects, hierarchical tags, and availability-based next-action computation. optimized for rapid inbox processing — single-key field mode for triage, project/tag assignment, and batch operations with sub-second interactions at 10,000+ actions. rust todo">
  <h3 class="card-title"><a href="projects/todo">Rust TUI GTD Todo (OmniFocus-inspired)</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-02-25</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">Keyboard-driven Rust TUI task manager built around a GTD workflow. Stores tasks in a local SQLite database with support for projects, hierarchical tags, and availability-based next-action computation. Optimized for rapid inbox processing — single-key field mode for triage, project/tag assignment, and batch operations with sub-second interactions at 10,000+ actions.</p>
</div>

<div class="project-card" data-search="yogaclass: teaching practice companion a desktop tool for yoga teachers to practise teaching their classes and get feedback on delivery. the teacher loads a class sequence, sees 3d animated student figures in the poses, speaks through the class out loud, and the app tracks their delivery via voice recognition — then provides feedback on timing, pacing, cue quality, sequence adherence, and overall flow. it also provides pre-class analysis: intensity arcs, muscle coverage, safety checks, and compositional insights. rust python yogaclass">
  <h3 class="card-title"><a href="projects/yogaclass">Yogaclass: Teaching Practice Companion</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Active</span> <span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">A desktop tool for yoga teachers to practise teaching their classes and get feedback on delivery. The teacher loads a class sequence, sees 3D animated student figures in the poses, speaks through the class out loud, and the app tracks their delivery via voice recognition — then provides feedback on timing, pacing, cue quality, sequence adherence, and overall flow. It also provides pre-class analysis: intensity arcs, muscle coverage, safety checks, and compositional insights.</p>
</div>

<div class="project-card" data-search="netsequence netsequence is being built into a production-ready change orchestration product for service-provider networks. it sits between structural change generation and operational deployment, turning topology mutations into risk-assessed, dependency-aware, verifiable execution plans with rollback. the product direction is external, not just internal tooling: the goal is to deliver something carrier engineering teams can trust during real maintenance work. rust netsequence">
  <h3 class="card-title"><a href="projects/netsequence">netsequence</a></h3>
  <div class="badges-row card-badges"><span class="status-badge status-active">Last Active: 2026-04-12</span> <span class="stack-badge">Rust</span></div>
  <p class="card-description">netsequence is being built into a production-ready change orchestration product for service-provider networks. It sits between structural change generation and operational deployment, turning topology mutations into risk-assessed, dependency-aware, verifiable execution plans with rollback. The product direction is external, not just internal tooling: the goal is to deliver something carrier engineering teams can trust during real maintenance work.</p>
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
    