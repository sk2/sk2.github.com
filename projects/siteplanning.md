---
layout: default
section: photography
description: "Astrophotography Site Planner — combines celestial event calculations with Bortle-scale light pollution, horizon profiles, and weather windows to rank shooting locations for a given target."
hand_written: true
---

# Astrophotography Site Planner

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">TypeScript</span> <span class="stack-badge">React</span>
</div>

---

## Concept

A planning tool for astrophotography sessions in the Adelaide region. The input is a session goal — "Milky Way core at 30° elevation," "Jupiter at opposition," "a clear south-facing horizon for the Magellanic Clouds" — and the output is a ranked shortlist of sites with timing windows, drive estimates, and weather context.

The site catalogue holds 50+ surveyed locations across the Adelaide Hills, Fleurieu Peninsula, and Murray Mallee, each with a pre-measured horizon profile, a Bortle-scale dark-sky rating, and access notes. Ephemeris and light-pollution interpolation run client-side, so the whole planner works offline once the catalogue is loaded.

---

## Architecture

<div class="mermaid">
flowchart TD
    GOAL["Session Goal<br/><small>target · elevation · time window</small>"]
    EPH["Celestial Engine<br/><small>rise/set · alt/az · events</small>"]
    SITES["Site Catalogue<br/><small>50+ sites · horizon · Bortle · access</small>"]
    LP["Light-Pollution Model<br/><small>SQM interpolation · moon-adjusted</small>"]
    WX["Weather Window<br/><small>cloud · transparency</small>"]
    RANK["Site Ranker<br/><small>goal-weighted score</small>"]
    OUT["Ranked Shortlist<br/><small>per-site timing + drive</small>"]
    GOAL --> RANK
    EPH --> RANK
    SITES --> RANK
    LP --> RANK
    WX --> RANK
    RANK --> OUT
</div>

The horizon profile per site is the part that makes the ranker honest: a Bortle-1 site with a hill exactly where the target rises is worse than a Bortle-3 site with a clear horizon, and the planner reflects that without the photographer having to remember it on the night.

---

[← Back to Photography & Astrophotography](../photography)
