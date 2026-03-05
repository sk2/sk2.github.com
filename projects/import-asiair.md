---
layout: default
section: projects
---

# ASIAIR Import Tool

<span class="status-badge status-active">Last Active: 2026-02-11</span>

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Concept

A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.

Eliminates manual file sorting after imaging sessions - scan hundreds of frames, organize by target/filter/date, validate calibration frame availability, and go straight to PixInsight processing.

A Python script that automates post-imaging-session file organization for astrophotography. It batch-imports FITS files from ASIAIR backup locations, organizes them by target and observation night, copies matching calibration frames, and prepares the directory structure for PixInsight's WBPP (Weighted Batch Preprocessing) workflow.

Eliminates manual file sorting after imaging sessions - scan hundreds of frames, organize by target/filter/date, validate calibration frame availability, and go straight to PixInsight processing.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## # Validated

<!-- Existing capabilities from current codebase -->

- ✓ Scan multiple ASIAIR backup locations (Udisk/EMMC across Autorun/Preview/Plan/Live folders) — existing
- ✓ Read FITS file headers to extract image metadata (type, filter, exposure, date, target) — existing
- ✓ Identify observation nights using date-shifted timestamps (16-hour shift to Adelaide timezone) — existing
- ✓ Extract target names from light frame filenames — existing
- ✓ Organize light frames into directory structure: `Import/{date}/{Target}/Data/P_{obsnight}/` — existing
- ✓ Copy matching flat frames for each filter used on observation night — existing
- ✓ Validate flat frame availability and warn when missing for a filter — existing
- ✓ Prevent destination folder overwrites (abort if import date folder exists) — existing
- ✓ Log frame counts grouped by target and filter — existing
- ✓ Generate stats.csv with detailed frame listing — existing
- ✓ Generate summary.csv with frame count totals — existing

---

## # Active

<!-- Current scope - documenting/organizing existing script -->

(None - capturing existing functionality)

---

## # Out of Scope

- Image stacking — PixInsight WBPP handles this
- Calibration processing — PixInsight WBPP handles this
- Dark/bias frame handling — not currently in workflow
- Cross-platform path handling — Windows-specific (D: drive paths)
- GUI interface — command-line script sufficient

---

## Context

**Astrophotography workflow:**
- ASIAIR device controls telescope/camera during imaging sessions
- Produces FITS files stored on Udisk/EMMC storage
- Files backed up to PC in multiple folders (Autorun, Preview, Plan, Live)
- After a night of imaging, hundreds of frames need organizing
- PixInsight's WBPP requires specific directory structure to process

**Current environment:**
- Windows-based workflow (D: drive paths)
- Adelaide timezone (Australia/Adelaide) with 16-hour observation night shift
- Uses astropy for FITS handling, pandas for data organization
- Dependencies: arrow, coloredlogs, tqdm, pandas, astropy

**File types:**
- Light frames: actual target exposures (deep sky objects)
- Flat frames: calibration exposures (per filter, per night)
- FITS and XISF formats supported

---

## Constraints

- **Platform**: Windows — hardcoded D: drive paths
- **Timezone**: Australia/Adelaide — observation night calculated with 16-hour shift
- **Tech stack**: Python with astropy, pandas — existing dependencies

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Use 16-hour shift for obs night | Imaging sessions span midnight; shift groups frames by session | — Pending |
| Copy files vs move | Preserves ASIAIR backups as source of truth | — Pending |
| Abort on existing destination | Prevents accidental overwrites of previous imports | — Pending |
| Target name from filename | ASIAIR encodes target in filename (second underscore-delimited element) | — Pending |

*Last updated: 2026-02-11 after initialization*

---

## Current Status

2026-02-11 —  plans across 4 waves

---

[← Back to Projects](../projects)
