---
layout: default
---

# Photo Tour

<span class="status-badge status-planning">Planning</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Planning phase |
| **Language** | Swift (SwiftUI) + Rust |
| **Platform** | iOS / iPadOS |
| **Edge AI** | Nvidia Jetson / RPi AI Kit (optional) |
| **Started** | 2026 |
| **License** | TBD |

---

## Overview

Photo Tour is a smart, interactive photography assistant for field use. Native iOS/iPadOS app that focuses on classical composition, AI-assisted wildlife triggering, and automated "Holy Grail" day-to-night transitions. Leverages [OpenAstro Core](open-astro-core) for camera control and mount coordination.

## Problem It Solves

Field photography requires balancing technical control with creative focus:

**Composition Challenges:**
- Difficult to visualize classical rules in viewfinder
- Rule of thirds is basic, misses advanced techniques
- No real-time feedback on composition quality
- Learning curve for Fibonacci spiral, golden triangles

**Wildlife Photography:**
- Constant shutter monitoring (tedious, tiring)
- Miss brief moments while adjusting settings
- Difficult to predict animal behavior
- High shot count with low keeper rate

**Timelapse Complexity:**
- Manual exposure ramping for day-to-night transitions
- Bulb ramping requires constant attention
- "Holy Grail" technique is time-consuming to learn
- Difficult to get smooth exposure transitions

**Focus Stacking:**
- Manual focus adjustments between shots
- Alignment issues from camera movement
- Time-consuming workflow
- Difficult in field conditions

**Photo Tour provides:**
- Interactive 8-point composition suite
- AI-assisted wildlife and lightning triggering
- Automated Holy Grail exposure ramping
- Focus stacking and giga-pan workflows
- Native iOS/iPad experience with optional edge AI

## Architecture

### Native iOS App (SwiftUI)

**Primary Interface:**
- Real-time composition overlays
- Camera control and settings
- Triggering configuration
- Gallery and review

**Integration:**
- [OpenAstro Core](open-astro-core) for camera control via Swift FFI
- Sony Camera Remote SDK for LiveView
- Benro Polaris protocol for gimbal control
- Local CoreML for on-device AI

### Edge AI Sentinel (Optional)

**Jetson Nano / RPi AI Kit module:**
- Offload AI processing from phone/iPad
- Wildlife detection models
- Lightning detection
- Scene change analysis
- Communicates with iOS app via WiFi

**Benefits:**
- Preserve phone battery
- More powerful AI models
- Continuous monitoring
- Hot-swappable processing

## Key Features

### Classical Composition Engine

Interactive 8-point suite with real-time overlays:

**Composition Rules:**
1. **Rule of Thirds** - Basic grid overlay
2. **Golden Ratio** - 1.618 grid for natural balance
3. **Fibonacci Spiral** - Natural flow and eye movement
4. **Golden Triangle** - Diagonal compositions
5. **Diagonal Method** - Dynamic energy
6. **Golden Grid** - Refined thirds
7. **Harmonic Armature** - Complex balance
8. **Dynamic Symmetry** - Baroque diagonal

**Interactive Mode:**
- Tap through rules quickly
- Opacity adjustment for overlays
- Live subject framing suggestions
- Composition scoring (optional feedback)

### Smart Triggering: Scene Delta

AI-assisted triggering for unpredictable subjects:

**Wildlife Detection:**
- Animal entry into frame
- Movement toward camera
- Behavior changes (feeding, calling)
- Subject prominence scoring

**Lightning Detection:**
- Flash detection in frame
- Brightness threshold tuning
- Rapid multi-shot capture
- Pre-lightning buffer (video analysis)

**Scene Change:**
- General motion detection
- Configurable sensitivity
- Region-of-interest focus
- False positive filtering

**Trigger Modes:**
- Immediate (zero-lag when possible)
- Burst (rapid sequence)
- Delayed (allow subject to settle)
- Interval (time-based with AI confirmation)

### Holy Grail Transitions

Automated day-to-night exposure ramping:

**Challenge:**
Manual bulb ramping requires constant adjustment as light fades. "Holy Grail" technique produces smooth timelapse transitions but is tedious.

**Solution:**
- Automatic exposure adjustment based on histogram
- Smooth ramping algorithm (no flicker)
- Preview and simulation mode
- Pre-configured profiles (sunset, sunrise, eclipse)

**Workflow:**
1. Set start and end times
2. Choose ramping profile
3. App adjusts ISO, shutter, aperture automatically
4. Smooth histogram-based corrections
5. Export-ready sequence

### Focus Stacking & Giga-Pan

Automated landscape and macro workflows:

**Focus Stacking:**
- Calculate focus steps from near to far
- Automated focus rail control (if available)
- Or software-based focus adjustments via camera
- Maintains exact framing between shots
- Export stack for post-processing

**Giga-Pan:**
- Grid-based panorama capture
- Benro Polaris gimbal coordination
- Row-by-row or spiral patterns
- Overlap calculation for stitching
- High-resolution landscape imaging

## Use Cases

**Wildlife Photography:**
Setup camera on tripod with Photo Tour monitoring. AI detects animal entry into frame and triggers camera. Photographer reviews shots and adjusts composition overlays for better framing.

**Landscape Timelapses:**
Holy Grail workflow captures sunset to night sky transition. Automated exposure ramping produces smooth video. No manual intervention required during golden hour.

**Macro Focus Stacking:**
Focus stacking mode captures flower at multiple focus distances. App coordinates camera focus adjustments. Export to Photoshop/Helicon for final stack.

**Lightning Photography:**
Scene Delta detects lightning flashes and triggers camera with minimal lag. Captures bolt without constant shutter monitoring.

**Composition Learning:**
Interactive composition engine teaches classical rules. Real-time overlays show how to improve framing. Scoring feedback helps develop compositional eye.

## Technical Details

### Platform: iOS/iPadOS

**Why iOS:**
- Excellent camera already in pocket
- High-quality displays for composition
- CoreML for on-device AI
- Swift/SwiftUI for native performance

**Requirements:**
- iOS 17+
- iPhone 12 or later (for ProRAW and computational photography)
- iPad Pro recommended for field use

### Camera Integration

**Supported Cameras:**
- Sony (via Camera Remote SDK + OpenAstro Core)
- Benro Polaris gimbal control
- Future: Canon, Nikon, Fuji via OpenAstro Core extensions

**Control:**
- LiveView streaming
- Exposure settings (ISO, shutter, aperture)
- Focus control
- Trigger shutter
- Image download

### AI Models

**On-Device (CoreML):**
- Wildlife detection (YOLO-based)
- Composition scoring
- Scene classification
- Fast inference (<100ms)

**Edge AI Sentinel (Optional):**
- More powerful models (ResNet, EfficientNet)
- Continuous monitoring
- Lower power on iOS device
- Communicates results over WiFi

### Composition Algorithms

**Golden Ratio Calculation:**
```
φ = 1.618033988749895
Grid points at φ/(1+φ) and 1/(1+φ)
```

**Fibonacci Spiral:**
- Clockwise and counter-clockwise variants
- Origin selectable (4 corners)
- Logarithmic spiral equation

## Development Status

**Planning Phase:**
- Architecture design in progress
- OpenAstro Core integration strategy defined
- Composition engine algorithms researched

**Next Steps:**
- Implement composition overlay engine
- Sony SDK integration via OpenAstro Core
- Scene Delta AI model training
- Holy Grail ramping algorithm

**Future Expansion:**
- Edge AI Sentinel module
- Benro Polaris protocol integration
- Additional camera brand support
- Cloud sync for settings and profiles

## Comparison

| Feature | Photo Tour | Built-in Camera | DSLR Controller Apps |
|---------|------------|-----------------|----------------------|
| Composition | 8-point suite | Rule of thirds | Basic grids |
| AI Triggering | Wildlife/lightning | No | No |
| Holy Grail | Automated | No | Manual |
| Focus Stack | Automated | No | Limited |
| Edge AI | Optional module | No | No |
| Platform | iOS/iPad native | iOS only | Various |

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **Related:** [OpenAstro Core](open-astro-core) provides camera control

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Composition overlay examples (all 8 rules)
- Wildlife detection in action
- Holy Grail ramping interface
- Focus stacking workflow
- Scene Delta configuration
- LiveView with composition scoring
- Edge AI Sentinel setup
- Giga-pan grid planning
-->
