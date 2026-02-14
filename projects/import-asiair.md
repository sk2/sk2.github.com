---
layout: default
section: photography
---

# ASIAIR Import Tool

<span class="status-badge status-active">Functional — Documentation Phase</span>

[← Back to Photography](../photography)

---

## The Insight

Eliminates manual file sorting after imaging sessions — scan hundreds of frames, organize by target/filter/date, validate calibration frame availability, and go straight to PixInsight processing.

## Quick Facts

| | |
|---|---|
| **Status** | Functional — Documentation Phase |
| **Language** | Python |
| **Started** | 2026 |

---

## What This Is

A Python tool that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames (darks, flats, bias), and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.

## Key Features

- **Multi-Location Scanning**: Scans ASIAIR backup paths (Udisk/EMMC across Autorun, Preview, Plan, Live folders)
- **FITS Header Reading**: Extracts image type, filter, exposure, date, and target from FITS metadata
- **Observation Night Grouping**: Date-shifted timestamps (16-hour shift to Adelaide timezone) for correct night grouping
- **Calibration Frame Matching**: Automatically copies matching darks, flats, and bias frames per filter and observation night
- **PixInsight-Ready Output**: Creates `Import/{date}/{Target}/Data/P_{obsnight}/` directory structure for WBPP
- **Duplicate Prevention**: Aborts if import date folder already exists
- **Statistics**: Generates `stats.csv` and `summary.csv` with frame counts per target and filter

## Tech Stack

Python (astropy, pandas, arrow, rich, tqdm), FITS file I/O, zoneinfo (Adelaide timezone)

---

[← Back to Photography](../photography)
