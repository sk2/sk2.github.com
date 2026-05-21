---
layout: default
section: photography
description: "Satellites — a terminal-based satellite tracker that propagates orbits from TLE data, predicts passes over the observer's location, and shows transmission frequencies."
hand_written: true
---

# Satellites

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Concept

A terminal-based satellite tracker for amateur radio operators and astrophotographers who want to know what's overhead right now and what passes are coming. Two-Line Element data goes in, SGP4 propagation gives position over time, and the result lands on a world map and a pass-prediction view in the same TUI. Transmission frequencies for each tracked satellite live alongside the position so a radio operator can tune as the pass starts.

A single statically-linked binary with no GUI dependencies — the whole thing fits in a terminal multiplexer pane and runs the same on a laptop and a remote observatory.

---

## Architecture

<div class="mermaid">
flowchart TD
    TLE["TLE Source<br/><small>periodic catalogue refresh</small>"]
    SGP4["SGP4 Propagator<br/><small>orbital state → position over time</small>"]
    OBS["Observer Geometry<br/><small>lat/lon · horizon</small>"]
    PASS["Pass Predictor<br/><small>visibility windows · max elevation</small>"]
    FREQ["Frequency Catalogue<br/><small>per-satellite transmit bands</small>"]
    MAP["World-Map View<br/><small>live positions</small>"]
    LIST["Pass List<br/><small>tonight · upcoming</small>"]
    TLE --> SGP4
    SGP4 --> MAP
    SGP4 --> PASS
    OBS --> PASS
    PASS --> LIST
    FREQ --> LIST
</div>

The map and the pass list run off the same propagator state, so the satellite under the cursor and the next pass in the queue agree on where things are without an extra synchronisation step.

---

[← Back to Photography & Astrophotography](../photography)
