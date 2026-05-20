---
layout: default
title: Photography & Astrophotography
description: Tools for field photography, astrophotography automation, aurora and eclipse capture, and image-processing workflows — capture handled by software, judgment left to the photographer.
---

# Photography & Astrophotography

Tools for field photography, astrophotography, and the processing that follows.
The dividing line is consistent: software handles the technical work — focus,
exposure sequencing, hardware control — and the photographer keeps the creative
decisions of composition, timing, and subject.

## Contents
- [How They Work Together](#how-they-work-together)
- [Astrophotography](#astrophotography)
- [Field Photography](#field-photography)

---

## How They Work Together

<div class="mermaid">
flowchart TD
    AP["AuroraPhoto"] --> CORE
    OAN["OpenAstro Node"] --> CORE
    PT["Photo Tour"] --> CORE
    EP["EclipsePhoto"] --> CORE
    CORE["OpenAstro Core<br/><small>shared coordinate math &amp; device drivers</small>"] --> PROC["Processing<br/><small>EclipseStack · ASIAIR Import → PixInsight</small>"]
</div>

The capture tools each target a different subject — aurora, deep sky, eclipse,
landscape — but draw on one shared Rust library for coordinate math and device
drivers, and hand their output to a common processing stage.

---

## Astrophotography

### AuroraPhoto

<span class="status-badge status-planning">Planning</span> · <span class="stack-badge">Python</span> <span class="stack-badge">Swift</span> · [Full Details →](projects/auroraphoto)

Automated aurora capture across a multi-node camera array. Raspberry Pi nodes
drive Sony a7R V and a7 IV cameras over USB; an iPhone app handles composition
and manages the array from one interface. Half-flux-radius tracking holds star
focus through the unpredictable bursts of an aurora display, where there is no
time to refocus by hand.

---

### OpenAstro Node

<span class="status-badge status-active">Active</span> · <span class="stack-badge">Rust</span> · [Full Details →](projects/open-astro-node)

A headless astrophotography controller for low-power Linux devices (Raspberry Pi,
Jetson). It manages the mount, camera, focuser, and filter wheel over INDI and
ASCOM Alpaca, executes multi-target imaging plans unattended, and monitors
weather and mount limits so an overnight session runs without supervision.

---

### OpenAstro Core

<span class="status-badge status-active">v0.1 — Celestial Math</span> · <span class="stack-badge">Rust</span> · [Full Details →](projects/open-astro-core)

The Rust library beneath the OpenAstro tools: coordinate math (RA/Dec transforms,
Julian date, sidereal time), an INDI protocol client, and an ASCOM Alpaca REST
client. OpenAstro Node and Photo Tour share one correct implementation of the
astronomy primitives rather than each reimplementing them.

---

### EclipsePhoto

<span class="status-badge status-active">Phase 1 — Hardware Foundation</span> · <span class="stack-badge">Python</span> · [Full Details →](projects/eclipsephoto)

A fire-and-forget Raspberry Pi controller for solar eclipse photography. It
coordinates a camera over gphoto2 and a mount (ZWO AM5, Benro Polaris) over INDI
to capture the full sequence from first to last contact. Guiding, exposure
ramping, and fault recovery run automatically, so the photographer can watch the
eclipse instead of the camera.

---

### EclipseStack

<span class="status-badge status-planning">Planning</span> · <span class="stack-badge">Rust</span> · [Full Details →](projects/eclipsestack)

Alignment for eclipse-totality image stacks. Totality yields hundreds of frames
but no background stars to align against, and tracker drift defeats a naive
overlay. EclipseStack detects the solar disk, models the drift rate from EXIF
timestamps, and uses solar flares as sub-pixel anchors — exporting aligned frames
ready for HDR stacking in PixInsight.

---

### ASIAIR Import Tool

<span class="status-badge status-active">Complete</span> · <span class="stack-badge">Python</span> · [Full Details →](projects/import-asiair)

Post-session file organization for astrophotography. It scans ASIAIR backups,
groups frames by target, night, and filter, matches the corresponding darks,
flats, and bias frames, and lays out a directory ready for PixInsight's Weighted
Batch Preprocessing.

---

## Field Photography

### Photo Tour

<span class="status-badge status-active">Active</span> · <span class="stack-badge">Swift</span> · [Full Details →](projects/photo-tour)

A field photography assistant for iPhone. It shows a live camera preview with
composition overlays — horizon level, rule of thirds, compass — and automates
repeatable workflows such as bracketing and focus stacking. Planned scene
analysis will suggest capture timing.

---

[← Back to Projects](projects) | [Network Automation](network-automation) | [Signal Processing](signal-processing) | [Data & Analytics](data-analytics) | [Autonomous Systems](agentic-systems)
