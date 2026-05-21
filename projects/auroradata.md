---
layout: default
section: photography
description: "Aurora Advisor — a decision tool that fuses real-time space-weather data, substorm detection, and local cloud-cover forecasts into a single Go/No-Go score for aurora viewing."
hand_written: true
---

# Aurora Advisor

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">TypeScript</span>
</div>

---

## Concept

A decision tool that answers a specific question for southern-hemisphere aurora observers: should I drive an hour to a dark site tonight, or stay home? The answer is rarely either the space-weather forecast alone (the sky might be clouded over) or the weather alone (the geomagnetic field might be quiet) — it's the join of the two, weighted by how much effort the trip actually costs.

The advisor consumes the real-time solar wind feed, watches for the substorm triggers that turn a quiet aurora into a visible one, pulls a local cloud-cover and moon-phase forecast, and folds everything into a single Go/No-Go score.

---

## Architecture

<div class="mermaid">
flowchart TD
    SW["Solar Wind Feed<br/><small>Bz, Kp, hemispheric power</small>"]
    SUB["Substorm Detector<br/><small>Bz drop + HPI jump triggers</small>"]
    WX["Local Forecast<br/><small>cloud cover · moon phase · transparency</small>"]
    TRIP["Trip Cost Model<br/><small>drive time · site elevation</small>"]
    SCORE["Go/No-Go Score<br/><small>weighted join</small>"]
    OUT["Notification<br/><small>actionable for tonight</small>"]
    SW --> SUB
    SUB --> SCORE
    WX --> SCORE
    TRIP --> SCORE
    SCORE --> OUT
</div>

The trip-cost branch is what separates this from a generic space-weather dashboard: a borderline Kp-5 event on a clear, moonless night close to home is a different call than the same event on a cloudy night two hours away.

---

[← Back to Photography & Astrophotography](../photography)
