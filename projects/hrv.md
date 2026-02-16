---
layout: default
---

# HRV Monitor

<span class="status-badge status-active">Active Development</span>

[← Back to Signal Processing](../signal-processing) | [← Back to Projects](../projects)

---

## Concept

Heart Rate Variability (HRV) reveals stress, recovery, and autonomic nervous system state through timing variations between heartbeats. Most consumer devices only report derived metrics without providing the underlying RR interval data needed for analysis. This Rust-based driver connects directly to Bluetooth LE heart rate monitors, streams raw RR intervals in real-time, computes time-domain HRV metrics, and logs sessions to columnar Parquet files for downstream analysis.

![HRV Monitor TUI](/images/hrv.png)
*Live RR interval tracking with rolling 60-second charts and computed HRV metrics.*

---

## Key Features

### Real-Time BLE Streaming
Connects to any device implementing the standard Bluetooth Heart Rate Profile (UUID 0x2A37) with RR interval support. Tested with Elite HRV CorSense (finger sensor) and Morpheus M7 (chest strap). Auto-discovery with immediate connection—no need to wait for scan completion.

### Time-Domain HRV Metrics
Computes four core metrics in real-time using rolling 60-second windows:
- **RMSSD**: Root mean square of successive differences (parasympathetic activity)
- **SDNN**: Standard deviation of RR intervals (overall variability)
- **pNN50**: Percentage of intervals differing by >50ms (autonomic balance)
- **AVNN**: Average RR interval (baseline heart rate)

### Terminal Dashboard
Built with `ratatui` for responsive TUI rendering. Live charts show heart rate and RR interval trends. Keyboard navigation (`j`/`k` for device selection, `i` for metric info screen, `q` to quit and save).

### Session Logging
Every session automatically saves to `~/hrv_data/YYYY-MM-DDTHH-MM-SS.parquet` with one row per RR interval. Columns: `timestamp` (UTC), `elapsed_secs`, `heart_rate`, `rr_interval_ms`. Query with DuckDB or load into Polars for analysis.

---

## Architecture

**BLE Stack**: `btleplug` for cross-platform Bluetooth Low Energy communication
**HRV Analysis**: `cardio-rs` for time-domain metric computation
**Storage**: Apache Arrow + Parquet for columnar session files
**TUI**: `ratatui` + `crossterm` for terminal UI
**Platform**: macOS (Linux/Raspberry Pi planned)

---

## Integration with HealthyPi

Designed to complement the [HealthyPi](healthypi) ecosystem:
- **Driver Layer**: This Rust implementation provides native BLE handling for consumer HRV sensors
- **Metric Alignment**: Uses the same HRV metrics (RMSSD, SDNN, pNN50) as HealthyPi's signal processing pipeline
- **Data Format**: Parquet files integrate with HealthyPi's DuckDB analytics layer
- **Use Case**: Detect stress baselines and autonomic trends for agentic health workflows

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

---

## Current Status

Active development. Core functionality complete: BLE scanning, device connection, real-time metric computation, session logging. Next: Linux support, frequency-domain metrics (LF/HF ratio), integration with HealthyPi agent workflows.

---

[← Back to Signal Processing](../signal-processing) | [← Back to Projects](../projects)

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
