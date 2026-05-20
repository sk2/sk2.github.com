---
layout: default
section: signal-processing
description: "Bistatic signal-reflection analysis on KrakenSDR — coherent IQ acquisition on a small node, distributed DSP on a workstation, four parallel surveillance beams with confirmed-track lifecycle."
hand_written: true
---

# Signal Reflection (KrakenSDR Multi-Beam)

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span>
</div>

---

## Concept

Bistatic illumination-reflection analysis on a KrakenSDR. A small acquisition node does nothing but capture coherent IQ across four channels and stream it to a workstation; all DSP — cross-ambiguity, beamforming, track formation, visualisation — runs on the more capable host. The split keeps the acquisition node electrically quiet and lets the processing side scale independently.

Four surveillance beams run in parallel with independent Range-Doppler displays, per-beam configuration of the illuminator of opportunity (FM broadcast, DAB+, DVB-T), and a confirmed-track lifecycle that requires M-of-N detections before a track is promoted from tentative to confirmed.

---

## Architecture

<div class="mermaid">
flowchart TD
    SDR["KrakenSDR<br/><small>4-channel coherent IQ</small>"]
    ACQ["Acquisition Node<br/><small>capture and stream only</small>"]
    NET["UDP Stream<br/><small>IQ to workstation</small>"]
    CAF["Cross-Ambiguity (CAF)<br/><small>per beam · 100 ms coherent integration</small>"]
    BF["Beamforming<br/><small>4 surveillance beams in parallel</small>"]
    TRK["Track Lifecycle<br/><small>tentative → confirmed (M-of-N)</small>"]
    DISP["Range-Doppler Display<br/><small>per beam, per illuminator</small>"]
    SDR --> ACQ
    ACQ --> NET
    NET --> CAF
    CAF --> BF
    BF --> TRK
    TRK --> DISP
</div>

The 100 ms coherent integration time is the dominant cost in the latency budget — the FFT inside the cross-ambiguity computation accounts for most of the per-beam wall time. Beam parallelism is across CPU cores, not across SDRs; the four beams share one coherent capture, not four independent radios.

---

[← Back to Signal Processing](../signal-processing)
