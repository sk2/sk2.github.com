---
layout: default
section: agentic-systems
---

# HRV Monitor

<span class="status-badge status-active">Active</span>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Concept

Developing...

---

## Architecture

**BLE Stack**: `btleplug` for cross-platform Bluetooth Low Energy communication
**HRV Analysis**: `cardio-rs` for time-domain metric computation
**Storage**: Apache Arrow + Parquet for columnar session files
**TUI**: `ratatui` + `crossterm` for terminal UI
**Platform**: macOS (Linux/Raspberry Pi planned)

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Rust |
| BLE | `btleplug` |
| TUI | `ratatui`, `crossterm` |
| HRV Analysis | `cardio-rs` |
| Storage | Apache Arrow, Parquet |
| Platform | macOS (Linux planned) |

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
</style>

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)
