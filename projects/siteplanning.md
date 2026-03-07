---
layout: default
section: photography
---

# Astrophotography Site Planner

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">TypeScript</span> <span class="stack-badge">React</span>
</div>

---

## Concept

A planning tool for astrophotography sessions in the Adelaide region. It combines celestial event calculations (moon phase, Milky Way rise/set, planet positions) with environmental data (Bortle-scale light pollution, cloud cover, elevation profiles) to recommend optimal shooting locations and times.

The planner covers 50+ sites across the Adelaide Hills, Fleurieu Peninsula, and Murray Mallee, each with pre-surveyed horizon profiles and light-pollution measurements. Given a target (e.g., "Milky Way core at 30 degrees elevation" or "Jupiter opposition"), it returns ranked site recommendations with drive-time estimates, weather windows, and time-lapse interval suggestions.

## Architecture

Built on React 19 with TypeScript and Vite. Mapbox GL renders the site map with Bortle-zone overlays. Astronomy Engine handles all ephemeris calculations client-side — no server required. Recharts powers the elevation-profile and sky-brightness graphs.

Key modules:
- **Celestial engine** — wraps Astronomy Engine for rise/set, altitude/azimuth, and event prediction (eclipses, conjunctions, meteor showers)
- **Site database** — JSON catalog of surveyed locations with GPS coordinates, Bortle class, horizon obstruction angles, and access notes
- **Light-pollution model** — interpolates SQM (Sky Quality Meter) readings across the region, adjusted for moon phase and atmospheric transparency
- **Planner** — scores sites against a session goal and returns a ranked shortlist with per-site timing windows

## Features

- Celestial event calendar with filtering by event type and visibility from Adelaide
- Interactive Mapbox site map with Bortle-zone colour overlays
- Per-site horizon profiles showing obstruction angles by azimuth
- Milky Way core visibility windows with galactic center altitude curves
- Time-lapse interval calculator based on focal length and star-trail tolerance
- Elevation profile charts for hiking-access sites
- Offline-capable PWA for field use without mobile signal

---

[← Back to Projects](/projects)
