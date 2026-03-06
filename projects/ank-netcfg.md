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

[← Back to Projects](../projects)

---

## Contents

- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Concept](#concept)
- [Current Milestone: v2.1 Protocol Library & Security Policy DSL](#current-milestone-v21-protocol-library-security-policy-dsl)
- [Current State (v1.2 Front & Back Ends — shipped)](#current-state-v12-front-back-ends-shipped)
- [Requirements](#requirements)
- [Key Decisions](#key-decisions)
- [Constraints](#constraints)

## Technical Reports

- [Download Technical Report: netcfg-techreport.pdf](/assets/docs/ank-netcfg-netcfg-techreport.pdf)

---

## Code Samples

### evpn-vxlan-fabric.yaml

```yaml
# examples/evpn-vxlan-fabric.yaml
#
# Multi-vendor EVPN-VXLAN Spine-Leaf Fabric
# This blueprint demonstrates:
#   1. Underlay (OSPF)
#   2. Control-plane (iBGP EVPN)
#   3. Overlay (VXLAN VNIs)
#   4. Advanced Policies (Prefix-lists, Community-lists)

version: 1

imports:
  - "../docs/library/datacenter-rules.yaml"
  - "../docs/library/hardware-lowering.yaml"

layers:
  # Stage 1: Resource Allocation (ASN, Loopbacks)
  - name: resources
    primitives:
      - type: map_hardware_inventory
        selector: "nodes[role=='leaf']"
        chassis_model: "dcs-7508"
        slots:
          1: "linecard-48port-10g"

      - type: allocate_resources
        selector: "nodes[true]"
        resource_type: "bgp_as"
        pool: "65001-65001" # Single AS for iBGP fabric
        strategy: dense

      - type: allocate_resources
        selector: "nodes[true]"
        resource_type: "router_id"
        pool: "10.255.0.1-10.255.0.255"
        strategy: dense

  # Stage 2: Underlay Connectivity
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

  # Stage 3: EVPN Control Plane
  - name: control_plane
    primitives:
      - type: build_protocol_layer
        selector: "nodes[true]"
        layer: bgp
        config:
          protocol_type: bgp
          peer_type: ibgp
        clone_underlying: false # iBGP usually peered via loopbacks

      - type: mesh_nodes
        selector: "nodes[layer=='bgp']"
        mesh_type: full # Simple full-mesh iBGP for this example

  # Stage 4: Advanced Filtering Policies
  - name: policies
    primitives:
      - type: build_prefix_list
        selector: "nodes[true]"
        prefix_list_name: "PL-LOOPBACKS"
        entries:
          - prefix: "10.255.0.0/24"
            action: "permit"
            le: 32

      - type: build_community_list
        selector: "nodes[true]"
        community_list_name: "CL-EVPN"
        entries:
          - community: "65001:1000"
            action: "permit"

      - type: build_routing_policy
        selector: "nodes[true]"
        policy_name: "RP-UNDERLAY-EXPORT"
        statements:
          - name: "PERMIT-LOOPBACKS"
            action: "permit"
            match_prefix_list: "PL-LOOPBACKS"

  # Stage 5: VXLAN Overlays
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

### evpn-vxlan-mapping.yaml

```yaml
# examples/evpn-vxlan-mapping.yaml
#
# Multi-vendor DeviceIR mapping for the EVPN-VXLAN fabric.
# Demonstrates how the same topology data generates vendor-specific CLI stanzas.

rules:
  # 1. Leaf Configuration
  - selector: "nodes[role=='leaf']"
    rules:
      - stanza:
          kind: "interface"
          fields:
            name: "Loopback0" # Template handles vendor-specific mapping if needed
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

  # 2. Spine Configuration
  - selector: "nodes[role=='spine']"
    rules:
      - stanza:
          kind: "interface"
          fields:
            name: "Loopback0"
            address: "{{ router_id }}/32"
            description: "Router-ID"

      - stanza:
          kind: "ospf_neighbor"
          fields:
            interface: "{{ interface }}"
            area: "0.0.0.0"
            network_type: "point-to-point"

  # 3. Global Policy Application (Prefix-Lists)
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

### multi-protocol-site.yaml

```yaml
# examples/multi-protocol-site.yaml
#
# Multi-protocol site blueprint — demonstrates composing protocol library
# fragments via imports.
#
# Topology: routers in a full mesh.
#   - All routers run OSPFv3 (IPv6 underlay) with BFD for fast failure detection.
#   - All routers run VRRP for gateway redundancy.
#
# How imports work:
#   Imported layers are appended after the root blueprint's own layers, so the
#   physical layer (defined here) is always processed first. Each protocol
#   fragment declares requires: [physical] to enforce this ordering.
#
# Overriding protocol defaults:
#   Create a supplementary import file that adds another build_protocol_layer
#   in a new layer after the protocol layer. Config is deep-merged, so you
#   only need to specify the fields you want to change. Example:
#
#     # protocols/overrides/bfd-fast.yaml
#     version: 1
#     layers:
#       - name: bfd_fast
#         requires: [bfd]
#         primitives:
#           - type: build_protocol_layer
#             selector: "nodes[role='spine']"
#             layer: bfd
#             config:
#               min_tx_ms: 100
#               min_rx_ms: 100
#
#   Then import it after the base protocol:
#     imports:
#       - ../protocols/bfd.yaml
#       - ../protocols/overrides/bfd-fast.yaml

version: 1
imports:
  - ../protocols/ospfv3.yaml
  - ../protocols/bfd.yaml
  - ../protocols/vrrp.yaml

layers:
  - name: physical
    primitives:
      - type: mesh_nodes
        selector: "nodes[true]"
        mesh_type: full

      - type: provision_ips
        selector: "edges[src>=0]"
        pool: "10.0.0.0/24"
        subnet_size: 30
        strategy: dense

```

### three-site-mesh-mapping.yaml

```yaml
# examples/three-site-mesh-mapping.yaml
#
# Companion mapping for three-site-mesh.yaml.
# Produces a BGP config file for site-a-r1 demonstrating end-to-end pipeline output.
#
# The mapping targets all_nodes and emits a bgp stanza grouped under "site-a-r1".
# Using kind: "bgp" ensures the rendered output contains BGP keywords.
#
# The default fallback template renders: kind={{ kind }} key={{ key }}
# So each matched node produces a line: "kind=bgp key="
#
# Note: the `node` field is used by generate_configs to group output by device.
# It is not passed to the stanza template renderer.

rules:
  - selector: "all_nodes"
    stanza:
      kind: "bgp"
      fields:
        node: "site-a-r1"
        local_asn: "65001"
        description: "site-a full-mesh BGP session"

```

### three-site-mesh.yaml

```yaml
# examples/three-site-mesh.yaml
#
# Three-site BGP mesh — canonical reference blueprint for [ank_pydantic](../ank_pydantic) consumers.
#
# This blueprint demonstrates the complete netcfg primitive pipeline:
#
#   Stage 1 — MeshNodes: creates full-mesh point-to-point links within each site.
#              Each site's routers are fully meshed independently (intra-site only).
#              A full mesh of N nodes produces N*(N-1)/2 edges.
#
#   Stage 2 — ProvisionIps: assigns /30 subnets to each P2P link.
#              Each site has its own /24 address pool — IPs are scoped per-site.
#              ProvisionIps MUST run after MeshNodes (edges must exist first).
#              Writes src_ip, dst_ip, subnet to each endpoint node's data.
#
#   Stage 3 — BuildProtocolLayer: clones each physical node into a BGP overlay layer.
#              The BGP node inherits its parent's IP data (src_ip, dst_ip).
#              BuildProtocolLayer MUST run after ProvisionIps to inherit IP addresses.
#
# Address plan:
#   Site A: 10.1.0.0/24 — routers site-a-r1..r4
#   Site B: 10.2.0.0/24 — routers site-b-r1..r4
#   Site C: 10.3.0.0/24 — routers site-c-r1..r4
#
# Each /24 provides 64 /30 subnets — more than enough for 6 links per site.

version: 1
layers:
  # Stage 1: Create full mesh of P2P links within each site.
  # Selector "nodes[site=...]" matches nodes whose data_json contains {"site": "..."}.
  # 4 nodes per site → 4*(4-1)/2 = 6 edges per site → 18 edges total.
  - name: input
    primitives:
      - type: mesh_nodes
        selector: "nodes[site='a']"
        mesh_type: full
        

      - type: mesh_nodes
        selector: "nodes[site='b']"
        mesh_type: full
        

      - type: mesh_nodes
        selector: "nodes[site='c']"
        mesh_type: full
        

  # Stage 2: Assign /30 P2P addresses from per-site pools.
  # ProvisionIps runs AFTER MeshNodes — edges must exist before IPs can be assigned.
  # Each /30 uses .1 (src_ip) and .2 (dst_ip) host addresses.
  # "edges[src>=0]" selects all edges in the physical layer.
  - name: input
    primitives:
      - type: provision_ips
        selector: "edges[src>=0]"
        pool: "10.1.0.0/24"
        subnet_size: 30
        strategy: dense

  # Stage 3: Build BGP overlay — one BGP node per physical node.
  # BuildProtocolLayer MUST run after ProvisionIps to inherit src_ip/dst_ip.
  # The BGP node's data_json is deep-merged from its physical parent, so
  # the BGP node carries the same IP data that ProvisionIps wrote.
  - name: input
    primitives:
      - type: build_protocol_layer
        selector: "nodes[true]"
        layer: bgp
        config:
          protocol_type: bgp
          asn_base: "65000"

```

### validate-test-blueprint.yaml

```yaml
version: 1
layers:
  - name: physical
    primitives:
      - type: mesh_nodes
        selector: "nodes[hostname != '']"
        mesh_type: "full"
        edge_properties: {}
      - type: provision_ips
        selector: "edges[true]"
        pool: "10.0.0.0/16"
        strategy: "dense"

```

### cross-layer.yaml

```yaml
version: 1
layers:
  - name: ipam
    primitives:
      - type: provision_ips
        selector: "nodes[role == 'leaf']"
        pool: "10.0.0.0/24"
        subnet_size: 32
  
  - name: bgp
    requires: [ipam]
    primitives:
      - type: build_protocol_layer
        selector: "nodes[role == 'leaf']"
        layer: "bgp"
        config: { asn: 65001 }

assertions:
  - name: "bgp_leaf_requires_ipam_address"
    select: "nodes[layer == 'bgp']"
    check:
      type: custom_cel
      # Cross-layer logic: get data from 'ipam' layer for this node
      expression: "get_layer_data(id, 'ipam').has('ipv4_address')"
    help: "Nodes in the BGP layer must first have an IP address assigned in the 'ipam' layer. Check the 'ipam' primitive selectors."

```


---

## Usage

### DSL Transformation Example

```yaml
# DSL Transformation Rule
# Applied when device_os matches 'nxos'
transformations:
  - name: nxos_lowering
    when: "device_os == 'nxos'"
    rules:
      - match: "kind == 'interface' && name.startsWith('Ethernet')"
        apply:
          name: "name + '/1'"
          mtu: 9216  # Force jumbo frames
```

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Concept

Deterministic, auditable, CI/CD-friendly Rust CLI that compiles declarative YAML network blueprints into vendor-neutral configuration artifacts. The `netcfg` binary orchestrates: blueprint parsing, topology transformation, DeviceIR generation, template rendering, and traceable config file emission.

---

## Current Milestone: v2.1 Protocol Library & Security Policy DSL

**Goal:** Deliver a standard library of importable protocol fragments covering the full simulator protocol set, LaTeX DSL formatting for technical reports, and a first-class security policy DSL with named groups, security zones, zone-based policy, NAT, and assertions.

**Target features:**
- Protocol Library — importable YAML fragments for all simulator protocols (OSPF, BGP, IS-IS, LACP, LLDP, ARP, STP, GRE, VXLAN, BGP-EVPN + existing BFD/VRRPv3/RIP/LDP/RSVP-TE)
- LaTeX DSL Formatter — `listings`-based syntax highlighting for blueprint YAML in the tech report
- Named Groups — `groups:` section in Blueprint, `$group_name` selectors, `tag_nodes` primitive
- Security Zones — `kind: security_zone` group type, zone membership from group resolution
- Zone Policy DSL — `build_zone_policy` primitive with address/service objects, permit/deny rules
- NAT Policy — `build_nat_policy` primitive for source/destination NAT
- Policy Assertions — verifiable security invariants on zone membership and zone policy

---

## Current State (v1.2 Front & Back Ends — shipped)

The front and back ends of the compiler are fully functional end-to-end:
- **** (The Rendering Engine): Vendor-specific config synthesis via MiniJinja template loading and `data_json` injection.
- **** (The CLI Application): Core `netcfg plan` and `netcfg generate` commands orchestrating the full pipeline and writing `.cfg` artifacts.
- **** (Rich Terminal Diagnostics): `miette`-powered source-snippet error reporting for blueprint validation and IP pool exhaustion.

**Known tech debt (v1.3):**
- Path dependency on `[ank_nte](../ank_nte)` prevents standalone crate publication
- Benchmarks for large topologies (10,000+ nodes) are missing
- `edge_properties` in `mesh_nodes` remains deferred

---

## Requirements



---

## # Active (v2.1)

- [ ] Remaining protocol fragments: OSPF, BGP, IS-IS, LACP, LLDP, ARP, STP, GRE, VXLAN, BGP-EVPN (PROTO-01–10)
- [ ] LaTeX DSL formatter for tech report (DOC-01)
- [ ] Named groups `groups:` section + `$name` selectors (GROUP-01–02)
- [ ] `tag_nodes` primitive for group membership tagging (GROUP-03)
- [ ] Nested groups with parent inheritance (GROUP-04)
- [ ] Security zone group type `kind: security_zone` (ZONE-01–02)
- [ ] `build_zone_policy` primitive with address/service objects (POLICY-01–04)
- [ ] `build_nat_policy` primitive for source/destination NAT (NAT-01–02)
- [ ] Policy assertions for security invariants (ASSERT-01–02)

---

## # Deferred (v2.0+)

- IPv6 pool support (IPAM-V2-03)
- Interface name derivation in `mesh_nodes` (MESH-V2-02)
- LSP server (`nte-lsp`) integration (LSP-01)

---

## # Validated (v1.0 - v1.2)

- ✓ Mapping DSL to populate stanza-based `DeviceIR` models
- ✓ Native template rendering via MiniJinja
- ✓ Strict data lineage
- ✓ Declarative YAML Graph Blueprints
- ✓ Stateful diff engine
- ✓ Single-binary capability
- ✓ Cross-phase integration
- ✓ `build_protocol_layer` implemented
- ✓ `provision_ips` implemented
- ✓ `mesh_nodes` implemented
- ✓ CLI `plan` and `generate`
- ✓ `miette` terminal diagnostics

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| `Topology::from_core()` wrapper bridges `CoreTopology` into Evaluator | Evaluator tightly coupled to Python-wrapper type; wrapping at phase boundary is cleanest | ✓ Good |
| `NamedTempFile::new_in(parent)` for transactional output | Same-filesystem guarantee enables atomic POSIX rename | ✓ Good |
| Clap 4 `Args` wrapper struct (`ConfigCommand`) containing `Subcommand` enum | Matches Clap 4 nested subcommand pattern, consistent with `BlueprintCommand` | ✓ Good |
| `RenderEngine::render_node` per-node API | Clean separation between transformation and configuration generation | ✓ Good |
| `miette` for diagnostic reporting | Provides out-of-the-box snippet and span highlighting for YAML errors | ✓ Good |

---

## Constraints

- Rust stable only — no nightly features
- British English in all documentation
- GSD workflow for phase-based planning

*Last updated: 2026-03-06 — Milestone v2.1 started*

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
