---
layout: default
---

# Photography & Astrophotography Ecosystem

Integrated tools for field photography, astrophotography automation, and image processing workflows.

## Contents
- [The Vision](#the-vision)
- [How They Work Together](#how-they-work-together)
- [Astrophotography](#astrophotography)
  - [AuroraPhoto — Automated Aurora Capture](#auroraphoto--automated-aurora-capture)
  - [OpenAstro Node — Autonomous Observatory](#openastro-node--autonomous-observatory)
  - [OpenAstro Core — Shared Astronomical Logic](#openastro-core--shared-astronomical-logic)
  - [EclipseStack — High-Precision Alignment](#eclipsestack--high-precision-alignment)
  - [ASIAIR Import Tool — Workflow Automation](#asiair-import-tool--workflow-automation)
- [Field Photography](#field-photography)
  - [Photo Tour — Interactive Assistant](#photo-tour--interactive-assistant)
- [Philosophy](#philosophy-why-this-approach)

---

## The Vision

Photography—whether capturing aurora bursts in sub-zero conditions or composing landscape shots in the field—demands tools that handle technical complexity while staying out of the creative flow. This ecosystem provides automation where it matters (focus, exposure, sequencing) and intelligent assistance where judgment is needed (composition, timing).

**Core Philosophy:**
- **Autonomous where possible**: Automated focus, exposure sequencing, hardware management
- **Assistive where valuable**: Composition guidance, timing suggestions, workflow optimization
- **Field-ready**: Designed for real-world conditions (cold, dark, no internet)
- **Workflow integration**: From capture through processing with minimal manual steps

## How They Work Together

```
┌────────────────────────────────────────────────────────────┐
│                    Field Capture Layer                      │
│   ┌─────────────────┬──────────────────┬─────────────────┐ │
│   │  AuroraPhoto    │   Photo Tour     │  OpenAstro Node │ │
│   │  (Aurora)       │   (General)      │  (Deep Sky)     │ │
│   └────────┬────────┴────────┬─────────┴────────┬─────────┘ │
└────────────┼─────────────────┼──────────────────┼───────────┘
             │                 │                  │
             └────────┬────────┴──────────────────┘
                      │
        ┌─────────────▼──────────────┐
        │   OpenAstro Core Library   │
        │  (Shared Astronomical      │
        │   Logic & Drivers)         │
        └─────────────┬──────────────┘
                      │
        ┌─────────────▼──────────────┐
        │    Processing Layer         │
        │  ┌────────────────────────┐ │
        │  │  EclipseStack          │ │
        │  │  ASIAIR Import Tool    │ │
        │  │  PixInsight Workflows  │ │
        │  └────────────────────────┘ │
        └────────────────────────────┘
```

**Typical Workflows:**

**Aurora Photography:**
1. AuroraPhoto receives aurora alert
2. Multi-node array automatically adjusts focus (HFR monitoring)
3. Executes optimized capture sequence
4. iPhone app provides composition assistance
5. Files organized for processing

**Deep Sky Imaging:**
1. OpenAstro Node plans imaging session from target list
2. Automated goto, focus, and exposure sequencing
3. Hardware safety monitoring (weather, mount limits)
4. ASIAIR Import Tool organizes captured frames
5. Ready for PixInsight WBPP processing

**Field Photography:**
1. Photo Tour displays live camera preview on iPhone
2. Composition overlay with horizon/thirds guides
3. Smart triggering suggestions based on scene analysis
4. Automated bracketing and focus stacking workflows

---

## Astrophotography

### AuroraPhoto — Automated Aurora Capture

<span class="status-badge status-planning">Planning</span> · [Full Details →](projects/auroraphoto)

**What It Is:**
Automated aurora photography system using Raspberry Pi nodes controlling Sony a7R V/a7 IV cameras via USB, with iPhone companion app for composition and multi-node management.

**Key Features:**
- **Star Sharpness Monitoring**: Automated HFR (Half-Flux Radius) tracking for pin-sharp focus
- **Burst Response**: Intelligent capture sequencing optimized for unpredictable aurora activity
- **Multi-Node Control**: Manage 4+ camera arrays from single iPhone interface
- **Field-Ready**: Wi-Fi hotspot connectivity for remote locations

**Use Case:** Capture high-quality aurora imagery during unpredictable "bursts" while maintaining perfect star focus in freezing field conditions.

**Tech Stack:** Raspberry Pi, iOS (SwiftUI), Python/Rust camera control

---

### OpenAstro Node — Autonomous Observatory

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/open-astro-node)

**What It Is:**
A headless, autonomous astrophotography controller designed for low-power Linux devices (RPi/Jetson). Manages hardware, executes imaging sequences, and ensures rig safety.

**Key Features:**
- **Hardware Management**: INDI/ASCOM Alpaca device control (mount, camera, focuser, filter wheel)
- **Autonomous Sequencing**: Execute multi-target imaging plans without intervention
- **Safety Monitoring**: Weather checks, mount limit detection, power management
- **Remote Access**: SSH-based control and monitoring

**Use Case:** Deploy a fully automated deep-sky imaging rig that runs unattended overnight sessions.

**Tech Stack:** Rust, INDI protocol, ASCOM Alpaca

---

### OpenAstro Core — Shared Astronomical Logic

<span class="status-badge status-active">v0.1 Celestial Math</span> · [Full Details →](projects/open-astro-core)

**What It Is:**
High-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem.

**Components:**
- **astro-core**: Coordinate math (RA, Dec, transforms), time calculations (Julian date, sidereal time)
- **astro-indi**: INDI protocol client and device abstraction
- **astro-alpaca**: ASCOM Alpaca REST client for modern hardware
- **sony-sdk-rs** (Planned): Sony Camera Remote SDK bindings
- **polaris-proto** (Planned): Benro Polaris protocol implementation

**Core Value:** Ensure both OpenAstro Node and Photo Tour use identical, correct coordinate math and driver logic.

**Current Milestone:** v0.1 Celestial Math (angle primitives, coordinate transforms, time helpers)

**Tech Stack:** Rust

---

### EclipseStack — High-Precision Alignment

<span class="status-badge status-planning">Planning</span> · [Full Details →](projects/eclipsestack)

**What It Is:**
High-precision alignment tool for solar eclipse photography that handles tracker drift to enable HDR stacking.

**The Challenge:**
Solar eclipse photography during totality captures hundreds of frames, but subtle tracker drift prevents perfect alignment. No background stars available for traditional astrophotography alignment methods.

**The Solution:**
- **Solar Disk Detection**: Automatically locate center of solar disk/moon silhouette
- **Temporal Drift Modeling**: Use EXIF timestamps to model tracker drift rate
- **Feature-Based Alignment**: Use solar flares as secondary anchors for sub-pixel precision
- **Interactive Review**: Web-based UI to visualize drift path and verify alignment

**Workflow:** Import .ARW files → Detect disk + flares → Model drift → Align frames → Export TIFF/FITS for PixInsight HDR stacking

**Tech Stack:** Rust (core processing), Web UI (Tauri or web stack)

---

### ASIAIR Import Tool — Workflow Automation

<span class="status-badge status-active">Phase 1/1</span> · [Full Details →](projects/import-asiair)

**What It Is:**
Python script that automates post-imaging-session file organization for astrophotography.

**Key Features:**
- **Batch Import**: Scan ASIAIR backup locations for FITS files
- **Smart Organization**: Group by target, observation night, filter
- **Calibration Matching**: Copy matching darks, flats, bias frames
- **WBPP Ready**: Prepare directory structure for PixInsight's Weighted Batch Preprocessing

**Use Case:** Eliminate manual file sorting after imaging sessions—scan hundreds of frames, organize by target/filter/date, validate calibration availability, go straight to processing.

**Tech Stack:** Python

---

## Field Photography

### Photo Tour — Interactive Assistant

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/photo-tour)

**What It Is:**
Smart, interactive photography assistant designed for field use. Helps compose shots, automate repeatable workflows, and progressively adds intelligent triggering and transition logic.

**Key Features:**
- **Live Preview**: See what the camera sees on iPhone display
- **Composition Assistance**: Overlay guides (horizon level, rule of thirds, compass)
- **Workflow Automation**: Bracketing, focus stacking, time-lapse sequencing
- **Smart Triggering** (Planned): ML-assisted scene analysis for optimal capture timing

**Use Case:** In the field, get actionable guidance and camera control fast enough to improve the shot.

**Tech Stack:** iOS (SwiftUI), Sony SDK integration

---

## Philosophy: Why This Approach?

### Automation Frees Creativity

Technical perfection (focus, exposure, tracking) should be automated. Creative decisions (composition, timing, subject) should remain human. The tools handle pixel-peeping so you can focus on the frame.

### Field-Ready Design

These tools are designed for real-world conditions:
- **Aurora shoots**: Sub-zero temperatures, no internet, unpredictable timing
- **Deep sky imaging**: Overnight unattended operation, safety monitoring
- **Landscape work**: Quick setup, minimal fumbling with settings

### Shared Core, Specialized UX

OpenAstro Core provides the mathematical foundation (coordinate transforms, device drivers) so higher-level apps (Node, Photo Tour, AuroraPhoto) can focus on their specific workflows without reimplementing astronomy primitives.

### Processing Integration

Capture is only half the workflow. These tools integrate with industry-standard processing pipelines (PixInsight WBPP, HDR stacking) through standardized file organization and metadata.

---

## Open Source & Contributions

- **AuroraPhoto**: [github.com/sk2/auroraphoto](https://github.com/sk2/auroraphoto)
- **OpenAstro Node**: [github.com/sk2/open-astro-node](https://github.com/sk2/open-astro-node)
- **OpenAstro Core**: [github.com/sk2/open-astro-core](https://github.com/sk2/open-astro-core)
- **EclipseStack**: [github.com/sk2/eclipsestack](https://github.com/sk2/eclipsestack)
- **ASIAIR Import Tool**: [github.com/sk2/import-asiair](https://github.com/sk2/import-asiair)
- **Photo Tour**: [github.com/sk2/photo-tour](https://github.com/sk2/photo-tour)

---

[← Back to Projects](projects) | [View CV](cv) | [Network Automation](network-automation) | [Signal Processing](signal-processing) | [Data Analytics](data-analytics) | [Agentic Systems](agentic-systems)

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
.status-planning {
  background-color: #ffc107;
  color: #343a40;
}
</style>
