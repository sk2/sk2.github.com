---
layout: default
section: signal-processing
---

# Signal Reflection Analysis

<span class="status-badge status-updated">Recently Updated</span>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Concept

### What This Is

A distributed multi-beam passive radar system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

### Core Value

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

---

## Architecture

**v1.0 Foundation :**
Established distributed multi-beam architecture using ProcessPoolExecutor for parallel surveillance channels. CFAR detection  implemented and verified.

**v2.0 Real-Time Analysis :**

Currently implementing analysis and association logic . The system now maintains analysis across multiple beams with detection-level recording for storage efficiency.

**Key Features:**
- **Multi-Beam Processing**: Parallel surveillance channels across 5-channel coherent array
- **CFAR Detection**: Constant False Alarm Rate detection complete
- **Analysis Management**: Per-beam analysis with cross-beam fusion planned for v3
- **Real-Time Operation**: Signal analysis with sub-second latency

---

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)
