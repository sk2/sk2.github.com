---
layout: default
section: photography
---

# Satellites

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Features](#features)
- [Current Status](#current-status)

## Concept

Terminal-based satellite tracker that displays real-time positions on a world map, predicts passes over the user's location, and shows transmission frequencies. Built with Rust and ratatui, using the SGP4 orbital propagation algorithm to compute positions from Two-Line Element (TLE) data. A single binary with no GUI dependencies — aimed at amateur radio operators and space enthusiasts.

---

## Architecture

- **Propagation**: `sgp4` crate for orbital mechanics, `map_3d` for coordinate transforms (ECI to geodetic)
- **Data sources**: CelesTrak (TLEs, free, no auth) and SatNOGS DB (transmitter frequencies)
- **TUI**: ratatui with immediate-mode rendering — full UI rebuilt from state each frame
- **Performance**: propagates ~1,000 satellites per tick (1s default) without frame drops

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

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust |

---

## What This Is

A terminal-based satellite tracker that displays real-time satellite positions on a world map, predicts passes over the user's location, and shows transmission/frequency data. Built with Rust, ratatui, and the SGP4 orbital propagation algorithm. Aimed at amateur radio operators, space enthusiasts, and anyone who wants to know what's overhead.

---

## Core Value

Real-time satellite positions rendered on a terminal world map with pass predictions — a single binary, no browser, no GUI dependencies.

---

## Requirements

---

## # Validated

- [x] Project scaffolding with Cargo.toml, README, LICENSE, .gitignore, config.example.toml
- [x] TUI skeleton: terminal setup/teardown, event loop, action dispatch, quit on `q`
- [x] World map rendering via ratatui Canvas widget
- [x] Status bar with location, time, satellite count, keybind hints
- [x] Satellite table view (rendering, keyboard navigation)
- [x] Detail panel (selected satellite orbital info)
- [x] CelesTrak API client with OMM JSON parsing
- [x] File-based JSON cache with TTL
- [x] SatNOGS API client (transmitter data)
- [x] Data models: Satellite, SatellitePosition, Transmitter, LookAngle, Pass
- [x] Config loading: TOML file + CLI args merge
- [x] Action/event pattern for state management

---

## # Active

- [x] SGP4 propagation wrapper (tracking/propagator.rs)
- [x] Coordinate transforms: ECI to Geodetic (tracking/coordinates.rs)
- [x] Wire up: fetch -> propagate on tick -> render dots on map
- [ ] IP geolocation fallback (location/geoip.rs)
- [ ] Manual location from config/CLI (location/manual.rs)
- [ ] Observer look angles: azimuth/elevation/range (tracking/observer.rs)
- [ ] Color satellites by visibility (overhead=yellow, below=blue)
- [ ] Observer marker on map
- [ ] Pass prediction: 60s intervals over 24h, zero-crossing detection, binary search refinement
- [ ] StatefulTable with keyboard scroll and selection highlight
- [ ] Sort: overhead first by elevation, then upcoming by AOS
- [ ] Fetch SatNOGS transmitters on satellite select
- [ ] Display frequency/mode list in detail panel
- [ ] Split layout: table left, detail right when selected
- [ ] Pass timeline chart (next 12-24h)
- [ ] Group switching (`g` key)
- [ ] Search satellites by name (`/` key)
- [ ] Refresh TLE data (`r` key)
- [ ] View cycling (`Tab` key)
- [ ] GitHub Actions CI (build, clippy, test)
- [ ] Tag v0.1.0 release

---

## # Out of Scope

- GUI/web interface — terminal only
- Satellite imagery or ground track visualization — dots on map only
- Doppler correction — frequency display only, no radio control
- Two-line element (TLE) editing — read-only from CelesTrak
- Orbit determination — uses published TLEs, no custom fitting
- Multi-user or networked mode — single-user CLI tool

---

## Context

- CelesTrak provides free TLE/OMM data in JSON format, grouped by satellite category (no auth)
- SatNOGS DB provides transmitter frequencies and modes via REST API (no auth)
- The `sgp4` Rust crate (v1) handles SGP4/SDP4 propagation and parses CelesTrak JSON natively
- `map_3d` crate handles ECI->ECEF->Geodetic->AER coordinate transforms
- ratatui's Canvas widget provides the world map with built-in coastline data
- Default group "active" contains ~1000 satellites; Starlink can have 5000+
- Pass prediction uses elevation zero-crossing detection with binary search for ~1s accuracy

---

## Constraints

- **Tech stack**: Rust 2021 edition, ratatui + crossterm for TUI, tokio for async
- **Data sources**: CelesTrak (TLEs) and SatNOGS DB (frequencies) — both free, no auth
- **Performance**: Must propagate ~1000 satellites per tick (1s default) without frame drops
- **Binary**: Single self-contained binary, no runtime dependencies beyond a terminal
- **Offline**: Must work with cached data when network is unavailable

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Rust over Python/Go | Performance for SGP4 propagation, single binary distribution | -- Pending |
| ratatui over cursive/tui-rs | Active maintenance, Canvas widget, rich widget library | -- Pending |
| sgp4 crate v1 | Pure Rust, parses CelesTrak JSON natively, well-tested | -- Pending |
| File-based JSON cache | Simple, no database dependency, human-readable | -- Pending |
| Immediate-mode UI | Rebuild entire UI from state each frame — simple, no sync bugs | -- Pending |
| Action/command pattern | Decouples input handling from state mutations | -- Pending |

*Last updated: 2026-02-15 after initialization*

---

## Current Status

** 2026-03-01 --  complete

---

[← Back to Projects](../projects)
