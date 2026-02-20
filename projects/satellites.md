---
layout: default
section: projects
## Current Status

2026-02-20 -- Created 02-CONTEXT.md

---

# Satellites

<span class="status-badge status-active">Phase 2/6 (20%)</span>

[← Back to Projects](../projects)

## Current Status

2026-02-20 -- Created 02-CONTEXT.md

---

## Concept

A terminal-based satellite tracker that plots real-time satellite positions on a world map, predicts passes over your location, and displays transmission frequencies from SatNOGS. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 2/6 (20%) |
| **Language** | N/A |
| **Started** | 2026 |

## Current Status

2026-02-20 -- Created 02-CONTEXT.md

---

## What This Does

Fetches Two-Line Element (TLE) orbital data from CelesTrak, propagates satellite positions in real time using SGP4, and renders them on a terminal canvas world map. Select a satellite to see its orbital parameters, upcoming passes with rise/set times, and transmitter frequencies from the SatNOGS database.

## TUI Layout

```
┌──────────────────────────────────────────────────┐
│              World Map (Canvas)                   │  ~40%
│  [satellite dots]  [observer ✕]  [labels]        │
├──────────────────────────┬───────────────────────┤
│  Satellite Table         │  Detail Panel         │  ~55%
│  Name | El | Az | Freq   │  Orbit info           │
│  ISS    45   NW  145.8   │  Transmitters list    │
│  SO-50  12   SE  436.8   │  Next pass timeline   │
├──────────────────────────┴───────────────────────┤
│ London 51.5°N 0.1°W │ 14:23 UTC │ 12 sats │ q/? │
└──────────────────────────────────────────────────┘
```

## Key Features

- **Real-time world map**: Satellite positions plotted on a terminal canvas, updated every second
- **Pass predictions**: Upcoming passes over the next 24 hours with rise/set times and max elevation, refined to ~1 second accuracy via binary search on elevation zero-crossings
- **Frequency data**: Transmitter frequencies and modes from SatNOGS DB
- **Interactive navigation**: Browse satellites with vim-style keybindings, search by name, switch between 15 CelesTrak satellite groups
- **Smart location**: IP geolocation on startup with config/CLI override
- **Starlink handling**: Coarser propagation (5-minute steps) for initial screening to manage the large constellation, with refinement near the observer's horizon
- **Local caching**: TLE and transmitter data cached to disk with configurable TTL (12h/48h defaults)

## Data Sources

- **[CelesTrak](https://celestrak.org)**: TLE/OMM orbital elements in JSON format, grouped by satellite category
- **[SatNOGS DB](https://db.satnogs.org)**: Satellite transmitter frequencies, modes, and metadata via REST API
- **IP Geolocation**: Fallback location detection

## Satellite Groups

15 CelesTrak groups available, switchable with `g`:

| Group | Description |
|-------|-------------|
| `active` | All active satellites (~1000) — default |
| `stations` | Space stations (ISS, Tiangong) |
| `amateur` | Amateur radio satellites |
| `weather` / `noaa` / `goes` | Weather satellites |
| `starlink` / `oneweb` | Mega-constellations |
| `geo` | Geostationary satellites |
| `science` / `military` / `cubesat` | Specialized groups |

## Coordinate Pipeline

TLE data flows through a multi-stage transformation:

```
TLE → SGP4 (ECI position/velocity)
    → ECEF rotation (Earth-fixed frame)
    → Geodetic (lat/lon/alt for map plotting)
    → AER (azimuth/elevation/range from observer)
```

Pass prediction propagates at 60-second intervals over 24 hours, detects elevation zero-crossings, then binary-searches to ~1 second accuracy for AOS/LOS times.

## Development Roadmap

- Phase 1: Project setup + README (complete)
- Phase 2: TUI skeleton + world map rendering
- Phase 3: Live satellite data on map (CelesTrak + SGP4)
- Phase 4: Observer location + overhead detection
- Phase 5: Interactive satellite table with pass predictions
- Phase 6: Detail panel + SatNOGS frequency data
- Phase 7: Pass timeline chart + group switching + search
- Phase 8: GitHub Actions CI + v0.1.0 release

## Tech Stack

- **Language**: Rust (2021 edition)
- **TUI**: ratatui + crossterm (canvas widget for world map)
- **Async**: tokio (background data fetching)
- **Orbital Mechanics**: sgp4 crate (SGP4/SDP4 propagation)
- **Coordinates**: map_3d (ECI → ECEF → Geodetic → AER)
- **HTTP**: reqwest (async JSON API calls)
- **CLI**: clap 4

## Current Status

2026-02-20 -- Created 02-CONTEXT.md

---

[← Back to Projects](../projects)
