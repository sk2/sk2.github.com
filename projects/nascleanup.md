---
layout: default
section: data-analytics
---

# NAS Cleanup & Intelligence

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

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

[← Back to Data Analytics](../data-analytics)
