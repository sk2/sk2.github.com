---
layout: default
---

# EclipseStack

<span class="status-badge status-planning">Planning</span>

[← Back to Projects](../projects)

---


## The Concept

Solar eclipse photography during totality captures hundreds of frames, but subtle tracker drift prevents perfect alignment for HDR stacking. **EclipseStack** solves this by combining computer vision (solar disk detection, flare tracking) with temporal drift modeling based on EXIF timestamps to achieve sub-pixel alignment.

## Quick Facts

| | |
|---|---|
| **Status** | Planning |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A high-precision alignment tool for solar eclipse photography designed to handle drift and enable HDR stacking. EclipseStack processes hundreds of Sony RAW (.ARW) files taken during totality, automatically detecting the solar disk and flares while modeling tracker drift over time using EXIF metadata.

## Core Value

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

## The Challenge

**Input:** Hundreds of Sony RAW files captured during totality
**Problem:** Subtle tracker drift over several minutes prevents perfect frame alignment
**Constraint:** No background stars available for traditional astrophotography alignment
**Solution:** Detect solar disk center + flares, model drift temporally, align to sub-pixel precision

## Key Features

- **RAW Processing**: Extract and decode Sony RAW files (.ARW) for analysis
- **Disk Detection**: Automatically locate the center of the solar disk/moon silhouette
- **Temporal Drift Modeling**: Use EXIF timestamps to model and extrapolate tracker drift
- **Feature-Based Alignment**: Use solar flares as secondary anchors for sub-pixel and rotational alignment
- **Interactive UI**: Web-based interface to visualize drift path and review alignments
- **Batch Export**: Export aligned frames as TIFF/FITS for PixInsight HDR stacking

## Workflow

1. **Import**: Load hundreds of .ARW files from eclipse imaging session
2. **Analyze**: Detect solar disk center and prominent flares in each frame
3. **Model**: Calculate tracker drift rate from EXIF timestamps
4. **Align**: Apply drift correction + feature-based fine-tuning
5. **Review**: Interactive visualization of alignment quality
6. **Export**: Output aligned TIFF/FITS for PixInsight processing

## Tech Stack

- **Core Processing**: Rust for performance-critical image analysis
- **UI**: Web-based (Tauri or web stack)
- **Output**: TIFF/FITS compatible with PixInsight

## Out of Scope

- **HDR Stacking**: The actual stacking/merging logic (deferred to PixInsight)
- **General Astrophotography**: Optimized specifically for solar eclipse geometry

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
