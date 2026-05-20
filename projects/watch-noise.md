---
layout: default
section: signal-processing
description: "Wave (StillState & FlowState) — on-device procedural noise and binaural-beat audio for sleep and deep work, with frequency calibration and route-aware adaptive masking."
hand_written: true
---

# Wave (StillState & FlowState)

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Swift</span>
</div>

---

## Concept

Two companion apps — StillState for sleep, FlowState for deep work — built around procedural audio rather than streamed playback. Every sample is generated on-device on demand, in response to the user's calibrated frequency preference, the route the audio is leaving on (headphones versus a speaker), and the ambient noise the microphone is hearing.

The synthesis chain is composable: noise colour, binaural-beat layer, EQ shaping, and adaptive masking are wrappers around each other, assembled at runtime from user preferences.

---

## Architecture

<div class="mermaid">
flowchart TD
    NG["Noise Generator<br/><small>white · brown · LFO-blended</small>"]
    BB["Binaural Beat Layer<br/><small>route-gated stereo offsets</small>"]
    EQ["Calibrated EQ<br/><small>+4 dB peaking biquad at user frequency</small>"]
    MASK["Adaptive Masking<br/><small>mic-driven gain envelope</small>"]
    OUT["Output<br/><small>route-aware (headphones · speaker)</small>"]
    NG --> BB
    BB --> EQ
    EQ --> MASK
    MASK --> OUT
</div>

Binaural beats are suppressed when the output route is mono, so the user never hears a phasing artefact instead of the intended effect. A one-time calibration wizard sweeps ten frequencies, gathers a subjective relaxation rating, and pins the EQ peak at the user's strongest response.

---

[← Back to Signal Processing](../signal-processing)
