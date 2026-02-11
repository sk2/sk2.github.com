---
layout: default
---

# Signal Processing & RF Ecosystem

Real-time biometric analysis, passive radar systems, and RF spectrum monitoring — transforming raw sensor data into actionable intelligence through advanced signal processing and machine learning.

---

## The Vision

Signal processing traditionally requires expensive proprietary hardware and closed-source software. This ecosystem demonstrates that research-grade capabilities are achievable with affordable SDR (Software-Defined Radio) hardware, open-source algorithms, and modern multi-agent architectures.

**Core Philosophy:**
- **Real-time processing**: Sub-second latency from sensor to insight
- **Open algorithms**: NeuroKit2, scipy, custom DSP pipelines
- **Affordable hardware**: KrakenSDR ($300), HealthyPi ($200), RTL-SDR ($30)
- **Agent-aware**: Treat sensor streams as events for intelligent automation
- **Reproducible science**: All processing pipelines documented and testable

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│              Raw Signal Sources                          │
│  (HealthyPi · KrakenSDR · Wi-Fi · RTL-SDR · HackRF)    │
└────────────┬────────────────────────────┬────────────────┘
             │                            │
    ┌────────▼─────────┐         ┌────────▼─────────┐
    │  Signal Pipeline │         │   RF Pipeline    │
    │  (Biometrics)    │         │   (Radar/SDR)    │
    └────────┬─────────┘         └────────┬─────────┘
             │                            │
    ┌────────▼─────────┐         ┌────────▼─────────┐
    │ Feature Extract  │         │ Detection/Track  │
    │ (HRV, Resp Rate) │         │ (Targets, Sigs)  │
    └────────┬─────────┘         └────────┬─────────┘
             │                            │
             └──────────┬─────────────────┘
                        │
          ┌─────────────▼──────────────┐
          │    Agent Coordination      │
          │    (NATS Event Stream)     │
          └────────────────────────────┘
```

---

## The Systems

### HealthyPi Ecosystem — Biometric Signal Processing

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/healthypi)

**What It Is:**
A modular, agent-aware health monitoring ecosystem built on top of the HealthyPi hardware platform (ECG, PPG, SpO2, temperature sensors). Translates raw biometric data into actionable insights and automated interventions through research-grade signal processing.

**The Problem:**
Commercial health monitors provide opaque "scores":
- **Black box algorithms**: Can't verify or customize analysis
- **Siloed apps**: No integration with automation or other sensors
- **Limited access**: Proprietary APIs, export-only data
- **Expensive**: Medical-grade devices cost thousands

**The Solution:**
Open-source signal processing on affordable hardware:
- **HealthyPi 6**: $200 for ECG, PPG, respiration, temperature
- **NeuroKit2 integration**: Research-validated HRV analysis
- **Real-time streaming**: NATS message bus for agent coordination
- **Full control**: Access raw signals, customize algorithms

**Signal Processing Pipeline:**

1. **Acquisition** (HealthyPi Hardware)
   - ECG: 125 Hz, 16-bit resolution
   - PPG: Photoplethysmography for heart rate and SpO2
   - Respiration: Impedance pneumography
   - Temperature: Body temp monitoring

2. **Preprocessing** (Python/NeuroKit2)
   ```python
   import neurokit2 as nk

   # Filter ECG signal
   ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=125)

   # Detect R-peaks
   signals, info = nk.ecg_peaks(ecg_cleaned, sampling_rate=125)

   # Compute HRV metrics
   hrv = nk.hrv(signals, sampling_rate=125)
   ```

3. **Feature Extraction**
   - **Time-domain HRV**: RMSSD, SDNN, pNN50
   - **Frequency-domain HRV**: LF, HF, LF/HF ratio
   - **Respiration rate**: Breaths per minute from impedance
   - **SpO2**: Blood oxygen saturation

4. **Event Publishing** (NATS)
   ```json
   {
     "timestamp": "2026-02-12T19:45:00Z",
     "source": "healthypi-agent",
     "metrics": {
       "heart_rate": 72,
       "hrv_rmssd": 42.3,
       "respiratory_rate": 14,
       "spo2": 98,
       "stress_index": 0.35
     },
     "analysis": {
       "status": "elevated_stress",
       "confidence": 0.82,
       "reason": "Low HRV, elevated HR for time of day"
     }
   }
   ```

**Agent Integration:**

Health insights trigger automated responses:
```
HealthyPi Agent: "Elevated stress detected (HRV < 30ms)"
  ↓
Multi-Agent Orchestrator: "Suggest intervention"
  ↓
Workflow Engine:
  ├─ Calendar Agent: Check for meetings (none in next hour)
  ├─ Hue Agent: Dim lights to encourage break
  └─ Notification: "Stress elevated, suggest 5-minute breathing exercise"
```

**Use Cases:**
- **Stress monitoring**: Track HRV trends, trigger interventions
- **Sleep analysis**: Correlate heart rate variability with sleep quality
- **Fitness recovery**: Monitor HRV for training readiness
- **Health research**: Export high-resolution biometric data for analysis

**Current Status:** Phase 6 (NATS integration + reconnection handling + tests)

**Tech Stack:** Python, NeuroKit2, numpy, scipy, NATS

---

### Project Spectra — RF Signal Census

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/signals)

**What It Is:**
An automated RF spectrum monitoring system that discovers, classifies, and tracks radio signals across wide frequency ranges. Transforms raw IQ samples into a structured "Signal Census" through ML classification and distributed acquisition.

**The Problem:**
RF spectrum is invisible and complex:
- **Manual scanning**: Slow, requires expertise
- **Commercial tools**: Expensive spectrum analyzers ($10K+)
- **Unknown signals**: "What's that transmission at 434 MHz?"
- **No persistence**: Signals come and go, hard to track

**The Solution:**
Automated signal discovery and classification:
- **Wide-band scanning**: RTL-SDR ($30) covers 24-1766 MHz
- **HackRF integration**: For transmit/receive and higher frequencies
- **ML classification**: Train on known signals, identify unknown
- **Distributed sensors**: Multiple receivers for geolocation

**Example Screenshot:**

![Spectra Signal Census](images/spectra-screenshot.png)

*Real-time signal detection showing frequency, bandwidth, modulation type, and classification confidence*

**Signal Processing Pipeline:**

1. **Acquisition** (RTL-SDR/HackRF)
   ```python
   from rtlsdr import RtlSdr

   sdr = RtlSdr()
   sdr.sample_rate = 2.4e6
   sdr.center_freq = 433.92e6
   sdr.gain = 'auto'

   # Capture IQ samples
   samples = sdr.read_samples(256*1024)
   ```

2. **Detection** (Energy-based + Pattern matching)
   ```python
   # FFT for spectrum analysis
   spectrum = np.fft.fft(samples)
   power = np.abs(spectrum) ** 2

   # Detect signals above noise floor
   threshold = np.mean(power) + 3 * np.std(power)
   signals = find_peaks(power, height=threshold)
   ```

3. **Feature Extraction**
   - **Center frequency**: Peak location in FFT
   - **Bandwidth**: Signal width at -3dB points
   - **Modulation**: AM, FM, FSK, PSK classification
   - **Time-domain**: Burst pattern, duty cycle

4. **Classification** (ML Pipeline)
   ```python
   # Extract features
   features = extract_signal_features(iq_samples)

   # Classify with trained model
   signal_type = classifier.predict(features)
   # Output: "ISM_433_sensor", "Weather_station", "Unknown"
   ```

5. **Tracking** (Persistence Database)
   ```sql
   -- Store signal observations
   INSERT INTO signals (freq_hz, bandwidth_hz, modulation, first_seen, last_seen)
   VALUES (433920000, 25000, 'OOK', NOW(), NOW());
   ```

**Signal Census Dashboard:**
```
Frequency Range: 430-440 MHz
Active Signals: 12

433.92 MHz  │ Weather Station     │ OOK      │ 95% confidence
434.33 MHz  │ Tire Pressure (car) │ FSK      │ 88% confidence
434.78 MHz  │ Door/Window Sensor  │ OOK      │ 92% confidence
438.55 MHz  │ Unknown (periodic)  │ FM       │ 45% confidence
```

**Use Cases:**
- **IoT security audit**: Discover all wireless devices in environment
- **Interference hunting**: Locate sources of RF interference
- **Signal intelligence**: Catalog local RF emissions
- **Research**: Build datasets of real-world signals for ML training

**Current Status:** Detection pipeline functional, building ML classification

**Tech Stack:** Python, numpy, scipy, RTL-SDR, HackRF, TensorFlow

---

### Passive Radar — KrakenSDR Multi-Beam System

<span class="status-badge status-active">Phase 2/4 (56%)</span> · [Full Details →](projects/passive)

**What It Is:**
A multi-beam passive radar system using KrakenSDR (5-channel coherent SDR) that tracks aircraft by analyzing reflections of existing FM radio transmissions. No active transmission required.

**The Concept:**
Passive radar exploits "illuminators of opportunity":
- **FM radio towers**: Constant broadcast signals
- **TV transmitters**: Known waveforms
- **Cell towers**: Ubiquitous coverage

Aircraft reflect these signals → detect reflections → compute range/bearing → track targets

**The Challenge:**
- **Weak signals**: Reflections are 60-80 dB below direct signal
- **Doppler shifts**: Moving targets change frequency
- **Clutter**: Ground reflections, multipath
- **Correlation**: Must match reflection to original signal

**KrakenSDR Advantages:**
- **5 coherent channels**: Phase-locked for beamforming
- **Direction finding**: Angle-of-arrival from phase differences
- **Multi-beam**: Process multiple directions simultaneously
- **Affordable**: $300 vs. $10K+ commercial passive radar

**Signal Processing Pipeline:**

1. **Reference Channel** (Direct signal from transmitter)
   ```python
   ref_signal = sdr.read_channel(0)  # Direct FM signal
   ref_cleaned = remove_multipath(ref_signal)
   ```

2. **Surveillance Channels** (Look for reflections)
   ```python
   for i in range(1, 5):
       surv_signal = sdr.read_channel(i)
       # Cross-correlate with reference
       correlation = np.correlate(surv_signal, ref_signal)
   ```

3. **Range-Doppler Processing**
   ```python
   # Build range-Doppler map
   for doppler_bin in doppler_range:
       shifted_ref = apply_doppler(ref_signal, doppler_bin)
       range_profile = cross_correlate(surv, shifted_ref)
       rd_map[doppler_bin, :] = range_profile
   ```

4. **Detection** (CFAR - Constant False Alarm Rate)
   ```python
   # Detect targets above adaptive threshold
   targets = cfar_detector(rd_map, threshold=12.0)
   ```

5. **Tracking** (Kalman Filter)
   ```python
   # Track targets across time
   for target in targets:
       track = kalman_filter.update(
           position=target.position,
           velocity=target.velocity
       )
   ```

**Example Output:**
```
Target 1: Range=12.3 km, Bearing=245°, Velocity=450 km/h
  → Commercial aircraft, climbing

Target 2: Range=8.7 km, Bearing=180°, Velocity=180 km/h
  → Small aircraft, descending

Target 3: Range=25.1 km, Bearing=045°, Velocity=500 km/h
  → Fast-moving aircraft, level flight
```

**Use Cases:**
- **Airspace awareness**: Track aircraft without ADS-B
- **Research platform**: Study passive radar techniques
- **Backup system**: Secondary tracking when primary radar fails
- **Education**: Hands-on SDR and radar signal processing

**Current Status:** Phase 2 (Clean, stable foundation for reliable tracking)

**Tech Stack:** Python, numpy, scipy, KrakenSDR firmware, Rust (planned migration)

---

### Wi-Fi Radar — Through-Wall Detection

<span class="status-badge status-active">Active Development</span> · [Full Details →](projects/wifi-radar)

**What It Is:**
A passive radar system that uses existing Wi-Fi signals (2.4 GHz / 5 GHz) for through-wall human detection and localization. Exploits the KrakenSDR coherent array for phase-based tracking.

**The Principle:**
Wi-Fi signals reflect off the human body:
- **Phase changes**: Human movement causes measurable phase shifts
- **Multi-channel**: Coherent array captures phase differences
- **Through-wall**: 2.4 GHz penetrates typical construction materials
- **Passive**: No active transmission required

**Signal Processing:**

1. **Channel State Information** (CSI extraction)
   ```python
   # Capture Wi-Fi packets on all 5 channels
   csi_data = kraken.capture_wifi_csi(duration=1.0)

   # Extract amplitude and phase
   amplitude = np.abs(csi_data)
   phase = np.angle(csi_data)
   ```

2. **Human Detection** (Phase variance analysis)
   ```python
   # Detect movement from phase changes
   phase_diff = phase[t] - phase[t-1]
   movement_score = np.var(phase_diff)

   if movement_score > threshold:
       human_detected = True
   ```

3. **Localization** (Beamforming)
   ```python
   # Compute angle of arrival from phase differences
   phase_delta = phase[ch1] - phase[ch0]
   angle = np.arcsin(phase_delta * wavelength / antenna_spacing)
   ```

**Use Cases:**
- **Security**: Detect intruders through walls
- **Healthcare**: Monitor elderly for falls (non-invasive)
- **Smart home**: Presence detection without cameras
- **Research**: Study RF-based sensing techniques

**Current Status:** Proof-of-concept detection working, refining localization

**Tech Stack:** Rust, KrakenSDR, Wi-Fi CSI extraction

---

## Philosophy: Why This Approach?

### Open Algorithms Over Black Boxes
Commercial health monitors give you a "stress score" — but how is it calculated? NeuroKit2 provides peer-reviewed, documented algorithms. You can verify, customize, and improve the processing pipeline.

### Affordable Hardware Enables Experimentation
$300 KrakenSDR vs. $10K commercial passive radar. $200 HealthyPi vs. $2K medical ECG. Lower cost enables hobbyists, researchers, and educators to explore signal processing without institutional budgets.

### Agent-Aware Architecture
Treating sensor streams as events (not just data) enables coordination. "Elevated stress" isn't just a number — it triggers workflows: check calendar, suggest break, adjust lighting. This is impossible with traditional "analyze and display" architectures.

### Real-Time Processing Matters
Sub-second latency from ECG signal to HRV metric enables real-time feedback. Waiting 5 seconds for processing breaks the feedback loop for breathing exercises or meditation guidance.

---

## Open Source & Contributions

- **HealthyPi Ecosystem**: [github.com/sk2/healthypi](https://github.com/sk2/healthypi)
- **Project Spectra**: [github.com/sk2/spectra](https://github.com/sk2/spectra)
- **Passive Radar**: [github.com/sk2/passive-radar](https://github.com/sk2/passive-radar)
- **Wi-Fi Radar**: [github.com/sk2/wifi-radar](https://github.com/sk2/wifi-radar)

---

[← Back to Projects](projects) | [View CV](cv) | [Network Automation](network-automation) | [Data Analytics](data-analytics) | [Agentic Systems](agentic-systems)

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
.status-planning {
  background-color: #ffc107;
  color: #343a40;
}
</style>
