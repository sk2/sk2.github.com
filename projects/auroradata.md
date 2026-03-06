---
layout: default
section: projects
---

# Aurora Advisor

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">TypeScript</span>
</div>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Why We're Building It](#why-were-building-it)
- [Current Milestone: v2.0 - Advanced Forecasting System](#current-milestone-v20-advanced-forecasting-system)
- [Key Decisions](#key-decisions)
- [Requirements](#requirements)
- [Roadmap](#roadmap)

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Concept

A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.

Providing a single, definitive "Go/No-Go" score that accounts for both space weather potential and local terrestrial conditions (travel time, clouds, moon).

---

## Why We're Building It

Existing tools like the Glendale app are powerful but difficult to use, and many sources lack the localized Australian context and travel-time "trade-off" logic required for confident planning. This tool aims to maximize observation success by providing a clear, advice-driven indicator of when to leave for a site.

---

## Current Milestone: v2.0 - Advanced Forecasting System

**Goal:** Transform from binary heuristic predictions to ML-based probabilistic forecasting with longer lead time and event timeline predictions.

**Target features:**
- Longer lead time forecasting (6-12 hours using L1 solar wind data from ACE/DSCOVR)
- ML models for improved accuracy (ensemble methods, feature engineering, trained on historical events)
- Probabilistic predictions (confidence intervals, risk scores instead of binary Go/No-Go)
- Event timeline forecasting (predict intensity curve, peak timing, optimal viewing windows)

---

## Key Decisions

- **Architecture:** Node.js/TypeScript prototype (currently CLI).
- **Primary Data:** NOAA SWPC JSON products (Solar Wind) and Text products (Hemispheric Power).
- **Weather Model:** ACCESS-G via Open-Meteo for Australian accuracy.
- **Future Expansion:** Design hooks for "Astro Predictor" (seeing, transparency) and Telegram alerts.

---

## Requirements



---

## # Validated (v1.0 shipped)

- ✓ Real-time substorm trigger detection (Bz drops + HP jumps) — Phase 1
- ✓ Multi-criteria site scoring (activity, weather, travel time, moon) — Phase 2
- ✓ Telegram bot with automated alerts — Phase 3
- ✓ Historical playback engine with tuning infrastructure — Phase 4
- ✓ Hybrid Rust/TypeScript architecture — 
- ✓ Fast offline analysis (Rust CLI, 10k configs in <1s) — Phase 6

---

## # Active (v2.0 in progress)

- [ ] Integrate L1 solar wind data for 6-12 hour lead time
- [ ] Build ML training pipeline with feature engineering
- [ ] Implement ensemble models for probabilistic predictions
- [ ] Add event timeline forecasting (intensity curve, peak timing)

---

## # Out of Scope

- [Exclusion 1] — **Historical Substorm Analysis:** Detailed correlation study of past solar events to refine trigger math (moved to future milestone).
- [Exclusion 2] — **Astro Predictor (Seeing/Transparency):** Captured as a future milestone/separate project to maintain focus on Aurora.
- [Exclusion 2] — **Mobile Native App:** Initial focus is CLI/Web-based alerts.

*Last updated: 2026-02-21 after completing v1.0 and starting v2.0 milestone*

---

## Roadmap

- **Scope (not prioritized):** 

---

[← Back to Projects](../projects)
