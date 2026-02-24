---
layout: default
section: projects
---

# Psytrance Generator

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Projects](../projects)

---

## Concept

### What This Is

A generative psytrance synthesis engine with real-time TUI controls. Creates complete tracks driven by a multi-level energy model, with live playback, step editing, and WAV export. Currently produces high-quality procedural psytrance but lacks workflow features for capturing ideas and iterating efficiently.

### Core Value

Energy-driven generative music that sounds professional and lets users quickly explore variations.

---

## Tech Stack

- **Language**: Rust
- **DSP**: Phase-accumulating oscillators, biquad filters, amplitude envelopes (f64 internal precision)
- **Effects** : fundsp
- **WAV Export**: hound
- **CLI**: clap 4
- **Playback**: cpal (real-time audio)
- **TUI**: ratatui + crossterm
- **RNG**: Seeded rand for reproducible generation

---

[← Back to Projects](../projects)
