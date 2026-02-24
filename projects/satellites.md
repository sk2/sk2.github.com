---
layout: default
section: projects
---

# Satellites

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Projects](../projects)

---

## Concept

### What This Is

A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm. Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead.

### Core Value

Real-time satellite positions rendered on a terminal world map with pass predictions — a single binary, no browser, no GUI dependencies.

---

## Tech Stack

- **Language**: Rust (2021 edition)
- **TUI**: ratatui + crossterm (canvas widget for world map)
- **Async**: tokio (background data fetching)
- **Orbital Mechanics**: sgp4 crate (SGP4/SDP4 propagation)
- **Coordinates**: map_3d (ECI → ECEF → Geodetic → AER)
- **HTTP**: reqwest (async JSON API calls)
- **CLI**: clap 4

---

[← Back to Projects](../projects)
