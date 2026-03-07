---
layout: default
section: network-automation
---

# Network Configuration Framework

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
- [Current Status](#current-status)
- [Technical Reports](#technical-reports)

## Concept

Network Configuration Framework is a Rust CLI that compiles declarative YAML blueprints into vendor-neutral configuration artifacts. A single binary orchestrates the full pipeline: blueprint parsing, topology transformation, DeviceIR generation, template rendering, and traceable config file emission.

The core problem is determinism. Hand-written network configs drift between devices, between sites, between engineers. The Network Configuration Framework treats configuration as a compilation target: a blueprint declares intent (protocol layers, IP pools, policy constraints), and the compiler produces auditable, diffable output files suitable for CI/CD pipelines.

Blueprints are composed from importable fragments. A site blueprint imports protocol definitions (OSPFv3, BFD, VRRP) as separate YAML files, each declaring layer dependencies. The compiler resolves the import graph, orders layers by their `requires:` declarations, and executes primitives in sequence.

---

## Code Samples

### ISP dual-stack peering blueprint

```yaml
version: 1

layers:
  - name: pools
    primitives:
      - type: global_pool
        name: fra-transit-v4
        pool: "198.51.100.0/24"
      - type: global_pool
        name: fra-transit-v6
        pool: "2001:db8:fra::/48"
      - type: global_resource_pool
        name: fra-private-asn
        resource_type: asn
        pool: "64512-64530"

  - name: topology
    primitives:
      - type: mesh_nodes
        mode: hub_and_spoke
        hubs: ["fra-br1", "fra-br2", "fra-br3"]
        spokes: ["transit-a", "transit-b", "ce-1", "ce-2"]

  - name: addressing
    requires: [pools, topology]
    primitives:
      - type: provision_ips
        pool_ref: fra-transit-v4
        prefix_length: 31
        scope: { link_role: transit }

  - name: bgp
    requires: [addressing]
    primitives:
      - type: build_protocol_layer
        protocol: bgp
        scope: { link_role: [transit, customer] }

assertions:
  - type: is_connected
  - type: reachability
    from: { role: border }
    to: { role: customer_edge }
```

### DSL transformation rule

```yaml
transformations:
  - name: nxos_lowering
    when: "device_os == 'nxos'"
    rules:
      - match: "kind == 'interface' && name.startsWith('Ethernet')"
        apply:
          name: "name + '/1'"
          mtu: 9216
```

---

## Usage

```bash
# Compile a blueprint to device configs
netcfg compile blueprint.yaml --output configs/

# Validate without generating output
netcfg validate blueprint.yaml

# Target a specific vendor
netcfg compile blueprint.yaml --target arista-eos --output configs/
```

---

## Architecture

<div class="mermaid">
flowchart LR
    P[Parse] --> T[Transform]
    T --> L[Lower]
    L --> R[Render]
    R --> E[Emit]
    style P fill:#e3f2fd
    style T fill:#e3f2fd
    style L fill:#e3f2fd
    style R fill:#e3f2fd
    style E fill:#e3f2fd
</div>

The pipeline runs in five phases:

1. **Parse** — Read the blueprint YAML, resolve imports, validate structure.
2. **Transform** — Execute primitives (`mesh_nodes`, `provision_ips`, `build_protocol_layer`) against the topology graph. Each primitive reads from and writes to node/edge data.
3. **Lower** — Apply mapping rules that convert graph data into vendor-intermediate representation (DeviceIR). Selectors match nodes by role, site, or layer.
4. **Render** — MiniJinja templates consume DeviceIR stanzas and produce vendor-specific CLI syntax. Template selection is driven by `device_os` metadata.
5. **Emit** — Write `.cfg` files per device, using atomic rename for transactional output.

Vendor abstraction lives in the lowering and rendering phases. The same blueprint produces Arista EOS, Cisco NX-OS, or Juniper Junos output by swapping the mapping rules and template set. The topology graph and primitive execution are vendor-agnostic.

<div class="mermaid">
flowchart TD
    BGP["bgp layer<br/><small>requires: addressing</small>"]
    ADDR["addressing layer<br/><small>requires: pools, topology</small>"]
    POOLS["pools layer"]
    TOPO["topology layer"]
    BGP --> ADDR
    ADDR --> POOLS
    ADDR --> TOPO
</div>

Error reporting uses `miette` for source-snippet diagnostics: blueprint validation errors, IP pool exhaustion, and selector mismatches all produce span-highlighted terminal output pointing to the relevant YAML lines.

---

## Current Status

v2.1 Protocol Library & Security Policy DSL in progress. Previous: v1.2 Front & Back Ends shipped.

---

## Technical Reports

- [Download Technical Report: techreport.pdf](/assets/docs/ank-netcfg-techreport.pdf)

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
