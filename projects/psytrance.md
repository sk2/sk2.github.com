---
layout: default
section: signal-processing
description: "Generative psytrance synthesis engine with real-time TUI controls."
---

# Overtone

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Technical Reports](#technical-reports)
- [Architecture](#architecture)
- [Features](#features)
- [Current Status](#current-status)

## Concept

Generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model (macro, meso, micro), with live playback, step editing, and WAV export. Procedural synthesis generates kick, bass, hihat, and clap patterns; an effects chain (sidechain compression, delay, reverb, HPF, limiter) and humanization (velocity jitter, micro-timing) produce output that sounds like a produced track rather than a sequencer demo.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/psytrance-techreport.pdf)

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

A generative cross-cultural music engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Spans psytrance, Indian classical, ambient, and beyond — with intelligent tradition blending and 197 planned expansion phases.

---

## Core Value

Energy-driven generative music that sounds professional and lets users quickly explore variations.

---

## Requirements



---

## # Validated

<!-- Shipped and working in current codebase -->

- ✓ Generative synthesis engine (kick, bass, hihat, clap synths) — existing
- ✓ Energy-driven pattern generation (macro/meso/micro levels) — existing
- ✓ Real-time audio playback via cpal — existing
- ✓ Interactive TUI with launch screen controls — existing
- ✓ Step editing with bar pattern overrides — existing
- ✓ Mood presets with key/scale/energy/filter configs — existing
- ✓ Theme presets (12 preset themes) — existing
- ✓ Filter modulation (envelope + LFO per note) — existing
- ✓ Effects chain (sidechain, delay, reverb, HPF, limiter) — existing
- ✓ Humanization (velocity jitter, micro-timing, kick variation) — existing
- ✓ Sample bank fallback system (round-robin WAV playback) — existing
- ✓ WAV export (16-bit stereo at 44.1kHz) — existing

---

## # Active

<!-- Workflow improvements for v1 -->

- [ ] Project save/load system - Save full session state (all parameters, overrides, seed)
- [ ] Preset management - Save/load/organize parameter snapshots
- [ ] Live parameter control - Tweak synthesis params during playback without re-render
- [ ] Test infrastructure - Comprehensive testing for DSP, synthesis, and pattern generation
- [ ] Code quality cleanup - Remove dead code, fix aliasing issues, improve filter stability
- [ ] Development tooling - Better debugging, profiling, and iteration tools

---

## # Out of Scope

- MIDI input/output — Audio-only tool, not a MIDI controller
- DAW plugin version — Standalone tool for now
- Real-time synthesis — Pre-render model is intentional for quality
- Visual waveform editing — TUI stays text-based
- Multi-track arrangement — Single generative track per session

---

## Context

**Technical Environment:**
- Rust 2021, modular architecture (engine/synths/dsp/tui/theory layers)
- f64 internal precision throughout, convert to f32 only at output
- 44.1kHz sample rate (hardcoded)
- Cross-platform audio via cpal (CoreAudio/ALSA/Wasapi)

**Current State:**
- Codebase is feature-complete for basic generation but lacks workflow polish
- Zero tests exist (critical gap for audio DSP code)
- Significant technical debt flagged: dead code (373 lines documented), naive sawtooth aliasing, filter stability concerns
- TUI state machine works but is fragile during rapid state transitions

**User Research:**
- Primary user workflow: iterate on parameters → find good sounds → lost when moving on
- Need to capture and recall good parameter sets
- Development workflow hampered by lack of tests and debugging tools

---

## Constraints

- **Platform**: macOS/Linux/Windows with audio device access
- **Architecture**: Must maintain current modular structure (don't break existing abstractions)
- **Performance**: Pre-render must stay under 50ms for smooth TUI experience
- **Dependencies**: Minimize new dependencies; prefer std lib or existing crates

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Pre-render model (not real-time) | Allows complex DSP without CPU pressure; ~20ms render time acceptable for TUI | ✓ Good — smooth experience |
| f64 internal precision | Audio quality and filter stability over memory efficiency | ✓ Good — clean sound |
| Energy-driven generation | Unified abstraction for all musical decisions | ✓ Good — coherent results |
| Zero tests currently | Rapid prototyping phase | ⚠️ Revisit — need stability now |
| Sample fallback pattern | Hybrid synthesis/sample approach for flexibility | ✓ Good — works well |

*Last updated: 2026-02-21 after GSD initialization*

---

## Current Status

2026-03-09 — Skipped human verification for -03 (DSP Engine Block-Based Rendering Optimization). Created  research doc.
