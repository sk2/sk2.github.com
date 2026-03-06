---
layout: default
section: network-automation
---

# Network Configuration Framework

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

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

## Code Samples

### 01_isp_dual_stack_peering.yaml

```yaml
# examples/case_studies/01_isp_dual_stack_peering.yaml
#
# ── ISP Dual-Stack Peering PoP ──────────────────────────────────────────
#
# Story: An ISP is commissioning a new Frankfurt PoP. Three border
#   routers (fra-br1..br3) peer with two transit providers (the "hubs")
#   and four customer-edge routers (the "spokes") over dual-stack
#   IPv4 + IPv6 sessions.  BGP MD5 keys are injected from environment
#   variables, and RFC 1918 bogon filters are auto-generated.
#
# Primitives demonstrated:
#   global_pool, global_resource_pool, mesh_nodes (hub_and_spoke),
#   naming_strategy, provision_ips (IPv6 dual-stack), inject_secrets,
#   generate_safe_bgp_filters, build_protocol_layer, transforms + when
#
# Assertions demonstrated:
#   is_connected, reachability, is_bipartite, field_exists, field_in_cidr
#
# Blast radius:
#   max_deletions — prevent accidental mass teardown
# ─────────────────────────────────────────────────────────────────────────

version: 1

# ── Named global pools ──────────────────────────────────────────────────
# global_pool registers a named CIDR so that downstream provision_ips
# primitives can reference pools by name rather than hard-coding CIDRs.
# global_resource_pool does the same for non-IP resources (here: ASNs).

layers:
  - name: pools
    primitives:
      # IPv4 transit link addressing — /31 point-to-point links
      - type: global_pool
        name: fra-transit-v4
        pool: "198.51.100.0/24"

      # IPv6 transit link addressing — /127 point-to-point links
      - type: global_pool
        name: fra-transit-v6
        pool: "2001:db8:fra::/48"

      # Customer-edge link addressing
      - type: global_pool
        name: fra-ce-v4
        pool: "203.0.113.0/24"

      - type: global_pool
        name: fra-ce-v6
        pool: "2001:db8:ce::/48"

      # Private ASN pool for customer-edge sessions
      - type: global_resource_pool
        name: fra-private-asn
        resource_type: asn
        pool: "64512-64530"

  # ── Topology wiring ─────────────────────────────────────────────────
  # Hub-and-spoke mesh: border routers are hubs; transit providers and
  # customer-edge routers are spokes.  This produces one link per
  # (hub, spoke) pair — not a full mesh among spokes.

  - name: peering
    requires:
      - pools
    primitives:
      # Transit provider peering — border routers ↔ transit upstreams
      - type: mesh_nodes
        selector: "nodes[role='border' or role='transit']"
        mesh_type: hub_and_spoke
        hub_selector: "nodes[role='border']"
        spoke_selector: "nodes[role='transit']"
        naming_strategy: cisco_ge

      # Customer-edge peering — border routers ↔ CE routers
      - type: mesh_nodes
        selector: "nodes[role='border' or role='ce']"
        mesh_type: hub_and_spoke
        hub_selector: "nodes[role='border']"
        spoke_selector: "nodes[role='ce']"
        naming_strategy: cisco_ge

  # ── IP addressing (dual-stack) ──────────────────────────────────────
  # provision_ips with ipv6_pool + ipv6_subnet_size assigns both
  # address families to the same edge in one pass.

  - name: addressing
    requires:
      - peering
    primitives:
      # Transit links: /31 IPv4 + /127 IPv6
      - type: provision_ips
        selector: "edges[link_type='transit']"
        pool: fra-transit-v4
        subnet_size: 31
        ipv6_pool: fra-transit-v6
        ipv6_subnet_size: 127

      # Customer-edge links: /30 IPv4 + /126 IPv6
      - type: provision_ips
        selector: "edges[link_type='ce']"
        pool: fra-ce-v4
        subnet_size: 30
        ipv6_pool: fra-ce-v6
        ipv6_subnet_size: 126

      # Allocate private ASNs to customer-edge routers
      - type: allocate_resources
        selector: "nodes[role='ce']"
        resource_type: asn
        pool: fra-private-asn

  # ── Secrets injection ───────────────────────────────────────────────
  # inject_secrets reads values from environment variables at execution
  # time and writes them into node data_json.  Keys must NOT be
  # committed to version control.

  - name: secrets
    requires:
      - addressing
    primitives:
      - type: inject_secrets
        selector: "nodes[role='border']"
        secrets:
          bgp_md5_transit: "${BGP_MD5_TRANSIT_KEY}"
          bgp_md5_customer: "${BGP_MD5_CUSTOMER_KEY}"
          tacacs_key: "${TACACS_SECRET}"

  # ── BGP safety filters ─────────────────────────────────────────────
  # generate_safe_bgp_filters creates prefix lists and route policies
  # that block RFC 1918, documentation prefixes, and other bogons.

  - name: filters
    requires:
      - secrets
    primitives:
      - type: generate_safe_bgp_filters
        selector: "nodes[role='border']"
        prefix_list_name: BOGON-FILTER-V4
        policy_name: TRANSIT-INBOUND
        block_rfc1918: true
        permit_default: false

  # ── Protocol overlay ────────────────────────────────────────────────
  - name: bgp
    requires:
      - filters
    primitives:
      - type: build_protocol_layer
        selector: "nodes[role='border' or role='transit' or role='ce']"
        layer: bgp
        clone_underlying: true
        config:
          protocol_type: bgp
          asn_base: "65100"

# ── Transforms ────────────────────────────────────────────────────────
# The `when` predicate restricts a transform to nodes whose device_os
# matches.  Here we normalise Junos interface names and add an
# apply-group annotation for the transit peering sessions.

transforms:
  - name: junos-interface-rewrite
    when: "device_os == 'junos'"
    rules:
      - match_expr: "stanza.kind == 'interface'"
        apply:
          name: "'xe-0/0/' + string(stanza.fields.abstract_index)"

  - name: junos-transit-apply-group
    when: "device_os == 'junos'"
    rules:
      - match_expr: "stanza.kind == 'bgp_neighbor' and stanza.fields.description == 'transit'"
        apply:
          apply_groups: "'TRANSIT-DEFAULTS'"

# ── Assertions ────────────────────────────────────────────────────────
# Post-pipeline design-rule checks.

assertions:
  # All border routers must form a connected subgraph (no orphaned BR)
  - name: border-routers-connected
    severity: error
    select: "nodes[role='border']"
    check:
      type: is_connected
    help: "A border router is isolated — check peering layer wiring."

  # Every CE must be reachable from at least one border router
  - name: ce-reachable-from-border
    severity: error
    select: "nodes[role='ce']"
    check:
      type: reachability
      target_selector: "nodes[role='border']"
    help: "A customer-edge router cannot reach any border router."

  # Transit peering is bipartite: border routers on one side,
  # transit providers on the other.  No transit↔transit links.
  - name: transit-peering-bipartite
    severity: error
    select: "nodes[role='border' or role='transit']"
    check:
      type: is_bipartite
    help: "Transit peering graph is not bipartite — unexpected link between same-role nodes."

  # Every addressed link must have a valid IPv4 address
  - name: links-have-ipv4
    severity: error
    select: "edges[true]"
    check:
      type: field_exists
      field: src_ip
    help: "An edge is missing its IPv4 source address — check provision_ips."

  # All transit-facing IPs must lie within the transit pool
  - name: transit-ips-in-range
    severity: warning
    select: "edges[link_type='transit']"
    check:
      type: field_in_cidr
      field: src_ip
      cidr: "198.51.100.0/24"
    help: "A transit link IP is outside the expected 198.51.100.0/24 range."

# ── Blast radius ──────────────────────────────────────────────────────
# Prevent destructive diffs: no more than 2 node deletions per plan
# across the entire topology.

blast_radius:
  - name: limit-teardown
    check:
      type: max_deletions
      count: 2

```

### 02_campus_compliance_audit.yaml

```yaml
# examples/case_studies/02_campus_compliance_audit.yaml
#
# ── Campus Network Compliance Audit ─────────────────────────────────────
#
# Story: A university campus runs quarterly compliance audits across
#   six buildings (eng, sci, lib, admin, med, arts).  Each building has
#   a distribution switch and 4-8 access switches.  This blueprint is
#   assertion-heavy — it validates the existing topology rather than
#   building new links.  A small conditional + custom_primitive block
#   provisions loopbacks and management ACLs for buildings that are
#   large enough.
#
# Primitives demonstrated:
#   custom_primitive, conditional, build_access_policy
#
# Assertions demonstrated:
#   rules + use_rule, match_schema, unique_per_group, is_acyclic,
#   min_edges, field_exists
#
# Blast radius:
#   max_percentage_changed — audit should not alter >  of the topology
# ─────────────────────────────────────────────────────────────────────────

version: 1

# ── Reusable design-rule macros ─────────────────────────────────────────
# The `rules` map defines named CEL expressions.  Assertions reference
# them via `use_rule`, keeping large expressions DRY and readable.
# Each rule receives the matched node's data_json fields in scope.

rules:
  ntp-configured: "has(node.ntp_servers) and size(node.ntp_servers) >= 2"
  syslog-configured: "has(node.syslog_server) and node.syslog_server != ''"
  management-vlan-correct: "has(node.mgmt_vlan) and node.mgmt_vlan == 99"

layers:
  # ── Conditional loopback provisioning ───────────────────────────────
  # Only allocate loopback addresses if the topology has at least three
  # nodes — small test topologies should skip this step.

  - name: provisioning
    primitives:
      - type: conditional
        condition: "topology.node_count >= 3"
        then_primitives:
          # custom_primitive wraps a reusable per-building provisioning
          # block.  Parameters are passed to child primitives via the
          # params.* interpolation syntax in selectors.
          - type: custom_primitive
            name: building-loopbacks
            parameters:
              pool_cidr: "10.250.0.0/16"
            primitives:
              - type: provision_ips
                selector: "nodes[role='distribution' or role='access']"
                pool: "{{params.pool_cidr}}"
                subnet_size: 32

  # ── Management-plane access policy ──────────────────────────────────
  # build_access_policy generates ACL stanzas on distribution switches
  # to restrict management access to the campus NOC subnet.

  - name: management
    requires:
      - provisioning
    primitives:
      - type: build_access_policy
        selector: "nodes[role='distribution']"
        policy_name: MGMT-ACCESS
        rules:
          - name: allow-noc-ssh
            action: permit
            source_prefix: "10.0.0.0/8"
            protocol: tcp
            destination_port: 22

          - name: allow-noc-https
            action: permit
            source_prefix: "10.0.0.0/8"
            protocol: tcp
            destination_port: 443

          - name: deny-all-mgmt
            action: deny

# ── Assertions (the heart of this audit) ──────────────────────────────

assertions:
  # ── Rule-based checks (use_rule) ────────────────────────────────────
  # These three assertions reuse the named rules defined above.

  - name: ntp-compliance
    severity: error
    select: "nodes[role='distribution' or role='access']"
    check:
      type: use_rule
      name: ntp-configured
    help: "Node is missing NTP configuration — at least 2 NTP servers required."

  - name: syslog-compliance
    severity: error
    select: "nodes[role='distribution' or role='access']"
    check:
      type: use_rule
      name: syslog-configured
    help: "Node has no syslog server configured."

  - name: management-vlan-audit
    severity: warning
    select: "nodes[role='access']"
    check:
      type: use_rule
      name: management-vlan-correct
    help: "Access switch management VLAN should be 99."

  # ── Schema validation (match_schema) ────────────────────────────────
  # match_schema validates each node's data_json against a JSON Schema.
  # Here we enforce that every distribution switch carries the required
  # inventory fields (serial_number, firmware_version, site).

  - name: distribution-inventory-schema
    severity: error
    select: "nodes[role='distribution']"
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
            pattern: "^[A-Z0-9]{11}$"
          firmware_version:
            type: string
          site:
            type: string
            enum:
              - eng
              - sci
              - lib
              - admin
              - med
              - arts
    help: "Distribution switch is missing required inventory fields or has invalid data."

  # ── Uniqueness (unique_per_group) ───────────────────────────────────
  # Hostnames must be unique within each building.  Two switches in the
  # same building with the same hostname would cause SNMP/syslog confusion.

  - name: hostnames-unique-per-building
    severity: error
    select: "nodes[role='distribution' or role='access']"
    check:
      type: unique_per_group
      field: hostname
      group_by: site
    help: "Duplicate hostname detected within the same building."

  # ── Graph structure checks ──────────────────────────────────────────

  # iBGP sessions (if present) must be loop-free
  - name: ibgp-acyclic
    severity: error
    select: "nodes[protocol='ibgp']"
    check:
      type: is_acyclic
    help: "iBGP session graph contains a [cycle](../cycle) — check route-reflector hierarchy."

  # Every access switch must be dual-homed (at least 2 uplinks)
  - name: access-dual-homed
    severity: error
    select: "nodes[role='access']"
    check:
      type: min_edges
      count: 2
    help: "Access switch has fewer than 2 uplinks — single point of failure."

  # Every node must have a hostname
  - name: all-nodes-have-hostname
    severity: error
    select: "nodes[true]"
    check:
      type: field_exists
      field: hostname
    help: "A node is missing its hostname field."

# ── Blast radius ──────────────────────────────────────────────────────
# A compliance audit should not alter more than  of the topology.
# This guards against a misconfigured provisioning layer accidentally
# rewriting large swathes of the network.

blast_radius:
  - name: audit-change-cap
    check:
      type: max_percentage_changed
      value: 10.0

```

### 03_wan_migration.yaml

```yaml
# examples/case_studies/03_wan_migration.yaml
#
# ── WAN Protocol Migration: OSPF → IS-IS + Segment Routing ─────────────
#
# Story: A service provider is migrating its WAN backbone from
#   OSPF+BGP to IS-IS+SR.  The cutover is phased city-by-city
#   (london, paris, frankfurt) with strict blast-radius limits.
#   Region-scoped secrets protect IS-IS authentication keys, and a
#   conditional guard ensures the pilot phase runs only on small
#   topologies before the full rollout.
#
# Primitives demonstrated:
#   global_resource_pool, inject_secrets (region-scoped),
#   conditional, generate_safe_bgp_filters, build_routing_policy,
#   build_protocol_layer, transforms + when
#
# Assertions demonstrated:
#   reachability, field_exists
#
# Blast radius:
#   max_modifications — limit concurrent PE changes during migration
# ─────────────────────────────────────────────────────────────────────────

version: 1

layers:
  # ── Resource pools ──────────────────────────────────────────────────
  # IS-IS NET addresses are allocated from a global pool.  Each PE
  # receives a unique system ID (49.0001.xxxx.xxxx.xxxx.00 format).

  - name: pools
    primitives:
      - type: global_resource_pool
        name: isis-net-pool
        resource_type: isis_net
        pool: "49.0001.0000.0000.0001-49.0001.0000.0000.0200"

      - type: global_resource_pool
        name: sr-sid-pool
        resource_type: segment_id
        pool: "16001-16200"

  # ── Pilot-phase guard ──────────────────────────────────────────────
  # In the pilot phase (topology.node_count < 10), only London PEs are
  # migrated.  Once the topology grows past the pilot threshold, all
  # cities are included.  This prevents accidental full-rollout on a
  # staging environment with few nodes.

  - name: migration
    requires:
      - pools
    primitives:
      - type: conditional
        condition: "topology.node_count < 10"
        then_primitives:
          # Pilot: London only
          - type: allocate_resources
            selector: "nodes[city='london' and role='pe']"
            resource_type: isis_net
            pool: isis-net-pool

          - type: allocate_resources
            selector: "nodes[city='london' and role='pe']"
            resource_type: segment_id
            pool: sr-sid-pool
        else_primitives:
          # Full rollout: all cities
          - type: allocate_resources
            selector: "nodes[role='pe']"
            resource_type: isis_net
            pool: isis-net-pool

          - type: allocate_resources
            selector: "nodes[role='pe']"
            resource_type: segment_id
            pool: sr-sid-pool

  # ── Region-scoped secrets ───────────────────────────────────────────
  # Each region has its own IS-IS authentication key stored in a
  # different environment variable.  inject_secrets is called once per
  # region, scoped by the city selector.

  - name: secrets
    requires:
      - migration
    primitives:
      - type: inject_secrets
        selector: "nodes[city='london']"
        secrets:
          isis_auth_key: "${ISIS_KEY_LONDON}"
          tacacs_key: "${TACACS_KEY_EU}"

      - type: inject_secrets
        selector: "nodes[city='paris']"
        secrets:
          isis_auth_key: "${ISIS_KEY_PARIS}"
          tacacs_key: "${TACACS_KEY_EU}"

      - type: inject_secrets
        selector: "nodes[city='frankfurt']"
        secrets:
          isis_auth_key: "${ISIS_KEY_FRANKFURT}"
          tacacs_key: "${TACACS_KEY_EU}"

  # ── BGP safety filters ─────────────────────────────────────────────
  # Remaining eBGP sessions (inter-AS peering) keep RFC 1918 filtering.
  # This is applied to border routers that still run eBGP alongside
  # the new IS-IS underlay.

  - name: filters
    requires:
      - secrets
    primitives:
      - type: generate_safe_bgp_filters
        selector: "nodes[role='border']"
        prefix_list_name: BOGON-INBOUND
        policy_name: EBGP-INBOUND-FILTER
        block_rfc1918: true
        permit_default: false

  # ── Migration routing policy ────────────────────────────────────────
  # build_routing_policy creates a route-map that prefers IS-IS routes
  # (lower local-pref for OSPF) during the transition window.

  - name: routing-policy
    requires:
      - filters
    primitives:
      - type: build_routing_policy
        selector: "nodes[role='pe']"
        policy_name: MIGRATION-PREFER-ISIS
        statements:
          - name: prefer-isis-routes
            action: permit
            match_community_list: ISIS-MIGRATED
            set_local_preference: 200

          - name: depref-ospf-routes
            action: permit
            match_community_list: OSPF-LEGACY
            set_local_preference: 80

          - name: default-permit
            action: permit

  # ── IS-IS protocol overlay ─────────────────────────────────────────
  - name: isis-overlay
    requires:
      - routing-policy
    primitives:
      - type: build_protocol_layer
        selector: "nodes[role='pe' or role='p']"
        layer: isis
        clone_underlying: true
        config:
          protocol_type: isis
          level: "level-2"

# ── Transforms ────────────────────────────────────────────────────────
# IOS-XR uses long-form interface names (e.g. GigabitEthernet0/0/0/0).
# The transform rewrites abstract interface indices for XR devices
# and annotates stanzas with SR-specific fields.

transforms:
  - name: iosxr-interface-rewrite
    when: "device_os == 'iosxr'"
    rules:
      - match_expr: "stanza.kind == 'interface'"
        apply:
          name: "'GigabitEthernet0/0/0/' + string(stanza.fields.abstract_index)"

  - name: iosxr-sr-annotation
    when: "device_os == 'iosxr'"
    rules:
      - match_expr: "stanza.kind == 'isis_neighbor'"
        apply:
          sr_enabled: "true"
          metric: "10"

# ── Assertions ────────────────────────────────────────────────────────

assertions:
  # After migration, every PE must reach at least one P router via
  # the IS-IS overlay.
  - name: pe-reaches-p-via-isis
    severity: error
    select: "nodes[role='pe']"
    check:
      type: reachability
      target_selector: "nodes[role='p']"
    help: "A PE router cannot reach any P router — IS-IS adjacency may be down."

  # Every migrated PE must have an IS-IS NET address assigned
  - name: pe-has-isis-net
    severity: error
    select: "nodes[role='pe']"
    check:
      type: field_exists
      field: isis_net
    help: "PE is missing its IS-IS NET address — check allocate_resources."

  # Every migrated PE must have a segment routing SID
  - name: pe-has-sr-sid
    severity: error
    select: "nodes[role='pe']"
    check:
      type: field_exists
      field: segment_id
    help: "PE is missing its SR node SID — check allocate_resources."

  # Border routers must still be reachable (eBGP not broken)
  - name: border-reachable
    severity: error
    select: "nodes[role='border']"
    check:
      type: reachability
      target_selector: "nodes[role='pe']"
    help: "Border router is unreachable from PE — migration may have broken transit."

# ── Blast radius ──────────────────────────────────────────────────────
# During phased migration, limit modifications to 5 nodes per plan.
# This forces city-by-city rollout rather than one large change.

blast_radius:
  - name: migration-change-limit
    check:
      type: max_modifications
      count: 5

```

### 04_multi_tenant_dc.yaml

```yaml
# examples/case_studies/04_multi_tenant_dc.yaml
#
# ── Multi-Tenant Data Centre Fabric ─────────────────────────────────────
#
# Story: A financial services firm operates a multi-tenant DC fabric.
#   Three tenants — equities, fixed-income, and risk — each get their
#   own VRF with potentially overlapping address space.  The fabric
#   uses spine-leaf (hub-and-spoke) topology with strict inter-VRF
#   deny rules.
#
# Primitives demonstrated:
#   mesh_nodes (hub_and_spoke), naming_strategy, provision_ips (VRF-
#   scoped), build_access_policy, build_protocol_layer, transforms + when
#
# Assertions demonstrated:
#   rules + use_rule, match_schema, unique_per_group, is_connected
#
# Blast radius:
#   max_deletions (tenant VRF protection), max_percentage_changed
# ─────────────────────────────────────────────────────────────────────────

version: 1

# ── Reusable design-rule macros ─────────────────────────────────────────
# These rules validate that every leaf carries its tenant and VLAN
# configuration.  Referenced by assertions via use_rule.

rules:
  tenant-assigned: "has(node.tenant) and node.tenant != ''"
  vrf-configured: "has(node.vrf_name) and node.vrf_name != ''"
  leaf-has-vlan: "has(node.vlan_id) and node.vlan_id > 0 and node.vlan_id < 4095"

layers:
  # ── Fabric wiring ──────────────────────────────────────────────────
  # Spine-leaf topology: spines are hubs, leaves are spokes.
  # naming_strategy: cisco_ge produces GigabitEthernet0/0, 0/1, ...

  - name: fabric
    primitives:
      - type: mesh_nodes
        selector: "nodes[role='spine' or role='leaf']"
        mesh_type: hub_and_spoke
        hub_selector: "nodes[role='spine']"
        spoke_selector: "nodes[role='leaf']"
        naming_strategy: cisco_ge

  # ── VRF-scoped IP addressing ────────────────────────────────────────
  # Each tenant gets the same RFC 1918 pool (10.100.0.0/16) but in a
  # different VRF.  The `vrf` field on provision_ips scopes the
  # allocation so addresses can overlap across tenants without conflict.

  - name: addressing
    requires:
      - fabric
    primitives:
      # Equities tenant — VRF EQ
      - type: provision_ips
        selector: "edges[tenant='equities']"
        pool: "10.100.0.0/16"
        subnet_size: 30
        vrf: equities

      # Fixed-income tenant — VRF FI
      - type: provision_ips
        selector: "edges[tenant='fixed-income']"
        pool: "10.100.0.0/16"
        subnet_size: 30
        vrf: fixed-income

      # Risk tenant — VRF RISK
      - type: provision_ips
        selector: "edges[tenant='risk']"
        pool: "10.100.0.0/16"
        subnet_size: 30
        vrf: risk

      # Fabric underlay — no VRF (global table)
      - type: provision_ips
        selector: "edges[link_type='fabric']"
        pool: "172.16.0.0/16"
        subnet_size: 31

  # ── Inter-VRF deny rules ────────────────────────────────────────────
  # build_access_policy generates ACLs on every spine that explicitly
  # deny cross-tenant traffic.  Each rule targets a specific source
  # and destination VRF prefix range.

  - name: security
    requires:
      - addressing
    primitives:
      - type: build_access_policy
        selector: "nodes[role='spine']"
        policy_name: INTER-VRF-DENY
        rules:
          # Deny equities → fixed-income
          - name: deny-eq-to-fi
            action: deny
            source_prefix: "10.100.0.0/16"
            destination_prefix: "10.100.0.0/16"
            protocol: ip

          # Deny equities → risk
          - name: deny-eq-to-risk
            action: deny
            source_prefix: "10.100.0.0/16"
            destination_prefix: "10.100.0.0/16"
            protocol: ip

          # Permit intra-VRF (same VRF traffic is allowed)
          - name: permit-intra-vrf
            action: permit

  # ── BGP overlay per tenant ──────────────────────────────────────────
  - name: overlay
    requires:
      - security
    primitives:
      - type: build_protocol_layer
        selector: "nodes[role='spine' or role='leaf']"
        layer: bgp
        clone_underlying: true
        config:
          protocol_type: bgp
          asn_base: "65200"

# ── Transforms ────────────────────────────────────────────────────────
# NX-OS leaves need NX-OS specific interface naming and VRF context
# commands in their rendered configuration.

transforms:
  - name: nxos-interface-rewrite
    when: "device_os == 'nxos'"
    rules:
      - match_expr: "stanza.kind == 'interface'"
        apply:
          name: "'Ethernet1/' + string(stanza.fields.abstract_index + 1)"

  - name: nxos-vrf-context
    when: "device_os == 'nxos'"
    rules:
      - match_expr: "stanza.kind == 'bgp_neighbor' and has(stanza.fields.vrf)"
        apply:
          nxos_vrf_context: "stanza.fields.vrf"

# ── Assertions ────────────────────────────────────────────────────────

assertions:
  # ── Rule-based checks ───────────────────────────────────────────────
  - name: every-leaf-has-tenant
    severity: error
    select: "nodes[role='leaf']"
    check:
      type: use_rule
      name: tenant-assigned
    help: "Leaf switch is missing tenant assignment."

  - name: every-leaf-has-vrf
    severity: error
    select: "nodes[role='leaf']"
    check:
      type: use_rule
      name: vrf-configured
    help: "Leaf switch has no VRF configured."

  - name: every-leaf-has-vlan
    severity: warning
    select: "nodes[role='leaf']"
    check:
      type: use_rule
      name: leaf-has-vlan
    help: "Leaf switch is missing VLAN ID — check tenant provisioning."

  # ── Schema validation ──────────────────────────────────────────────
  # Every tenant leaf must carry structured tenant metadata.

  - name: tenant-metadata-schema
    severity: error
    select: "nodes[role='leaf']"
    check:
      type: match_schema
      schema:
        type: object
        required:
          - hostname
          - tenant
          - vrf_name
          - vlan_id
        properties:
          hostname:
            type: string
            minLength: 1
          tenant:
            type: string
            enum:
              - equities
              - fixed-income
              - risk
          vrf_name:
            type: string
          vlan_id:
            type: integer
            minimum: 1
            maximum: 4094
    help: "Leaf node data does not match expected tenant metadata schema."

  # ── Uniqueness ─────────────────────────────────────────────────────
  # VLAN IDs must be unique within each tenant.  Two leaves in the
  # same tenant VRF with the same VLAN would cause L2 loops.

  - name: vlans-unique-per-tenant
    severity: error
    select: "nodes[role='leaf']"
    check:
      type: unique_per_group
      field: vlan_id
      group_by: tenant
    help: "Duplicate VLAN ID detected within the same tenant."

  # ── Connectivity ───────────────────────────────────────────────────
  # Each tenant's subgraph (leaves + spines serving that tenant) must
  # be fully connected.  An isolated leaf means lost tenant traffic.

  - name: equities-connected
    severity: error
    select: "nodes[tenant='equities' or role='spine']"
    check:
      type: is_connected
    help: "Equities tenant subgraph is disconnected — a leaf is unreachable."

  - name: fixed-income-connected
    severity: error
    select: "nodes[tenant='fixed-income' or role='spine']"
    check:
      type: is_connected
    help: "Fixed-income tenant subgraph is disconnected — a leaf is unreachable."

  - name: risk-connected
    severity: error
    select: "nodes[tenant='risk' or role='spine']"
    check:
      type: is_connected
    help: "Risk tenant subgraph is disconnected — a leaf is unreachable."

# ── Blast radius ──────────────────────────────────────────────────────
# Tenant VRF protection: no more than 3 deletions (prevents accidental
# VRF teardown).  Global change cap: no more than  of the fabric
# altered in a single plan.

blast_radius:
  - name: tenant-vrf-protection
    check:
      type: max_deletions
      count: 3

  - name: fabric-change-cap
    check:
      type: max_percentage_changed
      value: 25.0

```

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

The pipeline runs in five phases:

1. **Parse** -- Read the blueprint YAML, resolve imports, validate structure.
2. **Transform** -- Execute primitives (`mesh_nodes`, `provision_ips`, `build_protocol_layer`) against the topology graph. Each primitive reads from and writes to node/edge data.
3. **Lower** -- Apply mapping rules that convert graph data into vendor-intermediate representation (DeviceIR). Selectors match nodes by role, site, or layer; stanzas declare the configuration kind (`interface`, `bgp_neighbor`, `prefix_list`).
4. **Render** -- MiniJinja templates consume DeviceIR stanzas and produce vendor-specific CLI syntax. Template selection is driven by `device_os` metadata.
5. **Emit** -- Write `.cfg` files per device, using atomic rename for transactional output.

Vendor abstraction lives in the lowering and rendering phases. The same blueprint produces Arista EOS, Cisco NX-OS, or Juniper Junos output by swapping the mapping rules and template set. The topology graph and primitive execution are vendor-agnostic.

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


## Technical Reports

- [Download Technical Report: netcfg-techreport.pdf](/assets/docs/ank-netcfg-netcfg-techreport.pdf)


---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)
