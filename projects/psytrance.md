---
layout: default
section: projects
---

# Psytrance Generator

<span class="status-badge status-active">Phase 1/5 (0%)</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Quick Facts](#quick-facts)
- [Why Generative](#why-generative)
- [Multi-Level Energy Model](#multi-level-energy-model)
- [Sound Design](#sound-design)
- [Pattern Generation](#pattern-generation)
- [Mood Presets](#mood-presets)
- [Usage](#usage)
- [Output](#output)
- [Tech Stack](#tech-stack)
- [What This Is](#what-this-is)
- [Core Value](#core-value)

---

## Concept

A tool for exploring composition ideas through generative algorithms. A multi-level energy model drives every musical decision — from macro-level track arc (intro, build, peak, breakdown) down to per-16th-note accent patterns — producing coherent tracks with musical tension and release.

---

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1/5 (0%) |
| **Language** | N/A |

---

## Why Generative

Most music generation tools either randomize MIDI notes or stitch together pre-made loops. Neither approach produces tracks with intentional structure. This engine takes a different approach: model energy as the primary dimension, then derive all musical elements (pattern density, filter cutoff, accent placement) from that energy curve.

The result is a track that breathes — quiet sections build tension, peaks deliver density, and transitions feel intentional rather than arbitrary.

---

## Multi-Level Energy Model

The architectural core. Energy flows from macro structure down to individual note accents:

```
Macro (Track Arc)
  Control-point curves: intro → build → peak → breakdown → outro
  Linear interpolation between user-defined energy waypoints

    Meso (Phrase Breathing)
      8-bar phrase patterns creating tension/release cycles
      Layered on top of macro curve

        Micro (Groove Accents)
          16th-note accent patterns for swing and syncopation
```


```
          Drives velocity and timing variations

          Sub-Channels (Per-Element)
            Each element (kick, bass, hat, clap) has independent:
            - Energy threshold (when it activates)
            - Response curve (how it scales with energy)
            - Attack time (how quickly it responds)
```

---

## Sound Design

Phase-accumulating oscillators, biquad filters, and amplitude envelopes:

- **Kick**: Sine oscillator with pitch envelope (150 Hz → 50 Hz) plus a click transient for attack definition
- **Bass**: Sawtooth oscillator through a biquad lowpass filter with energy-driven cutoff modulation
- **Hi-hats**: Noise through a highpass filter — closed at 7 kHz with 30 ms decay, open at 6 kHz with 150 ms decay
- **Clap**: Multi-tap noise (3 bursts) through highpass filter, mimicking multiple hands

---

## Pattern Generation

Patterns respond to the energy model rather than following fixed sequences:

- **Kick**: Scales from 2-beat patterns at low energy through 4-on-the-floor to ghost 16th notes at peak
- **Bass**: Rolling 16th-note patterns with density proportional to energy level
- **Hi-hats**: Off-beat syncopation with closed/open variation driven by accent patterns
- **Clap**: Enters on beats 2 and 4 when energy exceeds a configurable threshold

---

## Mood Presets

Five presets, each defining a key, scale, energy curve shape, and filter range:

| Mood | Key | Scale | Character |
|------|-----|-------|-----------|
| Dark | D | Phrygian | Dark, driving |
| Mysterious | C# | Phrygian Dominant | Goa trance exotica |
| Euphoric | E | Lydian | Bright, uplifting |
| Melancholy | C | Harmonic Minor | Sad tension |
| Aggressive | D# | Minor | Hard, driving |

---

## Usage

```bash
cargo run

cargo run -- --bpm 145 --bars 64 --mood euphoric --output track.wav

cargo run -- --seed 42 --output reproducible.wav

cargo run -- --key D2 --scale phrygian
```

Without `--output`, the engine launches an interactive TUI with real-time playback, energy visualization, and pattern display.

---

## Output

- 16-bit stereo WAV at 44.1 kHz
- Soft-clip limiter (tanh normalization to -0.5 dB)
- Constant-power stereo panning
- Full tracks render in under 30 seconds

---

## Tech Stack

- **Language**: Rust
- **DSP**: Phase-accumulating oscillators, biquad filters, amplitude envelopes (f64 internal precision)
- **Effects** (Phase 2+): fundsp
- **WAV Export**: hound
- **CLI**: clap 4
- **Playback**: cpal (real-time audio)
- **TUI**: ratatui + crossterm
- **RNG**: Seeded rand for reproducible generation

---

## What This Is

A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently.

---

## Core Value

Energy-driven generative music that sounds professional and lets users quickly explore variations.

---

[← Back to Projects](../projects)
