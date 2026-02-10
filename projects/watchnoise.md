---
layout: default
---

# WatchNoise (Wave)

<span class="status-badge status-active">v1.1 Shipped</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | v1.1 shipped (Feb 9, 2026) |
| **Language** | Swift (SwiftUI) |
| **Platform** | watchOS 9.0+ |
| **Phase** | 15/17 (38/42 plans complete, 90%) |
| **Latest Release** | v1.1 Adaptive Audio Features |
| **Started** | 2026 |
| **License** | TBD |

---

## Overview

WatchNoise is a minimalist Apple Watch app that generates ambient noise for sleep through Bluetooth headphones. Procedural audio synthesis creates white noise, brown noise, blended soundscapes, and binaural beats—all from your wrist. Features adaptive audio with frequency calibration, heartbeat synchronization, and environmental noise monitoring.

## Problem It Solves

Sleeping in shared or noisy environments presents challenges:

**Shared Spaces:**
- Snoring in dormitories or retreats
- Human-centric noises that disrupt sleep
- Need for "noble silence" (no light, no speaker)

**Commercial Sleep Apps:**
- Require iPhone with screen on
- Drain phone battery overnight
- Not optimized for watch-only use
- Generic audio that doesn't adapt to individual hearing

**Generic White Noise:**
- One-size-fits-all frequencies
- No personalization for hearing sensitivity
- Static audio that doesn't respond to environment
- No integration with biometric data

**WatchNoise provides:**
- Watch-only operation (no phone required)
- Bluetooth headphones only (silent, private)
- Personalized frequency calibration for individual hearing
- Heartbeat-synchronized audio for grounding
- Adaptive masking based on environmental noise
- 6-8 hour battery life with background playback

## Architecture

### Procedural Audio Engine

Real-time synthesis using AVAudioSourceNode:

**Noise Generators:**
```swift
protocol NoiseGenerator {
    func generateAudio(frameCount: AVAudioFrameCount,
                      format: AVAudioFormat,
                      buffer: UnsafeMutablePointer<Float>)
}
```

**Implementations:**
- **White Noise**: Full-spectrum random signal
- **Brown Noise**: One-pole IIR lowpass filter (1/f² spectral density)
- **Blended Noise**: Time-varying LFO modulation between white/brown
- **Binaural Beats**: Stereo tone generation with precise frequency control

**Performance:**
- Sub-11ms render times (prevents audio dropouts)
- 256-sample buffer (~10ms latency)
- Optimized for Apple Watch processor

### Adaptive Audio Features

**Frequency Calibration ("Ear-Print"):**
- 10-step sweep from 20 Hz to 8 kHz
- User rates relaxation level at each frequency
- Identifies preferred frequency for personalization
- +4dB bias applied to preferred range
- Results persist across sessions

**Heartbeat Synchronization:**
- 4 BPM presets: 50, 55, 60, 65 BPM
- 5-8% amplitude modulation depth
- Grounding effect for stress reduction
- Optional feature (battery-first design)

**Adaptive Noise Masking:**
- Microphone-based environmental monitoring
- vDSP RMS-to-dB analysis (0.5s periodic sampling)
- Dynamic volume/frequency adjustment (v1.2)
- Preserves battery with periodic analysis vs. continuous

### State Management

Four-state playback machine:

```
stopped → starting → playing → pausing
```

**PlaybackManager:**
- Coordinates AudioEngine and AudioSessionManager
- Async/await for clean state transitions
- Handles Bluetooth route verification
- Auto-pause on headphone disconnect

**Settings Persistence:**
- @AppStorage for noise type, volume, binaural configuration
- Calibration results stored locally
- Per-feature toggles for battery optimization

### Bluetooth Audio Routing

AVAudioSession configuration:

**Routing Policy:**
- `.longFormAudio` category for background playback
- Bluetooth-only verification (rejects watch speaker)
- Stereo validation for binaural beats
- Auto-pause on route change (disconnect handling)

**User Experience:**
- Friendly errors when Bluetooth unavailable
- Automatic reconnection on headphone pairing
- No manual audio routing required

## Features

### v1.0 MVP (Feb 8, 2026) ✅

**Core Audio:**
- Three noise types: white, brown, blended
- Live hot-swap (change types without stopping playback)
- Procedural synthesis (no audio files)

**Binaural Beats:**
- 5 presets: Sleep, Focus, Relaxation, Meditation, Deep Sleep
- Custom parameters (carrier frequency, beat frequency)
- Noise bed mixing (combine beats with ambient noise)
- Stereo audio generation (2-20 Hz beat frequencies)

**Playback:**
- Large play/pause button with SF Symbols
- Digital Crown volume control
- Settings persistence
- Background audio with screen off

**Battery:**
- 6-8 hour continuous playback
- <12% base drain per hour
- Sleep-friendly optimization

### v1.1 Adaptive Features (Feb 9, 2026) ✅

**Frequency Calibration:**
- Interactive 10-step sweep (20 Hz - 8 kHz)
- Relaxation rating at each frequency
- +4dB bias for preferred range
- Persistent personalization
- Re-calibration available anytime

**Heartbeat Synchronization:**
- 4 BPM presets for resting heart rates
- Optional amplitude modulation
- Grounding effect for stress/anxiety
- Independent toggle (battery conscious)

**Environmental Monitoring:**
- Microphone RMS-to-dB analysis
- 0.5s periodic sampling (battery efficient)
- Infrastructure for adaptive masking
- Privacy-first (no audio recording)

**Battery Optimization:**
- All adaptive features default OFF
- Individual toggles per feature
- Smart disable on screen-off/disconnect
- <15% total drain with all features enabled

**UI Enhancements:**
- Settings reorganization
- Clear feature descriptions
- Calibration flow with instructions
- Binaural preset improvements

### v1.2 In Progress: Polish & Validation

**Full Adaptive Masking:**
- Dynamic volume adjustment based on environmental noise
- Frequency-aware masking algorithm
- Real-time response to noise changes

**Tech Debt Resolution:**
- CalibrationEngine timestamp tracking
- Settings section reorganization
- Orphaned singleton cleanup

**Hardware Validation:**
- Overnight battery testing on physical device
- Validate <15% drain targets
- Tune adaptive feature effectiveness

**Future: FlowState (macOS)**
- Productivity menu bar app
- Task-linked procedural audio
- "Genetic System" TODO integration
- Flow state reporting and metrics

## Use Cases

**Retreat/Dormitory Sleep:**
Primary use case. Block snoring and environmental noise in shared spaces while maintaining "noble silence" (no light/speaker). Personalized frequency calibration for individual hearing sensitivity.

**Travel Sleep:**
Airplanes, trains, hotels. Bluetooth-only operation avoids disturbing neighbors. Works without iPhone.

**Focus Meditation:**
Binaural beats for meditation states (theta/alpha waves). Heartbeat sync provides grounding for anxiety.

**Stress Reduction:**
Brown noise with heartbeat synchronization. Calming effect through frequency personalization and rhythmic modulation.

## Technical Details

### Audio Specifications

**Sample Rate:** 44.1 kHz
**Bit Depth:** 32-bit float
**Channels:** Stereo (required for binaural beats)
**Buffer Size:** 256 samples (~5.8ms @ 44.1 kHz)
**Latency:** <11ms render time

### Binaural Beat Frequencies

| Preset | Beat Frequency | Brain Wave | Effect |
|--------|---------------|------------|--------|
| Deep Sleep | 2 Hz | Deep Delta | Very deep sleep |
| Sleep | 4 Hz | Delta | Restful sleep |
| Meditation | 6 Hz | Theta | Meditative state |
| Relaxation | 8 Hz | Alpha | Calm relaxation |
| Focus | 15 Hz | Beta | Concentration |

### Battery Performance

**Base Playback:** <12% drain/hour
**With Calibration:** +<1% overhead
**With Heartbeat:** +<2% overhead
**With Adaptive Masking:** +~7% overhead (periodic sampling)
**Total (All Features):** <15% drain/hour

**Target:** 6-8 hours continuous playback

### Development Metrics

**Phase Completion:** 90% (38/42 plans)
**Total Execution Time:** 3.3 hours (v1.0: 2.5h, v1.1: 0.6h, v1.2: 0.4h)
**Average Plan Duration:** 4.7 minutes
**Test Coverage:** Comprehensive playback and audio tests

## Development Status

**v1.1 Shipped** (Feb 9, 2026) - Adaptive audio features complete

**v1.2 Active:** Hardware validation and adaptive masking algorithm (Phase 15/17)

**Roadmap:**
- Phase 15: Hardware battery validation ✅ (1/4 plans)
- Phase 16: Adaptive masking algorithm (planned)
- Phase 17: TestFlight distribution (planned)

**Future Vision:**
- FlowState macOS companion app
- Genetic audio DNA (parameters evolve with success metrics)
- Task-linked audio (only plays during active work)
- Pomodoro integration

## Technical Insights

### Audio Synthesis

**Brown Noise Filter:**
```swift
// One-pole IIR lowpass: y[n] = x[n] + α * y[n-1]
let alpha: Float = 0.96
let brown = white + alpha * previousBrown
```

**Binaural Beat Generation:**
```swift
// Left: carrier - (beat/2), Right: carrier + (beat/2)
let leftFreq = carrierFreq - (beatFreq / 2)
let rightFreq = carrierFreq + (beatFreq / 2)
```

### Wrapper Composition Pattern

Effects stack without modifying base generators:

```
AdaptiveMaskingGenerator(
  HeartbeatGenerator(
    FrequencyBiasGenerator(
      WhiteNoiseGenerator()
    )
  )
)
```

Allows hot-swap and independent feature toggling.

## Privacy & Security

**No Data Collection:**
- Runs entirely on Apple Watch
- No cloud services
- No analytics or tracking

**Microphone Usage:**
- Periodic RMS analysis only (no recording)
- Used for adaptive masking
- Completely local processing
- Optional feature with user control

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **Related:** Soundscape agent in [Multi-Agent Assistant](multi-agent) inspired by this project

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Main play/pause interface
- Settings screen with noise type selector
- Binaural beats configuration
- Frequency calibration flow (10-step sweep)
- Heartbeat sync settings
- Adaptive masking toggles
- Digital Crown volume control
- Bluetooth routing verification
- Battery usage stats
- About screen
-->
