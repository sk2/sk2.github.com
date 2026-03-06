---
layout: default
section: network-automation
---

# Device Interaction Framework

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Testbed Definition](#testbed-definition)
- [Verification](#verification)
- [Usage](#usage)
- [Status](#status)

## Concept

A Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities — testbed management, CLI output parsing, and state verification — without the complexity. Connects to devices (real, simulated, or mocked), executes commands, parses structured output, and verifies correctness with the type safety of compiled Rust.

---

## Architecture

**Three-tier testing strategy**: mock fixtures for fast parser development, Network Simulator integration for dynamic testing, real SSH for production validation. All three use the same `DeviceBackend` trait, so parsers and verification logic work identically across tiers.

- **Testbed loader**: YAML device inventory with connection parameters and role/tag metadata
- **Backend abstraction**: pluggable `DeviceBackend` trait (Mock, SSH via russh, Network Simulator)
- **Parser framework**: `nom`-based combinators that parse `show ip route`, `show interfaces`, `ping`, and `traceroute` into typed Rust structs
- **Connection pool**: per-device SSH session caching with single-flight execution to prevent race conditions

~7,000 lines of Rust across 5 crates. 131 tests passing.

---

## Testbed Definition

```yaml
testbed:
  name: example-lab
  credentials:
    default:
      username: admin
      password: admin_password

devices:
  spine-1:
    type: router
    os: cisco_ios
    role: spine
    tags: [core, datacenter-1]
    connections:
      ssh:
        protocol: ssh
        ip: 10.1.1.10
        port: 22
```

---

## Verification

Declarative verification suites check device state against expected conditions:

```yaml
name: "Connectivity Audit"
tests:
  - device: "spine-1"
    check: "interface_up"
    interface: "GigabitEthernet0/1"
    within: "30s"

  - device: "spine-1"
    check: "route_exists"
    destination: "10.0.0.0/8"

  - device: "spine-1"
    check: "ping"
    target: "8.8.8.8"
    threshold: 0.0
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

## Status

**Current**: v1.1 — verification framework (state assertion API with composable logic), CLI tool, end-to-end testing against Network Simulator daemon.

**Completed:**
- v1.0 — testbed management, SSH/mock/netsim backends, parser framework (4 parsers with real Cisco IOS fixtures), connection pooling

---

[← Back to Network Automation](../network-automation)
