---
layout: default
section: projects
---

# AuroraData — Aurora Planning & Substorm Advisor

<span class="status-badge status-active">v1.0 Complete — All 4 Phases Shipped</span>

[← Back to Projects](../projects)

---

## Concept

Aurora hunting in Australia requires a 60+ minute drive to dark sites, but most tools do not help answer the critical question: "Should I leave *now*?" AuroraData combines real-time solar wind monitoring, substorm trigger detection, local weather forecasts, and travel time to produce a single "Go/No-Go" score with site-specific recommendations.

## Quick Facts

| | |
|---|---|
| **Status** | v1.0 Complete (4/4 phases, 13/13 plans) |
| **Language** | TypeScript (Node.js) |
| **Started** | 2026 |

---

## The Problem

Existing tools like the Glendale app are powerful but complex. Australian observers face unique challenges:
- **Geographic disadvantage**: Need strong events (Kp 6-7+) to see aurora at southern Australian latitudes
- **Travel time investment**: 60-90 minute drives to dark sites required
- **Local weather gaps**: Most tools use global models, not Australian-specific forecasts
- **Decision paralysis**: Multiple data sources provide conflicting signals

The question this tool answers: "If I leave now, will I see aurora when I arrive in 90 minutes?"

## Architecture

```
┌──────────────────────────────────────────────────┐
│                 Data Sources                      │
│  NOAA SWPC (Bz, Bt, Speed, Density, HP)          │
│  Open-Meteo (ACCESS-G cloud cover, precipitation)│
│  Moon Phase Calculator                            │
└──────────────┬───────────────────────────────────┘
               │
      ┌────────▼────────────┐
      │  Substorm Analyzer  │
      │  Bz southward turns │
      │  HP step detection   │
      │  120-min trend buffer│
      └────────┬────────────┘
               │
      ┌────────▼────────────┐
      │  Site Scoring Engine│
      │  Activity (40%)     │
      │  Cloud cover (30%)  │
      │  Travel time (20%)  │
      │  Moon phase (10%)   │
      └────────┬────────────┘
               │
      ┌────────▼────────────┐
      │  Weather Reliability│
      │  MAE-based forecast │
      │  confidence scoring │
      └────────┬────────────┘
               │
      ┌────────▼────────────┐
      │   Output Layer      │
      │  CLI Dashboard      │
      │  LLM Advice (GPT)   │
      │  Telegram Bot        │
      │  Historical Playback │
      └─────────────────────┘
```

## Phase 1: Substorm Trigger Engine

Real-time space weather monitoring with substorm detection:
- **Solar Wind Buffer**: 120-minute rolling window with deduplication by time tag, sorted order
- **Substorm Triggers**: Bz southward turns (> 5 nT shift) combined with HP step changes (30-minute rolling window)
- **TOA Estimation**: Solar wind arrival time calculated from speed: `(1,500,000 / speed) / 60` minutes
- **Opportunity Scoring**: `(abs(Bz) * 5) + (Speed / 10)`, capped at 100, blended with terrestrial potential at 60/40

## Phase 2: Localized Planning & Site Selection

Multi-criteria site scoring with Australian-specific weather:
- **Scoring Weights**: Activity 40%, cloud cover 30%, travel time 20%, moon illumination 10%
- **Cloud Forecast**: Near-term weighting `[0.4, 0.3, 0.2, 0.1]` for hours 0-3 at arrival time, with fallback to 4-hour basic forecast beyond 12 hours
- **Travel Penalty**: Exponential decay (`rate=0.02`), 45-minute threshold for required activity increase
- **Weather Reliability**: MAE thresholds — `< 10 = HIGH`, `10-20 = MEDIUM`, `> 20 = LOW` reliability
- **Decision Output**: `>= 70 = GO`, `>= 40 = MAYBE`, `< 40 = NO-GO` with contextual warnings

## Phase 3: Intelligent Advice & Remote Access

LLM-generated recommendations and automated alerting:
- **Pipeline Architecture**: Analysis logic extracted into pure `pipeline.ts` function — no console output, no dotenv imports, fully reusable
- **LLM Advice**: GPT-4o-mini generates natural-language recommendations (max 300 tokens) with graceful degradation when API key is absent
- **Telegram Bot**: Automated alerts with 15-minute check interval, 1-hour cooldown between broadcasts, JSON file persistence for subscribers, auto-removal on send failure

## Phase 4: Historical Playback Engine

Backtesting and validation against real storm events:
- **Historical Data Loader**: Loads NOAA mag/plasma data with time-tag join for robust matching
- **HP History Support**: Uses last two injected HP points for jump detection
- **Playback Runner**: Simulates pipeline decisions against historical events with parallel site scoring
- **Analysis Report**: 3-hour prediction window for realistic accuracy evaluation

## Example Output

```
Location: Adelaide, SA
Target Site: Victor Harbor (75 min drive)

AuroraData Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Space Weather:
  Bz: -12 nT (southward, favorable)
  HP: 45 GW → 68 GW (building substorm)
  Speed: 580 km/s (elevated)
  Arrival: ~43 minutes

Site Recommendations:
  1. Victor Harbor — Score: 82 (GO)
     Cloud: 15%, Travel: 75 min, Moon: 12%
     Confidence: HIGH
  2. Port Germein — Score: 71 (GO)
     Cloud: 22%, Travel: 45 min, Moon: 12%

LLM Advice:
  "Strong substorm building with favorable Bz.
   Leave within 30 minutes for Victor Harbor
   to arrive during peak activity window."

Telegram: Alert sent to 12 subscribers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDATION: GO NOW
```

## Tech Stack

- **Language**: TypeScript (Node.js)
- **Data Sources**: NOAA SWPC (solar wind, hemispheric power), Open-Meteo API (ACCESS-G weather model)
- **LLM**: OpenAI GPT-4o-mini for advice generation
- **Alerting**: Telegram Bot API with subscriber management
- **Testing**: Jest with ts-jest (ESM support)

## Integration with AuroraPhoto

AuroraData handles the *planning* side (when to go, where to go), while AuroraPhoto handles the *capture* side (automated camera control, HFR focus):

1. **AuroraData**: "Strong event predicted, leave now for Victor Harbor"
2. **AuroraPhoto**: Automated multi-camera capture once on-site

---

[← Back to Projects](../projects)
