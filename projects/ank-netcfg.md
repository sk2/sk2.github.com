---
layout: default
section: network-automation
description: "Network Configuration Framework is a Rust CLI that compiles declarative YAML blueprints into vendor-neutral configuration artifacts."
---

# Network Configuration Framework

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Architecture](#architecture)

## Concept

Network Configuration Framework is a Rust CLI that compiles declarative YAML blueprints into vendor-neutral configuration artifacts. A single binary orchestrates the full pipeline: blueprint parsing, topology transformation, DeviceIR generation, template rendering, and traceable config file emission.

The core problem is determinism. Hand-written network configs drift between devices, between sites, between engineers. The Network Configuration Framework treats configuration as a [compilation](../compilation) target: a blueprint declares intent (protocol layers, IP pools, policy constraints), and the compiler produces auditable, diffable output files suitable for CI/CD pipelines.

Blueprints are composed from importable fragments. A site blueprint imports protocol definitions (OSPFv3, BFD, VRRP) as separate YAML files, each declaring layer dependencies. The compiler resolves the import graph, orders layers by their `requires:` declarations, and executes primitives in sequence.

---

## Technical Reports

- [Download Technical Report: netcfg-techreport.pdf](/assets/docs/ank-netcfg-netcfg-techreport.pdf)
- [Download Research Paper: netcfg-paper.pdf](/assets/docs/ank-netcfg-netcfg-paper.pdf)

---

## Code Samples

### 01_isp_dual_stack_peering.yaml

```yaml
version: 1
imports: []
layers:
- name: pools
  requires: []
  primitives:
  - type: global_pool
    name: fra-transit-v4
    pool: '198.51.100.0/24'
    vrf: null
  - type: global_pool
    name: fra-transit-v6
    pool: '2001:db8:fra::/48'
    vrf: null
  - type: global_pool
    name: fra-ce-v4
    pool: '203.0.113.0/24'
    vrf: null
  - type: global_pool
    name: fra-ce-v6
    pool: '2001:db8:ce::/48'
    vrf: null
  - type: global_resource_pool
    name: fra-private-asn
    resource_type: asn
    pool: '64512-64530'
- name: peering
  requires:
  - pools
  primitives:
  - type: mesh_nodes
    selector: $border_and_transit
    mesh_type: hub_and_spoke
    hub_selector: $borders
    spoke_selector: $transits
    naming_strategy: cisco_ge
  - type: mesh_nodes
    selector: $border_and_ce
    mesh_type: hub_and_spoke
    hub_selector: $borders
    spoke_selector: $customer_edges
    naming_strategy: cisco_ge
- name: addressing
  requires:
  - peering
  primitives:
  - type: provision_ips
    selector: $transit_links
    pool: fra-transit-v4
    subnet_size: 31
    ipv6_pool: fra-transit-v6
    ipv6_subnet_size: 127
    strategy: dense
    pool_size: null
    vrf: null
  - type: provision_ips
    selector: $ce_links
    pool: fra-ce-v4
    subnet_size: 30
    ipv6_pool: fra-ce-v6
    ipv6_subnet_size: 126
    strategy: dense
    pool_size: null
    vrf: null
  - type: allocate_resources
    selector: $customer_edges
    resource_type: asn
    pool: fra-private-asn
    strategy: dense
    pool_size: null
- name: secrets
  requires:
  - addressing
  primitives:
  - type: inject_secrets
    selector: $borders
    secrets:
      bgp_md5_transit: ${BGP_MD5_TRANSIT_KEY}
      bgp_md5_customer: ${BGP_MD5_CUSTOMER_KEY}
      tacacs_key: ${TACACS_SECRET}
- name: filters
  requires:
  - secrets
  primitives:
  - type: generate_safe_bgp_filters
    selector: $borders
    prefix_list_name: BOGON-FILTER-V4
    policy_name: TRANSIT-INBOUND
    block_rfc1918: true
    permit_default: false
- name: bgp
  requires:
  - filters
  primitives:
  - type: build_protocol_layer
    selector: $all_routers
    layer: bgp
    config:
      asn_base: '65100'
      protocol_type: bgp
    clone_underlying: true
assertions:
- name: border-routers-connected
  severity: error
  select: $borders
  check:
    type: is_connected
  help: A border router is isolated — check peering layer wiring.
- name: ce-reachable-from-border
  severity: error
  select: $customer_edges
  check:
    type: reachability
    target_selector: $borders
  help: A customer-edge router cannot reach any border router.
- name: transit-peering-bipartite
  severity: error
  select: $border_and_transit
  check:
    type: is_bipartite
  help: Transit peering graph is not bipartite — unexpected link between same-role nodes.
- name: links-have-ipv4
  severity: error
  select: edges[true]
  check:
    type: field_exists
    field: src_ip
  help: An edge is missing its IPv4 source address — check provision_ips.
- name: transit-ips-in-range
  severity: warning
  select: edges[link_type='transit']
  check:
    type: field_in_cidr
    field: src_ip
    cidr: '198.51.100.0/24'
  help: A transit link IP is outside the expected 198.51.100.0/24 range.
rules: {}
groups:
  transit_links: edges[link_type=='transit']
  all_routers: $borders | $transits | $customer_edges
  customer_edges: nodes[role=='ce']
  borders: nodes[role=='border']
  border_and_ce: $borders | $customer_edges
  border_and_transit: $borders | $transits
  ce_links: edges[link_type=='ce']
  transits: nodes[role=='transit']
blast_radius:
- name: limit-teardown
  select: null
  check:
    type: max_deletions
    count: 2
transforms:
- name: junos-interface-rewrite
  when: device_os == 'junos'
  rules:
  - match_expr: stanza.kind == 'interface'
    apply:
      name: '''xe-0/0/'' + string(stanza.fields.abstract_index)'
- name: junos-transit-apply-group
  when: device_os == 'junos'
  rules:
  - match_expr: stanza.kind == 'bgp_neighbor' and stanza.fields.description == 'transit'
    apply:
      apply_groups: '''TRANSIT-DEFAULTS'''
hardware_library:
  chassis: []
  linecards: []

```

### 02_campus_compliance_audit.yaml

```yaml
version: 1
imports: []
layers:
- name: provisioning
  requires: []
  primitives:
  - type: conditional
    condition: topology.node_count >= 3
    then_primitives:
    - type: custom_primitive
      name: building-loopbacks
      parameters:
        pool_cidr: '10.250.0.0/16'
      primitives:
      - type: provision_ips
        selector: $all_switches
        pool: '{{params.pool_cidr}}'
        subnet_size: 32
        ipv6_pool: null
        ipv6_subnet_size: null
        strategy: dense
        pool_size: null
        vrf: null
    else_primitives: null
- name: management
  requires:
  - provisioning
  primitives:
  - type: build_access_policy
    selector: $dist_switches
    policy_name: MGMT-ACCESS
    rules:
    - name: allow-noc-ssh
      action: permit
      source_prefix: '10.0.0.0/8'
      destination_prefix: null
      protocol: tcp
      source_port: null
      destination_port: 22
    - name: allow-noc-https
      action: permit
      source_prefix: '10.0.0.0/8'
      destination_prefix: null
      protocol: tcp
      source_port: null
      destination_port: 443
    - name: deny-all-mgmt
      action: deny
      source_prefix: null
      destination_prefix: null
      protocol: null
      source_port: null
      destination_port: null
assertions:
- name: ntp-compliance
  severity: error
  select: $all_switches
  check:
    type: use_rule
    name: ntp-configured
  help: Node is missing NTP configuration — at least 2 NTP servers required.
- name: syslog-compliance
  severity: error
  select: $all_switches
  check:
    type: use_rule
    name: syslog-configured
  help: Node has no syslog server configured.
- name: management-vlan-audit
  severity: warning
  select: $access_switches
  check:
    type: use_rule
    name: management-vlan-correct
  help: Access switch management VLAN should be 99.
- name: distribution-inventory-schema
  severity: error
  select: $dist_switches
  check:
    type: match_schema
    schema:
      properties:
        firmware_version:
          type: string
        hostname:
          minLength: 1
          type: string
        serial_number:
          pattern: ^[A-Z0-9]{11}$
          type: string
        site:
          enum:
          - eng
          - sci
          - lib
          - admin
          - med
          - arts
          type: string
      required:
      - hostname
      - serial_number
      - firmware_version
      - site
      type: object
  help: Distribution switch is missing required inventory fields or has invalid data.
- name: hostnames-unique-per-building
  severity: error
  select: $all_switches
  check:
    type: unique_per_group
    field: hostname
    group_by: site
  help: Duplicate hostname detected within the same building.
- name: ibgp-acyclic
  severity: error
  select: nodes[protocol='ibgp']
  check:
    type: is_acyclic
  help: iBGP session graph contains a [cycle](../cycle) — check route-reflector hierarchy.
- name: access-dual-homed
  severity: error
  select: $access_switches
  check:
    type: min_edges
    count: 2
  help: Access switch has fewer than 2 uplinks — single point of failure.
- name: all-nodes-have-hostname
  severity: error
  select: nodes[true]
  check:
    type: field_exists
    field: hostname
  help: A node is missing its hostname field.
rules:
  management-vlan-correct: has(node.mgmt_vlan) and node.mgmt_vlan == 99
  syslog-configured: has(node.syslog_server) and node.syslog_server != ''
  ntp-configured: has(node.ntp_servers) and size(node.ntp_servers) >= 2
groups:
  all_switches: $access_switches | $dist_switches
  access_switches: nodes[role=='access']
  dist_switches: nodes[role=='distribution']
  campus_links: edges[link_type=='campus']
blast_radius:
- name: audit-change-cap
  select: null
  check:
    type: max_percentage_changed
    value: 10.0
transforms: []
hardware_library:
  chassis: []
  linecards: []

```

### 03_wan_migration.yaml

```yaml
version: 1
imports: []
layers:
- name: pools
  requires: []
  primitives:
  - type: global_resource_pool
    name: isis-net-pool
    resource_type: isis_net
    pool: '49.0001.0000.0000.0001-49.0001.0000.0000.0200'
  - type: global_resource_pool
    name: sr-sid-pool
    resource_type: segment_id
    pool: '16001-16200'
- name: migration
  requires:
  - pools
  primitives:
  - type: conditional
    condition: topology.node_count < 10
    then_primitives:
    - type: allocate_resources
      selector: $london_pe
      resource_type: isis_net
      pool: isis-net-pool
      strategy: dense
      pool_size: null
    - type: allocate_resources
      selector: $london_pe
      resource_type: segment_id
      pool: sr-sid-pool
      strategy: dense
      pool_size: null
    else_primitives:
    - type: allocate_resources
      selector: $all_pe
      resource_type: isis_net
      pool: isis-net-pool
      strategy: dense
      pool_size: null
    - type: allocate_resources
      selector: $all_pe
      resource_type: segment_id
      pool: sr-sid-pool
      strategy: dense
      pool_size: null
- name: secrets
  requires:
  - migration
  primitives:
  - type: inject_secrets
    selector: nodes[city='london']
    secrets:
      isis_auth_key: ${ISIS_KEY_LONDON}
      tacacs_key: ${TACACS_KEY_EU}
  - type: inject_secrets
    selector: nodes[city='paris']
    secrets:
      isis_auth_key: ${ISIS_KEY_PARIS}
      tacacs_key: ${TACACS_KEY_EU}
  - type: inject_secrets
    selector: nodes[city='frankfurt']
    secrets:
      isis_auth_key: ${ISIS_KEY_FRANKFURT}
      tacacs_key: ${TACACS_KEY_EU}
- name: filters
  requires:
  - secrets
  primitives:
  - type: generate_safe_bgp_filters
    selector: $border_routers
    prefix_list_name: BOGON-INBOUND
    policy_name: EBGP-INBOUND-FILTER
    block_rfc1918: true
    permit_default: false
- name: routing-policy
  requires:
  - filters
  primitives:
  - type: build_routing_policy
    selector: $all_pe
    policy_name: MIGRATION-PREFER-ISIS
    statements:
    - name: prefer-isis-routes
      action: permit
      match_prefix_list: null
      match_community_list: ISIS-MIGRATED
      match_as_path: null
      set_local_preference: 200
      set_metric: null
      set_as_path_prepend: null
      set_community: null
      next_hop: null
    - name: depref-ospf-routes
      action: permit
      match_prefix_list: null
      match_community_list: OSPF-LEGACY
      match_as_path: null
      set_local_preference: 80
      set_metric: null
      set_as_path_prepend: null
      set_community: null
      next_hop: null
    - name: default-permit
      action: permit
      match_prefix_list: null
      match_community_list: null
      match_as_path: null
      set_local_preference: null
      set_metric: null
      set_as_path_prepend: null
      set_community: null
      next_hop: null
- name: isis-overlay
  requires:
  - routing-policy
  primitives:
  - type: build_protocol_layer
    selector: $pe_and_p
    layer: isis
    config:
      level: level-2
      protocol_type: isis
    clone_underlying: true
assertions:
- name: pe-reaches-p-via-isis
  severity: error
  select: $all_pe
  check:
    type: reachability
    target_selector: $p_routers
  help: A PE router cannot reach any P router — IS-IS adjacency may be down.
- name: pe-has-isis-net
  severity: error
  select: $all_pe
  check:
    type: field_exists
    field: isis_net
  help: PE is missing its IS-IS NET address — check allocate_resources.
- name: pe-has-sr-sid
  severity: error
  select: $all_pe
  check:
    type: field_exists
    field: segment_id
  help: PE is missing its SR node SID — check allocate_resources.
- name: border-reachable
  severity: error
  select: $border_routers
  check:
    type: reachability
    target_selector: $all_pe
  help: Border router is unreachable from PE — migration may have broken transit.
rules: {}
groups:
  p_routers: nodes[role=='p']
  london_pe: nodes[city=='london' and role=='pe']
  border_routers: nodes[role=='border']
  pe_and_p: $all_pe | $p_routers
  all_pe: nodes[role=='pe']
blast_radius:
- name: migration-change-limit
  select: null
  check:
    type: max_modifications
    count: 5
transforms:
- name: iosxr-interface-rewrite
  when: device_os == 'iosxr'
  rules:
  - match_expr: stanza.kind == 'interface'
    apply:
      name: '''GigabitEthernet0/0/0/'' + string(stanza.fields.abstract_index)'
- name: iosxr-sr-annotation
  when: device_os == 'iosxr'
  rules:
  - match_expr: stanza.kind == 'isis_neighbor'
    apply:
      metric: '10'
      sr_enabled: 'true'
hardware_library:
  chassis: []
  linecards: []

```

### 04_multi_tenant_dc.yaml

```yaml
version: 1
imports: []
layers:
- name: fabric
  requires: []
  primitives:
  - type: mesh_nodes
    selector: $spines_and_leaves
    mesh_type: hub_and_spoke
    hub_selector: $spines
    spoke_selector: $leaves
    naming_strategy: cisco_ge
- name: addressing
  requires:
  - fabric
  primitives:
  - type: provision_ips
    selector: $equities_links
    pool: '10.100.0.0/16'
    subnet_size: 30
    ipv6_pool: null
    ipv6_subnet_size: null
    strategy: dense
    pool_size: null
    vrf: equities
  - type: provision_ips
    selector: $fixed_income_links
    pool: '10.100.0.0/16'
    subnet_size: 30
    ipv6_pool: null
    ipv6_subnet_size: null
    strategy: dense
    pool_size: null
    vrf: fixed-income
  - type: provision_ips
    selector: $risk_links
    pool: '10.100.0.0/16'
    subnet_size: 30
    ipv6_pool: null
    ipv6_subnet_size: null
    strategy: dense
    pool_size: null
    vrf: risk
  - type: provision_ips
    selector: $fabric_links
    pool: '172.16.0.0/16'
    subnet_size: 31
    ipv6_pool: null
    ipv6_subnet_size: null
    strategy: dense
    pool_size: null
    vrf: null
- name: security
  requires:
  - addressing
  primitives:
  - type: build_access_policy
    selector: $spines
    policy_name: INTER-VRF-DENY
    rules:
    - name: deny-eq-to-fi
      action: deny
      source_prefix: '10.100.0.0/16'
      destination_prefix: '10.100.0.0/16'
      protocol: ip
      source_port: null
      destination_port: null
    - name: deny-eq-to-risk
      action: deny
      source_prefix: '10.100.0.0/16'
      destination_prefix: '10.100.0.0/16'
      protocol: ip
      source_port: null
      destination_port: null
    - name: permit-intra-vrf
      action: permit
      source_prefix: null
      destination_prefix: null
      protocol: null
      source_port: null
      destination_port: null
- name: overlay
  requires:
  - security
  primitives:
  - type: build_protocol_layer
    selector: $spines_and_leaves
    layer: bgp
    config:
      asn_base: '65200'
      protocol_type: bgp
    clone_underlying: true
assertions:
- name: every-leaf-has-tenant
  severity: error
  select: $leaves
  check:
    type: use_rule
    name: tenant-assigned
  help: Leaf switch is missing tenant assignment.
- name: every-leaf-has-vrf
  severity: error
  select: $leaves
  check:
    type: use_rule
    name: vrf-configured
  help: Leaf switch has no VRF configured.
- name: every-leaf-has-vlan
  severity: warning
  select: $leaves
  check:
    type: use_rule
    name: leaf-has-vlan
  help: Leaf switch is missing VLAN ID — check tenant provisioning.
- name: tenant-metadata-schema
  severity: error
  select: $leaves
  check:
    type: match_schema
    schema:
      properties:
        hostname:
          minLength: 1
          type: string
        tenant:
          enum:
          - equities
          - fixed-income
          - risk
          type: string
        vlan_id:
          maximum: 4094
          minimum: 1
          type: integer
        vrf_name:
          type: string
      required:
      - hostname
      - tenant
      - vrf_name
      - vlan_id
      type: object
  help: Leaf node data does not match expected tenant metadata schema.
- name: vlans-unique-per-tenant
  severity: error
  select: $leaves
  check:
    type: unique_per_group
    field: vlan_id
    group_by: tenant
  help: Duplicate VLAN ID detected within the same tenant.
- name: equities-connected
  severity: error
  select: $equities_or_spines
  check:
    type: is_connected
  help: Equities tenant subgraph is disconnected — a leaf is unreachable.
- name: fixed-income-connected
  severity: error
  select: $fixed_income_or_spines
  check:
    type: is_connected
  help: Fixed-income tenant subgraph is disconnected — a leaf is unreachable.
- name: risk-connected
  severity: error
  select: $risk_or_spines
  check:
    type: is_connected
  help: Risk tenant subgraph is disconnected — a leaf is unreachable.
rules:
  vrf-configured: has(node.vrf_name) and node.vrf_name != ''
  leaf-has-vlan: has(node.vlan_id) and node.vlan_id > 0 and node.vlan_id < 4095
  tenant-assigned: has(node.tenant) and node.tenant != ''
groups:
  risk_or_spines: nodes[tenant=='risk'] | $spines
  spines_and_leaves: $spines | $leaves
  equities_links: edges[tenant=='equities']
  risk_links: edges[tenant=='risk']
  fixed_income_links: edges[tenant=='fixed-income']
  equities_or_spines: nodes[tenant=='equities'] | $spines
  spines: nodes[role=='spine']
  fabric_links: edges[link_type=='fabric']
  fixed_income_or_spines: nodes[tenant=='fixed-income'] | $spines
  leaves: nodes[role=='leaf']
blast_radius:
- name: tenant-vrf-protection
  select: null
  check:
    type: max_deletions
    count: 3
- name: fabric-change-cap
  select: null
  check:
    type: max_percentage_changed
    value: 25.0
transforms:
- name: nxos-interface-rewrite
  when: device_os == 'nxos'
  rules:
  - match_expr: stanza.kind == 'interface'
    apply:
      name: '''Ethernet1/'' + string(stanza.fields.abstract_index + 1)'
- name: nxos-vrf-context
  when: device_os == 'nxos'
  rules:
  - match_expr: stanza.kind == 'bgp_neighbor' and has(stanza.fields.vrf)
    apply:
      nxos_vrf_context: stanza.fields.vrf
hardware_library:
  chassis: []
  linecards: []

```

### 05_sp_mpls_core.yaml

```yaml
# Case Study 05 — Service Provider MPLS Core
#
# Models a Tier-2 ISP backbone running IS-IS as the IGP with Segment
# Routing (SR-MPLS) replacing LDP for label distribution.  BFD provides
# sub-second failure detection on all core links.
#
# Topology:
#   3 Provider Edge (PE) routers — customer-facing, originate L3VPN services
#   2 Provider (P) routers — transit core, no customer interfaces
#   PE1–PE3 connect to P1 and P2 in a partial mesh (hub-and-spoke to core)
#   P1–P2 are fully meshed between themselves
#
# Design choices:
#   - IS-IS Level-2 only (flat backbone, no area hierarchy)
#   - SR-MPLS with SRGB 16000–23999; each PE gets a unique Node SID
#   - BFD with 100 ms timers for fast convergence
#   - TACACS+ for device administration with local fallback
#   - syslog + NTP for operational baseline
#   - IOS-XR transforms for GigabitEthernet naming
#
# Address plan:
#   P2P links:    10.0.0.0/16  (/31 subnets)
#   Router IDs:   192.0.2.0/24
#   Node SIDs:    16001–16200

version: 1
imports: []
layers:
- name: pools
  requires: []
  primitives:
  - type: global_resource_pool
    name: router-id-pool
    resource_type: router_id
    pool: '192.0.2.1-192.0.2.254'
  - type: global_resource_pool
    name: node-sid-pool
    resource_type: segment_id
    pool: '16001-16200'

- name: topology
  requires:
  - pools
  primitives:
  # Full mesh between P routers (P1–P2)
  - type: mesh_nodes
    selector: $p_routers
    mesh_type: full
    naming_strategy: cisco_ge
  # PE routers connect to every P router (hub-and-spoke)
  - type: mesh_nodes
    selector: $pe_and_p
    mesh_type: hub_and_spoke
    hub_selector: $p_routers
    spoke_selector: $pe_routers
    naming_strategy: cisco_ge

- name: addressing
  requires:
  - topology
  primitives:
  - type: provision_ips
    selector: $core_links
    pool: '10.0.0.0/16'
    subnet_size: 31
    strategy: dense
  - type: allocate_resources
    selector: $all_routers
    resource_type: router_id
    pool: router-id-pool
    strategy: dense
  - type: allocate_resources
    selector: $all_routers
    resource_type: segment_id
    pool: node-sid-pool
    strategy: dense

- name: underlay
  requires:
  - addressing
  primitives:
  - type: build_protocol_layer
    selector: $all_routers
    layer: isis
    config:
      level: level_2
      metric_style: wide
      protocol_type: isis
    clone_underlying: true
  - type: build_protocol_layer
    selector: $all_routers
    layer: sr_mpls
    config:
      srgb_start: 16000
      srgb_end: 23999
      prefer_sr: true
      ti_lfa: true
  - type: build_protocol_layer
    selector: $all_routers
    layer: bfd
    config:
      min_tx_ms: 100
      min_rx_ms: 100
      detect_mult: 3

- name: services
  requires:
  - underlay
  primitives:
  - type: build_protocol_layer
    selector: $pe_routers
    layer: bgp
    config:
      asn_base: '65100'
      protocol_type: bgp
      peer_type: ibgp
    clone_underlying: true
  - type: build_protocol_layer
    selector: $all_routers
    layer: tacacs
    config:
      servers: ["10.99.0.1", "10.99.0.2"]
      fallback_local: true
  - type: build_protocol_layer
    selector: $all_routers
    layer: ntp
    config:
      servers: ["10.99.0.10", "10.99.0.11"]
      source_interface: loopback0
  - type: build_protocol_layer
    selector: $all_routers
    layer: syslog
    config:
      servers: ["10.99.0.20"]
      facility: local7
      severity: informational

- name: secrets
  requires:
  - services
  primitives:
  - type: inject_secrets
    selector: $all_routers
    secrets:
      tacacs_key: ${TACACS_KEY}
      isis_auth_key: ${ISIS_AUTH_KEY}

assertions:
- name: pe-reaches-every-p
  severity: error
  select: $pe_routers
  check:
    type: reachability
    target_selector: $p_routers
  help: A PE router cannot reach a P router — check IS-IS adjacencies.

- name: core-is-connected
  severity: error
  select: $all_routers
  check:
    type: is_connected
  help: Core network is partitioned — a router is isolated.

- name: every-router-has-sid
  severity: error
  select: $all_routers
  check:
    type: field_exists
    field: segment_id
  help: Router is missing its SR Node SID — check allocate_resources.

- name: every-router-has-rid
  severity: error
  select: $all_routers
  check:
    type: field_exists
    field: router_id
  help: Router is missing its router-id — check allocate_resources.

- name: ntp-compliance
  severity: error
  select: $all_routers
  check:
    type: use_rule
    name: ntp-configured
  help: Router is missing NTP configuration.

rules:
  ntp-configured: has(node.ntp_servers) and size(node.ntp_servers) >= 2

groups:
  pe_routers: nodes[role=='pe']
  p_routers: nodes[role=='p']
  pe_and_p: $pe_routers | $p_routers
  all_routers: $pe_routers | $p_routers
  core_links: edges[true]

blast_radius:
- name: core-change-limit
  select: null
  check:
    type: max_modifications
    count: 5

transforms:
- name: iosxr-interface-naming
  when: device_os == 'iosxr'
  rules:
  - match_expr: stanza.kind == 'interface'
    apply:
      name: "'GigabitEthernet0/0/0/' + string(stanza.fields.abstract_index)"
- name: iosxr-isis-sr
  when: device_os == 'iosxr'
  rules:
  - match_expr: stanza.kind == 'isis_neighbor'
    apply:
      sr_enabled: 'true'
      metric: '10'

hardware_library:
  chassis: []
  linecards: []

```

### 06_campus_nac.yaml

```yaml
# Case Study 06 — Campus Network with 802.1X NAC
#
# Models a university campus network with three-tier architecture
# (core → distribution → access), 802.1X port-based access control,
# DHCP relay, VRRP gateway redundancy, and full compliance auditing.
#
# Topology:
#   2 Core routers          — OSPF area 0 backbone, VRRP gateway pair
#   2 Distribution switches — aggregate access layer, DHCP relay
#   4 Access switches       — host-facing, 802.1X + MAB enforcement
#
# Design choices:
#   - OSPF area 0 flat backbone (single area for simplicity)
#   - VRRP on core for default gateway redundancy
#   - RSTP with BPDU guard on access ports
#   - 802.1X with MAB fallback and guest VLAN 999
#   - RADIUS for 802.1X backend, TACACS+ for admin access
#   - DHCP relay on access switches → central DHCP server
#   - LLDP for neighbour discovery and topology verification
#   - NTP + syslog compliance assertions
#
# Address plan:
#   Core links:          10.0.0.0/24  (/30 subnets)
#   Distribution links:  10.0.1.0/24  (/30 subnets)
#   Access links:        10.0.2.0/24  (/30 subnets)

version: 1
imports: []
layers:
- name: topology
  requires: []
  primitives:
  # Core pair — full mesh (single link between core1 and core2)
  - type: mesh_nodes
    selector: $core
    mesh_type: full
  # Distribution connects to both core switches
  - type: mesh_nodes
    selector: $core_and_dist
    mesh_type: hub_and_spoke
    hub_selector: $core
    spoke_selector: $distribution
  # Access connects to distribution (dual-homed)
  - type: mesh_nodes
    selector: $dist_and_access
    mesh_type: hub_and_spoke
    hub_selector: $distribution
    spoke_selector: $access

- name: addressing
  requires:
  - topology
  primitives:
  - type: provision_ips
    selector: $core_links
    pool: '10.0.0.0/24'
    subnet_size: 30
    strategy: dense
  - type: provision_ips
    selector: $dist_links
    pool: '10.0.1.0/24'
    subnet_size: 30
    strategy: dense
  - type: provision_ips
    selector: $access_links
    pool: '10.0.2.0/24'
    subnet_size: 30
    strategy: dense

- name: routing
  requires:
  - addressing
  primitives:
  - type: build_protocol_layer
    selector: $all_switches
    layer: ospf
    config:
      area: '0.0.0.0'
      network_type: point_to_point
    clone_underlying: true
  - type: build_protocol_layer
    selector: $core
    layer: vrrp
    config:
      version: 3
      vrid: 10
      priority: 110
      preempt: true
      advertisement_interval_ms: 1000
  - type: build_protocol_layer
    selector: $all_switches
    layer: bfd
    config:
      min_tx_ms: 300
      min_rx_ms: 300
      detect_mult: 3

- name: switching
  requires:
  - routing
  primitives:
  - type: build_protocol_layer
    selector: $all_switches
    layer: stp
    config:
      mode: rstp
      bpdu_guard: true
  - type: build_protocol_layer
    selector: $all_switches
    layer: lldp
    config:
      tx_interval_s: 30
      hold_multiplier: 4
  - type: build_protocol_layer
    selector: $access
    layer: lacp
    config:
      mode: active
      min_links: 1
      lacp_rate: fast

- name: security
  requires:
  - switching
  primitives:
  # 802.1X on access layer with guest VLAN and MAB fallback
  - type: build_protocol_layer
    selector: $access
    layer: dot1x
    config:
      mode: multi-auth
      reauth_period_s: 3600
      guest_vlan: 999
      auth_fail_vlan: 998
      critical_vlan: 997
      mac_bypass: true
  # RADIUS for 802.1X backend
  - type: build_protocol_layer
    selector: $access
    layer: radius
    config:
      servers: ["10.99.0.50", "10.99.0.51"]
      auth_port: 1812
      acct_port: 1813
      use_accounting: true
  # TACACS+ for admin access on all devices
  - type: build_protocol_layer
    selector: $all_switches
    layer: tacacs
    config:
      servers: ["10.99.0.1", "10.99.0.2"]
      fallback_local: true
      authorization: true
      accounting: true
  # Management ACL restricting SSH/HTTPS access
  - type: build_access_policy
    selector: $all_switches
    policy_name: MGMT-ACCESS
    rules:
    - name: allow-noc-ssh
      action: permit
      source_prefix: '10.99.0.0/24'
      destination_prefix: null
      protocol: tcp
      source_port: null
      destination_port: 22
    - name: allow-noc-https
      action: permit
      source_prefix: '10.99.0.0/24'
      destination_prefix: null
      protocol: tcp
      source_port: null
      destination_port: 443
    - name: deny-all-mgmt
      action: deny
      source_prefix: null
      destination_prefix: null
      protocol: null
      source_port: null
      destination_port: null

- name: services
  requires:
  - security
  primitives:
  # DHCP relay on access switches pointing to central DHCP server
  - type: build_protocol_layer
    selector: $access
    layer: dhcp_relay
    config:
      servers: ["10.99.0.100"]
      option_82: true
      source_interface: loopback0
  # NTP on all devices
  - type: build_protocol_layer
    selector: $all_switches
    layer: ntp
    config:
      servers: ["10.99.0.10", "10.99.0.11"]
      source_interface: loopback0
  # Syslog on all devices
  - type: build_protocol_layer
    selector: $all_switches
    layer: syslog
    config:
      servers: ["10.99.0.20"]
      facility: local7
      severity: informational

- name: secrets
  requires:
  - services
  primitives:
  - type: inject_secrets
    selector: $all_switches
    secrets:
      tacacs_key: ${TACACS_KEY}
      radius_secret: ${RADIUS_SECRET}

assertions:
- name: access-dual-homed
  severity: error
  select: $access
  check:
    type: min_edges
    count: 2
  help: Access switch has fewer than 2 uplinks — single point of failure.

- name: core-connected
  severity: error
  select: $all_switches
  check:
    type: is_connected
  help: Campus network is partitioned — a switch is isolated.

- name: ntp-compliance
  severity: error
  select: $all_switches
  check:
    type: use_rule
    name: ntp-configured
  help: Switch is missing NTP configuration — at least 2 NTP servers required.

- name: syslog-compliance
  severity: error
  select: $all_switches
  check:
    type: use_rule
    name: syslog-configured
  help: Switch has no syslog server configured.

- name: hostnames-unique
  severity: error
  select: $all_switches
  check:
    type: field_exists
    field: hostname
  help: A switch is missing its hostname field.

- name: access-bipartite
  severity: error
  select: $dist_and_access
  check:
    type: is_bipartite
  help: Access-to-distribution graph is not bipartite — unexpected link between same-tier nodes.

rules:
  ntp-configured: has(node.ntp_servers) and size(node.ntp_servers) >= 2
  syslog-configured: has(node.syslog_server) and node.syslog_server != ''

groups:
  core: nodes[role=='core']
  distribution: nodes[role=='distribution']
  access: nodes[role=='access']
  core_and_dist: $core | $distribution
  dist_and_access: $distribution | $access
  all_switches: $core | $distribution | $access
  core_links: edges[tier=='core']
  dist_links: edges[tier=='distribution']
  access_links: edges[tier=='access']

blast_radius:
- name: campus-change-cap
  select: null
  check:
    type: max_percentage_changed
    value: 15.0

transforms: []
hardware_library:
  chassis: []
  linecards: []

```

### 07_sdwan_ipsec.yaml

```yaml
# Case Study 07 — Multi-Site SD-WAN with IPsec Overlay
#
# Models a hub-and-spoke SD-WAN connecting branch offices to dual DC
# hubs via IPsec tunnels, with OSPF running over the encrypted overlay
# for dynamic routing and BFD for fast failover.
#
# Topology:
#   2 DC hub routers   — terminate all branch tunnels, fully meshed
#   4 Branch routers   — each connects to both hubs (dual-homed)
#
# Design choices:
#   - IKEv2 with AES-256-GCM and DH group 20 (ECDH-384)
#   - OSPF over IPsec tunnels (point-to-point network type)
#   - BFD with relaxed timers (300 ms) for WAN tolerance
#   - PSK injected via inject_secrets (never hardcoded)
#   - NTP + syslog + SNMP for operational baseline
#   - WireGuard alternative shown as conditional (for VyOS branches)
#   - Blast radius limits: max 2 deletions to prevent mass decommission
#
# Address plan:
#   Hub-to-hub:    172.16.0.0/24  (/31 subnets)
#   Hub-to-branch: 172.16.1.0/24  (/30 subnets)

version: 1
imports: []
layers:
- name: topology
  requires: []
  primitives:
  # Full mesh between DC hub routers
  - type: mesh_nodes
    selector: $hubs
    mesh_type: full
  # Each branch connects to both hubs
  - type: mesh_nodes
    selector: $hubs_and_branches
    mesh_type: hub_and_spoke
    hub_selector: $hubs
    spoke_selector: $branches

- name: addressing
  requires:
  - topology
  primitives:
  - type: provision_ips
    selector: $hub_links
    pool: '172.16.0.0/24'
    subnet_size: 31
    strategy: dense
  - type: provision_ips
    selector: $branch_links
    pool: '172.16.1.0/24'
    subnet_size: 30
    strategy: dense

- name: encryption
  requires:
  - addressing
  primitives:
  # IPsec IKEv2 overlay on all routers
  - type: build_protocol_layer
    selector: $all_routers
    layer: ipsec
    config:
      ike_version: 2
      encryption: aes256gcm
      dh_group: 20
      ike_lifetime_s: 86400
      ipsec_lifetime_s: 3600
      dpd_interval_s: 30
      dpd_retries: 5
      tunnel_mode: tunnel
    clone_underlying: true
  # Conditional: use WireGuard instead of IPsec for VyOS branches
  - type: conditional
    condition: topology.node_count < 0
    then_primitives:
    - type: build_protocol_layer
      selector: nodes[device_os=='vyos']
      layer: wireguard
      config:
        listen_port: 51820
        mtu: 1420
        persistent_keepalive_s: 25
    else_primitives: null

- name: routing
  requires:
  - encryption
  primitives:
  - type: build_protocol_layer
    selector: $all_routers
    layer: ospf
    config:
      area: '0.0.0.0'
      network_type: point_to_point
    clone_underlying: true
  - type: build_protocol_layer
    selector: $all_routers
    layer: bfd
    config:
      min_tx_ms: 300
      min_rx_ms: 300
      detect_mult: 3

- name: management
  requires:
  - routing
  primitives:
  - type: build_protocol_layer
    selector: $all_routers
    layer: ntp
    config:
      servers: ["10.99.0.10", "10.99.0.11"]
      source_interface: loopback0
  - type: build_protocol_layer
    selector: $all_routers
    layer: syslog
    config:
      servers: ["10.99.0.20"]
      facility: local7
  - type: build_protocol_layer
    selector: $all_routers
    layer: snmp
    config:
      version: "3"
      v3_auth_protocol: sha
      v3_priv_protocol: aes128
      v3_security_level: authPriv
      trap_targets: ["10.99.0.30"]

- name: secrets
  requires:
  - management
  primitives:
  - type: inject_secrets
    selector: $all_routers
    secrets:
      ipsec_psk: ${IPSEC_PSK}
      snmp_auth_pass: ${SNMP_AUTH_PASS}
      snmp_priv_pass: ${SNMP_PRIV_PASS}

assertions:
- name: branch-dual-homed
  severity: error
  select: $branches
  check:
    type: min_edges
    count: 2
  help: Branch router has fewer than 2 hub connections — no failover path.

- name: hubs-connected
  severity: error
  select: $hubs
  check:
    type: is_connected
  help: DC hub routers are not directly connected.

- name: branch-reaches-hub
  severity: error
  select: $branches
  check:
    type: reachability
    target_selector: $hubs
  help: A branch router cannot reach any DC hub — check IPsec tunnel.

- name: ntp-compliance
  severity: error
  select: $all_routers
  check:
    type: use_rule
    name: ntp-configured
  help: Router is missing NTP configuration.

- name: all-have-ipsec-psk
  severity: error
  select: $all_routers
  check:
    type: field_exists
    field: ipsec_psk
  help: Router is missing IPsec pre-shared key — check inject_secrets.

rules:
  ntp-configured: has(node.ntp_servers) and size(node.ntp_servers) >= 2

groups:
  hubs: nodes[role=='hub']
  branches: nodes[role=='branch']
  hubs_and_branches: $hubs | $branches
  all_routers: $hubs | $branches
  hub_links: edges[tier=='hub']
  branch_links: edges[tier=='branch']

blast_radius:
- name: prevent-mass-decommission
  select: null
  check:
    type: max_deletions
    count: 2

transforms: []
hardware_library:
  chassis: []
  linecards: []

```

### 08_multicast_video.yaml

```yaml
# Case Study 08 — Multicast Video Distribution Network
#
# Models an IPTV / video distribution network using PIM Sparse Mode
# with a dedicated Rendezvous Point, IGMP on access-facing interfaces,
# and OSPF as the unicast underlay for RPF lookups.
#
# Topology:
#   1 Rendezvous Point (RP) — PIM-SM RP, BSR candidate
#   2 Core routers           — PIM transit, OSPF backbone
#   2 Distribution routers   — aggregate multicast streams
#   3 Access routers         — IGMP snooping, last-hop PIM
#
# Design choices:
#   - PIM-SM with static RP (RP address set on rp1's loopback)
#   - IGMPv3 on access layer for source-specific multicast (SSM) readiness
#   - OSPF area 0 as unicast underlay for RPF validation
#   - MLAG on distribution pairs for resilient multicast forwarding
#   - LLDP for topology discovery
#   - NetFlow/IPFIX on core for multicast traffic accounting
#   - BFD for fast PIM neighbour failure detection
#
# Address plan:
#   Core links:  10.10.0.0/24 (/31)
#   Dist links:  10.10.1.0/24 (/30)
#   Access links: 10.10.2.0/24 (/30)
#   Multicast:   239.1.0.0/16 (admin-scoped)

version: 1
imports: []
layers:
- name: pools
  requires: []
  primitives:
  - type: global_resource_pool
    name: router-id-pool
    resource_type: router_id
    pool: '10.255.0.1-10.255.0.50'

- name: topology
  requires:
  - pools
  primitives:
  # RP connects to both core routers
  - type: mesh_nodes
    selector: $rp_and_core
    mesh_type: hub_and_spoke
    hub_selector: $core
    spoke_selector: $rp
  # Core full mesh
  - type: mesh_nodes
    selector: $core
    mesh_type: full
  # Distribution connects to core
  - type: mesh_nodes
    selector: $core_and_dist
    mesh_type: hub_and_spoke
    hub_selector: $core
    spoke_selector: $distribution
  # Access connects to distribution
  - type: mesh_nodes
    selector: $dist_and_access
    mesh_type: hub_and_spoke
    hub_selector: $distribution
    spoke_selector: $access

- name: addressing
  requires:
  - topology
  primitives:
  - type: provision_ips
    selector: $core_links
    pool: '10.10.0.0/24'
    subnet_size: 31
    strategy: dense
  - type: provision_ips
    selector: $dist_links
    pool: '10.10.1.0/24'
    subnet_size: 30
    strategy: dense
  - type: provision_ips
    selector: $access_links
    pool: '10.10.2.0/24'
    subnet_size: 30
    strategy: dense
  - type: allocate_resources
    selector: $all_routers
    resource_type: router_id
    pool: router-id-pool
    strategy: dense

- name: underlay
  requires:
  - addressing
  primitives:
  - type: build_protocol_layer
    selector: $all_routers
    layer: ospf
    config:
      area: '0.0.0.0'
      network_type: point_to_point
    clone_underlying: true
  - type: build_protocol_layer
    selector: $all_routers
    layer: bfd
    config:
      min_tx_ms: 200
      min_rx_ms: 200
      detect_mult: 3

- name: multicast
  requires:
  - underlay
  primitives:
  # PIM-SM on all routers — RP address is rp1's loopback
  - type: build_protocol_layer
    selector: $all_routers
    layer: pim_sm
    config:
      mode: sparse
      rp_address: "10.255.0.1"
      hello_interval_s: 30
      join_prune_interval_s: 60
      spt_threshold_kbps: 0
  # BSR candidacy on RP node
  - type: build_protocol_layer
    selector: $rp
    layer: pim_sm
    config:
      use_bsr: true
      bsr_candidate: true
      bsr_priority: 200
      rp_candidate: true
  # IGMP on access layer for host-facing interfaces
  - type: build_protocol_layer
    selector: $access
    layer: igmp
    config:
      version: 3
      snooping: true
      querier: true
      query_interval_s: 125
      fast_leave: false
  # IGMP snooping only on distribution (no querier)
  - type: build_protocol_layer
    selector: $distribution
    layer: igmp
    config:
      version: 3
      snooping: true
      querier: false

- name: resilience
  requires:
  - multicast
  primitives:
  # MLAG on distribution pairs for dual-homed access switches
  - type: build_protocol_layer
    selector: $distribution
    layer: mlag
    config:
      domain_id: 1
      dual_primary_detection: true
      peer_gateway: true
      reload_delay_s: 300
  - type: build_protocol_layer
    selector: $all_routers
    layer: lldp
    config:
      tx_interval_s: 30
      hold_multiplier: 4

- name: telemetry
  requires:
  - resilience
  primitives:
  # NetFlow/IPFIX on core for multicast traffic accounting
  - type: build_protocol_layer
    selector: $core
    layer: netflow
    config:
      format: ipfix
      collectors: ["10.99.0.30"]
      collector_port: 4739
      sampling_rate: 1000
      active_timeout_s: 60

assertions:
- name: rp-reachable-from-access
  severity: error
  select: $access
  check:
    type: reachability
    target_selector: $rp
  help: Access router cannot reach RP — multicast joins will fail.

- name: network-connected
  severity: error
  select: $all_routers
  check:
    type: is_connected
  help: Network is partitioned — a router is isolated.

- name: access-dual-homed
  severity: error
  select: $access
  check:
    type: min_edges
    count: 2
  help: Access router has fewer than 2 uplinks — no multicast redundancy.

- name: every-router-has-rid
  severity: error
  select: $all_routers
  check:
    type: field_exists
    field: router_id
  help: Router is missing its router-id.

- name: dist-to-access-bipartite
  severity: error
  select: $dist_and_access
  check:
    type: is_bipartite
  help: Distribution-to-access graph is not bipartite.

rules: {}

groups:
  rp: nodes[role=='rp']
  core: nodes[role=='core']
  distribution: nodes[role=='distribution']
  access: nodes[role=='access']
  rp_and_core: $rp | $core
  core_and_dist: $core | $distribution
  dist_and_access: $distribution | $access
  all_routers: $rp | $core | $distribution | $access
  core_links: edges[tier=='core']
  dist_links: edges[tier=='distribution']
  access_links: edges[tier=='access']

blast_radius:
- name: multicast-change-cap
  select: null
  check:
    type: max_percentage_changed
    value: 20.0

transforms: []
hardware_library:
  chassis: []
  linecards: []

```

### 09_zerotrust_dc.yaml

```yaml
# Case Study 09 — Zero-Trust DC Microsegmentation
#
# Models a security-first datacentre design with zone-based firewall
# policies enforcing strict east-west traffic control between application
# tiers, NAT for external access, and MACsec on all inter-switch links.
#
# Topology:
#   2 Firewall nodes  — central policy enforcement point
#   2 Web servers     — DMZ tier, internet-facing
#   2 App servers     — application tier, internal APIs
#   2 DB servers      — data tier, strictly isolated
#
# Design choices:
#   - Zone-based firewall: web→app (TCP 8080), app→db (TCP 5432), mgmt→all (SSH)
#   - Default deny between all zones (explicit permit only)
#   - DNAT for inbound HTTPS to web tier
#   - SNAT for outbound internet access from app tier
#   - MACsec on all links for Layer 2 encryption
#   - SNMP + syslog + NTP for monitoring baseline
#   - NetFlow on firewalls for traffic visibility
#   - Strict blast radius: max 1 deletion, max  change
#
# Address plan:
#   Web tier:    10.10.1.0/24
#   App tier:    10.10.2.0/24
#   DB tier:     10.10.3.0/24
#   Management:  10.99.0.0/24
#   External:    203.0.113.0/24

version: 1
imports: []
layers:
- name: topology
  requires: []
  primitives:
  # Each tier connects through the firewall pair
  - type: mesh_nodes
    selector: $fw_and_web
    mesh_type: hub_and_spoke
    hub_selector: $firewalls
    spoke_selector: $web
  - type: mesh_nodes
    selector: $fw_and_app
    mesh_type: hub_and_spoke
    hub_selector: $firewalls
    spoke_selector: $app
  - type: mesh_nodes
    selector: $fw_and_db
    mesh_type: hub_and_spoke
    hub_selector: $firewalls
    spoke_selector: $db
  # Firewall pair interconnect
  - type: mesh_nodes
    selector: $firewalls
    mesh_type: full

- name: addressing
  requires:
  - topology
  primitives:
  - type: provision_ips
    selector: $web_links
    pool: '10.10.1.0/24'
    subnet_size: 30
    strategy: dense
  - type: provision_ips
    selector: $app_links
    pool: '10.10.2.0/24'
    subnet_size: 30
    strategy: dense
  - type: provision_ips
    selector: $db_links
    pool: '10.10.3.0/24'
    subnet_size: 30
    strategy: dense

- name: encryption
  requires:
  - addressing
  primitives:
  # MACsec on all inter-switch links
  - type: build_protocol_layer
    selector: $all_nodes
    layer: macsec
    config:
      cipher: gcm_aes_256
      confidentiality: must-encrypt
      include_sci: true
      replay_protection: true

- name: zone_policy
  requires:
  - encryption
  primitives:
  # Web → App: only HTTP API traffic
  - build_zone_policy:
      name: "web-to-app"
      select:
        role: firewall
      from_zone: web
      to_zone: app
      default_action: deny
      rules:
        - name: allow-api
          action: permit
          protocol: tcp
          destination_port: 8080
          source_prefixes: ["10.10.1.0/24"]
          destination_prefixes: ["10.10.2.0/24"]
          stateful: true
          log: true
        - name: allow-health-check
          action: permit
          protocol: tcp
          destination_port: 8081
          source_prefixes: ["10.10.1.0/24"]
          destination_prefixes: ["10.10.2.0/24"]
          stateful: true
          log: false

  # App → DB: only database traffic
  - build_zone_policy:
      name: "app-to-db"
      select:
        role: firewall
      from_zone: app
      to_zone: db
      default_action: deny
      rules:
        - name: allow-postgres
          action: permit
          protocol: tcp
          destination_port: 5432
          source_prefixes: ["10.10.2.0/24"]
          destination_prefixes: ["10.10.3.0/24"]
          stateful: true
          log: true
        - name: allow-redis
          action: permit
          protocol: tcp
          destination_port: 6379
          source_prefixes: ["10.10.2.0/24"]
          destination_prefixes: ["10.10.3.0/24"]
          stateful: true
          log: false

  # Management → All: SSH from NOC
  - build_zone_policy:
      name: "mgmt-to-all"
      select:
        role: firewall
      from_zone: management
      to_zone: web
      default_action: deny
      rules:
        - name: allow-ssh
          action: permit
          protocol: tcp
          destination_port: 22
          source_prefixes: ["10.99.0.0/24"]
          destination_prefixes: ["0.0.0.0/0"]
          stateful: true
          log: true
        - name: allow-icmp
          action: permit
          protocol: icmp
          stateful: false
          log: false

  # DB → anything: deny all (data tier never initiates)
  - build_zone_policy:
      name: "db-to-any"
      select:
        role: firewall
      from_zone: db
      to_zone: app
      default_action: deny
      rules: []

- name: nat
  requires:
  - zone_policy
  primitives:
  # DNAT: external HTTPS → web tier
  - build_nat_policy:
      name: "inbound-nat"
      select:
        role: firewall
      rules:
        - name: https-to-web
          nat_type: dnat
          external_address: "203.0.113.10"
          external_port: 443
          internal_address: "10.10.1.10"
          internal_port: 8443
          log: true

  # SNAT: app tier → internet via interface masquerade
  - build_nat_policy:
      name: "outbound-nat"
      select:
        role: firewall
      rules:
        - name: app-internet-snat
          nat_type: snat
          mode: interface
          source_prefixes: ["10.10.2.0/24"]
          from_zone: app
          to_zone: untrust
          log: false

- name: monitoring
  requires:
  - nat
  primitives:
  - type: build_protocol_layer
    selector: $all_nodes
    layer: syslog
    config:
      servers: ["10.99.0.20"]
      facility: local7
      severity: informational
  - type: build_protocol_layer
    selector: $all_nodes
    layer: ntp
    config:
      servers: ["10.99.0.10", "10.99.0.11"]
  - type: build_protocol_layer
    selector: $all_nodes
    layer: snmp
    config:
      version: "3"
      v3_security_level: authPriv
      trap_targets: ["10.99.0.30"]
  # NetFlow on firewalls for traffic analysis
  - type: build_protocol_layer
    selector: $firewalls
    layer: netflow
    config:
      format: ipfix
      collectors: ["10.99.0.40"]
      sampling_rate: 100

- name: secrets
  requires:
  - monitoring
  primitives:
  - type: inject_secrets
    selector: $all_nodes
    secrets:
      macsec_cak: ${MACSEC_CAK}
      macsec_ckn: ${MACSEC_CKN}
      snmp_auth_pass: ${SNMP_AUTH_PASS}
      snmp_priv_pass: ${SNMP_PRIV_PASS}

assertions:
- name: zone-policy-web-to-app
  severity: error
  select: $firewalls
  check:
    type: zone_policy_exists
    from_zone: web
    to_zone: app
  help: Missing zone policy from web to app — east-west traffic is uncontrolled.

- name: zone-policy-app-to-db
  severity: error
  select: $firewalls
  check:
    type: zone_policy_exists
    from_zone: app
    to_zone: db
  help: Missing zone policy from app to db — database access is uncontrolled.

- name: web-reachable-from-fw
  severity: error
  select: $web
  check:
    type: reachability
    target_selector: $firewalls
  help: Web server cannot reach firewall — check topology wiring.

- name: db-isolated-from-web
  severity: warning
  select: $db
  check:
    type: use_rule
    name: no-direct-web-link
  help: DB server has a direct link to web tier — violates zero-trust model.

- name: all-links-encrypted
  severity: error
  select: $all_nodes
  check:
    type: use_rule
    name: macsec-enabled
  help: A node is missing MACsec — all links must be encrypted in zero-trust.

rules:
  no-direct-web-link: "!has(node.direct_web_link) or node.direct_web_link == false"
  macsec-enabled: has(node.macsec_config) and node.macsec_config != ''

groups:
  firewalls: nodes[role=='firewall']
  web: nodes[role=='web']
  app: nodes[role=='app']
  db: nodes[role=='db']
  fw_and_web: $firewalls | $web
  fw_and_app: $firewalls | $app
  fw_and_db: $firewalls | $db
  all_nodes: $firewalls | $web | $app | $db
  web_links: edges[zone=='web']
  app_links: edges[zone=='app']
  db_links: edges[zone=='db']

blast_radius:
- name: strict-deletion-limit
  select: null
  check:
    type: max_deletions
    count: 1
- name: strict-change-cap
  select: null
  check:
    type: max_percentage_changed
    value: 10.0

transforms: []
hardware_library:
  chassis: []
  linecards: []

```

### 10_financial_compliance.yaml

```yaml
# Case Study 10 — Compliance-Hardened Financial Network
#
# Models a PCI-DSS / SOX-compliant financial trading network with strict
# access controls, encrypted management plane, comprehensive auditing,
# and MACsec on all inter-switch links.
#
# Topology:
#   2 Core routers     — OSPF backbone, route reflectors
#   1 DMZ router       — internet-facing, heavily filtered
#   2 Trading switches — low-latency trading floor, MACsec encrypted
#   1 Management node  — out-of-band management, TACACS+ / RADIUS
#
# Design choices:
#   - OSPF backbone with BGP safety filters on DMZ (bogon + RFC1918 block)
#   - MACsec (AES-256-GCM) on trading links for wire-speed encryption
#   - TACACS+ for all admin access with command authorisation + accounting
#   - RADIUS for 802.1X on trading floor ports
#   - NTP with authentication (compliance requirement)
#   - Syslog over TLS to centralised SIEM
#   - SNMP v3 with authPriv (no v2c permitted)
#   - NetFlow/IPFIX for PCI-DSS audit trail
#   - Strict schema assertions: hostname, serial, firmware, site required
#   - Zone policy: DMZ → trading denied; management → all permitted (SSH only)
#   - Blast radius: max 1 deletion, max  change (change-averse environment)
#
# Address plan:
#   Core:        10.1.0.0/24
#   DMZ:         10.2.0.0/24
#   Trading:     10.3.0.0/24
#   Management:  10.99.0.0/24
#   External:    203.0.113.0/28

version: 1
imports: []
layers:
- name: topology
  requires: []
  primitives:
  # Core full mesh
  - type: mesh_nodes
    selector: $core
    mesh_type: full
  # DMZ connects to core
  - type: mesh_nodes
    selector: $core_and_dmz
    mesh_type: hub_and_spoke
    hub_selector: $core
    spoke_selector: $dmz
  # Trading connects to core
  - type: mesh_nodes
    selector: $core_and_trading
    mesh_type: hub_and_spoke
    hub_selector: $core
    spoke_selector: $trading
  # Management connects to core (out-of-band path)
  - type: mesh_nodes
    selector: $core_and_mgmt
    mesh_type: hub_and_spoke
    hub_selector: $core
    spoke_selector: $management

- name: addressing
  requires:
  - topology
  primitives:
  - type: provision_ips
    selector: $core_links
    pool: '10.1.0.0/24'
    subnet_size: 30
    strategy: dense
  - type: provision_ips
    selector: $dmz_links
    pool: '10.2.0.0/24'
    subnet_size: 30
    strategy: dense
  - type: provision_ips
    selector: $trading_links
    pool: '10.3.0.0/24'
    subnet_size: 30
    strategy: dense

- name: routing
  requires:
  - addressing
  primitives:
  - type: build_protocol_layer
    selector: $all_routers
    layer: ospf
    config:
      area: '0.0.0.0'
    clone_underlying: true
  - type: build_protocol_layer
    selector: $all_routers
    layer: bfd
    config:
      min_tx_ms: 100
      min_rx_ms: 100
      detect_mult: 3

- name: bgp_safety
  requires:
  - routing
  primitives:
  # BGP safety filters on DMZ router — block bogons and RFC1918
  - type: generate_safe_bgp_filters
    selector: $dmz
    prefix_list_name: BOGON-FILTER-V4
    policy_name: DMZ-INBOUND
    block_rfc1918: true
    permit_default: false

- name: encryption
  requires:
  - bgp_safety
  primitives:
  # MACsec on trading links — wire-speed L2 encryption
  - type: build_protocol_layer
    selector: $trading
    layer: macsec
    config:
      cipher: gcm_aes_256
      confidentiality: must-encrypt
      include_sci: true
      replay_protection: true
      replay_window: 64

- name: zone_security
  requires:
  - encryption
  primitives:
  # DMZ → Trading: deny all (PCI-DSS requirement)
  - build_zone_policy:
      name: "dmz-to-trading"
      select:
        role: core
      from_zone: dmz
      to_zone: trading
      default_action: deny
      rules: []

  # Management → All: SSH only
  - build_zone_policy:
      name: "mgmt-to-all"
      select:
        role: core
      from_zone: management
      to_zone: trading
      default_action: deny
      rules:
        - name: allow-ssh
          action: permit
          protocol: tcp
          destination_port: 22
          source_prefixes: ["10.99.0.0/24"]
          destination_prefixes: ["0.0.0.0/0"]
          stateful: true
          log: true
        - name: allow-icmp-diag
          action: permit
          protocol: icmp
          log: true

- name: aaa
  requires:
  - zone_security
  primitives:
  # TACACS+ for device admin — command auth + accounting
  - type: build_protocol_layer
    selector: $all_routers
    layer: tacacs
    config:
      servers: ["10.99.0.1", "10.99.0.2"]
      fallback_local: true
      authorization: true
      accounting: true
      single_connection: true
  # RADIUS for 802.1X on trading floor
  - type: build_protocol_layer
    selector: $trading
    layer: radius
    config:
      servers: ["10.99.0.50", "10.99.0.51"]
      use_accounting: true
  # 802.1X on trading floor ports
  - type: build_protocol_layer
    selector: $trading
    layer: dot1x
    config:
      mode: single
      reauth_period_s: 1800
      mac_bypass: false
      guest_vlan: null

- name: compliance_services
  requires:
  - aaa
  primitives:
  # NTP with authentication (PCI-DSS 10.4)
  - type: build_protocol_layer
    selector: $all_routers
    layer: ntp
    config:
      servers: ["10.99.0.10", "10.99.0.11"]
      authentication: true
      source_interface: loopback0
  # Syslog over TLS to SIEM (PCI-DSS 10.5)
  - type: build_protocol_layer
    selector: $all_routers
    layer: syslog
    config:
      servers: ["10.99.0.20"]
      facility: local7
      severity: informational
      transport: tcp
      use_tls: true
  # SNMP v3 only — no v2c permitted
  - type: build_protocol_layer
    selector: $all_routers
    layer: snmp
    config:
      version: "3"
      v3_auth_protocol: sha
      v3_priv_protocol: aes256
      v3_security_level: authPriv
      trap_targets: ["10.99.0.30"]
      source_interface: loopback0
  # NetFlow/IPFIX for audit trail (PCI-DSS 10.2)
  - type: build_protocol_layer
    selector: $core
    layer: netflow
    config:
      format: ipfix
      collectors: ["10.99.0.40"]
      collector_port: 4739
      sampling_rate: 1
      active_timeout_s: 60

- name: secrets
  requires:
  - compliance_services
  primitives:
  - type: inject_secrets
    selector: $all_routers
    secrets:
      tacacs_key: ${TACACS_KEY}
      radius_secret: ${RADIUS_SECRET}
      macsec_cak: ${MACSEC_CAK}
      macsec_ckn: ${MACSEC_CKN}
      ntp_auth_key: ${NTP_AUTH_KEY}
      snmp_auth_pass: ${SNMP_AUTH_PASS}
      snmp_priv_pass: ${SNMP_PRIV_PASS}

assertions:
# --- Topology assertions ---
- name: core-connected
  severity: error
  select: $all_routers
  check:
    type: is_connected
  help: Network is partitioned — a router is isolated.

- name: dmz-reaches-core
  severity: error
  select: $dmz
  check:
    type: reachability
    target_selector: $core
  help: DMZ cannot reach core routers.

- name: trading-reaches-core
  severity: error
  select: $trading
  check:
    type: reachability
    target_selector: $core
  help: Trading switches cannot reach core routers.

# --- Security assertions ---
- name: zone-policy-dmz-trading
  severity: error
  select: $core
  check:
    type: zone_policy_exists
    from_zone: dmz
    to_zone: trading
  help: Missing zone policy blocking DMZ→trading — PCI-DSS violation.

# --- Compliance assertions ---
- name: ntp-compliance
  severity: error
  select: $all_routers
  check:
    type: use_rule
    name: ntp-configured
  help: Router is missing NTP — PCI-DSS 10.4 requires synchronised clocks.

- name: syslog-compliance
  severity: error
  select: $all_routers
  check:
    type: use_rule
    name: syslog-configured
  help: Router is missing syslog — PCI-DSS 10.5 requires centralised logging.

- name: all-have-hostname
  severity: error
  select: $all_routers
  check:
    type: field_exists
    field: hostname
  help: A router is missing its hostname field.

- name: inventory-schema
  severity: error
  select: $all_routers
  check:
    type: match_schema
    schema:
      type: object
      required:
      - hostname
      - serial_number
      - firmware_version
      - site
      properties:
        hostname:
          type: string
          minLength: 1
        serial_number:
          type: string
          pattern: "^[A-Z0-9]{9,14}$"
        firmware_version:
          type: string
        site:
          type: string
          enum: [london-primary, london-dr, new-york]
  help: Router is missing required inventory fields — SOX audit trail requirement.

- name: hostnames-unique-per-site
  severity: error
  select: $all_routers
  check:
    type: unique_per_group
    field: hostname
    group_by: site
  help: Duplicate hostname within the same site.

rules:
  ntp-configured: has(node.ntp_servers) and size(node.ntp_servers) >= 2
  syslog-configured: has(node.syslog_server) and node.syslog_server != ''

groups:
  core: nodes[role=='core']
  dmz: nodes[role=='dmz']
  trading: nodes[role=='trading']
  management: nodes[role=='management']
  core_and_dmz: $core | $dmz
  core_and_trading: $core | $trading
  core_and_mgmt: $core | $management
  all_routers: $core | $dmz | $trading | $management
  core_links: edges[tier=='core']
  dmz_links: edges[tier=='dmz']
  trading_links: edges[tier=='trading']

blast_radius:
- name: strict-deletion-limit
  select: null
  check:
    type: max_deletions
    count: 1
- name: strict-change-cap
  select: null
  check:
    type: max_percentage_changed
    value: 5.0

transforms:
- name: junos-interface-rewrite
  when: device_os == 'junos'
  rules:
  - match_expr: stanza.kind == 'interface'
    apply:
      name: "'xe-0/0/' + string(stanza.fields.abstract_index)"

hardware_library:
  chassis: []
  linecards: []

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

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust |

---

## What This Is

Deterministic, auditable, CI/CD-friendly Rust CLI for compiling declarative YAML network blueprints into vendor-neutral configuration artifacts. The `netcfg` binary orchestrates: blueprint parsing → topology transformation → DeviceIR generation → template rendering → traceable config file emission.

---

## Current Milestone: v3.0 Policy Verification, QoS & IPv6

**Goal:** Complete the security policy verification engine, add interface-level zone membership, introduce a full QoS policy DSL (classification, marking, queuing, policing, shaping), and add IPv6 support (NAT64, NPTv6, IPv6 IPAM pool provisioning).

**Target features:**
- `SecurityModel` IR as the stable contract between DSL and renderers
- Interface-level zone membership (zones assigned per-interface, not per-device)
- Policy verification assertions: `no_shadowed_rules`, `zone_pairs_covered`, `zone_policy_denies/permits`
- Full QoS policy DSL: `build_qos_policy` with traffic classes, DSCP/CoS marking, queuing/scheduling, policing, and shaping
- QoS vendor templates across all 7 vendors
- IPv6 IPAM pool provisioning (`provision_ips` with IPv6 prefixes)
- NAT64 (stateful IPv6-to-IPv4 translation) in `build_nat_policy`
- NPTv6 (Network Prefix Translation for IPv6) in `build_nat_policy`

---

## Previous State (v2.2 shipped 2026-03-09)

The compiler delivers a complete security policy DSL with full vendor rendering:
- **Protocol Library:** 16 importable YAML fragments with all 7 vendor templates rendering new stanza kinds
- **Named Groups & Security Zones:** `groups:` section with `$group_name` expansion, `tag_nodes`, typed group variants (`kind: security_zone`), zone auto-tagging across all executor paths
- **Zone Policy DSL:** `objects:` section for reusable address/service objects, `build_zone_policy` with permit/deny rules, implicit deny-all, stateful inspection; rendered across all 7 vendors
- **NAT Policy:** `build_nat_policy` with SNAT (interface/pool) and DNAT (port-forward), rendered across all 7 vendors
- **Policy Assertions:** `ZoneMembership` and `ZonePolicyExists` check types
- **~22,000 LOC Rust** across netcfg-core and netcfg crates

---

## Core Value

Single-binary network compiler: design, transform, and generate configs from YAML blueprints without Python.

---

## Requirements



---

## # Active (v3.0)

- `SecurityModel` IR as stable renderer contract
- Interface-level zone membership
- Policy verification assertions (`no_shadowed_rules`, `zone_pairs_covered`, `zone_policy_denies/permits`)
- Full QoS policy DSL (`build_qos_policy`) with vendor templates for all 7 vendors
- IPv6 IPAM pool provisioning (`provision_ips` with IPv6 prefixes)
- NAT64 and NPTv6 in `build_nat_policy`

---

## # Validated (v2.2)

- ✓ Vendor template rendering for `zone_policy_rule` and `nat_rule` stanzas — v2.2
- ✓ `apply_zone_tags()` in all CLI direct-shadow paths — v2.2
- ✓ Stateful inspection for zone policy — v2.2

---

## # Deferred

- Interface name derivation in `mesh_nodes` (MESH-V2-02)
- LSP server (`nte-lsp`) integration (LSP-01)
- GUI/web editor for group and zone declarations
- Formal zone policy verification via Batfish integration

---

## # Validated (v1.0 - v2.1)

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
- ✓ Protocol fragment library (16 protocols) — v2.1
- ✓ NetcfgDSL LaTeX syntax highlighting — v2.1
- ✓ Named groups with `$group_name` expansion — v2.1
- ✓ `tag_nodes` primitive — v2.1
- ✓ Security zones (`kind: security_zone`) — v2.1
- ✓ `build_zone_policy` with objects and permit/deny — v2.1
- ✓ `build_nat_policy` with SNAT/DNAT — v2.1
- ✓ Zone membership and policy existence assertions — v2.1

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| `Topology::from_core()` wrapper bridges `CoreTopology` into Evaluator | Evaluator tightly coupled to Python-wrapper type; wrapping at phase boundary is cleanest | ✓ Good |
| `NamedTempFile::new_in(parent)` for transactional output | Same-filesystem guarantee enables atomic POSIX rename | ✓ Good |
| Clap 4 `Args` wrapper struct (`ConfigCommand`) containing `Subcommand` enum | Matches Clap 4 nested subcommand pattern, consistent with `BlueprintCommand` | ✓ Good |
| `RenderEngine::render_node` per-node API | Clean separation between transformation and configuration generation | ✓ Good |
| `miette` for diagnostic reporting | Provides out-of-the-box snippet and span highlighting for YAML errors | ✓ Good |
| Groups as first-class Blueprint section | Zone declarations are group variants — no separate primitive required | ✓ Good |
| GroupSpec untagged enum | Selector(String) shorthand + Full{} for backward compat | ✓ Good |
| Zone auto-tagging before primitives | Metadata stamped in runner before primitive loop — primitives query via selectors | ✓ Good |
| NAT separate from zone policy | Distinct stanza kinds mirror vendor evaluation order (NAT → security policy) | ✓ Good |
| Objects section for reuse | Named address/service objects resolved to concrete values before stanza emission | ✓ Good |
| Protocol library YAML-only | No Rust changes needed — `build_protocol_layer` is already protocol-agnostic | ✓ Good |

---

## Constraints

- Rust stable only — no nightly features
- British English in all documentation
- GSD workflow for phase-based planning

*Last updated: 2026-03-09 — v3.0 milestone started*
