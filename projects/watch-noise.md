---
layout: default
section: projects
---

# Wave (StillState & FlowState)

<span class="status-badge status-active">Last Active: 2026-02-21</span>

[← Back to Projects](../projects)

---

## Contents

- [What This Is](#what-this-is)
- [Core Value](#core-value)
- [Current State (v1.1 Shipped 2026-02-09)](#current-state-v11-shipped-2026-02-09)
- [Requirements](#requirements)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Technical Debt](#technical-debt)
- [Current Status](#current-status)

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-02-21 |

---

## What This Is

**Wave** is an evolutionary ambient audio ecosystem designed to manage the user's sensory environment across rest and work.

1. **StillState (Watch):** An adaptive sleep sounds app for Apple Watch with personalized frequency calibration, heartbeat synchronization, and microphone-based environmental monitoring.
2. **FlowState (Mac):** A productivity-focused menu bar app that links procedural audio to the user's active tasks and "Genetic System" TODO list (planned).

---

## Core Value

- **StillState:** Reclaiming silence and rest in shared or noisy environments through intelligent, adaptive audio.
- **FlowState:** Achieving and maintaining a "Steady State" of focus through task-linked audio and genetic evolution.

---

## Current State (v1.1 Shipped 2026-02-09)

**Latest release:** v1.1 Adaptive Audio Features

**What's built:**
- Procedural audio engine (white, brown, blended noise) with live hot-swap
- Binaural beats system (5 presets + custom parameters + noise bed mixing)
- Interactive frequency calibration (10-step sweep 20 Hz - 8 kHz, personalized +4dB bias)
- Heartbeat synchronization (4 BPM presets 50-65 BPM, 5- amplitude modulation)
- Microphone monitoring infrastructure (vDSP RMS-to-dB analysis, periodic 0.5s sampling)
- Smart battery preservation (all features toggleable, defaults OFF, screen-off/disconnect auto-disable)
- Bluetooth-only routing with auto-pause and stereo validation
- Background audio with overnight reliability (< base drain, < all features)

**Next milestone goals (v1.2):**
- Full adaptive masking algorithm (dynamic volume/frequency adjustment based on environmental noise)
- Tech debt resolution (CalibrationEngine timestamp, orphaned singleton, Settings reorg)
- Hardware battery validation (overnight testing, confirm < drain targets)
- Adaptive feature tuning (calibration bias perception, heartbeat effectiveness, mic accuracy)

---

## Requirements



---

## # Validated

<details>
<summary>v1.0 MVP (Shipped 2026-02-08)</summary>

- ✓ **Generate white, brown, and blended noise** — Procedural synthesis with live hot-swap — v1.0
- ✓ **Binaural beats mode** — 5 presets + custom parameters + noise bed compositing — v1.0
- ✓ **Bluetooth-only audio routing** — .longFormAudio policy, auto-pause on disconnect — v1.0
- ✓ **Play/pause controls** — SF Symbols UI with state-based icons and haptics — v1.0
- ✓ **Settings persistence** — Noise type, beats configuration, auto-resume strategy — v1.0
- ✓ **Background audio** — Indefinite playback with screen off, < battery drain/hour — v1.0

</details>

<details>
<summary>v1.1 Adaptive Audio Features (Shipped 2026-02-09)</summary>

**Ear-Print Calibration:**
- ✓ **CALIB-01**: User can access calibration flow from Settings — v1.1
- ✓ **CALIB-02**: Calibration runs 20 Hz - 8 kHz sweep — v1.1
- ✓ **CALIB-03**: User can rate relaxation level — v1.1
- ✓ **CALIB-04**: Calibration identifies preferred frequency — v1.1
- ⚠️ **CALIB-05**: Calibration results persist in @AppStorage — v1.1 (partial: preference saved, timestamp missing)
- ✓ **CALIB-06**: App uses sensible defaults if skipped — v1.1
- ⚠️ **CALIB-07**: Calibration can be re-run — v1.1 (partial: NavigationLink exists, timestamp won't update)
- ✓ **CALIB-08**: Calibration UI provides clear instructions — v1.1

**Heartbeat Sync:**
- ✓ **HEART-01 to HEART-09**: All heartbeat requirements fully satisfied — v1.1

**Adaptive Noise Masking (Infrastructure):**
- ✓ **MASK-01 to MASK-10**: All adaptive masking infrastructure requirements fully satisfied — v1.1

**Integration & Performance:**
- ✓ **INTG-01 to INTG-05**: All integration requirements fully satisfied — v1.1
- ✓ **PERF-01 to PERF-03**: All performance requirements fully satisfied — v1.1

**UI & UX:**
- ✓ **UI-06, UI-07, UI-09, UI-10**: All delivered UI requirements fully satisfied — v1.1

**Total v1.1:** 35 requirements fully satisfied, 2 partial, 10 skipped 

</details>

---

## # Active (v1.2 Polish & Validation)

**Milestone goal:** Complete adaptive masking algorithm, resolve tech debt, validate on hardware, and prepare TestFlight distribution for internal testing.

**Target deliverables:**
- [ ] Full adaptive masking algorithm (dynamic volume/frequency adjustment based on mic analysis)
- [ ] Tech debt resolution (CalibrationEngine timestamp, orphaned singleton, Settings reorg)
- [ ] Hardware battery validation (overnight testing, confirm < drain targets)
- [ ] Adaptive feature tuning (calibration bias perception, heartbeat effectiveness, mic accuracy)
- [ ] TestFlight distribution setup (internal testing infrastructure, no public App Store)

**Deferred from v1.1:**
- Environment synthesis generators ("Muffled Voices", "Distant Traffic") — moved to future backlog

---

## # Future: FlowState (macOS)

- [ ] **Genetic System Hook**: Consumes active task data from external JSON/API
- [ ] **Genetic Audio DNA**: Audio parameters evolve based on session success/interruption metrics
- [ ] **Flow-Locking**: Audio only plays when an active task is pulled from the genetic system
- [ ] **State ROI**: Reporting "Focus Quality" metrics back to the Genetic System
- [ ] **Pomodoro Sync**: Integrated 25/5 timer with automated Focus/Nature audio transitions

---

## Context

**Primary use case:**
- **StillState:** Sleeping on retreats or in shared dorms. User needs to block human-centric noises (snoring) while respecting "noble silence" (no light/no watch speaker). Now with personalized frequency bias and optional heartbeat grounding.
- **FlowState:** Deep work sessions at a desk. Noise serves as a "Flow State" trigger linked directly to productivity metrics and task DNA.

**Shipped versions:**
- v1.0: Base audio engine with noise synthesis and binaural beats (2026-02-08)
- v1.1: Adaptive features (calibration, heartbeat, microphone monitoring) (2026-02-09)

---

## Constraints

- **Tech stack**: SwiftUI and modern watchOS/macOS
- **StillState Audio**: Bluetooth headphones only (no Watch speaker support)
- **FlowState Audio**: Flexible output, optimized for focus
- **Battery**: StillState must support 6-8 hours continuous playback

---

## Key Decisions

| Decision | Rationale | Outcome | Status |
|----------|-----------|---------|--------|
| Wrapper composition pattern | Allows stacking effects (bias → heartbeat) without modifying base generators | Validated in v1.1, enabled hot-swap support | ✓ Good |
| Conservative modulation depths | Calibration +4dB, heartbeat 5- to avoid startling/distracting users during sleep | User feedback pending, no complaints in testing | — Pending |
| Periodic analysis (0.5s timer) | Saves ~5- battery vs continuous microphone processing | Validated in code, actual battery impact deferred to usage testing | — Pending |
| Dedicated input AVAudioEngine | Prevents feedback loops between mic monitoring and audio playback | No feedback issues encountered | ✓ Good |
| Battery-first philosophy | All v1.1 features default OFF with individual toggles | Aligns with overnight use case, user has full control | ✓ Good |
| Skip .1 release | Milestone delivered on time, environment moved to backlog | ✓ Good |
| Binaural carrier purity | Wrapper effects apply to noise bed only, not beats carrier | Preserves accurate brainwave entrainment frequency | ✓ Good |

---

## Technical Debt

From v1.1 milestone audit:

1. **CalibrationEngine timestamp tracking** (Low severity)
   - saveResults() doesn't call markCompleted(), timestamp not saved
   - Impact: User can't see "last calibrated" date
   - Fix: Call CalibrationStorage.shared.markCompleted(preferredFrequency, hasPreference)

2. **AdaptiveMaskingSettings singleton orphaned** (Info severity)
   - Singleton defined but not used (direct @AppStorage instead)
   - Impact: ~20 lines of unused code
   - Fix: Remove singleton or refactor to use it consistently

3. **Settings section order** (Info severity)
   - Background Audio/Display sections interleaved vs spec
   - Impact: None - all sections functional
   - Fix: Consolidate Display into Advanced, move Background Audio

4. **Battery overhead estimates** (Deferred validation)
   - Calibration <, Heartbeat <, Adaptive ~ (research-based)
   - Fix: Validate during extended usage sessions


*Last updated: 2026-02-09 after v1.2 milestone planning*

---

## Current Status

2026-02-21 — Completed 26-01 FlowState Hotkeys + Quick Actions

---

[← Back to Projects](../projects)
