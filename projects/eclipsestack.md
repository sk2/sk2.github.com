---
layout: default
section: projects
---

# EclipseStack

<span class="status-badge status-active">Active</span>

[← Back to Projects](../projects)

---

## Concept

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

EclipseStack is a Rust-powered utility (with a web-based UI) specifically designed to align hundreds of RAW solar eclipse images taken during totality. It addresses the challenge of tracker drift by combining image feature detection (solar disk and flares) with temporal extrapolation based on EXIF data. The goal is to produce a perfectly aligned set of frames ready for HDR stacking in professional tools like PixInsight.

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Context & Constraints

- **Input:** Hundreds of Sony RAW files (.ARW).
- **Subject:** Total solar eclipse (totality), centered disk, visible solar flares.
- **Challenge:** Subtle tracker drift over time; lack of background stars for traditional alignment.
- **Technology:** Rust (core processing), Web-based UI (potentially via Tauri or a web-tech stack), EXIF data for drift modeling.
- **Output:** Aligned frames (likely TIFF/FITS) compatible with PixInsight.

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

---

[← Back to Projects](../projects)
