---
layout: default
section: data-analytics
---

# NAS Cleanup & Intelligence

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Current Status](#current-status)

## Concept

Rust CLI for managing large-scale Synology NAS file systems. Performs duplicate detection (bit-for-bit and fuzzy), astrophotography file optimization (ASIair workflow cleanup), conventional RAW/sidecar management, and intelligent organization. Designed for Docker or native execution on DSM to minimize network latency during scanning.

---

## Architecture

- **Scanner**: parallel directory traversal using `jwalk` with `rayon` thread pool
- **Hasher**: BLAKE3 content hashing for fast duplicate identification
- **Deduplicator**: identifies exact and fuzzy duplicates across large file trees
- **Cleaner**: workflow-specific rules for astrophotography (ASIair) and photography (RAW/sidecar pairing)
- **TUI**: `ratatui` terminal interface for reviewing and acting on findings

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust |

---

## Goal

Develop a high-performance Rust application to manage large-scale Synology NAS file systems, focusing on duplicate detection, astrophotography optimization, conventional RAW photography management, and intelligent organization.

---

## Key Components

- **Scanner:** Parallel directory walker utilizing `jwalk` or `rayon`.
- **Hasher:** `blake3` based content hashing.
- **Deduplicator:** Logic to identify bit-for-bit and fuzzy duplicates.
- **Cleaner:** Workflow-specific cleanup rules (e.g., ASIair/Astrophotography and Conventional RAW/Sidecar management).
- **TUI:** Terminal interface for reviewing and acting on findings.

---

## Tech Stack

- **Rust:** `tokio`, `rayon`, `blake3`, `jwalk`, `ignore`, `clap` (CLI), `ratatui` (TUI).
- **DSM Integration:** `syno-api` (if available/needed), BTRFS ioctls.

---

## Current Status

2026-03-03 - Completed 10-01-PLAN.md (Doctor Diagnostics)
