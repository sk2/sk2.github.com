---
layout: default
section: signal-processing
description: "Spatial audio analysis on a microphone array — time-of-arrival localisation, beamforming, and gated classification into provenance-bearing events."
hand_written: true
---

# Sound Array

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

---

## Concept

Spatial audio analysis on a microphone array: capture multi-channel audio, estimate time-of-arrival differences between channels to localise sound sources, apply beamforming to isolate them directionally, and classify each isolated stream — vehicles, aircraft, wildlife — into provenance-bearing events that an analysis agent can act on.

The pipeline is built around a single consistency boundary: a windowed audio snapshot becomes the input to every downstream estimator, so localisation, beamforming, and classification all reason about the same coherent slice of time.

---

## Architecture

<div class="mermaid">
flowchart TD
    MIC["Microphone Array<br/><small>multi-channel USB/HAT</small>"]
    SNAP["Snapshot Window<br/><small>consistency boundary · happens-before</small>"]
    GCC["GCC-PHAT<br/><small>per-pair delay estimation</small>"]
    BF["Beamforming<br/><small>geometry-driven directional isolation</small>"]
    CLS["Gated Classification<br/><small>vehicles · aircraft · wildlife</small>"]
    EV["Events<br/><small>provenance-bearing predicates over time</small>"]
    MIC --> SNAP
    SNAP --> GCC
    GCC --> BF
    BF --> CLS
    CLS --> EV
</div>

Each stage is a deterministic transform over the snapshot: the same input window produces byte-identical localisation, beamforming, and classification outputs. Geometry provenance and timing certainty propagate downstream, so an event carries the uncertainty of its inputs rather than absorbing it silently.

---

[← Back to Signal Processing](../signal-processing)
