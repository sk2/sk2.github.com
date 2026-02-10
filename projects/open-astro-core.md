---
layout: default
---

# OpenAstro Core

<span class="status-badge status-planning">Planning</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Planning/Early Development |
| **Language** | Rust |
| **Type** | Library |
| **Ecosystem** | OpenAstro |
| **Started** | 2026 |
| **License** | TBD |

---

## Overview

OpenAstro Core is a high-performance Rust library providing shared astronomical logic, hardware drivers, and protocol implementations for the OpenAstro ecosystem. It serves as the foundation for both OpenAstro Node (astrophotography controller) and Photo Tour (iOS photography assistant).

## Problem It Solves

Building multiple astronomy applications requires duplicating hardware control logic:

**Code Duplication:**
- Astronomical calculations (RA, Dec, angles) repeated across apps
- INDI protocol clients reimplemented per project
- Hardware drivers written multiple times
- No shared testing or validation

**Inconsistent Behavior:**
- Different coordinate math in different tools
- Protocol implementation variations
- Hardware quirks handled differently
- Difficult to debug cross-platform issues

**Performance Concerns:**
- Python overhead for time-critical operations
- Slow coordinate transformations
- Inefficient hardware communication

**OpenAstro Core provides:**
- Single source of truth for astronomical logic
- Shared hardware drivers across ecosystem
- High-performance Rust implementation
- Consistent behavior across all OpenAstro tools

## Architecture

### Workspace Structure

**astro-core**: Shared astronomical types and utilities
- Coordinate types (RA, Dec, Altitude, Azimuth)
- Angle calculations and transformations
- Time utilities (sidereal time, Julian dates)
- Common astronomical algorithms

**astro-indi**: INDI protocol client
- Device discovery and connection
- Property subscription and control
- BLOB (Binary Large Object) transfer for images
- Device abstraction layer

**astro-alpaca**: ASCOM Alpaca REST client
- Modern HTTP/REST protocol for astronomy hardware
- Cross-platform device support
- JSON-based communication
- Future support for Windows-originated devices

**sony-sdk-rs** (Planned): Sony Camera Remote SDK bindings
- Rust wrapper for Sony's camera control SDK
- LiveView streaming
- Focus control and shutter release
- Settings management

**polaris-proto** (Planned): Benro Polaris protocol
- Native implementation of Benro gimbal protocol
- Pan/tilt control for wildlife tracking
- Integration with Photo Tour AI triggering

## Components

### Astronomical Core

**Coordinate Types:**
```rust
pub struct RightAscension {
    hours: f64,  // 0-24
}

pub struct Declination {
    degrees: f64,  // -90 to +90
}

pub struct Angle {
    degrees: f64,
}
```

**Transformations:**
- Equatorial to horizon coordinates
- Altitude/azimuth calculations
- Field rotation computations
- Precession corrections

### INDI Protocol Client

**Device Abstraction:**
- Camera interface (exposure, gain, cooling)
- Mount interface (slewing, tracking, parking)
- Focuser interface (position control)
- Filter wheel interface
- Generic device properties

**Communication:**
- XML-based protocol over TCP
- Asynchronous property updates
- BLOB streaming for images
- Connection pooling

### ASCOM Alpaca Client

**REST API Integration:**
- HTTP/JSON protocol
- Device discovery via Alpaca API
- Cross-platform compatibility
- Modern alternative to INDI for newer hardware

## Features

### Planned Core Features

**Type-Safe Astronomy:**
- Strong types for coordinates (prevent unit errors)
- Validated angle ranges
- Safe arithmetic operations
- Compile-time correctness

**Hardware Abstraction:**
- Unified interface for INDI and Alpaca devices
- Automatic protocol selection
- Device capability detection
- Graceful fallbacks

**Performance:**
- Zero-copy data transfer where possible
- Efficient coordinate transformations
- Minimal allocation in hot paths
- Async I/O for hardware communication

**Error Handling:**
- Typed error hierarchy
- Connection recovery
- Timeout handling
- Detailed error context

## Use Cases

**OpenAstro Node Integration:**
Core library powers the headless astrophotography controller. Provides INDI/Alpaca connectivity, coordinate math for targeting, and hardware abstractions.

**Photo Tour Integration:**
iOS app uses Core library for composition calculations, camera control, and mount coordination. Rust performance with Swift UI.

**Third-Party Applications:**
Other developers can build astronomy tools using Core library. Consistent behavior and tested implementations.

## Technical Details

### Language: Rust

**Why Rust:**
- Performance: Near-C speed for coordinate math
- Safety: Prevents memory errors in critical hardware control
- Async: Efficient handling of multiple device connections
- FFI: Easy bindings for Swift (iOS) and Python

### Cross-Platform

**Supported Platforms:**
- Linux (Raspberry Pi, Jetson, x86_64)
- macOS (development and Photo Tour)
- iOS (Photo Tour via Swift bindings)
- Windows (planned via Alpaca support)

### Dependencies

**Minimal Dependencies:**
- tokio: Async runtime
- serde: Serialization (XML/JSON)
- thiserror: Error handling
- tracing: Logging and diagnostics

## Development Status

**Planning Phase:**
- Architecture design in progress
- Component boundaries defined
- Protocol research complete

**Next Steps:**
- Implement astro-core foundation
- Build INDI protocol client
- Create device abstraction layer
- Add ASCOM Alpaca support

**Integration:**
- OpenAstro Node will migrate to Core library
- Photo Tour will use Core from inception

## Design Goals

### Consistency

Both Node and Photo Tour use identical:
- Coordinate transformations
- Hardware driver logic
- Protocol implementations
- Error handling patterns

### Performance

**Critical Paths:**
- Sub-millisecond coordinate calculations
- Minimal latency for hardware commands
- Efficient image transfer (BLOB streaming)
- Low CPU overhead on embedded devices

### Safety

**Robust Operation:**
- Typed hardware state machines
- Connection failure recovery
- Timeout handling for all operations
- Validated hardware commands

## Future Expansion

**Additional Protocols:**
- ZWO native SDK (camera control)
- QHY camera SDK
- PHD2 guiding protocol
- TheSkyX automation interface

**Hardware Support:**
- Direct USB camera drivers
- Serial mount protocols (LX200, Celestron)
- PWM focus controllers
- Relay-based device control

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **Related:** [OpenAstro Node](open-astro-node) and [Photo Tour](photo-tour) use this library

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add technical diagrams:
- Workspace component structure
- INDI protocol flow
- Alpaca REST API integration
- Coordinate transformation pipeline
- Device abstraction layers
- Error handling hierarchy
-->
