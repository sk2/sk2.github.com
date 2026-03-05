---
layout: default
section: projects
---

# Project: NAS Cleanup & Intelligence

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Architecture](#architecture)
- [Goal](#goal)
- [Key Components](#key-components)
- [Tech Stack](#tech-stack)
- [Current Status](#current-status)

## Architecture

- **Language:** Rust (for performance and safety).
- **Core Engine:** A CLI tool capable of rapid traversal and content-based hashing.
- **Execution:** Optimized for Docker/Native execution on DSM to minimize network latency.
- **Data Model:** Indexing layer to store file hashes and metadata for fast comparison.
- **Intelligence:** Future integration of ML for content-based classification.

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

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

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)
