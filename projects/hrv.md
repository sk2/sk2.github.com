---
layout: default
section: agentic-systems
---

# HRV Monitor

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Concept

Rust TUI application for real-time heart rate variability monitoring. Connects to BLE heart rate sensors via `btleplug`, computes time-domain HRV metrics (RMSSD, SDNN, pNN50) using `cardio-rs`, and stores session data in Apache Arrow/Parquet format for longitudinal analysis.

---

## Architecture

- **BLE**: `btleplug` for cross-platform Bluetooth Low Energy communication
- **HRV analysis**: `cardio-rs` for time-domain metric computation
- **Storage**: Apache Arrow + Parquet for columnar session files
- **TUI**: `ratatui` + `crossterm` for terminal interface
- **Platform**: macOS (Linux/Raspberry Pi planned)

---

[← Back to Autonomous Systems](/agentic-systems)

[← Back to Projects](/projects)
