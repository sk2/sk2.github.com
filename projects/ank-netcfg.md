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
- [What This Is](#what-this-is)
- [Current Milestone: v1.3 Advanced Topology & Production Readiness](#current-milestone-v13-advanced-topology-production-readiness)
- [Current State (v1.2 Front & Back Ends — shipped)](#current-state-v12-front-back-ends-shipped)
- [Core Value](#core-value)
- [Requirements](#requirements)
- [Key Decisions](#key-decisions)
- [Constraints](#constraints)

## Technical Reports

- [Download Technical Report: netcfg-techreport.pdf](/assets/docs/ank-netcfg-netcfg-techreport.pdf)
- [Download Technical Report: netcfg-paper.pdf](/assets/docs/ank-netcfg-netcfg-paper.pdf)

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

### generate_fabric_topo.rs

```rust
use nte_topology::Topology;
use std::collections::HashMap;
use serde_json::json;

fn main() {
    let mut topo = Topology::new();
    
    // 2 Spines, 2 Leaves
    let ids = vec![1, 2, 3, 4];
    let types = vec!["Router".to_string(); 4];
    let layers = vec!["input".to_string(); 4];
    
    topo.add_nodes_with_metadata(&ids, &types, &layers).unwrap();
    
    let mut data = Vec::new();
    // Spine 1 (NX-OS)
    data.push(json!({"hostname": "spine1", "device_os": "nxos", "role": "spine"}).to_string());
    // Spine 2 (NX-OS)
    data.push(json!({"hostname": "spine2", "device_os": "nxos", "role": "spine"}).to_string());
    // Leaf 1 (EOS)
    data.push(json!({"hostname": "leaf1", "device_os": "eos", "role": "leaf"}).to_string());
    // Leaf 2 (EOS)
    data.push(json!({"hostname": "leaf2", "device_os": "eos", "role": "leaf"}).to_string());

    let df = polars::prelude::DataFrame::new(vec![
        polars::prelude::Column::from(polars::prelude::Series::new("id".into(), ids)),
        polars::prelude::Column::from(polars::prelude::Series::new("data_json".into(), data)),
    ]).unwrap();
    
    topo.set_dataframe("Router".to_string(), df);
    
    // Physical Cabling
    // spine1 -> leaf1, leaf2
    // spine2 -> leaf1, leaf2
    let graph = topo.graph_mut();
    graph.ensure_device_shortcuts(1, 3).unwrap();
    graph.ensure_device_shortcuts(1, 4).unwrap();
    graph.ensure_device_shortcuts(2, 3).unwrap();
    graph.ensure_device_shortcuts(2, 4).unwrap();
    
    let bytes = topo.save_to_bytes().unwrap();
    std::fs::write("fabric_topo.nte", bytes).unwrap();
    println!("Created fabric_topo.nte");
}

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

### advanced_primitive_tests.rs

```rust
use nte_topology::Topology;
use netcfg_core::dsl::schema::{
    Primitive, BuildPrefixListSpec, BuildCommunityListSpec
};
use netcfg_core::primitives::vxlan::{BuildVxlanSpec, BuildEvpnSpec};
use netcfg_core::models::stanza::{PrefixListEntry, CommunityListEntry};
use netcfg_core::primitives::{PrimitiveContext, PrimitiveRunner};
use ipnet::IpNet;
use std::str::FromStr;

fn setup_topo() -> Topology {
    let mut topo = Topology::new();
    topo.add_nodes_with_metadata(
        &[1],
        &["Router".to_string()],
        &["input".to_string()],
    )
    .unwrap();
    topo
}

#[test]
fn test_build_prefix_list() {
    let mut topo = setup_topo();
    let mut ctx = PrimitiveContext::new(&mut topo, "input");

    let spec = Primitive::BuildPrefixList(BuildPrefixListSpec {
        selector: "nodes[true]".to_string(),
        name: "PL-TEST".to_string(),
        entries: vec![
            PrefixListEntry {
                prefix: IpNet::from_str("10.0.0.0/8").unwrap(),
                action: "permit".to_string(),
                le: Some(32),
                ge: None,
            }
        ],
    });

    spec.execute(&mut ctx).expect("executed");
    
    let dev_ctx = ctx.get_device_context("Router", 1).unwrap();
    assert_eq!(dev_ctx.stanzas.len(), 1);
    assert_eq!(dev_ctx.stanzas[0].kind, "prefix_list");
    assert_eq!(dev_ctx.stanzas[0].key, Some("PL-TEST".to_string()));
}

#[test]
fn test_build_community_list() {
    let mut topo = setup_topo();
    let mut ctx = PrimitiveContext::new(&mut topo, "input");

    let spec = Primitive::BuildCommunityList(BuildCommunityListSpec {
        selector: "nodes[true]".to_string(),
        name: "CL-TEST".to_string(),
        entries: vec![
            CommunityListEntry {
                community: "65000:100".to_string(),
                action: "permit".to_string(),
            }
        ],
    });

    spec.execute(&mut ctx).expect("executed");
    
    let dev_ctx = ctx.get_device_context("Router", 1).unwrap();
    assert_eq!(dev_ctx.stanzas.len(), 1);
    assert_eq!(dev_ctx.stanzas[0].kind, "community_list");
}

#[test]
fn test_build_vxlan() {
    let mut topo = setup_topo();
    let mut ctx = PrimitiveContext::new(&mut topo, "input");

    let spec = Primitive::BuildVxlan(BuildVxlanSpec {
        selector: "nodes[true]".to_string(),
        vni_base: 10000,
        mcast_group_base: Some("239.1.1.1".to_string()),
    });

    spec.execute(&mut ctx).expect("executed");
    
    let dev_ctx = ctx.get_device_context("Router", 1).unwrap();
    let vxlan_stanza = dev_ctx.stanzas.iter().find(|s| s.kind == "vxlan_vtep").unwrap();
    assert_eq!(vxlan_stanza.fields.get("vni").unwrap().as_u64().unwrap(), 10000);
}

#[test]
fn test_build_evpn() {
    let mut topo = setup_topo();
    let mut ctx = PrimitiveContext::new(&mut topo, "input");

    let spec = Primitive::BuildEvpn(BuildEvpnSpec {
        selector: "nodes[true]".to_string(),
        route_distinguisher_base: "65000:1".to_string(),
        route_target_base: "65000:1".to_string(),
    });

    spec.execute(&mut ctx).expect("executed");
    
    let dev_ctx = ctx.get_device_context("Router", 1).unwrap();
    let evpn_stanza = dev_ctx.stanzas.iter().find(|s| s.kind == "evpn_instance").unwrap();
    assert_eq!(evpn_stanza.fields.get("rd").unwrap().as_str().unwrap(), "65000:1");
}

```

### diff_tests.rs

```rust
use nte_topology::Topology;

use netcfg_core::diff::{Change, DiffEngine, PlanRenderer};

#[test]
fn test_diff_engine_add_remove_update() {
    let mut current = Topology::new();
    // Add 1 node in current
    current
        .add_nodes_with_metadata(&[1], &["Router".to_string()], &["physical".to_string()])
        .unwrap();

    let mut desired = Topology::new();
    // Add node 2 in desired
    desired
        .add_nodes_with_metadata(&[2], &["Router".to_string()], &["physical".to_string()])
        .unwrap();

    // Compute diff
    let plan = DiffEngine::compute_plan(&current, &desired).expect("diff failed");

    // We expect:
    // - Add node 2
    // - Remove node 1
    let stats = plan.statistics();
    assert_eq!(stats.nodes_added, 1);
    assert_eq!(stats.nodes_updated, 0);
    assert_eq!(stats.nodes_removed, 1);

    // Check specific changes
    let mut found_add = false;
    let mut found_remove = false;

    for change in &plan.changes {
        match change {
            Change::AddNode { id, node_type, .. } => {
                assert_eq!(*id, 2);
                assert_eq!(node_type, "Router");
                found_add = true;
            }
            Change::RemoveNode { id, .. } => {
                assert_eq!(*id, 1);
                found_remove = true;
            }
            _ => {}
        }
    }

    assert!(found_add, "Add node 2 not found");
    assert!(found_remove, "Remove node 1 not found");

    // Test reverse direction (should flip add/remove)
    let rev_plan = DiffEngine::compute_plan(&desired, &current).expect("reverse diff failed");
    let rev_stats = rev_plan.statistics();
    assert_eq!(rev_stats.nodes_added, 1);
    assert_eq!(rev_stats.nodes_removed, 1);
    assert_eq!(rev_stats.nodes_updated, 0);

    // Test renderer output
    let text = PlanRenderer::render_verbose(&plan);
    assert!(text.contains("Nodes: +1 -1 ~0"));
    assert!(text.contains("+ Node 2 [Router]"));
    assert!(text.contains("- Node 1 [Router]"));
}

#[test]
fn test_diff_engine_stable_output() {
    let mut current = Topology::new();
    let mut desired = Topology::new();

    current
        .add_nodes_with_metadata(&[1], &["Router".to_string()], &["physical".to_string()])
        .unwrap();
    desired
        .add_nodes_with_metadata(&[1], &["Router".to_string()], &["physical".to_string()])
        .unwrap();

    let plan1 = DiffEngine::compute_plan(&current, &desired).unwrap();
    let plan2 = DiffEngine::compute_plan(&current, &desired).unwrap();

    assert_eq!(plan1, plan2);
    assert_eq!(plan1.statistics().additions(), 0);
    assert_eq!(plan1.statistics().changes(), 0);
    assert_eq!(plan1.statistics().removals(), 0);

    let text = PlanRenderer::render_text(&plan1);
    assert!(text.contains("No changes detected"));
}

```

---

## Usage

### DSL Transformation Example

```rust
// Define a transformation rule in the netcfg DSL
let nxos_transform = TransformationSpec {
    name: "nxos_lowering".to_string(),
    when: Some("device_os == 'nxos'".to_string()),
    rules: vec![
        RewriteRule {
            match_expr: "kind == 'interface' && name.startsWith('Ethernet')".to_string(),
            apply: HashMap::from([
                ("name".to_string(), "name + '/1'".to_string()),
                ("mtu".to_string(), "9216".to_string()), // Force Jumbo frames
            ]),
        }
    ],
};
```

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## What This Is

Deterministic, auditable, CI/CD-friendly Rust CLI for compiling declarative YAML network blueprints into vendor-neutral configuration artifacts. The `netcfg` binary orchestrates: blueprint parsing → topology transformation → DeviceIR generation → template rendering → traceable config file emission.

---

## Current Milestone: v1.3 Advanced Topology & Production Readiness

**Goal:** Elevate the compiler to production readiness by introducing advanced primitives (route reflectors, edge cloning), an auditable state validation mode, rigorous benchmarking, and decoupling repository dependencies for crate publication.

**Target features:**
- Advanced Primitives — `mesh_nodes` partial meshes and `build_protocol_layer` overlay edge cloning
- State Validation — `netcfg validate` mode enforcing addressing plans without mutation
- Performance & Publishing — `criterion` benchmarking suites and `[ank_nte](../ank_nte)` repository absorption/decoupling

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

## Core Value

Single-binary network compiler: design, transform, and generate configs from YAML blueprints without Python.

---

## Requirements



---

## # Active (v1.3)

- [ ] Partial Meshes (hub-and-spoke/route reflectors) (MESH-V2-01)
- [ ] Overlay Edge Cloning (PROT-V2-01)
- [ ] State Validation Mode: `netcfg validate` (IPAM-V2-01)
- [ ] Addressing Plan Enforcement (IPAM-V2-02)
- [ ] Benchmarking suites for Diff/Render engines (PERF-01)
- [ ] Repository Decoupling of `[ank_nte](../ank_nte)` (PUB-01)

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

*Last updated: 2026-03-01 after v1.2 Front & Back Ends milestone*

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)
