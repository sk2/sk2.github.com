---
layout: default
section: photography
---

# EclipseStack

<span class="status-badge status-planning">Phase 1 — Ingestion & Foundation</span>

[← Back to Photography](../photography)

---

## Concept

Enable high-fidelity HDR solar composites by providing sub-pixel alignment of eclipse frames through a combination of computer vision and temporal drift modeling.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1 — Ingestion & Foundation |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A Rust-powered utility with a web-based UI (Tauri + Leptos) for aligning hundreds of RAW solar eclipse images taken during totality. It combines solar disk feature detection with temporal drift extrapolation from EXIF data to produce a perfectly aligned frame set ready for HDR stacking in PixInsight.

## Key Features

- **Automated Disk Centering**: Hough Circle Transform to locate and align the solar disk across frames
- **Sub-Pixel Flare Alignment**: Solar limb feature tracking for sub-pixel registration accuracy
- **Temporal Drift Modeling**: EXIF-based drift extrapolation for frames where solar features are obscured
- **Batch Processing**: Handles hundreds of Sony RAW (.ARW) files with tile-based demand-driven processing to avoid OOM
- **Interactive UI**: Visual drift path plots, manual X/Y/rotation nudging, onion-skin verification
- **PixInsight Export**: 16-bit TIFF output with metadata tags for seamless PixInsight integration

## Roadmap

- **Phase 1: Ingestion & Foundation** — RAW file loading/decoding, EXIF timestamp extraction, format validation
- **Phase 2: Core Geometry Alignment** — Solar disk detection, pixel-level centering, field rotation correction
- **Phase 3: Fine Feature & Drift Modeling** — Sub-pixel accuracy via flare tracking, temporal drift interpolation
- **Phase 4: Interactive Interface** — Tauri/Leptos UI with drift visualization, manual nudging, onion-skin overlay
- **Phase 5: Production Export** — Batch 16-bit TIFF export with PixInsight compatibility validation

## Tech Stack

Rust (libraw-rs, OpenCV, kornia-rs, rayon), Tauri v2 + Leptos (web UI), kamadak-exif

---

[← Back to Photography](../photography)
