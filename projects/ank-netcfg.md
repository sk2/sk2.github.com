---
layout: default
section: network-automation
---

# Network Configuration Framework

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](../network-automation)

---

## Concept

Network Configuration Framework is a Rust CLI that compiles declarative YAML blueprints into vendor-neutral configuration artifacts. A single binary orchestrates the full pipeline: blueprint parsing, topology transformation, DeviceIR generation, template rendering, and traceable config file emission.

The core problem is determinism. Hand-written network configs drift between devices, between sites, between engineers. The Network Configuration Framework treats configuration as a compilation target: a blueprint declares intent (protocol layers, IP pools, policy constraints), and the compiler produces auditable, diffable output files suitable for CI/CD pipelines.

Blueprints are composed from importable fragments. A site blueprint imports protocol definitions (OSPFv3, BFD, VRRP) as separate YAML files, each declaring layer dependencies. The compiler resolves the import graph, orders layers by their `requires:` declarations, and executes primitives in sequence.

---

## Architecture

The pipeline runs in five phases:

1. **Parse** -- Read the blueprint YAML, resolve imports, validate structure.
2. **Transform** -- Execute primitives (`mesh_nodes`, `provision_ips`, `build_protocol_layer`) against the topology graph. Each primitive reads from and writes to node/edge data.
3. **Lower** -- Apply mapping rules that convert graph data into vendor-intermediate representation (DeviceIR). Selectors match nodes by role, site, or layer; stanzas declare the configuration kind (`interface`, `bgp_neighbor`, `prefix_list`).
4. **Render** -- MiniJinja templates consume DeviceIR stanzas and produce vendor-specific CLI syntax. Template selection is driven by `device_os` metadata.
5. **Emit** -- Write `.cfg` files per device, using atomic rename for transactional output.

Vendor abstraction lives in the lowering and rendering phases. The same blueprint produces Arista EOS, Cisco NX-OS, or Juniper Junos output by swapping the mapping rules and template set. The topology graph and primitive execution are vendor-agnostic.

Error reporting uses `miette` for source-snippet diagnostics: blueprint validation errors, IP pool exhaustion, and selector mismatches all produce span-highlighted terminal output pointing to the relevant YAML lines.

---

## Examples

### Blueprint: EVPN-VXLAN Fabric

A blueprint declares layers in execution order. Each layer contains primitives that operate on the topology graph.

```yaml
# examples/evpn-vxlan-fabric.yaml
version: 1

imports:
  - "../docs/library/datacenter-rules.yaml"
  - "../docs/library/hardware-lowering.yaml"

layers:
  - name: resources
    primitives:
      - type: allocate_resources
        selector: "nodes[true]"
        resource_type: "bgp_as"
        pool: "65001-65001"
        strategy: dense

      - type: allocate_resources
        selector: "nodes[true]"
        resource_type: "router_id"
        pool: "10.255.0.1-10.255.0.255"
        strategy: dense

  - name: underlay
    primitives:
      - type: provision_ips
        selector: "edges[true]"
        pool: "10.0.0.0/24"
        subnet_size: 31
        strategy: dense

      - type: build_protocol_layer
        selector: "nodes[true]"
        layer: ospf
        config:
          area: "0.0.0.0"
        clone_underlying: true

  - name: overlays
    primitives:
      - type: build_vxlan
        selector: "nodes[role=='leaf']"
        vni_base: 10000
        mcast_group_base: "239.1.1.1"

      - type: build_evpn
        selector: "nodes[role=='leaf']"
        route_distinguisher_base: "auto"
        route_target_base: "65001:10000"

assertions:
  - name: "loopback-prefix-check"
    severity: error
    select: "nodes[true]"
    check:
      type: "field_in_cidr"
      field: "router_id"
      cidr: "10.255.0.0/24"
```

### Mapping: DeviceIR Generation

Mapping rules convert graph data into vendor-intermediate stanzas. Jinja2 expressions (`{{ router_id }}`) interpolate values from each node's data.

```yaml
# examples/evpn-vxlan-mapping.yaml
rules:
  - selector: "nodes[role=='leaf']"
    rules:
      - stanza:
          kind: "interface"
          fields:
            name: "Loopback0"
            address: "{{ router_id }}/32"
            description: "Router-ID / VTEP source"

      - stanza:
          kind: "bgp_neighbor"
          fields:
            local_as: "{{ bgp_as }}"
            peer_ip: "{{ peer_ip }}"
            remote_as: "{{ remote_as }}"
            description: "iBGP EVPN Peer"
            export_policy: "RP-UNDERLAY-EXPORT"

  - selector: "nodes[true]"
    rules:
      - stanza:
          kind: "prefix_list"
          key: "PL-LOOPBACKS"
          fields:
            entries:
              - prefix: "10.255.0.0/24"
                action: "permit"
                le: 32
```

### Vendor-Specific Lowering

DSL transformation rules apply vendor-specific adjustments during the lowering phase:

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
# Validate a blueprint and show the execution plan
ank_netcfg plan --blueprint examples/evpn-vxlan-fabric.yaml

# Generate vendor configs from blueprint + mapping
ank_netcfg generate \
  --blueprint examples/evpn-vxlan-fabric.yaml \
  --mapping examples/evpn-vxlan-mapping.yaml \
  --output-dir ./configs/
```

The `plan` command parses, validates, and displays the layer execution order and primitive sequence without generating output. The `generate` command runs the full pipeline and writes `.cfg` files to the output directory.

---

## Status

The front and back ends of the compiler are fully functional. Blueprint parsing, topology transformation, DeviceIR generation, template rendering, and config emission all work end-to-end. The rendering engine uses MiniJinja for vendor-specific config synthesis. Terminal diagnostics use `miette` for source-snippet error reporting.

Current work (v2.1) focuses on a standard protocol library (importable YAML fragments for the full simulator protocol set), a security policy DSL with named groups, security zones, and zone-based policy, and NAT policy primitives.

---

## Technical Reports

- [Download Technical Report: netcfg-techreport.pdf](/assets/docs/ank-netcfg-netcfg-techreport.pdf)

---

[← Back to Network Automation](../network-automation)
