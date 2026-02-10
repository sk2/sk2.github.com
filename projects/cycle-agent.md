---
layout: default
---

# Cycle Agent

<span class="status-badge status-planning">Planning Phase</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Planning phase |
| **Language** | Swift (SwiftUI) |
| **Stack** | SwiftUI · SceneKit · FTMS (BLE) · NATS |
| **Platforms** | iPadOS · tvOS (Apple TV) |
| **Hardware** | Wahoo KICKR Core · Apple Watch |
| **Started** | 2025 |
| **License** | TBD |

---

## Overview

Cycle Agent is a native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (Wahoo KICKR Core smart trainer) with dynamic AI-driven workout logic via NATS message broker. Features high-performance infinite terrain visualization in SceneKit with 60fps smooth rendering.

## Problem It Solves

Indoor cycling training software has limitations:

**Existing Training Apps (Zwift, TrainerRoad):**
- Subscription services ($15-20/month)
- Fixed workout plans
- No custom AI-driven logic
- Limited extensibility
- Cloud-dependent operation

**DIY Training Apps:**
- Complex Bluetooth FTMS implementation
- No AI integration
- Limited visualization
- Platform-specific code

**Cycle Agent provides:**
- Native SwiftUI for iPad and Apple TV
- Direct KICKR Core control via Bluetooth FTMS
- AI-driven workout adaptation through NATS Agent Bridge
- Infinite terrain visualization with SceneKit
- Real-time heart rate from Apple Watch
- Offline-capable with optional cloud intelligence

## Architecture

### SwiftUI Native Interface

Modern declarative UI for iOS/tvOS:

**iPad Interface:**
- Real-time telemetry dashboard
- Workout controls and metrics
- Terrain visualization
- Heart rate monitoring

**Apple TV Interface:**
- Full-screen immersive terrain
- Simplified controls (Siri Remote)
- Large-format metrics display
- Optimized for 10-foot viewing

### Bluetooth FTMS Control

Direct communication with KICKR Core:

**Fitness Machine Service (FTMS):**
- Standard Bluetooth LE profile for fitness equipment
- Power, cadence, speed telemetry
- Resistance control (0-100% or wattage target)
- Real-time data streaming

**Control Modes:**
- **Target Power:** Set wattage goal, trainer adjusts resistance
- **Slope Simulation:** Mimic grade percentage (terrain)
- **Manual Resistance:** Direct resistance percentage

### NATS Agent Bridge

Message broker connects to AI agent framework:

**Telemetry Publishing:**
```swift
// Publish real-time cycling metrics
nats.publish(subject: "cycling.telemetry", data: {
    power: 250,
    cadence: 90,
    speed: 35.2,
    heart_rate: 155,
    timestamp: Date()
})
```

**Command Subscription:**
```swift
// Receive workout adjustments from agent
nats.subscribe(subject: "cycling.commands") { message in
    if message.type == "set_power" {
        kickr.setTargetPower(watts: message.target)
    }
}
```

**Agent Integration:**
AI agent analyzes telemetry and sends dynamic workout adjustments:
- Increase/decrease target power
- Change terrain simulation
- Interval timing adjustments
- Recovery period triggers

### SceneKit Terrain Visualization

High-performance 3D infinite terrain:

**Rendering:**
- 60 FPS on Apple TV and iPad
- Procedural terrain generation
- Level-of-detail (LOD) optimization
- Metal-backed rendering

**Features:**
- Infinite scrolling terrain
- Dynamic elevation based on workout
- Speed-synchronized movement
- Environmental effects (lighting, shadows)

## Features

### Planned Core Features

**Hardware Integration:**
- Bluetooth LE FTMS connection to KICKR Core
- Low-latency power/cadence/speed telemetry (<100ms)
- Target power or slope control
- Automatic reconnection handling

**Apple Watch Integration:**
- Real-time heart rate streaming
- HealthKit workout integration
- Workout recording and history

**AI-Driven Workouts:**
- NATS connection to agent framework
- Real-time telemetry publishing
- Dynamic workout adjustments
- Intelligent interval timing
- Fatigue-based adaptation

**Visualization:**
- SceneKit infinite terrain
- Speed-synchronized scrolling
- Dynamic elevation changes
- 60fps smooth rendering
- Apple TV optimized display

**Workout Recording:**
- FIT file export
- HealthKit integration
- Historical data tracking
- Performance analytics

### iOS/tvOS Lifecycle Handling

**Background Modes:**
- Maintain Bluetooth connection when backgrounded
- Continue NATS message flow
- Preserve workout state

**Interruption Handling:**
- Phone calls on iPad
- tvOS sleep mode
- Graceful pause and resume
- State restoration

## Use Cases

**AI-Coached Intervals:**
Agent analyzes power and heart rate trends. Dynamically adjusts interval intensity and duration based on real-time fatigue indicators.

**Terrain Simulation:**
Agent coordinates with mapping data to simulate real-world routes. KICKR resistance matches elevation changes. SceneKit renders matching terrain.

**Recovery Rides:**
Agent monitors heart rate variability and power output. Keeps workout in Zone 2 by adjusting target power. Prevents overtraining.

**Structured Workouts:**
Agent orchestrates complex interval sequences. Ramp tests, VO2 max intervals, threshold work. Real-time adjustments based on performance.

## Technical Details

### Bluetooth FTMS Implementation

**Services Used:**
- Fitness Machine Service (UUID: 0x1826)
- Indoor Bike Data characteristic (0x2AD2)
- Fitness Machine Control Point (0x2AD9)
- Fitness Machine Status (0x2ADA)

**Data Parsing:**
- Binary protocol per Bluetooth spec
- Power (watts), cadence (rpm), speed (km/h)
- Status flags (paused, stopped, targeting)

### NATS Integration

**Swift NATS Client:**
- Pure Swift implementation
- TLS 1.3 support for security
- Async/await for modern concurrency
- Lifecycle management for iOS/tvOS

**Subject Hierarchy:**
```
cycling.telemetry           # Real-time metrics
cycling.commands            # Agent control messages
cycling.workouts.{id}       # Workout-specific channel
cycling.status              # Connection/state updates
```

### SceneKit Performance

**Optimization Strategies:**
- LOD terrain meshes (high detail near rider, low detail distant)
- Frustum culling (only render visible terrain)
- Procedural generation (GPU-based noise)
- Texture atlasing for reduced draw calls

**Target Performance:**
- 60 FPS on Apple TV 4K
- 60 FPS on iPad Pro
- <50ms input latency
- <100ms Bluetooth latency

## Development Status

**Planning Phase:**
- Architecture design complete
- Technology stack selected
- Integration patterns defined

**Next Steps:**
- Implement FTMS Bluetooth client
- NATS Swift client integration
- Basic SwiftUI interface
- SceneKit terrain prototype
- Apple Watch heart rate streaming

**Constraints:**
- Must be native Swift/SwiftUI
- Support tvOS and iPadOS
- Follow FTMS standards
- Handle iOS/tvOS lifecycle correctly

## Hardware Requirements

**Essential:**
- Wahoo KICKR Core smart trainer
- iPad (iOS 17+) or Apple TV 4K (tvOS 17+)
- Apple Watch (for heart rate)

**Optional:**
- ANT+ sensors (cadence, power)
- External heart rate monitors
- Second display (iPad + Apple TV)

## Integration

**Multi-Agent Framework:**
Cycle Agent publishes telemetry to NATS. AI agent in containerized framework analyzes data and sends workout commands. Orchestrator coordinates with other agents (health monitoring, calendar).

**Apple Health:**
Workout data syncs to HealthKit. Integrates with Health Agent for holistic health tracking.

## Comparison

| Feature | Cycle Agent | Zwift | TrainerRoad | Wahoo SYSTM |
|---------|------------|-------|-------------|-------------|
| Platform | iPad/Apple TV | Multi-platform | Multi-platform | Multi-platform |
| Cost | Free (+ cloud agent optional) | $15/mo | $20/mo | $15/mo |
| AI Coaching | Custom agent-driven | Fixed plans | Fixed plans | Fixed plans |
| Offline | Yes | No | Limited | Limited |
| Extensibility | Agent framework | No | No | No |
| Visualization | SceneKit terrain | 3D world | 2D graphs | Video |
| Smart Trainer | KICKR Core | Many | Many | Many |

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **Related:** [Multi-Agent Assistant](multi-agent) provides agent framework

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- iPad interface with telemetry dashboard
- Apple TV full-screen terrain view
- SceneKit infinite terrain rendering
- Bluetooth FTMS connection flow
- NATS message structure examples
- Heart rate integration from Apple Watch
- Workout recording FIT file
- Agent-driven interval adjustment
- iOS lifecycle state handling
- Target power control UI
-->
