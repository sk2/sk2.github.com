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
- [Download User Manual: netcfg-usermanual.pdf](/assets/docs/ank-netcfg-netcfg-usermanual.pdf)

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

### evpn-vxlan-fabric.yaml

```yaml
version: 1
imports:
- '../docs/library/datacenter-rules.yaml'
- '../docs/library/hardware-lowering.yaml'
layers:
- name: resources
  requires: []
  primitives:
  - type: map_hardware_inventory
    selector: $leaves
    chassis_model: dcs-7508
    slots:
      1: linecard-48port-10g
  - type: allocate_resources
    selector: $all_nodes
    resource_type: bgp_as
    pool: '65001-65001'
    strategy: dense
    pool_size: null
  - type: allocate_resources
    selector: $all_nodes
    resource_type: router_id
    pool: '10.255.0.1-10.255.0.255'
    strategy: dense
    pool_size: null
- name: underlay
  requires: []
  primitives:
  - type: provision_ips
    selector: edges[true]
    pool: '10.0.0.0/24'
    subnet_size: 31
    ipv6_pool: null
    ipv6_subnet_size: null
    strategy: dense
    pool_size: null
    vrf: null
  - type: build_protocol_layer
    selector: $all_nodes
    layer: ospf
    config:
      area: '0.0.0.0'
    clone_underlying: true
- name: control_plane
  requires: []
  primitives:
  - type: build_protocol_layer
    selector: $all_nodes
    layer: bgp
    config:
      peer_type: ibgp
      protocol_type: bgp
    clone_underlying: false
  - type: mesh_nodes
    selector: $bgp_nodes
    mesh_type: full
    hub_selector: null
    spoke_selector: null
    naming_strategy: null
- name: policies
  requires: []
  primitives:
  - type: build_prefix_list
    selector: $all_nodes
    prefix_list_name: PL-LOOPBACKS
    entries:
    - prefix: '10.255.0.0/24'
      action: permit
      le: 32
      ge: null
  - type: build_community_list
    selector: $all_nodes
    community_list_name: CL-EVPN
    entries:
    - community: '65001:1000'
      action: permit
  - type: build_routing_policy
    selector: $all_nodes
    policy_name: RP-UNDERLAY-EXPORT
    statements:
    - name: PERMIT-LOOPBACKS
      action: permit
      match_prefix_list: PL-LOOPBACKS
      match_community_list: null
      match_as_path: null
      set_local_preference: null
      set_metric: null
      set_as_path_prepend: null
      set_community: null
      next_hop: null
- name: overlays
  requires: []
  primitives:
  - type: build_vxlan
    selector: $leaves
    vni_base: 10000
    mcast_group_base: '239.1.1.1'
  - type: build_evpn
    selector: $leaves
    route_distinguisher_base: auto
    route_target_base: '65001:10000'
assertions:
- name: loopback-prefix-check
  severity: error
  select: $all_nodes
  check:
    type: field_in_cidr
    field: router_id
    cidr: '10.255.0.0/24'
  help: null
rules: {}
groups:
  spines: nodes[role=='spine']
  leaves: nodes[role=='leaf']
  all_nodes: nodes[true]
  bgp_nodes: nodes[layer=='bgp']
blast_radius: []
transforms: []
hardware_library:
  chassis: []
  linecards: []

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
version: 1
imports:
- '../protocols/ospfv3.yaml'
- '../protocols/bfd.yaml'
- '../protocols/vrrp.yaml'
layers:
- name: physical
  requires: []
  primitives:
  - type: mesh_nodes
    selector: $all_nodes
    mesh_type: full
    hub_selector: null
    spoke_selector: null
    naming_strategy: null
  - type: provision_ips
    selector: $all_links
    pool: '10.0.0.0/24'
    subnet_size: 30
    ipv6_pool: null
    ipv6_subnet_size: null
    strategy: dense
    pool_size: null
    vrf: null
assertions: []
rules: {}
groups:
  spines: nodes[role=='spine']
  all_links: edges[src>=0]
  all_nodes: nodes[true]
blast_radius: []
transforms: []
hardware_library:
  chassis: []
  linecards: []

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

## Core Value

Single-binary network compiler: design, transform, and generate configs from YAML blueprints without Python.

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
