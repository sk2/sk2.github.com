---
layout: default
section: photography
description: "EclipseStack — sub-pixel alignment of hundreds of eclipse RAW frames for HDR composite stacking, combining solar-disk detection with EXIF-timestamp drift modelling."
hand_written: true
---

# EclipseStack

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">TypeScript</span>
</div>

---

## Concept

Alignment for hundreds of RAW frames captured during totality, ready to hand to a stacking tool for HDR composite work. The hard part isn't detecting the solar disk in any one frame — it's bridging the frames where the disk is occluded or the contrast is wrong, without losing sub-pixel precision.

The approach combines two signals: confident frames where the solar disk (or the moon's silhouette) is unambiguous, and a temporal-drift model fitted to the camera's EXIF timestamps. The drift model fills in the alignment for the awkward frames, and solar flares act as secondary anchors for sub-pixel and rotational refinement.

---

## Architecture

<div class="mermaid">
flowchart TD
    RAW["RAW Frame Set<br/><small>hundreds of files, full-totality span</small>"]
    DET["Disk / Crescent Detection<br/><small>solar disk · lunar silhouette</small>"]
    DRIFT["Temporal Drift Model<br/><small>EXIF timestamp regression</small>"]
    FLARE["Flare Anchor Detection<br/><small>sub-pixel, rotational</small>"]
    ALIGN["Sub-Pixel Aligner<br/><small>confident anchors + drift fill</small>"]
    UI["Web Review UI<br/><small>drift paths · seed confident frames</small>"]
    OUT["TIFF / FITS Export<br/><small>ready for HDR stacking</small>"]
    RAW --> DET
    RAW --> DRIFT
    RAW --> FLARE
    DET --> ALIGN
    DRIFT --> ALIGN
    FLARE --> ALIGN
    ALIGN --> UI
    UI --> OUT
</div>

The web UI exists because eclipse data is finicky enough that fully-automatic alignment is the wrong target. The tool's job is to be confident about the easy frames and visibly honest about the hard ones, so a human can seed the gaps.

---

[← Back to Photography & Astrophotography](../photography)
