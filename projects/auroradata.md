---
layout: default
section: projects
---

# Aurora Advisor

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Roadmap](#roadmap)

## Concept

### What This Is

A specialized tool for Australian aurora observers that solves the "should I drive 60 minutes?" problem. It combines real-time solar wind data (NOAA), substorm trigger logic (Bz/HP trends), and local weather (ACCESS-G model) to provide actionable advice.

### Core Value

Providing a single, definitive "Go/No-Go" score that accounts for both space weather potential and local terrestrial conditions (travel time, clouds, moon).

---

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
```


```
      │  HP step detection   │
      │  120-min trend buffer│
      └────────┬────────────┘
               │
      ┌────────▼────────────┐
      │  Site Scoring Engine│
      │  Activity ()     │
      │  Cloud cover ()  │
      │  Travel time ()  │
      │  Moon phase ()   │
```



```
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

---

## Tech Stack

- **Language**: TypeScript (Node.js)
- **Data Sources**: NOAA SWPC (solar wind, hemispheric power), Open-Meteo API (ACCESS-G weather model)
- **LLM**: OpenAI GPT-4o-mini for advice generation
- **Alerting**: Telegram Bot API with subscriber management
- **Testing**: Jest with ts-jest (ESM support)

---

## Roadmap

- Scope (not prioritized):

---

[← Back to Projects](../projects)
