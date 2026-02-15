---
layout: default
section: network-automation
---

# Topology Modeling Library

<span class="status-badge status-active">v1.8 — Performance & Optimization</span>

[← Back to Network Automation](../network-automation)

---


## The Insight

Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. The **Topology Modeling Library** eliminates this trade-off by using Pydantic for schema validation and a high-performance Rust core (`petgraph`) for graph traversals.

## Quick Facts

| | |
|---|---|
| **Status** | v1.8 — Performance & Optimization |
| **Language** | N/A |
| **Started** | 2026 |

---

## What This Is

A Python library for modeling and querying network topologies with type-safe Pydantic models and a high-performance Rust core. Expressive Python API backed by blazing-fast graph algorithms, with automatic configuration generation for multi-vendor network deployments.

## Key Features

- **Two-Stage Transformation Model**: Whiteboard (sketch) → Plan (logical) → Protocol Layers (physical)
- **Type-Safe Models**: Pydantic validation ensures correct topology structure at design time
- **Lazy Query API**: Composable queries with Rust-backed execution (powered by `petgraph`)
- **Configuration Generation**: Automatic multi-vendor config generation (Cisco IOS/IOS-XR/NX-OS, Juniper JunOS, Arista EOS)
- **Batteries-Included Blueprints**: Pre-built domain models for ISIS, MPLS, EVPN, L3VPN, IXP
- **Rust Core (`ank_nte`)**: Graph operations run at native speed with Python FFI bindings

## Examples

### Service Provider Core: IS-IS + MPLS + iBGP

**Input Topology** (transitnet.yaml):

```yaml
topology:
  - metadata:
      name: TransitNet SP Core
      organisation: TransitNet
      asn: 65000

  - nodes:
      - P1:
          role: core
          data:
            pop: West
            platform: iosxr
            loopback: 10.0.0.1/32
          endpoints:
            - Gi0/0/0/0  # to P3
            - Gi0/0/0/1  # to P5
            - Gi0/0/0/2  # to PE1

      - P3:
          role: core
          data:
            pop: East
            platform: iosxr
            loopback: 10.0.0.3/32
          endpoints:
            - Gi0/0/0/0  # to P1
            - Gi0/0/0/2  # to PE3

      - PE1:
          role: pe
          data:
            pop: West
            platform: iosxr
            loopback: 10.0.0.11/32
          endpoints:
            - Gi0/0/0/0  # to P1

  - links:
      - [P1, Gi0/0/0/0, P3, Gi0/0/0/0]   # West-East core
      - [P1, Gi0/0/0/2, PE1, Gi0/0/0/0]  # Core-PE
```

**Build Protocol Layers:**

```python
from ank_pydantic import Topology
from ank_pydantic.blueprints.designs.isis import build_isis_layer
from ank_pydantic.blueprints.designs.mpls import build_mpls_layer

# ank_pydantic
topology = Topology.from_yaml("transitnet.yaml")

# ank_pydantic
isis_layer = build_isis_layer(
    topology,
    level=2,
    area="49.0001",
    parent_layer="physical"
)

# ank_pydantic
mpls_layer = build_mpls_layer(
    topology,
    igp_layer="isis",
    layer_name="mpls"
)
```

**Generated Configuration** (P1 - Cisco IOS-XR):

```cisco
hostname P1
!
interface Loopback0
 ipv4 address 10.0.0.1 255.255.255.255
!
interface GigabitEthernet0/0/0/0
 description to P3
 ipv4 address 10.1.0.1 255.255.255.252
!
interface GigabitEthernet0/0/0/2
 description to PE1
 ipv4 address 10.1.0.5 255.255.255.252
!
router isis CORE
 is-type level-2-only
 net 49.0001.0100.0000.0001.00
 address-family ipv4 unicast
  metric-style wide
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
 !
 interface GigabitEthernet0/0/0/0
  point-to-point
  address-family ipv4 unicast
   metric 10
  !
 !
 interface GigabitEthernet0/0/0/2
  point-to-point
  address-family ipv4 unicast
   metric 10
  !
 !
!
mpls ldp
 router-id 10.0.0.1
 interface GigabitEthernet0/0/0/0
 !
 interface GigabitEthernet0/0/0/2
 !
!
```

### L3VPN Configuration

**Input:** Add customer sites to PE routers:

```yaml
# ank_pydantic
- nodes:
    - CE1:
        role: ce
        data:
          organisation: NetCorp
          asn: 65100
          loopback: 192.168.1.1/32
        endpoints:
          - Gi0/0

    - CE2:
        role: ce
        data:
          organisation: NetCorp
          asn: 65100
          loopback: 192.168.2.1/32
        endpoints:
          - Gi0/0

- links:
    - [PE1, Gi0/0/0/1, CE1, Gi0/0]  # PE-CE link
    - [PE3, Gi0/0/0/1, CE2, Gi0/0]  # PE-CE link
```

**Build L3VPN Layer:**

```python
from ank_pydantic.blueprints.designs.l3vpn import build_l3vpn_layer

# ank_pydantic
l3vpn_layer = build_l3vpn_layer(
    topology,
    service_name="NetCorp-L3VPN",
    customer="NetCorp",
    customer_asn=65100,
    provider_asn=65000,
    vpn_id=100
)
```

**Generated VRF Configuration** (PE1):

```cisco
vrf NETCORP
 address-family ipv4 unicast
  import route-target
   65000:100
  !
  export route-target
   65000:100
  !
 !
!
interface GigabitEthernet0/0/0/1
 description to CE1 (NetCorp)
 vrf NETCORP
 ipv4 address 10.100.1.1 255.255.255.252
!
router bgp 65000
 vrf NETCORP
  rd 65000:100
  address-family ipv4 unicast
   redistribute connected
  !
  neighbor 10.100.1.2
   remote-as 65100
   description CE1
   address-family ipv4 unicast
    route-policy NETCORP-IN in
    route-policy NETCORP-OUT out
   !
  !
 !
!
```

### Containerlab Deployment

**Export to Containerlab:**

```python
from ank_pydantic.blueprints.environments import get_environment

# ank_pydantic
env = get_environment('containerlab')

# ank_pydantic
artifacts = env.generate(topology)

# ank_pydantic
with open("transitnet.clab.yml", "w") as f:
    f.write(artifacts.files['topology.clab.yml'])
```

**Generated Containerlab File** (transitnet.clab.yml):

```yaml
name: transitnet
mgmt:
  network: mgmt
  ipv4-subnet: 172.20.20.0/24

topology:
  nodes:
    P1:
      kind: cisco_xrv9k
      image: vrnetlab/vr-xrv9k:7.3.2
      mgmt-ipv4: 172.20.20.11
      binds:
        - ./configs/P1.cfg:/config/startup-config.cfg

    P3:
      kind: cisco_xrv9k
      image: vrnetlab/vr-xrv9k:7.3.2
      mgmt-ipv4: 172.20.20.13
      binds:
        - ./configs/P3.cfg:/config/startup-config.cfg

    PE1:
      kind: cisco_xrv9k
      image: vrnetlab/vr-xrv9k:7.3.2
      mgmt-ipv4: 172.20.20.21
      binds:
        - ./configs/PE1.cfg:/config/startup-config.cfg

  links:
    - endpoints: ["P1:Gi0/0/0/0", "P3:Gi0/0/0/0"]
    - endpoints: ["P1:Gi0/0/0/2", "PE1:Gi0/0/0/0"]
```

**Deploy and Verify:**

```bash
# ank_pydantic
sudo containerlab deploy -t transitnet.clab.yml

# ank_pydantic
sudo containerlab inspect -t transitnet.clab.yml

# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic

# ank_pydantic
docker exec -it clab-transitnet-P1 show isis neighbors

# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic

# ank_pydantic
docker exec -it clab-transitnet-P1 show mpls ldp neighbor

# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
# ank_pydantic
```

### Query API Usage

Composable queries with Rust-backed execution:

```python
# Filter by keyword attributes
core_routers = topology.query.nodes().where(
    role="core", pop="North"
).models()

# Count with attribute filters
inter_pop_links = topology.query.links().where(
    link_type="long-haul"
).count()

# Layer-scoped queries
mpls_devices = topology.layer("mpls").nodes().where(
    mpls_enabled=True
).ids()
```

### Integration with the Network Visualization Engine

Export for visualization:

```python
# ank_pydantic
topology.export_for_netvis(
    "output.json",
    layout="hierarchical",
    node_metadata=True
)
```

The Network Visualization Engine applies advanced layout algorithms to produce publication-quality diagrams.

---

## YAML Topology Format

Define topologies in YAML for rapid prototyping:

```yaml
topology:
  - metadata:
      name: TransitNet SP Core
      organisation: TransitNet
      asn: 65000

  - nodes:
      - P1:
          role: core
          data:
            pop: West
            platform: iosxr
            loopback: 10.0.0.1/32
          endpoints:
            - Gi0/0/0/0  # to P3
            - Gi0/0/0/1  # to P5

      - PE1:
          role: pe
          data:
            pop: West
            platform: iosxr
            loopback: 10.0.0.11/32
          endpoints:
            - Gi0/0/0/0  # to P1
            - Gi0/0/0/1  # customer-facing

  - links:
      - [P1, Gi0/0/0/0, P3, Gi0/0/0/0]   # West-East
      - [P1, Gi0/0/0/1, P5, Gi0/0/0/0]   # West-North
      - [P1, Gi0/0/0/2, PE1, Gi0/0/0/0]  # Core-PE
```

Load and process:

```python
topology = Topology.from_yaml("transitnet.yaml")

# ank_pydantic
isis_layer = build_isis_layer(topology, level=2, area="49.0001")
mpls_layer = build_mpls_layer(topology, igp_layer="isis")

# ank_pydantic
env = get_environment('containerlab')
artifacts = env.generate(topology)
```

---

## Available Blueprints

Pre-built design functions for common network patterns:

| Blueprint | Purpose | Key Features |
|-----------|---------|--------------|
| **IS-IS** | IGP routing | Multi-level (L1, L2, L1/L2), area assignment, NET generation |
| **MPLS/LDP** | Label switching | Follows IGP adjacencies, label range configuration, targeted LDP |
| **L3VPN** | VPN services | VRF configuration, RD/RT generation, PE-CE sessions |
| **EVPN** | L2/L3 overlay | VXLAN, MAC/IP routes, multi-tenancy |
| **IXP** | Peering fabric | Route server, bilateral peering, BGP communities |
| **Data Center** | Spine-leaf | CLOS topology, ECMP, BGP unnumbered |

Each blueprint provides:
- **Layer builder functions** for protocol derivation
- **Pydantic models** for type-safe configuration
- **Query helpers** for network analysis
- **Config templates** for multi-vendor export

---

## Milestones

**v1.0 API Polish** (Shipped Jan 24, 2026)
Standardized manager API and query API foundation.

**v1.1 Batteries-Included** (Shipped Jan 25, 2026)
Transform operations, IP allocation helpers, and query demos.

**v1.2 Foundations Extraction** (Shipped Jan 27, 2026)
Extracted domain models into blueprints module (ISIS, MPLS, EVPN, L3VPN, IXP).

**v1.3 Whiteboard-to-Blueprint** (Shipped Jan 31, 2026)
Two-stage transformation model and Rust-backed query engine.
- Whiteboard (sketch) → Plan (logical) → Protocol Layers pipeline
- Rust query execution via nte-query with QuerySpec DTO pattern

**v1.4 Native Foundation** (Shipped Feb 1, 2026)
Rust-first architecture with CoreTopology as single source of truth.

**v1.5 API Ergonomics** (Shipped Feb 3, 2026)
Query API completion — sorting, between queries, graph traversal, cascade delete.

**v1.6 Documentation & Adoption** (Shipped Feb 5, 2026)
MkDocs site with Diataxis structure, tested examples, and domain case studies.

**v1.7 API Usability & Ergonomics** (Shipped Feb 9, 2026)
Collision handling policies, safe defaults, round-trip I/O, and blueprint validation.

**v1.8 Performance & Optimization** (In Progress)
Query optimization and large-scale topology support (10k+ nodes).
- Profiling infrastructure with py-spy, cProfile, and cargo-flamegraph
- LadybugDB backend evaluation and backend abstraction layer
- LazyFrame executor with filter planning, materialized query cache (100-1000x speedup)
- Hierarchical analytics with cross-layer queries (planned)

**Roadmap:**

- **IP addressing** — Automated IP address allocation and management across topology layers
- **NSOT integration** — Workflow to import/export topology state with Network Source of Truth systems

## Tech Stack

Python (Pydantic), Rust core (`petgraph`-backed), PyO3 bindings

---

[← Back to Network Automation](../network-automation)
