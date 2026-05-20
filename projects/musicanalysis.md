---
layout: default
section: data-analytics
description: "MusicBrain — modular music information retrieval pipeline: HT-Demucs stem separation, per-stem analysis, structured FeatureSet, and genre-specific semantic interpretation."
hand_written: true
---

# MusicBrain

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Concept

A music-information-retrieval pipeline that takes an audio file and produces both a low-level FeatureSet (rhythm, harmony, timbre, dynamics) and a high-level SemanticResult (genre-specific interpretation — what the piece is doing, in human-readable terms).

Source separation runs first: HT-Demucs splits the input into stems so every downstream analyser sees a clean isolated track rather than fighting source overlap. Each stem is then analysed independently and the results are recombined into a single time-aligned feature surface.

---

## Architecture

<div class="mermaid">
flowchart TD
    IN["Audio Input<br/><small>file or stream</small>"]
    SEP["HT-Demucs Separation<br/><small>drums · bass · vocals · other</small>"]
    A1["Per-Stem Analysis<br/><small>spectral · rhythmic · harmonic</small>"]
    FS["FeatureSet<br/><small>frame-level structured features</small>"]
    SR["SemanticResult<br/><small>genre-specific expert analysis</small>"]
    IN --> SEP
    SEP --> A1
    A1 --> FS
    FS --> SR
</div>

The FeatureSet is the data contract between mid-level (mechanical) and high-level (interpretive) analysis. Genre experts read the FeatureSet, not the audio, so new genre modules can be added without re-running source separation.

---

[← Back to Data & Analytics](../data-analytics)
