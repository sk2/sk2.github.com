---
layout: default
section: signal-processing
---

# Satellite Tracker

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Concept

Terminal-based satellite tracker that displays real-time positions on a world map, predicts passes over the user's location, and shows transmission frequencies. Built with Rust and ratatui, using the SGP4 orbital propagation algorithm to compute positions from Two-Line Element (TLE) data. A single binary with no GUI dependencies — aimed at amateur radio operators and space enthusiasts.

---

## Features

- Real-time satellite positions rendered on a terminal world map (ratatui Canvas)
- SGP4/SDP4 orbital propagation from CelesTrak TLE/OMM data
- Pass prediction with elevation zero-crossing detection and binary search refinement
- SatNOGS integration for transmitter frequency and mode data
- Satellite grouping, search, and keyboard navigation
- File-based JSON cache with TTL for offline operation
- Color-coded visibility (overhead vs. below horizon)
- Observer look angles: azimuth, elevation, range

---

## Architecture

- **Propagation**: `sgp4` crate for orbital mechanics, `map_3d` for coordinate transforms (ECI to geodetic)
- **Data sources**: CelesTrak (TLEs, free, no auth) and SatNOGS DB (transmitter frequencies)
- **TUI**: ratatui with immediate-mode rendering — full UI rebuilt from state each frame
- **Performance**: propagates ~1,000 satellites per tick (1s default) without frame drops

---

[← Back to Signal Processing](../signal-processing)
