---
layout: default
section: photography
description: "Alignment tool for solar eclipse HDR composites. Takes hundreds of RAW frames captured during totality and produces sub-pixel-aligned output ready for HDR…"
---

# EclipseStack: Expertise-Led Solar Alignment

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">TypeScript</span>
</div>

---

## Concept

Alignment tool for solar eclipse HDR composites. Takes hundreds of RAW frames captured during totality and produces sub-pixel-aligned output ready for HDR stacking in PixInsight. Addresses tracker drift by combining solar disk detection (computer vision) with temporal drift modeling from EXIF timestamps — the constant drift rate fills alignment gaps between confident frames.

---

## Features

- Sony RAW (.ARW) file decoding and processing
- Automatic solar disk and moon silhouette center detection
- Temporal drift modeling using EXIF timestamps for frame-to-frame extrapolation
- Solar flare detection as secondary anchors for sub-pixel and rotational alignment
- Web UI for visualizing drift paths, reviewing alignments, and seeding confident frames
- Batch export to TIFF/FITS for PixInsight

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust |

---

## Core Value

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of totality sequences through a combination of geometric computer vision and temporal drift modeling.

---

## Requirements

...

---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] **RAW Processing:** Extract and decode Sony RAW files for processing.
- [ ] **Disk Detection:** Automatically locate the center of the solar disk/moon silhouette in each frame.
- [ ] **Temporal Drift Modeling:** Use EXIF timestamps to model and extrapolate tracker drift across frames.
- [ ] **Feature-Based Alignment:** Identify and use solar flares as secondary anchors for sub-pixel and rotational alignment.
- [ ] **Interactive UI:** A web-based interface to visualize the drift path, review alignments, and manually "seed" confident frames.
- [ ] **Batch Export:** Export aligned frames in a format optimized for PixInsight (TIFF/FITS).

---

## # Out of Scope

- **HDR Stacking:** The actual stacking/merging logic (deferred to PixInsight).
- **General Astrophotography:** This tool is specifically optimized for solar eclipse geometry.
- **ML Alignment (v1):** Machine learning-based feature detection is deferred to v2.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Rust Language | High performance for image processing and safety. | — Pending |
| Web UI | Better accessibility and visualization for manual alignment nudging. | — Pending |
| EXIF-Based Extrapolation | Leverages the constant drift rate to fill gaps between confident frames. | — Pending |

*Last updated: Friday 13 February 2026 after initialization*
