---
layout: default
section: photography
---

# Aurora Advisor

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">TypeScript</span> <span class="stack-badge">Rust</span>
</div>

[← Back to Photography](../photography)

[← Back to Projects](../projects)

---

## Concept

Decision tool for Australian aurora observers that answers "should I drive 60 minutes to a dark site tonight?" Combines real-time solar wind data (NOAA SWPC), substorm trigger detection (Bz drops + hemispheric power jumps), and local weather forecasts (ACCESS-G model via Open-Meteo) into a single Go/No-Go score that accounts for both space weather potential and terrestrial conditions (cloud cover, moon phase, travel time).

---

## Features

**Shipped (v1.0):**
- Real-time substorm trigger detection from NOAA solar wind data
- Multi-criteria site scoring (activity, weather, travel time, moon)
- Telegram bot with automated aurora alerts
- Historical playback engine with parameter tuning infrastructure
- Hybrid Rust/TypeScript architecture — Rust CLI for fast offline analysis (10k configs in <1s)

**In progress (v2.0):**
- Longer lead-time forecasting (6–12 hours using L1 solar wind from ACE/DSCOVR)
- ML-based probabilistic predictions replacing binary heuristics
- Event timeline forecasting (intensity curve, peak timing, optimal viewing windows)

---

[← Back to Photography](../photography)
