---
layout: default
---

# AuroraData — Aurora Planning & Substorm Advisor

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Concept

Aurora hunting in Australia requires a 60+ minute drive to dark sites, but most tools don't help answer the critical question: "Should I leave *now*?" **AuroraData** solves this by combining real-time solar wind data, substorm trigger logic, local weather forecasts, and travel time to provide a single, actionable "Go/No-Go" decision.

## Quick Facts

| | |
|---|---|
| **Status** | Active Development |
| **Language** | TypeScript (Node.js) |
| **Started** | 2026 |

---

## What This Is

A specialized tool for Australian aurora observers that combines real-time space weather monitoring (NOAA), substorm prediction logic (Bz/HP trends), and localized terrestrial weather (ACCESS-G model) to provide clear, advice-driven recommendations on when to leave for observation sites.

## Core Value

Providing a single, definitive "Go/No-Go" score that accounts for both space weather potential and local terrestrial conditions (travel time, cloud cover, moon illumination).

## The Problem

Existing tools like Glendale app are powerful but complex. Australian observers face unique challenges:
- **Geographic disadvantage**: Need strong events (Kp 6-7+) to see aurora at southern Australian latitudes
- **Travel time investment**: 60-90 minute drives to dark sites required
- **Local weather gaps**: Most tools use global models, not Australian-specific forecasts
- **Decision paralysis**: Multiple data sources provide conflicting signals

**The question:** "If I leave now, will I see aurora when I arrive in 90 minutes?"

## The Solution

### Real-Time Space Weather Monitoring
- **Solar Wind Data**: NOAA SWPC JSON products (Bz, Bt, Speed, Density)
- **Hemispheric Power**: NOAA text products showing auroral power levels
- **Substorm Triggers**: Detect Bz southward turns + HP step changes

### Localized Terrestrial Conditions
- **Australian Weather**: ACCESS-G model via Open-Meteo (cloud cover, precipitation)
- **Moon Illumination**: Calculate moon phase impact on aurora visibility
- **Site-Specific Forecasts**: 2-4 hour ahead prediction for specific observation locations

### Travel Time Intelligence
- Accounts for drive time from current location
- Hour-ahead planning based on HP building trends
- "Leave now" vs "wait 30 minutes" recommendations

## Key Features

**Already Implemented:**
- ✓ NOAA Solar Wind fetcher (Bz, Bt, Speed, Density)
- ✓ NOAA Hemispheric Power fetcher
- ✓ Open-Meteo weather integration (cloud cover, precipitation)
- ✓ Basic moon illumination logic
- ✓ Opportunity scoring engine

**In Development:**
- Hour-ahead planning logic based on HP building trends
- Site-specific travel time integration
- Refined substorm trigger math (Bz drops + HP step changes)
- Site-specific weather forecasting for next 2-4 hours

## Example Use Case

```
Location: Adelaide, SA
Target Site: Willow Springs (90 min drive)
Time: 21:30 ACDT

AuroraData Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Space Weather:
  Bz: -12 nT (southward, favorable)
  HP: 45 GW → 68 GW (building substorm)
  Speed: 580 km/s (elevated)
  Forecast: Strong activity next 1-2 hours

Local Conditions:
  Cloud Cover: 15% (clearing)
  Precipitation: 0mm (dry)
  Moon: 12% illumination (dark skies)
  Weather at arrival (23:00): Clear

Travel Time: 90 minutes
Arrival Window: 23:00-01:00
Peak Activity: 23:30-00:30 (predicted)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDATION: GO NOW
Confidence: 85%
Leave by: 21:45
Expected conditions: Strong activity, clear skies, dark
```

## Architecture

```
┌─────────────────────────────────────┐
│      Data Sources (Polling)         │
├─────────────────────────────────────┤
│ • NOAA SWPC (Solar Wind, HP)        │
│ • Open-Meteo (ACCESS-G Weather)     │
│ • Moon Phase Calculator             │
└────────────┬────────────────────────┘
             │
    ┌────────▼────────────┐
    │  Substorm Analyzer  │
    │  (Bz/HP Triggers)   │
    └────────┬────────────┘
             │
    ┌────────▼────────────┐
    │  Opportunity Scorer │
    │  (Go/No-Go Logic)   │
    └────────┬────────────┘
             │
    ┌────────▼────────────┐
    │   Output Layer      │
    │  • CLI Dashboard    │
    │  • Future: Telegram │
    └─────────────────────┘
```

## Tech Stack

- **Language**: TypeScript (Node.js)
- **Data Sources**:
  - NOAA SWPC (Space Weather Prediction Center)
  - Open-Meteo API (ACCESS-G Australian weather model)
- **Architecture**: CLI prototype, designed for future web/mobile expansion
- **Future**: Telegram bot integration for real-time alerts

## Integration with AuroraPhoto

While AuroraPhoto handles the *capture* side (automated camera control, HFR focus), AuroraData handles the *planning* side (when to go, where to go). They complement each other:

1. **AuroraData**: "Strong event predicted, leave now for Willow Springs"
2. **AuroraPhoto**: Automated multi-camera capture once on-site

## Out of Scope (v1)

- **Astro Predictor** (Seeing/Transparency): Separate future project
- **Mobile Native App**: Initial focus on CLI/web-based alerts

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
