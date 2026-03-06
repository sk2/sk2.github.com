---
layout: default
section: signal-processing
---

# Algorithmic Music Engine

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Concept

Generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model (macro, meso, micro), with live playback, step editing, and WAV export. Procedural synthesis generates kick, bass, hihat, and clap patterns; an effects chain (sidechain compression, delay, reverb, HPF, limiter) and humanization (velocity jitter, micro-timing) produce output that sounds like a produced track rather than a sequencer demo.

---

## Features

- Energy-driven pattern generation across three temporal scales
- Procedural synthesis with per-note filter modulation (envelope + LFO)
- 12 theme presets and mood presets (key, scale, energy, filter configs)
- Binaural beats system with 5 presets and custom parameters
- Sample bank fallback with round-robin WAV playback
- Live parameter control during playback without re-render
- Session save/load and preset management
- Wavetable synthesis, modulation matrix, and extended FX chain
- WAV export (16-bit stereo, 44.1 kHz)
- Pre-render model: ~20ms render time for smooth TUI interaction

---

## Architecture

- Rust 2021, modular layers (engine, synths, DSP, TUI, theory)
- f64 internal precision throughout, f32 only at output
- Cross-platform audio via `cpal` (CoreAudio/ALSA/WASAPI)
- Wrapper composition pattern: effects stack (bias, heartbeat) without modifying base generators

---

[← Back to Signal Processing](../signal-processing)
