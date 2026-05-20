---
layout: default
section: network-automation
description: "A Rust library and CLI for network device interaction and automated testing."
---

# Device Interaction Framework

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Architecture](#architecture)

## Concept

A Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities — testbed management, CLI output parsing, and state verification — without the complexity. Connects to devices (real, simulated, or mocked), executes commands, parses structured output, and verifies correctness with the type safety of compiled Rust.

---

## Code Samples

### connectivity-check.yaml

```yaml
# Example Verification Suite
# Demonstrates common network state checks.

name: "Connectivity Audit"
tests:
  # Check if the uplink interface is up on the spine
  - device: "spine-1"
    check: "interface_up"
    interface: "GigabitEthernet0/1"
    within: "30s"

  # Check for a critical route
  - device: "spine-1"
    check: "route_exists"
    destination: "10.0.0.0/8"

  # Verify connectivity to an external target
  - device: "spine-1"
    check: "ping"
    target: "8.8.8.8"
    threshold: 0.0

```

### lab-testbed.yaml

```yaml
# Example Testbed for Device Interaction Framework
# This testbed demonstrates a mix of Mock and real SSH devices.
# For pilot environments, replace the inline password below with
# `${DI_STORE:example-lab.default.password}` after running:
# `di credentials set example-lab.default --username admin --password-file ~/.secrets/example-lab-password`

testbed:
  name: example-lab
  credentials:
    default:
      username: admin
      password: admin_password

devices:
  # A core spine router using Mock backend for development
  spine-1:
    type: router
    os: cisco_ios
    role: spine
    tags: [core, datacenter-1]
    connections:
      mock:
        protocol: mock
        ip: 127.0.0.1

  # A leaf switch using SSH for production
  leaf-1:
    type: switch
    os: cisco_ios
    role: leaf
    tags: [access, rack-1]
    connections:
      ssh:
        protocol: ssh
        ip: 10.1.1.10
        port: 22

  # Another leaf switch
  leaf-2:
    type: switch
    os: cisco_ios
    role: leaf
    tags: [access, rack-2]
    connections:
      ssh:
        protocol: ssh
        ip: 10.1.1.11
        port: 22

```

---

## Usage

```bash
# Connect to a device interactively
di-cli connect spine-1 --testbed lab.yaml

# Execute a command
di-cli exec spine-1 "show ip route" --testbed lab.yaml

# Run a verification suite
di-cli verify connectivity-check.yaml --testbed lab.yaml
```

---

## Architecture

<div class="mermaid">
flowchart TD
    DB[DeviceBackend trait]
    DB --> MOCK["Mock<br/><small>Fast parser development</small>"]
    DB --> SIM["Simulator<br/><small>Dynamic protocol testing</small>"]
    DB --> SSH["Real SSH<br/><small>Production validation</small>"]
    style MOCK fill:#e8f5e9
    style SIM fill:#fff3e0
    style SSH fill:#fce4ec
</div>

**Three-tier testing strategy**: mock fixtures for fast parser development, [Network Simulator](/projects/netsim) integration for dynamic testing, real SSH for production validation. All three use the same `DeviceBackend` trait, so parsers and verification logic work identically across tiers.

- **Testbed loader**: YAML device inventory with connection parameters and role/tag metadata
- **Backend abstraction**: pluggable `DeviceBackend` trait (Mock, SSH via russh, Network Simulator)
- **Parser framework**: `nom`-based combinators that parse `show ip route`, `show interfaces`, `ping`, and `traceroute` into typed Rust structs
- **Connection pool**: per-device SSH session caching with single-flight execution

~7,000 lines of Rust across 5 crates. 131 tests passing.

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust |

---

## What This Is

A fast, simple, and ergonomic Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities—testbed management, CLI parsing, and state verification—without the complexity, as a focused component in a broader network automation toolkit.

---

## Core Value

Enable rapid, type-safe validation of network device state through streamlined device interaction: connect to devices (real, simulated, or mocked), execute commands, parse structured output, and verify correctness—all with the performance and safety guarantees of Rust.

---

## Current Milestone: v1.1 Complete Testing Stack

**Goal:** Complete the original vision by adding code-first verification framework and user-facing CLI tool, enabling end-to-end device testing workflow.

**Target features:**
- Verification Framework — State assertion API with composable logic and typed results
- CLI Tool — Interactive and one-shot commands (connect, exec, verify)
- Testing & Examples — Example testbeds, E2E tests, verification scripts

---

## Requirements



---

## # Validated

**Core Connectivity (v1.0):**
- ✓ Load testbed definitions from YAML (device inventory, topology, connection parameters) — v1.0
- ✓ Connection abstraction supporting multiple backends (SSH, mock replay, [netsim](../netsim) native) — v1.0
- ✓ SSH connection pooling and lifecycle management — v1.0
- ✓ Command execution with proper error handling and timeouts — v1.0

**Parser Framework (v1.0):**
- ✓ Trait-based parser system for extensibility — v1.0
- ✓ Parse `show ip route` output into typed structs (Route, NextHop, Metric) — v1.0
- ✓ Parse `show interfaces` output into typed structs (Interface, Status, Speed, Duplex) — v1.0
- ✓ Parse ping responses into typed results (packets sent/received, RTT) — v1.0
- ✓ Parse traceroute responses into hop-by-hop path data — v1.0
- ✓ Parser tests using mock fixtures with real vendor outputs — v1.0

**Backend Implementations (v1.0):**
- ✓ Mock SSH backend using pre-recorded command/response fixtures (YAML/JSON) — v1.0
- ✓ SSH backend for real device connections (using russh) — v1.0
- ✓ [netsim](../netsim) backend integration (SSH-based wrapper) — v1.0

**Testing & Examples (v1.0):**
- ✓ Parser fixtures with real Cisco IOS outputs — v1.0 (4 fixture files)

---

## # Active

**Verification Framework:**
- [ ] State assertion API (e.g., assert interface up, assert route exists)
- [ ] Typed verification results with detailed failure messages
- [ ] Composable verification logic (AND/OR conditions)

**CLI Tool:**
- [ ] `di-cli connect` - interactive device connection
- [ ] `di-cli exec` - one-shot command execution
- [ ] `di-cli verify` - run verification suite against testbed

**Testing & Examples:**
- [ ] Example testbed YAML files
- [ ] End-to-end test suite against [netsim](../netsim) daemon
- [ ] Example verification scripts demonstrating library usage

---

## # Out of Scope

- **Dashboard/Web UI** — CLI and library only; visualization is not this tool's concern
- **YAML-based test definitions (Blitz-style)** — Code-first approach with Rust API; config-driven testing adds complexity we're avoiding
- **Orchestration and workflow engine** — Other tools in the broader automation toolkit handle multi-device orchestration
- **Configuration management** — Focus on state verification and command execution, not config generation/deployment
- **Complete PyATS feature parity** — Only testbeds, parsers, and verifications; skip XPRESSO, Genie object models, etc.
- **Day-1 multi-vendor support** — Start with Cisco (IOS/IOS-XE/NX-OS) as reference implementation; extensibility for others comes later

---

## Context

**Current State (v1.0 shipped 2026-02-22):**
- **Codebase:** ~7,000 lines of Rust across 5 crates (di-core, di-testbed, di-parsers, di-models, di-collect)
- **Tech Stack:** Rust 1.70+, tokio async runtime, russh for SSH, nom for parsing, serde for YAML/JSON
- **Test Coverage:** 131 tests passing (di-core: 34, di-parsers: 76, di-testbed: 31, di-models: 8)
- **Deliverables:** Foundation (testbed + backend abstraction), Mock backend (fixtures), SSH integration (pooling), Parser framework (4 parsers + registry)

**Known Technical Debt (from v1.0 audit):**
- di-collect doc test [compilation](../compilation) failure (documentation issue)
- Missing integration test for Backend → Parser combined flow
- Unused imports in parser modules (cleanup opportunity)

**Ecosystem Integration:**
This tool is one component in a broader network automation toolkit. Related projects:
- `[netsim](../netsim)` (~/dev/[network-simulator](../netsim)) — Full-featured network topology simulator with OSPF, IS-IS, BGP, MPLS, daemon mode, interactive CLI
- This tool enables testing automation against [netsim](../netsim) before deploying to real hardware

**Development Workflow:**
1. Develop parsers using mock fixtures (real vendor outputs) ✓
2. Test against [netsim](../netsim) daemon (dynamic simulation) — partial (backend exists, integration tests pending)
3. Validate against real devices (production hardware) — ready (SSH backend complete)

**Inspiration:**
PyATS/Genie provides excellent network automation capabilities but is heavyweight and Python-based. This tool extracts the essential testing loop (define topology → connect → parse → verify) with:
- Better performance (Rust vs Python) ✓
- Stronger type safety (compile-time validation) ✓
- Simpler deployment (single binary vs Python runtime) — in progress
- Streamlined API (focused feature set vs kitchen sink) ✓

---

## Constraints

- **Tech Stack: Rust** — Rust 1.70+ with tokio async runtime; this is non-negotiable for performance and safety goals
- **Testing Infrastructure: [netsim](../netsim) required** — Must integrate with existing [netsim](../netsim) project for simulation-based testing
- **Protocol Support: SSH primary** — SSH is the universal device protocol; Telnet and REST APIs are lower priority
- **Parser Accuracy: Real vendor outputs** — All parsers must be tested against actual device outputs, not synthetic examples
- **Performance: Zero-cost abstractions** — Backend abstraction must compile to efficient code; no runtime overhead for trait dispatch in hot paths
- **Deployment: Single binary** — CLI tool must be a standalone executable with no runtime dependencies

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Three-tier testing strategy (mock → [netsim](../netsim) → real) | Enables fast parser development (mock fixtures), dynamic testing ([netsim](../netsim)), and production validation (real hardware) without blocking on device availability | ✓ Good — MockBackend enables testing without hardware, SSH backend ready for real devices |
| Trait-based backend abstraction (`DeviceBackend` trait) | Allows pluggable connection mechanisms (SSH, mock, [netsim](../netsim) native) while maintaining type safety and enabling compile-time optimization | ✓ Good — 3 backend implementations (Mock, SSH, Netsim), zero overhead trait dispatch |
| Start with core commands (route, interfaces, ping, traceroute) | Proves the full stack (connect → parse → verify) works before expanding to 15+ commands; faster path to validation against [netsim](../netsim) | ✓ Good — All 4 parsers working with real IOS fixtures, full stack validated |
| Code-first verification API (not YAML tests) | Rust API provides type safety, IDE support, and composability; YAML adds parsing complexity and loses compile-time checks | — Pending — Verification framework is Phase 5 |
| Cisco as reference implementation | Most mature [netsim](../netsim) support; well-documented CLI; establishes parser patterns before expanding to multi-vendor | ✓ Good — Cisco IOS parser patterns established, extensible to other vendors |
| Use russh over thrussh | russh is actively maintained fork with better async support and security updates | ✓ Good — SSH backend works reliably, prompt-delimited execution successful |
| Parser registry with trait objects | Enables dynamic parser lookup by command name while maintaining type safety through downcasting | ✓ Good — Registry integration tests pass, type-safe API validated |
| nom for parsing with nom_locate | Provides composable parser combinators with line/column error reporting | ✓ Good — Reusable primitives (ip, interface, protocol), actionable error messages |
| ConnectionPool per-device caching | Reuse SSH sessions to avoid reconnection overhead | ✓ Good — Pool unit tests prove session reuse, single-flight execution prevents race conditions |

*Last updated: 2026-02-22 after v1.1 milestone start*
