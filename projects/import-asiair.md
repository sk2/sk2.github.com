---
layout: default
section: photography
description: "ASIAIR Import — scans ASIAIR backup folders, reads FITS headers, and organises captured frames by target and observation night into a structure ready for PixInsight's WBPP workflow."
hand_written: true
---

# ASIAIR Import Tool

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

---

## Concept

A glue tool that lives between an ASIAIR session in the field and a PixInsight stack at the desk. ASIAIR scatters captures across several backup folders (Autorun, Preview, Plan, Live) on internal storage and a USB stick; PixInsight's Weighted Batch Preprocessing wants frames sorted by target and observation night. This script makes that translation reliable for hundreds of frames per session.

Metadata comes from FITS headers, not from filenames, so the organisation is grounded in what was actually captured rather than whatever naming convention happened that night.

---

## Architecture

<div class="mermaid">
flowchart TD
    BK["ASIAIR Backup Sources<br/><small>Udisk · EMMC · Autorun · Plan · Live · Preview</small>"]
    SCAN["Recursive Scan<br/><small>FITS / XISF discovery</small>"]
    META["Header Reader<br/><small>target · date · filter · exposure</small>"]
    GROUP["Group by Target / Night<br/><small>session boundaries from timestamps</small>"]
    OUT["WBPP-Ready Tree<br/><small>target/night/{lights,flats,darks,bias}</small>"]
    BK --> SCAN
    SCAN --> META
    META --> GROUP
    GROUP --> OUT
</div>

The night boundary is computed from the capture timestamps and local sunset, not from the calendar date — a session that crosses midnight stays a single night in the output tree.

---

[← Back to Photography & Astrophotography](../photography)
