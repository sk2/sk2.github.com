---
layout: default
section: signal-processing
description: "Generative psytrance synthesis engine with real-time TUI controls."
---

# Overtone

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Features](#features)

## Concept

Generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model (macro, meso, micro), with live playback, step editing, and WAV export. Procedural synthesis generates kick, bass, hihat, and clap patterns; an effects chain (sidechain compression, delay, reverb, HPF, limiter) and humanization (velocity jitter, micro-timing) produce output that sounds like a produced track rather than a sequencer demo.

---

## Architecture

- Rust 2021, modular layers (engine, synths, DSP, TUI, theory)
- f64 internal precision throughout, f32 only at output
- Cross-platform audio via `cpal` (CoreAudio/ALSA/WASAPI)
- Wrapper composition pattern: effects stack (bias, heartbeat) without modifying base generators

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

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust |

---

## What This Is

Overtone is a standalone native GUI tool for music producers. It generates and shapes tracks locally, lets users audition them quickly, and hands them off to Ableton through export when needed.

---

## Core Value

Strong local generation for producers:

- generate a useful starting point
- shape it meaningfully inside the app
- audition it immediately
- export it cleanly
- finish it in Ableton

---

## Constraints

- Preserve the existing Rust codebase and modular architecture
- Do not delete exploratory work; park it clearly instead
- Prefer stable local behavior over fragile external integrations
- Keep the roadmap short enough to guide execution

---

## Key Decisions

| Decision | Why |
|----------|-----|
| Native GUI is the product center | It best matches the target user and launch path |
| Deep local generation beats DAW dependence | It keeps the creative core inside Overtone |
| Local audition beats live sync | It is more reliable and fully under our control |
| Export is the primary Ableton handoff | It avoids fragile runtime integration as the main user path |
| TUI stays, but as secondary | It contains useful tooling without setting product direction |
| Parked work remains in the repo | Focus should not destroy prior investment |

*Reset: 2026-04-10*
