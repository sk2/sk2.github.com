---
layout: default
section: signal-processing
description: "Algorithmic Music Engine — generative psytrance synthesis driven by a multi-scale energy model, with procedural drum and bass patterns, effects chain, and live TUI control."
hand_written: true
---

# Overtone

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Concept

Generative psytrance synthesis from first principles. A multi-scale energy model — macro (the arc of a track), meso (sections), micro (individual bars) — drives procedural pattern generation for kick, bass, hi-hat, and clap, then runs the result through a fixed effects chain (sidechain compression, delay, reverb, HPF, limiter) and a humanisation layer (velocity jitter, micro-timing) so the output sounds like a produced track rather than a step-sequencer demo.

The compositional model also draws on Indian classical rhythm — Tala-style additive cycles and Rasa-driven aesthetic state mapping — and applies them as constraints on the underlying psytrance grid.

---

## Architecture

<div class="mermaid">
flowchart TD
    ENERGY["Energy Model<br/><small>macro · meso · micro</small>"]
    RASA["Rasa / Tala Bias<br/><small>aesthetic & rhythmic constraints</small>"]
    PAT["Pattern Generator<br/><small>kick · bass · hi-hat · clap</small>"]
    SYNTH["Procedural Synthesis<br/><small>per-voice oscillator stack</small>"]
    FX["Effects Chain<br/><small>sidechain · delay · reverb · HPF · limiter</small>"]
    HUM["Humanisation<br/><small>velocity jitter · micro-timing</small>"]
    OUT["WAV / Live Playback"]
    ENERGY --> PAT
    RASA --> PAT
    PAT --> SYNTH
    SYNTH --> FX
    FX --> HUM
    HUM --> OUT
</div>

Phase-coherent sidechain alignment keeps the kick and the bass from masking each other in the 40–100 Hz region; the effects chain is sequenced so dynamics shaping happens before delay tails are generated.

---

[← Back to Signal Processing](../signal-processing)
