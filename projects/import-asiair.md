---
layout: default
section: photography
---

# ASIAIR Import Tool

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Photography](../photography)

[← Back to Projects](../projects)

---

## Concept

Python script that automates post-imaging file organization for astrophotography. Scans ASIAIR backup locations (Udisk/EMMC across Autorun, Preview, Plan, and Live folders), reads FITS headers to extract metadata, and organizes hundreds of frames by target and observation night into a directory structure ready for PixInsight's Weighted Batch Preprocessing (WBPP) workflow.

---

## Features

- Scans multiple ASIAIR backup locations and FITS/XISF formats
- Groups frames by observation night using timezone-shifted timestamps (16-hour shift for Adelaide)
- Organizes light frames into `Import/{date}/{Target}/Data/P_{obsnight}/` structure
- Copies matching flat frames per filter per night, warns on missing calibration data
- Generates `stats.csv` (detailed frame listing) and `summary.csv` (frame count totals)
- Prevents destination folder overwrites to protect previous imports
- Uses astropy for FITS handling and pandas for data organization

---

[← Back to Photography](../photography)
