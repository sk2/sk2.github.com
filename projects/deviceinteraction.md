---
layout: default
section: network-automation
---

# Device Interaction Framework

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Architecture](#architecture)
- [Current Status](#current-status)

## Concept

A Rust library and CLI for network device interaction and automated testing. Provides the essential PyATS capabilities — testbed management, CLI output parsing, and state verification — without the complexity. Connects to devices (real, simulated, or mocked), executes commands, parses structured output, and verifies correctness with the type safety of compiled Rust.

---

## Code Samples

### Verification suite

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

### Testbed definition

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
    connections:
      mock:
        protocol: mock
        ip: 127.0.0.1

  leaf-1:
    type: switch
    os: cisco_ios
    role: leaf
    connections:
      ssh:
        protocol: ssh
        ip: 10.1.1.10
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

## Current Status

v1.1 Complete Testing Stack in progress. v1.0 shipped 2026-02-22.

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
