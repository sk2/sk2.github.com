---
layout: default
section: photography
---

# EclipseStack

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Photography](../photography)

[← Back to Projects](../projects)

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

[← Back to Photography](../photography)
