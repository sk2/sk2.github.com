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

A distributed multi-beam passive radar system based on KrakenSDR hardware. Pi handles data acquisition, Mac/Linux handles compute-intensive DSP. All 4 surveillance channels process in parallel with independent Range-Doppler visualization, per-beam configuration, and real-time performance monitoring. v2 adds per-beam target tracking with geographic visualization, ADS-B correlation, and detection recording for offline analysis.

Clean, understandable, stable codebase that reliably tracks aircraft in real-time.

---

## Core Principles

**Signal Reflection and Processing:**
- **Ambient Transmitters**: FM radio, DVB-T, or cellular signals serve as convenient RF sources
- **Bistatic Geometry**: Separates transmitter and receiver — objects reflect signals toward the receiver
- **Cross-Correlation Processing**: Correlates reference channel (direct signal) with surveillance channels (reflections)
- **Range-Doppler Mapping**: Extracts time-delay and frequency-shift information from reflections

**Signal Processing Chain:**
1. **Reference Signal Capture**: Acquire clean direct signal from transmitter
2. **Reflection Channel Processing**: Receive signals containing reflections
3. **Adaptive Interference Cancellation**: Remove direct signal and static multipath
4. **Cross-Correlation**: Extract reflection signatures via time-delay analysis
5. **Doppler Analysis**: Apply FFT to study frequency shifts from motion
6. **Detection Processing**: Threshold analysis and signal extraction

**Why This Approach:**
- **Cost-Effective**: Uses existing RF infrastructure for experiments
- **Educational**: Practical exploration of bistatic geometry and signal processing techniques

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
